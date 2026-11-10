"""
All site content.

Every fact here comes from the original drgiuseppecolombo.com (pages, CV, journal
articles, course posters), translated faithfully from the Italian originals.
Nothing medical has been invented: "facts" blocks only appear where the doctor's
own texts state them.
"""

SITE = {
    "name": "Dr. Giuseppe Colombo",
    "title_suffix": "Dr. Giuseppe Colombo · Plastic Surgery",
    "role": "Specialist in Plastic, Reconstructive and Aesthetic Surgery · Ph.D., University of Genoa",
    "url": "https://www.drgiuseppecolombo.com",
    "email": "info@drgiuseppecolombo.com",
    "email_training": "formazione@drgiuseppecolombo.com",
    "phones": [
        {"label": "Switzerland", "display": "+41 76 297 69 87", "tel": "+41762976987"},
        {"label": "Italy", "display": "+39 342 327 5364", "tel": "+393423275364"},
    ],
    "hours": "Monday to Friday, 10:00–18:00",
    "locations": [
        {
            "key": "lugano",
            "city": "Lugano",
            "country": "Switzerland",
            "role": "Practice & operating theatre",
            "lines": ["Clinica Sant'Anna", "Via Sant'Anna 1"],
            "extra": "Practice: Via Nassa 7 · Via Clemente Maraini 8",
        },
        {
            "key": "zurich",
            "city": "Zurich",
            "country": "Switzerland",
            "role": "Surgical consultations",
            "lines": ["By appointment"],
            "extra": "",
        },
        {
            "key": "italy",
            "city": "Italy",
            "country": "",
            "role": "Consultations",
            "lines": ["By appointment"],
            "extra": "",
        },
    ],
    "social": [
        {"name": "Instagram", "url": "https://www.instagram.com/drgiuseppecolombo/"},
        {"name": "LinkedIn", "url": "https://www.linkedin.com/in/giuseppe-colombo-aa873217b/"},
        {"name": "YouTube", "url": "https://www.youtube.com/channel/UCkqkRZ4UNGxubDt0YGGaI9w"},
    ],
    "map_query": "Clinica Sant'Anna, Via Sant'Anna 1, Lugano",
}

NAV = [
    {"label": "Philosophy", "href": "/philosophy/"},
    {"label": "Face", "href": "/face/"},
    {"label": "Breast", "href": "/breast/"},
    {"label": "Academy", "href": "/academy/"},
    {"label": "Contact", "href": "/contact/"},
]

QUOTES = {
    "measure_it": "Il giusto è il più bello.",
    "measure_en": "The right measure is the most beautiful.",
    "limit_it": "Odia l'eccesso, rispetta il limite.",
    "limit_en": "Hate excess. Respect the limit.",
    "discretion_it": "Un professionista serio non rivela mai chi sono i suoi pazienti. Diffida da chi lo fa.",
    "discretion_en": "A serious professional never reveals who his patients are. Be wary of anyone who does.",
    "naturalness": "Only one word guides my practice: naturalness. Never give in to excess, never distort people — only try to bring out the best in them.",
}

# --------------------------------------------------------------------------
# Videos (titles from the doctor's YouTube channel; videos are in Italian)
# --------------------------------------------------------------------------
VIDEOS = {
    "HnflefgVqMM": "Facelift",
    "852M8oEXm4A": "How much does a facelift cost?",
    "_yyDI8cqhWU": "Rejuvenating the eyes",
    "86dQ-Oy1_eg": "Breast augmentation",
    "o-ksV1W2LeI": "Liposuction (English subtitles)",
    "-9COFP65Fl8": "Choosing a surgeon: warning signs not to ignore",
    "rIZn6oLeCpI": "Interview with Dr. Giuseppe Colombo",
    "DIH4McTTDNs": "Decus conference report",
    "U47HAtXf1ao": "Decus — two locations (English subtitles)",
}

# --------------------------------------------------------------------------
# Areas
# --------------------------------------------------------------------------
AREAS = {
    "face": {
        "slug": "face",
        "label": "Face",
        "title": "Face",
        "drawing": "face-woman",
        "lede": "Facelift, eyelids, brow, lips, ears and chin — and aesthetic medicine for the skin. Every treatment starts from the same principle: respect the face that is already yours.",
        "intro": "I have concentrated my practice on the face and neck, with particular attention to the facelift and to eyelid surgery.",
        "meta": "Facial plastic surgery and aesthetic medicine by Dr. Giuseppe Colombo in Lugano: facelift, blepharoplasty, brow lift, lip lift, otoplasty, chin surgery, hyaluronic acid, botulinum toxin and biorevitalisation.",
        "groups": [
            {"title": "Facial surgery", "items": ["facelift", "blepharoplasty", "brow-lift", "lip-lift", "otoplasty", "chin"]},
            {"title": "Aesthetic medicine", "items": ["hyaluronic-acid", "botulinum-toxin", "biorevitalisation"]},
        ],
    },
    "breast": {
        "slug": "breast",
        "label": "Breast",
        "title": "Breast",
        "drawing": "breast-pair",
        "lede": "Lift, augmentation, reduction and gynecomastia. Each procedure is chosen for the body in front of us — never for a trend.",
        "intro": "For the breast, my work focuses on reduction, lift and corrective augmentation.",
        "meta": "Breast surgery by Dr. Giuseppe Colombo in Lugano: mastopexy (breast lift), breast augmentation, breast reduction and gynecomastia.",
        "groups": [
            {"title": "Breast surgery", "items": ["mastopexy", "augmentation", "reduction", "gynecomastia"]},
        ],
    },
}

