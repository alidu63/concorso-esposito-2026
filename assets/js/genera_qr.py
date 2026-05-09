#!/usr/bin/env python3
"""
Genera i QR code per tutte le pagine del sito.

USO:
    1. Apri questo file con un editor di testo
    2. Cambia BASE_URL con l'URL pubblico del sito (es. il tuo dominio GitHub Pages)
    3. Da terminale, esegui:    python3 genera_qr.py
    4. I QR vengono salvati in ../img/qr/

Esempio di BASE_URL:
    https://mario-rossi.github.io/concorso-esposito-2026/
    https://ic-esposito-sarno.github.io/concorso-2026/
"""
import qrcode
from pathlib import Path

# ============================================================================
# CONFIGURA QUI L'URL DEL SITO PUBBLICATO
# ============================================================================
BASE_URL = "https://alidu63.github.io/concorso-esposito-2026/"
# ============================================================================

PAGES = [
    ("index", "index.html"),
    ("commissario", "commissario.html"),
    ("sarno", "sarno.html"),
    ("legalita", "legalita.html"),
    ("noi", "noi.html"),
    ("materiali", "materiali.html"),
]

OUT = Path(__file__).resolve().parent.parent / "img" / "qr"
OUT.mkdir(parents=True, exist_ok=True)

print(f"Genero QR code per: {BASE_URL}")
print(f"Output: {OUT}\n")

for name, page in PAGES:
    url = BASE_URL.rstrip("/") + "/" + page
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=14,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0E2A47", back_color="white")
    out_path = OUT / f"{name}.png"
    img.save(out_path)
    print(f"  ✓ {out_path.name}  →  {url}")

print("\nFatto.")
