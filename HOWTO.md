# WORLD CUP SHOP – Produktseiten-Generator

## Übersicht

Mit diesem System pflegst du neue Produkte in einem Google Sheet und erzeugst daraus automatisch:
- eine fertige HTML-Produktdetailseite (`product-[slug].html`)
- einen aktualisierten Produktgrid auf der Übersichtsseite (`product.html`)

---

## Wichtige Dateien

| Datei / Ordner | Zweck |
|---|---|
| `scripts/generate.py` | Das Generator-Script – startest du zum Erzeugen der Seiten |
| `scripts/config.json` | Konfiguration: Google-Sheet-URL, Einstellungen |
| `scripts/requirements.txt` | Python-Abhängigkeiten |
| `templates/product-detail-template.html` | HTML-Vorlage für alle Produktdetailseiten |
| `templates/product-card-template.html` | HTML-Vorlage für eine Produktkachel im Grid |
| `data/products-example.csv` | Vorlage / Beispieldaten für das Google Sheet |
| `data/backups/` | Automatische Sicherungen vor jedem Überschreiben |
| `data/generator.log` | Protokoll des letzten Generator-Laufs |
| `product.html` | Produktübersichtsseite – Grid wird automatisch aktualisiert |

---

## Einmalige Einrichtung

### 1. Python installieren
Du benötigst Python 3.10 oder neuer.
Download: https://www.python.org/downloads/

### 2. Abhängigkeiten installieren
Öffne ein Terminal im Shop-Ordner und führe aus:
```
pip install -r scripts/requirements.txt
```

### 3. Google Sheet einrichten
1. Kopiere die Datei `data/products-example.csv` als Vorlage
2. Erstelle ein neues Google Sheet
3. Importiere die CSV-Datei: *Datei → Importieren*
4. Füge neue Produkte in neue Zeilen ein (Spaltenstruktur beibehalten!)

### 4. Google Sheet veröffentlichen und URL eintragen
1. Klicke im Google Sheet auf: **Datei → Freigeben → Im Web veröffentlichen**
2. Wähle: das richtige Tabellenblatt (nicht "Gesamtes Dokument")
3. Wähle als Format: **Durch Kommas getrennte Werte (.csv)**
4. Klicke auf **Veröffentlichen** und kopiere die URL
5. Öffne `scripts/config.json` und trage die URL ein:
   ```json
   "sheets_csv_url": "https://docs.google.com/spreadsheets/d/DEINE-ID/pub?output=csv"
   ```

---

## Produkt anlegen – Schritt für Schritt

### 1. Bilder hochladen
Lade das Produktbild in den Ordner `images/` hoch, z.B.:
```
images/mein-neues-shirt.png
images/mein-neues-shirt-2.png
```

### 2. Zeile im Google Sheet eintragen
Füge eine neue Zeile im Sheet hinzu. Pflichtfelder:

| Spalte | Beispiel | Erklärung |
|---|---|---|
| `name` | `Kurdistan Azadi Shirt` | Produktname, wird auf der Seite angezeigt |
| `slug` | `krd-azadi-shirt` | URL-Teil: `product-krd-azadi-shirt.html` – nur Kleinbuchstaben + Bindestriche! |
| `price` | `34.99` | Preis ohne €-Zeichen, Punkt als Dezimaltrennzeichen |
| `sku` | `KRD-AZADI-001` | Artikelnummer |
| `status` | `draft` oder `active` | `draft` = nicht veröffentlicht, `active` = live |
| `short_desc` | `Fan-Shirt im Kurdistan-Look.` | Kurzbeschreibung unter dem Preis |
| `image1` | `images/krd-azadi-shirt.png` | Hauptbild – Pfad relativ zum Shop-Root |

### 3. Optionale Felder

| Spalte | Erklärung | Default wenn leer |
|---|---|---|
| `title` | Browser-Titel | `{name} \| WORLD CUP SHOP` |
| `long_desc` | Längere Beschreibung im Accordion | – |
| `bullets` | Stichpunkte, getrennt durch `\|` | – |
| `washing` | Pflegehinweise, getrennt durch `\|` | – |
| `image2` | 2. Galeriebild | = image1 |
| `image3` | 3. Galeriebild | = image1 |
| `colors` | Farben, getrennt durch `\|` oder `,` | Schwarz, Weiß, Rot, Blau |
| `loyalty_points` | Treuepunkte | Preis × 6 automatisch |
| `category` | Kategorie | – |
| `show_on_listing` | Im Grid anzeigen? `yes` / `no` | `yes` |
| `sort_order` | Reihenfolge im Grid (1, 2, 3...) | alphabetisch |
| `meta_title` | SEO-Titel | = title |
| `meta_description` | SEO-Beschreibung | = short_desc |
| `og_image` | Social-Media-Vorschaubild | = image1 |

