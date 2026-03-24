# ═══════════════════════════════════════════════════════════════════════════════
# KRIMI DINNER — SZENARIO 01
# "Das Herrenhaus Dunkelbach"
# ═══════════════════════════════════════════════════════════════════════════════
# 4–10 Spieler · 90–120 Minuten · Zufälliger Mörder
# ═══════════════════════════════════════════════════════════════════════════════

SCENARIO = {
    "id": "dunkelbach",
    "title": "Das Herrenhaus Dunkelbach",
    "title_en": "Dunkelbach Manor",
    "min_players": 4,
    "max_players": 10,
    "description": {
        "de": "Ein Sommerabend, 1923. Baron Aldric von Dunkelbach lädt seine engsten Vertrauten zu einem Abendessen. Am Morgen danach findet man ihn tot in seiner Bibliothek. Wer war es — und warum?",
        "en": "A summer evening, 1923. Baron Aldric von Dunkelbach invites his closest confidants to a dinner. The next morning, he is found dead in his library. Who was it — and why?"
    },
    "atmosphere": "Eine Villa im Schwarzwald. Regen. Kamine. Weingläser. Geheimnisse.",
    "host_setup_note": {
        "de": "VOR DEM SPIEL: Verstecke einen gefalteten Zettel mit '§7 — Die Wahrheit liegt im Verborgenen' an einem geheimen Ort in deiner Wohnung. Du wirst später sagen wo. Stelle Wein oder Sekt bereit — das ist Teil des Spiels.",
        "en": "BEFORE THE GAME: Hide a folded note with '§7 — The truth lies hidden' somewhere secret in your home. You will reveal where later. Prepare wine or sparkling drinks — this is part of the game."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # ROLLEN
    # ─────────────────────────────────────────────────────────────────────────
    "roles": {

        # ── PFLICHT-ROLLEN (immer dabei, 4 Spieler) ──────────────────────────

        "butler": {
            "name": {"de": "Edmund, der Butler", "en": "Edmund, the Butler"},
            "min_players": 4,
            "can_be_murderer": True,
            "intro": {
                "de": "Ich bin Edmund Kraus, seit 31 Jahren Butler im Haus Dunkelbach. Ich kenne jeden Winkel, jedes Geheimnis dieser Villa. Der Baron war kein einfacher Mann — aber er war mein Mann.",
                "en": "I am Edmund Kraus, butler at Dunkelbach Manor for 31 years. I know every corner, every secret of this villa. The Baron was not a simple man — but he was my man."
            },
            "appearance": {
                "de": "Tadellos gekleidet. Immer mit weißen Handschuhen. Macht nervös kleine Handbewegungen wenn er lügt.",
                "en": "Impeccably dressed. Always white gloves. Makes small nervous hand movements when lying."
            },
            "secret": {
                "de": "Ich unterschlug seit 3 Jahren Geld aus der Haushaltskasse. Der Baron wusste es. Er hatte mir eine Woche gegeben um es zurückzuzahlen. Die Frist lief heute ab.",
                "en": "For 3 years I embezzled money from the household fund. The Baron knew. He gave me one week to repay it. The deadline was today."
            },
            "ability": {
                "name": {"de": "Herr des Hauses", "en": "Master of the House"},
                "description": {"de": "Du kennst jeden Raum. Einmal pro Spiel kannst du einen anderen Spieler fragen: 'Wo warst du um Mitternacht?' — er muss antworten, darf aber lügen. Du siehst ob seine Antwort mit den Grundrissen übereinstimmt.",
                "en": "You know every room. Once per game you may ask another player: 'Where were you at midnight?' — they must answer but may lie. You can tell if their answer matches the floor plan."}
            },
            "win_condition": {
                "de": "Überlebe. Werde nicht als Mörder verurteilt. Wenn der echte Mörder gefasst wird, gewinnst du — außer jemand beweist deinen Diebstahl. Dann verlierst du trotz allem.",
                "en": "Survive. Don't get convicted as murderer. If the real killer is caught, you win — unless someone proves your theft. Then you lose despite everything."
            },
            "murderer_motive_if_assigned": {
                "de": "Der Baron hatte ein Testament geändert — Edmund würde nichts erben. Schlimmer: Er würde angezeigt. Edmund vergiftete den Wein des Barons mit Digitalis aus der Gartenküche.",
                "en": "The Baron had changed his will — Edmund would inherit nothing. Worse: he would be reported. Edmund poisoned the Baron's wine with digitalis from the garden kitchen."
            },
            "clues_i_hold": ["key_cellar", "household_ledger"],
            "starting_knowledge": {
                "de": "Du weißt, dass der Baron heute Nachmittag ein Telegramm erhalten hat. Du hast es nicht gelesen — aber du hast gesehen wie er danach bebte.",
                "en": "You know the Baron received a telegram this afternoon. You didn't read it — but you saw how he trembled afterwards."
            }
        },

        "niece": {
            "name": {"de": "Constanze, die Nichte", "en": "Constanze, the Niece"},
            "min_players": 4,
            "can_be_murderer": True,
            "intro": {
                "de": "Constanze von Dunkelbach, die einzige Verwandte des Barons. Ich bin nicht seinetwegen hier — ich bin wegen dem, was ihm gehört.",
                "en": "Constanze von Dunkelbach, the Baron's only living relative. I'm not here for him — I'm here for what belongs to him."
            },
            "appearance": {
                "de": "Elegant aber angespannt. Überprüft ständig ihr Handtäschchen. Hat einen versiegelten Brief dabei den sie niemanden zeigt.",
                "en": "Elegant but tense. Constantly checks her handbag. Carries a sealed letter she shows no one."
            },
            "secret": {
                "de": "Der Baron hatte versprochen, mir sein gesamtes Vermögen zu hinterlassen. Letzten Monat erfuhr ich durch einen Anwalt: Er hatte das Testament geändert. Ich erbe fast nichts.",
                "en": "The Baron had promised to leave me his entire fortune. Last month I learned from a lawyer: he had changed the will. I inherit almost nothing."
            },
            "ability": {
                "name": {"de": "Das Erbe", "en": "The Inheritance"},
                "description": {"de": "Du trägst einen echten Brief. Du entscheidest wann du ihn öffnest und vorliest. Der Inhalt des Briefes verändert das Spiel — er enthält einen Hinweis auf die wahre Todesursache. Aber wenn du ihn zu früh zeigst, machst du dich verdächtig.",
                "en": "You carry a real letter. You decide when to open and read it aloud. The letter's contents change the game — it contains a clue to the true cause of death. But showing it too early makes you suspicious."}
            },
            "win_condition": {
                "de": "Überlebe. Wenn der Mörder gefasst wird: Du gewinnst nur wenn niemand das neue Testament findet. Findet jemand das Testament, gewinnst du nur wenn du den Mörder als erste benennst.",
                "en": "Survive. If the killer is caught: You win only if nobody finds the new will. If someone finds it, you only win if you're the first to name the murderer."
            },
            "murderer_motive_if_assigned": {
                "de": "Das neue Testament hätte Constanze ruiniert. Sie fand in der Bibliothek Raum und Gelegenheit — und das Brieföffner-Messer des Barons.",
                "en": "The new will would have ruined Constanze. She found room and opportunity in the library — and the Baron's letter opener."
            },
            "clues_i_hold": ["sealed_letter", "new_will_location"],
            "starting_knowledge": {
                "de": "Du weißt wo das neue Testament liegt. Du hast es heute Nachmittag heimlich gelesen. Du wirst alles dafür tun dass es niemand findet.",
                "en": "You know where the new will is. You read it secretly this afternoon. You will do anything to make sure nobody finds it."
            }
        },

        "witness": {
            "name": {"de": "Marta, die Zeugin", "en": "Marta, the Witness"},
            "min_players": 4,
            "can_be_murderer": False,
            "intro": {
                "de": "Ich bin Marta Stein, Schriftstellerin. Der Baron kannte meine Mutter. Er lud mich zum Dinner ein — ich dachte, es wäre eine nette Gelegenheit. Ich hätte es ablehnen sollen.",
                "en": "I am Marta Stein, a writer. The Baron knew my mother. He invited me to dinner — I thought it would be a nice occasion. I should have declined."
            },
            "appearance": {
                "de": "Beobachtet alles. Macht mentale Notizen. Hat immer ein kleines Notizbuch dabei. Spricht wenig, hört viel.",
                "en": "Observes everything. Takes mental notes. Always has a small notebook. Speaks little, listens much."
            },
            "secret": {
                "de": "Ich habe etwas gesehen. Kurz vor Mitternacht, durchs Fenster. Ich weiß selbst nicht genau was — eine Silhouette, Bewegung, ein Licht das ausging. Ich habe Angst zu sagen was ich gesehen habe.",
                "en": "I saw something. Just before midnight, through the window. I'm not sure exactly what — a silhouette, movement, a light going out. I'm afraid to say what I saw."
            },
            "ability": {
                "name": {"de": "Die Beobachterin", "en": "The Observer"},
                "description": {"de": "Du erhältst im Laufe des Spiels automatisch Hinweise durch deine Beobachtungsgabe — ohne danach suchen zu müssen. Aber: Jeder dieser Hinweise kommt mit einer Frage die nur du beantworten kannst. Beantworten bringt mehr Hinweise. Schweigen ist sicherer aber langsamer.",
                "en": "Throughout the game you automatically receive clues through your observational skills — without searching for them. But: Each clue comes with a question only you can answer. Answering brings more clues. Silence is safer but slower."}
            },
            "win_condition": {
                "de": "Wenn du am Ende die richtige Person nennst UND beweist was du gesehen hast, gewinnst du allein — selbst wenn die Mehrheit falsch liegt.",
                "en": "If at the end you name the right person AND prove what you saw, you win alone — even if the majority is wrong."
            },
            "clues_i_hold": [],
            "starting_knowledge": {
                "de": "Du hast eine Silhouette gesehen. Du weißt noch nicht wer es war. Im Laufe des Spiels werden sich deine Erinnerungen schärfen — aber nur wenn du aktiv sprichst.",
                "en": "You saw a silhouette. You don't yet know who it was. As the game progresses your memory will sharpen — but only if you actively speak."
            }
        },

        "doctor": {
            "name": {"de": "Dr. Heinrich Voss", "en": "Dr. Heinrich Voss"},
            "min_players": 4,
            "can_be_murderer": True,
            "intro": {
                "de": "Dr. Heinrich Voss, Arzt. Der Baron war mein Patient — und mein Freund. Ich war heute Abend dabei. Ich hätte es verhindern sollen.",
                "en": "Dr. Heinrich Voss, physician. The Baron was my patient — and my friend. I was there tonight. I should have prevented it."
            },
            "appearance": {
                "de": "Ruhig. Professionell. Hat immer eine kleine Arzttasche dabei. Wird blass wenn jemand über Gift spricht.",
                "en": "Calm. Professional. Always carries a small doctor's bag. Goes pale when someone mentions poison."
            },
            "secret": {
                "de": "Vor zwei Jahren verschrieb ich dem Baron das falsche Medikament. Er wurde fast blind. Er hatte mir vergeben — oder so dachte ich. Heute Abend teilte er mir mit: Er hatte eine Klage eingereicht. Meine Karriere wäre vorbei.",
                "en": "Two years ago I prescribed the Baron the wrong medication. He almost went blind. He had forgiven me — or so I thought. This evening he informed me: he had filed a complaint. My career would be over."
            },
            "ability": {
                "name": {"de": "Die Autopsie", "en": "The Autopsy"},
                "description": {"de": "Du allein kannst die Todesursache offiziell bestimmen. Wenn du dein Ergebnis verkündest, glauben es alle — außer einer Person (der Mörder weiß dass du recht oder unrecht hast). Aber Achtung: Du kannst auch absichtlich lügen. Nur du weißt das.",
                "en": "Only you can officially determine the cause of death. When you announce your finding, everyone believes it — except one person (the murderer knows if you're right or wrong). But beware: you can deliberately lie. Only you know that."}
            },
            "win_condition": {
                "de": "Wenn du die Todesursache korrekt benennst UND den richtigen Mörder mitbenennst, erhältst du den Ehrentitel 'Meisterdetektiv'. Lügst du bei der Todesursache und der Mörder entkommt, verlierst du.",
                "en": "If you correctly name the cause of death AND name the right murderer, you receive the honorary title 'Master Detective'. If you lie about the cause of death and the murderer escapes, you lose."
            },
            "murderer_motive_if_assigned": {
                "de": "Heinrich Voss tötete den Baron mit einer Überdosis seines eigenen Herzmedikaments — ein Tod der wie natürlich aussieht. Fast perfekt. Fast.",
                "en": "Heinrich Voss killed the Baron with an overdose of his own heart medication — a death that looks natural. Almost perfect. Almost."
            },
            "clues_i_hold": ["medical_bag", "cause_of_death"],
            "starting_knowledge": {
                "de": "Du weißt: Der Baron hatte ein Herzleiden. Die Medikamente die er nahm könnten bei falscher Dosierung tödlich sein. Das ist kein Geheimnis — aber nicht jeder weiß es.",
                "en": "You know: The Baron had a heart condition. The medication he took could be lethal at the wrong dosage. This isn't secret — but not everyone knows it."
            }
        },

        # ── OPTIONALE ROLLEN (kommen hinzu je nach Spielerzahl) ───────────────

        "cook": {
            "name": {"de": "Rosa, die Köchin", "en": "Rosa, the Cook"},
            "min_players": 5,
            "can_be_murderer": True,
            "intro": {
                "de": "Rosa Müller, Köchin seit 8 Jahren im Haus Dunkelbach. Ich habe das Dinner gekocht. Ich habe alles gesehen. Ich sage nichts.",
                "en": "Rosa Müller, cook for 8 years at Dunkelbach Manor. I cooked the dinner. I saw everything. I say nothing."
            },
            "appearance": {
                "de": "Nervös. Hände immer in Bewegung. Vermeidet Blickkontakt. Hat ein kleines Kruzifix um den Hals das sie ständig berührt.",
                "en": "Nervous. Hands always moving. Avoids eye contact. Has a small crucifix around her neck she constantly touches."
            },
            "secret": {
                "de": "Jemand kam heute Nachmittag in meine Küche und bat mich etwas in das Essen des Barons zu geben. Ich dachte es sei Herzstärkendes. Ich stellte keine Fragen. Ich bekam Geld. Viel Geld.",
                "en": "Someone came to my kitchen this afternoon and asked me to put something in the Baron's food. I thought it was a heart tonic. I asked no questions. I received money. A lot of money."
            },
            "ability": {
                "name": {"de": "Was in der Küche geschah", "en": "What Happened in the Kitchen"},
                "description": {"de": "Einmal kannst du die Wahrheit enthüllen: Wer dich beauftragte. Aber du weißt nur einen Namen — und du bist nicht sicher ob dieser Name der Mörder ist oder nur ein Werkzeug. Diese Enthüllung verändert das komplette Spiel.",
                "en": "Once you may reveal the truth: who hired you. But you only know a name — and you're not sure if that name is the murderer or just a pawn. This revelation changes the entire game."}
            },
            "win_condition": {
                "de": "Du überlebst wenn du die Wahrheit sagst ODER wenn niemand herausfindet was du getan hast. Schweigen ist riskant — aber reden auch.",
                "en": "You survive if you tell the truth OR if nobody discovers what you did. Silence is risky — but so is talking."
            },
            "murderer_motive_if_assigned": {
                "de": "Rosa liebte den Baron — aber er behandelte sie wie Möbel. Sie beauftragte sich selbst. Sie mixte Gift in seine Suppe. Dann aß sie selbst davon, um unverdächtig zu sein. Nur wenig — nicht genug.",
                "en": "Rosa loved the Baron — but he treated her like furniture. She commissioned herself. She mixed poison into his soup. Then ate some herself, to avoid suspicion. Only a little — not enough."
            },
            "clues_i_hold": ["kitchen_substance", "payment_receipt"],
            "starting_knowledge": {
                "de": "Du weißt was du dem Baron gegeben hast. Du weißt aber nicht ob es ihn getötet hat. Das erfährst du wenn der Arzt die Todesursache nennt.",
                "en": "You know what you gave the Baron. But you don't know if it killed him. You'll find out when the doctor names the cause of death."
            }
        },

        "stranger": {
            "name": {"de": "Der Fremde", "en": "The Stranger"},
            "min_players": 5,
            "can_be_murderer": True,
            "intro": {
                "de": "Ich gebe meinen Namen nicht preis. Der Baron wusste wer ich bin. Der Rest von euch wird es erfahren — wenn ich es für richtig halte.",
                "en": "I don't reveal my name. The Baron knew who I am. The rest of you will learn — when I see fit."
            },
            "appearance": {
                "de": "Keine Erklärung warum er/sie hier ist. Hat eine Visitenkarte die nur eine Nummer trägt. Spricht selten — aber wenn, dann sehr präzise.",
                "en": "No explanation for being here. Carries a business card with only a number on it. Speaks rarely — but when they do, very precisely."
            },
            "secret": {
                "de": "Ich bin ein Privatdetektiv. Der Baron hat mich engagiert um jemanden in dieser Runde zu beschatten. Ich darf nicht sagen wen — das steht in meinem Vertrag. Nun ist mein Auftraggeber tot.",
                "en": "I am a private detective. The Baron hired me to surveil someone in this group. I may not say who — that's in my contract. Now my client is dead."
            },
            "ability": {
                "name": {"de": "Die Akte", "en": "The File"},
                "description": {"de": "Du hast eine Akte über eine Person am Tisch. Du darfst jeden Hinweis aus dieser Akte anonym weitergeben — aber nie direkt. Jede Weitergabe trägt das Risiko dass man dich als Quelle identifiziert.",
                "en": "You have a file on one person at the table. You may pass any clue from this file anonymously — but never directly. Each pass carries the risk of being identified as the source."}
            },
            "win_condition": {
                "de": "Du gewinnst wenn dein Klient gerächt wird — also wenn der echte Mörder gefasst wird. Aber du verlierst wenn die Person die du beschattest verurteilt wird UND es der falsche Mörder ist.",
                "en": "You win if your client is avenged — that is, if the real murderer is caught. But you lose if the person you were surveilling is convicted AND they're the wrong murderer."
            },
            "murderer_motive_if_assigned": {
                "de": "Der Fremde entdeckte: Der Baron plante ihn/sie zu ruinieren. Das 'Beschatten' war ein Test — ein Vertrauenstest. Den hatte der Fremde bestanden. Dann erfuhr er/sie die Wahrheit. Und handelte.",
                "en": "The Stranger discovered: the Baron planned to ruin them. The 'surveillance' was a test — a test of trust. The Stranger had passed it. Then they learned the truth. And acted."
            },
            "clues_i_hold": ["surveillance_file", "telegram_copy"],
            "starting_knowledge": {
                "de": "Du weißt wer in dieser Runde die meisten Geheimnisse hat. Du weißt es nicht durch Magie — sondern weil du seit Wochen Notizen machst.",
                "en": "You know who in this group has the most secrets. Not through magic — because you've been taking notes for weeks."
            }
        },

        "detective": {
            "name": {"de": "Inspektor Wahl", "en": "Inspector Wahl"},
            "min_players": 6,
            "can_be_murderer": False,
            "intro": {
                "de": "Inspektor Karl Wahl, Kriminalpolizei München. Ich bin nicht als Gast hier — ich war bereits auf dem Weg zum Baron als ich die Nachricht erhielt. Der Baron hatte mich gerufen. Er hatte Angst.",
                "en": "Inspector Karl Wahl, Criminal Police Munich. I'm not here as a guest — I was already on my way to the Baron when I received the news. The Baron had summoned me. He was afraid."
            },
            "appearance": {
                "de": "Trägt trotz Gesellschaft keine Abendkleidung. Schreibt alles auf. Hat kalte Augen die nichts vergessen.",
                "en": "Despite the social setting, doesn't wear evening clothes. Writes everything down. Has cold eyes that forget nothing."
            },
            "secret": {
                "de": "Der Brief den der Baron mir schickte enthielt einen Namen: eine Person am heutigen Tisch. Der Baron fürchtete diese Person. Ich habe diesen Brief — aber ich darf ihn aus rechtlichen Gründen noch nicht zeigen.",
                "en": "The letter the Baron sent me contained a name: one person at today's table. The Baron feared this person. I have this letter — but for legal reasons I cannot yet show it."
            },
            "ability": {
                "name": {"de": "Offizielles Verhör", "en": "Official Interrogation"},
                "description": {"de": "Einmal kannst du ein offizielles Verhör ausrufen. Jeder muss die Gruppe verlassen — du redest 2 Minuten allein mit einer Person. Was in diesen 2 Minuten gesagt wird, entscheidet ihr selbst. Aber danach muss jeder sagen ob die Person kooperativ war.",
                "en": "Once you may call an official interrogation. Everyone must leave the group — you talk alone with one person for 2 minutes. What happens in those 2 minutes is up to you. But afterwards everyone must say whether the person was cooperative."}
            },
            "win_condition": {
                "de": "Du gewinnst nur wenn DU den Mörder als erster offiziell benennst — mit Beweisen. Benennt jemand anderes den Mörder zuerst korrekt, gewinnst du nur Bronze.",
                "en": "You win only if YOU are the first to officially name the murderer — with evidence. If someone else names the murderer correctly first, you only get bronze."
            },
            "clues_i_hold": ["baron_letter", "suspects_list"],
            "starting_knowledge": {
                "de": "Der Baron schrieb dir: 'Ich fürchte [NAME]. Wenn mir etwas passiert — suche in der Bibliothek unter dem Teppich.' Du hast diesen Brief. Und du weißt welcher Name darin steht. Aber dieser Name ist nicht zwingend der Mörder.",
                "en": "The Baron wrote to you: 'I fear [NAME]. If something happens to me — look in the library under the carpet.' You have this letter. And you know which name it contains. But this name is not necessarily the murderer."
            }
        },

        "lover": {
            "name": {"de": "Viktor, der Geliebte", "en": "Viktor, the Lover"},
            "min_players": 7,
            "can_be_murderer": True,
            "intro": {
                "de": "Viktor Reiss, Geschäftspartner des Barons. Wir kannten uns gut. Sehr gut. Zu gut, wenn ich ehrlich bin.",
                "en": "Viktor Reiss, business partner of the Baron. We knew each other well. Very well. Too well, if I'm honest."
            },
            "appearance": {
                "de": "Charmant. Zu charmant. Hat ein Monogramm-Taschentuch. Wird rot wenn jemand bestimmte Namen nennt.",
                "en": "Charming. Too charming. Has a monogrammed handkerchief. Turns red when certain names are mentioned."
            },
            "secret": {
                "de": "Viktor und eine andere Person am Tisch haben eine geheime Affäre. Beide wissen es. Keiner darf es zugeben. Viktors Alibi — er war nicht allein um Mitternacht — kann nur bewiesen werden wenn die andere Person die Affäre zugibt. Aber das würde sie/ihn ruinieren.",
                "en": "Viktor and another person at the table have a secret affair. Both know it. Neither may admit it. Viktor's alibi — he was not alone at midnight — can only be proven if the other person admits the affair. But that would ruin them."
            },
            "ability": {
                "name": {"de": "Das Alibi", "en": "The Alibi"},
                "description": {"de": "Du warst nicht allein. Du kannst deinen geheimen Partner um Bestätigung bitten — aber nur einmal, per Privatnachricht in der App. Er oder sie entscheidet ob sie dich decken. Tun sie es nicht, wirst du automatisch der Hauptverdächtige.",
                "en": "You were not alone. You can ask your secret partner for confirmation — but only once, via private message in the app. They decide whether to cover for you. If they don't, you automatically become the prime suspect."}
            },
            "win_condition": {
                "de": "Du überlebst wenn dein Alibi bestätigt wird ODER wenn der echte Mörder gefasst wird ohne dass deine Affäre öffentlich wird.",
                "en": "You survive if your alibi is confirmed OR if the real murderer is caught without your affair becoming public."
            },
            "murderer_motive_if_assigned": {
                "de": "Der Baron entdeckte die Affäre. Er drohte mit Veröffentlichung. Viktor konnte nicht zulassen dass sein Ruf — und der seiner Geliebten — vernichtet wurde.",
                "en": "The Baron discovered the affair. He threatened to publicize it. Viktor could not allow his reputation — and that of his lover — to be destroyed."
            },
            "clues_i_hold": ["business_contract", "affair_evidence"],
            "starting_knowledge": {
                "de": "Du weißt: Eine andere Person am Tisch ist dein/e Geliebte/r. Die App hat euch beide informiert wer das ist. Ihr müsst das geheim halten — aber auch voneinander lernen.",
                "en": "You know: one other person at this table is your secret lover. The app has informed you both who that is. You must keep it secret — but also learn from each other."
            }
        },

        "heir": {
            "name": {"de": "Maximilian, der Erbe", "en": "Maximilian, the Heir"},
            "min_players": 8,
            "can_be_murderer": True,
            "intro": {
                "de": "Maximilian von Furst. Ich bin durch Heirat mit dem Dunkelbach-Clan verbunden. Der Baron war mein Onkel durch Adoption. Ich komme selten her — aber heute musste ich.",
                "en": "Maximilian von Furst. I am connected to the Dunkelbach clan by marriage. The Baron was my uncle by adoption. I rarely come here — but today I had to."
            },
            "appearance": {
                "de": "Ungepflegt für einen Mann seines Standes. Trinkt zu schnell. Hat jemanden mitgebracht — einen Anwalt, der draußen wartet.",
                "en": "Unkempt for a man of his standing. Drinks too quickly. Has brought someone — a lawyer who waits outside."
            },
            "secret": {
                "de": "Ich bin tief verschuldet. Der Baron war die einzige Person die mich hätte retten können. Ich kam heute um ihn um Geld zu bitten. Er sagte nein. Er lachte mich an.",
                "en": "I am deeply in debt. The Baron was the only person who could have saved me. I came today to ask him for money. He said no. He laughed at me."
            },
            "ability": {
                "name": {"de": "Der Anwalt", "en": "The Lawyer"},
                "description": {"de": "Du hast einen Anwalt dabei. Einmal kannst du ihn rufen. Er erscheint und liest das Testament vor — das echte, aktuelle Testament. Das verändert alles. Aber Vorsicht: Der Inhalt könnte dich ruinieren.",
                "en": "You have a lawyer with you. Once you may call him. He appears and reads the will — the real, current will. That changes everything. But beware: the contents could ruin you."}
            },
            "win_condition": {
                "de": "Du gewinnst wenn das Testament nicht verlesen wird ODER wenn deine Schulden darin erwähnt werden aber der Mörder trotzdem gefasst wird. Du verlierst wenn das Testament verlesen wird und deine Demütigung öffentlich wird.",
                "en": "You win if the will is not read OR if your debts are mentioned in it but the murderer is still caught. You lose if the will is read and your humiliation becomes public."
            },
            "murderer_motive_if_assigned": {
                "de": "Maximilian tötete den Baron bevor er das Testament unterzeichnen konnte. Das alte Testament — das er noch nicht ändern konnte — macht Maximilian reich. Wenn das neue Testament existiert, ist er ruiniert.",
                "en": "Maximilian killed the Baron before he could sign the will. The old will — which he hadn't changed yet — makes Maximilian rich. If the new will exists, he is ruined."
            },
            "clues_i_hold": ["debt_documents", "old_will"],
            "starting_knowledge": {
                "de": "Du weißt: Das alte Testament begünstigt dich. Das neue — das du gesehen hast bevor der Baron es unterschreiben konnte — nicht. Du musst verhindern dass es unterschrieben oder gefunden wird.",
                "en": "You know: the old will favours you. The new one — which you saw before the Baron could sign it — does not. You must prevent it from being signed or found."
            }
        },

        "shadow": {
            "name": {"de": "Die Schatten-Figur", "en": "The Shadow"},
            "min_players": 6,
            "can_be_murderer": False,
            "is_wildcard": True,
            "intro": {
                "de": "Ich bin... niemand besonderes. Ein Gast. Vergesst mich.",
                "en": "I am... nobody special. A guest. Forget me."
            },
            "appearance": {
                "de": "Unauffällig. Das ist Absicht. Aber wer genau hinschaut sieht: diese Person beobachtet alles sehr genau.",
                "en": "Inconspicuous. That's intentional. But those who look carefully see: this person is watching everything very closely."
            },
            "secret": {
                "de": "Du bist kein Gast. Du bist ein Erpresser. Du weißt über die meisten Personen am Tisch etwas Belastendes. Du bist heute Abend hier um das neue Testament zu stehlen — und zu vernichten. Du schuldest jemandem Geld. Viel Geld.",
                "en": "You are not a guest. You are a blackmailer. You know something damaging about most people at the table. You are here tonight to steal the new will — and destroy it. You owe someone money. A lot of money."
            },
            "ability": {
                "name": {"de": "Der Diebstahl", "en": "The Theft"},
                "description": {
                    "de": "Du hast eine einzige spezielle Aktion: Das Testament stehlen. Wenn du weißt wo es liegt (Hinweis durch Beobachten anderer), kannst du in der App 'Testament stehlen' auswählen. Wenn du dabei unentdeckt bleibst: Du gewinnst. Wird du entdeckt: Du verlierst sofort.",
                    "en": "You have one special action: steal the will. If you know where it is (by observing others), you can select 'Steal will' in the app. If you remain undiscovered: You win. If you're caught: You lose immediately."
                }
            },
            "win_condition": {
                "de": "DU GEWINNST NUR wenn du das Testament stiehlst UND zerstörst ohne entdeckt zu werden. Das ist schwer. Das soll schwer sein. Dein Sieg beeinflusst alle anderen — das Spiel geht weiter aber das Testament existiert nicht mehr.",
                "en": "YOU WIN ONLY if you steal the will AND destroy it without being discovered. This is hard. It should be hard. Your victory affects everyone — the game continues but the will no longer exists."
            },
            "clues_i_hold": ["blackmail_files"],
            "starting_knowledge": {
                "de": "Du weißt über 3 Personen am Tisch etwas Belastendes. Die App zeigt dir diese Infos privat. Du entscheidest welche du nutzt — aber jede Nutzung macht dich sichtbarer.",
                "en": "You know something damaging about 3 people at the table. The app shows you this info privately. You decide which to use — but each use makes you more visible."
            }
        },

        "medium": {
            "name": {"de": "Eleonore, das Medium", "en": "Eleonore, the Medium"},
            "min_players": 9,
            "can_be_murderer": False,
            "intro": {
                "de": "Eleonore Baum. Der Baron lud mich ein um... nun. Er glaubte an das Übernatürliche. Ich tue es nicht. Aber ich spielte das Spiel für ihn. Und heute Nacht — ich höre ihn. Ich höre ihn wirklich.",
                "en": "Eleonore Baum. The Baron invited me to... well. He believed in the supernatural. I don't. But I played along for him. And tonight — I hear him. I really hear him."
            },
            "appearance": {
                "de": "Hat immer die Augen halb geschlossen. Spricht in Rätseln. Niemand weiß ob es Schauspiel oder Ernst ist.",
                "en": "Always has eyes half-closed. Speaks in riddles. Nobody knows if it's theatre or serious."
            },
            "secret": {
                "de": "Eleonore hört den Toten nicht wirklich — aber sie hat etwas im Zimmer des Barons gefunden. Etwas das sie sich nicht erklären kann. Und sie hat Angst.",
                "en": "Eleonore doesn't really hear the dead — but she found something in the Baron's room. Something she can't explain. And she's afraid."
            },
            "ability": {
                "name": {"de": "Die Botschaft", "en": "The Message"},
                "description": {
                    "de": "Einmal im Spiel kannst du eine 'Botschaft vom Toten' übermitteln. Diese Botschaft ist echt — sie enthält einen echten Hinweis den nur du kennst. Aber du darfst nicht erklären woher du ihn hast. Glaubt man dir — großes Momentum. Glaubt man dir nicht — du wirst verdächtig.",
                    "en": "Once in the game you may deliver a 'message from the dead'. This message is real — it contains a real clue only you know. But you may not explain where you got it. If believed — huge momentum. If not — you become suspicious."
                }
            },
            "win_condition": {
                "de": "Du gewinnst wenn deine Botschaft zum Fassen des Mörders beiträgt UND du nicht als Scharlatan entlarvt wirst.",
                "en": "You win if your message contributes to catching the murderer AND you're not exposed as a charlatan."
            },
            "clues_i_hold": ["barons_journal", "hidden_room_key"],
            "starting_knowledge": {
                "de": "Du fandst im Zimmer des Barons ein verstecktes Tagebuch. Du hast nur die letzte Seite gelesen. Sie enthält den Namen einer Person — aber dieser Name könnte der Mörder oder das Opfer eines anderen Plans sein.",
                "en": "You found a hidden diary in the Baron's room. You only read the last page. It contains a name — but this name could be the murderer or the victim of another plan."
            }
        },

        "journalist": {
            "name": {"de": "Frederic, der Journalist", "en": "Frederic, the Journalist"},
            "min_players": 10,
            "can_be_murderer": True,
            "intro": {
                "de": "Frederic Haas, Redakteur der Münchner Zeitung. Der Baron ist eine öffentliche Person — sein Tod ist eine Geschichte. Eine sehr gute Geschichte.",
                "en": "Frederic Haas, editor of the Munich Gazette. The Baron is a public figure — his death is a story. A very good story."
            },
            "appearance": {
                "de": "Hat immer Block und Stift in der Hand. Stellt Fragen auch wenn niemand antwortet. Hat keine Hemmungen.",
                "en": "Always has notebook and pen in hand. Asks questions even when nobody answers. Has no inhibitions."
            },
            "secret": {
                "de": "Frederic schrieb bereits den Artikel — bevor der Baron starb. Er wusste was passieren würde. Jemand hatte ihn informiert. Er verkauft diese Information nicht — weil er Angst hat. Großer Angst.",
                "en": "Frederic had already written the article — before the Baron died. He knew what would happen. Someone had informed him. He's not selling this information — because he's afraid. Very afraid."
            },
            "ability": {
                "name": {"de": "Die Enthüllung", "en": "The Revelation"},
                "description": {
                    "de": "Du kannst jederzeit eine 'Pressemitteilung' machen — eine öffentliche Enthüllung an alle. Diese Enthüllung enthält einen echten Fakt. Aber: Jede Enthüllung macht dich zum Ziel. Der Mörder wird versuchen dich zu diskreditieren.",
                    "en": "At any time you may make a 'press statement' — a public announcement to everyone. This contains a real fact. But: each revelation makes you a target. The murderer will try to discredit you."
                }
            },
            "win_condition": {
                "de": "Du gewinnst wenn du ZUERST den Mörder öffentlich benennst. Du verlierst wenn du den falschen Mörder nennst.",
                "en": "You win if you're FIRST to publicly name the murderer. You lose if you name the wrong murderer."
            },
            "murderer_motive_if_assigned": {
                "de": "Frederic war kein Journalist. Er war ein Erpresser mit Presseausweis. Der Baron hatte ihn enttarnt. Der Artikel war sein letzter Versuch Druck auszuüben.",
                "en": "Frederic was not a journalist. He was a blackmailer with a press pass. The Baron had exposed him. The article was his last attempt to apply pressure."
            },
            "clues_i_hold": ["article_draft", "informant_letter"],
            "starting_knowledge": {
                "de": "Du weißt: Der Mord war geplant. Er war nicht spontan. Dein Informant nannte dir eine Zeit — kurz vor Mitternacht. Und einen Ort — die Bibliothek.",
                "en": "You know: the murder was planned. It was not spontaneous. Your informant told you a time — just before midnight. And a place — the library."
            }
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # HINWEISE (Clues)
    # ─────────────────────────────────────────────────────────────────────────
    "clues": {
        "key_cellar": {
            "name": {"de": "Schlüssel zum Weinkeller", "en": "Wine Cellar Key"},
            "text": {"de": "Ein alter Messing-Schlüssel. Auf der Rückseite eingraviert: 'W-7'. Der Weinkeller — aber warum wäre das wichtig?", "en": "An old brass key. Engraved on the back: 'W-7'. The wine cellar — but why would that matter?"},
            "unlocks": ["wine_cellar_content"],
            "trigger": "butler_uses_ability"
        },
        "household_ledger": {
            "name": {"de": "Das Haushaltsbuch", "en": "The Household Ledger"},
            "text": {"de": "Seite 47 zeigt Abweichungen. Jemand hat Zahlen korrigiert — mit einer anderen Tinte. Die Korrekturen summieren sich auf 8.400 Mark über drei Jahre.", "en": "Page 47 shows discrepancies. Someone has corrected numbers — with different ink. The corrections add up to 8,400 marks over three years."},
            "unlocks": ["butler_motive_confirmed"],
            "trigger": "witness_finds_library"
        },
        "sealed_letter": {
            "name": {"de": "Der versiegelte Brief (Constanze)", "en": "The Sealed Letter (Constanze)"},
            "text": {"de": "Liebe Constanze, wenn du dies liest bin ich tot. Die Wahrheit über deine Mutter — und über mich — liegt in der Bibliothek. Drittes Regal, hinter Schiller. Verbrenne es nicht. —Aldric", "en": "Dear Constanze, if you read this I am dead. The truth about your mother — and about me — is in the library. Third shelf, behind Schiller. Do not burn it. —Aldric"},
            "unlocks": ["library_schiller", "constanze_real_heritage"],
            "trigger": "niece_opens_letter"
        },
        "cause_of_death": {
            "name": {"de": "Todesursache (Dr. Voss)", "en": "Cause of Death (Dr. Voss)"},
            "text": {"de": "Herzversagen — aber die Pupillen sind erweitert. Das ist nicht typisch. Entweder starke Aufregung oder... Digitalis. In zu hoher Dosis. Das Herzmedikament des Barons selbst.", "en": "Heart failure — but the pupils are dilated. That's not typical. Either strong agitation or... Digitalis. In too high a dose. The Baron's own heart medication."},
            "unlocks": ["digitalis_source", "medication_bottle"],
            "trigger": "doctor_examines_body"
        },
        "kitchen_substance": {
            "name": {"de": "Das Küchenpäckchen", "en": "The Kitchen Package"},
            "text": {"de": "Ein kleines Päckchen weißes Pulver. Geruchlos. Die Köchin sagt: 'Es war Herzstärkendes. So wurde es mir gesagt.' Der Arzt wird das anders sehen.", "en": "A small package of white powder. Odourless. The cook says: 'It was a heart tonic. That's what I was told.' The doctor will see it differently."},
            "unlocks": ["digitalis_confirmed", "cook_payment"],
            "trigger": "cook_reveals_truth"
        },
        "payment_receipt": {
            "name": {"de": "Die Quittung", "en": "The Receipt"},
            "text": {"de": "200 Mark. Kein Name. Datum: Heute. Ausgestellt in einer Gasthausschrift die nach München riecht.", "en": "200 marks. No name. Date: today. Written in an inn handwriting that smells of Munich."},
            "unlocks": ["who_paid_cook"],
            "trigger": "cook_found_with_money"
        },
        "surveillance_file": {
            "name": {"de": "Die Observationsakte", "en": "The Surveillance File"},
            "text": {"de": "12 Seiten über eine Person am Tisch. Zeiten, Orte, Kontakte. Darunter ein Name der immer wieder auftaucht — ein Name den niemand sonst kennt.", "en": "12 pages on one person at the table. Times, places, contacts. Including a name that appears repeatedly — a name nobody else knows."},
            "unlocks": ["stranger_target_revealed"],
            "trigger": "stranger_chooses_to_reveal"
        },
        "baron_letter": {
            "name": {"de": "Der Brief des Barons (Inspektor)", "en": "The Baron's Letter (Inspector)"},
            "text": {"de": "Auf dem Briefkopf des Barons: 'Ich fürchte [ROLLE]. Sie wissen zu viel. Wenn mir etwas passiert — Bibliothek, unter dem Teppich, dritte Bodendiele.' Datum: Gestern.", "en": "On the Baron's letterhead: 'I fear [ROLE]. They know too much. If something happens to me — library, under the carpet, third floorboard.' Date: yesterday."},
            "unlocks": ["library_floorboard"],
            "trigger": "inspector_arrives",
            "dynamic": True,
            "dynamic_field": "feared_person"
        },
        "telegram_copy": {
            "name": {"de": "Telegramm-Kopie", "en": "Telegram Copy"},
            "text": {"de": "HEUTE NACHT WIRD ALLES ENDEN STOP ICH HABE ALLES STOP DU WEISST WAS ZU TUN IST STOP — KEIN ABSENDER", "en": "TONIGHT EVERYTHING ENDS STOP I HAVE EVERYTHING STOP YOU KNOW WHAT TO DO STOP — NO SENDER"},
            "unlocks": ["telegram_sender_investigation"],
            "trigger": "stranger_investigates_study"
        },
        "medical_bag": {
            "name": {"de": "Die Arzttasche", "en": "The Doctor's Bag"},
            "text": {"de": "Standard-Ausrüstung — aber eine Spritze fehlt. Die Schachtel Digitalis ist offen. Zwei Tabletten fehlen. Das ist seltsam für einen Arzt der nur zum Dinner eingeladen war.", "en": "Standard equipment — but one syringe is missing. The box of digitalis is open. Two tablets are missing. That's odd for a doctor only invited to dinner."},
            "unlocks": ["doctor_motive_hint"],
            "trigger": "detective_examines_bag"
        },
        "wine_cellar_content": {
            "name": {"de": "Inhalt des Weinkellers", "en": "Wine Cellar Contents"},
            "text": {"de": "Hinter Reihe W-7: Ein Tresor. Darin ein Umschlag beschriftet mit 'Für den Fall meines Todes'. Und ein zweites Testament. Handgeschrieben. Heute datiert. Noch nicht unterschrieben.", "en": "Behind row W-7: a safe. Inside an envelope labelled 'In case of my death'. And a second will. Handwritten. Dated today. Not yet signed."},
            "unlocks": ["unsigned_will_found", "shadow_alert"],
            "trigger": "key_used_in_cellar"
        },
        "library_schiller": {
            "name": {"de": "Hinter dem Schiller", "en": "Behind the Schiller"},
            "text": {"de": "Ein Foto. Der Baron mit einer Frau — Constanzes Mutter. Und ein Kind das nicht Constanze ist. Ein Kind das jemand anderes am Tisch sein könnte.", "en": "A photograph. The Baron with a woman — Constanze's mother. And a child that is not Constanze. A child that could be someone else at the table."},
            "unlocks": ["barons_secret_child", "real_heir_revealed"],
            "trigger": "niece_finds_clue"
        },
        "blackmail_files": {
            "name": {"de": "Die Erpressungsakten (Schatten)", "en": "The Blackmail Files (Shadow)"},
            "text": {"de": "Drei Dossiers. Drei Personen. Drei Geheimnisse. Jede Information allein wäre vernichtend — zusammen ist es ein Mosaik das auf den Mörder zeigt.", "en": "Three dossiers. Three people. Three secrets. Each piece of information alone would be damning — together it's a mosaic that points to the murderer."},
            "unlocks": ["shadow_knows_murderer"],
            "trigger": "shadow_observes_long_enough",
            "private_to_shadow": True
        },
        "barons_journal": {
            "name": {"de": "Das geheime Tagebuch des Barons", "en": "The Baron's Secret Journal"},
            "text": {"de": "Letzte Eintragung: 'Heute Abend werde ich alles klären. Ich werde [NAME] konfrontieren. Wenn ich recht habe — und ich habe recht — dann ist mein Leben in Gefahr. Eleonore weiß was zu tun ist.'", "en": "Last entry: 'Tonight I will settle everything. I will confront [NAME]. If I am right — and I am right — then my life is in danger. Eleonore knows what to do.'"},
            "unlocks": ["baron_knew_murderer"],
            "trigger": "medium_shares_message",
            "dynamic": True,
            "dynamic_field": "feared_person"
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # REAL-WELT AUFGABEN (Physical Tasks)
    # ─────────────────────────────────────────────────────────────────────────
    "physical_tasks": {

        "task_bathroom": {
            "id": "task_bathroom",
            "trigger_phase": 1,
            "trigger_condition": "game_started_5min",
            "assigned_to": "random_non_murderer",
            "instruction": {
                "de": "🚶 GEHEIMAUFTRAG: Geh jetzt ins Badezimmer — allein. Schau hinter dem Spiegel nach (oder unter dem Waschbecken, wo der Host vorher etwas versteckt hat). Du findest dort etwas. Bring es mit. Zeig es NIEMANDEM sofort. Wenn jemand fragt wo du warst: Du hast dein Telefon geladen.",
                "en": "🚶 SECRET MISSION: Go to the bathroom now — alone. Look behind the mirror (or under the sink, where the host hid something earlier). You'll find something there. Bring it. Show it to NOBODY immediately. If asked where you were: you were charging your phone."
            },
            "what_they_find": {
                "de": "Ein gefaltetes Papier mit: 'Der Baron sagte mir: Wer auch immer nach meinem Tod ZUERST nach meiner Bibliothek fragt — der hat etwas zu verbergen.'",
                "en": "A folded piece of paper: 'The Baron told me: Whoever is FIRST to ask about my library after my death — has something to hide.'"
            },
            "game_effect": "library_first_asker_flagged"
        },

        "task_drinking": {
            "id": "task_drinking",
            "trigger_phase": 1,
            "trigger_condition": "first_10_minutes",
            "assigned_to": "witness",
            "instruction": {
                "de": "🍷 ERINNERUNGSAUFTRAG: Trinke innerhalb der nächsten 3 Minuten dreimal von deinem Glas. Beim DRITTEN Schluck schaust du der Person direkt gegenüber in die Augen — ohne wegzusehen — für 5 Sekunden. Was siehst du? Das schärft deine Erinnerung an die Nacht.",
                "en": "🍷 MEMORY TASK: Drink from your glass three times in the next 3 minutes. On the THIRD sip, look directly into the eyes of the person across from you — without looking away — for 5 seconds. What do you see? This sharpens your memory of the night."
            },
            "game_effect": "witness_receives_vision_clue",
            "clue_revealed": {
                "de": "Deine Erinnerung schärft sich: Die Silhouette die du saHst — sie trug etwas. In der rechten Hand. Etwas Langes, Dünnes. Eine Spritze? Ein Messer? Ein Schlüssel?",
                "en": "Your memory sharpens: the silhouette you saw — they were carrying something. In the right hand. Something long, thin. A syringe? A knife? A key?"
            }
        },

        "task_whisper": {
            "id": "task_whisper",
            "trigger_phase": 1,
            "trigger_condition": "random_15min",
            "assigned_to": "random",
            "instruction": {
                "de": "🗣️ FLÜSTERAUFTRAG: Lehne dich unauffällig zur Person links von dir und flüstere ihr ins Ohr: 'Der Baron hatte einen Feind den niemand kannte.' Sag nicht von wem das kommt. Beobachte ihre Reaktion genau.",
                "en": "🗣️ WHISPER TASK: Casually lean toward the person to your left and whisper: 'The Baron had an enemy nobody knew about.' Don't say where it comes from. Watch their reaction carefully."
            },
            "game_effect": "reaction_logged_for_murderer_check"
        },

        "task_glass": {
            "id": "task_glass",
            "trigger_phase": 2,
            "trigger_condition": "body_discovered_plus_5min",
            "assigned_to": "doctor",
            "instruction": {
                "de": "🥃 ARZT-AUFGABE: Geh zur Tischseite wo das Glas des Barons stand. Hebe es auf (es liegt jetzt auf dem Boden oder wurde umgestellt). Rieche daran. Du weißt was du riechst. Du weißt es sehr gut. Verkünde NUR wenn du bereit bist was du riechst — aber noch nicht die Bedeutung.",
                "en": "🥃 DOCTOR'S TASK: Go to the table side where the Baron's glass stood. Pick it up (it's now on the floor or was moved). Smell it. You know what you smell. You know it very well. Only announce when you're ready what you smell — but not yet the significance."
            },
            "game_effect": "glass_smell_clue_revealed"
        },

        "task_stand_window": {
            "id": "task_stand_window",
            "trigger_phase": 2,
            "trigger_condition": "investigation_begins",
            "assigned_to": "stranger",
            "instruction": {
                "de": "👁️ OBSERVATIONSAUFGABE: Steh auf und geh zum Fenster. Schau 30 Sekunden hinaus — ohne zu reden. Danach sagst du laut: 'Jemand war draußen.' Und setzt dich. Kein weiteres Wort dazu.",
                "en": "👁️ OBSERVATION TASK: Stand up and go to the window. Look outside for 30 seconds — without speaking. Then say out loud: 'Someone was outside.' And sit down. No further word about it."
            },
            "game_effect": "outdoor_presence_revealed",
            "note": "This is theatric — but it will make the murderer very nervous if they used the garden."
        },

        "task_note_suspect": {
            "id": "task_note_suspect",
            "trigger_phase": 3,
            "trigger_condition": "midgame",
            "assigned_to": "all",
            "instruction": {
                "de": "📝 GEHEIMABSTIMMUNG: Alle schreiben jetzt auf einen Zettel den Namen der Person die sie am meisten verdächtigen. Faltet den Zettel. Gebt ihn dem Host. Noch kein Ergebnis — aber der Host sieht ob der Mörder nervös wird wenn er den eigenen Namen sieht.",
                "en": "📝 SECRET VOTE: Everyone now writes on a piece of paper the name of the person they most suspect. Fold it. Give it to the host. No result yet — but the host can see if the murderer gets nervous seeing their own name."
            },
            "game_effect": "mid_game_suspicion_snapshot",
            "note": "Host reads privately, does not reveal results yet. This is information for the host only."
        },

        "task_knock": {
            "id": "task_knock",
            "trigger_phase": 2,
            "trigger_condition": "random_after_murder",
            "assigned_to": "shadow",
            "instruction": {
                "de": "✊ SIGNAL: Klopfe dreimal auf den Tisch. Warte. Wenn jemand zurückklopft — auch dreimal — ist das dein stiller Verbündeter. Wenn niemand zurückklopft in 10 Sekunden: Du bist allein.",
                "en": "✊ SIGNAL: Knock three times on the table. Wait. If someone knocks back — also three times — they are your silent ally. If nobody knocks back in 10 seconds: you are alone."
            },
            "game_effect": "shadow_ally_possibly_revealed",
            "note": "No ally exists — this is a test. If someone DOES knock back (by chance), it creates massive suspicion on them."
        },

        "task_empty_glass": {
            "id": "task_empty_glass",
            "trigger_phase": 3,
            "trigger_condition": "investigation_midpoint",
            "assigned_to": "detective",
            "instruction": {
                "de": "🔍 DETEKTIV-SIGNAL: Stelle dein Glas auffällig leer auf den Tisch wenn du glaubst den Mörder zu kennen. Dies ist ein Signal an alle dass du kurz vor einer Enthüllung bist. Der Mörder weiß dann dass du heiß bist — und wird reagieren. Beobachte die Reaktionen.",
                "en": "🔍 DETECTIVE SIGNAL: Place your glass conspicuously empty on the table when you believe you know the murderer. This signals to everyone you're close to a revelation. The murderer will know you're hot — and will react. Observe the reactions."
            },
            "game_effect": "murderer_alert_triggered"
        },

        "task_confession_moment": {
            "id": "task_confession_moment",
            "trigger_phase": 3,
            "trigger_condition": "cook_under_pressure",
            "assigned_to": "cook",
            "instruction": {
                "de": "😰 DER MOMENT DER WAHRHEIT: Du bist unter Druck. Alle schauen dich an. Trinke jetzt langsam von deinem Glas — einen langen Schluck. Wenn du willst dass jemand mit dir redet, stelle dein Glas ab UND legst die Hände flach auf den Tisch. Das ist ein Zeichen dass du reden willst — aber nur mit einer Person.",
                "en": "😰 MOMENT OF TRUTH: You're under pressure. Everyone is watching. Drink slowly from your glass now — one long sip. If you want someone to talk to you, set your glass down AND place your hands flat on the table. That's a signal you want to talk — but to only one person."
            },
            "game_effect": "cook_confession_available"
        },

        "task_cold_reading": {
            "id": "task_cold_reading",
            "trigger_phase": 2,
            "trigger_condition": "medium_activated",
            "assigned_to": "medium",
            "instruction": {
                "de": "🕯️ DIE BOTSCHAFT: Schließe kurz die Augen. 5 Sekunden. Dann öffne sie und schau langsam jeden am Tisch an. Sag: 'Ich höre ihn. Er sagt — jemand hier hat etwas in der Tasche das ihm gehörte.' Das ist wahr. Einer der Spieler hat tatsächlich einen Gegenstand des Barons. Wer das ist — weißt du nicht. Aber sie wissen es.",
                "en": "🕯️ THE MESSAGE: Close your eyes briefly. 5 seconds. Then open them and look at everyone at the table slowly. Say: 'I hear him. He says — someone here has something in their pocket that belonged to him.' This is true. One player actually has an object of the Baron's. Who — you don't know. But they do."
            },
            "game_effect": "medium_clue_delivered"
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # SPIELPHASEN
    # ─────────────────────────────────────────────────────────────────────────
    "phases": {
        0: {
            "name": {"de": "Ankunft & Vorstellung", "en": "Arrival & Introduction"},
            "duration_hint": {"de": "20–30 Minuten", "en": "20–30 minutes"},
            "description": {
                "de": "Jeder stellt seinen Charakter vor. Lest eure Intro-Texte laut vor. Danach: 10 Minuten freies Gespräch — bleibt in der Rolle. In dieser Phase passiert schon etwas: Der Mörder erhält um Minute 10 seine geheime Nachricht.",
                "en": "Everyone introduces their character. Read your intro texts aloud. Then: 10 minutes of free conversation — stay in character. In this phase something already happens: the murderer receives their secret message at minute 10."
            },
            "murderer_message": {
                "de": "⚠️ DU BIST DER MÖRDER. Du hast den Baron getötet. Dein Motiv steht in deiner Rollenakte. Deine Methode: {method}. Du weißt das seit Stunden — du musstest heute Abend nur noch warten. Verhalte dich normal. Du hast die Nacht überlebt. Jetzt musst du auch das Spiel überleben.",
                "en": "⚠️ YOU ARE THE MURDERER. You killed the Baron. Your motive is in your role file. Your method: {method}. You've known this for hours — you only had to wait until tonight. Behave normally. You survived the night. Now you must survive the game."
            },
            "host_note": {
                "de": "Wenn alle vorgestellt sind: Sag 'Der Baron bittet zu Tisch.' Startet das Dinner. Echtes Essen/Trinken ist jetzt Teil des Spiels.",
                "en": "When all have been introduced: say 'The Baron invites you to table.' The dinner begins. Real eating/drinking is now part of the game."
            }
        },
        1: {
            "name": {"de": "Das Dinner", "en": "The Dinner"},
            "duration_hint": {"de": "20–30 Minuten", "en": "20–30 minutes"},
            "description": {
                "de": "Freies Rollenspiel am Tisch. Der Host spielt den Baron (oder eine NPC-Rolle). Aufgaben beginnen zu erscheinen. Geheimnisse werden angedeutet. Noch ist niemand tot.",
                "en": "Free roleplay at the table. The host plays the Baron (or an NPC role). Tasks begin to appear. Secrets are hinted at. Nobody is dead yet."
            },
            "host_note": {
                "de": "Als Baron: Sage beim Dinner zu jeder Person etwas Bedeutungsvolles. Sag dem Arzt: 'Danke für alles, Heinrich. Ich hoffe wir sehen uns bald — unter besseren Umständen.' Sag dem Butler: 'Edmund. Wir müssen reden. Später.' Sag der Nichte: 'Constanze. Du weißt dass ich dich liebe.' Dann: Verlasse unauffällig den Raum. 3 Minuten später: Schrei (oder lass schreien). Der Baron wurde gefunden.",
                "en": "As Baron: say something meaningful to each person at dinner. Tell the doctor: 'Thank you for everything, Heinrich. I hope we see each other soon — under better circumstances.' Tell the butler: 'Edmund. We need to talk. Later.' Tell the niece: 'Constanze. You know I love you.' Then: Leave the room inconspicuously. 3 minutes later: scream (or have someone scream). The Baron has been found."
            }
        },
        2: {
            "name": {"de": "Der Mord", "en": "The Murder"},
            "duration_hint": {"de": "5–10 Minuten", "en": "5–10 minutes"},
            "description": {
                "de": "Der Schrei. Jemand hat den Baron gefunden. In der Bibliothek. Tot. Ab jetzt ist niemand mehr ein Gast — alle sind Verdächtige.",
                "en": "The scream. Someone found the Baron. In the library. Dead. From this moment nobody is a guest — everyone is a suspect."
            },
            "announcement": {
                "de": "🔔 DER BARON WURDE GEFUNDEN. Todeszeit: Kurz vor Mitternacht. Ort: Die Bibliothek. Niemand verlässt das Haus. Die Ermittlung beginnt.",
                "en": "🔔 THE BARON HAS BEEN FOUND. Time of death: just before midnight. Location: the library. Nobody leaves the house. The investigation begins."
            },
            "immediate_tasks": ["task_stand_window", "task_glass"],
            "witness_trigger": True
        },
        3: {
            "name": {"de": "Die Ermittlung", "en": "The Investigation"},
            "duration_hint": {"de": "40–50 Minuten", "en": "40–50 minutes"},
            "description": {
                "de": "Hinweise werden gefunden. Rollen interagieren. Geheimnisse kommen ans Licht. Vier Runden: Jede Runde wird durch ein Ereignis ausgelöst das die App ankündigt.",
                "en": "Clues are found. Roles interact. Secrets come to light. Four rounds: each round triggered by an event the app announces."
            },
            "rounds": {
                "A": {
                    "name": {"de": "Runde A: Erste Verdächtigungen", "en": "Round A: First Suspicions"},
                    "trigger": "phase_3_start",
                    "events": ["doctor_examines", "butler_questioned", "witness_speaks"],
                    "app_message": {
                        "de": "🔍 ERMITTLUNG BEGINNT. Jeder hat jetzt 10 Minuten um Hinweise zu suchen, Fragen zu stellen und Verdächtigungen auszusprechen. In dieser Zeit werden die ersten Hinweise enthüllt.",
                        "en": "🔍 INVESTIGATION BEGINS. Everyone now has 10 minutes to search for clues, ask questions and voice suspicions. In this time the first clues will be revealed."
                    }
                },
                "B": {
                    "name": {"de": "Runde B: Das Geheimnis der Küche", "en": "Round B: The Kitchen Secret"},
                    "trigger": "after_round_A",
                    "events": ["cook_pressured", "payment_found", "stranger_observes"],
                    "app_message": {
                        "de": "🍴 NEUE INFORMATION: In der Küche wurde etwas gefunden. Die Köchin wird befragt.",
                        "en": "🍴 NEW INFORMATION: Something was found in the kitchen. The cook is being questioned."
                    }
                },
                "C": {
                    "name": {"de": "Runde C: Das Testament", "en": "Round C: The Will"},
                    "trigger": "after_round_B",
                    "events": ["will_location_hinted", "cellar_key_used", "shadow_acts"],
                    "app_message": {
                        "de": "📜 DER ANWALT WARTET. Jemand hat einen Anwalt dabei. Das Testament — welches gilt? Das alte oder das neue?",
                        "en": "📜 THE LAWYER WAITS. Someone brought a lawyer. The will — which counts? The old or the new?"
                    }
                },
                "D": {
                    "name": {"de": "Runde D: Alles kommt ans Licht", "en": "Round D: Everything Comes to Light"},
                    "trigger": "after_round_C",
                    "events": ["medium_reveals", "detective_interrogates", "affair_revealed"],
                    "app_message": {
                        "de": "⚡ LETZTE CHANCE. Alle Karten liegen bald auf dem Tisch. Wer schweigt verliert seine Chance.",
                        "en": "⚡ LAST CHANCE. All cards will soon be on the table. Whoever remains silent loses their chance."
                    }
                }
            }
        },
        4: {
            "name": {"de": "Die Abrechnung", "en": "The Reckoning"},
            "duration_hint": {"de": "10–15 Minuten", "en": "10–15 minutes"},
            "description": {
                "de": "Letzte Anschuldigungen. Jeder hat 60 Sekunden um seine Theorie zu präsentieren. Dann: Die Abstimmung. Dann: Die Enthüllung.",
                "en": "Final accusations. Everyone has 60 seconds to present their theory. Then: the vote. Then: the revelation."
            },
            "accusation_order": "clockwise",
            "vote_mechanic": {
                "de": "Jeder wählt einen Namen in der App. Mehrheit entscheidet. Bei Gleichstand: Der Inspektor hat die Stichstimme.",
                "en": "Everyone votes a name in the app. Majority decides. In case of tie: the inspector has the casting vote."
            }
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # ENDE-SZENARIEN
    # ─────────────────────────────────────────────────────────────────────────
    "endings": {
        "murderer_caught": {
            "condition": "majority_votes_murderer_correctly",
            "title": {"de": "Gerechtigkeit", "en": "Justice"},
            "text": {
                "de": "Der Mörder wurde gefasst. {murderer_name} gestand — oder wurde durch Beweise überführt. Das Herrenhaus Dunkelbach wird nie wieder dasselbe sein. Aber Gerechtigkeit hat gesiegt.\n\nWer gewann:\n• Alle Überlebenden die für den richtigen Mörder stimmten\n• Der Inspektor (falls er als erster anklagte)\n• Die Zeugin (falls ihre Vision sich bewahrheitete)",
                "en": "The murderer was caught. {murderer_name} confessed — or was convicted by evidence. Dunkelbach Manor will never be the same. But justice prevailed.\n\nWho won:\n• All survivors who voted for the right murderer\n• The inspector (if they accused first)\n• The witness (if their vision proved true)"
            }
        },
        "murderer_escapes": {
            "condition": "majority_votes_wrong_person",
            "title": {"de": "Der Mörder entkommt", "en": "The Murderer Escapes"},
            "text": {
                "de": "Ein Unschuldiger wurde verurteilt. Der wahre Mörder sitzt unter euch — und lacht. {murderer_name} hat gewonnen. Das Herrenhaus Dunkelbach hat sein erstes Opfer gefunden.\n\nDer Mörder offenbart sich jetzt selbst.",
                "en": "An innocent was convicted. The real murderer sits among you — and laughs. {murderer_name} has won. Dunkelbach Manor has claimed its first victim.\n\nThe murderer now reveals themselves."
            }
        },
        "shadow_wins": {
            "condition": "shadow_steals_will_undiscovered",
            "title": {"de": "Der Dieb im Dunkeln", "en": "The Thief in the Dark"},
            "text": {
                "de": "Während alle sich gegenseitig beschuldigten — verschwand das Testament. Die Schattenfigur hat gewonnen. Wer erbt jetzt was? Niemand weiß es. Das Spiel geht weiter — ohne Testament.\n\nDie Ermittlung muss ohne dieses Dokument abgeschlossen werden.",
                "en": "While everyone accused each other — the will disappeared. The Shadow figure has won. Who inherits what now? Nobody knows. The game continues — without a will.\n\nThe investigation must be concluded without this document."
            }
        },
        "perfect_solve": {
            "condition": "witness_and_doctor_both_correct",
            "title": {"de": "Die Vollendete Lösung", "en": "The Perfect Solve"},
            "text": {
                "de": "Die Zeugin sah die Wahrheit. Der Arzt bestätigte sie. Gemeinsam haben sie das Unmögliche getan — den Mörder mit lückenlosem Beweis überführt. Das ist selten. Das ist brillant.",
                "en": "The witness saw the truth. The doctor confirmed it. Together they did the impossible — convicted the murderer with complete evidence. This is rare. This is brilliant."
            }
        },
        "two_murderers": {
            "condition": "random_chance_8_plus_players",
            "title": {"de": "Zwei Mörder", "en": "Two Murderers"},
            "description": {
                "de": "Bei 8+ Spielern: 20% Chance dass zwei Personen unabhängig voneinander den Baron töten wollten. Nur einer war schneller. Der zweite weiß das — und muss verhindern dass der erste entdeckt wird, da sonst auch sein Plan auffliegt.",
                "en": "With 8+ players: 20% chance that two people independently wanted to kill the Baron. Only one was faster. The second knows this — and must prevent the first from being discovered, as their own plan would also be revealed."
            }
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # EREIGNIS-KETTEN (Event Chains)
    # ─────────────────────────────────────────────────────────────────────────
    "event_chains": [
        {
            "id": "chain_suspicion_pair",
            "trigger": "two_players_talk_privately_3min",
            "message_to_third": {
                "de": "👁️ Du hast bemerkt: {player_a} und {player_b} flüstern seit Minuten. Das ist verdächtig. Du kannst alle aufrufen und es ansprechen — oder sie weiter beobachten.",
                "en": "👁️ You noticed: {player_a} and {player_b} have been whispering for minutes. This is suspicious. You can call everyone's attention to it — or keep observing."
            },
            "assigned_to": "random_suspicious_role"
        },
        {
            "id": "chain_wine_drinker",
            "trigger": "player_drinks_third_time",
            "message_to_observer": {
                "de": "🍷 {player} trinkt ungewöhnlich viel — und gerade jetzt, wo sie/er etwas Wichtiges erzählt. Wein löst Zungen — aber auch Gewissen. Rede mit ihr/ihm.",
                "en": "🍷 {player} is drinking unusually much — and right now while saying something important. Wine loosens tongues — and consciences. Talk to them."
            },
            "assigned_to": "person_who_was_told_to_watch_drinker"
        },
        {
            "id": "chain_confrontation",
            "trigger": "suspicion_meter_high",
            "message_to_suspicious": {
                "de": "⚠️ WARNUNG: Du wirst verdächtigt. Mindestens zwei Personen am Tisch sprechen gerade über dich. Du kannst jetzt proaktiv handeln — bevor sie anklagen.",
                "en": "⚠️ WARNING: You are being suspected. At least two people at the table are talking about you right now. You can act proactively — before they accuse."
            }
        },
        {
            "id": "chain_lover_revelation",
            "trigger": "viktor_under_pressure",
            "message_to_lover": {
                "de": "💌 Viktor braucht dich. Er steht kurz davor verdächtigt zu werden. Wenn du jetzt nichts tust — fällt er. Und mit ihm du. Die App wartet auf deine Entscheidung: Deckst du ihn?",
                "en": "💌 Viktor needs you. He's about to be accused. If you do nothing — he falls. And with him, you. The app awaits your decision: do you cover for him?"
            },
            "assigned_to": "viktor_secret_lover",
            "choice": {
                "confirm_alibi": {
                    "de": "Ja, ich bestätige das Alibi",
                    "en": "Yes, I confirm the alibi"
                },
                "deny_alibi": {
                    "de": "Nein, ich sage nichts",
                    "en": "No, I say nothing"
                }
            }
        },
        {
            "id": "chain_medium_timing",
            "trigger": "medium_observes_30min",
            "message_to_medium": {
                "de": "🕯️ Jetzt ist dein Moment. Der Raum ist ruhig genug. Deine Botschaft wird Eindruck machen. Nutze deine Fähigkeit — aber wähle den Moment weise.",
                "en": "🕯️ Now is your moment. The room is quiet enough. Your message will make an impression. Use your ability — but choose the moment wisely."
            }
        },
        {
            "id": "chain_shadow_discovered",
            "trigger": "shadow_acts",
            "message_to_random": {
                "de": "🌑 Du hast gerade bemerkt: Eine Person am Tisch schaut auffällig oft zur Tür — als würde sie auf eine Möglichkeit warten. Warum?",
                "en": "🌑 You just noticed: one person at the table is looking conspicuously often toward the door — as if waiting for an opportunity. Why?"
            }
        }
    ],

    # ─────────────────────────────────────────────────────────────────────────
    # ATMOSPHÄREN-NACHRICHTEN (broadcast to all at key moments)
    # ─────────────────────────────────────────────────────────────────────────
    "atmosphere_messages": [
        {
            "trigger_time_min": 5,
            "phase": 1,
            "text": {"de": "🌧️ Draußen beginnt es zu regnen. Der Regen trommelt gegen die Fenster des Herrenhauses. Niemand kann jetzt gehen.", "en": "🌧️ Outside it begins to rain. Rain drums against the manor windows. Nobody can leave now."}
        },
        {
            "trigger_time_min": 15,
            "phase": 1,
            "text": {"de": "🕙 Die Uhr schlägt 22 Uhr. Der Baron klopft mit seinem Glas auf den Tisch: 'Ich habe eine Ankündigung zu machen. Aber zuerst — trinken wir.'", "en": "🕙 The clock strikes 10pm. The Baron taps his glass: 'I have an announcement to make. But first — let us drink.'"}
        },
        {
            "trigger": "phase_2_start",
            "text": {"de": "💀 DER SCHREI. Aus der Bibliothek. Jemand hat etwas gefunden. Der Baron von Dunkelbach ist tot.", "en": "💀 THE SCREAM. From the library. Someone found something. Baron von Dunkelbach is dead."}
        },
        {
            "trigger": "round_B_start",
            "text": {"de": "🍴 Ein Geruch aus der Küche. Süßlich. Fast medizinisch. Was war das?", "en": "🍴 A smell from the kitchen. Sweet. Almost medicinal. What was that?"}
        },
        {
            "trigger": "round_C_start",
            "text": {"de": "📜 Ein Anwalt wartet draußen. Jemand hat ihn mitgebracht. Warum jetzt?", "en": "📜 A lawyer waits outside. Someone brought him. Why now?"}
        },
        {
            "trigger": "10min_before_reckoning",
            "text": {"de": "⚡ Die Stunde der Wahrheit naht. Wer schweigt verliert. Wer lügt wird entlarvt. Wer die Wahrheit sagt — überlebt vielleicht.", "en": "⚡ The hour of truth approaches. Those who remain silent lose. Those who lie will be exposed. Those who tell the truth — may survive."}
        }
    ],

    # ─────────────────────────────────────────────────────────────────────────
    # HOST-OBJEKTE (Dinge die der Host vorbereiten muss)
    # ─────────────────────────────────────────────────────────────────────────
    "host_objects": [
        {
            "object": "hidden_note",
            "instruction": {"de": "Falte einen Zettel mit folgendem Text und verstecke ihn im Badezimmer (hinter dem Spiegel oder unter dem Waschbecken): 'Der Baron sagte mir: Wer auch immer nach meinem Tod ZUERST nach meiner Bibliothek fragt — der hat etwas zu verbergen.'", "en": "Fold a note with the following text and hide it in the bathroom (behind the mirror or under the sink): 'The Baron told me: whoever is FIRST to ask about my library after my death — has something to hide.'"}
        },
        {
            "object": "barons_glass",
            "instruction": {"de": "Stelle ein besonderes Weinglas bereit — das 'Glas des Barons'. Es muss sich optisch von den anderen unterscheiden. Wenn der Baron stirbt: Stelle es auf den Boden neben dem Stuhl.", "en": "Prepare a special wine glass — the 'Baron's glass'. It must look different from the others. When the Baron dies: place it on the floor beside the chair."}
        },
        {
            "object": "sealed_envelope",
            "instruction": {"de": "Gib der Spielerin die die Nichte spielt einen echten versiegelten Brief. Inhalt: 'Liebe Constanze, wenn du dies liest bin ich tot. Die Wahrheit über deine Mutter liegt in der Bibliothek — drittes Regal, hinter Schiller. Verbrenne es nicht. — Aldric'", "en": "Give the player playing the niece a real sealed envelope. Contents: 'Dear Constanze, if you read this I am dead. The truth about your mother is in the library — third shelf, behind Schiller. Do not burn it. — Aldric'"}
        },
        {
            "object": "schiller_clue",
            "instruction": {"de": "Stelle ein Buch von Schiller sichtbar irgendwo auf. Verstecke darin ein Foto (jedes alte Foto reicht) mit der Notiz auf der Rückseite: 'Blut ist dicker als Versprechen. — A.'", "en": "Place a book by Schiller somewhere visible. Hide inside it a photo (any old photo works) with a note on the back: 'Blood is thicker than promises. — A.'"}
        }
    ]
}