# --------------------------------------------------------------------------
# Procedures
# --------------------------------------------------------------------------
PROCEDURES = {
    # ---------------- FACE ----------------
    "facelift": {
        "area": "face", "group": "Facial surgery",
        "title": "Facelift", "subtitle": "Cervico-facial lift", "it": "Lifting cervico-facciale",
        "drawing": "profile-jaw",
        "lede": "The principal procedure in the surgery of facial ageing: it repositions, stably over time, the structures that the years have moved.",
        "body": [
            "The face ages at a pace that varies from person to person, depending on family predisposition and lifestyle. Ageing affects every element of the face — skin, subcutaneous fat and the deep musculature. The result is a heaviness that is often most visible in the lower third of the face and in the neck.",
            "In these cases only the cervico-facial lift — the principal procedure in the surgery of facial ageing — can correct these changes, by repositioning the structures involved, stably over time. The skin and, above all, the deeper tissues, in particular the musculature, are gently tensioned and stabilised to restore the right proportions and the natural harmony of the face.",
            "The key is a precise knowledge of the SMAS, the layer of tissue that lies beneath the skin and fat. The nerves that move the face, the salivary glands, the main vessels and the muscles that move the mouth symmetrically all lie beneath it.",
            "Surgery cannot give back the skin of a twenty-five-year-old, nor make every wrinkle disappear. That is why it is essential that the patient understands the whole process: their collaboration is fundamental to the best result.",
        ],
        "facts": [
            ("Layers treated", "Skin, subcutaneous fat and the deep musculature (SMAS)"),
            ("Main area", "Lower third of the face and the neck"),
            ("Principle", "Tension on the deep structures — not on the skin"),
        ],
        "quote": "By applying the force to the deep structures and not to the skin, we avoid tension on the scars — and firm, deep anchoring gives the result a far more lasting duration.",
        "videos": ["HnflefgVqMM", "852M8oEXm4A"],
        "article": "lifting-ringiovanimento-volto-invecchiamento-cutaneo-viso-ringiovanire-viso",
        "meta": "Cervico-facial lift by Dr. Giuseppe Colombo, Lugano: repositioning the deep structures of the face and neck (SMAS) for natural, lasting results.",
    },
    "blepharoplasty": {
        "area": "face", "group": "Facial surgery",
        "title": "Eyelid surgery", "subtitle": "Blepharoplasty", "it": "Blefaroplastica",
        "drawing": "eye-brow",
        "lede": "The eyes are the first to show the passing of time. Eyelid surgery restores a rested look while fully respecting the eye's function and expression.",
        "body": [
            "Those who ask about blepharoplasty are usually women between forty and forty-five, or slightly older men, whose face is otherwise well structured but who are bothered by excess skin — and sometimes fat — around the eyes. They are active people who dislike waking up with a tired look that has nothing to do with how they feel.",
            "Upper blepharoplasty removes the excess skin and a thin strip of the orbicularis muscle, which better defines the eyelid crease. The fat pockets are corrected in the right amount and in the right place — the only way to obtain a natural result and avoid a hollow, “sunken” look. The scar is hidden in the natural fold of the eyelid.",
            "Lower blepharoplasty is today almost always performed through the inside of the eyelid (transconjunctival approach). There is no external scar and, more importantly, the orbicularis muscle that holds the shape of the lower lid is preserved. When the outer corner of the eye has descended, a canthopexy can re-tension it and define the eye again.",
            "In more than half of the patients who are candidates for upper blepharoplasty, the problem is not only excess eyelid skin but also a descended eyebrow, especially in its outer portion. In these cases the ideal treatment combines blepharoplasty with a brow lift.",
        ],
        "facts": [
            ("Anaesthesia", "Local, with light sedation if needed"),
            ("Going home", "Usually within 24 hours"),
            ("Stitches removed", "After 4–7 days"),
            ("Normal appearance", "After 7–10 days"),
            ("Make-up & sun", "After the first week, with full sun protection"),
            ("Final result", "After about one year"),
            ("Duration", "Retouches are rarely needed before 10–15 years"),
        ],
        "quote": "It is preferable that a few small lines remain, to preserve as much as possible the original shape of the eye.",
        "videos": ["_yyDI8cqhWU"],
        "article": "la-chirurgia-delle-palpebre-limportanza-dello-sguardo-tecniche-per-il-miglioramento-della-regione-orbitaria-e-periorbitaria",
        "meta": "Upper and lower blepharoplasty by Dr. Giuseppe Colombo, Lugano: natural eyelid rejuvenation, hidden scars, recovery in 7–10 days.",
    },
    "brow-lift": {
        "area": "face", "group": "Facial surgery",
        "title": "Brow lift", "subtitle": "Lifting of the eyebrow", "it": "Lifting del sopracciglio",
        "drawing": "eyes",
        "lede": "A descended eyebrow is often underestimated — by patients and, unfortunately, by some surgeons.",
        "body": [
            "Brow ptosis — the descent of the eyebrow — is a frequently underestimated part of facial ageing. In more than half of the patients who are candidates for an upper blepharoplasty, the problem is not only excess eyelid skin but also a descended brow, especially in its outer portion. The ideal treatment must therefore combine blepharoplasty with a brow lift.",
            "The most widely used and effective methods are a so-called “direct” approach, with an easily concealed incision along the upper edge of the eyebrow, or — more often preferred — a trans-temporal approach: a small incision within the hairline, which remains completely invisible, through which the outer third of the eyebrow is lifted.",
        ],
        "facts": [
            ("Approach", "Trans-temporal (incision hidden in the hairline) or direct"),
            ("Area lifted", "The outer third of the eyebrow"),
            ("Often combined with", "Upper blepharoplasty"),
        ],
        "quote": "",
        "videos": ["_yyDI8cqhWU"],
        "article": "la-chirurgia-delle-palpebre-limportanza-dello-sguardo-tecniche-per-il-miglioramento-della-regione-orbitaria-e-periorbitaria",
        "meta": "Brow lift by Dr. Giuseppe Colombo, Lugano: lifting the outer third of the eyebrow through an invisible incision in the hairline.",
    },
    "lip-lift": {
        "area": "face", "group": "Facial surgery",
        "title": "Lip lift", "subtitle": "Upper lip lift", "it": "Lip-lifting",
        "drawing": "lip-profile",
        "lede": "A definitive reshaping of the upper lip — defined, natural and harmonious, without the need for further filler.",
        "body": [
            "The lip lift, or upper-lip lift, is a technique increasingly requested by patients. With age the upper lip often loses definition at the Cupid's bow, flattens and becomes longer: the distance between the columella — the base of the nose — and the vermilion increases.",
            "Several techniques exist, with different incisions. The most widely used, which guarantees a well-hidden scar along the alar-facial fold and the columella, is the “bullhorn” technique. It gives a well-defined, natural and harmonious upper lip that needs no further filler injections.",
        ],
        "facts": [
            ("Technique", "“Bullhorn” lip lift"),
            ("Scar", "Hidden at the base of the nose (alar-facial fold and columella)"),
            ("Result", "Definitive reshaping — no further filler needed"),
        ],
        "quote": "",
        "videos": [],
        "article": "",
        "meta": "Lip lift (upper lip lift) by Dr. Giuseppe Colombo, Lugano: the bullhorn technique for a defined, natural upper lip with a hidden scar.",
    },
    "otoplasty": {
        "area": "face", "group": "Facial surgery",
        "title": "Otoplasty", "subtitle": "Ear surgery", "it": "Otoplastica",
        "drawing": "ear-neck",
        "lede": "Correcting the shape of the ear by remodelling its cartilage — with a scar completely hidden behind the ear.",
        "body": [
            "Otoplasty is a surgical procedure that corrects imperfections of the outer ear. The most common is the so-called “prominent ear”: an ear that stands out from the head because of an open oto-mastoid angle and the absence of the antihelix, the main fold of the ear.",
            "The procedure changes the shape, size and position of the ear by remodelling its cartilage framework — weakening the cartilage and, where necessary, using stabilising sutures that restore the natural folds and curves of normal ear anatomy. The residual scar is completely hidden in the groove behind the ear.",
            "Ears can be corrected from the age of five or six, when they have reached a size and development that allow surgery; many patients are seen for the first time as adults, between twenty and thirty.",
        ],
        "facts": [
            ("Anaesthesia", "Local in adults, general in children"),
            ("From age", "5–6 years"),
            ("Scar", "Hidden in the groove behind the ear"),
            ("Check-up", "The day after surgery"),
            ("Afterwards", "A soft headband for at least one week; hair can be washed after the first week"),
        ],
        "quote": "",
        "videos": [],
        "article": "lotoplastica-come-correggere-i-difetti-del-padiglione-auricolare-una-breve-descrizione",
        "meta": "Otoplasty (prominent ear correction) by Dr. Giuseppe Colombo, Lugano: cartilage remodelling with a scar hidden behind the ear.",
    },
    "chin": {
        "area": "face", "group": "Facial surgery",
        "title": "Chin surgery", "subtitle": "Mentoplasty", "it": "Mentoplastica",
        "drawing": "lip-profile",
        "lede": "A harmonious profile depends on the chin as much as on the nose.",
        "body": [
            "For some patients rhinoplasty alone is not enough for a harmonious profile, because the chin sits too far back. Reducing the nose drastically to match the chin would be the wrong approach.",
            "The ideal is to study the profile carefully: the tip of the nose should project slightly further forward than the chin. If the chin is very retruded, the plan includes either a chin implant or the patient's own fat (lipofilling).",
            "Two small incisions of about two to three centimetres are made inside the mouth, behind the lower lip. The implants are made of silicone — solid yet flexible, so the surgeon can shape them during the procedure to the desired form. The incisions are closed with absorbable stitches.",
        ],
        "facts": [
            ("Anaesthesia", "Local with sedation; general when combined with rhinoplasty"),
            ("Incisions", "Inside the mouth, behind the lower lip"),
            ("Options", "Silicone implant or lipofilling"),
            ("Recovery", "Usual activities after about one week"),
        ],
        "quote": "",
        "videos": [],
        "article": "correzione-mento-mentoplastica",
        "meta": "Chin surgery (mentoplasty) by Dr. Giuseppe Colombo, Lugano: balancing the profile with a silicone implant or lipofilling.",
    },
    # ---------------- AESTHETIC MEDICINE ----------------
    "hyaluronic-acid": {
        "area": "face", "group": "Aesthetic medicine",
        "title": "Hyaluronic acid", "subtitle": "Aesthetic medicine", "it": "Acido ialuronico",
        "drawing": "molecule",
        "lede": "A natural component of the skin, restored where time has reduced it — for firmness, hydration and radiance.",
        "body": [
            "Hyaluronic acid is one of the main components of the connective tissue of the dermis, in which the collagen and elastic fibres are embedded. By binding water, it increases the elasticity, hydration and tone of the tissues, and it also has healing and anti-inflammatory properties.",
            "Its concentration in the skin decreases with age — one of the main causes of skin ageing. Injected hyaluronic acid re-tones mature skin, stimulating cellular function and restoring lost firmness and luminosity. For these reasons it has been used successfully in aesthetic dermatology for many years.",
            "It is reproduced in the laboratory and, apart from isolated cases of hypersensitivity, has no side effects. The doctor injects it with a very fine needle into the dermis or the subcutaneous tissue, depending on the area and depth to be treated. The filling or smoothing effect varies with the type of skin and the quality and quantity of hyaluronic acid used.",
        ],
        "facts": [
            ("Injection", "Very fine needle, into the dermis or subcutaneous tissue"),
            ("Duration", "Not permanent — repeated about every 6–12 months"),
            ("Not indicated", "Pregnancy, breastfeeding, collagen diseases or autoimmune skin diseases"),
        ],
        "quote": "",
        "videos": [],
        "article": "medicina-estetica-filler-botulino-acido-jaluronico-biostimolanti-invecchiamento-cutaneo-biorivitalizzazione",
        "meta": "Hyaluronic acid treatments by Dr. Giuseppe Colombo, Lugano: restoring hydration, firmness and radiance to mature skin.",
    },
    "botulinum-toxin": {
        "area": "face", "group": "Aesthetic medicine",
        "title": "Botulinum toxin", "subtitle": "Aesthetic medicine", "it": "Tossina botulinica",
        "drawing": "half-face",
        "lede": "Softening — not erasing — the expression lines that make the face look tired.",
        "body": [
            "Botulinum toxin is a highly purified substance, derived from the bacterium Clostridium botulinum, that temporarily and locally reduces the excessive contraction of certain facial muscles — and with it the formation of dynamic wrinkles in the upper third of the face: forehead, brow, the area between the brows and crow's feet.",
            "These lines give a tired look, especially around the eyes. The real goal of the treatment is to give the eyes and the surrounding areas a toned, rested appearance — a fresh expression in the evening as well as in the morning. Unlike hyaluronic-acid fillers, it does not fill.",
            "It is also used to slim a hypertrophic masseter muscle, which can make the face look square, restoring a more oval shape; to treat the vertical bands of the platysma muscle in the neck; and, in small doses, to tone the sides of the neck for those who wish to postpone a neck lift. Another important indication is hyperhidrosis — excessive sweating of the underarms, hands or feet.",
        ],
        "facts": [
            ("Anaesthesia", "None needed — practically painless"),
            ("Effect begins", "After about 3 days"),
            ("Duration", "About 5 months, after which it can be repeated"),
            ("Areas", "Forehead, brow, glabella, crow's feet · masseter · neck"),
        ],
        "quote": "More than any other procedure, this one depends on the doctor. Used with aesthetic sense and measure, in agreement with the patient's expectations, it aims not to erase every imperfection but to soften the lines that age the face. Respect these rules and the frozen, over-pulled look will not occur.",
        "videos": [],
        "article": "medicina-estetica-filler-botulino-acido-jaluronico-biostimolanti-invecchiamento-cutaneo-biorivitalizzazione",
        "meta": "Botulinum toxin by Dr. Giuseppe Colombo, Lugano: softening expression lines with measure — never a frozen look.",
    },
    "biorevitalisation": {
        "area": "face", "group": "Aesthetic medicine",
        "title": "Biorevitalisation", "subtitle": "Aesthetic medicine", "it": "Biorivitalizzazione",
        "drawing": "face-woman",
        "lede": "Improving the quality of the skin itself — without changing the volumes of the face.",
        "body": [
            "Facial bio-restructuring is an advanced aesthetic-medicine treatment that improves the quality of the tissues by stimulating the skin's natural regeneration, without altering the volumes of the face. It is not meant to “fill”, but to reactivate the biological function of the skin — countering laxity, dehydration and the loss of elasticity and tone.",
            "It acts on the different layers of the skin, encouraging the production of collagen and elastin and improving the structure of the dermis over time. It is suited both to the first signs of ageing and as a maintenance treatment or a preparation for more invasive procedures.",
            "The treatment consists of targeted micro-injections of bio-regenerative substances, selected according to the characteristics of the skin and the clinical goals. The result is a fresher, firmer and more luminous face — a natural, progressive rejuvenation that respects each person's anatomy and expression.",
        ],
        "facts": [
            ("Setting", "Outpatient treatment, well tolerated"),
            ("Downtime", "No significant recovery time"),
            ("Suited to", "First signs of ageing, maintenance, or preparation for surgery"),
        ],
        "quote": "",
        "videos": [],
        "article": "medicina-estetica-filler-botulino-acido-jaluronico-biostimolanti-invecchiamento-cutaneo-biorivitalizzazione",
        "meta": "Biorevitalisation by Dr. Giuseppe Colombo, Lugano: micro-injections that restore the skin's quality without changing facial volumes.",
    },
    # ---------------- BREAST ----------------
    "mastopexy": {
        "area": "breast", "group": "Breast surgery",
        "title": "Breast lift", "subtitle": "Mastopexy", "it": "Mastopessi",
        "drawing": "mastopexy",
        "lede": "Lifting and reshaping a breast that has descended and lost volume.",
        "body": [
            "Mastopexy corrects an excessive descent of the breast. It re-tones a breast that has sagged and emptied, improving its shape and volume and correcting the changes caused by pregnancy, breastfeeding, significant weight loss and natural ageing. The aim is to regain, as far as possible, a full, firm appearance.",
            "The technique depends on the degree of ptosis. In milder cases it is enough to remove a ring of skin around the areola to return the breast to its correct position; the scar is easily concealed at the border between the areola and the skin. In more severe cases further skin must be removed, and the scar around the areola is usually combined with a vertical scar down to the fold beneath the breast and a horizontal scar within that fold (an inverted “T”).",
            "In some cases removing the excess skin and lifting the breast are combined with latest-generation implants, for greater volume (augmentation mastopexy).",
        ],
        "facts": [
            ("Corrects", "The effects of pregnancy, breastfeeding, weight loss and ageing"),
            ("Scars", "Around the areola in mild cases; inverted “T” in more severe cases"),
            ("Option", "Combined with implants for more volume (augmentation mastopexy)"),
        ],
        "quote": "",
        "videos": [],
        "article": "",
        "meta": "Breast lift (mastopexy) by Dr. Giuseppe Colombo, Lugano: restoring the position and shape of the breast after pregnancy, weight loss or ageing.",
    },
    "augmentation": {
        "area": "breast", "group": "Breast surgery",
        "title": "Breast augmentation", "subtitle": "Augmentation mammaplasty", "it": "Mastoplastica additiva",
        "drawing": "implant",
        "lede": "More volume — chosen for the right reasons, and only when it is the right answer.",
        "body": [
            "Sometimes increasing volume alone is not the right choice for the best result. When a lack of volume comes with a descended breast (ptosis), an implant alone cannot correct the sagging — it may even make it worse. In these cases a breast lift combined with implants is the ideal combination.",
            "Today's silicone-gel implants, with an outer shell of silicone elastomer chosen for its strength, durability and flexibility, are the ones that best reproduce the look and feel of a natural breast.",
        ],
        "facts": [
            ("Implants", "Latest-generation silicone gel"),
            ("With sagging", "Combined with a breast lift for the best result"),
        ],
        "quote": "Fashion should never condition the decision to change one's body. The reasons for an aesthetic procedure must be clear, serious and considered — based on feeling well with oneself, and on bringing outer and inner appearance into harmony.",
        "videos": ["86dQ-Oy1_eg"],
        "article": "mastoplastica-additiva-di-cosa-si-tratta-parliamone-storia-protesi",
        "meta": "Breast augmentation by Dr. Giuseppe Colombo, Lugano: silicone-gel implants, combined with a lift when needed, for a natural result.",
    },
    "reduction": {
        "area": "breast", "group": "Breast surgery",
        "title": "Breast reduction", "subtitle": "Reduction mammaplasty", "it": "Mastoplastica riduttiva",
        "drawing": "female-torso",
        "lede": "Lightening the breast — for its appearance, and for the body's comfort.",
        "body": [
            "Breast reduction is the procedure for gigantomastia or hypertrophy of the mammary gland. It is performed not only for aesthetic reasons but also for functional ones: a breast that is too large and heavy weighs on the front of the body and often causes pain in the shoulders, the neck and the upper spine.",
            "A reduction of even four or five sizes can be achieved. The procedure also lifts a breast that has descended too far and, at the same time, fills its upper part.",
            "Surgical techniques have evolved and been refined over the years, and so has the quality of the scars. For future check-ups — mammography, ultrasound or CT — the radiologist and gynaecologist should be told about the operation: it helps them read the results correctly.",
        ],
        "facts": [
            ("Reasons", "Aesthetic and functional (shoulder, neck and upper-back pain)"),
            ("Reduction", "Up to four or five sizes"),
            ("Also", "Lifts the breast and fills its upper part"),
        ],
        "quote": "",
        "videos": [],
        "article": "la-chirurgia-per-ridurre-il-volume-del-seno-la-mastoplastica-riduttiva",
        "meta": "Breast reduction by Dr. Giuseppe Colombo, Lugano: relief from the weight of a large breast, with a lifted, natural shape.",
    },
    "gynecomastia": {
        "area": "breast", "group": "Breast surgery",
        "title": "Gynecomastia", "subtitle": "Male breast correction", "it": "Ginecomastia",
        "drawing": "male-torso",
        "lede": "Correcting a male chest that feels feminine.",
        "body": [
            "The procedure corrects a typically male condition: an abundant accumulation of fat in the chest (false gynecomastia) or of glandular tissue (true gynecomastia). In some cases both components are present (mixed gynecomastia).",
            "It is much requested by men between twenty and forty, who feel uncomfortable with a chest that looks feminine rather than masculine.",
        ],
        "facts": [
            ("Types", "False (fat), true (glandular) or mixed"),
            ("Typical patients", "Men aged 20–40"),
        ],
        "quote": "",
        "videos": [],
        "article": "",
        "meta": "Gynecomastia correction by Dr. Giuseppe Colombo, Lugano: restoring a masculine chest contour.",
    },
}

