import os
import re

# Read the component header which has the perfect original code
with open('components/header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

count = 0
for file in html_files:
    if file == 'components/header.html':
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace placeholder with header html
    new_content = re.sub(r'<div id="header-placeholder"></div>', lambda _: header_html, content)
    
    # Remove the load-header.js script tag
    new_content = re.sub(r'<script src="js/load-header.js"></script>\n?', '', new_content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Restored {file}")
        count += 1
    else:
        # User script might have messed up index.html and nation.html?
        # Let's check if the header is missing entirely and insert it after <body ...>
        if '<header ' not in new_content and '<div id="header-placeholder"></div>' not in new_content:
            new_content = re.sub(r'(<body[^>]*>)\s*', r'\1\n\n\t<!-- Header -->\n\t' + header_html.replace('\\', '\\\\') + '\n\n', new_content, 1)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Force Restored header into {file}")
            count += 1
            
print(f"Restored header in {count} files")
