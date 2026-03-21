const fs = require('fs');
const path = require('path');

const indexHtml = fs.readFileSync('index.html', 'utf8');
const headerMatch = indexHtml.match(/<!-- Header -->[\s\S]*?<!-- Cart -->/);
if (!headerMatch) throw new Error("Header block not found in index.html");
const headerHtml = headerMatch[0];

function getAllHtmlFiles(dir, fileList = []) {
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);
        if (stat.isDirectory()) {
            if (!['node_modules', '.git', 'recovery_backup', 'safe_restore', 'data'].includes(file)) {
                getAllHtmlFiles(filePath, fileList);
            }
        } else if (file.endsWith('.html') && file !== 'index.html') {
            fileList.push(filePath);
        }
    });
    return fileList;
}

const filesToUpdate = getAllHtmlFiles('.');

filesToUpdate.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let updated = false;

    // 1. Try to replace standard Header block
    if (content.includes('<!-- Header -->') && content.includes('<!-- Cart -->')) {
        content = content.replace(/<!-- Header -->[\s\S]*?<!-- Cart -->/, headerHtml);
        updated = true;
    } 
    // 2. Try to replace Flutter Header block if standard is not present
    else if (content.includes('<!-- Flutter Header -->') && content.includes('<!-- Cart -->')) {
        content = content.replace(/<!-- Flutter Header -->[\s\S]*?<!-- Cart -->/, headerHtml);
        updated = true;
    }

    if (updated) {
        // REMOVE DUPLICATE SIDEBARS (anything that might be outside the header block)
        // We only want ONE wrap-sidebar-menu. The one we just inserted is already there.
        // If there are more, they are orphans from previous versions.
        const sidebarCount = (content.match(/<div class="wrap-sidebar-menu/g) || []).length;
        if (sidebarCount > 1) {
            // Keep the first one, remove the others
            const firstSidebarIdx = content.indexOf('<div class="wrap-sidebar-menu');
            const restOfContent = content.substring(firstSidebarIdx + 30);
            const secondSidebarIdx = restOfContent.indexOf('<div class="wrap-sidebar-menu');
            
            if (secondSidebarIdx !== -1) {
                // This is crude but we can look for the closing </div></div> of the sidebar
                // Actually, let's just use a more surgical approach for the known files
                content = content.replace(/<!-- Sidebar -->[\s\S]*?<\/div>[\s]*?<\/div>/g, (match, offset) => {
                    // Only replace if it's NOT the first one
                    return offset === content.indexOf('<!-- Sidebar -->') ? match : '';
                });
            }
        }

        // REMOVE DUPLICATE SEARCH MODALS
        // We only want ONE wrap-search-modal. The one we just inserted is already there.
        // If there are more, they are orphans from previous versions.
        const searchModalCount = (content.match(/<div class="wrap-search-modal/g) || []).length;
        if (searchModalCount > 1) {
            // Keep the first one, remove the others
            const firstSearchModalIdx = content.indexOf('<div class="wrap-search-modal');
            const restOfContent = content.substring(firstSearchModalIdx + 30); // Adjust offset if needed
            const secondSearchModalIdx = restOfContent.indexOf('<div class="wrap-search-modal');
            
            if (secondSearchModalIdx !== -1) {
                content = content.replace(/<!-- Search Modal -->[\s\S]*?<\/div>[\s]*?<\/div>/g, (match, offset) => {
                    // Only replace if it's NOT the first one
                    return offset === content.indexOf('<!-- Search Modal -->') ? match : '';
                });
            }
        }

        // Add dark mode to body if not present
        if (!content.includes('dark-mode')) {
            content = content.replace(/<body class="animsition">/, '<body class="animsition dark-mode">');
        }
        
        fs.writeFileSync(file, content);
        console.log(`Updated and cleaned ${file}`);
    }
});
