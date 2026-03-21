# Dokumentation: Statischer Shop Generator (Google Sheets)

Dieses Dokument erklärt, wie neue Produkte über eine CSV-Datei (z.B. Export aus Google Sheets) gepflegt werden, sodass automatisch neue Produktdetailseiten generiert und die Shop-Listingseite (`nation.html`) aktualisiert werden.

## 1. Welche Dateien sind wichtig?
- **`data/products_export.csv`**: Die Datenquelle. Hierhin musst du deine Tabelle aus Google Sheets exportieren.
- **`scripts/generate_shop.py`**: Das Python-Script, das die HTML-Dateien aus der CSV baut.
- **`templates/product-detail-template.html`**: Das HTML-Template für die Detailseiten mit den `%%PLATZHALTER%%` Variablen.
- **`data/products.js`**: Die Shop-Datenbank. Diese Datei wird **automatisch** vom Script mit neuen CSV-Produkten ergänzt, damit die Produktkarten auf der Übersichtsseite erscheinen.
- **`generated/`**: In diesem neuen Ordner landen alle finalen, generierten HTML-Detailseiten.
- **`images/`**: Hier liegen die Bilder (idealerweise als Unterordner pro Nation strukturiert, z.B. `images/krd/bild.png`).

## 2. Wie ist die Tabelle (Google Sheets) aufgebaut?
Das Sheet braucht exakt folgende Spalten-Namen in der ersten Zeile (siehe die beiliegende Dummy-Datei):
`id`, `name`, `price`, `type`, `nation`, `image`, `image2`, `image3`, `image4`, `image5`, `shortDescription`, `description`, `bullets`, `washingInstructions`, `colors`, `sizeNote`, `category`, `keywords`, `status`

### Pflichtfelder
- `id`: Der Eindeutige Slug des Produktes (z.B. `krd-azadi-shirt-white`). Wird für die Dateibenennung genutzt.
- `name`: Der Produktname (z.B. `Kurdistan Azadi T-Shirt White`).
- `price`: Der Preis als Zahl (z.B. `34.99` - Wichtig: Punkt statt Komma).
- `nation`: Der Ländercode (z.B. `krd`, `de`).
- `image`: Das Hauptbild (Pfade relativ zum Hauptordner, also `images/krd/meinbild.png`).
- **`status`**: Muss exakt `active` lauten! Nur Produkte mit Status "active" werden generiert.

### Optionale Felder
- `image2` bis `image5`: Zusätzliche Bilder für die Galerie-Ansicht.
- `colors`: Verfügbare Farben, getrennt durch das Pipe-Zeichen `|` (z.B. `Schwarz|Weiß`).
- `bullets`: Bullet-Points für die Beschreibung, getrennt durch `|` (z.B. `100% Baumwolle|Slim Fit`).
- `washingInstructions`: Waschhinweise, getrennt durch `|`.
- `description`: Langer Beschreibungstext.

*Anmerkung: Wenn Listen benötigt werden (z.B. Farben, Bulletpoints), immer mit `|` trennen.*

## 3. Wie werden neue Produkte angelegt (Bedienfluss)?
1. **Bilder ablegen**: Lege deine neuen Bilder in den Ordner `images/` (oder z.B. `images/krd/`) innerhalb von `cozastore-master` ab.
2. **Sheet pflegen**: Trage die Produktdaten in dein Google Sheet ein. Setze den `status` auf `active`.
3. **CSV herunterladen**: Gehe in Google Sheets auf *Datei > Herunterladen > als CSV (.csv)*.
4. **CSV speichern**: Speichere die heruntergeladene Datei im Ordner `cozastore-master/data/` und nenne sie exakt **`products_export.csv`** (überschreibe die bestehende).
5. **Generator starten**: Führe das Python-Script über das Terminal / CMD aus. (siehe Punkt 4).

## 4. Wie wird der Generator gestartet?
Öffne das Terminal in deinem `cozastore-master` Verzeichnis und tippe in die Konsole (Kommandozeile):

```bash
python scripts/generate_shop.py
```

Das Skript gibt dir anschließend Feedback:
- Wie viele Produkte verarbeitet wurden.
- In welche HTML-Dateien sie unter `/generated/` gespeichert wurden.
- Ob `products.js` erfolgreich aktualisiert wurde.

## 5. Wo landen die Dateien?
- Die HTML-Dateien liegen im **`generated/`** Ordner (z.B. `generated/product-krd-azadi-shirt-white.html`).
- Durch den in das Template eingesetzten `<base href="../">` Tag funktionieren Bilder, CSS und JS auf den generierten Unterseiten reibungslos.
- Die **Übersichtsseite / Listing Seite (`nation.html`) bleibt unverändert**. Da das Python-Skript aber automatisch dein neues Produkt als Liste ans Ende von `data/products.js` schreibt (zwischen die "AUTO GENERATED" Kommentare), baut die `nation.html`-Seite vollautomatisch die neue Produktkachel für das Listing und verlinkt von dort aus direkt auf die `generated/` Datei!

## 6. Fehler & Fallbacks erkennen
- Wenn das Script stoppt oder im Terminal steht: `Skipping product with missing id/slug`, dann fehlt eine ID in der CSV.
- Fehlen in der CSV `image2` oder `image3`, nutzt der Generator einfach stumm das Hauptbild (`image`) auch für die Thumbnails, damit die Galerie fehlerfrei läuft.
- Bei CSS/Bild Anzeige-Fehlern in der generierten HTML: Überprüfe, ob der Bildpfad exakt stimmt (z.B. `images/krd/...`).
- **Wichtig**: Du solltest alte, hardcodierte "KRD"-Produkte in der `data/products.js` (die vor dem `AUTO GENERATED` Block stehen) nicht mit identischen IDs (Slugs) in der Google-Tabelle neu anlegen, da sie sonst doppelt im Listing auftauchen könnten. Lösche die hardcodierten Einträge notfalls in der Datei `data/products.js` heraus, wenn du voll auf Google Sheets umgestiegen bist.
