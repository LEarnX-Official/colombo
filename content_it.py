"""Italian content — the site's primary language.
Texts are the doctor's originals from drgiuseppecolombo.com (typos corrected);
interface strings are new. Anything not defined here falls back to content.py."""
import content as EN

LANG = "it"
MONTHS = "gennaio febbraio marzo aprile maggio giugno luglio agosto settembre ottobre novembre dicembre".split()

PATHS = {
    "home": "/", "philosophy": "/filosofia/", "face": "/viso/", "breast": "/seno/",
    "reconstructive": "/chirurgia-ricostruttiva/", "academy": "/academy/", "journal": "/academy/journal/",
    "contact": "/contatti/",
}
PROC_SLUGS = {
    "facelift": "lifting-cervico-facciale", "blepharoplasty": "blefaroplastica", "brow-lift": "lifting-del-sopracciglio",
    "lip-lift": "lip-lifting", "otoplasty": "otoplastica", "chin": "mentoplastica",
    "hyaluronic-acid": "acido-ialuronico", "botulinum-toxin": "tossina-botulinica", "biorevitalisation": "biorivitalizzazione",
    "mastopexy": "mastopessi", "augmentation": "mastoplastica-additiva", "reduction": "mastoplastica-riduttiva",
    "gynecomastia": "ginecomastia",
}
NAV_LABELS = {"philosophy": "Filosofia", "face": "Viso", "breast": "Seno", "academy": "Academy", "contact": "Contatti"}

SITE = dict(EN.SITE)
SITE.update({
    "role": "Specialista in Chirurgia Plastica, Ricostruttiva ed Estetica · Ph.D. Università di Genova",
    "hours": "dal lunedì al venerdì, dalle 10 alle 18",
    "locations": [
        {"key": "lugano", "city": "Lugano", "country": "Svizzera", "role": "Studio e sala operatoria",
         "lines": ["Clinica Sant'Anna", "Via Sant'Anna 1"], "extra": "Studio: Via Nassa 7 · Via Clemente Maraini 8"},
        {"key": "zurich", "city": "Zurigo", "country": "Svizzera", "role": "Consulenze chirurgiche", "lines": ["Su appuntamento"], "extra": ""},
        {"key": "italy", "city": "Italia", "country": "", "role": "Consulenze", "lines": ["Su appuntamento"], "extra": ""},
    ],
    "phones": [
        {"label": "Svizzera", "display": "+41 76 297 69 87", "tel": "+41762976987"},
        {"label": "Italia", "display": "+39 342 327 5364", "tel": "+393423275364"},
    ],
})

QUOTES = dict(EN.QUOTES)
QUOTES.update({"measure_en": "", "limit_en": "", "discretion_en": ""})
QUOTES["naturalness"] = "Per quanto riguarda la mia filosofia, solo una parola guida la mia pratica: naturalezza. Mai cedere agli eccessi, mai stravolgere le persone, ma solo cercare di valorizzarle al meglio."

VIDEOS = {
    "HnflefgVqMM": "Lifting", "852M8oEXm4A": "Quanto costa un lifting?", "_yyDI8cqhWU": "Ringiovanimento dello sguardo",
    "86dQ-Oy1_eg": "Mastoplastica additiva", "o-ksV1W2LeI": "Liposuzione", "-9COFP65Fl8": "Scegliere il chirurgo: i campanelli d'allarme da non ignorare",
    "rIZn6oLeCpI": "Intervista al Dr. Giuseppe Colombo", "DIH4McTTDNs": "Decus — report del congresso", "U47HAtXf1ao": "Decus — due location",
}

AREAS = {
    "face": {
        "title": "Viso",
        "lede": "Lifting, palpebre, sopracciglio, labbra, orecchie e mento — e la medicina estetica per la pelle. Ogni trattamento parte dallo stesso principio: rispettare il volto che è già tuo.",
        "intro": "Ho focalizzato la mia attenzione sugli interventi di lifting facciale e blefaroplastica per quanto concerne il volto.",
        "meta": "Chirurgia plastica del viso e medicina estetica del Dr. Giuseppe Colombo a Lugano: lifting cervico-facciale, blefaroplastica, lifting del sopracciglio, lip-lifting, otoplastica, mentoplastica, acido ialuronico, tossina botulinica, biorivitalizzazione.",
        "group_titles": ["Chirurgia del viso", "Medicina estetica"],
    },
    "breast": {
        "title": "Seno",
        "lede": "Mastopessi, mastoplastica additiva, riduttiva e ginecomastia. Ogni intervento è scelto per il corpo che abbiamo davanti — mai per una moda.",
        "intro": "Per quanto concerne la mammella, mi dedico agli interventi di mastoplastica riduttiva, pessi e correttiva di aumento.",
        "meta": "Chirurgia del seno del Dr. Giuseppe Colombo a Lugano: mastopessi, mastoplastica additiva, mastoplastica riduttiva e ginecomastia.",
        "group_titles": ["Chirurgia del seno"],
    },
}