RECONSTRUCTIVE = {
    "title": "Reconstructive surgery",
    "drawing": "dash-arrow",
    "lede": "Restoring form and function — with a particular focus on the face after skin-cancer surgery.",
    "focus": "I have always had reconstructive surgery at heart. In this field I deal exclusively with reconstruction of the face after cutaneous oncological surgery.",
    "areas": ["Complex dermatological surgery", "Oncological dermatological surgery", "Reconstructive surgery of the face"],
    "body": [
        "The purpose of reconstructive surgery is to restore the form and function of regions of the face and body that have been damaged or deformed. Surgery can improve or resolve problems caused by trauma, tumours, burns, congenital malformations, infections, facial fractures and nerve injuries.",
    ],
    "techniques": [
        ("Skin grafts", "Transfer of skin from one part of the body to another, to cover an area with new skin."),
        ("Flaps", "Transfer of skin, fat, muscle, cartilage and/or bone from neighbouring regions, without interrupting their blood supply, to repair soft-tissue defects."),
        ("Autografts", "Harvesting tissue — cartilage, tendon, fat, dermis, muscle, nerve or bone — from other parts of the body to provide what the reconstruction needs."),
        ("Microsurgery", "Reconstruction of missing tissue by transfer from another site, using microsurgical techniques to restore blood supply and nerve function."),
    ],
    "meta": "Reconstructive surgery by Dr. Giuseppe Colombo, Lugano: facial reconstruction after skin-cancer surgery, grafts, flaps and microsurgery.",
}

