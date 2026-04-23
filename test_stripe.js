const http = require('http');

const data = JSON.stringify({
    cart: [
        {
            product: {
                id: 'test-1',
                name: 'Test Produkt',
                price: 19.99,
                image: 'images/item-cart-01.jpg'
            },
            qty: 1
        }
    ],
    email: 'test@example.com'
});

const options = {
    hostname: 'localhost',
    port: 3000,
    path: '/api/create-checkout-session',
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Content-Length': data.length
    }
};

const req = http.request(options, (res) => {
    let responseBody = '';
    res.on('data', (chunk) => {
        responseBody += chunk;
    });
    res.on('end', () => {
        console.log('Status Code:', res.statusCode);
        console.log('Response:', responseBody);
    });
});

req.on('error', (error) => {
    console.error('Error:', error);
});

req.write(data);
req.end();
