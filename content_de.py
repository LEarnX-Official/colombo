"""German content — translated faithfully from the doctor's Italian originals.
Anything not defined here falls back to content.py."""
import content as EN

LANG = "de"
MONTHS = "Januar Februar März April Mai Juni Juli August September Oktober November Dezember".split()

PATHS = {
    "home": "/de/", "philosophy": "/de/philosophie/", "face": "/de/gesicht/", "breast": "/de/brust/",
    "reconstructive": "/de/rekonstruktive-chirurgie/", "academy": "/de/akademie/", "journal": "/de/akademie/journal/",
    "contact": "/de/kontakt/",
}
PROC_SLUGS = {
    "facelift": "facelift", "blepharoplasty": "lidstraffung", "brow-lift": "brauenlifting",
    "lip-lift": "lip-lift", "otoplasty": "ohrenkorrektur", "chin": "kinnkorrektur",
    "hyaluronic-acid": "hyaluronsaeure", "botulinum-toxin": "botulinumtoxin", "biorevitalisation": "biorevitalisierung",
    "mastopexy": "bruststraffung", "augmentation": "brustvergroesserung", "reduction": "brustverkleinerung",
    "gynecomastia": "gynaekomastie",
}
NAV_LABELS = {"philosophy": "Philosophie", "face": "Gesicht", "breast": "Brust", "academy": "Akademie", "contact": "Kontakt"}

SITE = dict(EN.SITE)
SITE.update({
    "role": "Facharzt für Plastische, Rekonstruktive und Ästhetische Chirurgie · Ph.D. Universität Genua",
    "hours": "Montag bis Freitag, 10–18 Uhr",
    "locations": [
        {"key": "lugano", "city": "Lugano", "country": "Schweiz", "role": "Praxis und Operationssaal",
         "lines": ["Clinica Sant'Anna", "Via Sant'Anna 1"], "extra": "Praxis: Via Nassa 7 · Via Clemente Maraini 8"},
        {"key": "zurich", "city": "Zürich", "country": "Schweiz", "role": "Chirurgische Beratungen", "lines": ["Nach Vereinbarung"], "extra": ""},
        {"key": "italy", "city": "Italien", "country": "", "role": "Beratungen", "lines": ["Nach Vereinbarung"], "extra": ""},
    ],
    "phones": [
        {"label": "Schweiz", "display": "+41 76 297 69 87", "tel": "+41762976987"},
        {"label": "Italien", "display": "+39 342 327 5364", "tel": "+393423275364"},
    ],
})

QUOTES = dict(EN.QUOTES)
QUOTES.update({
    "measure_en": "Das rechte Maß ist das Schönste.",
    "limit_en": "Hasse das Übermaß, respektiere die Grenze.",
    "discretion_en": "Ein seriöser Arzt verrät niemals, wer seine Patienten sind. Misstrauen Sie jedem, der es tut.",
    "naturalness": "Nur ein Wort leitet meine Arbeit: Natürlichkeit. Niemals dem Übermaß nachgeben, niemals Menschen verfremden — sondern nur versuchen, das Beste in ihnen zur Geltung zu bringen.",
})

VIDEOS = {
    "HnflefgVqMM": "Facelift", "852M8oEXm4A": "Was kostet ein Facelift?", "_yyDI8cqhWU": "Verjüngung des Blicks",
    "86dQ-Oy1_eg": "Brustvergrößerung", "o-ksV1W2LeI": "Fettabsaugung (englische Untertitel)", "-9COFP65Fl8": "Die Wahl des Chirurgen: Warnsignale, die man nicht ignorieren sollte",
    "rIZn6oLeCpI": "Interview mit Dr. Giuseppe Colombo", "DIH4McTTDNs": "Decus — Kongressbericht", "U47HAtXf1ao": "Decus — zwei Standorte (englische Untertitel)",
}

AREAS = {
    "face": {
        "title": "Gesicht",
        "lede": "Facelift, Lider, Brauen, Lippen, Ohren und Kinn — und ästhetische Medizin für die Haut. Jede Behandlung folgt demselben Prinzip: das Gesicht zu respektieren, das bereits Ihres ist.",
        "intro": "Beim Gesicht gilt meine besondere Aufmerksamkeit dem Facelift und der Lidchirurgie.",
        "meta": "Plastische Gesichtschirurgie und ästhetische Medizin von Dr. Giuseppe Colombo in Lugano: Facelift, Lidstraffung, Brauenlifting, Lip-Lift, Ohrenkorrektur, Kinnkorrektur, Hyaluronsäure, Botulinumtoxin und Biorevitalisierung.",
        "group_titles": ["Gesichtschirurgie", "Ästhetische Medizin"],
    },
    "breast": {
        "title": "Brust",
        "lede": "Straffung, Vergrößerung, Verkleinerung und Gynäkomastie. Jeder Eingriff wird für den Körper gewählt, den wir vor uns haben — niemals für einen Trend.",
        "intro": "Bei der Brust widme ich mich der Verkleinerung, der Straffung und der korrigierenden Vergrößerung.",
        "meta": "Brustchirurgie von Dr. Giuseppe Colombo in Lugano: Bruststraffung, Brustvergrößerung, Brustverkleinerung und Gynäkomastie.",
        "group_titles": ["Brustchirurgie"],
    },
}