# --------------------------------------------------------------------------
# Philosophy / About
# --------------------------------------------------------------------------
ABOUT = [
    "I am a specialist in plastic and reconstructive surgery. I was fortunate, during my training, to learn at the side of great masters of this fascinating branch of surgery — spending long periods in Spain and France and, of course, in Italy. For years I was a consultant to prestigious hospitals such as the Ospedale Evangelico Internazionale in Genoa.",
    "To offer my patients the best possible result, I have concentrated my attention and my practice on the face and neck and on the breast: the facelift and blepharoplasty for the face; reduction, lift and corrective augmentation for the breast. I have always had reconstructive surgery at heart, and in this field I deal exclusively with reconstruction of the face after skin-cancer surgery.",
    "Over the years I have organised many dissection courses, to give colleagues the opportunity to share my experience and theirs. In the same spirit I edited an important Atlas of Surgery. It is a great pleasure to host young doctors and colleagues in my operating rooms. Medicine and surgery progress very quickly and give better and better results when all doctors share their experience — this is my spirit.",
    "As for my philosophy in aesthetic medicine and plastic surgery, a single word guides my practice: naturalness. Never give in to excess, never distort people — only try to bring out the best in them.",
]

MILESTONES = [
    ("2005", "Degree in Medicine and Surgery", "University of Genoa — 110/110 cum laude, with the medal for academic merit. Thesis: an experimental study on tissue expansion."),
    ("Specialisation", "Plastic, Reconstructive and Aesthetic Surgery", "University of Genoa — first place in the admission exam; diploma 50/50 cum laude. Thesis: “Anatomy and surgical techniques of facial rejuvenation: treatment of the SMAS. Evolution of results over time.”"),
    ("2007–08", "SICPRE scholarship", "Awarded by the Italian Society of Plastic, Reconstructive and Aesthetic Surgery for anatomical dissection."),
    ("2008–10", "Training with masters", "Villa Bella, Salò (Prof. Botti) · Academy of Human Anatomy, Brussels · Clínica Quirón (Dr. Tapia), facial rejuvenation and the triple SMAS flap."),
    ("2009", "Breast surgery in Geneva and Lyon", "Senology unit, Geneva University Hospitals (HUG), a EUSOMA-certified European reference centre · Plastic and reconstructive surgery, Centre Léon Bérard, Lyon."),
    ("Since 2008", "Anatomy in Nice", "Regular anatomical dissection at the Department of Human Anatomy, Université Sophia-Antipolis, Nice — breast and cranio-facial regions."),
    ("2010–18", "Director of dissection courses", "Theoretical-practical courses in Nice and Madrid: face, breast, microsurgery, rhinoplasty and sutures."),
    ("2013–15", "Co-director, Ospedale Evangelico Internazionale", "Plastic and Reconstructive Surgery, Genoa — and director of its Centre of Excellence for Plastic Surgery."),
    ("Today", "Author & teacher", "Editor of the Stepwise Atlas of Aesthetic Medicine and Surgery (Springer) · Lecturer, Master in Aesthetic Surgery, University of Pavia."),
]

