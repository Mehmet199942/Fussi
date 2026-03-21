import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\mehme\Desktop\cozastore-master\checkout.html', 'r', encoding='utf-8') as f:
    c = f.read()

# ── 1. Replace left-column form (from <!-- Contact --> to </div><!-- /col left -->) ──
old_form_start = c.find('<!-- Contact -->')
old_form_end   = c.find('</div><!-- /col left -->')

new_form = '''<!-- Kontakt -->
					<div style="margin-bottom:24px;">
						<p class="checkout-section-title">Kontakt</p>
						<div class="checkout-field">
							<label>E-Mail-Adresse *</label>
							<input type="email" id="field-email" placeholder="max@beispiel.de" autocomplete="email">
							<div class="field-error-msg">Bitte gültige E-Mail eingeben.</div>
						</div>
					</div>

					<!-- Lieferung -->
					<div style="margin-bottom:24px;">
						<p class="checkout-section-title">Lieferung</p>

						<div class="checkout-field">
							<label>Land / Region</label>
							<select id="field-country" autocomplete="country">
								<option value="">– Land auswählen –</option>
								<option value="DE" selected>🇩🇪 Deutschland</option>
								<option value="AT">🇦🇹 Österreich</option>
								<option value="CH">🇨🇭 Schweiz</option>
								<option value="TR">🇹🇷 Türkei</option>
								<option value="NL">🇳🇱 Niederlande</option>
								<option value="BE">🇧🇪 Belgien</option>
								<option value="FR">🇫🇷 Frankreich</option>
								<option value="IT">🇮🇹 Italien</option>
								<option value="ES">🇪🇸 Spanien</option>
								<option value="PL">🇵🇱 Polen</option>
								<option value="GB">🇬🇧 Vereinigtes Königreich</option>
								<option value="US">🇺🇸 USA</option>
								<option value="OTHER">Anderes Land</option>
							</select>
							<div class="field-error-msg">Bitte Land auswählen.</div>
						</div>

						<div class="field-row">
							<div class="checkout-field">
								<label>Vorname *</label>
								<input type="text" id="field-firstname" placeholder="Max" autocomplete="given-name">
								<div class="field-error-msg">Bitte Vorname eingeben.</div>
							</div>
							<div class="checkout-field">
								<label>Nachname *</label>
								<input type="text" id="field-lastname" placeholder="Mustermann" autocomplete="family-name">
								<div class="field-error-msg">Bitte Nachname eingeben.</div>
							</div>
						</div>

						<div class="checkout-field">
							<label>Firma (optional)</label>
							<input type="text" id="field-company" placeholder="Muster GmbH" autocomplete="organization">
						</div>

						<div class="checkout-field" style="position:relative;">
							<label>Adresse *</label>
							<input type="text" id="field-street" placeholder="Musterstraße 1" autocomplete="off">
							<div class="field-error-msg">Bitte Adresse eingeben.</div>
						</div>

						<div class="checkout-field">
							<label>Wohnung, Zimmer, usw. (optional)</label>
							<input type="text" id="field-apartment" placeholder="App. 4B" autocomplete="address-line2">
						</div>

						<div class="field-row">
							<div class="checkout-field">
								<label>Postleitzahl *</label>
								<input type="text" id="field-zip" placeholder="12345" autocomplete="postal-code">
								<div class="field-error-msg">Bitte PLZ eingeben.</div>
							</div>
							<div class="checkout-field" style="flex:2;">
								<label>Stadt *</label>
								<input type="text" id="field-city" placeholder="Berlin" autocomplete="address-level2">
								<div class="field-error-msg">Bitte Stadt eingeben.</div>
							</div>
						</div>

						<div class="checkout-field">
							<label>Telefon (optional)</label>
							<input type="tel" id="field-phone" placeholder="+49 123 456789" autocomplete="tel">
						</div>

						<label style="display:flex;align-items:flex-start;gap:10px;cursor:pointer;font-family:Poppins-Regular;font-size:13px;color:#888;margin-top:6px;margin-bottom:4px;">
							<input type="checkbox" id="save-info" style="margin-top:3px;flex-shrink:0;width:15px;height:15px;accent-color:#fff;">
							<span>Meine Informationen speichern und nächstes Mal schneller bezahlen</span>
						</label>
					</div>

					<!-- Payment -->
					<div style="margin-bottom: 32px;">
						<p class="checkout-section-title">Zahlungsart</p>

						<div style="margin-bottom:6px;">
							<button type="button" onclick="selectPayment('paypal'); submitOrder(event);" style="width:100%;background:#FFC439;border:none;border-radius:6px;padding:16px 20px;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:4px;transition:background .2s;" onmouseover="this.style.background='#f0b429'" onmouseout="this.style.background='#FFC439'">
								<span style="font-family:Arial,sans-serif;font-weight:900;font-size:22px;color:#003087;letter-spacing:-0.5px;">Pay</span><span style="font-family:Arial,sans-serif;font-weight:900;font-size:22px;color:#009cde;letter-spacing:-0.5px;">Pal</span>
							</button>
							<p style="text-align:center;font-family:Poppins-Regular;font-size:11px;color:#555;margin:8px 0 0;">Du wirst sicher zu PayPal weitergeleitet.</p>
						</div>

						<div style="display:flex;align-items:center;gap:12px;margin:20px 0;">
							<div style="flex:1;height:1px;background:#222;"></div>
							<span style="font-family:Poppins-Regular;font-size:12px;color:#555;white-space:nowrap;">Oder zahle mit</span>
							<div style="flex:1;height:1px;background:#222;"></div>
						</div>

						<div class="payment-option selected" data-method="card" onclick="selectPayment('card')">
							<input type="radio" name="payment" value="card" checked>
							<div class="payment-radio-dot"></div>
							<i class="fa fa-credit-card payment-icon"></i>
							<span class="payment-label">Kreditkarte</span>
							<div class="payment-logos">
								<span style="background:#1a1a4e;color:#fff;font-family:Poppins-Bold;font-size:11px;padding:3px 7px;border-radius:3px;letter-spacing:0;">VISA</span>
								<span style="background:#1a1a1a;color:#eb001b;font-family:Poppins-Bold;font-size:10px;padding:3px 6px;border-radius:3px;letter-spacing:0;">MC</span>
								<span style="background:#003087;color:#fff;font-family:Poppins-Bold;font-size:10px;padding:3px 6px;border-radius:3px;letter-spacing:0;">AMEX</span>
							</div>
						</div>

						<div id="card-fields-panel" class="visible">
							<div class="card-panel-inner">
								<div class="card-row-icons">
									<span>VISA</span><span style="color:#eb001b;">MC</span><span style="color:#2566af;">AMEX</span>
								</div>
								<div class="checkout-field">
									<label>Karteninhaber *</label>
									<input type="text" id="field-card-name" placeholder="MAX MUSTERMANN" autocomplete="cc-name" style="text-transform:uppercase;">
									<div class="field-error-msg">Bitte Namen eingeben.</div>
								</div>
								<div class="checkout-field">
									<label>Kartennummer *</label>
									<input type="text" id="field-card-number" placeholder="0000 0000 0000 0000" autocomplete="cc-number" maxlength="19" inputmode="numeric">
									<div class="field-error-msg">Bitte gültige Kartennummer eingeben.</div>
								</div>
								<div class="field-row">
									<div class="checkout-field">
										<label>Ablaufdatum *</label>
										<input type="text" id="field-card-expiry" placeholder="MM / JJ" autocomplete="cc-exp" maxlength="7" inputmode="numeric">
										<div class="field-error-msg">Bitte Datum eingeben.</div>
									</div>
									<div class="checkout-field">
										<label>CVV *</label>
										<input type="text" id="field-card-cvv" placeholder="•••" autocomplete="cc-csc" maxlength="4" inputmode="numeric">
										<div class="field-error-msg">Bitte CVV eingeben.</div>
									</div>
								</div>
							</div>
						</div>

						<div class="payment-option" data-method="bank" onclick="selectPayment('bank')">
							<input type="radio" name="payment" value="bank">
							<div class="payment-radio-dot"></div>
							<i class="fa fa-university payment-icon"></i>
							<span class="payment-label">Banküberweisung (SEPA)</span>
						</div>

						<div id="bank-panel">
							<div class="bank-info">
								<p style="margin:0 0 12px 0;color:#aaa;">Überweise den Betrag auf folgendes Konto. Deine Bestellung wird bearbeitet, sobald die Zahlung eingegangen ist.</p>
								<table>
									<tr><td>Empfänger</td><td>WORLD CUP SHOP GmbH</td></tr>
									<tr><td>IBAN</td><td>DE89 3704 0044 0532 0130 00</td></tr>
									<tr><td>BIC</td><td>COBADEFFXXX</td></tr>
									<tr><td>Verwendungszweck</td><td id="bank-reference">Wird nach Bestellung angezeigt</td></tr>
								</table>
							</div>
						</div>

						<div id="paypal-panel" style="display:none;"></div>
					</div>

					<!-- Terms & Submit (mobile) -->
					<div class="d-lg-none">
						<label style="display:flex;align-items:flex-start;gap:10px;cursor:pointer;font-family:Poppins-Regular;font-size:13px;color:#888;margin-bottom:20px;">
							<input type="checkbox" id="terms-check-mobile" style="margin-top:2px;flex-shrink:0;width:16px;height:16px;accent-color:#fff;">
							<span>Ich akzeptiere die <a href="#" style="color:#fff;">AGB</a> und die <a href="#" style="color:#fff;">Datenschutzerklärung</a>.</span>
						</label>
						<button class="btn-place-order" onclick="submitOrder(event)">Bestellung aufgeben</button>
						<div class="secure-badge">
							<i class="zmdi zmdi-lock"></i>
							<span>SSL-gesicherte Übertragung</span>
						</div>
					</div>

				'''