PROCEDURES = {
    "facelift": {
        "group": "Gesichtschirurgie", "title": "Facelift", "subtitle": "Hals- und Gesichtslifting",
        "lede": "Der wichtigste Eingriff in der Chirurgie der Gesichtsalterung: Er bringt die Strukturen, die sich mit den Jahren verschoben haben, dauerhaft wieder in Position.",
        "body": [
            "Das Gesicht altert in einem Tempo, das von Mensch zu Mensch verschieden ist — je nach familiärer Veranlagung und Lebensweise. Die Alterung betrifft alle Elemente des Gesichts: Haut, Unterhautfettgewebe und die tiefe Muskulatur. Das Ergebnis ist eine Schwere, die oft im unteren Gesichtsdrittel und am Hals besonders sichtbar wird.",
            "In diesen Fällen kann nur das Hals- und Gesichtslifting — der wichtigste Eingriff in der Chirurgie der Gesichtsalterung — diese Veränderungen korrigieren, indem es die betroffenen Strukturen dauerhaft neu positioniert. Haut und vor allem die tieferen Gewebe, insbesondere die Muskulatur, werden behutsam gestrafft und stabilisiert, um die richtigen Proportionen und die natürliche Harmonie des Gesichts wiederherzustellen.",
            "Entscheidend ist die genaue Kenntnis des SMAS, der Gewebeschicht unter Haut und Fett. Die Nerven, die das Gesicht bewegen, die Speicheldrüsen, die wichtigsten Gefäße und die Muskeln, die den Mund symmetrisch bewegen, liegen alle darunter.",
            "Die Chirurgie kann weder die Haut eines Fünfundzwanzigjährigen zurückgeben noch jede Falte verschwinden lassen. Deshalb ist es wesentlich, dass der Patient den gesamten Ablauf versteht: Seine Mitwirkung ist für das beste Ergebnis grundlegend.",
        ],
        "facts": [("Behandelte Schichten", "Haut, Unterhautfett und tiefe Muskulatur (SMAS)"), ("Hauptbereich", "Unteres Gesichtsdrittel und Hals"), ("Prinzip", "Zug auf die tiefen Strukturen — nicht auf die Haut")],
        "quote": "Indem wir die Kraft auf die tiefen Strukturen und nicht auf die Haut ausüben, vermeiden wir Spannung auf den Narben — und feste, tiefe Fixierungen verleihen dem Ergebnis eine weit dauerhaftere Beständigkeit.",
        "meta": "Hals- und Gesichtslifting von Dr. Giuseppe Colombo, Lugano: Neupositionierung der tiefen Strukturen (SMAS) für ein natürliches, dauerhaftes Ergebnis.",
    },
    "blepharoplasty": {
        "group": "Gesichtschirurgie", "title": "Lidstraffung", "subtitle": "Blepharoplastik",
        "lede": "Die Augen zeigen als Erste das Vergehen der Zeit. Die Lidchirurgie schenkt einen ausgeruhten Blick — bei voller Achtung von Funktion und Ausdruck des Auges.",
        "body": [
            "Wer sich nach einer Blepharoplastik erkundigt, ist meist eine Frau zwischen vierzig und fünfundvierzig oder ein etwas älterer Mann, mit ansonsten gut strukturiertem Gesicht, der sich an überschüssiger Haut — und manchmal Fett — um die Augen stört. Es sind aktive Menschen, die es nicht mögen, morgens müde auszusehen, obwohl sie es nicht sind.",
            "Bei der Oberlidstraffung werden die überschüssige Haut und ein schmaler Streifen des Ringmuskels entfernt, wodurch die Lidfalte klarer wird. Die Fettpolster werden in der richtigen Menge und an der richtigen Stelle korrigiert — der einzige Weg zu einem natürlichen Ergebnis ohne „eingefallene“ Augen. Die Narbe verbirgt sich in der natürlichen Lidfalte.",
            "Die Unterlidstraffung erfolgt heute fast immer von der Innenseite des Lides (transkonjunktival): Es entsteht keine äußere Narbe und, noch wichtiger, der Ringmuskel, der die Form des Unterlids hält, bleibt erhalten. Ist der äußere Augenwinkel abgesunken, kann eine Kanthopexie ihn wieder anheben und das Auge neu definieren.",
            "Bei mehr als der Hälfte der Patienten, die für eine Oberlidstraffung in Frage kommen, liegt das Problem nicht nur in überschüssiger Lidhaut, sondern auch in einer abgesunkenen Augenbraue, vor allem in ihrem äußeren Teil. In diesen Fällen verbindet die ideale Behandlung die Lidstraffung mit einem Brauenlifting.",
        ],
        "facts": [("Anästhesie", "Lokal, bei Bedarf mit leichter Sedierung"), ("Entlassung", "Meist innerhalb von 24 Stunden"), ("Fadenentfernung", "Nach 4–7 Tagen"), ("Normales Aussehen", "Nach 7–10 Tagen"), ("Make-up & Sonne", "Nach der ersten Woche, mit vollem Sonnenschutz"), ("Endergebnis", "Nach etwa einem Jahr"), ("Haltbarkeit", "Korrekturen sind selten vor 10–15 Jahren nötig")],
        "quote": "Es ist besser, wenn einige kleine Fältchen bleiben, um die ursprüngliche Form des Auges so weit wie möglich zu bewahren.",
        "meta": "Ober- und Unterlidstraffung von Dr. Giuseppe Colombo, Lugano: natürliche Verjüngung des Blicks, verborgene Narben, Erholung in 7–10 Tagen.",
    },
    "brow-lift": {
        "group": "Gesichtschirurgie", "title": "Brauenlifting", "subtitle": "Anhebung der Augenbraue",
        "lede": "Eine abgesunkene Augenbraue wird oft unterschätzt — von Patienten und leider auch von manchen Chirurgen.",
        "body": [
            "Die Ptosis — das Absinken — der Augenbraue ist ein häufig unterschätzter Teil der Gesichtsalterung. Bei mehr als der Hälfte der Patienten, die für eine Oberlidstraffung in Frage kommen, liegt das Problem nicht nur in überschüssiger Lidhaut, sondern auch in einer abgesunkenen Braue, vor allem in ihrem äußeren Teil. Die ideale Behandlung muss daher die Lidstraffung mit einem Brauenlifting verbinden.",
            "Die gebräuchlichsten und wirksamsten Methoden sind ein sogenannter „direkter“ Zugang mit einem leicht zu kaschierenden Schnitt am oberen Rand der Braue — oder, häufiger bevorzugt, ein transtemporaler Zugang: ein kleiner Schnitt im behaarten Kopfbereich, der völlig unsichtbar bleibt und über den das äußere Drittel der Braue angehoben wird.",
        ],
        "facts": [("Zugang", "Transtemporal (Schnitt im Haaransatz verborgen) oder direkt"), ("Angehobener Bereich", "Das äußere Drittel der Augenbraue"), ("Oft kombiniert mit", "Oberlidstraffung")],
        "meta": "Brauenlifting von Dr. Giuseppe Colombo, Lugano: Anhebung des äußeren Brauendrittels über einen unsichtbaren Schnitt im Haaransatz.",
    },
    "lip-lift": {
        "group": "Gesichtschirurgie", "title": "Lip-Lift", "subtitle": "Oberlippenlifting",
        "lede": "Eine dauerhafte Neuformung der Oberlippe — definiert, natürlich und harmonisch, ohne weitere Filler.",
        "body": [
            "Das Lip-Lift, die Straffung der Oberlippe, wird von Patienten immer häufiger gewünscht. Mit dem Alter verliert die Oberlippe oft an Definition am Amorbogen, flacht ab und wird länger: Der Abstand zwischen Columella — dem Nasensteg — und Lippenrot nimmt zu.",
            "Es gibt mehrere Techniken mit unterschiedlichen Schnitten. Die gebräuchlichste, die eine gut verborgene Narbe in der Nasenflügel-Wangen-Falte und an der Columella garantiert, ist die „Bullhorn“-Technik. Sie ergibt eine klar definierte, natürliche und harmonische Oberlippe, die keine weiteren Filler-Injektionen benötigt.",
        ],
        "facts": [("Technik", "„Bullhorn“-Lip-Lift"), ("Narbe", "Am Nasenansatz verborgen (Nasenflügelfalte und Columella)"), ("Ergebnis", "Dauerhafte Neuformung — keine weiteren Filler nötig")],
        "meta": "Lip-Lift von Dr. Giuseppe Colombo, Lugano: die Bullhorn-Technik für eine definierte, natürliche Oberlippe mit verborgener Narbe.",
    },
    "otoplasty": {
        "group": "Gesichtschirurgie", "title": "Ohrenkorrektur", "subtitle": "Otoplastik",
        "lede": "Die Form der Ohrmuschel durch Modellierung des Knorpels korrigieren — mit einer Narbe, die vollständig hinter dem Ohr verborgen ist.",
        "body": [
            "Die Otoplastik ist ein chirurgischer Eingriff zur Korrektur von Formfehlern der Ohrmuschel. Am häufigsten sind die sogenannten „abstehenden Ohren“: Die Ohrmuschel steht wegen eines offenen Winkels zum Kopf und des Fehlens der Anthelix, der Hauptfalte des Ohrs, deutlich ab.",
            "Der Eingriff verändert Form, Größe und Stellung der Ohrmuschel durch eine Modellierung des Knorpelgerüsts — der Knorpel wird geschwächt und, falls nötig, mit stabilisierenden Nähten geformt, die die natürlichen Falten und Rundungen der Ohranatomie wiederherstellen. Die verbleibende Narbe ist vollständig in der Furche hinter dem Ohr verborgen.",
            "Ab einem Alter von fünf oder sechs Jahren haben die Ohren eine Größe und Entwicklung erreicht, die einen Eingriff erlaubt; viele Patienten kommen erst als Erwachsene, zwischen zwanzig und dreißig, zum ersten Mal.",
        ],
        "facts": [("Anästhesie", "Lokal bei Erwachsenen, Vollnarkose bei Kindern"), ("Ab dem Alter von", "5–6 Jahren"), ("Narbe", "In der Furche hinter dem Ohr verborgen"), ("Kontrolle", "Am Tag nach dem Eingriff"), ("Danach", "Mindestens eine Woche ein weiches Stirnband; Haarewaschen nach der ersten Woche")],
        "meta": "Ohrenkorrektur (Otoplastik) von Dr. Giuseppe Colombo, Lugano: Modellierung des Knorpels mit verborgener Narbe hinter dem Ohr.",
    },
    "chin": {
        "group": "Gesichtschirurgie", "title": "Kinnkorrektur", "subtitle": "Mentoplastik",
        "lede": "Ein harmonisches Profil hängt vom Kinn ebenso ab wie von der Nase.",
        "body": [
            "Bei manchen Patienten reicht eine Nasenkorrektur allein für ein harmonisches Profil nicht aus, weil das Kinn zu weit zurückliegt. Die Nase drastisch zu verkleinern, um sie dem Kinn anzupassen, wäre der falsche Ansatz.",
            "Ideal ist eine genaue Analyse des Profils: Die Nasenspitze sollte etwas weiter nach vorne ragen als das Kinn. Liegt das Kinn stark zurück, sieht der Plan entweder ein Kinnimplantat oder körpereigenes Fett (Lipofilling) vor.",
            "Im Mund, hinter der Unterlippe, werden zwei kleine Schnitte von etwa zwei bis drei Zentimetern gesetzt. Die Implantate bestehen aus Silikon — fest und zugleich flexibel, sodass der Chirurg sie während des Eingriffs in die gewünschte Form bringen kann. Die Schnitte werden mit resorbierbaren Fäden verschlossen.",
        ],
        "facts": [("Anästhesie", "Lokal mit Sedierung; Vollnarkose in Kombination mit einer Nasenkorrektur"), ("Schnitte", "Im Mund, hinter der Unterlippe"), ("Optionen", "Silikonimplantat oder Lipofilling"), ("Erholung", "Gewohnte Aktivitäten nach etwa einer Woche")],
        "meta": "Kinnkorrektur (Mentoplastik) von Dr. Giuseppe Colombo, Lugano: Harmonisierung des Profils mit Silikonimplantat oder Lipofilling.",
    },
    "hyaluronic-acid": {
        "group": "Ästhetische Medizin", "title": "Hyaluronsäure", "subtitle": "Ästhetische Medizin",
        "lede": "Ein natürlicher Bestandteil der Haut, dort ersetzt, wo die Zeit ihn verringert hat — für Festigkeit, Feuchtigkeit und Ausstrahlung.",
        "body": [
            "Hyaluronsäure ist einer der Hauptbestandteile des Bindegewebes der Lederhaut, in das die Kollagen- und elastischen Fasern eingebettet sind. Indem sie Wasser bindet, erhöht sie Elastizität, Feuchtigkeit und Spannkraft der Gewebe und hat zudem wundheilende und entzündungshemmende Eigenschaften.",
            "Ihre Konzentration in der Haut nimmt mit dem Alter ab — eine der Hauptursachen der Hautalterung. Injizierte Hyaluronsäure strafft reife Haut, regt die Zellfunktion an und gibt ihr die verlorene Festigkeit und Leuchtkraft zurück. Deshalb wird sie seit vielen Jahren erfolgreich in der ästhetischen Dermatologie eingesetzt.",
            "Sie wird im Labor hergestellt und hat, abgesehen von vereinzelten Überempfindlichkeiten, keine Nebenwirkungen. Der Arzt injiziert sie mit einer sehr feinen Nadel in die Lederhaut oder das Unterhautgewebe, je nach Bereich und Tiefe. Die füllende oder glättende Wirkung hängt vom Hauttyp sowie von Qualität und Menge der verwendeten Hyaluronsäure ab.",
        ],
        "facts": [("Injektion", "Sehr feine Nadel, in Lederhaut oder Unterhautgewebe"), ("Dauer", "Nicht dauerhaft — Wiederholung etwa alle 6–12 Monate"), ("Nicht geeignet bei", "Schwangerschaft, Stillzeit, Kollagenosen oder autoimmunen Hauterkrankungen")],
        "meta": "Behandlungen mit Hyaluronsäure von Dr. Giuseppe Colombo, Lugano: Feuchtigkeit, Festigkeit und Ausstrahlung für reife Haut.",
    },
    "botulinum-toxin": {
        "group": "Ästhetische Medizin", "title": "Botulinumtoxin", "subtitle": "Ästhetische Medizin",
        "lede": "Mimikfalten mildern — nicht auslöschen —, die das Gesicht müde wirken lassen.",
        "body": [
            "Botulinumtoxin ist eine hochgereinigte Substanz aus dem Bakterium Clostridium botulinum, die die übermäßige Kontraktion bestimmter Gesichtsmuskeln vorübergehend und örtlich vermindert — und damit die Bildung dynamischer Falten im oberen Gesichtsdrittel: Stirn, Brauen, Zornesfalte und Krähenfüße.",
            "Diese Falten lassen das Gesicht müde wirken, besonders um die Augen. Das eigentliche Ziel der Behandlung ist, den Augen und ihrer Umgebung ein frisches, ausgeruhtes Aussehen zu geben — am Abend ebenso wie am Morgen. Anders als Hyaluronsäure-Filler füllt es nicht auf.",
            "Es wird auch eingesetzt, um einen vergrößerten Kaumuskel (Masseter), der das Gesicht kantig wirken lässt, zu verschlanken und so eine ovalere Form zurückzugeben; zur Behandlung der senkrechten Platysmabänder am Hals; und in kleinen Dosen zur Straffung der seitlichen Halspartien für alle, die ein Halslifting hinauszögern möchten. Eine weitere wichtige Indikation ist die Hyperhidrose — übermäßiges Schwitzen unter den Achseln, an Händen oder Füßen.",
        ],
        "facts": [("Anästhesie", "Nicht nötig — praktisch schmerzfrei"), ("Wirkungseintritt", "Nach etwa 3 Tagen"), ("Dauer", "Etwa 5 Monate, danach kann wiederholt werden"), ("Bereiche", "Stirn, Brauen, Zornesfalte, Krähenfüße · Masseter · Hals")],
        "quote": "Mehr als jedes andere Verfahren hängt dieses vom Arzt ab. Mit ästhetischem Gespür und Maß eingesetzt, im Einklang mit den Erwartungen des Patienten, zielt es nicht darauf, jede Unvollkommenheit auszulöschen, sondern die Falten zu mildern, die das Gesicht altern lassen.",
        "meta": "Botulinumtoxin von Dr. Giuseppe Colombo, Lugano: Mimikfalten mit Maß mildern — nie ein starrer Ausdruck.",
    },
    "biorevitalisation": {
        "group": "Ästhetische Medizin", "title": "Biorevitalisierung", "subtitle": "Ästhetische Medizin",
        "lede": "Die Qualität der Haut selbst verbessern — ohne die Volumen des Gesichts zu verändern.",
        "body": [
            "Die Biorestrukturierung des Gesichts ist eine fortschrittliche Behandlung der ästhetischen Medizin, die die Gewebequalität verbessert, indem sie die natürliche Regeneration der Haut anregt, ohne die Volumen des Gesichts zu verändern. Sie soll nicht „auffüllen“, sondern die biologische Funktion der Haut reaktivieren — gegen Erschlaffung, Feuchtigkeitsverlust und den Verlust von Elastizität und Spannkraft.",
            "Sie wirkt auf die verschiedenen Hautschichten, fördert die Bildung von Kollagen und Elastin und verbessert mit der Zeit die Struktur der Lederhaut. Sie eignet sich bei ersten Zeichen der Hautalterung ebenso wie zur Erhaltung oder zur Vorbereitung auf invasivere Eingriffe.",
            "Die Behandlung besteht aus gezielten Mikroinjektionen bioregenerativer Substanzen, ausgewählt nach den Eigenschaften der Haut und den klinischen Zielen. Das Ergebnis ist ein frischeres, festeres und strahlenderes Gesicht — eine natürliche, fortschreitende Verjüngung, die Anatomie und Ausdruck jedes Menschen respektiert.",
        ],
        "facts": [("Rahmen", "Ambulante Behandlung, gut verträglich"), ("Ausfallzeit", "Keine nennenswerte Erholungszeit"), ("Geeignet für", "Erste Alterungszeichen, Erhaltung oder Vorbereitung auf eine Operation")],
        "meta": "Biorevitalisierung von Dr. Giuseppe Colombo, Lugano: Mikroinjektionen, die die Hautqualität verbessern, ohne Volumen zu verändern.",
    },
    "mastopexy": {
        "group": "Brustchirurgie", "title": "Bruststraffung", "subtitle": "Mastopexie",
        "lede": "Eine abgesunkene, erschlaffte Brust anheben und neu formen.",
        "body": [
            "Die Mastopexie korrigiert ein übermäßiges Absinken der Brust. Sie strafft eine hängende, entleerte Brust, verbessert Form und Volumen und korrigiert die Folgen von Schwangerschaft, Stillzeit, starker Gewichtsabnahme und natürlicher Alterung. Ziel ist, so weit wie möglich ein volles, festes Aussehen zurückzugewinnen.",
            "Die Technik richtet sich nach dem Grad der Ptosis. In leichteren Fällen genügt es, einen Hautring um den Warzenhof zu entfernen, um die Brust in die richtige Position zu bringen; die Narbe lässt sich am Übergang zwischen Warzenhof und Haut gut kaschieren. In schwereren Fällen muss mehr Haut entfernt werden, und zur Narbe um den Warzenhof kommen meist eine senkrechte Narbe bis zur Unterbrustfalte und eine waagrechte Narbe in dieser Falte (umgekehrtes „T“).",
            "In manchen Fällen werden die Entfernung der überschüssigen Haut und die Anhebung der Brust mit Implantaten der neuesten Generation kombiniert, für mehr Volumen (augmentierende Mastopexie).",
        ],
        "facts": [("Korrigiert", "Folgen von Schwangerschaft, Stillzeit, Gewichtsverlust und Alterung"), ("Narben", "Um den Warzenhof in leichten Fällen; umgekehrtes „T“ in schwereren Fällen"), ("Option", "Kombiniert mit Implantaten für mehr Volumen")],
        "meta": "Bruststraffung (Mastopexie) von Dr. Giuseppe Colombo, Lugano: Position und Form der Brust nach Schwangerschaft, Gewichtsverlust oder Alterung wiederherstellen.",
    },
    "augmentation": {
        "group": "Brustchirurgie", "title": "Brustvergrößerung", "subtitle": "Augmentationsmammaplastik",
        "lede": "Mehr Volumen — aus den richtigen Gründen gewählt, und nur dann, wenn es die richtige Antwort ist.",
        "body": [
            "Manchmal ist die Vergrößerung allein nicht die richtige Wahl für das beste Ergebnis. Geht ein Volumenmangel mit einer abgesunkenen Brust (Ptosis) einher, kann ein Implantat allein das Erschlaffen nicht korrigieren — es kann es sogar verschlimmern. In diesen Fällen ist eine Bruststraffung in Kombination mit Implantaten die ideale Lösung.",
            "Die heutigen Silikongel-Implantate mit einer Außenhülle aus Silikonelastomer, ausgewählt wegen ihrer Festigkeit, Haltbarkeit und Flexibilität, kommen dem Aussehen und Gefühl einer natürlichen Brust am nächsten.",
        ],
        "facts": [("Implantate", "Silikongel der neuesten Generation"), ("Bei Ptosis", "Kombiniert mit einer Bruststraffung für das beste Ergebnis")],
        "quote": "Die Mode sollte NIEMALS die Entscheidung bestimmen, den eigenen Körper zu verändern. Die Gründe für einen ästhetischen Eingriff müssen klar, ernsthaft und überlegt sein — getragen vom Wunsch, sich wohlzufühlen und das äußere mit dem inneren Erscheinungsbild in Einklang zu bringen.",
        "meta": "Brustvergrößerung von Dr. Giuseppe Colombo, Lugano: Silikongel-Implantate, bei Bedarf kombiniert mit einer Straffung, für ein natürliches Ergebnis.",
    },
    "reduction": {
        "group": "Brustchirurgie", "title": "Brustverkleinerung", "subtitle": "Reduktionsmammaplastik",
        "lede": "Die Brust erleichtern — für ihr Aussehen und für das Wohlbefinden des Körpers.",
        "body": [
            "Die Brustverkleinerung ist der Eingriff bei Gigantomastie oder Hypertrophie der Brustdrüse. Sie erfolgt nicht nur aus ästhetischen, sondern auch aus funktionellen Gründen: Eine zu große, schwere Brust lastet auf der Vorderseite des Körpers und verursacht häufig Schmerzen in Schultern, Nacken und oberer Wirbelsäule.",
            "Eine Verkleinerung um vier bis fünf Größen ist möglich. Der Eingriff hebt zugleich eine zu tief abgesunkene Brust an und füllt ihren oberen Teil.",
            "Die Operationstechniken haben sich im Laufe der Jahre weiterentwickelt und verfeinert — und damit auch die Qualität der Narben. Bei späteren Kontrollen — Mammographie, Ultraschall oder CT — sollten Radiologe und Gynäkologe über die Operation informiert werden: Das hilft ihnen, die Befunde richtig zu deuten.",
        ],
        "facts": [("Gründe", "Ästhetisch und funktionell (Schulter-, Nacken- und Rückenschmerzen)"), ("Verkleinerung", "Bis zu vier oder fünf Größen"), ("Zudem", "Hebt die Brust an und füllt ihren oberen Teil")],
        "meta": "Brustverkleinerung von Dr. Giuseppe Colombo, Lugano: Entlastung vom Gewicht einer großen Brust, mit angehobener, natürlicher Form.",
    },
    "gynecomastia": {
        "group": "Brustchirurgie", "title": "Gynäkomastie", "subtitle": "Korrektur der männlichen Brust",
        "lede": "Eine männliche Brust korrigieren, die weiblich wirkt.",
        "body": [
            "Der Eingriff korrigiert eine typisch männliche Veränderung: eine starke Fettansammlung in der Brust (falsche Gynäkomastie) oder von Drüsengewebe (echte Gynäkomastie). In manchen Fällen liegen beide Komponenten vor (gemischte Gynäkomastie).",
            "Er wird häufig von Männern zwischen zwanzig und vierzig gewünscht, die sich mit einer Brust unwohl fühlen, die eher weiblich als männlich wirkt.",
        ],
        "facts": [("Formen", "Falsch (Fett), echt (Drüse) oder gemischt"), ("Typische Patienten", "Männer zwischen 20 und 40 Jahren")],
        "meta": "Gynäkomastie: Korrektur der männlichen Brust von Dr. Giuseppe Colombo, Lugano.",
    },
}