PROCEDURES = {
    "facelift": {
        "group": "Chirurgia del viso", "title": "Lifting cervico-facciale", "subtitle": "Lifting del viso e del collo",
        "lede": "La procedura principe nella chirurgia dell'invecchiamento facciale: riposiziona, stabilmente nel tempo, le strutture che gli anni hanno spostato.",
        "body": [
            "L'invecchiamento del viso compare con una progressione ed una velocità che può variare a seconda dell'individuo, della sua predisposizione familiare e dello stile di vita che conduce. Si manifesta a carico di tutti gli elementi del viso: pelle, grasso sottocutaneo e muscolatura profonda. Ne risulta un appesantimento che, spesso, è particolarmente evidente a livello del terzo inferiore del volto e del collo.",
            "In questi casi soltanto il Lifting Cervico-Facciale, che rappresenta la procedura principe nella Chirurgia dell'Invecchiamento Facciale, permette di correggere tali inestetismi riposizionando, stabilmente nel tempo, le strutture coinvolte in questo processo. Infatti la cute e i tessuti più profondi, in particolare la muscolatura, vengono opportunamente trazionati e stabilizzati cercando di ripristinare le giuste proporzioni e la corretta armonia del volto.",
            "La conoscenza anatomica dello SMAS è fondamentale per il chirurgo: i nervi deputati alla mobilità del viso, le ghiandole salivari, le vene, le arterie più importanti ed i muscoli necessari per muovere simmetricamente la bocca si trovano al di sotto di questa lamina di tessuto.",
            "Non possiamo far tornare la pelle dei venticinque o trent'anni, né far sparire tutte le rughe. Per questo è molto importante che il paziente abbia capito tutto il processo: la sua collaborazione sarà fondamentale per ottenere il miglior risultato.",
        ],
        "facts": [("Strati trattati", "Pelle, grasso sottocutaneo e muscolatura profonda (SMAS)"), ("Area principale", "Terzo inferiore del volto e collo"), ("Principio", "Trazione sulle strutture profonde, non sulla pelle")],
        "quote": "Applicando la forza sulle strutture profonde e non sulla pelle, si evitano problemi spiacevoli, come le tensioni sulle cicatrici. Inoltre i punti fermi e profondi daranno al risultato una durata molto più permanente.",
        "meta": "Lifting cervico-facciale del Dr. Giuseppe Colombo, Lugano: riposizionare le strutture profonde del viso e del collo (SMAS) per un risultato naturale e duraturo.",
    },
    "blepharoplasty": {
        "group": "Chirurgia del viso", "title": "Blefaroplastica", "subtitle": "Chirurgia delle palpebre",
        "lede": "Gli occhi sono i primi a subire gli effetti del passare del tempo. La blefaroplastica restituisce uno sguardo riposato, nel maggior rispetto della funzione visiva e di quella espressiva.",
        "body": [
            "Solitamente le persone che chiedono informazioni per una blefaroplastica sono donne tra i quaranta e i quarantacinque anni, o uomini un po' più maturi, con il resto del viso ben strutturato, ma che si lamentano dell'eccesso di pelle e a volte di grasso intorno agli occhi. Sono persone molto attive, infastidite dall'alzarsi già al mattino con un aspetto stanco che non corrisponde per niente al loro buon umore.",
            "Nella blefaroplastica superiore, una volta eliminato il fuso di pelle in eccesso, si elimina una sottile striscia di muscolo orbicolare, marcando maggiormente il solco palpebrale. Le borse di grasso vanno resecate nella quantità giusta e nel luogo adeguato: è l'unico modo di conseguire un risultato naturale ed evitare la sensazione di “occhi infossati”. La cicatrice si nasconde nella piega naturale della palpebra.",
            "Oggigiorno il trattamento delle borse delle palpebre inferiori quasi sempre si realizza per via transcongiuntivale, cioè all'interno della palpebra: si evitano cicatrici esterne e, cosa più importante, si evita di tagliare il muscolo orbicolare che mantiene la forma del bordo della palpebra. Quando il bordo laterale dell'occhio è sceso, una cantopessi permette di riportarlo in alto e definire nuovamente lo sguardo.",
            "In più della metà dei casi di pazienti candidati ad una blefaroplastica superiore, il problema non è solo rappresentato dall'esubero cutaneo palpebrale ma anche dalla ptosi del sopracciglio, soprattutto a livello della sua porzione laterale. In questi casi il trattamento ideale associa alla blefaroplastica l'intervento di brow lift.",
        ],
        "facts": [("Anestesia", "Locale, con lieve sedazione se necessario"), ("Dimissione", "Normalmente entro 24 ore"), ("Rimozione dei punti", "Dopo 4–7 giorni"), ("Aspetto normale", "Dopo 7–10 giorni"), ("Trucco e sole", "Dopo la prima settimana, con protezione solare totale"), ("Risultato definitivo", "Dopo circa un anno"), ("Durata", "Ritocchi raramente necessari prima di 10–15 anni")],
        "quote": "È preferibile che resti qualche piccola ruga per preservare al massimo la forma originaria dell'occhio.",
        "meta": "Blefaroplastica superiore e inferiore del Dr. Giuseppe Colombo, Lugano: ringiovanimento naturale dello sguardo, cicatrici nascoste, recupero in 7–10 giorni.",
    },
    "brow-lift": {
        "group": "Chirurgia del viso", "title": "Lifting del sopracciglio", "subtitle": "Brow lift",
        "lede": "La discesa del sopracciglio è un fenomeno spesso sottovalutato — dal paziente e, purtroppo, da alcuni chirurghi.",
        "body": [
            "La ptosi (discesa) del sopracciglio è un fenomeno spesso sottovalutato nel trattamento dell'invecchiamento facciale sia dal paziente che, purtroppo, da alcuni chirurghi. Infatti, in più della metà dei casi di pazienti candidati ad una blefaroplastica superiore, il problema non è solo rappresentato dall'esubero cutaneo palpebrale ma anche dalla ptosi del sopracciglio, soprattutto a livello della sua porzione laterale. Il trattamento ideale deve necessariamente associare alla blefaroplastica l'intervento di brow lift.",
            "Le metodiche più utilizzate ed efficaci prevedono o un approccio cosiddetto “diretto”, con un'incisione facilmente mimetizzabile nella porzione più alta del sopracciglio stesso o, come più frequentemente si preferisce, un approccio trans-temporale per mezzo di una piccola incisione nel capillizio, che rimane completamente invisibile ed attraverso la quale viene sollevato il terzo laterale del sopracciglio.",
        ],
        "facts": [("Approccio", "Trans-temporale (incisione nascosta nel capillizio) o diretto"), ("Area sollevata", "Il terzo laterale del sopracciglio"), ("Spesso associato a", "Blefaroplastica superiore")],
        "meta": "Lifting del sopracciglio del Dr. Giuseppe Colombo, Lugano: sollevare il terzo laterale del sopracciglio con un'incisione invisibile nel capillizio.",
    },
    "lip-lift": {
        "group": "Chirurgia del viso", "title": "Lip-lifting", "subtitle": "Lifting del labbro superiore",
        "lede": "Un rimodellamento definitivo del labbro superiore — definito, naturale ed armonico, senza bisogno di ulteriori filler.",
        "body": [
            "Il “lip-lifting” o lifting del labbro superiore è una tecnica sempre più richiesta dai pazienti che garantisce un rimodellamento definitivo del labbro superiore. Molto spesso il labbro superiore, anche come conseguenza diretta dei processi di invecchiamento, perde definizione a livello dell'arco di Cupido, si appiattisce ed aumenta la sua dimensione verticale (la distanza tra la columella ed il vermiglio).",
            "Esistono varie tecniche chirurgiche che prevedono diverse incisioni; quella più utilizzata e che garantisce una cicatrice ben nascosta a livello della piega alare-facciale e della columella è quella del “bullhorn”. Grazie a questa tecnica si ottiene un labbro superiore ben definito, naturale ed armonico che non necessita di ulteriori trattamenti iniettivi di filler.",
        ],
        "facts": [("Tecnica", "Lip-lifting “bullhorn”"), ("Cicatrice", "Nascosta alla base del naso (piega alare-facciale e columella)"), ("Risultato", "Rimodellamento definitivo, senza ulteriori filler")],
        "meta": "Lip-lifting del Dr. Giuseppe Colombo, Lugano: la tecnica bullhorn per un labbro superiore definito e naturale, con cicatrice nascosta.",
    },
    "otoplasty": {
        "group": "Chirurgia del viso", "title": "Otoplastica", "subtitle": "Chirurgia delle orecchie",
        "lede": "Correggere la forma del padiglione auricolare rimodellandone la cartilagine — con una cicatrice completamente nascosta dietro l'orecchio.",
        "body": [
            "L'otoplastica è un intervento chirurgico finalizzato alla correzione degli inestetismi del padiglione auricolare. La malformazione di più frequente riscontro è rappresentata dalle cosiddette “orecchie a ventola”, caratterizzate da un padiglione auricolare particolarmente distaccato dalla testa dovuto ad un angolo oto-mastoideo aperto e all'assenza dell'antelice (la piega maggiore del padiglione auricolare).",
            "Tale procedura chirurgica consente di modificare la forma, le dimensioni e l'attaccatura del padiglione auricolare mediante un rimodellamento dell'impalcatura cartilaginea, che viene eseguito indebolendo la cartilagine e, se necessario, utilizzando anche suture di stabilizzazione che consentono di ripristinare le fisiologiche pieghe e curvature tipiche della normale anatomia auricolare. La cicatrice residua risulta completamente nascosta a livello del solco retro-auricolare.",
            "Fra i cinque e i sei anni l'orecchio ha una dimensione, forma e sviluppo su cui si può intervenire chirurgicamente; molti pazienti vengono visitati per la prima volta in età adulta, fra i venti e i trent'anni.",
        ],
        "facts": [("Anestesia", "Locale negli adulti, generale nei bambini"), ("Dall'età di", "5–6 anni"), ("Cicatrice", "Nascosta nel solco retro-auricolare"), ("Controllo", "Il giorno dopo l'intervento"), ("Dopo", "Una fascia per capelli per almeno una settimana; si può lavare la testa dopo la prima settimana")],
        "meta": "Otoplastica del Dr. Giuseppe Colombo, Lugano: correzione delle orecchie a ventola con cicatrice nascosta dietro l'orecchio.",
    },
    "chin": {
        "group": "Chirurgia del viso", "title": "Mentoplastica", "subtitle": "Chirurgia del mento",
        "lede": "L'armonia del profilo dipende dal mento quanto dal naso.",
        "body": [
            "Esiste un gruppo di pazienti in cui la rinoplastica può non essere sufficiente per ottenere una linea del profilo armonica poiché il mento risulta troppo arretrato. Questo potrebbe presupporre una riduzione nasale molto marcata per uguagliare la linea del mento, ma è una concezione sbagliata.",
            "L'ideale in questi casi è studiare molto bene il profilo del paziente: la proiezione della punta del naso deve essere lievemente più avanti di quella del mento e, se questo è molto indietro, nel piano operatorio bisognerà prevedere la collocazione o di una protesi nel mento o di tessuto adiposo (lipofilling).",
            "All'interno della bocca, dietro il labbro inferiore, si fanno due incisioni laterali di circa due o tre centimetri. Le protesi sono di silicone: un materiale solido ma allo stesso tempo flessibile e malleabile, che il chirurgo può modellare durante l'intervento per renderlo il più fedele possibile alla forma desiderata. Le incisioni si chiudono con punti di sutura riassorbibili.",
        ],
        "facts": [("Anestesia", "Locale con sedazione; generale se associata a rinoplastica"), ("Incisioni", "All'interno della bocca, dietro il labbro inferiore"), ("Opzioni", "Protesi in silicone o lipofilling"), ("Recupero", "Attività abituali dopo circa una settimana")],
        "meta": "Mentoplastica del Dr. Giuseppe Colombo, Lugano: armonizzare il profilo con protesi in silicone o lipofilling.",
    },
    "hyaluronic-acid": {
        "group": "Medicina estetica", "title": "Acido ialuronico", "subtitle": "Medicina estetica",
        "lede": "Un componente naturale della pelle, restituito dove il tempo lo ha ridotto — per compattezza, idratazione e luminosità.",
        "body": [
            "L'acido ialuronico rappresenta uno dei principali componenti del tessuto connettivo del derma, nel quale sono immerse le fibre collagene ed elastiche. Legandosi all'acqua presente nei tessuti ne aumenta l'elasticità, l'idratazione e la tonicità, oltre ad avere proprietà cicatrizzanti ed antinfiammatorie.",
            "La sua concentrazione all'interno del tessuto connettivo cutaneo tende a diminuire con l'avanzare dell'età: è tra i principali responsabili dell'invecchiamento cutaneo. L'iniezione di acido ialuronico consente di ritonificare le pelli mature stimolando la funzionalità cellulare e donando alla cute la compattezza e la luminosità perdute. Per questi motivi viene utilizzato con successo in campo dermatologico-estetico ormai da diversi anni.",
            "Viene riprodotto in laboratorio e, se si escludono isolati casi di ipersensibilità, è privo di effetti collaterali. Viene iniettato dal medico con un piccolissimo ago nello spessore dermico o nel tessuto sottocutaneo, in dipendenza dalla sede e dalla profondità da trattare. L'effetto riempitivo o spianante è variabile e dipende dal tipo di pelle e dalla qualità e quantità di acido ialuronico utilizzato.",
        ],
        "facts": [("Iniezione", "Ago sottilissimo, nel derma o nel tessuto sottocutaneo"), ("Durata", "Non permanente — si ripete circa ogni 6–12 mesi"), ("Controindicazioni", "Gravidanza, allattamento, collagenopatie o malattie cutanee autoimmuni")],
        "meta": "Trattamenti con acido ialuronico del Dr. Giuseppe Colombo, Lugano: idratazione, compattezza e luminosità per le pelli mature.",
    },
    "botulinum-toxin": {
        "group": "Medicina estetica", "title": "Tossina botulinica", "subtitle": "Medicina estetica",
        "lede": "Attenuare — non cancellare — le rughe d'espressione che danno al volto un aspetto stanco.",
        "body": [
            "Il botulino è un presidio altamente purificato (deriva da un batterio, il Clostridium botulinum) che in ambito medico-estetico permette di inibire temporaneamente e localmente l'eccessiva contrazione di alcuni muscoli mimici e conseguentemente la formazione di rughe a livello del terzo superiore del volto: fronte, regione sopraccigliare, glabellare e perioculare (zampe di gallina).",
            "Si tratta di rughe dinamiche che determinano un aspetto stanco e affaticato, soprattutto intorno agli occhi. Il vero obiettivo del trattamento è riconferire agli occhi e alle aree limitrofe un aspetto tonico e riposato: un'espressione sempre fresca, alla sera come al mattino. Il botulino non riempie come i filler a base di acido ialuronico.",
            "Viene utilizzato anche per ridurre le ipertrofie del muscolo massetere, che conferiscono al volto una forma troppo quadrata, riconferendo al viso una forma più ovalare; nel trattamento delle bande verticali del muscolo platisma del collo; e, a piccole dosi, per tonificare le regioni laterali del collo per chi desidera posticipare un lifting. Un'altra importante indicazione è l'iperidrosi, l'eccessiva sudorazione ascellare, delle mani o dei piedi.",
        ],
        "facts": [("Anestesia", "Non necessaria — praticamente indolore"), ("Inizio dell'effetto", "Dopo circa 3 giorni"), ("Durata", "Circa 5 mesi, poi si può ripetere"), ("Aree", "Fronte, sopracciglia, glabella, zampe di gallina · massetere · collo")],
        "quote": "È fondamentale sottolineare che questa, più di altre procedure, è altamente operatore dipendente. Un buon utilizzo del botulino, oltre al senso e alla misura estetica del medico in accordo con le aspettative del paziente, mirerà non a cancellare del tutto gli inestetismi del viso ma ad attenuare le troppe rughe che invecchiano il nostro volto.",
        "meta": "Tossina botulinica del Dr. Giuseppe Colombo, Lugano: attenuare le rughe d'espressione con misura — mai un effetto bloccato.",
    },
    "biorevitalisation": {
        "group": "Medicina estetica", "title": "Biorivitalizzazione", "subtitle": "Medicina estetica",
        "lede": "Migliorare la qualità della pelle stessa — senza alterare i volumi del viso.",
        "body": [
            "La bioristrutturazione del volto è un trattamento di medicina estetica avanzata finalizzato a migliorare la qualità dei tessuti, stimolando i naturali processi di rigenerazione cutanea senza alterare i volumi del viso. Non nasce per “riempire”, ma per riattivare la funzionalità biologica della pelle, contrastando lassità, disidratazione, perdita di elasticità e tono.",
            "Agisce sui diversi strati cutanei favorendo la produzione di collagene ed elastina e migliorando l'architettura dermica nel tempo. È indicata sia nei primi segni di invecchiamento sia come trattamento di mantenimento o preparazione a procedure più invasive.",
            "La procedura prevede micro-iniezioni mirate di sostanze biorigenerative, selezionate in base alle caratteristiche della pelle e agli obiettivi clinici. Il risultato è un volto più fresco, compatto e luminoso, con un ringiovanimento naturale e progressivo, rispettoso dell'anatomia e dell'espressività individuale.",
        ],
        "facts": [("Contesto", "Trattamento ambulatoriale, ben tollerato"), ("Recupero", "Nessun tempo di recupero significativo"), ("Indicata per", "Primi segni di invecchiamento, mantenimento o preparazione alla chirurgia")],
        "meta": "Biorivitalizzazione del Dr. Giuseppe Colombo, Lugano: micro-iniezioni che migliorano la qualità della pelle senza alterare i volumi.",
    },
    "mastopexy": {
        "group": "Chirurgia del seno", "title": "Mastopessi", "subtitle": "Lifting del seno",
        "lede": "Sollevare e rimodellare un seno sceso e svuotato.",
        "body": [
            "La mastopessi permette di correggere la discesa eccessiva del seno, consentendo di ritonificare un seno cadente e svuotato, migliorandone la forma ed il volume e correggendo gli inestetismi causati da gravidanza, allattamento, dimagrimenti eccessivi e fisiologico invecchiamento. Il rimodellamento punta al riacquisto massimo di un aspetto pieno e sodo.",
            "Esistono varie tecniche di mastopessi a seconda della gravità della ptosi mammaria. Nei casi meno gravi è sufficiente rimuovere un anello cutaneo intorno all'areola per riportare la mammella nella giusta posizione: la cicatrice risulterà facilmente mimetizzabile a livello della zona di passaggio tra l'areola e la cute. Nelle ptosi più severe è necessario rimuovere ulteriori porzioni di pelle e solitamente alla cicatrice periareolare si associa una cicatrice verticale che arriva fino al solco inframammario e una cicatrice orizzontale (cicatrice a “T” invertita) a livello del solco stesso.",
            "In taluni casi la rimozione della cute in eccesso ed il sollevamento del seno vengono combinati con l'inserimento di protesi mammarie di ultimissima generazione per un aumento volumetrico maggiore (mastopessi additiva).",
        ],
        "facts": [("Corregge", "Gli effetti di gravidanza, allattamento, dimagrimento e invecchiamento"), ("Cicatrici", "Periareolare nei casi lievi; a “T” invertita nei casi più severi"), ("Opzione", "Associata a protesi per più volume (mastopessi additiva)")],
        "meta": "Mastopessi del Dr. Giuseppe Colombo, Lugano: ripristinare posizione e forma del seno dopo gravidanza, dimagrimento o invecchiamento.",
    },
    "augmentation": {
        "group": "Chirurgia del seno", "title": "Mastoplastica additiva", "subtitle": "Aumento del seno",
        "lede": "Più volume — scelto per le giuste ragioni, e solo quando è la risposta giusta.",
        "body": [
            "In alcuni casi il solo aumento di volume mammario non rappresenta la scelta giusta per ottenere il risultato migliore. Quando alla mancanza di volume della mammella è associata una ptosi (discesa) del parenchima mammario, la sola protesi non è sufficiente a correggere tale rilassamento, ma anzi può causare essa stessa un ulteriore peggioramento della situazione. In questi casi la mastopessi associata all'inserimento di protesi rappresenta la combinazione ideale.",
            "Le protesi in gel di silicone di oggi, con uno speciale involucro esterno in elastomero siliconico selezionato per la sua resistenza, durata e flessibilità, sono quelle che contribuiscono alla migliore simulazione di un seno naturale.",
        ],
        "facts": [("Protesi", "Gel di silicone di ultima generazione"), ("Con ptosi", "Associata a mastopessi per il risultato migliore")],
        "quote": "La moda non dovrebbe MAI condizionare le decisioni di cambiare o meno il proprio corpo. Le motivazioni per sottoporsi ad un intervento estetico devono essere ben chiare, serie, ragionate, basate sullo stare bene con se stessi e con il mettere in armonia il proprio aspetto esteriore e quello interiore.",
        "meta": "Mastoplastica additiva del Dr. Giuseppe Colombo, Lugano: protesi in gel di silicone, associate a mastopessi quando serve, per un risultato naturale.",
    },
    "reduction": {
        "group": "Chirurgia del seno", "title": "Mastoplastica riduttiva", "subtitle": "Riduzione del seno",
        "lede": "Alleggerire il seno — per l'estetica e per il benessere del corpo.",
        "body": [
            "È l'intervento che prevede la riduzione del seno in caso di gigantomastia o ipertrofia della ghiandola mammaria. Viene praticato non solo per ragioni estetiche ma anche per motivi funzionali: chi ha un seno esageratamente grande e pesante lo sente gravare sulla parte anteriore del corpo e ha facilmente dolori alle spalle, al collo ed alla porzione alta della colonna vertebrale.",
            "Si può arrivare alla riduzione anche di quattro/cinque taglie. La mastoplastica riduttiva consente di tonificare la piramide mammaria discesa eccessivamente verso il basso e un contemporaneo riempimento dei quadranti superiori del seno.",
            "Con il tempo le tecniche chirurgiche riduttive si sono evolute e perfezionate, migliorando anche il risultato delle cicatrici. Nel caso di accertamenti di controllo come mammografia, ecografia e TAC, il radiologo e il ginecologo dovranno essere informati dell'intervento: questo li aiuterà a capire con maggiore chiarezza i risultati.",
        ],
        "facts": [("Motivi", "Estetici e funzionali (dolori a spalle, collo e schiena)"), ("Riduzione", "Fino a quattro/cinque taglie"), ("Inoltre", "Solleva il seno e riempie i quadranti superiori")],
        "meta": "Mastoplastica riduttiva del Dr. Giuseppe Colombo, Lugano: sollievo dal peso di un seno troppo grande, con una forma sollevata e naturale.",
    },
    "gynecomastia": {
        "group": "Chirurgia del seno", "title": "Ginecomastia", "subtitle": "Correzione del torace maschile",
        "lede": "Correggere un torace maschile che appare femminile.",
        "body": [
            "L'intervento è indicato per correggere un inestetismo tipicamente maschile che si può presentare con un abbondante accumulo adiposo a livello del torace (ginecomastia falsa) o con un abbondante accumulo di tessuto ghiandolare (ginecomastia vera). In qualche caso si possono manifestare contemporaneamente le due componenti (ginecomastia mista).",
            "L'intervento è molto richiesto dagli uomini di età compresa tra i 20 e i 40 anni che sentono il disagio di un torace poco virile perché femminilizzante.",
        ],
        "facts": [("Tipi", "Falsa (adiposa), vera (ghiandolare) o mista"), ("Pazienti tipici", "Uomini tra i 20 e i 40 anni")],
        "meta": "Ginecomastia: correzione del torace maschile del Dr. Giuseppe Colombo, Lugano.",
    },
}

