const fs = require('fs');
const path = 'c:/Users/mehme/Desktop/cozastore-master/data/products.js';
let content = fs.readFileSync(path, 'utf8');

// Replace standard generated URLs
content = content.replace(/"url": "generated\/product-(.*?)\.html"/g, (match, id) => {
    return `"url": "product-detail.html?id=${id}"`;
});

// Also handle ones that don't have generated/ prefix if any
// (though based on my read they all had generated/)

fs.writeFileSync(path, content);
console.log('Successfully updated product URLs in products.js');
