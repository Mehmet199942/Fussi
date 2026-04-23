const express = require('express');
const cors = require('cors');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const { exec } = require('child_process');
require('dotenv').config();
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for regular JSON bodies
app.use(cors());

// Webhook endpoint needs raw body for signature verification
app.post('/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
    const sig = req.headers['stripe-signature'];
    let event;

    try {
        event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET);
    } catch (err) {
        console.error(`Webhook Error: ${err.message}`);
        return res.status(400).send(`Webhook Error: ${err.message}`);
    }

    // Handle the event
    if (event.type === 'checkout.session.completed') {
        const session = event.data.object;
        console.log('Order successful:', session.id);

        // Log order to data/orders.json
        const orderData = {
            id: session.id,
            customer_email: session.customer_details.email,
            amount_total: session.amount_total / 100,
            currency: session.currency,
            payment_status: session.payment_status,
            shipping_details: session.shipping_details,
            created_at: new Date().toISOString()
        };

        const ORDERS_PATH = path.join(__dirname, 'data', 'orders.json');
        let orders = [];
        if (fs.existsSync(ORDERS_PATH)) {
            orders = JSON.parse(fs.readFileSync(ORDERS_PATH, 'utf-8'));
        }
        orders.push(orderData);
        fs.writeFileSync(ORDERS_PATH, JSON.stringify(orders, null, 4));
        
        // Note: Confirmation email would be sent here (Stripe does it automatically if configured)
    }

    res.json({ received: true });
});

// Regular JSON parsing for other routes
app.use(express.json());
app.use(express.static(path.join(__dirname))); // Serve the entire project
app.use(express.static(path.join(__dirname, 'public'))); // Serve public assets

const DB_PATH = path.join(__dirname, 'data', 'database.json');

// --- Product Admin API (Reused from admin-server.js) ---
const readDB = () => {
    if (!fs.existsSync(DB_PATH)) return [];
    return JSON.parse(fs.readFileSync(DB_PATH, 'utf-8'));
};
const writeDB = (data) => fs.writeFileSync(DB_PATH, JSON.stringify(data, null, 4));

app.get('/api/products', (req, res) => {
    res.json(readDB());
});

app.post('/api/create-checkout-session', async (req, res) => {
    try {
        const { cart, email } = req.body;

        if (!cart || cart.length === 0) {
            return res.status(400).json({ error: 'Cart is empty' });
        }

        const line_items = cart.map(item => {
            const p = item.product;
            // Ensure price is in cents
            const unitAmount = Math.round((p.discountedPrice || p.price) * 100);
            
            return {
                price_data: {
                    currency: 'eur',
                    product_data: {
                        name: p.name,
                        images: [p.image.startsWith('http') ? p.image : `${process.env.YOUR_DOMAIN || req.protocol + '://' + req.get('host')}/${p.image}`],
                    },
                    unit_amount: unitAmount,
                    tax_behavior: 'inclusive',
                },
                quantity: item.qty,
            };
        });

        const session = await stripe.checkout.sessions.create({
            payment_method_types: ['card', 'klarna', 'sepa_debit'], // Add sepa/klarna
            line_items: line_items,
            mode: 'payment',
            customer_email: email,
            success_url: `${process.env.YOUR_DOMAIN || req.protocol + '://' + req.get('host')}/success.html?session_id={CHECKOUT_SESSION_ID}`,
            cancel_url: `${process.env.YOUR_DOMAIN || req.protocol + '://' + req.get('host')}/cancel.html`,
            shipping_address_collection: {
                allowed_countries: ['DE', 'AT', 'CH'],
            },
            shipping_options: [
                {
                    shipping_rate_data: {
                        type: 'fixed_amount',
                        fixed_amount: { amount: 590, currency: 'eur' },
                        display_name: 'DHL Standard',
                        delivery_estimate: {
                            minimum: { unit: 'business_day', value: 3 },
                            maximum: { unit: 'business_day', value: 5 },
                        },
                    },
                },
                {
                    shipping_rate_data: {
                        type: 'fixed_amount',
                        fixed_amount: { amount: 790, currency: 'eur' },
                        display_name: 'UPS Express',
                        delivery_estimate: {
                            minimum: { unit: 'business_day', value: 1 },
                            maximum: { unit: 'business_day', value: 2 },
                        },
                    },
                },
            ],
            automatic_tax: { enabled: true },
            allow_promotion_codes: true,
        });

        res.json({ url: session.url });
    } catch (err) {
        console.error('Stripe Session Error:', err);
        res.status(500).json({ error: err.message });
    }
});

// Admin: Generate Shop Pages
app.post('/api/generate', (req, res) => {
    exec('python scripts/generate_shop.py', (error, stdout, stderr) => {
        if (error) return res.status(500).json({ error: error.message, output: stderr });
        res.json({ success: true, output: stdout });
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