### Beispiel für Bullets-Spalte:
```
Design: Azadi Schriftzug|Material: 85% Baumwolle|Slim-Fit Schnitt|4 Farben verfügbar
```

### 4. Status setzen
- `draft` → Seite wird nicht generiert, nicht im Grid angezeigt
- `active` → Seite wird generiert und im Grid angezeigt

---

## Generator starten

```bash
# Alle aktiven Produkte generieren (normaler Betrieb)
python scripts/generate.py

# Trockenlauf – nichts wird geschrieben, nur Vorschau
python scripts/generate.py --dry-run

# Nur ein bestimmtes Produkt generieren
python scripts/generate.py --slug krd-azadi-shirt

# Lokale CSV-Datei statt Google Sheets (zum Testen)
python scripts/generate.py --local data/products-example.csv

# Ausführliche Ausgabe (für Fehlersuche)
python scripts/generate.py --verbose
```

---

## Wo landen die fertigen Dateien?

| Was | Wo |
|---|---|
| Produktdetailseiten | `product-[slug].html` im Shop-Root |
| Aktualisiertes Produktgrid | `product.html` (Grid wird zwischen den Markern ersetzt) |
| Sicherungen (Backups) | `data/backups/` |
| Protokoll | `data/generator.log` |

---

## Fehler erkennen und beheben

### 1. Generator-Log lesen
```bash
cat data/generator.log
```
Oder einfach die Ausgabe im Terminal lesen.

### 2. Häufige Fehler

| Fehlermeldung | Ursache | Lösung |
|---|---|---|
| `Pflichtfeld fehlt: 'slug'` | Slug-Spalte leer | Slug eintragen |
| `Ungültiger Slug 'Mein Shirt'` | Slug hat Großbuchstaben/Leerzeichen | z.B. `mein-shirt` |
| `Doppelter Slug 'krd-shirt'` | Zwei Produkte haben denselben Slug | Einmalige Slugs vergeben |
| `Template nicht gefunden` | `templates/`-Ordner fehlt oder unvollständig | Templates-Ordner nicht löschen |
| `sheets_csv_url` leer | Keine URL in config.json | URL eintragen (Schritt 4 der Einrichtung) |
| `requests`-Fehler | Internet-Verbindung oder Sheets-URL falsch | URL überprüfen, Sheet veröffentlicht? |

### 3. Dry-Run nutzen
Vor dem echten Generieren immer zuerst mit `--dry-run` testen:
```bash
python scripts/generate.py --dry-run
```
So sieht man, was generiert werden würde, ohne etwas zu verändern.

### 4. Backup wiederherstellen
Falls etwas schief läuft, liegen Sicherungen in `data/backups/`. Einfach die gewünschte Datei in den Shop-Root kopieren und umbenennen.

---

## Ablauf im Betrieb

```
1. Produktbild in images/ hochladen
      ↓
2. Neue Zeile im Google Sheet eintragen
      ↓
3. status = draft (zum Testen) oder active (sofort live)
      ↓
4. python scripts/generate.py --dry-run  ← prüfen
      ↓
5. python scripts/generate.py           ← generieren
      ↓
6. product-[slug].html ist fertig, product.html aktualisiert
      ↓
7. Dateien auf den Server hochladen (wie gewohnt per FTP/Deploy)
```

---

## Pflichtfelder auf einen Blick

```
name          ← immer
slug          ← immer (URL-sicher: nur a-z, 0-9, -)
price         ← immer (z.B. 29.99)
sku           ← immer (Artikelnummer)
status        ← immer (draft oder active)
short_desc    ← immer (Kurzbeschreibung)
image1        ← immer (Hauptbild, Pfad relativ zum Shop-Root)
```

---

## Design-Hinweise

Das Design wird **nicht verändert**. Das System ersetzt nur Inhalte in vordefinierten Platzhaltern. CSS, Header, Footer und JavaScript bleiben unberührt.

Möchtest du das Design der Produktseite anpassen, editiere:
- `templates/product-detail-template.html` → Layoutänderungen für alle Produktseiten
- `templates/product-card-template.html` → Änderungen an den Grid-Kacheln

Nach Änderungen an Templates: Generator erneut ausführen, um alle Seiten neu zu erzeugen.