RECONSTRUCTIVE = {
    "title": "Rekonstruktive Chirurgie", "drawing": "dash-arrow",
    "lede": "Form und Funktion wiederherstellen — mit besonderem Augenmerk auf das Gesicht nach Hautkrebschirurgie.",
    "focus": "Die rekonstruktive Chirurgie lag mir immer am Herzen. In diesem Bereich widme ich mich ausschließlich der Rekonstruktion des Gesichts nach onkologischer Hautchirurgie.",
    "areas": ["Komplexe dermatologische Chirurgie", "Onkologische dermatologische Chirurgie", "Rekonstruktive Gesichtschirurgie"],
    "body": ["Ziel der rekonstruktiven Chirurgie ist es, Form und Funktion geschädigter oder verformter Regionen von Gesicht und Körper wiederherzustellen. Ein Eingriff kann Probleme durch Verletzungen, Tumore, Verbrennungen, angeborene Fehlbildungen, Infektionen, Gesichtsfrakturen und Nervenverletzungen verbessern oder beheben."],
    "techniques": [
        ("Hauttransplantate", "Übertragung von Haut von einer Körperstelle auf eine andere, um einen Bereich mit neuer Haut zu bedecken."),
        ("Lappenplastiken", "Übertragung von Haut, Fett, Muskel, Knorpel und/oder Knochen aus benachbarten Regionen, ohne die Blutversorgung zu unterbrechen, um Weichteildefekte zu verschließen."),
        ("Autotransplantate", "Entnahme von Gewebe — Knorpel, Sehne, Fett, Lederhaut, Muskel, Nerv oder Knochen — an anderen Körperstellen, um der Rekonstruktion das Nötige zu liefern."),
        ("Mikrochirurgie", "Rekonstruktion fehlenden Gewebes durch Übertragung von einer anderen Stelle, mit mikrochirurgischen Techniken zur Wiederherstellung von Blutversorgung und Nervenfunktion."),
    ],
    "meta": "Rekonstruktive Chirurgie von Dr. Giuseppe Colombo, Lugano: Gesichtsrekonstruktion nach Hautkrebschirurgie, Transplantate, Lappenplastiken und Mikrochirurgie.",
}

