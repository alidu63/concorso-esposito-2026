# Sito web — Concorso «Legalità e Ambiente» 2026

Sito statico per il concorso scolastico **«Legalità e Ambiente» 2026**, in memoria
del Commissario Antonio Esposito. Realizzato dalle classi 5ª A, 5ª B e 5ª C
dell'IC «Antonio Esposito» di Sarno (SA).

---

## Cosa contiene

```
Sito_Web_Concorso/
├── index.html                  ← home + player video + QR
├── commissario.html            ← Antonio Esposito: vita, sacrificio, memoria
├── sarno.html                  ← Fiume Sarno + frana 1998 + ecomafie
├── legalita.html               ← La «legalità ecologica» (Don Ciotti, A. Serra)
├── noi.html                    ← Le 3 promesse della classe + «era uno di noi»
├── materiali.html              ← Download di tutti gli elaborati
├── README.md                   ← questo file
└── assets/
    ├── css/style.css           ← stile «quaderno scolastico» (navy + oro)
    ├── js/main.js              ← navigazione attiva, smooth scroll
    ├── js/genera_qr.py         ← script per (ri)generare i QR code
    ├── img/illustrations/*.jpg ← frame estratti dal video NotebookLM
    ├── img/qr/*.png            ← QR code per ogni pagina (rigenerabili)
    ├── video/Video_Finale_Concorso_v5.mp4  ← video del concorso (27 MB)
    └── downloads/              ← lettera, cartellone, audio, presentazione…
```

Sito totalmente **statico** — solo HTML + CSS + un po' di JS. Nessun framework,
nessuna build, nessuna dipendenza. Funziona offline aprendo `index.html` con un
doppio click, oppure online via GitHub Pages.

---

## ⚙️ Pubblicare su GitHub Pages (5 passi)

