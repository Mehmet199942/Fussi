const fs = require('fs');
let content = fs.readFileSync('product-detail.html', 'utf8');

const shopJsMarker = '<script src="js/shop.js"></script>';
const shopJsIdx = content.lastIndexOf(shopJsMarker);

// Find the second (last) </script> before shop.js
const secondScriptClose = content.lastIndexOf('</script>', shopJsIdx);

// Everything between the second </script> and shopJsMarker is orphaned code
const orphanBlock = content.substring(secondScriptClose + 9, shopJsIdx);
console.log('Orphan block length:', orphanBlock.length);
console.log('Orphan starts with:', orphanBlock.substring(0, 40));

// Remove it
const cleaned = content.substring(0, secondScriptClose + 9) + '\n' + content.substring(shopJsIdx);

fs.writeFileSync('product-detail.html', cleaned, 'utf8');
console.log('Done! File cleaned.');