CV_GROUPS = [
    ("Education", [
        "1999 — Classical high-school diploma (Maturità classica).",
        "1999–2005 — Medicine and Surgery, University of Genoa.",
        "2005 — Degree in Medicine and Surgery, University of Genoa, 110/110 cum laude with the medal for academic merit. Thesis: experimental study on tissue expansion, in collaboration between the Department of Biochemistry and the Chair of Plastic Surgery.",
        "First place in the admission exam to the School of Specialisation in Plastic, Reconstructive and Aesthetic Surgery, University of Genoa.",
        "Specialisation diploma in Plastic, Reconstructive and Aesthetic Surgery, 50/50 cum laude. Thesis: “Anatomy and surgical techniques of facial rejuvenation, treatment of the SMAS. Evolution of results over time.”",
        "European Inter-University Diploma in Surgical Practice in Oncology (DIU Européen de Pratiques Chirurgicales en Cancérologie — Universities of Lyon, Nantes, Genoa, Nancy, Paris).",
    ]),
    ("Positions", [
        "Since 2012 — Head of plastic and aesthetic surgery, Villa Serena, Genoa.",
        "June 2013 – October 2015 — Co-director, Plastic and Reconstructive Surgery, Ospedale Evangelico Internazionale, Genoa.",
        "Director, Centre of Excellence for Plastic Surgery — Ospedale Evangelico Internazionale, Genoa.",
        "Lecturer, Master in Aesthetic Surgery — University of Pavia.",
        "2011–2013 — Consultant in plastic surgery, Policlinico di Monza.",
        "April 2011 – December 2013 — SUMAI consultant in plastic and reconstructive surgery for ASL2 Savonese, Cairo Montenotte hospital.",
        "Since December 2010 — Court-appointed technical expert in plastic, reconstructive and aesthetic surgery, Court of Savona.",
        "Since January 2010 — Board member, Società Polispecialistica dei Giovani Chirurghi, Liguria section.",
    ]),
    ("Clinical training", [
        "2008, 2010 — Visiting surgeon at Day Clinic Villa Bella, Salò (Prof. Botti): face, neck and breast anatomy and the main techniques of aesthetic surgery.",
        "October–November 2008 — Academy of Human Anatomy, Brussels: theoretical-practical course with cadaver dissection on the main techniques of facial aesthetic surgery.",
        "March–June 2009 — Internal physician, Senology unit, Geneva University Hospitals (HUG), Prof. Jean-Bernard Dubuisson — a EUSOMA-certified European reference centre.",
        "July 2009 and June–July 2010 — Visiting surgeon at Clínica Quirón, plastic and aesthetic surgery (Dr. Tapia): facial rejuvenation, the triple SMAS flap facelift.",
        "October 2009 — Internal physician, Plastic and Reconstructive Surgery, Centre Léon Bérard, Lyon — the French reference centre for breast reconstruction.",
        "Since 2008 — Regular monthly anatomical dissection at the Department of Human Anatomy, Université Sophia-Antipolis, Nice, with particular interest in the breast and cranio-facial regions.",
    ]),
    ("Memberships & reviewing", [
        "2007–2008 — SICPRE scholarship for anatomical dissection.",
        "2008 — International Delegate, World Society of Anti-Aging Medicine.",
        "December 2008 — Tutor in the use of fillers for Q-Med, on the basis of clinical experience.",
        "Reviewer for international journals indexed on PubMed-Medline: Minerva Chirurgica (since 2009), Rare Tumors (since 2009), Il Giornale di Chirurgia (since 2010), Minerva Medica, World Journal of Surgical Oncology.",
    ]),
    ("Teaching", [
        "2007–2009 — Lecturer in Human Anatomy at upper-secondary institutes in Savona and Albenga.",
        "2010–2018 — Co-director and director of theoretical-practical anatomy and surgery courses in Nice and Madrid (see the Academy).",
    ]),
]