RECONSTRUCTIVE = {
    "title": "Chirurgia ricostruttiva", "drawing": "dash-arrow",
    "lede": "Ripristinare forma e funzione — con un'attenzione particolare al volto dopo la chirurgia oncologica cutanea.",
    "focus": "Ho sempre avuto a cuore la chirurgia ricostruttiva e, sotto questo aspetto, mi occupo esclusivamente di ricostruzioni del distretto facciale post chirurgia oncologica cutanea.",
    "areas": ["Chirurgia dermatologica complessa", "Chirurgia dermatologica oncologica", "Chirurgia ricostruttiva del viso"],
    "body": ["Lo scopo della chirurgia ricostruttiva è quello di ripristinare la forma e la funzione di regioni anatomiche del viso e del corpo danneggiate o deformate. L'intervento chirurgico può migliorare o risolvere i problemi derivanti da traumi, tumori, ustioni, malformazioni congenite, infezioni, fratture facciali e lesioni nervose."],
    "techniques": [
        ("Innesti di pelle", "Trasferimento di tessuto cutaneo da una parte del corpo a un'altra per fornire una copertura con nuova pelle."),
        ("Lembi", "Trasferimento di tessuto cutaneo, adiposo, muscolare, cartilagineo e/o osseo da regioni limitrofe, senza interrompere l'afflusso vascolare, per riparare i difetti dei tessuti molli."),
        ("Autotrapianti", "Prelievo di tessuto come cartilagine, tendini, grasso, derma, muscolo, nervo od ossa da altre parti del corpo per fornire i componenti necessari alla ricostruzione."),
        ("Microchirurgia", "Ricostruzione di un tessuto mancante mediante trasferimento da un altro sito corporeo, con tecniche microchirurgiche per ristabilire l'apporto di sangue e la funzione nervosa."),
    ],
    "meta": "Chirurgia ricostruttiva del Dr. Giuseppe Colombo, Lugano: ricostruzione del viso dopo chirurgia oncologica cutanea, innesti, lembi e microchirurgia.",
}

