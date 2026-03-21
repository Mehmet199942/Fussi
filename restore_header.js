const fs = require('fs');

const headerHtml = fs.readFileSync('components/header.html', 'utf8');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

let count = 0;
for (const file of files) {
    if (file === 'components/header.html') continue;

    let content = fs.readFileSync(file, 'utf8');
    let newContent = content;

    // Replace placeholder with header html
    newContent = newContent.replace(/<div id="header-placeholder"><\/div>/i, () => headerHtml);

    // Remove the load-header.js script tag
    newContent = newContent.replace(/<script src="js\/load-header\.js"><\/script>\n?/i, '');

    if (newContent !== content) {
        fs.writeFileSync(file, newContent, 'utf8');
        console.log(`Restored placeholder in ${file}`);
        count++;
    } else {
        // User script might have messed up index.html and nation.html
        // Check if header is completely gone and insert after body
        if (!newContent.includes('<header ') && !newContent.includes('<div id="header-placeholder"></div>')) {
            newContent = newContent.replace(/(<body[^>]*>)\s*/i, `$1\n\n\t<!-- Header -->\n\t${headerHtml}\n\n`);
            fs.writeFileSync(file, newContent, 'utf8');
            console.log(`Force Restored header into ${file}`);
            count++;
        }
    }
}
console.log(`Restored header in ${count} files`);