# --------------------------------------------------------------------------
# Academy
# --------------------------------------------------------------------------
ATLAS = {
    "title": "Stepwise Atlas of Aesthetic Medicine and Surgery",
    "publisher": "Springer",
    "role": "Editor",
    "url": "https://link.springer.com/book/10.1007/978-3-031-95036-0",
    "text": [
        "A practical, up-to-date reference for those approaching — or already working in — aesthetic medicine and surgery. Richly illustrated with more than 320 original photographs and organised in two sections, theoretical and practical, it guides the reader through every fundamental aspect of aesthetic procedures, from pre-operative planning to post-operative management, with a clear, step-by-step approach.",
        "Written for young surgeons and experienced professionals alike, it covers all the main anatomical areas and techniques, providing the essential tools to perform treatments safely and competently.",
    ],
    "previous": {
        "title": "Atlante iconografico di chirurgia e medicina estetica — I fondamenti step by step",
        "note": "Earlier atlas edited by Giuseppe Colombo and Vittorio Ruvolo.",
    },
}

FELLOWSHIP = [
    "It is a great pleasure for Dr. Colombo to share his experience with colleagues. Colleagues who join a fellowship follow him in the clinics where he operates and in the practices where he holds consultations and aesthetic-medicine treatments.",
    "Half of the operations are facial procedures; the other half are breast surgery. The secretary's office can help visiting colleagues find suitable accommodation if they wish to stay for several days.",
]

COURSES = [
    {
        "year": "2024", "place": "Cremona · Palazzo Trecchi", "items": [
            {"date": "9–10 May 2024", "title": "Reasoned anatomy of the face and facial rejuvenation techniques — from blepharoplasty to facelift, step by step", "poster": "poster-2024-face", "pdf": "https://drive.google.com/file/d/1YyaZKkfx91MeeYevs6LGi2GqsA2VDePq/view?usp=sharing"},
            {"date": "10 May 2024", "title": "Reasoned anatomy of the nasal pyramid — rhinoplasty, step by step", "poster": "poster-2024-nose", "pdf": "https://drive.google.com/file/d/1eV02PMOJFgKv12vFeOzOwCGKCSG1H3jw/view?usp=sharing"},
            {"date": "8 June 2024", "title": "Facial aesthetic medicine, live dissection — anatomy, techniques and injection planes, step by step", "poster": "poster-2024-aesthetic", "pdf": "https://drive.google.com/file/d/17SqSwN3W17Xzsr8S0PoNju7DHroAcK_h/view?usp=sharing"},
        ],
    },
    {
        "year": "2018", "place": "Nice · Université Sophia-Antipolis", "items": [
            {"date": "6–7 February 2018", "title": "Cadaver lab — facelift and blepharoplasty", "poster": "poster-2018-face", "pdf": ""},
            {"date": "7 February 2018", "title": "Cadaver lab — rhinoplasty", "poster": "poster-2018-rhino", "pdf": ""},
            {"date": "8–9 February 2018", "title": "Cadaver lab — breast surgery and gluteoplasty", "poster": "poster-2018-breast", "pdf": ""},
        ],
    },
    {
        "year": "2017", "place": "Nice · Université Sophia-Antipolis", "items": [
            {"date": "2017", "title": "Practical course in aesthetic medicine — KORU Anatomy & Surgery", "poster": "poster-2017-aesthetic", "pdf": ""},
        ],
    },
    {
        "year": "2015", "place": "Nice · Université Sophia-Antipolis", "items": [
            {"date": "3–4 February 2015", "title": "Aesthetic plastic surgery and reasoned anatomy of the face and neck", "poster": "poster-2015-face", "pdf": ""},
            {"date": "5–6 February 2015", "title": "Breast course", "poster": "poster-2015-breast", "pdf": ""},
            {"date": "6 February 2015", "title": "Surgical anatomy of the abdominal region", "poster": "poster-2015-abdomen", "pdf": ""},
            {"date": "6 February 2015", "title": "Surgical sutures on cadaver", "poster": "poster-2015-sutures", "pdf": ""},
        ],
    },
    {
        "year": "2013", "place": "Savona", "items": [
            {"date": "8–9 June 2013", "title": "Biennial of Morphodynamic Surgery — decision making in aesthetic plastic surgery (co-president)", "poster": "poster-2013-biennale", "pdf": ""},
        ],
    },
]

COURSES_EARLY = [
    "Nice, December 2010 — Anatomy and basic surgical techniques of the breast and gluteal regions; anatomy and basic microsurgical techniques (anterolateral thigh, radial, peroneal and dorsal regions).",
    "Nice, June 2011 — Anatomy and basic surgical techniques of the breast and gluteal regions; basic microsurgery.",
    "Madrid, October 2011 — Anatomy and basic surgery of the cervico-facial region; reasoned anatomy and basic techniques in rhinoplasty and profileplasty.",
    "Nice, December 2011 — Basic surgery of the breast and gluteal region; basic microsurgery.",
    "Nice, April 2012 — Sutures; conservative surgery of the cervico-facial region.",
    "Nice, July 2012 — Surgical techniques of the foot; reasoned anatomy of the abdomen; sutures.",
    "Madrid, October 2012 — Microsurgery; rhinoplasty and profileplasty; basic aesthetic plastic surgery and reasoned anatomy of the face and neck; reasoned oncological anatomy and surgery of the face and neck.",
    "Nice, February 2013–2018 — Annual courses in facelift and blepharoplasty, and in breast and gluteal surgery.",
]

PUBLICATIONS = [
    ("2021", "Ten-year revision of breast augmentation with preoperative imaging diagnostics", "JPD Journal", "Breast"),
    ("2018", "Global facial rejuvenation, new technique", "Plastic and Aesthetic Research", "Face"),
    ("2017", "Effectiveness of Biocollagen", "JPD Journal, Aesthetic Medicine", "Aesthetic medicine"),
    ("2014", "KORU lifting: personal approach. A safe way to perform a face lift", "Oral & Maxillo Journal", "Face"),
    ("2011", "Prosthetic breast implant rupture: imaging — pictorial essay", "Aesthetic Plastic Surgery", "Breast"),
    ("2011", "Destructive granulomatous reaction to polyacrylamide lip injection: solution for a complex case", "Aesthetic Plastic Surgery", "Aesthetic medicine"),
    ("2010", "A vast intranasal filler-induced granulomatous reaction: a case report", "Aesthetic Plastic Surgery", "Aesthetic medicine"),
    ("2009", "Informed consent in surgery. Fundamental principles", "Clinical and Experimental Plastic Surgery — Italian Journal of Plastic Surgery", "General"),
    ("2009", "Oncoplastic surgery for the treatment of breast cancer", "Minerva Ginecologica 61(5):439–44", "Breast"),
    ("2009", "Malignant mixed Müllerian tumors: use of CD34 as an additional parameter for the evaluation of prognostic factors", "Revue Gynécologie-Obstétrique", "Oncology"),
    ("2009", "Local anaesthesia in outpatient surgery: a fundamental, always open issue. Principles", "Clinical and Experimental Plastic Surgery — Italian Journal of Plastic Surgery", "General"),
    ("2008", "Plication of the rectus muscles in abdominoplasty, both functional and aesthetic. Technical notes", "Clinical and Experimental Plastic Surgery — Italian Journal of Plastic Surgery", "Body"),
    ("2008", "PONV: a debilitating problem in plastic surgery. How to treat it, how to prevent it", "Clinical and Experimental Plastic Surgery — Italian Journal of Plastic Surgery", "General"),
    ("2008", "Prophylaxis of bacterial infections in prosthetic breast surgery", "Clinical and Experimental Plastic Surgery — Italian Journal of Plastic Surgery", "Breast"),
    ("", "The plant hormone abscisic acid increases in human plasma after hyperglycemia and stimulates glucose consumption by adipocytes and myoblasts", "FASEB Journal", "Research"),
    ("", "Comparative studies on different techniques of acute tissue expansion · Tissue expansion: experimental models · New methods for tissue expansion · Intermittent acute tissue expansion: DMSO versus traditional technique", "Experimental studies", "Research"),
    ("", "Melanoma and spectrophotometric study: an experimental study", "Experimental study", "Oncology"),
    ("", "D-Sculptor: 3D anatomical pictures in plastic surgery", "", "Research"),
    ("", "New trends in flexor tendon repair and sutures · Experimental progress in hair restoration surgery · Scalp reduction: experimental and clinical evaluations", "", "Research"),
]