ABOUT = [
    "Sono uno specialista in chirurgia plastica e ricostruttiva. Per mia grande fortuna, durante il periodo della mia formazione sono stato alla corte di grandi maestri di questa affascinante branca della chirurgia: in particolare ho trascorso lunghi periodi in Spagna e Francia e, ovviamente, in Italia. Sono stato consulente per anni di alcuni prestigiosi istituti ospedalieri, come l'Ospedale Evangelico Internazionale di Genova.",
    "Per cercare di offrire il miglior risultato possibile ai miei pazienti, ho concentrato la mia attenzione e la mia pratica sul distretto cervico-facciale e mammario: in particolare sugli interventi di lifting facciale e blefaroplastica per il volto, e sugli interventi di mastoplastica riduttiva, pessi e correttiva di aumento per la mammella. Ho sempre avuto a cuore la chirurgia ricostruttiva e, sotto questo aspetto, mi occupo esclusivamente di ricostruzioni del distretto facciale post chirurgia oncologica cutanea.",
    "Negli anni mi sono impegnato ad organizzare moltissimi corsi di dissezione per offrire ai colleghi la possibilità di condividere la mia esperienza e la loro. Con lo stesso spirito ho curato la redazione di un importante Atlante di Chirurgia. Con enorme piacere ospito nelle mie sale operatorie giovani medici e colleghi che hanno voglia di accrescere il loro bagaglio culturale. La medicina e la chirurgia fanno progressi rapidissimi ed offrono risultati sempre migliori se tutti i medici condividono la loro esperienza: questo è il mio spirito.",
    "Per quanto riguarda la mia filosofia inerente la medicina estetica e la chirurgia plastica, solo una parola guida la mia pratica: naturalezza. Mai cedere agli eccessi, mai stravolgere le persone, ma solo cercare di valorizzarle al meglio.",
]