### 1. Crea l'account GitHub (se non l'hai già)
- Vai su [github.com](https://github.com) e fai sign-up.
- Suggerimento: usa un nome account leggibile, es. `ic-esposito-sarno` o
  `cinque-elementare-sarno-2026`.

### 2. Crea un nuovo repository
- Sulla tua pagina GitHub clicca **+** in alto a destra → **New repository**.
- Nome consigliato: `concorso-esposito-2026`
- Visibilità: **Public** (necessario per Pages gratuito).
- Senza README, senza .gitignore, senza license — clicca **Create**.

### 3. Carica i file della cartella `Sito_Web_Concorso`
**Opzione A — via web** (più semplice se non sai usare git):
- Sulla pagina del nuovo repo clicca **"uploading an existing file"**.
- Trascina **tutto il contenuto** di `Sito_Web_Concorso/` (non la cartella
  esterna, ma i file dentro: `index.html`, `commissario.html`, …, `assets/`).
- Scrivi un commento tipo *"primo upload"* e clicca **Commit changes**.

**Opzione B — via terminale** (se hai git installato):
```bash
cd Sito_Web_Concorso
git init -b main
git add .
git commit -m "Sito iniziale concorso Esposito 2026"
git remote add origin https://github.com/<TUO_USERNAME>/concorso-esposito-2026.git
git push -u origin main
```

### 4. Attiva GitHub Pages
- Sul repository: **Settings** → **Pages** (nel menu a sinistra)
- *Source*: **Deploy from a branch**
- *Branch*: **main** · *Folder*: **/ (root)**
- Clicca **Save**.
- Aspetta 1–2 minuti. GitHub ti mostrerà il link tipo:
  `https://<TUO_USERNAME>.github.io/concorso-esposito-2026/`

### 5. Aggiorna i QR code col tuo URL
Una volta che il sito è online, devi rigenerare i QR perché ora puntino davvero al sito.

```bash
# Apri lo script
open assets/js/genera_qr.py
```

- Cambia la riga `BASE_URL = "https://USERNAME.github.io/concorso-esposito-2026/"`
  con il tuo URL reale (quello visto al passo 4).
- Salva, poi da terminale dentro la cartella del sito:

```bash
python3 assets/js/genera_qr.py
```

I 6 PNG dei QR vengono rigenerati in `assets/img/qr/`. **Ricaricali su GitHub** (stessi passi del 3 ma solo per quei file) e i QR funzioneranno.

---

## 🖨 Stampare i QR code

I QR sono PNG ad alta risoluzione (~700 px) — ottimi per la stampa.

Suggerimenti:
- Per attaccarli accanto al cartellone: stampa formato **8×8 cm** o più grande.
- Per metterli sotto il poster nel corridoio della scuola: **15×15 cm**.
- Stampa in bianco/nero (i QR sono già blu navy + bianco — funzionano in entrambi).

Posizioni consigliate dei QR:
- `qr/index.png` — ingresso scuola, locandina del concorso
- `qr/commissario.png` — accanto al ritratto di Antonio Esposito
- `qr/sarno.png` — accanto a un disegno del fiume Sarno
- `qr/legalita.png` — in classe, sul cartellone «Era uno di noi»
- `qr/noi.png` — accanto alle impronte di mano della classe
- `qr/materiali.png` — alla cerimonia di premiazione (per scaricare l'opera)

---

## ✏️ Modifiche

Tutto il sito è in italiano leggibile, niente codice complicato. Per modificare:

- **Testi**: apri il file `.html` con TextEdit / Notepad / VS Code, modifica
  e salva. Ricarica la pagina nel browser per vedere le modifiche.
- **Colori e font**: tutto in `assets/css/style.css`, prime righe (le
  variabili CSS `--c-navy`, `--c-gold`, ecc.).
- **Aggiungere un materiale**: copia il file in `assets/downloads/` e
  aggiungi un blocco `.material` in `materiali.html` simile agli altri.

---

## 📦 Materiali allegati

Nel sito sono già inclusi:

| File | Cosa è |
|---|---|
| `Video_Finale_Concorso_v5.mp4` | Video di 10:27 — l'elaborato multimediale completo |
| `01_Lettera_Collettiva.docx` | Lettera della classe al Commissario |
| `01_Lettera_Audio_Elsa.mp3` | Versione audio della lettera (voce Elsa neurale) |
| `02_Cartellone_Istruzioni.docx` | Istruzioni di realizzazione del cartellone |
| `03_Audio_Poesia_Copione.docx` | Copione della poesia in 6 voci |
| `Cartellone_Era_uno_di_noi.png` | Layout grafico del cartellone ufficiale |
| `Cartelloni_alternativi.zip` | Le altre 2 alternative di cartellone |
| `Le_Regole_degli_Eroi.pptx` | Presentazione PowerPoint (15 slide) |
| `Concorso_Esposito_2026_completo.zip` | Tutto il pacchetto in un solo download |

---

## ⚖️ Crediti

- Realizzazione: classi 5ª A, 5ª B, 5ª C dell'IC «Antonio Esposito» di Sarno (SA).
- In memoria del Commissario Antonio Esposito (Sarno 30/11/1942 — Genova 21/06/1978).
- Concorso «Legalità e Ambiente» — Comune di Sarno, anno 2026.
- Premiazione: 25 maggio 2026, Giornata Nazionale della Legalità.
- Patrocini: Comune di Sarno · Polizia di Stato · Ministero dell'Istruzione e del Merito.

---

## 🆘 Aiuto

Se qualcosa non va:
1. Apri `index.html` con un doppio click — il sito deve aprirsi nel browser
   anche senza internet.
2. Se i QR rimandano a `USERNAME.github.io` (placeholder), significa che
   non hai ancora rigenerato i QR (vedi passo 5 sopra).
3. Se il video non parte: verifica che `assets/video/Video_Finale_Concorso_v5.mp4`
   esista (è quello da 27 MB).