# Journal: which articles to publish (the duplicate liposuction article is merged)
JOURNAL_SKIP = {"liposuzione-laser-liposuzione-tessuto-adiposo-grasso"}
JOURNAL_EN_TITLES = {
    "lifting-ringiovanimento-volto-invecchiamento-cutaneo-viso-ringiovanire-viso": ("The facelift: rejuvenating the face, harmoniously", "Face"),
    "correzione-mento-mentoplastica": ("Correcting the chin: mentoplasty", "Face"),
    "la-chirurgia-per-ridurre-il-volume-del-seno-la-mastoplastica-riduttiva": ("Surgery to reduce breast volume: reduction mammaplasty", "Breast"),
    "il-tessuto-adiposo-anatomia-e-patologia-come-trattarlo-le-diverse-metodiche-di-liposuzione": ("Adipose tissue — anatomy, pathology and the different liposuction techniques", "Body"),
    "la-chirurgia-delle-palpebre-limportanza-dello-sguardo-tecniche-per-il-miglioramento-della-regione-orbitaria-e-periorbitaria": ("Eyelid surgery: the importance of the gaze", "Face"),
    "addominoplastica-il-cambiamento-della-parete-addominale-con-il-passare-del-tempo": ("Abdominoplasty: how the abdominal wall changes over time", "Body"),
    "cosa-e-la-chirurgia-estetica": ("What plastic — and above all aesthetic — surgery really is", "Philosophy"),
    "lotoplastica-come-correggere-i-difetti-del-padiglione-auricolare-una-breve-descrizione": ("Otoplasty: correcting the shape of the ear", "Face"),
    "mastoplastica-additiva-di-cosa-si-tratta-parliamone-storia-protesi": ("A history of breast implant surgery", "Breast"),
    "medicina-estetica-filler-botulino-acido-jaluronico-biostimolanti-invecchiamento-cutaneo-biorivitalizzazione": ("The skin, ageing, and the options of aesthetic medicine", "Aesthetic medicine"),
    "storia-della-chirurgia-plastica-una-branca-meravigliosa-della-medicina-savona-genova-alessandria-lugano": ("A history of plastic surgery — a wonderful branch of medicine", "Philosophy"),
}

# ==========================================================================
# Language-specific settings (English)
# ==========================================================================
LANG = "en"
MONTHS = "January February March April May June July August September October November December".split()

PATHS = {
    "home": "/en/", "philosophy": "/en/philosophy/", "face": "/en/face/", "breast": "/en/breast/",
    "reconstructive": "/en/reconstructive/", "academy": "/en/academy/", "journal": "/en/academy/journal/",
    "contact": "/en/contact/",
}
PROC_SLUGS = {k: k for k in PROCEDURES}
NAV_LABELS = {"philosophy": "Philosophy", "face": "Face", "breast": "Breast", "academy": "Academy", "contact": "Contact"}

JOURNAL_TITLES = {k: v[0] for k, v in JOURNAL_EN_TITLES.items()}
JOURNAL_CATS = {k: v[1] for k, v in JOURNAL_EN_TITLES.items()}