c = c[:old_form_start] + new_form + c[old_form_end:]

# ── 2. Replace Nominatim block with Google Places ──
ac_pos  = c.find('<!-- ═════════ ADDRESS AUTOCOMPLETE')
body_pos = c.find('</body>', ac_pos)

new_ac = '''<!-- Google Places Autocomplete -->
\t<style>
\t\t.pac-container {
\t\t\tbackground:#111 !important;
\t\t\tborder:1px solid #333 !important;
\t\t\tborder-top:none !important;
\t\t\tborder-radius:0 0 4px 4px;
\t\t\tbox-shadow:0 8px 24px rgba(0,0,0,.7) !important;
\t\t\tfont-family:Poppins-Regular,Arial,sans-serif;
\t\t\tz-index:99999 !important;
\t\t}
\t\t.pac-item {
\t\t\tpadding:11px 14px;
\t\t\tborder-top:1px solid #1e1e1e !important;
\t\t\tcursor:pointer;
\t\t\tcolor:#888;
\t\t\tbackground:#111 !important;
\t\t\tfont-size:13px;
\t\t\tline-height:1.4;
\t\t}
\t\t.pac-item:hover, .pac-item-selected { background:#1a1a1a !important; color:#fff; }
\t\t.pac-item-query { color:#ddd !important; font-family:Poppins-Medium,Arial,sans-serif; font-size:13px; }
\t\t.pac-matched { font-weight:700; color:#fff !important; }
\t\t.pac-icon { filter:invert(.5) brightness(2); margin-top:2px; }
\t\t.pac-logo::after { filter:invert(.3); padding:6px 14px; }
\t</style>
\t<script>
\t\tfunction initGooglePlaces() {
\t\t\tvar input = document.getElementById('field-street');
\t\t\tif (!input || !window.google) return;
\t\t\tvar ac = new google.maps.places.Autocomplete(input, {
\t\t\t\tcomponentRestrictions: { country: 'de' },
\t\t\t\tfields: ['address_components'],
\t\t\t\ttypes: ['address']
\t\t\t});
\t\t\tac.addListener('place_changed', function () {
\t\t\t\tvar place = ac.getPlace();
\t\t\t\tvar comps = place.address_components || [];
\t\t\t\tvar num = '', road = '', city = '', zip = '';
\t\t\t\tcomps.forEach(function (cp) {
\t\t\t\t\tvar t = cp.types[0];
\t\t\t\t\tif (t === 'street_number') num  = cp.long_name;
\t\t\t\t\telse if (t === 'route')    road = cp.long_name;
\t\t\t\t\telse if (t === 'locality' || t === 'postal_town') city = city || cp.long_name;
\t\t\t\t\telse if (t === 'postal_code') zip = cp.long_name;
\t\t\t\t});
\t\t\t\tinput.value = road + (num ? ' ' + num : '');
\t\t\t\tif (zip)  document.getElementById('field-zip').value  = zip;
\t\t\t\tif (city) document.getElementById('field-city').value = city;
\t\t\t\tdocument.getElementById('field-country').value = 'DE';
\t\t\t});
\t\t}
\t</script>
\t<!-- Replace YOUR_GOOGLE_MAPS_API_KEY with your key (Google Cloud Console → Maps JS API + Places API) -->
\t<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY&libraries=places&callback=initGooglePlaces" async defer></script>
'''

c = c[:ac_pos] + new_ac + '</body>\n</html>'

with open(r'C:\Users\mehme\Desktop\cozastore-master\checkout.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done. Size:', len(c))
