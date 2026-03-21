const nations = [
    // --- Pinned Favorites ---
    { id: "de", name: "Deutschland", code: "DE" },
    { id: "br", name: "Brasilien", code: "BR" },
    { id: "tr", name: "Türkei", code: "TR" },
    { id: "krd", name: "Kurdistan", code: "KRD", flagCode: "iq-kr" },
    { id: "es", name: "Spanien", code: "ES" },
    { id: "it", name: "Italien", code: "IT" },
    { id: "fr", name: "Frankreich", code: "FR" },

    // --- Alphabetical order (A-Z) ---
    { id: "ar", name: "Argentinien", code: "AR" },
    { id: "au", name: "Australien", code: "AU" },
    { id: "be", name: "Belgien", code: "BE" },
    { id: "cr", name: "Costa Rica", code: "CR" },
    { id: "dk", name: "Dänemark", code: "DK" },
    { id: "ec", name: "Ecuador", code: "EC" },
    { id: "gb-eng", name: "England", code: "GB-ENG" },
    { id: "gh", name: "Ghana", code: "GH" },
    { id: "ir", name: "Iran", code: "IR" },
    { id: "jp", name: "Japan", code: "JP" },
    { id: "cm", name: "Kamerun", code: "CM" },
    { id: "ca", name: "Kanada", code: "CA" },
    { id: "qa", name: "Katar", code: "QA" },
    { id: "hr", name: "Kroatien", code: "HR" },
    { id: "ma", name: "Marokko", code: "MA" },
    { id: "mx", name: "Mexiko", code: "MX" },
    { id: "nl", name: "Niederlande", code: "NL" },
    { id: "pl", name: "Polen", code: "PL" },
    { id: "pt", name: "Portugal", code: "PT" },
    { id: "sa", name: "Saudi-Arabien", code: "SA" },
    { id: "ch", name: "Schweiz", code: "CH" },
    { id: "sn", name: "Senegal", code: "SN" },
    { id: "rs", name: "Serbien", code: "RS" },
    { id: "kr", name: "Südkorea", code: "KR" },
    { id: "tn", name: "Tunesien", code: "TN" },
    { id: "us", name: "USA", code: "US" },
    { id: "uy", name: "Uruguay", code: "UY" },
    { id: "gb-wls", name: "Wales", code: "GB-WLS" }
];

const nationColors = {
    "ec": "FFDD00", "nl": "F36C21", "qa": "8A1538", "sn": "00853F",
    "gb-eng": "FFFFFF", "ir": "239F40", "us": "002868", "gb-wls": "AE2630",
    "ar": "75AADB", "mx": "006847", "pl": "DC143C", "sa": "006C35",
    "au": "FFCD00", "dk": "C60C30", "fr": "002395", "tn": "E70013",
    "cr": "CE1126", "de": "FFFFFF", "jp": "000555", "es": "AA151B",
    "be": "E30613", "ca": "FF0000", "hr": "FF0000", "ma": "C1272D",
    "br": "FFD700", "cm": "007A5E", "rs": "C6363C", "ch": "FF0000",
    "gh": "FFFFFF", "pt": "FF0000", "kr": "000000", "uy": "75AADB",
    "tr": "E30A17", "it": "0066B2", "krd": "2E8C4A"
};

const nationTextColors = {
    "de": "000000", "gb-eng": "CE1124", "gh": "000000",
    "tr": "FFFFFF", "it": "FFFFFF", "krd": "FFFFFF"
};

const productTypes = {
    SHIRT: "shirt",
    BALACLAVA: "balaclava",
    FLAG: "flag",
    HOODIE: "hoodie",
    AZADI_SHIRT: "azadi"
};

const products = [];

// The products array is now exclusively populated by the Google Sheets CSV import.
// (The hardcoded generic products have been removed)

