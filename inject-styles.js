const fs = require('fs');

const filesToUpdate = ['product.html', 'product-detail.html', 'shoping-cart.html'];
const styleToInject = `
	<link rel="stylesheet" type="text/css" href="css/custom.css">
	<style>
		/* Force nav bar to solid black on this page */
		.header-v4 .wrap-menu-desktop,
		.header-v4 .top-bar {
			background-color: #000000 !important;
		}
	</style>
</head>`;

filesToUpdate.forEach(f => {
    let content = fs.readFileSync(f, 'utf8');
    // Ensure we haven't already injected it
    if (!content.includes('href="css/custom.css"')) {
        content = content.replace('</head>', styleToInject);
        fs.writeFileSync(f, content);
        console.log('Injected styles to ' + f);
    }
});