MILESTONES = [
    ("2005", "Laurea in Medicina e Chirurgia", "Università di Genova — 110/110 con lode e medaglia al valore accademico. Tesi: studio sperimentale sull'espansione tissutale."),
    ("Specializzazione", "Chirurgia Plastica, Ricostruttiva ed Estetica", "Università di Genova — primo posto al concorso d'ingresso; diploma 50/50 con lode. Tesi: “Anatomia e tecniche chirurgiche di ringiovanimento facciale, trattamento dello SMAS. Evoluzione dei risultati nel tempo.”"),
    ("2007–08", "Borsa di studio SICPRE", "Società Italiana di Chirurgia Plastica, Ricostruttiva ed Estetica, per dissezioni anatomiche."),
    ("2008–10", "Formazione con i maestri", "Villa Bella, Salò (Prof. Botti) · Accademia di Anatomia Umana di Bruxelles · Clinica Quirón (Dr. Tapia), ringiovanimento del volto e lifting a triplice lembo di SMAS."),
    ("2009", "Senologia a Ginevra e Lione", "U.O.C. di Senologia, Ospedale Cantonale HUG di Ginevra, centro di riferimento europeo certificato EUSOMA · Chirurgia plastica e ricostruttiva, Centre Léon Bérard, Lione."),
    ("Dal 2008", "Anatomia a Nizza", "Frequenze regolari al Dipartimento di Anatomia Umana dell'Università Sophia-Antipolis di Nizza — regioni mammaria e cranio-facciale."),
    ("2010–18", "Direttore di corsi di dissezione", "Corsi teorico-pratici a Nizza e Madrid: viso, mammella, microchirurgia, rinoplastica e suture."),
    ("2013–15", "Co-Direttore, Ospedale Evangelico Internazionale", "Chirurgia Plastica e Ricostruttiva, Genova — e Direttore del Centro di eccellenza per la chirurgia plastica."),
    ("Oggi", "Autore e docente", "Curatore dello Stepwise Atlas of Aesthetic Medicine and Surgery (Springer) · Docente, Master di Chirurgia Estetica, Università di Pavia."),
]

