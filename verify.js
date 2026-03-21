const fs = require('fs');
const c = fs.readFileSync('product-detail.html', 'utf8');
console.log('slick3-pd exists:', c.includes('slick3-pd'));
console.log('item-slick3-pd exists:', c.includes('item-slick3-pd'));
console.log('old slick3 class remains:', c.includes('class="slick3 '));
console.log('old item-slick3 remains:', c.includes('class="item-slick3"'));