// --- AUTO GENERATED FROM CSV START ---
const csvProducts = [
    {
        "id": "krd 12",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 1,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/12.png",
        "category": "",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "",
        "sizeNote": "",
        "keywords": "",
        "related_products": "",
        "url": "generated/product-krd 12.html",
        "image2": "images/krd/12.png",
        "image3": "images/krd/12.png"
    },
    {
        "id": "br 1",
        "name": "Brasilien Retro",
        "price": 29.9,
        "priority": 0,
        "type": "shirt",
        "nation": "br",
        "image": "images/br/1.png",
        "category": "",
        "shortDescription": "Brasilien Retro",
        "description": "",
        "sizeNote": "",
        "keywords": "",
        "related_products": "",
        "url": "generated/product-br 1.html",
        "image2": "images/br/1.png",
        "image3": "images/br/1.png"
    },
    {
        "id": "de 1",
        "name": "Deutschland Retro Trikot",
        "price": 29.9,
        "priority": 0,
        "type": "shirt",
        "nation": "de",
        "image": "images/de/07556799.jpg",
        "category": "",
        "shortDescription": "Deutschland Retro Trikot",
        "description": "",
        "sizeNote": "",
        "keywords": "",
        "related_products": "",
        "url": "generated/product-de 1.html",
        "image2": "images/de/07556799.jpg",
        "image3": "images/de/07556799.jpg"
    },
    {
        "id": "krd 1",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/1.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "30 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 1.html",
        "image2": "images/krd/1.png",
        "image3": "images/krd/1.png"
    },
    {
        "id": "krd 2",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/2.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "31 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 2.html",
        "image2": "images/krd/2.png",
        "image3": "images/krd/2.png"
    },
    {
        "id": "krd 3",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/3.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "32 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 3.html",
        "image2": "images/krd/3.png",
        "image3": "images/krd/3.png"
    },
    {
        "id": "krd 4",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/4.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "33 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 4.html",
        "image2": "images/krd/4.png",
        "image3": "images/krd/4.png"
    },
    {
        "id": "krd 5",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/5.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "34 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 5.html",
        "image2": "images/krd/5.png",
        "image3": "images/krd/5.png"
    },
    {
        "id": "krd 6",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/6.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "35 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 6.html",
        "image2": "images/krd/6.png",
        "image3": "images/krd/6.png"
    },
    {
        "id": "krd 7",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/7.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "36 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 7.html",
        "image2": "images/krd/7.png",
        "image3": "images/krd/7.png"
    },
    {
        "id": "krd 8",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/8.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "37 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 8.html",
        "image2": "images/krd/8.png",
        "image3": "images/krd/8.png"
    },
    {
        "id": "krd 9",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/9.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "38 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 9.html",
        "image2": "images/krd/9.png",
        "image3": "images/krd/9.png"
    },
    {
        "id": "krd 10",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/10.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "39 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 10.html",
        "image2": "images/krd/10.png",
        "image3": "images/krd/10.png"
    },
    {
        "id": "krd 11",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/11.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "40 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 11.html",
        "image2": "images/krd/11.png",
        "image3": "images/krd/11.png"
    },
    {
        "id": "krd 13",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/13.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "42 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 13.html",
        "image2": "images/krd/13.png",
        "image3": "images/krd/13.png"
    },
    {
        "id": "krd 14",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/14.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "43 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 14.html",
        "image2": "images/krd/14.png",
        "image3": "images/krd/14.png"
    },
    {
        "id": "krd 15",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/15.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "44 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 15.html",
        "image2": "images/krd/15.png",
        "image3": "images/krd/15.png"
    },
    {
        "id": "krd 16",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/16.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "45 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 16.html",
        "image2": "images/krd/16.png",
        "image3": "images/krd/16.png"
    },
    {
        "id": "krd 17",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/17.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "46 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 17.html",
        "image2": "images/krd/17.png",
        "image3": "images/krd/17.png"
    },
    {
        "id": "krd 18",
        "name": "Kurdistan Retro",
        "price": 24.9,
        "priority": 0,
        "type": "shirt",
        "nation": "krd",
        "image": "images/krd/18.png",
        "category": "Trikots",
        "shortDescription": "Das klassische gelbe Retro-Shirt aus Brasilien",
        "description": "Hol dir das originale Gefühl vom Zuckerhut nach Hause. Retro-Design in höchster Qualität.",
        "sizeNote": "Fällt normal aus",
        "keywords": "Brasilien",
        "related_products": "",
        "bullets": [
            "100% Baumwolle",
            "Klassischer Schnitt",
            "Retro Logo"
        ],
        "washingInstructions": [
            "47 Grad waschen"
        ],
        "colors": [
            "Schwarz",
            "Weiß",
            "Rot",
            "Blau"
        ],
        "url": "generated/product-krd 18.html",
        "image2": "images/krd/18.png",
        "image3": "images/krd/18.png"
    }
];
csvProducts.forEach(p => products.push(p));
// --- AUTO GENERATED FROM CSV END ---




