CV_GROUPS = [
    ("Formazione", [
        "1999 — Diploma di Maturità classica.",
        "1999–2005 — Studi di Medicina e Chirurgia presso l'Università di Genova.",
        "2005 — Laurea in Medicina e Chirurgia presso l'Università di Genova con 110/110 con lode e medaglia al valore accademico. Tesi: studio sperimentale sull'espansione tissutale, in collaborazione tra il Dipartimento di Biochimica e la cattedra di Chirurgia Plastica.",
        "Primo posto al concorso per l'ingresso alla Scuola di Specialità in Chirurgia Plastica, Ricostruttiva ed Estetica dell'Università di Genova.",
        "Diploma di Specializzazione in Chirurgia Plastica, Ricostruttiva ed Estetica con 50/50 con lode. Tesi: “Anatomia e tecniche chirurgiche di ringiovanimento facciale, trattamento dello SMAS. Evoluzione dei risultati nel tempo.”",
        "Diploma Interuniversitario Europeo di Pratica in Chirurgia Oncologica — DIU Européen de Pratiques Chirurgicales en Cancérologie (Università di Lione, Nantes, Genova, Nancy, Parigi).",
    ]),
    ("Incarichi", [
        "Dal 2012 — Responsabile Chirurgia plastica ed estetica, Villa Serena, Genova.",
        "Giugno 2013 – Ottobre 2015 — Co-Direttore Chirurgia Plastica e Ricostruttiva, Ospedale Evangelico Internazionale, Genova.",
        "Direttore Centro di eccellenza per la chirurgia plastica — Ospedale Evangelico Internazionale, Genova.",
        "Docente Master di Chirurgia Estetica — Università di Pavia.",
        "2011–2013 — Consulente per la Chirurgia Plastica del Policlinico di Monza.",
        "Aprile 2011 – Dicembre 2013 — Consulente SUMAI per l'ASL2 Savonese, Chirurgia Plastica e Ricostruttiva, presidio ospedaliero di Cairo Montenotte.",
        "Da dicembre 2010 — Consulente Tecnico d'Ufficio per il Tribunale di Savona in Chirurgia Plastica, Ricostruttiva ed Estetica.",
        "Da gennaio 2010 — Consigliere della Società Polispecialistica dei Giovani Chirurghi, Sezione Liguria.",
    ]),
    ("Formazione clinica", [
        "2008, 2010 — Medico visitatore presso la Day Clinic Villa Bella di Salò (Prof. Botti): anatomia dei distretti cervico-facciale e mammario e principali tecniche di Chirurgia Estetica.",
        "Ottobre–novembre 2008 — Accademia di Anatomia Umana di Bruxelles: corso teorico-pratico con dissezioni su cadavere inerenti le principali tecniche di Chirurgia Estetica del volto.",
        "Marzo–giugno 2009 — Medico interno presso l'U.O.C. di Senologia dell'Ospedale Cantonale HUG di Ginevra (Prof. Jean-Bernard Dubuisson), centro di riferimento europeo certificato EUSOMA.",
        "Luglio 2009 e giugno–luglio 2010 — Medico visitatore presso la Clinica Quirón, chirurgia plastica ed estetica (Dr. Tapia): ringiovanimento del volto, lifting a triplice lembo di SMAS.",
        "Ottobre 2009 — Medico interno presso la Chirurgia Plastica e Ricostruttiva del Centre Léon Bérard di Lione, centro di riferimento per la ricostruzione mammaria in Francia.",
        "Dal 2008 — Frequenze mensili presso il Dipartimento di Anatomia Umana dell'Università Sophia-Antipolis di Nizza, con particolare interesse per la regione mammaria e cranio-facciale.",
    ]),
    ("Società e revisioni", [
        "2007–2008 — Vincitore della Borsa di studio SICPRE per dissezioni anatomiche.",
        "2008 — International Delegate, World Society of Anti-Aging Medicine.",
        "Dicembre 2008 — Tutor per l'utilizzo dei filler per la ditta Q-Med, sulla base dell'esperienza clinica.",
        "Reviewer per riviste internazionali indicizzate su PubMed-Medline: Minerva Chirurgica (dal 2009), Rare Tumors (dal 2009), Il Giornale di Chirurgia (dal 2010), Minerva Medica, World Journal of Surgical Oncology.",
    ]),
    ("Insegnamento", [
        "2007–2009 — Docente del corso di Anatomia Umana presso istituti superiori di Savona e Albenga.",
        "2010–2018 — Co-Direttore e Direttore di corsi teorico-pratici di anatomia e chirurgia a Nizza e Madrid (vedi Academy).",
    ]),
]

ATLAS = dict(EN.ATLAS)
ATLAS.update({
    "role": "Curatore",
    "text": [
        "Stepwise Atlas of Aesthetic Medicine and Surgery è un'opera di riferimento pratica e aggiornata per chi si avvicina o già opera nel campo della medicina e chirurgia estetica. Riccamente illustrato con oltre 320 fotografie originali e organizzato in due sezioni — teorica e pratica — accompagna il lettore attraverso tutti gli aspetti fondamentali delle procedure estetiche, dalla pianificazione pre-operatoria alla gestione post-operatoria, con un approccio chiaro e step by step.",
        "Ideale sia per giovani chirurghi che per professionisti esperti, copre tutte le principali aree anatomiche e tecniche, fornendo strumenti essenziali per eseguire trattamenti in sicurezza e con competenza.",
    ],
    "previous": {"title": EN.ATLAS["previous"]["title"], "note": "Atlante precedente, a cura di Giuseppe Colombo e Vittorio Ruvolo."},
})

FELLOWSHIP = [
    "Con enorme piacere il dott. Colombo condivide la sua esperienza con altri colleghi. I colleghi che vorranno partecipare alle fellowship seguiranno il dott. Colombo nelle cliniche dove esercita e negli studi dove effettua consulti e trattamenti di medicina estetica.",
    "La metà degli interventi chirurgici sono procedure facciali, l'altra metà sono interventi al seno. La segreteria potrà dare aiuto per trovare un'adeguata sistemazione al collega frequentatore, se deciderà di fermarsi per più giorni.",
]

