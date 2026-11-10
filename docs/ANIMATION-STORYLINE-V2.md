# Dr. Giuseppe Colombo — Original Design & Animation Storyline (v2)

| | |
|---|---|
| **Concept** | *L'Atlante della Misura* — The Atlas of Measure |
| **Replaces** | v1 direction (ivory + bronze + the old site's orange line drawings) |
| **Keeps** | All verified content in IT / DE / EN, the site structure, the build system and Cloudflare setup |
| **Date** | 10 Nov 2026 |

---

## 1. Why a new design

The v1 build reused the **visual identity of the current website**: the doctor's orange line drawings (face, breast, eye, molecule…), the script "Dr. Colombo" logo and the circle-profile favicon. As a result it looked like a polished copy of the original.

**v2 drops all of those.** It keeps only **content and documentary material**:

| Kept from the original site | Dropped |
|---|---|
| All texts and facts (procedures, CV, quotes, contacts) | Orange line drawings (all 15) |
| Doctor's photographs (Portrait A, Portrait B) | Script "Dr. Colombo" logo |
| Books: Springer *Stepwise Atlas*; *Atlante iconografico* | Circle-profile favicon |
| Papers: 19 publications, journals, years | Orange/terracotta colour |
| Event images: 12 course posters + 3 programme sheets | WordPress layout patterns |
| 9 YouTube videos, 11 journal articles | |

The new identity is built from scratch: palette, typography, monogram, motion language and storyline.

---

## 2. Concept: *L'Atlante della Misura*

Dr. Colombo's story rests on three facts from his own material:

1. **Measure.** *"Il giusto è il più bello. Odia l'eccesso, rispetta il limite."*
2. **Anatomy.** Dissection courses, a thesis on the SMAS, and his own texts describing the face in **thirds** (*terzo superiore, medio, inferiore*).
3. **The atlas.** He is the editor of an atlas organised as a step-by-step sequence of plates.

So the website itself becomes **an atlas of measure**:

- The homepage is divided into **Plates (Tavole I–VIII)**, like the chapters of a surgical atlas.
- The visual language is that of **precision instruments**: rulers, millimetre ticks, coordinates, the surgeon's dashed marking line and suture lines.
- Everything is *measured*, nothing is *excessive*. Motion is exact, short and calm.

> One sentence for the client: *"Your site will feel like opening a beautifully printed surgical atlas — where every element is measured, and nothing is excessive."*

---

## 3. Colour: *Bordeaux & Bone*

The palette comes from the doctor's **own photographs**. In his portraits he wears **bordeaux scrubs against a black background**. Instead of fighting that colour (v1 had to turn the photos black-and-white), v2 makes it the brand. Bordeaux is Italian, warm and luxurious (wine, velvet, Italian couture), and it suggests medicine without looking clinical.

| Token | Hex | Role |
|---|---|---|
| `--bone` | `#F3EDE5` | Main light background (warm, skin-adjacent paper) |
| `--linen` | `#E7DED2` | Alternate light sections, cards |
| `--ink` | `#1B1517` | Text (warm near-black with a red undertone) |
| `--mauve` | `#6E5B5E` | Secondary text, captions |
| `--bordeaux` | `#5C1A2B` | **Brand colour**: headlines on light, buttons, chapter fields |
| `--night` | `#21090F` | Deep sections (hero, discretion, footer) |
| `--champagne` | `#C9A56B` | Fine lines, rulers, numerals, accents on dark |
| `--rose` | `#D9C2BC` | Soft text on dark, hover tints |
| `--lake` | `#2F4A50` | Used **only** in the Lugano plate (dusk over the lake) |

**Contrast (checked):**

| Pair | Ratio | Use |
|---|---|---|
| ink on bone | 15.5 : 1 | body text |
| bordeaux on bone | 11.0 : 1 | headlines, links |
| mauve on bone | 5.4 : 1 | captions (AA) |
| bone on night | 16.3 : 1 | text on dark |
| champagne on night | 8.2 : 1 | numerals, labels on dark |
| champagne on bordeaux | 5.5 : 1 | labels on bordeaux |
| champagne on bone | 2.0 : 1 | **lines only — never text** |

**Rules**
- Light plates use bone and ink, with bordeaux headlines.
- Dark plates use night, with champagne detail.
- Bordeaux appears as **full colour fields** only at chapter transitions (curtain wipes).
- Champagne is always thin: 1 px rules, tick marks, numerals. Never use it for blocks.

---

## 4. Typography

| Role | Font | Why |
|---|---|---|
| Display | **Bodoni Moda** (OFL, variable optical size) | Bodoni was born in **Parma**: Italian typographic heritage, high-contrast, couture-like |
| Text | **Instrument Sans** (OFL) | Clean and contemporary; neutral next to Bodoni |
| Measure / labels | **IBM Plex Mono** (OFL) | Plate numbers, coordinates, millimetres, dates: the "instrument" voice |

- **Display sizes:** `clamp(56px, 9vw, 160px)`; italic for one key word per headline (*bello*, *limite*, *misura*).
- **Labels:** in mono, uppercase, 11–12 px, letter spacing 0.12em, e.g. `TAV. III — SENO`, `46.0037° N`.
- All fonts are self-hosted, like v1, with no Google requests.

**Monogram:** a new **"GC"** set in Bodoni Moda italic between two champagne tick marks: `| GC |`. It works like a measured interval and is used in the header, favicon and loader. It owes nothing to the old script logo.

---

## 5. Signature devices (the visual vocabulary)

| # | Device | What it is | Where |
|---|---|---|---|
| D1 | **The Ruler** | A fixed vertical millimetre ruler on the left edge. A champagne marker travels down it as you scroll; chapter ticks I–VIII are labelled; clicking a tick jumps there. The whole homepage is "100 mm" long. | Whole homepage (desktop); a thin top bar with a `mm` counter on mobile |
| D2 | **Facial thirds** | Three horizontal lines that divide the doctor's real portrait into *terzo superiore / medio / inferiore* | Plates I & II, face procedure pages |
| D3 | **The marking line** | A dashed bordeaux line that draws itself, like a surgeon's pre-operative marking (his eyelid article describes marking before surgery) | Section dividers, underlines, hover states |
| D4 | **The suture** | A dashed line that "stitches" closed: cross-stitches appear one by one along it | Plate IV (reconstructive) |
| D5 | **Tape measure** | A horizontal tape with numbers that slides past | Plate III (breast) |
| D6 | **Coordinates** | Latitude and longitude counting to the real values | Lugano plate, contact page |
| D7 | **Plate labels** | `TAV. I`, `FIG. 2`, captions like a printed atlas | Every section |

---

## 6. Asset inventory (all from the original website)

**Doctor images**
- `portrait-a` — serious, chin on hands, bordeaux scrubs, black background. The **hero**, facial-thirds plate and About.
- `portrait-b` — smiling, hands on cheeks. Used once, in Plate VII-bis "the person" and on the About page.
- Programme sheets `13.35.15`, `13.35.51` and `13.36.43` include small photos of Dr. Colombo with Dr. Vittorio Ruvolo at the courses. Used as **documentary detail** in the teaching plate.

**Books**
- *Stepwise Atlas of Aesthetic Medicine and Surgery* (Springer, editor): cover, more than 320 original photographs, two sections (theory and practice).
- *Atlante iconografico di chirurgia e medicina estetica — I fondamenti step by step* (eds. G. Colombo, V. Ruvolo): cover.

**Papers**: 19 publications (2008–2021, plus undated experimental studies) in journals including *Aesthetic Plastic Surgery*, *Minerva Ginecologica*, *Plastic and Aesthetic Research*, *JPD Journal*, *FASEB Journal* and *Italian Journal of Plastic Surgery*. He also reviews for 5 journals.

**Event images** (chronological)

| Year | City | Event | Image |
|---|---|---|---|
| 2013 | Savona | Biennale di Chirurgia Morfodinamica (co-president) | `poster-2013-biennale` |
| 2015 | Nice | KORU — face course (3–4 Feb) | `poster-2015-face` |
| 2015 | Nice | KORU — breast course (5–6 Feb) | `poster-2015-breast` |
| 2015 | Nice | Abdominal surgical anatomy (6 Feb) | `poster-2015-abdomen` |
| 2015 | Nice | Sutures on cadaver (6 Feb) | `poster-2015-sutures` |
| 2017 | Nice | Practical course, aesthetic medicine | `poster-2017-aesthetic` |
| 2018 | Nice | Cadaver lab — facelift & blepharoplasty | `poster-2018-face` |
| 2018 | Nice | Cadaver lab — rhinoplasty | `poster-2018-rhino` |
| 2018 | Nice | Cadaver lab — breast & gluteoplasty | `poster-2018-breast` |
| 2024 | Cremona | Face anatomy & rejuvenation (9–10 May) | `poster-2024-face` |
| 2024 | Cremona | Nasal pyramid & rhinoplasty (10 May) | `poster-2024-nose` |
| 2024 | Cremona | Aesthetic medicine live dissection (8 June) | `poster-2024-aesthetic` |

Earlier courses: Nice and Madrid, 2010–2012 (from the CV).

**Video**: 9 videos from his YouTube channel.

---

## 7. The animation storyline — homepage, plate by plate

Scroll lengths are in screen heights (vh). Total ≈ **1,500 vh** desktop, about 75–100 seconds. Every scene names its **shot**, its **motion**, its **assets** and the **source of its copy**.

```
Emotion
  ▲                         ● V Atlas & papers (respect)
  │  ● Hero (presence)                  ● VI Teaching (momentum)      ● VIII Lugano (desire)
  │         ● I Measure (insight)
  │                ● II Face    ● IV Restore                ● VII Discretion
  │                     ● III Breast                          (stillness)          ● Finale (intimacy)
  └──────────────────────────────────────────────────────────────────────────────────▶ 0 → 100 mm
```

---

### 0 · Loader: "Calibrating" (≤ 1.2 s, first visit only)
- **Shot:** night screen; a champagne ruler at the centre fills from `0` to `100 mm` while the counter runs in mono.
- **End:** the `| GC |` monogram snaps between the two final ticks, then a bordeaux curtain lifts upward to reveal the hero.
- **Skipped** on later visits in the same session and when the visitor prefers reduced motion.

### Hero · *Il giusto è il più bello.* (100 vh, auto-play then scrub)
- **Shot:** the night field. The doctor (Portrait A) stands centre-right; his bordeaux scrubs merge with the palette.
- **Motion:**
  1. 0.2 s — a **1 px vertical slit of light** appears where the portrait will be.
  2. 0.4–1.6 s — the slit **opens like an aperture** to reveal the full portrait, with a slow scale from 1.12 to 1.
  3. 0.9 s — the headline rises line by line in Bodoni (bone), with *bello* in champagne italic.
  4. 1.6 s — **rulers draw along two edges of the portrait** with tick marks; a mono caption reads `FIG. 1 — Dr. Giuseppe Colombo, Lugano`.
  5. 2.0 s — the left-edge **Ruler (D1)** slides in, its marker at `0 mm · TAV. —`.
- **On scroll:** the portrait drifts up more slowly than the text (parallax) and the headline fades.
- **Copy:** his quote (IT original, translated line in DE and EN); "Plastic surgery of the face and breast · Lugano · Zürich · Italia".

### TAV. I · *La misura*: philosophy (pinned 220 vh)
- **Transition:** a bordeaux curtain wipes up and the field turns **bone**: from night to day.
- **Shot:** Portrait A on the left, now on a linen card; text on the right.
- **Timeline:**

| Progress | Motion | Text |
|---|---|---|
| 0–20% | Three champagne **thirds lines (D2)** draw across his face: hairline–brow–nose base–chin | `TERZO SUPERIORE · MEDIO · INFERIORE` labels type in (mono) |
| 20–45% | Measurement brackets appear between the lines, with "1 : 1 : 1" | *"Odia l'eccesso, rispetta il limite."* rises (Bodoni, bordeaux) |
| 45–75% | The lines **relax and fade**; the portrait stays, unmeasured | *"Solo una parola guida la mia pratica: naturalezza."* |
| 75–100% | The marking line (D3) underlines *naturalezza* | "Meet Dr. Colombo →" |

- **Message:** *measure first, then restraint.* The thirds come straight from his texts (the facelift acts on the lower third; botulinum toxin on the upper third).

### TAV. II · *Viso*: the face, by thirds (pinned 260 vh)
- **Shot:** the portrait stays sticky on the left, with the thirds lines back on. On the right is a list of treatments that changes by third.
- **Timeline:** scrolling moves the highlighted band (a soft bordeaux tint over that third):

| Third | Highlight | Treatments listed (from his texts) |
|---|---|---|
| Upper | forehead, brow, eyes | Blefaroplastica · Lifting del sopracciglio · Tossina botulinica |
| Middle | cheeks, nose, upper lip | Acido ialuronico · Biorivitalizzazione · Lip-lifting |
| Lower + neck | jaw, chin, neck | Lifting cervico-facciale · Mentoplastica |
| (lateral) | ear | Otoplastica |

- Each treatment name is a link. On hover, a dashed marking line (D3) draws under it and a one-line summary (from the procedure lede) appears.
- **Mobile:** the portrait shrinks to a strip at the top and the thirds become three tabs.

### TAV. III · *Seno*: the breast (pinned 180 vh)
- **Shot:** typographic, with **no body imagery** (discreet and original). Bone background.
- **Motion:**
  - A **tape measure (D5)** slides horizontally across the middle of the screen as you scroll.
  - Four large Bodoni numerals and words lock into place one by one, each with its procedure:

| Lock-in | Big figure | Procedure | Source |
|---|---|---|---|
| 1 | **↑** "Riposizionare" | Mastopessi | his text: corrects pregnancy, breastfeeding, weight loss, ageing |
| 2 | **+** "Volume, con misura" | Mastoplastica additiva | his quote: fashion must never condition the decision |
| 3 | **4–5** "taglie in meno" | Mastoplastica riduttiva | his text: reduction of 4–5 sizes |
| 4 | **20–40** "anni" | Ginecomastia | his text: men aged 20–40 |

- **End:** the tape stops exactly at its centre mark and the CTA "Scopri →" appears.

### TAV. IV · *Ricostruire*: reconstructive (120 vh)
- **Transition:** linen field.
- **Shot:** one long **suture line (D4)** crosses the screen diagonally.
- **Motion:** as you scroll, the cross-stitches close one by one from left to right, and the four techniques appear along it as stations: *innesti · lembi · autotrapianti · microchirurgia*.
- **Copy:** his own words: *"mi occupo esclusivamente di ricostruzioni del distretto facciale post chirurgia oncologica cutanea."*

### TAV. V · *L'Atlante e le pubblicazioni*: books & papers (pinned 240 vh)
- **Transition:** curtain to **night**.
- **Shot A — the book (0–55%):**
  - The Springer Atlas floats in 3D and rotates from −35° to −8° with scroll.
  - At 25% the **cover swings open**. Inside, a champagne counter runs from `0` to `320+` *"fotografie originali"*.
  - Labels slide out: `PARTE I — TEORIA`, `PARTE II — PRATICA`.
  - The older *Atlante iconografico* appears behind it, smaller, as "the first edition of the idea".
- **Shot B — the papers (55–100%):**
  - The book slides left. On the right a **journal index** scrolls upward like a printed contents page: year · title · journal in mono and serif, all 19 papers.
  - Counters lock: `19 pubblicazioni · 2008 → 2021 · 5 riviste come reviewer`.
- **Copy:** Atlas description (his page), publication list (his CV).

### TAV. VI · *Insegnare*: teaching & events (pinned horizontal 300 vh)
- **Shot:** a **horizontal film strip** of the 12 course posters in chronological order, moving sideways as you scroll down. Below it, a **minimal map** with exact city dots: Savona, Nice, Madrid, Cremona, Lugano.
- **Motion:**
  - As each poster passes the centre, it straightens from 4° tilt to 0, its date and city type in, and its **city dot pulses** on the map.
  - A champagne **arc draws** from the previous city to the next: Madrid 2011 → Nice 2015 → … → Cremona 2024 → Lugano.
  - The programme sheets with the photos of Colombo and Ruvolo appear as small inset "documents".
- **End:** "Fellowship — metà viso, metà seno" card with `formazione@drgiuseppecolombo.com`.
- **Mobile:** a vertical stack of posters with the map at the top.

### TAV. VII · *Discrezione*: stillness (100 vh)
- **Shot:** the **night** field, nearly empty.
- **Motion:** **everything stops, including the Ruler's marker**. Only the quote fades in over 2 s:
  > *"Un professionista serio non rivela mai chi sono i suoi pazienti. Diffida da chi lo fa."*
- After it, a small Portrait B (smiling) fades in at low opacity: the human warmth behind the rule.

### TAV. VIII · *Lugano*: the place (pinned 180 vh)
- **Shot:** a full-screen **colour field** with no illustration: a slow gradient from night to bordeaux to **lake** at dusk, with fine champagne horizontal lines like water reflections.
- **Motion:**
  - Huge Bodoni "**Lugano**" rises.
  - Below it, coordinates count up in mono to `46.0037° N · 8.9511° E`.
  - The gradient shifts toward lake blue as you scroll (dusk).
  - Three coordinate cards then lock in:
    - **Lugano**: *Clinica Sant'Anna — studio e sala operatoria* · `46.00° N 8.95° E`
    - **Zürich**: *consulenze chirurgiche, su appuntamento* · `47.37° N 8.54° E`
    - **Italia**: *consulenze, su appuntamento*
- **Copy:** original contact data (to be confirmed by the client).

### Finale · *Inizia con una conversazione* (100 vh)
- **Shot:** bone field, quiet and intimate.
- **Motion:**
  - The Ruler's marker reaches **100 mm** and the ruler folds away.
  - The headline rises and a bordeaux marking line (D3) underlines *conversazione*.
  - Three location buttons appear; each opens the booking panel with that location pre-selected.
- **Footer** (night): the `| GC |` monogram, contacts, the **IT · DE · EN** switcher and the Lugano clock.

---

## 8. Motion system

| Token | Value | Use |
|---|---|---|
| Ease "measure" | `cubic-bezier(0.65, 0, 0.35, 1)` | Rulers, lines, curtains: precise, symmetric |
| Ease "settle" | `cubic-bezier(0.16, 1, 0.3, 1)` | Text and images arriving |
| Line draw | 0.9–1.4 s | Rulers, thirds, marking lines |
| Text rise | 1.0 s, 70 ms stagger per line | Headlines (mask reveal) |
| Curtain | 0.9 s | Chapter transitions (bordeaux) |
| Counters | 1.2–1.6 s, ease-out | 320+, coordinates, mm |

**Rules**
1. **Measure, then stop.** Every animation ends in an exact resting state; nothing loops except the loader.
2. **One instrument per plate.** Ruler, thirds, tape, suture, map or coordinates; never two at once.
3. **Scroll is the timeline.** Story motion is scrubbed; hover feedback is under 0.4 s.
4. **Stillness is a scene** (Plate VII).
5. **Reduced motion:** all plates render in their final measured state, pins are removed, and counters show their final values.
6. **Mobile:** pins are shortened by about 40%, the Ruler becomes a top progress bar with a `mm` counter, the horizontal film strip becomes vertical, and the 3D book becomes a flat open spread.

---

## 9. Inner pages: the same language

| Page | Signature motion |
|---|---|
| **Procedure (face)** | A mini portrait with the thirds; the third that this procedure treats is highlighted. Facts appear as an atlas table with millimetre-tick separators. |
| **Procedure (breast)** | A tape-measure divider; key numbers (sizes, ages, recovery) count up. |
| **Reconstructive** | A suture line closes as the techniques appear. |
| **Filosofia** | Portrait A with a slit reveal; the CV as an atlas index (`TAV.` numbered sections); the milestones run along a horizontal **ruler timeline** from 1999 to today. |
| **Academy** | The book opening, the journal index, the poster film strip and the map, as full sections. |
| **Journal** | Articles as "plates" with figure numbers; a champagne reading ruler at the top. |
| **Contatti** | Coordinate cards and the booking panel. The map still loads only on request. |
| **Page transitions** | A bordeaux curtain wipe carrying the `| GC |` monogram (0.6 s). |

---

## 10. Implementation plan (on the existing project)

| Step | Work |
|---|---|
| 1 | New tokens and fonts (Bodoni Moda, Instrument Sans, IBM Plex Mono, self-hosted); remove line drawings, script logo and old favicon; new `| GC |` monogram and favicon |
| 2 | Components: Ruler (D1), Thirds overlay (D2, positions measured on Portrait A), marking line (D3), suture (D4), tape (D5), coordinates counter (D6), 3D book, journal index, poster film strip, city map |
| 3 | New `home.html` + `home.js`: hero and Plates I–VIII as above |
| 4 | Inner pages restyled with the new devices |
| 5 | Same content files for IT / DE / EN; new UI strings for plate labels |
| 6 | QA: desktop and mobile screenshots, reduced motion, contrast, link check |
| 7 | Push to `LEarnX-Official/colombo`; Cloudflare redeploys automatically |

**To confirm with the client:** the bordeaux palette (an alternative exists: *Lake & Sand*, deep teal `#1F3A40` + sand `#EADFCF` + copper `#B0703F`); permission to show the course posters and the photos of colleagues on the programme sheets; and the contact data.
