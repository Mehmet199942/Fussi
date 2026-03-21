import os

BASE_DIR = r"C:\Users\mehme\Desktop\cozastore-master"

PRODUCTS = [
    {
        "file": "product-efrin-shirt.html",
        "title": "EFRÎN T-Shirt | WORLD CUP SHOP",
        "name": "EFRÎN T-Shirt",
        "price": "34.99",
        "sku": "KRD-EFRIN-SHIRT",
        "category": "Kurdistan Collection",
        "short_desc": "Statement-Shirt für stolze Kurdinnen und Kurden weltweit – EFRÎN in den Farben der Kurdistan-Flagge.",
        "long_desc": "Das EFRÎN T-Shirt ist mehr als nur Kleidung – es ist ein Statement. Der Name EFRÎN, geschrieben in den leuchtenden Farben der Kurdistan-Flagge (Rot, Weiß, Grün und Gold), erinnert an eine der ältesten und schönsten Städte Kurdistans.",
        "bullets": [
            "Design: EFRÎN Schriftzug in Kurdischen Flaggenfarben",
            "Erhältlich in 4 Farben: Schwarz, Weiß, Rot, Blau",
            "Material: 85% Baumwolle, 15% Polyester",
            "Athletischer Schnitt mit kontrastierenden Schulterstreifen",
            "Atmungsaktiv &amp; hautfreundlich",
            "Unisex-Passform – ideal für Damen und Herren",
        ],
        "washing": [
            "Maschinenwäsche bei max. 30°C",
            "Nicht bleichen",
            "Nicht Tumbletrocknen",
            "Bügeln bei niedriger Temperatur",
        ],
        "image1": "images/efrin-shirt.png",
        "image2": "images/efrin-shirt.png",
        "image3": "images/efrin-shirt.png",
        "loyalty_points": "209",
    },
    {
        "file": "product-krd-flag-shirt.html",
        "title": "Kurdistan Flaggen T-Shirt | WORLD CUP SHOP",
        "name": "Kurdistan Flaggen T-Shirt",
        "price": "29.99",
        "sku": "KRD-FLAG-SHIRT",
        "category": "Kurdistan Collection",
        "short_desc": "Klassisches T-Shirt mit gesticktem Kurdistan-Flaggen-Patch – zeitlos, stolz und hochwertig.",
        "long_desc": "Das Kurdistan Flaggen T-Shirt vereint sportlichen Stil mit kultureller Identität. Das gestickte Kurdistan-Flaggen-Patch auf der Brust ist ein dezentes, aber kraftvolles Symbol für Stolz und Zugehörigkeit.",
        "bullets": [
            "Design: Gesticktes Kurdistan-Flaggen-Patch auf der Brust",
            "Erhältlich in 4 Farben: Schwarz, Weiß, Rot, Blau",
            "Material: 100% Baumwolle (Premium-Qualität)",
            "Klassischer Rundhalsausschnitt mit Kontrastpaspel",
            "Athletischer Schnitt mit Schulterstreifen",
            "Weich, atmungsaktiv und langlebig",
        ],
        "washing": [
            "Maschinenwäsche bei max. 30°C",
            "Nicht bleichen",
            "Nicht Tumbletrocknen",
            "Bei Bedarf auf links bügeln",
        ],
        "image1": "images/krd/2.png",
        "image2": "images/krd/2.png",
        "image3": "images/krd/2.png",
        "loyalty_points": "179",
    },
    {
        "file": "product-krd-map-shirt.html",
        "title": "Kurdistan Karte T-Shirt | WORLD CUP SHOP",
        "name": "Kurdistan Karte T-Shirt",
        "price": "34.99",
        "sku": "KRD-MAP-SHIRT",
        "category": "Kurdistan Collection",
        "short_desc": "Eindrucksvolles T-Shirt mit der Kurdistan-Karte, Flagge und Freiheitssymbolen – für jeden Kurden, der seinen Wurzeln treu bleibt.",
        "long_desc": "Das Kurdistan Karte T-Shirt zeigt ein kraftvolles Design: Die Karte Kurdistans mit der Kurdistan-Flagge, der strahlenden Sonne, einer weißen Friedenstaube und einer jubelnden Menge. Dieses Shirt ist ein Statement für Frieden, Freiheit und kulturelle Identität.",
        "bullets": [
            "Design: Kurdistan-Karte mit Flagge, Sonne und Freiheitssymbolen",
            "Schriftzug: KURDISTAN in Großbuchstaben",
            "Erhältlich in 4 Farben: Schwarz, Weiß, Rot, Blau",
            "Material: 85% Baumwolle, 15% Polyester",
            "Sportlicher Schnitt mit Schulterstreifen",
            "Hochauflösender Digitaldruck – farbintensiv und langlebig",
        ],
        "washing": [
            "Maschinenwäsche bei max. 30°C, links waschen",
            "Nicht bleichen",
            "Nicht Tumbletrocknen",
            "Bei niedriger Temperatur bügeln (nicht auf Druck)",
        ],
        "image1": "images/krd/3.png",
        "image2": "images/krd/3.png",
        "image3": "images/krd/3.png",
        "loyalty_points": "209",
    },
    {
        "file": "product-krd-number10.html",
        "title": "Kurdistan #10 Trikot | WORLD CUP SHOP",
        "name": "Kurdistan #10 Trikot",
        "price": "39.99",
        "sku": "KRD-NUMBER10-JERSEY",
        "category": "Kurdistan Trikots",
        "short_desc": "Offiziell inspiriertes Kurdistan-Trikot mit der ikonischen Nummer 10 und der Kurdistan-Flagge – für echte Fans auf und neben dem Spielfeld.",
        "long_desc": "Das Kurdistan #10 Trikot ist das perfekte Fanshirt für jeden Kurdistanfan. Die Nummer 10 – die Rückennummer der Legenden – kombiniert mit der Kurdistan-Flagge macht dieses Trikot zu einem echten Eyecatcher. Geeignet für Sport, Freizeit und Fan-Events.",
        "bullets": [
            "Design: Nummer 10 mit Kurdistan-Flagge",
            "Offiziell inspiriertes Sportdesign",
            "Erhältlich in 4 Farben: Schwarz, Weiß, Rot, Blau",
            "Material: 100% Polyester (Sportmesh)",
            "Atmungsaktiv &amp; feuchtigkeitsableitend",
            "Leicht und schnelltrocknend – ideal für Sport",
        ],
        "washing": [
            "Maschinenwäsche bei max. 30°C",
            "Nicht bleichen",
            "Nicht Tumbletrocknen",
            "Nicht bügeln auf den Druck",
        ],
        "image1": "images/krd/10.png",
        "image2": "images/krd/10.png",
        "image3": "images/krd/10.png",
        "loyalty_points": "239",
    },
    {
        "file": "product-krd-text-shirt.html",
        "title": "Kurdistan Text T-Shirt | WORLD CUP SHOP",
        "name": "Kurdistan Text T-Shirt",
        "price": "29.99",
        "sku": "KRD-TEXT-SHIRT",
        "category": "Kurdistan Collection",
        "short_desc": "Klares Statement mit großem KURDISTAN-Schriftzug und Flaggen-Patch – für alle, die ihren Stolz offen zeigen.",
        "long_desc": "Das Kurdistan Text T-Shirt spricht für sich: Großer KURDISTAN-Schriftzug auf der Brust, kombiniert mit dem markanten Kurdistan-Flaggen-Patch. Schlicht, stark und unverwechselbar – perfekt für den Alltag und besondere Anlässe.",
        "bullets": [
            "Design: Großer KURDISTAN Schriftzug + Flaggen-Patch",
            "Schrift in Rot für maximale Ausdruckskraft",
            "Erhältlich in 4 Farben: Schwarz, Weiß, Rot, Blau",
            "Material: 90% Baumwolle, 10% Polyester",
            "Entspannter Schnitt mit Schulterstreifen",
            "Weicher Griff, hautfreundlich und langlebig",
        ],
        "washing": [
            "Maschinenwäsche bei max. 30°C",
            "Nicht bleichen",
            "Nicht Tumbletrocknen",
            "Bügeln bei niedriger Temperatur",
        ],
        "image1": "images/krd/1.png",
        "image2": "images/krd/1.png",
        "image3": "images/krd/1.png",
        "loyalty_points": "179",
    },
]

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
	<title>{title}</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="{short_desc}">
	<link rel="icon" type="image/png" href="images/icons/favicon.png" />
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="fonts/iconic/css/material-design-iconic-font.min.css">
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
	<link rel="stylesheet" type="text/css" href="vendor/animsition/css/animsition.min.css">
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
	<link rel="stylesheet" type="text/css" href="vendor/slick/slick.css">
	<link rel="stylesheet" type="text/css" href="vendor/MagnificPopup/magnific-popup.css">
	<link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
	<link rel="stylesheet" type="text/css" href="css/custom.css?v=3">
	<style>
		.header-v4 .wrap-menu-desktop, .header-v4 .top-bar {{ background-color: #000000 !important; }}
		
		/* ======= DESKTOP SPLIT-SCREEN LAYOUT ======= */
		@media (min-width: 992px) {{
			.sec-product-detail {{ padding: 0 !important; }}
			.sec-product-detail > .container {{ max-width: 100% !important; padding: 0 !important; margin: 0 !important; }}
			.sec-product-detail > .container > .row {{ display: flex; flex-direction: row; min-height: 100vh; margin: 0 !important; }}

			/* LEFT Panel */
			.sec-product-detail > .container > .row > div:first-child {{
				flex: 0 0 55%; max-width: 55%; padding: 0 !important; position: sticky; top: 0; height: 100vh; overflow: hidden;
			}}
			.sec-product-detail .wrap-pic-w img {{ width: 100%; height: 100vh; object-fit: cover; }}
			.sec-product-detail .wrap-slick3-dots-pd {{ display: none !important; }}

			/* RIGHT Panel */
			.sec-product-detail > .container > .row > div:last-child {{
				flex: 0 0 45%; max-width: 45%; overflow-y: auto; height: 100vh; padding: 0 !important; background: #000; display: flex; align-items: center; justify-content: center;
			}}
			.sec-product-detail .product-info-panel-inner {{ width: 100%; max-width: 500px; margin: 0 auto; padding: 120px 20px 50px 20px !important; }}

			/* Typography Redesign */
			.detail-name-price-wrapper {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 20px; margin-bottom: 12px; }}
			#detail-product-name {{ font-size: 36px !important; line-height: 1.15 !important; letter-spacing: -1px !important; margin-bottom: 0 !important; font-family: Poppins-Bold, sans-serif !important; flex: 1; }}
			#detail-product-price {{ font-size: 28px !important; color: #eee !important; white-space: nowrap; padding-top: 6px; }}
			.detail-rating-row {{ margin-bottom: 16px; font-size: 15px !important; }}
			#detail-product-description {{ font-size: 15px !important; color: #aaa !important; line-height: 1.6 !important; }}
			.size-item {{ min-width: 48px !important; height: 48px !important; font-size: 15px !important; }}
			.btn-add-to-bag {{ font-size: 15px !important; height: 48px !important; width: 100% !important; }}
			
			/* Icon positioning overrides */
			.how-pos1 {{ left: 10px !important; right: auto !important; }}
			.product-badge-new {{ right: 10px !important; left: auto !important; }}
		}}
	</style>
</head>
<body class="animsition dark-mode dark-product-detail">

<header class="header-v4">
	<div class="container-menu-desktop">
		<div class="top-bar">
			<div class="content-topbar flex-sb-m h-full container" style="justify-content:space-between;font-family:Poppins-Medium;">
				<div class="left-top-bar" style="color:white;font-size:11px;">Höchste Qualität seit 2018</div>
				<div class="right-top-bar flex-w h-full">
					<div class="flex-c-m trans-04 p-lr-25" style="color:white;border:none;font-size:11px;">Internationaler Versand</div>
				</div>
			</div>
		</div>
		<div class="wrap-menu-desktop how-shadow1">
			<nav class="limiter-menu-desktop container">
				<a href="index.html" class="logo"><img src="images/icons/logo-new.png" alt="WORLD CUP SHOP"></a>
				<div class="menu-desktop"><ul class="main-menu js-desktop-nations"></ul></div>
			</nav>
		</div>
	</div>
</header>

<section class="sec-product-detail bg0">
	<div class="container">
		<div class="row">
			<div class="col-md-6 col-lg-7">
				<div class="wrap-slick3-pd">
					<div class="slick3-pd">
						<div class="item-slick3-pd" data-thumb="{image1}">
							<div class="wrap-pic-w pos-relative">
								<img src="{image1}" alt="{name}">
								<a class="flex-c-m size-108 how-pos1 bor0 fs-16 cl10 bg0 hov-btn3 trans-04" href="{image1}">
									<i class="fa fa-expand"></i>
								</a>
							</div>
						</div>
						<div class="item-slick3-pd" data-thumb="{image2}">
							<div class="wrap-pic-w pos-relative">
								<img src="{image2}" alt="{name}">
								<a class="flex-c-m size-108 how-pos1 bor0 fs-16 cl10 bg0 hov-btn3 trans-04" href="{image2}">
									<i class="fa fa-expand"></i>
								</a>
							</div>
						</div>
						<div class="item-slick3-pd" data-thumb="{image3}">
							<div class="wrap-pic-w pos-relative">
								<img src="{image3}" alt="{name}">
								<a class="flex-c-m size-108 how-pos1 bor0 fs-16 cl10 bg0 hov-btn3 trans-04" href="{image3}">
									<i class="fa fa-expand"></i>
								</a>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="col-md-6 col-lg-5">
				<div class="product-info-panel-inner">
					<div class="detail-name-price-wrapper">
						<h4 id="detail-product-name">{name}</h4>
						<span id="detail-product-price">€{price}</span>
					</div>
					<div class="detail-rating-row">★★★★★ 4.8 (47 Reviews)</div>
					<p id="detail-product-description">{short_desc}</p>
					<div class="p-t-33">
						<div class="size-grid" style="display:flex;gap:10px;margin-bottom:20px;">
							<div class="size-item">S</div><div class="size-item active">M</div><div class="size-item">L</div><div class="size-item">XL</div>
						</div>
						<button class="btn-add-to-bag">IN DEN WARENKORB LEGEN</button>
					</div>
				</div>
			</div>
		</div>
		<div class="p-t-50 p-b-50" style="max-width:800px;margin:0 auto;">
			<h4 style="font-weight:700;margin-bottom:15px;">BESCHREIBUNG</h4>
			<p>{long_desc}</p>
			<ul style="list-style:disc;padding-left:20px;margin-top:10px;">{bullets}</ul>
		</div>
	</div>
</section>

<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<script src="vendor/slick/slick.min.js"></script>
<script>
	$(document).ready(function () {{
		$('.slick3-pd').slick({{ slidesToShow: 1, slidesToScroll: 1, fade: true, dots: true }});
	}});
</script>
<script src="js/main.js"></script>
</body>
</html>"""

for p in PRODUCTS:
    bullets_html = "\n".join(f"\t\t\t\t\t\t<li>{item}</li>" for item in p["bullets"])
    washing_html = "\n".join(f"\t\t\t\t\t\t\t<li>{item}</li>" for item in p["washing"])

    html = PAGE_TEMPLATE.format(
        title=p["title"],
        name=p["name"],
        price=p["price"],
        sku=p["sku"],
        category=p["category"],
        short_desc=p["short_desc"],
        long_desc=p["long_desc"],
        image1=p["image1"],
        image2=p["image2"],
        image3=p["image3"],
        loyalty_points=p["loyalty_points"],
        bullets=bullets_html,
        washing=washing_html,
    )

    filepath = os.path.join(BASE_DIR, p["file"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {p['file']}")

print("Done!")