COURSES = [
    {"year": "2024", "place": "Cremona · Palazzo Trecchi", "items": [
        {"date": "9–10 maggio 2024", "title": "Anatomia ragionata del volto e tecniche di ringiovanimento facciale. Dalla blefaroplastica al lifting: step by step"},
        {"date": "10 maggio 2024", "title": "Anatomia ragionata della piramide nasale. Rinoplastica step by step"},
        {"date": "8 giugno 2024", "title": "Medicina estetica del volto, live dissection: anatomia, tecniche e piani di iniezione step by step"},
    ]},
    {"year": "2018", "place": "Nizza · Università Sophia-Antipolis", "items": [
        {"date": "6–7 febbraio 2018", "title": "Cadaver lab — lifting facciale e blefaroplastica"},
        {"date": "7 febbraio 2018", "title": "Cadaver lab — rinoplastica"},
        {"date": "8–9 febbraio 2018", "title": "Cadaver lab — mastoplastica e gluteoplastica"},
    ]},
    {"year": "2017", "place": "Nizza · Università Sophia-Antipolis", "items": [
        {"date": "2017", "title": "Corso pratico di medicina estetica — KORU Anatomy & Surgery"},
    ]},
    {"year": "2015", "place": "Nizza · Università Sophia-Antipolis", "items": [
        {"date": "3–4 febbraio 2015", "title": "Chirurgia plastica estetica e anatomia ragionata del distretto cervico-facciale"},
        {"date": "5–6 febbraio 2015", "title": "Corso mammella"},
        {"date": "6 febbraio 2015", "title": "Anatomia chirurgica della regione addominale"},
        {"date": "6 febbraio 2015", "title": "Corso teorico-pratico di suture chirurgiche su cadavere"},
    ]},
    {"year": "2013", "place": "Savona", "items": [
        {"date": "8–9 giugno 2013", "title": "Biennale di Chirurgia Morfodinamica — decision making in aesthetic plastic surgery (co-presidente)"},
    ]},
]

COURSES_EARLY = [
    "Nizza, dicembre 2010 — Anatomia e tecniche chirurgiche di base delle regioni mammaria e glutea; anatomia e tecniche microchirurgiche di base (regioni anterolaterale di coscia, radiale, peroneale e dorsale).",
    "Nizza, giugno 2011 — Anatomia e tecniche chirurgiche di base delle regioni mammaria e glutea; microchirurgia di base.",
    "Madrid, ottobre 2011 — Anatomia e chirurgia di base della regione cervico-facciale; anatomia ragionata e tecniche di base in rino e profiloplastica.",
    "Nizza, dicembre 2011 — Chirurgia di base sulla mammella e regione glutea; microchirurgia di base.",
    "Nizza, aprile 2012 — Suture; chirurgia conservatrice del distretto cervico-facciale.",
    "Nizza, luglio 2012 — Tecniche chirurgiche del piede; anatomia ragionata dell'addome; suture.",
    "Madrid, ottobre 2012 — Microchirurgia; rino e profiloplastica; chirurgia plastica estetica di base e anatomia ragionata del distretto cervico-facciale; chirurgia e anatomia oncologica ragionata del distretto cervico-facciale.",
    "Nizza, febbraio 2013–2018 — Corsi annuali di lifting facciale e blefaroplastica, e di chirurgia della mammella e della regione glutea.",
]

JOURNAL_TITLES = {}  # Italian: the build uses each article's original Italian title

UI = {
    "skip": "Vai al contenuto", "home": "Home", "home_aria": "Dr. Giuseppe Colombo — home", "language": "Lingua",
    "book": "Prenota una consulenza", "menu": "Menu", "close": "Chiudi", "contact": "Contatti",
    "first_step": "— Il primo passo", "begin_html": "Inizia con una <em>conversazione</em>",
    "discover": "Scopri", "dr": "Dr. Colombo",
    "bk_label": "— Richiesta di consulenza", "bk_q1": "Di che cosa vorresti parlare?",
    "bk_opts": ["Viso — chirurgia", "Viso — medicina estetica", "Seno", "Chirurgia ricostruttiva", "Altro"],
    "bk_q2": "Dove preferisci incontrarci?", "bk_q3": "Come possiamo contattarti?",
    "bk_name": "Nome", "bk_email": "Email", "bk_phone": "Telefono", "bk_lang": "Lingua preferita",
    "bk_q4": "C'è qualcosa che vorresti farci sapere?", "bk_msg": "Messaggio (facoltativo)",
    "bk_consent": "Acconsento che i miei dati siano usati solo per rispondere a questa richiesta.",
    "bk_thanks": "Grazie.",
    "bk_done": "Si è aperta la tua app di posta con la richiesta indirizzata a {email}: invia il messaggio per completarla. La segreteria risponde {hours}.",
    "bk_conf": "I tuoi dati sono riservati.", "bk_back": "← Indietro", "bk_continue": "Continua", "bk_or_call": "Oppure chiama",
    "key_facts": "In sintesi", "facts_note": "Dai testi del Dr. Colombo. Ogni caso viene valutato individualmente durante la consulenza.",
    "the_procedure": "— L'intervento", "from_journal": "dal Journal", "video_it": "— Video",
    "videos_it": "— Video", "from_journal_label": "— Dal Journal", "in_italian": "",
    "read_article": "Leggi l'articolo", "also_in": "— Anche in", "min": "min", "min_read": "min di lettura",
    "discuss_html": "Parlane con il <em>Dr. Colombo</em>.", "discuss_sub": "Ogni percorso inizia con una consulenza — a Lugano, Zurigo o in Italia.",
    "begin_full_html": "Inizia con una <em>conversazione</em>.",
    "area_cta_sub": "Ogni trattamento inizia con l'ascolto — di ciò che desideri, e di ciò che la tua anatomia consente.",
    "recon_label": "— Chirurgia ricostruttiva", "recon_band": "Ricostruire il volto dopo la chirurgia oncologica cutanea.",
    "purpose": "— Scopo", "techniques": "— Tecniche", "play": "Guarda il video",
    "in_his_words": "— Con le sue parole", "thanks_trust": "Grazie per la fiducia.", "path": "— Percorso",
    "path_h_html": "Formato dai <em>maestri</em>.<br>Plasmato dall'anatomia.", "the_person": "— La persona",
    "person_h_html": "La medicina progredisce quando i medici <em>condividono</em>.",
    "person_p": "Giovani medici e colleghi sono i benvenuti nelle sue sale operatorie — lo stesso spirito dei corsi, delle fellowship e dell'Atlante.",
    "the_academy": "L'Academy", "discretion": "— Discrezione", "cv": "— Curriculum vitae", "cv_h": "Il curriculum completo.",
    "portrait_alt": "Ritratto del Dr. Giuseppe Colombo", "smile_alt": "Il Dr. Giuseppe Colombo sorridente",
    "academy_quote": "“La medicina e la chirurgia fanno progressi rapidissimi ed offrono risultati sempre migliori se tutti i medici condividono la loro esperienza: questo è il mio spirito.”",
    "on_page": "In questa pagina", "j_atlas": "L'Atlante", "j_fellow": "Fellowship", "j_courses": "Corsi", "j_pubs": "Pubblicazioni", "j_journal": "Journal", "j_videos": "Video",
    "atlas_label": "— L'Atlante", "view_springer": "Vedi su Springer ↗", "earlier_work": "— Opera precedente",
    "fellow_label": "— Fellowship", "fellow_h_html": "Metà viso.<br><em>Metà seno.</em>", "information": "Info e contatti:",
    "courses_label": "— Corsi e dissezioni", "courses_h_html": "Anatomia, <em>step by step.</em>",
    "courses_lead": "Le nuove date vengono pubblicate qui. Per informazioni sui prossimi corsi scrivi a",
    "brochure": "Brochure (PDF)", "poster": "Locandina del corso", "earlier_courses": "Corsi diretti in precedenza, 2010–2018",
    "pubs_label": "— Pubblicazioni", "pubs_h_html": "Lavori <em>pubblicati.</em>", "filter_topic": "Filtra per tema", "all": "Tutti",
    "journal_label": "— Journal", "journal_h_html": "Dal <em>Journal.</em>", "all_articles": "Tutti gli articoli",
    "topics": {"Face": "Viso", "Breast": "Seno", "Aesthetic medicine": "Medicina estetica", "Oncology": "Oncologia", "General": "Generale", "Research": "Ricerca", "Body": "Corpo"},
    "cats": {"Face": "Viso", "Breast": "Seno", "Body": "Corpo", "Aesthetic medicine": "Medicina estetica", "Philosophy": "Filosofia"},
    "journal": "Journal", "journal_lead": "Gli articoli del Dr. Colombo sul viso, sul seno, sulla medicina estetica e sulla storia della chirurgia plastica.",
    "latest": "Ultimo", "filter_cat": "Filtra per categoria", "article_note": "",
    "related_proc": "Intervento correlato:", "continue_reading": "— Continua a leggere", "academy": "Academy",
    "contact_h_html": "Inizia con una <em>conversazione.</em>",
    "contact_lead": "Consulenze a Lugano, Zurigo e in Italia, su appuntamento. La segreteria risponde {hours}.",
    "request_consult": "Richiedi una consulenza", "request_appt": "Richiedi un appuntamento",
    "telephone": "— Telefono", "email": "— Email", "info_appts": "Info e appuntamenti", "fellow_courses": "Fellowship e corsi",
    "map_text": "La mappa è fornita da Google e viene caricata solo se lo richiedi.", "show_map": "Mostra la mappa",
    "nf_h_html": "Questa pagina ha perso la sua <em>misura.</em>", "nf_p": "La pagina che cerchi non esiste — o si è spostata con il nuovo sito.", "nf_btn": "Torna alla home",
    "suffix": "Dr. Giuseppe Colombo · Chirurgia Plastica",
    "home_title": "Dr. Giuseppe Colombo — Chirurgia plastica del viso e del seno, Lugano",
    "home_meta": "Dr. Giuseppe Colombo, chirurgo plastico specializzato nella chirurgia plastica ed estetica del viso e del seno. Prenota una consulenza a Lugano, Zurigo o in Italia.",
    "phil_title": "Filosofia", "phil_meta": "Dr. Giuseppe Colombo: formazione, percorso e filosofia. Chirurgo plastico specializzato nel viso e nella mammella — naturalezza prima di tutto.",
    "acad_meta": "L'Academy del Dr. Giuseppe Colombo: lo Stepwise Atlas of Aesthetic Medicine and Surgery (Springer), fellowship, corsi di dissezione e pubblicazioni.",
    "journal_meta": "Gli articoli del Dr. Giuseppe Colombo su chirurgia del viso, del seno, medicina estetica e storia della chirurgia plastica.",
    "contact_title": "Contatti", "contact_meta": "Prenota una consulenza con il Dr. Giuseppe Colombo: Clinica Sant'Anna, Lugano; consulenze a Zurigo e in Italia su appuntamento.",
    "nf_title": "Pagina non trovata",
    "js": {
        "menu": "Menu", "close": "Chiudi", "send": "Invia la richiesta", "continue": "Continua",
        "e1": "Scegli un'opzione.", "e2": "Scegli una sede.", "e3": "Inserisci il tuo nome.",
        "e4": "Inserisci un indirizzo email valido.", "e5": "Conferma il consenso privacy.",
        "subject": "Richiesta di consulenza", "interest": "Interesse", "location": "Sede", "name": "Nome",
        "email": "Email", "phone": "Telefono", "language": "Lingua preferita", "map": "Mappa: Clinica Sant'Anna, Lugano",
    },
}