ABOUT = [
    "Ich bin Facharzt für plastische und rekonstruktive Chirurgie. Zu meinem großen Glück durfte ich während meiner Ausbildung bei großen Meistern dieses faszinierenden Fachs lernen — mit langen Aufenthalten in Spanien und Frankreich und natürlich in Italien. Über Jahre war ich Berater renommierter Kliniken wie des Ospedale Evangelico Internazionale in Genua.",
    "Um meinen Patienten das bestmögliche Ergebnis zu bieten, habe ich meine Aufmerksamkeit und meine Praxis auf Gesicht, Hals und Brust konzentriert: Facelift und Lidstraffung beim Gesicht; Verkleinerung, Straffung und korrigierende Vergrößerung bei der Brust. Die rekonstruktive Chirurgie lag mir immer am Herzen; hier widme ich mich ausschließlich der Rekonstruktion des Gesichts nach onkologischer Hautchirurgie.",
    "Über die Jahre habe ich zahlreiche Präparationskurse organisiert, um Kollegen die Möglichkeit zu geben, meine Erfahrung und ihre eigene zu teilen. Im selben Geist habe ich einen bedeutenden Chirurgie-Atlas herausgegeben. Mit großer Freude empfange ich junge Ärzte und Kollegen in meinen Operationssälen. Medizin und Chirurgie machen rasante Fortschritte und erzielen immer bessere Ergebnisse, wenn alle Ärzte ihre Erfahrung teilen — das ist mein Geist.",
    "Was meine Philosophie in der ästhetischen Medizin und plastischen Chirurgie betrifft, leitet ein einziges Wort meine Arbeit: Natürlichkeit. Niemals dem Übermaß nachgeben, niemals Menschen verfremden — sondern nur versuchen, das Beste in ihnen zur Geltung zu bringen.",
]

