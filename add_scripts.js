const fs = require('fs');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let modified = false;

    // Some files like index.html already have it correctly.
    // If not, inject right before </body> or near other scripts

    if (!content.includes('src="data/products.js"')) {
        content = content.replace(/<\/body>/i, '\t<script src="data/products.js"></script>\n</body>');
        modified = true;
    }

    if (!content.includes('src="js/shop.js"')) {
        content = content.replace(/<\/body>/i, '\t<script src="js/shop.js"></script>\n</body>');
        modified = true;
    }

    if (modified) {
        fs.writeFileSync(file, content, 'utf8');
        console.log('Added missing scripts to ' + file);
    }
});
