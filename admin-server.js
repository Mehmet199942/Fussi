const express = require('express');
const cors = require('cors');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const { exec } = require('child_process');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname))); // Serve the entire project for preview

const DB_PATH = path.join(__dirname, 'data', 'database.json');
const ORDERS_PATH = path.join(__dirname, 'data', 'orders.json');

// Define storage for images
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        const nation = req.body.nation || 'general';
        const dir = path.join(__dirname, 'images', nation);
        if (!fs.existsSync(dir)){
            fs.mkdirSync(dir, { recursive: true });
        }
        cb(null, dir);
    },
    filename: function (req, file, cb) {
        // Prevent overwriting by appending timestamp if needed, or just use original name
        cb(null, file.originalname);
    }
});
const upload = multer({ storage: storage });

// Create database if not exists
if (!fs.existsSync(DB_PATH)) {
    fs.writeFileSync(DB_PATH, JSON.stringify([]));
}

// Helpers for Products
const readDB = () => JSON.parse(fs.readFileSync(DB_PATH, 'utf-8'));
const writeDB = (data) => fs.writeFileSync(DB_PATH, JSON.stringify(data, null, 4));

// Helpers for Orders
const readOrders = () => {
    if (!fs.existsSync(ORDERS_PATH)) return [];
    return JSON.parse(fs.readFileSync(ORDERS_PATH, 'utf-8'));
};
const writeOrders = (data) => fs.writeFileSync(ORDERS_PATH, JSON.stringify(data, null, 4));

// API: Get all products
app.get('/api/products', (req, res) => {
    try {
        const products = readDB();
        res.json(products);
    } catch (err) {
        res.status(500).json({ error: 'Failed to read database' });
    }
});

// API: Upload an image
app.post('/api/upload', upload.single('image'), (req, res) => {
    if (!req.file) {
        return res.status(400).json({ error: 'No file uploaded' });
    }
    const nation = req.body.nation || 'general';
    const imagePath = `images/${nation}/${req.file.filename}`;
    res.json({ imagePath });
});

// API: Bulk upload images
app.post('/api/bulk-upload', upload.array('images', 20), (req, res) => {
    if (!req.files || req.files.length === 0) {
        return res.status(400).json({ error: 'No files uploaded' });
    }
    const nation = req.body.nation || 'general';
    const fileInfos = req.files.map(file => ({
        originalName: file.originalname,
        imagePath: `images/${nation}/${file.filename}`
    }));
    res.json({ files: fileInfos });
});

// API: Add or Update a product
app.post('/api/products', (req, res) => {
    try {
        const newProduct = req.body;
        if (!newProduct.id) {
            return res.status(400).json({ error: 'Product ID is required' });
        }
        
        let products = readDB();
        const index = products.findIndex(p => p.id === newProduct.id);
        
        if (index >= 0) {
            products[index] = newProduct; // Update
        } else {
            products.push(newProduct); // Create
        }
        
        writeDB(products);
        res.json({ success: true, product: newProduct });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// API: Get all orders
app.get('/api/orders', (req, res) => {
    try {
        res.json(readOrders());
    } catch (err) {
        res.status(500).json({ error: 'Failed to read orders' });
    }
});

// API: Update order status
app.put('/api/orders/:id', (req, res) => {
    try {
        const { id } = req.params;
        const { status } = req.body;
        let orders = readOrders();
        const index = orders.findIndex(o => o.id === id);
        if (index >= 0) {
            orders[index].status = status;
            writeOrders(orders);
            res.json({ success: true, order: orders[index] });
        } else {
            res.status(404).json({ error: 'Order not found' });
        }
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// API: Delete a product
app.delete('/api/products/:id', (req, res) => {
    try {
        let products = readDB();
        products = products.filter(p => p.id !== req.params.id);
        writeDB(products);
        res.json({ success: true });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// API: Trigger Python Generator
app.post('/api/generate', (req, res) => {
    exec('python scripts/generate_shop.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return res.status(500).json({ error: error.message, output: stderr });
        }
        res.json({ success: true, output: stdout });
    });
});

app.listen(PORT, () => {
    console.log(`Admin Server is running on http://localhost:${PORT}`);
    console.log(`Open Dashboard at: http://localhost:${PORT}/admin/index.html`);
});