MILESTONES = [
    ("2005", "Studienabschluss in Medizin und Chirurgie", "Universität Genua — 110/110 cum laude, mit der Medaille für akademische Verdienste. Arbeit: experimentelle Studie zur Gewebeexpansion."),
    ("Facharzt", "Plastische, Rekonstruktive und Ästhetische Chirurgie", "Universität Genua — Erster bei der Aufnahmeprüfung; Abschluss 50/50 cum laude. Arbeit: „Anatomie und chirurgische Techniken der Gesichtsverjüngung, Behandlung des SMAS. Entwicklung der Ergebnisse im Lauf der Zeit.“"),
    ("2007–08", "SICPRE-Stipendium", "Verliehen von der Italienischen Gesellschaft für Plastische, Rekonstruktive und Ästhetische Chirurgie für anatomische Präparation."),
    ("2008–10", "Ausbildung bei Meistern", "Villa Bella, Salò (Prof. Botti) · Akademie für Humananatomie, Brüssel · Clínica Quirón (Dr. Tapia), Gesichtsverjüngung und dreifacher SMAS-Lappen."),
    ("2009", "Brustchirurgie in Genf und Lyon", "Senologie, Universitätsspital Genf (HUG), EUSOMA-zertifiziertes europäisches Referenzzentrum · Plastische und rekonstruktive Chirurgie, Centre Léon Bérard, Lyon."),
    ("Seit 2008", "Anatomie in Nizza", "Regelmäßige anatomische Präparation am Institut für Humananatomie der Universität Sophia-Antipolis, Nizza — Brust- und kraniofaziale Region."),
    ("2010–18", "Leiter von Präparationskursen", "Theoretisch-praktische Kurse in Nizza und Madrid: Gesicht, Brust, Mikrochirurgie, Rhinoplastik und Nahttechnik."),
    ("2013–15", "Co-Direktor, Ospedale Evangelico Internazionale", "Plastische und Rekonstruktive Chirurgie, Genua — und Direktor des dortigen Exzellenzzentrums für plastische Chirurgie."),
    ("Heute", "Autor und Dozent", "Herausgeber des Stepwise Atlas of Aesthetic Medicine and Surgery (Springer) · Dozent, Master in Ästhetischer Chirurgie, Universität Pavia."),
]

CV_GROUPS = [
    ("Ausbildung", [
        "1999 — Humanistisches Abitur (Maturità classica).",
        "1999–2005 — Studium der Medizin und Chirurgie, Universität Genua.",
        "2005 — Studienabschluss in Medizin und Chirurgie, Universität Genua, 110/110 cum laude mit der Medaille für akademische Verdienste. Arbeit: experimentelle Studie zur Gewebeexpansion, in Zusammenarbeit zwischen dem Institut für Biochemie und dem Lehrstuhl für Plastische Chirurgie.",
        "Erster Platz bei der Aufnahmeprüfung der Facharztschule für Plastische, Rekonstruktive und Ästhetische Chirurgie, Universität Genua.",
        "Facharztdiplom in Plastischer, Rekonstruktiver und Ästhetischer Chirurgie, 50/50 cum laude. Arbeit: „Anatomie und chirurgische Techniken der Gesichtsverjüngung, Behandlung des SMAS. Entwicklung der Ergebnisse im Lauf der Zeit.“",
        "Europäisches interuniversitäres Diplom für chirurgische Praxis in der Onkologie (DIU Européen de Pratiques Chirurgicales en Cancérologie — Universitäten Lyon, Nantes, Genua, Nancy, Paris).",
    ]),
    ("Positionen", [
        "Seit 2012 — Leiter Plastische und Ästhetische Chirurgie, Villa Serena, Genua.",
        "Juni 2013 – Oktober 2015 — Co-Direktor Plastische und Rekonstruktive Chirurgie, Ospedale Evangelico Internazionale, Genua.",
        "Direktor des Exzellenzzentrums für plastische Chirurgie — Ospedale Evangelico Internazionale, Genua.",
        "Dozent, Master in Ästhetischer Chirurgie — Universität Pavia.",
        "2011–2013 — Berater für Plastische Chirurgie, Policlinico di Monza.",
        "April 2011 – Dezember 2013 — SUMAI-Berater für Plastische und Rekonstruktive Chirurgie, ASL2 Savonese, Spital Cairo Montenotte.",
        "Seit Dezember 2010 — Gerichtlicher Sachverständiger für Plastische, Rekonstruktive und Ästhetische Chirurgie, Gericht Savona.",
        "Seit Januar 2010 — Vorstandsmitglied der Società Polispecialistica dei Giovani Chirurghi, Sektion Ligurien.",
    ]),
    ("Klinische Ausbildung", [
        "2008, 2010 — Gastarzt in der Day Clinic Villa Bella, Salò (Prof. Botti): Anatomie von Gesicht, Hals und Brust und die wichtigsten Techniken der ästhetischen Chirurgie.",
        "Oktober–November 2008 — Akademie für Humananatomie, Brüssel: theoretisch-praktischer Kurs mit Präparation am Körperspender zu den wichtigsten Techniken der ästhetischen Gesichtschirurgie.",
        "März–Juni 2009 — Assistenzarzt, Senologie, Universitätsspital Genf (HUG), Prof. Jean-Bernard Dubuisson — EUSOMA-zertifiziertes europäisches Referenzzentrum.",
        "Juli 2009 und Juni–Juli 2010 — Gastarzt an der Clínica Quirón, plastische und ästhetische Chirurgie (Dr. Tapia): Gesichtsverjüngung, Facelift mit dreifachem SMAS-Lappen.",
        "Oktober 2009 — Assistenzarzt, Plastische und Rekonstruktive Chirurgie, Centre Léon Bérard, Lyon — französisches Referenzzentrum für Brustrekonstruktion.",
        "Seit 2008 — Monatliche anatomische Präparation am Institut für Humananatomie der Universität Sophia-Antipolis, Nizza, mit Schwerpunkt Brust- und kraniofaziale Region.",
    ]),
    ("Mitgliedschaften & Gutachten", [
        "2007–2008 — SICPRE-Stipendium für anatomische Präparation.",
        "2008 — International Delegate, World Society of Anti-Aging Medicine.",
        "Dezember 2008 — Tutor für die Anwendung von Fillern für Q-Med, auf Grundlage seiner klinischen Erfahrung.",
        "Gutachter für in PubMed-Medline indexierte Fachzeitschriften: Minerva Chirurgica (seit 2009), Rare Tumors (seit 2009), Il Giornale di Chirurgia (seit 2010), Minerva Medica, World Journal of Surgical Oncology.",
    ]),
    ("Lehre", [
        "2007–2009 — Dozent für Humananatomie an höheren Schulen in Savona und Albenga.",
        "2010–2018 — Co-Leiter und Leiter theoretisch-praktischer Anatomie- und Chirurgiekurse in Nizza und Madrid (siehe Akademie).",
    ]),
]

ATLAS = dict(EN.ATLAS)
ATLAS.update({
    "role": "Herausgeber",
    "text": [
        "Ein praxisnahes, aktuelles Referenzwerk für alle, die sich der ästhetischen Medizin und Chirurgie nähern oder bereits darin tätig sind. Reich illustriert mit mehr als 320 Originalfotografien und in zwei Teile gegliedert — Theorie und Praxis — führt es den Leser Schritt für Schritt durch alle grundlegenden Aspekte ästhetischer Eingriffe, von der präoperativen Planung bis zur postoperativen Betreuung.",
        "Für junge Chirurgen ebenso wie für erfahrene Fachleute deckt es alle wichtigen anatomischen Bereiche und Techniken ab und vermittelt die wesentlichen Werkzeuge, um Behandlungen sicher und kompetent durchzuführen.",
    ],
    "previous": {"title": EN.ATLAS["previous"]["title"], "note": "Früherer Atlas, herausgegeben von Giuseppe Colombo und Vittorio Ruvolo."},
})