HOME = {
    "kicker": "— Dr. Giuseppe Colombo · Lugano",
    "hero_line_html": "Una sola parola guida la mia pratica: <em>naturalezza</em>.",
    "hero_sub": "Chirurgia plastica del viso e del seno",
    "philosophy": "— Filosofia", "doc_tr": "", "meet": "Chi sono",
    "beneath": "— Sotto la superficie", "layers_h": "Gli strati del volto",
    "steps": [
        ("01 · Pelle", "Ciò che vedi.", "La superficie — una barriera contro il vento, il sole e tutto ciò che incontriamo ogni giorno."),
        ("02 · Grasso", "Ciò che sta sotto.", "Uno strato di pochi millimetri, che con gli anni si sposta e scende."),
        ("03 · SMAS", "Ciò che sostiene.", "Lo strato profondo su cui lavora il chirurgo. Conoscerlo con precisione è fondamentale."),
        ("04 · Profondità", "Ciò che va protetto.", "I nervi che muovono il viso, le arterie più importanti e i muscoli della bocca si trovano tutti al di sotto."),
    ],
    "anat_close_html": "Un risultato naturale e duraturo nasce dal lavoro sulle strutture profonde — <em>non dalla trazione della pelle.</em>",
    "areas_label": "— Due distretti, una sola attenzione", "areas_h_html": "Viso. <em>Seno.</em>",
    "areas_lead": "Ho concentrato la mia attenzione e la mia pratica sul distretto cervico-facciale e mammario — per offrire il miglior risultato possibile ai miei pazienti.",
    "face_list": "Lifting · Blefaroplastica · Sopracciglio · Lip-lifting · Otoplastica · Mento · Medicina estetica",
    "breast_list": "Mastopessi · Additiva · Riduttiva · Ginecomastia",
    "recon_link": "Chirurgia ricostruttiva — ricostruire il volto dopo la chirurgia oncologica cutanea",
    "teacher": "— Docente e autore", "teacher_h_html": "Un chirurgo che <em>insegna</em> ai chirurghi.",
    "atlas_lead_html": "Curatore di <em>{title}</em> ({publisher}): oltre <strong data-count=\"320\">320</strong> fotografie originali che accompagnano il lettore, step by step, dalla pianificazione pre-operatoria alla gestione post-operatoria.",
    "facts": [("Ph.D.", "Università di Genova"), ("Docente", "Master di Chirurgia Estetica, Università di Pavia"), ("Corsi", "Nizza · Madrid · Cremona"), ("Fellowship", "Viso e seno")],
    "discover_academy": "Scopri l'Academy", "atlas_alt": "Copertina dello Stepwise Atlas of Aesthetic Medicine and Surgery, a cura di Giuseppe Colombo (Springer)",
    "discretion": "— Discrezione", "discretion_aria": "Discrezione",
    "place": "— Il luogo", "lugano_h_html": "Lugano, <em>Svizzera.</em>",
    "lugano_p": "Clinica Sant'Anna — studio e sala operatoria nella stessa sede.",
    "convo_h_pre": "Inizia con una", "convo_word": "conversazione",
    "convo_lead": "Raccontaci di che cosa vorresti parlare. La segreteria risponde {hours}.",
}