UI = {
    "skip": "Skip to content", "home": "Home", "home_aria": "Dr. Giuseppe Colombo — home", "language": "Language",
    "book": "Book a consultation", "menu": "Menu", "close": "Close", "contact": "Contact",
    "first_step": "— The first step", "begin_html": "Begin with a <em>conversation</em>",
    "discover": "Discover", "dr": "Dr. Colombo",
    # booking
    "bk_label": "— Consultation request", "bk_q1": "What would you like to discuss?",
    "bk_opts": ["Face — surgery", "Face — aesthetic medicine", "Breast", "Reconstructive surgery", "Something else"],
    "bk_q2": "Where would you like to meet?", "bk_q3": "How can we reach you?",
    "bk_name": "Name", "bk_email": "Email", "bk_phone": "Phone", "bk_lang": "Preferred language",
    "bk_q4": "Anything you would like us to know?", "bk_msg": "Message (optional)",
    "bk_consent": "I agree that my details are used only to answer this request.",
    "bk_thanks": "Thank you.",
    "bk_done": "Your email app has opened with your request addressed to {email} — please send it to complete. The secretary's office answers {hours}.",
    "bk_conf": "Your information is confidential.", "bk_back": "← Back", "bk_continue": "Continue", "bk_or_call": "Or call",
    # procedure / area
    "key_facts": "Key facts", "facts_note": "From Dr. Colombo's own texts. Every case is assessed individually during the consultation.",
    "the_procedure": "— The procedure", "from_journal": "from the Journal", "video_it": "— Video · in Italian",
    "videos_it": "— Videos · in Italian", "from_journal_label": "— From the Journal", "in_italian": "in Italian",
    "read_article": "Read the article", "also_in": "— Also in", "min": "min", "min_read": "min read",
    "discuss_html": "Discuss {x} with <em>Dr. Colombo</em>.", "discuss_sub": "A consultation is where every plan begins — in Lugano, Zurich or Italy.",
    "begin_full_html": "Begin with a <em>conversation</em>.",
    "area_cta_sub": "Every treatment starts with listening — to what you want, and to what your anatomy allows.",
    "recon_label": "— Reconstructive surgery", "recon_band": "Restoring the face after skin-cancer surgery.",
    "purpose": "— Purpose", "techniques": "— Techniques", "play": "Play video",
    # philosophy
    "in_his_words": "— In his words", "thanks_trust": "Thank you for your trust.", "path": "— Path",
    "path_h_html": "Trained by <em>masters</em>.<br>Shaped by anatomy.", "the_person": "— The person",
    "person_h_html": "Medicine progresses fastest when doctors <em>share</em>.",
    "person_p": "Young doctors and colleagues are welcome in his operating rooms — the same spirit behind the courses, the fellowships and the Atlas.",
    "the_academy": "The Academy", "discretion": "— Discretion", "cv": "— Curriculum vitae", "cv_h": "The full record.",
    "portrait_alt": "Portrait of Dr. Giuseppe Colombo", "smile_alt": "Dr. Giuseppe Colombo smiling",
    # academy
    "academy_quote": "“Medicine and surgery progress very quickly, and give better and better results when all doctors share their experience — this is my spirit.”",
    "on_page": "On this page", "j_atlas": "The Atlas", "j_fellow": "Fellowship", "j_courses": "Courses", "j_pubs": "Publications", "j_journal": "Journal", "j_videos": "Videos",
    "atlas_label": "— The Atlas", "view_springer": "View on Springer ↗", "earlier_work": "— Earlier work",
    "fellow_label": "— Fellowship", "fellow_h_html": "Half face.<br><em>Half breast.</em>", "information": "Information:",
    "courses_label": "— Courses & dissection labs", "courses_h_html": "Anatomy, <em>step by step.</em>",
    "courses_lead": "New dates are announced here. For information on upcoming courses, write to",
    "brochure": "Brochure (PDF)", "poster": "Course poster", "earlier_courses": "Earlier courses directed, 2010–2018",
    "pubs_label": "— Publications", "pubs_h_html": "Published <em>work.</em>", "filter_topic": "Filter by topic", "all": "All",
    "journal_label": "— Journal", "journal_h_html": "From the <em>Journal.</em>", "all_articles": "All articles",
    "topics": {"Face": "Face", "Breast": "Breast", "Aesthetic medicine": "Aesthetic medicine", "Oncology": "Oncology", "General": "General", "Research": "Research", "Body": "Body"},
    "cats": {"Face": "Face", "Breast": "Breast", "Body": "Body", "Aesthetic medicine": "Aesthetic medicine", "Philosophy": "Philosophy"},
    # journal
    "journal": "Journal", "journal_lead": "Dr. Colombo's articles on the face, the breast, aesthetic medicine and the history of plastic surgery. Articles are published in Italian.",
    "latest": "Latest", "filter_cat": "Filter by category", "article_note": "This article is published in Italian, as written by Dr. Colombo.",
    "related_proc": "Related procedure:", "continue_reading": "— Continue reading", "academy": "Academy",
    # contact
    "contact_h_html": "Begin with a <em>conversation.</em>",
    "contact_lead": "Consultations in Lugano, Zurich and Italy, by appointment. The secretary's office answers {hours}.",
    "request_consult": "Request a consultation", "request_appt": "Request an appointment",
    "telephone": "— Telephone", "email": "— Email", "info_appts": "Information and appointments", "fellow_courses": "Fellowships and courses",
    "map_text": "The map is provided by Google and loads only if you ask for it.", "show_map": "Show map",
    # 404
    "nf_h_html": "This page has lost its <em>measure.</em>", "nf_p": "The page you are looking for does not exist — or has moved with the new site.", "nf_btn": "Return home",
    # titles / meta
    "suffix": "Dr. Giuseppe Colombo · Plastic Surgery",
    "home_title": "Dr. Giuseppe Colombo — Plastic surgery of the face and breast, Lugano",
    "home_meta": "Dr. Giuseppe Colombo, specialist in plastic, reconstructive and aesthetic surgery. Face and breast surgery in Lugano, with consultations in Zurich and Italy. Naturalness above all.",
    "phil_title": "Philosophy", "phil_meta": "Dr. Giuseppe Colombo: training, career and philosophy. Plastic surgeon focused on the face and the breast — naturalness above all.",
    "acad_meta": "The Academy of Dr. Giuseppe Colombo: the Springer Stepwise Atlas of Aesthetic Medicine and Surgery, fellowships, dissection courses and publications.",
    "journal_meta": "Articles by Dr. Giuseppe Colombo on facial surgery, breast surgery, aesthetic medicine and the history of plastic surgery.",
    "contact_title": "Contact", "contact_meta": "Book a consultation with Dr. Giuseppe Colombo: Clinica Sant'Anna, Lugano; consultations in Zurich and Italy by appointment.",
    "nf_title": "Page not found",
    "js": {
        "menu": "Menu", "close": "Close", "send": "Send request", "continue": "Continue",
        "e1": "Please choose one option.", "e2": "Please choose a location.", "e3": "Please enter your name.",
        "e4": "Please enter a valid email address.", "e5": "Please confirm the privacy consent.",
        "subject": "Consultation request", "interest": "Interest", "location": "Location", "name": "Name",
        "email": "Email", "phone": "Phone", "language": "Preferred language", "map": "Map: Clinica Sant'Anna, Lugano",
    },
}

HOME = {
    "kicker": "— Dr. Giuseppe Colombo · Lugano",
    "hero_line_html": "The right <em>measure</em> is the most beautiful.",
    "hero_sub": "Plastic surgery of the face and breast",
    "philosophy": "— Philosophy", "doc_tr": "Hate excess. Respect the limit.", "meet": "Meet Dr. Colombo",
    "beneath": "— Beneath the surface", "layers_h": "The layers of the face",
    "steps": [
        ("01 · Skin", "What you see.", "The surface — a barrier against wind, sun and everything we meet each day."),
        ("02 · Fat", "What lies beneath.", "A layer only a few millimetres thick, which shifts and descends with the years."),
        ("03 · SMAS", "What holds it.", "The deep layer the surgeon works on. Knowing it precisely is fundamental."),
        ("04 · Deep", "What must be protected.", "The nerves that move the face, the main vessels and the muscles of the mouth all lie beneath it."),
    ],
    "anat_close_html": "Natural, lasting results come from working on the deep structures — <em>not from pulling the skin.</em>",
    "areas_label": "— Two areas, one focus", "areas_h_html": "Face. <em>Breast.</em>",
    "areas_lead": "I have concentrated my practice on the face and neck and on the breast — to offer every patient the best possible result.",
    "face_list": "Facelift · Eyelid surgery · Brow lift · Lip lift · Otoplasty · Chin · Aesthetic medicine",
    "breast_list": "Breast lift · Augmentation · Reduction · Gynecomastia",
    "recon_link": "Reconstructive surgery — restoring the face after skin-cancer surgery",
    "teacher": "— Teacher & author", "teacher_h_html": "A surgeon who <em>teaches</em> surgeons.",
    "atlas_lead_html": "Editor of <em>{title}</em> ({publisher}): more than <strong data-count=\"320\">320</strong> original photographs guiding the reader, step by step, from pre-operative planning to post-operative care.",
    "facts": [("Ph.D.", "University of Genoa"), ("Lecturer", "Master in Aesthetic Surgery, University of Pavia"), ("Courses", "Nice · Madrid · Cremona"), ("Fellowships", "Face & breast")],
    "discover_academy": "Discover the Academy", "atlas_alt": "Cover of Stepwise Atlas of Aesthetic Medicine and Surgery, edited by Giuseppe Colombo (Springer)",
    "discretion": "— Discretion", "discretion_aria": "Discretion",
    "place": "— The place", "lugano_h_html": "Lugano, <em>Switzerland.</em>",
    "lugano_p": "Clinica Sant'Anna — practice and operating theatre under one roof.",
    "convo_h_pre": "Begin with a", "convo_word": "conversation",
    "convo_lead": "Tell us what you would like to discuss. The secretary's office answers {hours}.",
}