FELLOWSHIP = [
    "Mit großer Freude teilt Dr. Colombo seine Erfahrung mit Kollegen. Wer an einem Fellowship teilnimmt, begleitet ihn in die Kliniken, in denen er operiert, und in die Praxen, in denen er Beratungen und Behandlungen der ästhetischen Medizin durchführt.",
    "Die Hälfte der Eingriffe betrifft das Gesicht, die andere Hälfte die Brust. Das Sekretariat hilft gastierenden Kollegen gern bei der Suche nach einer passenden Unterkunft, wenn sie mehrere Tage bleiben möchten.",
]

COURSES = [
    {"year": "2024", "place": "Cremona · Palazzo Trecchi", "items": [
        {"date": "9.–10. Mai 2024", "title": "Angewandte Anatomie des Gesichts und Techniken der Gesichtsverjüngung — von der Lidstraffung zum Facelift, Schritt für Schritt"},
        {"date": "10. Mai 2024", "title": "Angewandte Anatomie der Nasenpyramide — Rhinoplastik, Schritt für Schritt"},
        {"date": "8. Juni 2024", "title": "Ästhetische Gesichtsmedizin, Live-Präparation — Anatomie, Techniken und Injektionsebenen, Schritt für Schritt"},
    ]},
    {"year": "2018", "place": "Nizza · Universität Sophia-Antipolis", "items": [
        {"date": "6.–7. Februar 2018", "title": "Cadaver Lab — Facelift und Lidstraffung"},
        {"date": "7. Februar 2018", "title": "Cadaver Lab — Rhinoplastik"},
        {"date": "8.–9. Februar 2018", "title": "Cadaver Lab — Brustchirurgie und Gluteoplastik"},
    ]},
    {"year": "2017", "place": "Nizza · Universität Sophia-Antipolis", "items": [
        {"date": "2017", "title": "Praxiskurs ästhetische Medizin — KORU Anatomy & Surgery"},
    ]},
    {"year": "2015", "place": "Nizza · Universität Sophia-Antipolis", "items": [
        {"date": "3.–4. Februar 2015", "title": "Ästhetische plastische Chirurgie und angewandte Anatomie von Gesicht und Hals"},
        {"date": "5.–6. Februar 2015", "title": "Brustkurs"},
        {"date": "6. Februar 2015", "title": "Chirurgische Anatomie der Bauchregion"},
        {"date": "6. Februar 2015", "title": "Chirurgische Nahttechnik am Körperspender"},
    ]},
    {"year": "2013", "place": "Savona", "items": [
        {"date": "8.–9. Juni 2013", "title": "Biennale der Morphodynamischen Chirurgie — Decision Making in der ästhetischen plastischen Chirurgie (Co-Präsident)"},
    ]},
]

COURSES_EARLY = [
    "Nizza, Dezember 2010 — Anatomie und chirurgische Grundtechniken der Brust- und Gesäßregion; Anatomie und mikrochirurgische Grundtechniken (anterolateraler Oberschenkel, radial, peroneal, dorsal).",
    "Nizza, Juni 2011 — Anatomie und chirurgische Grundtechniken der Brust- und Gesäßregion; Grundlagen der Mikrochirurgie.",
    "Madrid, Oktober 2011 — Anatomie und chirurgische Grundlagen der Hals-Gesichts-Region; angewandte Anatomie und Grundtechniken der Rhino- und Profilplastik.",
    "Nizza, Dezember 2011 — Grundlagen der Chirurgie von Brust und Gesäßregion; Grundlagen der Mikrochirurgie.",
    "Nizza, April 2012 — Nahttechnik; konservative Chirurgie der Hals-Gesichts-Region.",
    "Nizza, Juli 2012 — Chirurgische Techniken am Fuß; angewandte Anatomie des Bauches; Nahttechnik.",
    "Madrid, Oktober 2012 — Mikrochirurgie; Rhino- und Profilplastik; ästhetische plastische Chirurgie und angewandte Anatomie von Gesicht und Hals; onkologische Anatomie und Chirurgie von Gesicht und Hals.",
    "Nizza, Februar 2013–2018 — Jährliche Kurse zu Facelift und Lidstraffung sowie zur Chirurgie von Brust und Gesäßregion.",
]

JOURNAL_TITLES = {
    "lifting-ringiovanimento-volto-invecchiamento-cutaneo-viso-ringiovanire-viso": "Das Facelift: das Gesicht harmonisch verjüngen",
    "correzione-mento-mentoplastica": "Die Korrektur des Kinns: Mentoplastik",
    "la-chirurgia-per-ridurre-il-volume-del-seno-la-mastoplastica-riduttiva": "Chirurgie zur Verkleinerung der Brust: die Reduktionsmammaplastik",
    "il-tessuto-adiposo-anatomia-e-patologia-come-trattarlo-le-diverse-metodiche-di-liposuzione": "Das Fettgewebe — Anatomie, Pathologie und die Methoden der Fettabsaugung",
    "la-chirurgia-delle-palpebre-limportanza-dello-sguardo-tecniche-per-il-miglioramento-della-regione-orbitaria-e-periorbitaria": "Lidchirurgie: die Bedeutung des Blicks",
    "addominoplastica-il-cambiamento-della-parete-addominale-con-il-passare-del-tempo": "Bauchdeckenstraffung: wie sich die Bauchwand mit der Zeit verändert",
    "cosa-e-la-chirurgia-estetica": "Was plastische — und vor allem ästhetische — Chirurgie wirklich ist",
    "lotoplastica-come-correggere-i-difetti-del-padiglione-auricolare-una-breve-descrizione": "Otoplastik: die Form des Ohrs korrigieren",
    "mastoplastica-additiva-di-cosa-si-tratta-parliamone-storia-protesi": "Eine Geschichte der Brustimplantat-Chirurgie",
    "medicina-estetica-filler-botulino-acido-jaluronico-biostimolanti-invecchiamento-cutaneo-biorivitalizzazione": "Die Haut, das Altern und die Möglichkeiten der ästhetischen Medizin",
    "storia-della-chirurgia-plastica-una-branca-meravigliosa-della-medicina-savona-genova-alessandria-lugano": "Eine Geschichte der plastischen Chirurgie — ein wunderbares Fach der Medizin",
}

