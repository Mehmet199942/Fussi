import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\mehme\Desktop\cozastore-master\checkout.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove Google Places block + closing tags (everything from that comment to end)
start = c.find('\n\t<!-- Google Places Autocomplete -->')
if start == -1:
    start = c.find('\n\t<!-- Address Autocomplete')
c = c[:start]

nominatim_block = """
\t<!-- Address Autocomplete (OpenStreetMap Nominatim) -->
\t<style>
\t\t#street-suggestions {
\t\t\tdisplay: none;
\t\t\tposition: absolute;
\t\t\ttop: 100%;
\t\t\tleft: 0;
\t\t\tright: 0;
\t\t\tbackground: #111;
\t\t\tborder: 1px solid #333;
\t\t\tborder-top: none;
\t\t\tborder-radius: 0 0 4px 4px;
\t\t\tbox-shadow: 0 8px 24px rgba(0,0,0,.7);
\t\t\tz-index: 99999;
\t\t\tmax-height: 320px;
\t\t\toverflow-y: auto;
\t\t}
\t\t.sug-item {
\t\t\tdisplay: flex;
\t\t\talign-items: flex-start;
\t\t\tgap: 12px;
\t\t\tpadding: 11px 14px;
\t\t\tcursor: pointer;
\t\t\tborder-top: 1px solid #1e1e1e;
\t\t\ttransition: background .15s;
\t\t}
\t\t.sug-item:first-child { border-top: none; }
\t\t.sug-item:hover, .sug-item.active { background: #1a1a1a; }
\t\t.sug-pin {
\t\t\tflex-shrink: 0;
\t\t\tmargin-top: 3px;
\t\t\tcolor: #555;
\t\t\tfont-size: 15px;
\t\t\twidth: 18px;
\t\t\ttext-align: center;
\t\t}
\t\t.sug-text { flex: 1; min-width: 0; }
\t\t.sug-main {
\t\t\tfont-family: Poppins-Medium, Arial, sans-serif;
\t\t\tfont-size: 13px;
\t\t\tcolor: #ddd;
\t\t\twhite-space: nowrap;
\t\t\toverflow: hidden;
\t\t\ttext-overflow: ellipsis;
\t\t}
\t\t.sug-main b { color: #fff; font-weight: 700; }
\t\t.sug-sub {
\t\t\tfont-family: Poppins-Regular, Arial, sans-serif;
\t\t\tfont-size: 11px;
\t\t\tcolor: #555;
\t\t\tmargin-top: 2px;
\t\t\twhite-space: nowrap;
\t\t\toverflow: hidden;
\t\t\ttext-overflow: ellipsis;
\t\t}
\t\t.sug-footer {
\t\t\tpadding: 5px 14px 7px;
\t\t\ttext-align: right;
\t\t\tborder-top: 1px solid #1e1e1e;
\t\t\tfont-family: Poppins-Regular, Arial, sans-serif;
\t\t\tfont-size: 10px;
\t\t\tcolor: #444;
\t\t}
\t</style>
\t<script>
\t(function () {
\t\tvar input, box, timer, activeIdx = -1, lastResults = [];

\t\tfunction init() {
\t\t\tinput = document.getElementById('field-street');
\t\t\tif (!input) return;

\t\t\tbox = document.createElement('div');
\t\t\tbox.id = 'street-suggestions';
\t\t\tinput.parentNode.style.position = 'relative';
\t\t\tinput.parentNode.appendChild(box);

\t\t\tinput.addEventListener('input', function () {
\t\t\t\tclearTimeout(timer);
\t\t\t\tvar q = input.value.trim();
\t\t\t\tif (q.length < 3) { hide(); return; }
\t\t\t\ttimer = setTimeout(function () { fetchSuggestions(q); }, 350);
\t\t\t});

\t\t\tinput.addEventListener('keydown', function (e) {
\t\t\t\tvar items = box.querySelectorAll('.sug-item');
\t\t\t\tif (!items.length) return;
\t\t\t\tif (e.key === 'ArrowDown') {
\t\t\t\t\te.preventDefault();
\t\t\t\t\tactiveIdx = Math.min(activeIdx + 1, items.length - 1);
\t\t\t\t\thighlight(items);
\t\t\t\t} else if (e.key === 'ArrowUp') {
\t\t\t\t\te.preventDefault();
\t\t\t\t\tactiveIdx = Math.max(activeIdx - 1, 0);
\t\t\t\t\thighlight(items);
\t\t\t\t} else if (e.key === 'Enter' && activeIdx >= 0) {
\t\t\t\t\te.preventDefault();
\t\t\t\t\tfillFromResult(lastResults[activeIdx]);
\t\t\t\t\thide();
\t\t\t\t} else if (e.key === 'Escape') {
\t\t\t\t\thide();
\t\t\t\t}
\t\t\t});

\t\t\tdocument.addEventListener('click', function (e) {
\t\t\t\tif (!input.parentNode.contains(e.target)) hide();
\t\t\t});
\t\t}

\t\tfunction highlight(items) {
\t\t\titems.forEach(function (el, i) {
\t\t\t\tel.classList.toggle('active', i === activeIdx);
\t\t\t});
\t\t}

\t\tfunction fetchSuggestions(q) {
\t\t\tvar url = 'https://nominatim.openstreetmap.org/search'
\t\t\t\t+ '?format=json&addressdetails=1&limit=6&countrycodes=de,at,ch'
\t\t\t\t+ '&q=' + encodeURIComponent(q);
\t\t\tfetch(url, { headers: { 'Accept-Language': 'de' } })
\t\t\t\t.then(function (r) { return r.json(); })
\t\t\t\t.then(function (data) { render(data); })
\t\t\t\t.catch(function () { hide(); });
\t\t}

\t\tfunction render(results) {
\t\t\tlastResults = results;
\t\t\tactiveIdx = -1;
\t\t\tbox.innerHTML = '';
\t\t\tif (!results.length) { hide(); return; }

\t\t\tresults.forEach(function (r) {
\t\t\t\tvar a = r.address || {};
\t\t\t\tvar road = a.road || a.pedestrian || a.path || a.suburb || '';
\t\t\t\tvar num  = a.house_number || '';
\t\t\t\tvar city = a.city || a.town || a.village || a.municipality || '';
\t\t\t\tvar state = a.state || '';
\t\t\t\tvar zip  = a.postcode || '';

\t\t\t\tvar mainText = road + (num ? ' ' + num : '');
\t\t\t\tif (!mainText) mainText = r.display_name.split(',')[0];
\t\t\t\tvar subText = [zip, city, state].filter(Boolean).join(', ');

\t\t\t\tvar item = document.createElement('div');
\t\t\t\titem.className = 'sug-item';
\t\t\t\titem.innerHTML =
\t\t\t\t\t'<div class="sug-pin"><i class="zmdi zmdi-pin"></i></div>' +
\t\t\t\t\t'<div class="sug-text">' +
\t\t\t\t\t\t'<div class="sug-main">' + esc(mainText) + '</div>' +
\t\t\t\t\t\t'<div class="sug-sub">'  + esc(subText)  + '</div>' +
\t\t\t\t\t'</div>';

\t\t\t\t(function (res) {
\t\t\t\t\titem.addEventListener('mousedown', function (e) {
\t\t\t\t\t\te.preventDefault();
\t\t\t\t\t\tfillFromResult(res);
\t\t\t\t\t\thide();
\t\t\t\t\t});
\t\t\t\t}(r));

\t\t\t\tbox.appendChild(item);
\t\t\t});

\t\t\tvar foot = document.createElement('div');
\t\t\tfoot.className = 'sug-footer';
\t\t\tfoot.textContent = 'Powered by OpenStreetMap';
\t\t\tbox.appendChild(foot);

\t\t\tbox.style.display = 'block';
\t\t}

\t\tfunction fillFromResult(r) {
\t\t\tvar a = r.address || {};
\t\t\tvar road = a.road || a.pedestrian || a.path || '';
\t\t\tvar num  = a.house_number || '';
\t\t\tvar city = a.city || a.town || a.village || a.municipality || '';
\t\t\tvar zip  = a.postcode || '';
\t\t\tvar cc   = (a.country_code || 'de').toUpperCase();

\t\t\tinput.value = road + (num ? ' ' + num : '');
\t\t\tif (zip)  document.getElementById('field-zip').value  = zip;
\t\t\tif (city) document.getElementById('field-city').value = city;
\t\t\tvar sel = document.getElementById('field-country');
\t\t\tif (sel) {
\t\t\t\tfor (var i = 0; i < sel.options.length; i++) {
\t\t\t\t\tif (sel.options[i].value === cc) { sel.selectedIndex = i; break; }
\t\t\t\t}
\t\t\t}
\t\t}

\t\tfunction hide() { box.style.display = 'none'; activeIdx = -1; }

\t\tfunction esc(s) {
\t\t\treturn String(s)
\t\t\t\t.replace(/&/g, '&amp;')
\t\t\t\t.replace(/</g, '&lt;')
\t\t\t\t.replace(/>/g, '&gt;');
\t\t}

\t\tif (document.readyState === 'loading') {
\t\t\tdocument.addEventListener('DOMContentLoaded', init);
\t\t} else {
\t\t\tinit();
\t\t}
\t})();
\t</script>
</body>
</html>"""

c = c + nominatim_block

with open(r'C:\Users\mehme\Desktop\cozastore-master\checkout.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done. Size:', len(c))
print('Nominatim present:', 'nominatim.openstreetmap.org' in c)
print('Google Places removed:', 'maps.googleapis.com' not in c)