UI = {
    "skip": "Zum Inhalt springen", "home": "Startseite", "home_aria": "Dr. Giuseppe Colombo — Startseite", "language": "Sprache",
    "book": "Beratung vereinbaren", "menu": "Menü", "close": "Schließen", "contact": "Kontakt",
    "first_step": "— Der erste Schritt", "begin_html": "Beginnen Sie mit einem <em>Gespräch</em>",
    "discover": "Entdecken", "dr": "Dr. Colombo",
    "bk_label": "— Beratungsanfrage", "bk_q1": "Worüber möchten Sie sprechen?",
    "bk_opts": ["Gesicht — Chirurgie", "Gesicht — ästhetische Medizin", "Brust", "Rekonstruktive Chirurgie", "Etwas anderes"],
    "bk_q2": "Wo möchten Sie uns treffen?", "bk_q3": "Wie erreichen wir Sie?",
    "bk_name": "Name", "bk_email": "E-Mail", "bk_phone": "Telefon", "bk_lang": "Bevorzugte Sprache",
    "bk_q4": "Möchten Sie uns noch etwas mitteilen?", "bk_msg": "Nachricht (optional)",
    "bk_consent": "Ich bin einverstanden, dass meine Angaben nur zur Beantwortung dieser Anfrage verwendet werden.",
    "bk_thanks": "Vielen Dank.",
    "bk_done": "Ihr E-Mail-Programm hat sich mit Ihrer Anfrage an {email} geöffnet — bitte senden Sie sie ab. Das Sekretariat antwortet {hours}.",
    "bk_conf": "Ihre Angaben werden vertraulich behandelt.", "bk_back": "← Zurück", "bk_continue": "Weiter", "bk_or_call": "Oder rufen Sie an",
    "key_facts": "Auf einen Blick", "facts_note": "Aus Dr. Colombos eigenen Texten. Jeder Fall wird in der Beratung individuell beurteilt.",
    "the_procedure": "— Der Eingriff", "from_journal": "aus dem Journal", "video_it": "— Video · auf Italienisch",
    "videos_it": "— Videos · auf Italienisch", "from_journal_label": "— Aus dem Journal", "in_italian": "auf Italienisch",
    "read_article": "Artikel lesen", "also_in": "— Ebenfalls im Bereich", "min": "Min.", "min_read": "Min. Lesezeit",
    "discuss_html": "Sprechen Sie mit <em>Dr. Colombo</em> darüber.", "discuss_sub": "Jeder Weg beginnt mit einer Beratung — in Lugano, Zürich oder Italien.",
    "begin_full_html": "Beginnen Sie mit einem <em>Gespräch</em>.",
    "area_cta_sub": "Jede Behandlung beginnt mit Zuhören — darauf, was Sie wünschen, und darauf, was Ihre Anatomie erlaubt.",
    "recon_label": "— Rekonstruktive Chirurgie", "recon_band": "Das Gesicht nach Hautkrebschirurgie wiederherstellen.",
    "purpose": "— Ziel", "techniques": "— Techniken", "play": "Video abspielen",
    "in_his_words": "— In seinen Worten", "thanks_trust": "Danke für Ihr Vertrauen.", "path": "— Werdegang",
    "path_h_html": "Ausgebildet von <em>Meistern</em>.<br>Geprägt von der Anatomie.", "the_person": "— Der Mensch",
    "person_h_html": "Medizin kommt am schnellsten voran, wenn Ärzte <em>teilen</em>.",
    "person_p": "Junge Ärzte und Kollegen sind in seinen Operationssälen willkommen — derselbe Geist wie hinter den Kursen, den Fellowships und dem Atlas.",
    "the_academy": "Die Akademie", "discretion": "— Diskretion", "cv": "— Lebenslauf", "cv_h": "Der vollständige Lebenslauf.",
    "portrait_alt": "Porträt von Dr. Giuseppe Colombo", "smile_alt": "Dr. Giuseppe Colombo lächelnd",
    "academy_quote": "„Medizin und Chirurgie machen rasante Fortschritte und erzielen immer bessere Ergebnisse, wenn alle Ärzte ihre Erfahrung teilen — das ist mein Geist.“",
    "on_page": "Auf dieser Seite", "j_atlas": "Der Atlas", "j_fellow": "Fellowship", "j_courses": "Kurse", "j_pubs": "Publikationen", "j_journal": "Journal", "j_videos": "Videos",
    "atlas_label": "— Der Atlas", "view_springer": "Bei Springer ansehen ↗", "earlier_work": "— Früheres Werk",
    "fellow_label": "— Fellowship", "fellow_h_html": "Halb Gesicht.<br><em>Halb Brust.</em>", "information": "Information:",
    "courses_label": "— Kurse & Präparationslabore", "courses_h_html": "Anatomie, <em>Schritt für Schritt.</em>",
    "courses_lead": "Neue Termine werden hier veröffentlicht. Informationen zu kommenden Kursen erhalten Sie unter",
    "brochure": "Broschüre (PDF)", "poster": "Kursplakat", "earlier_courses": "Frühere geleitete Kurse, 2010–2018",
    "pubs_label": "— Publikationen", "pubs_h_html": "Veröffentlichte <em>Arbeiten.</em>", "filter_topic": "Nach Thema filtern", "all": "Alle",
    "journal_label": "— Journal", "journal_h_html": "Aus dem <em>Journal.</em>", "all_articles": "Alle Artikel",
    "topics": {"Face": "Gesicht", "Breast": "Brust", "Aesthetic medicine": "Ästhetische Medizin", "Oncology": "Onkologie", "General": "Allgemein", "Research": "Forschung", "Body": "Körper"},
    "cats": {"Face": "Gesicht", "Breast": "Brust", "Body": "Körper", "Aesthetic medicine": "Ästhetische Medizin", "Philosophy": "Philosophie"},
    "journal": "Journal", "journal_lead": "Dr. Colombos Artikel über Gesicht, Brust, ästhetische Medizin und die Geschichte der plastischen Chirurgie. Die Artikel erscheinen auf Italienisch.",
    "latest": "Neueste", "filter_cat": "Nach Kategorie filtern", "article_note": "Dieser Artikel erscheint auf Italienisch, so wie Dr. Colombo ihn geschrieben hat.",
    "related_proc": "Passender Eingriff:", "continue_reading": "— Weiterlesen", "academy": "Akademie",
    "contact_h_html": "Beginnen Sie mit einem <em>Gespräch.</em>",
    "contact_lead": "Beratungen in Lugano, Zürich und Italien, nach Vereinbarung. Das Sekretariat antwortet {hours}.",
    "request_consult": "Beratung anfragen", "request_appt": "Termin anfragen",
    "telephone": "— Telefon", "email": "— E-Mail", "info_appts": "Information und Termine", "fellow_courses": "Fellowships und Kurse",
    "map_text": "Die Karte wird von Google bereitgestellt und nur auf Ihren Wunsch geladen.", "show_map": "Karte anzeigen",
    "nf_h_html": "Diese Seite hat ihr <em>Maß</em> verloren.", "nf_p": "Die gesuchte Seite existiert nicht — oder ist mit der neuen Website umgezogen.", "nf_btn": "Zur Startseite",
    "suffix": "Dr. Giuseppe Colombo · Plastische Chirurgie",
    "home_title": "Dr. Giuseppe Colombo — Plastische Chirurgie von Gesicht und Brust, Lugano",
    "home_meta": "Dr. Giuseppe Colombo, Facharzt für Plastische, Rekonstruktive und Ästhetische Chirurgie. Gesichts- und Brustchirurgie in Lugano, Beratungen in Zürich und Italien. Natürlichkeit vor allem.",
    "phil_title": "Philosophie", "phil_meta": "Dr. Giuseppe Colombo: Ausbildung, Werdegang und Philosophie. Plastischer Chirurg mit Schwerpunkt Gesicht und Brust — Natürlichkeit vor allem.",
    "acad_meta": "Die Akademie von Dr. Giuseppe Colombo: der Springer-Atlas Stepwise Atlas of Aesthetic Medicine and Surgery, Fellowships, Präparationskurse und Publikationen.",
    "journal_meta": "Artikel von Dr. Giuseppe Colombo über Gesichtschirurgie, Brustchirurgie, ästhetische Medizin und die Geschichte der plastischen Chirurgie.",
    "contact_title": "Kontakt", "contact_meta": "Vereinbaren Sie eine Beratung mit Dr. Giuseppe Colombo: Clinica Sant'Anna, Lugano; Beratungen in Zürich und Italien nach Vereinbarung.",
    "nf_title": "Seite nicht gefunden",
    "js": {
        "menu": "Menü", "close": "Schließen", "send": "Anfrage senden", "continue": "Weiter",
        "e1": "Bitte wählen Sie eine Option.", "e2": "Bitte wählen Sie einen Ort.", "e3": "Bitte geben Sie Ihren Namen ein.",
        "e4": "Bitte geben Sie eine gültige E-Mail-Adresse ein.", "e5": "Bitte bestätigen Sie die Datenschutz-Einwilligung.",
        "subject": "Beratungsanfrage", "interest": "Anliegen", "location": "Ort", "name": "Name",
        "email": "E-Mail", "phone": "Telefon", "language": "Bevorzugte Sprache", "map": "Karte: Clinica Sant'Anna, Lugano",
    },
}

HOME = {
    "kicker": "— Dr. Giuseppe Colombo · Lugano",
    "hero_line_html": "Das rechte <em>Maß</em> ist das Schönste.",
    "hero_sub": "Plastische Chirurgie von Gesicht und Brust",
    "philosophy": "— Philosophie", "doc_tr": "Hasse das Übermaß. Respektiere die Grenze.", "meet": "Dr. Colombo kennenlernen",
    "beneath": "— Unter der Oberfläche", "layers_h": "Die Schichten des Gesichts",
    "steps": [
        ("01 · Haut", "Was man sieht.", "Die Oberfläche — eine Schutzschicht gegen Wind, Sonne und alles, was uns täglich begegnet."),
        ("02 · Fett", "Was darunter liegt.", "Eine Schicht von nur wenigen Millimetern, die sich mit den Jahren verschiebt und absinkt."),
        ("03 · SMAS", "Was es hält.", "Die tiefe Schicht, an der der Chirurg arbeitet. Sie genau zu kennen, ist grundlegend."),
        ("04 · Tiefe", "Was geschützt werden muss.", "Die Nerven, die das Gesicht bewegen, die wichtigsten Gefäße und die Muskeln des Mundes liegen alle darunter."),
    ],
    "anat_close_html": "Natürliche, dauerhafte Ergebnisse entstehen durch Arbeit an den tiefen Strukturen — <em>nicht durch Zug an der Haut.</em>",
    "areas_label": "— Zwei Bereiche, ein Fokus", "areas_h_html": "Gesicht. <em>Brust.</em>",
    "areas_lead": "Ich habe meine Praxis auf Gesicht, Hals und Brust konzentriert — um jedem Patienten das bestmögliche Ergebnis zu bieten.",
    "face_list": "Facelift · Lidstraffung · Brauenlifting · Lip-Lift · Ohrenkorrektur · Kinn · Ästhetische Medizin",
    "breast_list": "Straffung · Vergrößerung · Verkleinerung · Gynäkomastie",
    "recon_link": "Rekonstruktive Chirurgie — das Gesicht nach Hautkrebschirurgie wiederherstellen",
    "teacher": "— Lehrer & Autor", "teacher_h_html": "Ein Chirurg, der Chirurgen <em>lehrt</em>.",
    "atlas_lead_html": "Herausgeber von <em>{title}</em> ({publisher}): mehr als <strong data-count=\"320\">320</strong> Originalfotografien, die den Leser Schritt für Schritt von der präoperativen Planung bis zur Nachsorge führen.",
    "facts": [("Ph.D.", "Universität Genua"), ("Dozent", "Master in Ästhetischer Chirurgie, Universität Pavia"), ("Kurse", "Nizza · Madrid · Cremona"), ("Fellowships", "Gesicht & Brust")],
    "discover_academy": "Die Akademie entdecken", "atlas_alt": "Cover des Stepwise Atlas of Aesthetic Medicine and Surgery, herausgegeben von Giuseppe Colombo (Springer)",
    "discretion": "— Diskretion", "discretion_aria": "Diskretion",
    "place": "— Der Ort", "lugano_h_html": "Lugano, <em>Schweiz.</em>",
    "lugano_p": "Clinica Sant'Anna — Praxis und Operationssaal unter einem Dach.",
    "convo_h_pre": "Beginnen Sie mit einem", "convo_word": "Gespräch",
    "convo_lead": "Sagen Sie uns, worüber Sie sprechen möchten. Das Sekretariat antwortet {hours}.",
}

LUCE = {
    "kicker": "Dr. Giuseppe Colombo · Plastische Chirurgie · Lugano",
    "nat_label": "— Natürlichkeit",
    "nat_word": "Natürlichkeit",
    "nat_lead": "Ein einziges Wort leitet seine Arbeit.",
    "nat_never": ["Niemals dem Übermaß nachgeben.", "Niemals Menschen verfremden.", "Nur das Beste in ihnen zur Geltung bringen."],
    "meet": "Dr. Colombo kennenlernen",
    "concern_label": "— Wo beginnen",
    "concern_h_html": "Was möchten Sie <em>verfeinern</em>?",
    "concern_lead": "Wählen Sie einen Bereich. Jede Behandlung wird mit Dr. Colombos eigenen Worten erklärt.",
    "concerns": {
        "face": ("Gesicht & Hals", "Unteres Gesicht, Hals und Profil"),
        "eyes": ("Die Augen", "Lider, Brauen und Mimikfalten"),
        "lips": ("Die Lippen", "Form und Definition der Oberlippe"),
        "skin": ("Die Haut", "Feuchtigkeit, Spannkraft und Ausstrahlung"),
        "ears": ("Die Ohren", "Form und Stellung der Ohrmuschel"),
        "breast": ("Die Brust", "Straffung, Volumen, Verkleinerung — und die männliche Brust"),
        "restore": ("Rekonstruktion", "Das Gesicht nach Hautkrebschirurgie"),
    },
    "see_all": "Alle Behandlungen",
    "journey_label": "— Der Weg",
    "journey_h_html": "Vom ersten Gespräch<br>zu einem <em>natürlichen</em> Ergebnis.",
    "journey": [
        ("Beratung", "Ein erstes Gespräch in Lugano, Zürich oder Italien — Ihre Wünsche, Ihre Anatomie, Ihre Fragen."),
        ("Ein Plan für Sie", "Jeder Fall wird individuell beurteilt. Der Eingriff wird für Sie gewählt — nie für einen Trend."),
        ("Der Eingriff in Lugano", "Clinica Sant'Anna — Praxis und Operationssaal unter einem Dach."),
        ("Die Erholung", "Sie hängt vom Eingriff ab: Nach einer Lidstraffung zum Beispiel ist das Aussehen nach 7–10 Tagen wieder normal."),
        ("Ein natürliches Ergebnis", "Das Gewebe setzt sich über Monate — bei den Lidern wird das Endergebnis nach etwa einem Jahr beurteilt."),
    ],
    "trust_label": "— Erfahrung",
    "trust_h_html": "Ausgebildet von Meistern.<br>Er <em>lehrt</em> Kollegen.",
    "trust": [
        ("2005", "Medizinstudium, Genua", "110/110 cum laude — danach Facharzt, 50/50 cum laude, und ein Ph.D."),
        ("320+", "Originalfotografien", "in dem von ihm herausgegebenen Springer-Atlas der ästhetischen Medizin und Chirurgie."),
        ("19", "Publikationen", "in internationalen Fachzeitschriften, von 2008 bis 2021."),
        ("2010", "Präparationskurse", "seit 2010 für Chirurgen in Nizza, Madrid und Cremona geleitet."),
    ],
    "trust_more": "Die Akademie entdecken",
    "place_label": "— Der Ort",
    "proc_journey": "— Ihr Weg",
    "facts_title": "Auf einen Blick",
    "morning": "Morgen", "evening": "Abend",
    "concern_word": "Bereich",
}

LUCE["anat_label"] = "— Anatomie"
LUCE["anat_note"] = "Illustrative Zeichnung — kein medizinisches Schema. Jede Anatomie wird in der Beratung individuell beurteilt."
LUCE["anat"] = {
    "facelift": "Die Schichten des Gesichts: Haut, Unterhautfett und SMAS — darunter liegen die Nerven, die das Gesicht bewegen, die wichtigsten Gefäße und die Muskeln des Mundes.",
    "blepharoplasty": "Die Lider: dünne Haut, der Ringmuskel, der das Auge schließt, und die Fettpolster darunter — zwei im Oberlid, drei im Unterlid.",
    "brow-lift": "Das obere Gesichtsdrittel: die Braue und die Muskeln um die Augen, wo das äußere Brauendrittel abzusinken neigt.",
    "botulinum-toxin": "Die Mimikmuskeln: Stirn, Brauen und die Augenpartie — sowie Masseter und Platysma, die ebenfalls mit Botulinumtoxin behandelt werden.",
    "otoplasty": "Die Ohrmuschel und ihre Knorpelfalten — die Anthelix ist die Hauptfalte des Ohrs.",
    "lip-lift": "Das Profil der Lippe: die Columella am Nasenansatz, der Amorbogen und das Lippenrot.",
    "chin": "Die Harmonie des Profils: Die Nasenspitze sollte etwas weiter nach vorne ragen als das Kinn.",
    "hyaluronic-acid": "Die Schichten der Haut: Hyaluronsäure ist Teil des Bindegewebes der Lederhaut, zwischen Kollagen- und elastischen Fasern.",
    "biorevitalisation": "Die Schichten der Haut, in denen die Biorevitalisierung die Bildung von Kollagen und Elastin fördert.",
    "mastopexy": "Die Brust im Profil: Haut, Drüsengewebe und Fett, auf der Brustwand ruhend.",
    "augmentation": "Die Brust im Profil: Haut, Drüsengewebe und Fett, auf der Brustwand ruhend.",
    "reduction": "Die Brust im Profil: Haut, Drüsengewebe und Fett, auf der Brustwand ruhend.",
    "gynecomastia": "Die männliche Brust: Ansammlung von Fett (falsche Gynäkomastie), von Drüsengewebe (echte) — oder beides (gemischte).",
}
