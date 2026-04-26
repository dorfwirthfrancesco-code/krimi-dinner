# KRIMI DINNER — SZENARIO 04
# "Der finale Pitch"
# Berlin, 2024 — Ein KI-Startup. Eine Funding-Party. Ein toter CEO.
#
# STATS v1.0:
# - 11 Rollen
# - 62 physische Aufgaben
#   * 8 Moerder-Tasks (privat)
#   * 10 Trink-Tasks
#   * 12 Ketten-Tasks
#   * 9 Zufalls-Momente
#   * 23 Standard-Aufgaben
# - 35 Hinweise in 8 Ketten
# - 14 Rollenverbindungen
# - 7 Ereignisketten
# - 5 Spielenden
#
# NEUE MECHANIKEN:
# - Burner-Handy (Zettel mit 3 anonymen Nachrichten)
# - Screenshot-Beweise (Zettel im Handy-Format)
# - Social Media Post (einmal laut posten = alle hoeren es)
# - Slack-Log (ausgedruckter Chat-Verlauf als Hinweis)
# - USB-Stick (Zettel mit Originalcode)
# - Namensschilder (alle tragen Startup-Rollen-Aufkleber)

SCENARIO = {
    "id": "pitch",
    "title": "Der finale Pitch",
    "min_players": 4,
    "max_players": 11,
    "price": "4.99",
    "description": {
        "de": "Berlin, 2024. NovaTech AI feiert seine groesste Funding-Runde. 50 Millionen Euro stehen kurz vor dem Abschluss. Dann wird Magnus Frey, Gruender und CEO, tot im Serverraum gefunden. Sein Laptop ist offen. Das Pitch Deck ist weg. Auf dem Bildschirm steht: 'Ich weiss was du getan hast.' Irgendwer in diesem Raum hat geluegen — ueber die KI, ueber das Geld, und ueber den Abend.",
        "en": "Berlin, 2024. NovaTech AI celebrates its biggest funding round. 50 million euros are about to close. Then Magnus Frey, founder and CEO, is found dead in the server room. His laptop is open. The pitch deck is gone. On the screen: 'I know what you did.' Someone in this room lied — about the AI, about the money, and about the evening.",
        "fr": "Berlin, 2024. NovaTech AI celebre sa plus grande levee de fonds. 50 millions sur le point de se clore. Puis Magnus Frey est trouve mort dans la salle des serveurs.",
        "it": "Berlino, 2024. NovaTech AI festeggia il suo piu grande round. 50 milioni quasi firmati. Poi Magnus Frey viene trovato morto nella sala server.",
        "es": "Berlin, 2024. NovaTech AI celebra su mayor ronda. 50 millones a punto de cerrarse. Magnus Frey aparece muerto en la sala de servidores.",
        "pt": "Berlim, 2024. NovaTech AI celebra sua maior rodada. 50 milhoes prestes a fechar. Magnus Frey e encontrado morto na sala de servidores.",
    },
    "atmosphere": "Rooftop. Berliner Nacht. Champagner. Und irgendwo — ein Laptop der noch laeuft.",

    "host_guide": {
        "before_game": {
            "de": [
                "NAMENSSCHILDER: Jeder bekommt einen Aufkleber-Zettel als Startup-Namensschild. Rollenname + Jobtitel drauf schreiben.",
                "BURNER-HANDY: Einen Zettel (Handy-Format) mit 3 anonymen Nachrichten fuer die Hacker-Rolle: '1: Ich weiss von dir und M. | 2: Das Pitch Deck luegt. | 3: Komm allein in den Serverraum.'",
                "SCREENSHOT-BEWEISE: 5 kleine Zettel (Handy-Format) vorbereiten — jeder sieht aus wie ein Screenshot: Chat-Verlauf, Email, Kontoauszug. Texte sind in den Hinweisen beschrieben.",
                "SLACK-LOG: Einen A4-Zettel als 'Slack-Export': '#general | 21:04 Frey_Magnus: Wir muessen reden. Alle. Serverraum. Jetzt. | 21:09 Frey_Magnus: Ich weiss wer es war.' Dann nichts mehr.",
                "LAPTOP (TATORT): Einen Zettel 'LAPTOP — SERVERRAUM — GESPERRT' mit Post-it: 'Ich weiss was du getan hast.'",
                "PITCH DECK: Einen dicken Umschlag 'PITCH DECK — NOVATECH AI — VERTRAULICH' — LEER (gestohlen).",
                "USB-STICK: Einen Zettel 'USB-STICK' fuer den Ex-Mitgruender.",
                "CHAMPAGNER oder Sekt — Party-Atmosphaere, Trinken ist Spielmechanik.",
                "DAS OPFER Magnus Frey spielt NICHT mit. Kein Geist-Modus.",
            ]
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # ROLLEN (11)
    # ─────────────────────────────────────────────────────────────────────────
    "roles": {

        "investor_lead": {
            "name": {"de": "Dr. Sarah Chen, Lead-Investorin", "en": "Dr. Sarah Chen, Lead Investor",
                     "fr": "Dr. Sarah Chen, Investisseure principale", "it": "Dr. Sarah Chen, Lead Investor",
                     "es": "Dra. Sarah Chen, Inversora principal", "pt": "Dra. Sarah Chen, Investidora principal"},
            "min_players": 4,
            "can_be_murderer": True,
            "startup_role": "Managing Partner — Apex Ventures",
            "intro": {
                "de": "Sarah Chen. Managing Partner bei Apex Ventures. 47 Investments. NovaTech war mein groesstes Bet. 50 Millionen unterschrieben. Dann stirbt Magnus — und ich weiss nicht ob ich gerade die groesste Fehlinvestition meiner Karriere gemacht habe.",
                "en": "Sarah Chen. Managing Partner at Apex Ventures. 47 investments. NovaTech was my biggest bet. 50 million signed. Then Magnus dies — and I don't know if I just made the worst investment of my career.",
            },
            "appearance": {
                "de": "Perfekt gekleidet. Telefon immer in der Hand. Traegt den unterschriebenen Investitionsvertrag in ihrer Tasche. Gibt ihn nicht aus der Hand.",
                "en": "Perfectly dressed. Phone always in hand. Carries the signed investment contract in her bag. Does not let it go.",
            },
            "secret": {
                "de": "Ich habe herausgefunden dass die KI von NovaTech zu 60% auf gestohlenen Daten trainiert wurde. Ich wollte den Deal trotzdem abschliessen — mein Fonds braucht dringend einen Exit. Magnus wusste dass ich es wusste. Heute Abend wurde es sehr unangenehm zwischen uns.",
                "en": "I discovered NovaTech's AI was 60% trained on stolen data. I still wanted to close the deal — my fund urgently needs an exit. Magnus knew I knew. Tonight things got very unpleasant between us.",
            },
            "ability": {
                "name": {"de": "Der Scheck", "en": "The Check"},
                "description": {
                    "de": "Du hast den unterschriebenen Vertrag. Du entscheidest wann du ihn zeigst oder oeffentlich vernichtest. Zeigst du ihn: Alle kennen das Motiv aller Beteiligten. Vernichtest du ihn: Das Spiel aendert sich komplett.",
                    "en": "You have the signed contract. You decide when to show or publicly destroy it. Show it: everyone knows everyone's motive. Destroy it: the game changes completely.",
                }
            },
            "win_condition": {
                "de": "Ueberlebe. Der Datenbetrug darf nicht oeffentlich werden. Wenn der Moerder gefasst wird und der Datenbetrug geheim bleibt: Du gewinnst.",
                "en": "Survive. The data fraud must not become public. If the murderer is caught and the data fraud stays secret: you win.",
            },
            "murderer_motive_if_assigned": {
                "de": "Magnus wollte den Deal platzen lassen — er wollte den Datenbetrug melden. Sarah konnte 50 Millionen nicht riskieren. Sie handelte.",
                "en": "Magnus wanted to kill the deal — he wanted to report the data fraud. Sarah could not risk 50 million. She acted.",
            },
            "clues_i_hold": ["investment_contract_signed", "data_theft_report_draft"],
            "starting_knowledge": {
                "de": "Du weisst vom Datenbetrug. Du hast heute Abend mit Magnus gestritten. Der CTO weiss auch davon. Im Pitch Deck stehen Details die dich ruinieren koennen.",
                "en": "You know about the data fraud. You argued with Magnus tonight. The CTO also knows. The pitch deck contains details that could ruin you.",
            },
            "connection": {"with": "cto", "type": "both_know_fraud"}
        },

        "cofounder": {
            "name": {"de": "Leon Weber, Co-Founder & COO", "en": "Leon Weber, Co-Founder & COO",
                     "fr": "Leon Weber, Co-fondateur & COO", "it": "Leon Weber, Co-fondatore & COO",
                     "es": "Leon Weber, Co-fundador & COO", "pt": "Leon Weber, Co-fundador & COO"},
            "min_players": 4,
            "can_be_murderer": True,
            "startup_role": "Co-Founder & COO — NovaTech AI",
            "intro": {
                "de": "Leon Weber. Sechs Jahre NovaTech. Jede Nacht. Jedes Wochenende. Und heute Abend hat Magnus mir per Mail mitgeteilt dass er mich aus dem Unternehmen draengen will. Am groessten Tag unserer Geschichte.",
                "en": "Leon Weber. Six years of NovaTech. Every night. Every weekend. And tonight Magnus emailed me that he wants to push me out of the company. On the biggest day of our history.",
            },
            "appearance": {
                "de": "Erschoepft. Schaut alle 30 Sekunden aufs Telefon. Hat Magnus' Mail noch geoeeffnet. Versucht ruhig zu wirken.",
                "en": "Exhausted. Checks phone every 30 seconds. Still has Magnus' email open. Trying to appear calm.",
            },
            "secret": {
                "de": "Magnus hat mir heute Abend die Co-Founder-Partnerschaft aufgeloest. Sofortige Wirkung. Ich behalte 8% statt 45%. Nach sechs Jahren. Das kostet mich 20 Millionen. Ich habe ihm geschrieben: 'Das wirst du bereuen.' 30 Minuten spaeter war er tot.",
                "en": "Magnus dissolved our co-founder partnership tonight. Immediate effect. I keep 8% instead of 45%. After six years. That costs me 20 million. I wrote to him: 'You will regret this.' 30 minutes later he was dead.",
            },
            "ability": {
                "name": {"de": "Der interne Slack", "en": "The Internal Slack"},
                "description": {
                    "de": "Du hast Zugang zum internen Slack. Einmal kannst du einen Slack-Log vorlesen — echt oder manipuliert. Nur du weisst welches.",
                    "en": "You have access to internal Slack. Once you may read a Slack log aloud — real or manipulated. Only you know which.",
                }
            },
            "win_condition": {
                "de": "Ueberlebe ohne dass deine 'Das wirst du bereuen'-Nachricht als Morddrohung gewertet wird.",
                "en": "Survive without your 'you will regret this' message being treated as a death threat.",
            },
            "murderer_motive_if_assigned": {
                "de": "Leon toetete Magnus bevor dieser den neuen Vertrag an seinen Anwalt schicken konnte. Der Laptop musste geloescht werden. Fast erfolgreich.",
                "en": "Leon killed Magnus before he could send the new contract to his lawyer. The laptop had to be deleted. Almost successful.",
            },
            "clues_i_hold": ["partnership_dissolution_email", "slack_log_threat"],
            "starting_knowledge": {
                "de": "Du hast Magnus eine Nachricht geschrieben die wie eine Drohung klingt. Jemand kennt sie bereits. Der Journalist sucht danach. Der Serverraum hat eine Kamera — aber die Aufnahmen fehlen.",
                "en": "You wrote Magnus a message that sounds like a threat. Someone already knows it. The journalist is looking for it. The server room has a camera — but recordings are missing.",
            },
            "connection": {"with": "cto", "type": "cofounder_cto_alliance"}
        },

        "cto": {
            "name": {"de": "Mia Hoffmann, CTO", "en": "Mia Hoffmann, CTO",
                     "fr": "Mia Hoffmann, CTO", "it": "Mia Hoffmann, CTO",
                     "es": "Mia Hoffmann, CTO", "pt": "Mia Hoffmann, CTO"},
            "min_players": 4,
            "can_be_murderer": True,
            "startup_role": "Chief Technology Officer — NovaTech AI",
            "intro": {
                "de": "Mia Hoffmann. Ich habe die KI gebaut. Oder — ich habe das System gebaut auf dem sie laeuft. Was genau drin ist... ist kompliziert. Magnus hat bestimmte Entscheidungen getroffen ohne mich zu fragen.",
                "en": "Mia Hoffmann. I built the AI. Or — I built the system on which it runs. What exactly is inside... is complicated. Magnus made certain decisions without asking me.",
            },
            "appearance": {
                "de": "Schwarzer Hoodie unter allen in Businesskleidung. Haelt Laptop bei sich. Tippt auch jetzt noch. Wird nervoes wenn jemand 'Serverraum' sagt.",
                "en": "Black hoodie among everyone in business attire. Keeps laptop with her. Still typing even now. Gets nervous whenever someone says 'server room'.",
            },
            "secret": {
                "de": "Die KI von NovaTech ist keine echte KI. Es ist ein ausgefeiltes Skript das KI simuliert — mit gestohlenen Trainingsdaten. Magnus zwang mich es zu bauen. Heute Abend wollte er den Investoren die Wahrheit sagen. Ich haette alles verloren.",
                "en": "NovaTech's AI is not real AI. It is a sophisticated script simulating AI — with stolen training data. Magnus forced me to build it. Tonight he wanted to tell the investors the truth. I would have lost everything.",
            },
            "ability": {
                "name": {"de": "Die Serverlogs", "en": "The Server Logs"},
                "description": {
                    "de": "Du hast Zugang zu den Serverlogs. Einmal kannst du einen Log vorlesen der zeigt wer wann im Netzwerk war — echt oder manipuliert. Wenn jemand beweist dass du luegst: Du verlierst sofort.",
                    "en": "You have access to server logs. Once you may read a log showing who was on the network when — real or manipulated. If someone proves you're lying: you lose immediately.",
                }
            },
            "win_condition": {
                "de": "Ueberlebe ohne dass oeffentlich wird dass die KI eine Faelschung ist.",
                "en": "Survive without it becoming public that the AI is a fake.",
            },
            "murderer_motive_if_assigned": {
                "de": "Mia fand Magnus im Serverraum dabei die Wahrheit per Email an alle Investoren zu schicken. Sie handelte. Den Laptop gesperrt. Magnus hatte keine Chance mehr.",
                "en": "Mia found Magnus in the server room about to email the truth to all investors. She acted. Locked the laptop. Magnus had no more chances.",
            },
            "clues_i_hold": ["server_logs_original", "ai_fakery_code_snippet"],
            "starting_knowledge": {
                "de": "Die KI ist fake. Magnus wollte es veroeffentlichen. Die Kameraaufnahmen aus dem Serverraum — du hast sie geloescht. Oder du dachtest das.",
                "en": "The AI is fake. Magnus wanted to publish it. The camera recordings from the server room — you deleted them. Or you thought you did.",
            },
            "connection_multiple": [
                {"with": "investor_lead", "type": "both_know_fraud"},
                {"with": "cofounder", "type": "cofounder_cto_alliance"}
            ]
        },

        "designer": {
            "name": {"de": "Jess Park, UX-Designerin", "en": "Jess Park, UX Designer",
                     "fr": "Jess Park, Designer UX", "it": "Jess Park, UX Designer",
                     "es": "Jess Park, Disenadora UX", "pt": "Jess Park, Designer UX"},
            "min_players": 4,
            "can_be_murderer": False,
            "startup_role": "Senior UX Designer — NovaTech AI",
            "intro": {
                "de": "Jess Park. Ich designe die Interfaces. Ich war heute Abend die Einzige die nichts von dem Chaos wusste. Dachte ich. Bis ich um 21:43 Uhr auf Magnus' Laptop-Bildschirm etwas gesehen habe das ich nicht haette sehen sollen.",
                "en": "Jess Park. I design the interfaces. I was the only one tonight who knew nothing about all the chaos. I thought. Until at 9:43pm I saw something on Magnus' laptop screen I should not have seen.",
            },
            "appearance": {
                "de": "Kopfhoerer um den Hals. Skizzenbuch dabei. Hat ein unscharfes Foto auf ihrem Handy das sie noch niemandem gezeigt hat.",
                "en": "Headphones around her neck. Sketchbook with her. Has a blurry photo on her phone she has not shown anyone.",
            },
            "secret": {
                "de": "Ich habe um 21:43 Uhr fuer einen Bruchteil einer Sekunde Magnus' Laptop-Bildschirm gesehen. Eine offene Email. Einen Namen. Ich habe es mit meinem Handy fotografiert. Das Foto ist unscharf — aber man kann den Namen lesen wenn man weiss wonach man sucht.",
                "en": "At 9:43pm for a fraction of a second I saw Magnus' laptop screen. An open email. A name. I photographed it. The photo is blurry — but you can read the name if you know what to look for.",
            },
            "ability": {
                "name": {"de": "Der Screenshot", "en": "The Screenshot"},
                "description": {
                    "de": "Du hast ein unscharfes Foto. Du entscheidest wann du es zeigst. Wer es sieht muss raten was darauf steht. Zeigst du es zu frueh: Jemand koennte luegen was er sieht.",
                    "en": "You have a blurry photo. You decide when to show it. Whoever sees it must guess what it says. Show it too early: someone might lie about what they see.",
                }
            },
            "win_condition": {
                "de": "Wenn du am Ende die richtige Person nennst UND erklaerst was auf deinem Foto steht: Du gewinnst allein.",
                "en": "If at the end you name the right person AND explain what is on your photo: you win alone.",
            },
            "clues_i_hold": [],
            "starting_knowledge": {
                "de": "Du hast das Foto. Der Name darauf — die App sagt dir was du wirklich sahst. Je mehr du redest desto klarer wird deine Erinnerung.",
                "en": "You have the photo. The name on it — the app tells you what you really saw. The more you speak the clearer your memory becomes.",
            },
            "connection": {"with": "murderer", "type": "designer_saw_laptop"}
        },

        "journalist": {
            "name": {"de": "Tim Reuter, Tech-Journalist", "en": "Tim Reuter, Tech Journalist",
                     "fr": "Tim Reuter, Journaliste tech", "it": "Tim Reuter, Giornalista tech",
                     "es": "Tim Reuter, Periodista tech", "pt": "Tim Reuter, Jornalista tech"},
            "min_players": 5,
            "can_be_murderer": False,
            "startup_role": "Senior Reporter — TechCrunch DE",
            "intro": {
                "de": "Tim Reuter. TechCrunch Deutschland. Ich war nicht wegen des Artikels hier — ich war hier wegen der Geschichte dahinter. NovaTech ist kein KI-Startup. Und das kann ich jetzt beweisen.",
                "en": "Tim Reuter. TechCrunch Germany. I was not here for the article — I was here for the story behind it. NovaTech is not an AI startup. And I can now prove it.",
            },
            "appearance": {
                "de": "Aufnahmegeraet (Stift/Handy) immer sichtbar. Stellt Fragen die klingen als waeren sie kein Interview. Hat heute Abend schon drei Leute einzeln in die Ecke genommen.",
                "en": "Recording device (pen/phone) always visible. Asks questions that sound like they're not an interview. Has already cornered three people individually tonight.",
            },
            "secret": {
                "de": "Ich recherchiere seit vier Monaten. KI ist fake. Jemand hat mir anonym Dokumente zugespielt — ich weiss nicht wer. Heute Abend wollte ich Magnus konfrontieren. Er war schon tot als ich in den Serverraum kam.",
                "en": "I have been researching for four months. AI is fake. Someone anonymously sent me documents — I don't know who. Tonight I wanted to confront Magnus. He was already dead when I reached the server room.",
            },
            "ability": {
                "name": {"de": "Der Exklusiv-Bericht", "en": "The Exclusive Story"},
                "description": {
                    "de": "Wenn du bis zum Ende Moerder + KI-Betrug + Pitch-Deck-Dieb + anonymen Informanten aufgedeckt hast: Journalist des Jahres. Nur Moerder: normaler Sieg. Nichts: Verlust.",
                    "en": "If by the end you uncovered murderer + AI fraud + pitch deck thief + anonymous informant: journalist of the year. Only murderer: normal win. Nothing: loss.",
                }
            },
            "win_condition": {
                "de": "Alle Wahrheiten aufdecken: Story des Jahres. Nur Moerder: normaler Sieg. Nichts: Verlust.",
                "en": "Uncover all truths: story of the year. Only murderer: normal win. Nothing: loss.",
            },
            "clues_i_hold": ["investigative_notes", "anonymous_source_document"],
            "starting_knowledge": {
                "de": "Du weisst vom KI-Betrug. Jemand hat dir anonym Dokumente geschickt — die App zeigt dir einen Hinweis wer. Du brauchst noch mehr.",
                "en": "You know about the AI fraud. Someone anonymously sent you documents — the app gives you a hint who. You need more.",
            },
            "connection": {"with": "investor_lead", "type": "journalist_got_leak_from_someone"}
        },

        "pr_manager": {
            "name": {"de": "Lara Vogel, PR-Managerin", "en": "Lara Vogel, PR Manager",
                     "fr": "Lara Vogel, Responsable PR", "it": "Lara Vogel, PR Manager",
                     "es": "Lara Vogel, Directora de PR", "pt": "Lara Vogel, Gerente de PR"},
            "min_players": 5,
            "can_be_murderer": True,
            "startup_role": "Head of Communications — NovaTech AI",
            "intro": {
                "de": "Lara Vogel. Ich manage die Kommunikation. Ich habe heute Abend alles organisiert. Und jetzt ist alles in Truemmern. Ich bin die Einzige die weiss wie man das noch retten kann.",
                "en": "Lara Vogel. I manage communications. I organized everything tonight. And now everything is in ruins. I am the only one who knows how to still save this.",
            },
            "appearance": {
                "de": "Perfekte Frisur. Drei verschiedene Handys. Beantwortet noch immer Journalisten-Anfragen. Weint nicht — obwohl sie es koennte.",
                "en": "Perfect hair. Three different phones. Still answering journalist requests. Does not cry — although she could.",
            },
            "secret": {
                "de": "Magnus und ich hatten eine Affaere — acht Monate. Heute Abend wollte er Schluss machen. Er hatte eine Mail an alle 50 Mitarbeiter fertig: 'Persoenliche Angelegenheiten muessen getrennt bleiben.' Er meinte mich. Ich war im Serverraum als er sie schrieb.",
                "en": "Magnus and I had an affair — eight months. Tonight he wanted to end it. He had an email ready to all 50 employees: 'Personal matters must remain separate.' He meant me. I was in the server room when he wrote it.",
            },
            "ability": {
                "name": {"de": "Der Social Media Post", "en": "The Social Media Post"},
                "description": {
                    "de": "Einmal kannst du etwas 'posten' — du liest es laut vor und es gilt als oeffentliche Aussage. Wahr oder falsch. Danach kann es nicht zurueckgenommen werden.",
                    "en": "Once you may 'post' something — you read it aloud and it counts as a public statement. True or false. Afterwards it cannot be taken back.",
                }
            },
            "win_condition": {
                "de": "Ueberlebe ohne dass die Affaere mit Magnus oeffentlich wird.",
                "en": "Survive without the affair with Magnus becoming public.",
            },
            "murderer_motive_if_assigned": {
                "de": "Lara toetete Magnus bevor er die Mail abschicken konnte. Sie hatte seinen Kaffee. Sie hatte Zugang. Sie hatte ein Motiv das sie nie zugeben wird.",
                "en": "Lara killed Magnus before he could send the email. She had his coffee. She had access. She had a motive she will never admit.",
            },
            "clues_i_hold": ["affair_whatsapp_screenshot", "company_email_draft"],
            "starting_knowledge": {
                "de": "Du hast Magnus' Mail-Entwurf gelesen. Du warst im Serverraum — kurz. Niemand weiss es. Oder? Der Co-Founder koennte von der Affaere wissen.",
                "en": "You read Magnus' email draft. You were in the server room — briefly. Nobody knows. Or do they? The co-founder might know about the affair.",
            },
            "connection": {"with": "cofounder", "type": "cofounder_knows_affair"}
        },

        "lawyer": {
            "name": {"de": "Jonas Krause, Anwalt", "en": "Jonas Krause, Lawyer",
                     "fr": "Jonas Krause, Avocat", "it": "Jonas Krause, Avvocato",
                     "es": "Jonas Krause, Abogado", "pt": "Jonas Krause, Advogado"},
            "min_players": 6,
            "can_be_murderer": True,
            "startup_role": "Founding Attorney — NovaTech AI",
            "intro": {
                "de": "Jonas Krause. Ich habe alle Vertraege aufgesetzt. Ich weiss was drin steht. Und ich weiss was NICHT drin steht — was aber eigentlich drin sein muesste.",
                "en": "Jonas Krause. I set up all the contracts. I know what is in them. And I know what is NOT in them — but what actually should be.",
            },
            "appearance": {
                "de": "Makellos. Immer eine Akte dabei. Antwortet nie direkt. Jede Antwort beginnt mit 'Das kommt darauf an'.",
                "en": "Immaculate. Always a file with him. Never answers directly. Every answer begins with 'That depends'.",
            },
            "secret": {
                "de": "Die Investitionsvertraege haben eine Klausel die niemand bemerkt hat: Bei Tod des CEOs geht die operative Kontrolle an einen stillen Teilhaber. Das bin ich. Magnus wollte das heute Abend aendern. Um 22:00 Uhr haette er unterschrieben.",
                "en": "The investment contracts have a clause nobody noticed: upon death of CEO, operational control goes to a silent partner. That is me. Magnus wanted to change that tonight. At 10pm he would have signed.",
            },
            "ability": {
                "name": {"de": "Die Klausel", "en": "The Clause"},
                "description": {
                    "de": "Du kennst eine Klausel die alles veraendert. Offenbarst du sie: Du wirst sofort verdaechtig — aber auch maechtiger. Schweigst du: Sie koennte trotzdem gefunden werden.",
                    "en": "You know a clause that changes everything. Reveal it: you become immediately suspicious — but also more powerful. Stay silent: it might still be found.",
                }
            },
            "win_condition": {
                "de": "Ueberlebe. Die Klausel muss still in Kraft bleiben.",
                "en": "Survive. The clause must remain quietly in force.",
            },
            "murderer_motive_if_assigned": {
                "de": "Jonas toetete Magnus bevor er um 22:00 Uhr die Klausel aendern konnte. Mit Magnus' Tod erbt Jonas die Kontrolle. Legal. Perfekt. Wenn niemand die Klausel findet.",
                "en": "Jonas killed Magnus before he could change the clause at 10pm. With Magnus' death Jonas inherits control. Legal. Perfect. If nobody finds the clause.",
            },
            "clues_i_hold": ["investment_contract_clause", "corporate_structure_chart"],
            "starting_knowledge": {
                "de": "Die Klausel macht dich zum Hauptnutzniesser von Magnus' Tod. Das weiss noch niemand. Aber der Journalist sucht nach Vertragsdetails.",
                "en": "The clause makes you the main beneficiary of Magnus' death. Nobody knows yet. But the journalist is looking for contract details.",
            },
            "connection": {"with": "investor_lead", "type": "lawyer_investor_know_clause"}
        },

        "angel_investor": {
            "name": {"de": "Kai Mehta, Angel Investor", "en": "Kai Mehta, Angel Investor",
                     "fr": "Kai Mehta, Business Angel", "it": "Kai Mehta, Angel Investor",
                     "es": "Kai Mehta, Inversor angel", "pt": "Kai Mehta, Investidor anjo"},
            "min_players": 7,
            "can_be_murderer": True,
            "startup_role": "Angel Investor — Early Stage",
            "intro": {
                "de": "Kai Mehta. Vor drei Jahren 500.000 Euro in NovaTech investiert. Heute Abend war mein Exit. 8 Millionen. Dann wurde Magnus tot gefunden. Ich brauche dieses Geld.",
                "en": "Kai Mehta. Three years ago I invested 500,000 euros in NovaTech. Tonight was my exit. 8 million. Then Magnus was found dead. I need this money.",
            },
            "appearance": {
                "de": "Trinkt zu viel. Hat sein Telefon versteckt. War heute Abend dreimal 'auf der Toilette'.",
                "en": "Drinking too much. Has hidden his phone. Tonight went to the 'bathroom' three times.",
            },
            "secret": {
                "de": "Ich brauche die 8 Millionen dringend. Mein Privatvermogen ist in anderen Investments versunken. Ich bin faktisch bankrott — niemand weiss es. Magnus wusste es. Er drohte es zu veroeffentlichen wenn ich einer Vertragsaenderung nicht zustimme.",
                "en": "I urgently need the 8 million. My private assets have sunk into other investments. I am effectively bankrupt — nobody knows. Magnus knew. He threatened to publish it if I didn't agree to a contract change.",
            },
            "ability": {
                "name": {"de": "Der Exit-Vertrag", "en": "The Exit Contract"},
                "description": {
                    "de": "Du hast einen Exit-Vertrag der dir 8 Millionen sichert — aber nur wenn der Deal abschliesst. Zeigst du ihn: Alle kennen dein Motiv. Versteckst du ihn: Du wirkst verdaechtiger je laenger das Spiel dauert.",
                    "en": "You have an exit contract securing 8 million — but only if the deal closes. Show it: everyone knows your motive. Hide it: you become more suspicious the longer the game goes on.",
                }
            },
            "win_condition": {
                "de": "Ueberlebe ohne dass deine faktische Pleite oeffentlich wird.",
                "en": "Survive without your effective bankruptcy becoming public.",
            },
            "murderer_motive_if_assigned": {
                "de": "Kai toetete Magnus um den Deal zu retten — mit einem anderen CEO laeuft der Deal weiter. Er brauchte nur Magnus zu entfernen. Schnell.",
                "en": "Kai killed Magnus to save the deal — with a different CEO the deal continues. He just needed to remove Magnus. Quickly.",
            },
            "clues_i_hold": ["exit_contract_draft", "bankruptcy_hidden_traces"],
            "starting_knowledge": {
                "de": "Du brauchst dieses Geld. Magnus wusste es und nutzte es. Dein Handy hat Nachrichten die du nicht zeigen willst. Und du warst dreimal 'auf der Toilette' — aber nicht auf der Toilette.",
                "en": "You need this money. Magnus knew and exploited it. Your phone has messages you don't want to show. And you went to the 'bathroom' three times — but not to the bathroom.",
            },
            "connection": {"with": "lawyer", "type": "investor2_lawyer_share_interest"}
        },

        "ex_partner": {
            "name": {"de": "Finn Bauer, Ex-Mitgruender", "en": "Finn Bauer, Ex-Co-Founder",
                     "fr": "Finn Bauer, Ex-cofondateur", "it": "Finn Bauer, Ex-cofondatore",
                     "es": "Finn Bauer, Ex-cofundador", "pt": "Finn Bauer, Ex-cofundador"},
            "min_players": 7,
            "can_be_murderer": True,
            "startup_role": "Freelancer (ehem. Co-Founder — NovaTech AI)",
            "intro": {
                "de": "Finn Bauer. Ich war einmal Co-Gruender. Dann hat Magnus mich rausgeworfen — mit einem laecherlichen Abfindungsangebot. Die Kernidee von NovaTech? Stammt von mir. Heute Nacht wollte ich es zurueck.",
                "en": "Finn Bauer. I was once co-founder. Then Magnus threw me out — with a ridiculous severance. The core idea of NovaTech? Came from me. Tonight I wanted it back.",
            },
            "appearance": {
                "de": "Kein Namensschild — nicht eingeladen. Mehrere leere Glaeser. Sehr ruhig. Zu ruhig.",
                "en": "No name badge — not invited. Several empty glasses. Very calm. Too calm.",
            },
            "secret": {
                "de": "Nicht eingeladen aber trotzdem hier. Ich habe einen USB-Stick mit dem Originalcode — mit meinem Namen in den Kommentaren. Ich habe Magnus ein Ultimatum gestellt: 5% Anteile oder ich gehe an die Presse. Er hat gelacht.",
                "en": "Not invited but here anyway. I have a USB stick with the original code — with my name in the comments. I gave Magnus an ultimatum: 5% shares or I go to the press. He laughed.",
            },
            "ability": {
                "name": {"de": "Der USB-Stick", "en": "The USB Stick"},
                "description": {
                    "de": "Du hast einen USB-Stick mit dem Originalcode. Zeigst du ihn: Starker Beweis fuer deinen Diebstahlsvorwurf. Versteckst du ihn: Mysterioser aber verdaechtiger.",
                    "en": "You have a USB stick with the original code. Show it: strong evidence for your theft accusation. Hide it: more mysterious but more suspicious.",
                }
            },
            "win_condition": {
                "de": "Wenn am Ende anerkannt wird dass Magnus die Kernidee gestohlen hat: Du gewinnst — auch ohne den Moerder zu nennen.",
                "en": "If at the end it is acknowledged that Magnus stole the core idea: you win — even without naming the murderer.",
            },
            "murderer_motive_if_assigned": {
                "de": "Finn toetete Magnus nach seinem Lachen. Sechs Jahre Arbeit. Eine gestohlene Idee. Und dann lacht er. Das war zu viel.",
                "en": "Finn killed Magnus after his laughter. Six years of work. A stolen idea. And then he laughs. That was too much.",
            },
            "clues_i_hold": ["original_code_usb", "termination_contract_unfair"],
            "starting_knowledge": {
                "de": "Du warst im Gespraech mit Magnus. Er hat gelacht. Dann bist du gegangen. Dann war er tot. Du warst nicht eingeladen — das macht dich automatisch verdaechtiger als alle anderen.",
                "en": "You were in conversation with Magnus. He laughed. Then you left. Then he was dead. You were not invited — that automatically makes you more suspicious than everyone else.",
            },
            "connection": {"with": "journalist", "type": "expartner_journalist_share_info"}
        },

        "hacker": {
            "name": {"de": "Ronja, Security-Beraterin", "en": "Ronja, Security Consultant",
                     "fr": "Ronja, Consultante en securite", "it": "Ronja, Consulente di sicurezza",
                     "es": "Ronja, Consultora de seguridad", "pt": "Ronja, Consultora de seguranca"},
            "min_players": 7,
            "can_be_murderer": False,
            "is_wildcard": True,
            "startup_role": "Freelance Security Consultant (inoffiziell)",
            "intro": {
                "de": "Ronja. Security-Beraterin. Ich bin hier weil mich jemand darum gebeten hat. Den Namen nenne ich nicht. Ich war nicht im Serverraum. Ich habe nichts gestohlen. Und dieses Burner-Handy gehoert mir nicht.",
                "en": "Ronja. Security consultant. I am here because someone asked me to be. I won't name who. I was not in the server room. I stole nothing. And this burner phone is not mine.",
            },
            "appearance": {
                "de": "Schwarze Kleidung. Haelt das Burner-Handy (Zettel) in der Hand. Gibt es nicht aus der Hand.",
                "en": "Black clothing. Holds the burner phone (note) in her hand. Does not let it go.",
            },
            "secret": {
                "de": "Jemand hat mich bezahlt das Pitch Deck zu stehlen und auf einem bestimmten Server hochzuladen. Ich habe es getan. Ich weiss wer mich beauftragt hat — und dieser Auftraggeber weiss nicht dass ich auch den kompletten Slack-Export gesichert habe. Als Absicherung.",
                "en": "Someone paid me to steal the pitch deck and upload it to a specific server. I did it. I know who commissioned me — and that client does not know I also backed up the complete Slack export. As insurance.",
            },
            "ability": {
                "name": {"de": "Der Slack-Export", "en": "The Slack Export"},
                "description": {
                    "de": "Du hast den kompletten Slack-Export des Abends. Darin steht alles. Du entscheidest was du zeigst und was du behaeltst.",
                    "en": "You have the complete Slack export of the evening. Everything is in it. You decide what to show and what to keep.",
                }
            },
            "win_condition": {
                "de": "Das Pitch Deck darf niemand finden. Wenn der Moerder gefasst wird und niemand weiss wo das Deck ist: Du gewinnst.",
                "en": "Nobody must find the pitch deck. If the murderer is caught and nobody knows where the deck is: you win.",
            },
            "clues_i_hold": ["slack_export_tonight", "burner_phone_messages", "upload_confirmation"],
            "starting_knowledge": {
                "de": "Du hast das Pitch Deck gestohlen — auf Auftrag. Du hast den Slack-Export. Die App sagt dir wer dich beauftragt hat. Du warst im Serverraum — aber NACH dem Tod.",
                "en": "You stole the pitch deck — on commission. You have the Slack export. The app tells you who commissioned you. You were in the server room — but AFTER the death.",
            },
            "connection": {"with": "cto", "type": "hacker_hired_by_someone"}
        },

        "detective": {
            "name": {"de": "Inspektor Nina Wolf", "en": "Inspector Nina Wolf",
                     "fr": "Inspectrice Nina Wolf", "it": "Ispettrice Nina Wolf",
                     "es": "Inspectora Nina Wolf", "pt": "Inspetora Nina Wolf"},
            "min_players": 8,
            "can_be_murderer": False,
            "startup_role": "Kriminalinspektion Berlin — LKA Wirtschaftskriminalitaet",
            "intro": {
                "de": "Nina Wolf. LKA Berlin, Wirtschaftskriminalitaet. Ich war als Gaestin hier — mein Bruder arbeitet bei NovaTech. Jetzt bin ich im Dienst. Verstaerkung kommt in zwei Stunden. Bis dahin bin ich alles was ihr habt.",
                "en": "Nina Wolf. LKA Berlin, Economic Crime. I was here as a guest — my brother works at NovaTech. Now I am on duty. Reinforcements arrive in two hours. Until then I am all you have.",
            },
            "appearance": {
                "de": "Dienstmarke herausgekramt. Einzige ohne Startup-Namensschild. Macht Sprachnotizen auf dem Telefon.",
                "en": "Badge produced. Only one without startup name badge. Making voice notes on phone.",
            },
            "secret": {
                "de": "Ich bin nicht zufaellig hier. Ich observiere NovaTech seit sechs Wochen wegen Datenmissbrauch und Investorenbetrug. Mein Bruder ist meine inoffizielle Quelle — er weiss es nicht. Ich darf diese Verbindung nicht offenbaren.",
                "en": "I am not here by chance. I have been surveilling NovaTech for six weeks due to data misuse and investor fraud. My brother is my unofficial source — he doesn't know. I cannot reveal this connection.",
            },
            "ability": {
                "name": {"de": "Die offizielle Befragung", "en": "The Official Questioning"},
                "description": {
                    "de": "Einmal kannst du eine offizielle Befragung ausrufen. Alle verlassen den Raum. Du redest 3 Minuten allein mit einer Person. Danach sagen alle ob sie kooperativ war.",
                    "en": "Once you may call an official questioning. Everyone leaves the room. You talk alone with one person for 3 minutes. Afterwards everyone says if they were cooperative.",
                }
            },
            "win_condition": {
                "de": "Du gewinnst NUR wenn DU als erste den Moerder offiziell mit mindestens zwei Beweisen korrekt nennst.",
                "en": "You win ONLY if YOU are first to officially and correctly name the murderer with at least two pieces of evidence.",
            },
            "clues_i_hold": ["lka_surveillance_notes", "novatech_investigation_file"],
            "starting_knowledge": {
                "de": "Du weisst von Datenmissbrauch und Investorenbetrug bei NovaTech. Jemand hier hat heute Abend anonym Dokumente weitergegeben. Dein Bruder kennt den Moerder — ohne es zu wissen.",
                "en": "You know about data misuse and investor fraud at NovaTech. Someone here tonight anonymously passed on documents. Your brother knows the murderer — without knowing it.",
            },
            "connection": {"with": "cofounder", "type": "inspector_brother_is_cofounder"}
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # HINWEIS-KETTEN (8 Ketten, 35 Hinweise)
    # ─────────────────────────────────────────────────────────────────────────
    "clue_chains": {
        "chain_tod": {
            "name": {"de": "Die Todeskette", "en": "The Death Chain"},
            "clues_in_order": ["cause_of_death_pitch", "coffee_mug_residue", "time_of_death_logs", "server_room_access", "camera_deleted"],
            "reveal_condition": "inspector_examines"
        },
        "chain_ai": {
            "name": {"de": "Die KI-Kette", "en": "The AI Chain"},
            "clues_in_order": ["ai_fakery_code_snippet", "training_data_stolen", "pitch_deck_lie", "demo_script_found"],
            "reveal_condition": "journalist_reveals"
        },
        "chain_laptop": {
            "name": {"de": "Die Laptop-Kette", "en": "The Laptop Chain"},
            "clues_in_order": ["laptop_screen_message", "deleted_email_draft", "designer_blurry_photo", "email_timestamp"],
            "reveal_condition": "designer_shows_photo"
        },
        "chain_pitchdeck": {
            "name": {"de": "Die Pitch-Deck-Kette", "en": "The Pitch Deck Chain"},
            "clues_in_order": ["pitch_deck_gone", "upload_confirmation", "burner_phone_messages", "hacker_tools_found"],
            "reveal_condition": "hacker_pressured"
        },
        "chain_slack": {
            "name": {"de": "Die Slack-Kette", "en": "The Slack Chain"},
            "clues_in_order": ["slack_log_threat", "slack_export_tonight", "magnus_last_message", "partnership_dissolution_email"],
            "reveal_condition": "cofounder_pressured"
        },
        "chain_vertrag": {
            "name": {"de": "Die Vertragskette", "en": "The Contract Chain"},
            "clues_in_order": ["investment_contract_signed", "investment_contract_clause", "corporate_structure_chart", "exit_contract_draft"],
            "reveal_condition": "lawyer_pressured"
        },
        "chain_affaere": {
            "name": {"de": "Die Affaerenkette", "en": "The Affair Chain"},
            "clues_in_order": ["affair_whatsapp_screenshot", "company_email_draft", "pr_server_room_trace", "cofounder_knows_affair_clue"],
            "reveal_condition": "pr_pressured"
        },
        "chain_betrug": {
            "name": {"de": "Die Betrugskette", "en": "The Fraud Chain"},
            "clues_in_order": ["data_theft_report_draft", "anonymous_source_document", "investigative_notes", "lka_surveillance_notes", "bankruptcy_hidden_traces"],
            "reveal_condition": "journalist_inspector_cooperate"
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # HINWEISE (35 Stueck)
    # ─────────────────────────────────────────────────────────────────────────
    "clues": {
        # Todeskette
        "cause_of_death_pitch": {
            "name": {"de": "Todesursache (vorlaeufig)", "en": "Cause of Death (preliminary)"},
            "text": {"de": "Herzstillstand. Aber: Kaffeebecherrand hat weissen Rueckstand. Kein natuerlicher Tod. Verdacht: Barbiturate — schnell loeslich, geruchlos. Todeszeit: zwischen 21:40 und 22:00 Uhr.", "en": "Cardiac arrest. But: coffee mug rim has white residue. Not natural death. Suspicion: barbiturates — fast dissolving, odourless. Time of death: between 9:40 and 10pm."}
        },
        "coffee_mug_residue": {
            "name": {"de": "[Screenshot] Kaffeebecheranalyse", "en": "[Screenshot] Coffee Mug Analysis"},
            "text": {"de": "Foto des Kaffeebechers im Serverraum. Rand: weisser Rueckstand. Handschriftliche Notiz: 'Wer hatte Zugang zu Magnus' Becher? Becher stand die ganze Party auf seinem Schreibtisch.'", "en": "Photo of the coffee mug in the server room. Rim: white residue. Handwritten note: 'Who had access to Magnus' mug? Mug was on his desk all evening.'"}
        },
        "time_of_death_logs": {
            "name": {"de": "Server-Log: Zugriffszeiten", "en": "Server Log: Access Times"},
            "text": {"de": "Server-Log-Auszug: 21:31 — Serverraum-Tuer geoeffnet (Chip-Karte unbekannt). 21:47 — Laptop-Aktivitaet eingestellt. 21:58 — Tuer erneut geoeffnet (Chip-Karte: Mia Hoffmann, CTO).", "en": "Server log excerpt: 9:31pm — server room door opened (chip card unknown). 9:47pm — laptop activity stopped. 9:58pm — door opened again (chip card: Mia Hoffmann, CTO)."}
        },
        "server_room_access": {
            "name": {"de": "Zugangsliste Serverraum", "en": "Server Room Access List"},
            "text": {"de": "Chip-Ausweise fuer den Serverraum: CTO (Mia), CEO (Magnus — tot), Co-Founder (Leon), und eine Gast-Karte ausgegeben um 17:00 Uhr. Wer hat die Gast-Karte?", "en": "Chip cards for server room: CTO (Mia), CEO (Magnus — dead), Co-Founder (Leon), and a guest card issued at 5pm. Who has the guest card?"}
        },
        "camera_deleted": {
            "name": {"de": "Kameraaufnahmen geloescht", "en": "Camera Recordings Deleted"},
            "text": {"de": "Die Serverraum-Kamera hat Aufnahmen — aber ab 21:30 Uhr sind sie geloescht. Manuell. Jemand mit NAS-Zugang: die CTO — oder der Co-Founder.", "en": "The server room camera has recordings — but from 9:30pm they are deleted. Manually. Someone with NAS access: the CTO — or the co-founder."}
        },
        # KI-Kette
        "ai_fakery_code_snippet": {
            "name": {"de": "[Screenshot] Echter Code", "en": "[Screenshot] Real Code"},
            "text": {"de": "Python-Code-Screenshot: '# TODO: Replace hardcoded responses with actual ML // Magnus: just ship it, nobody will notice'. Datum: vor 8 Monaten. Autor: mia_h@novatech.ai", "en": "Python code screenshot: '# TODO: Replace hardcoded responses with actual ML // Magnus: just ship it, nobody will notice'. Date: 8 months ago. Author: mia_h@novatech.ai"}
        },
        "training_data_stolen": {
            "name": {"de": "Datendiebstahl-Report", "en": "Data Theft Report"},
            "text": {"de": "Interner Report: 60% der Trainingsdaten aus nicht lizenzierten Quellen. GDPR-Verletzung. Potenzieller Schaden: unbegrenzt. Unterzeichner: Dr. S. Chen — aber nie weitergeleitet.", "en": "Internal report: 60% of training data from unlicensed sources. GDPR violation. Potential damage: unlimited. Signatory: Dr. S. Chen — but never forwarded."}
        },
        "pitch_deck_lie": {
            "name": {"de": "[Abschrift] Pitch Deck Slide 12", "en": "[Transcript] Pitch Deck Slide 12"},
            "text": {"de": "'Unsere proprietaere KI-Engine verarbeitet 2 Milliarden Parameter...' — darunter handgeschrieben: 'Das stimmt nicht. M.F. weiss es. S.C. weiss es. — anonym'", "en": "'Our proprietary AI engine processes 2 billion parameters...' — below handwritten: 'This is not true. M.F. knows it. S.C. knows it. — anonymous'"}
        },
        "demo_script_found": {
            "name": {"de": "Demo-Script: Live-Investor-Demo", "en": "Demo Script: Live Investor Demo"},
            "text": {"de": "Ausdruck unter Magnus' Schreibtisch: 'WENN Investorin dritte Frage stellt — Tab zu Skript B wechseln. NICHT Skript A.' Ein auf Bestellung inszenierter Betrug.", "en": "Printout under Magnus' desk: 'WHEN investor asks third question — switch tab to Script B. NOT Script A.' A fraud staged on demand."}
        },
        # Laptop-Kette
        "laptop_screen_message": {
            "name": {"de": "Laptop: Letzte Nachricht", "en": "Laptop: Last Message"},
            "text": {"de": "Post-it auf Magnus' Laptop: 'Ich weiss was du getan hast.' Dahinter: angefangene Email. Empfaenger: alle@novatech.ai. Betreff: 'Die Wahrheit ueber NovaTech'.", "en": "Post-it on Magnus' laptop: 'I know what you did.' Behind it: unfinished email. Recipient: all@novatech.ai. Subject: 'The truth about NovaTech'."}
        },
        "deleted_email_draft": {
            "name": {"de": "Geloeschter Email-Entwurf", "en": "Deleted Email Draft"},
            "text": {"de": "Aus dem Papierkorb wiederhergestellt: Magnus' Email. 'Ich muss euch etwas gestehen...' — bricht ab. Zeitstempel: 21:44. Drei Minuten vor seinem Tod.", "en": "Restored from trash: Magnus' email. 'I have to confess something to you...' — stops. Timestamp: 9:44pm. Three minutes before his death."}
        },
        "designer_blurry_photo": {
            "name": {"de": "Jess Parks unscharfes Foto", "en": "Jess Park's Blurry Photo"},
            "text": {"de": "Jess hat ein Foto von Magnus' Laptop-Bildschirm. Unscharf. Aufgenommen um 21:43:12. Man kann einen Namen in der offenen Email erkennen — wenn man genau hinschaut.", "en": "Jess has a photo of Magnus' laptop screen. Blurry. Taken at 9:43:12pm. A name in the open email can be recognized — if you look carefully."}
        },
        "email_timestamp": {
            "name": {"de": "Email: Zeitstempel & CC", "en": "Email: Timestamp & CC"},
            "text": {"de": "Der Email-Entwurf wurde angefangen um 21:43. Empfaenger: alle@novatech.ai. CC: Eine Person — Name wurde geloescht. Wer loescht einen CC aus einem Entwurf?", "en": "The email draft was started at 9:43pm. Recipient: all@novatech.ai. CC: one person — name was deleted. Who deletes a CC from a draft?"}
        },
        # Pitch-Deck-Kette
        "pitch_deck_gone": {
            "name": {"de": "Pitch Deck: Weg", "en": "Pitch Deck: Gone"},
            "text": {"de": "Der Umschlag 'PITCH DECK — VERTRAULICH' ist leer. Gestohlen. Es lag auf Magnus' Schreibtisch im Serverraum. Wer war heute Abend im Serverraum?", "en": "The envelope 'PITCH DECK — CONFIDENTIAL' is empty. Stolen. It was on Magnus' desk in the server room. Who was in the server room tonight?"}
        },
        "upload_confirmation": {
            "name": {"de": "[Burner-Handy] Upload-Bestaetigung", "en": "[Burner Phone] Upload Confirmation"},
            "text": {"de": "Nachricht auf dem Burner-Handy: 'Upload bestaetigt. Datei auf Server XY. Zugang: [ZENSIERT]. Danke — Auftraggeber.' Zeitstempel: 22:01 Uhr.", "en": "Message on burner phone: 'Upload confirmed. File on server XY. Access: [CENSORED]. Thank you — client.' Timestamp: 10:01pm."}
        },
        "burner_phone_messages": {
            "name": {"de": "[Burner-Handy] 3 anonyme Nachrichten", "en": "[Burner Phone] 3 Anonymous Messages"},
            "text": {"de": "Drei Nachrichten: '1: Ich weiss von dir und M. | 2: Das Pitch Deck luegt. | 3: Komm allein in den Serverraum.' Von drei verschiedenen Nummern die alle nach 20:00 Uhr erstellt wurden.", "en": "Three messages: '1: I know about you and M. | 2: The pitch deck lies. | 3: Come to the server room alone.' From three different numbers all created after 8pm."}
        },
        "hacker_tools_found": {
            "name": {"de": "Hacker-Equipment", "en": "Hacker Equipment"},
            "text": {"de": "In einer Handtasche auf der Party: Lock-Pick-Set, USB-Rubber-Ducky, Latex-Handschuhe. Professionell. Nicht die Ausruestung einer normal eingeladenen Sicherheitsberaterin.", "en": "In a handbag at the party: lock pick set, USB rubber ducky, latex gloves. Professional. Not the equipment of a normally invited security consultant."}
        },
        # Slack-Kette
        "slack_log_threat": {
            "name": {"de": "[Slack-Log] Die Drohung", "en": "[Slack Log] The Threat"},
            "text": {"de": "DM Leon → Magnus, 21:13: 'Das wirst du bereuen.' Magnus → Leon, 21:14: 'Zu spaet.' Leon → Magnus, 21:15: [keine Antwort]", "en": "DM Leon → Magnus, 9:13pm: 'You will regret this.' Magnus → Leon, 9:14pm: 'Too late.' Leon → Magnus, 9:15pm: [no response]"}
        },
        "slack_export_tonight": {
            "name": {"de": "Slack-Export: Heute Abend", "en": "Slack Export: Tonight"},
            "text": {"de": "Ronja hat den kompletten Slack-Export. Alle Nachrichten. Alle Zeitstempel. Wer will was sehen? Sie entscheidet.", "en": "Ronja has the complete Slack export. All messages. All timestamps. Who wants to see what? She decides."}
        },
        "magnus_last_message": {
            "name": {"de": "[Slack] Magnus' letzte Nachricht", "en": "[Slack] Magnus' Last Message"},
            "text": {"de": "#general, 21:09, Frey_Magnus: 'Ich weiss wer es war.' Dann: Stille. Drei Personen haben die Nachricht gelesen — Lesebestaetigung sichtbar. Drei Namen.", "en": "#general, 9:09pm, Frey_Magnus: 'I know who it was.' Then: silence. Three people read the message — read receipts visible. Three names."}
        },
        "partnership_dissolution_email": {
            "name": {"de": "Email: Partnerschaftsaufloesung", "en": "Email: Partnership Dissolution"},
            "text": {"de": "Email Magnus → Leon, 20:47: 'Hiermit loeese ich die Co-Founder-Vereinbarung auf. Sofortige Wirkung. Dein Anteil: 8%. Anwalt Jonas ist informiert.' 47 Minuten spaeter war Magnus tot.", "en": "Email Magnus → Leon, 8:47pm: 'I hereby dissolve the co-founder agreement. Immediate effect. Your share: 8%. Attorney Jonas is informed.' 47 minutes later Magnus was dead."}
        },
        # Vertragskette
        "investment_contract_signed": {
            "name": {"de": "Investitionsvertrag: Unterschrieben", "en": "Investment Contract: Signed"},
            "text": {"de": "Dr. Sarah Chen hat unterschrieben. 50 Millionen Euro. Aber: Seite 47 hat eine Klausel die niemand bemerkt hat — oder die niemand bemerken sollte.", "en": "Dr. Sarah Chen has signed. 50 million euros. But: page 47 has a clause nobody noticed — or that nobody was supposed to notice."}
        },
        "investment_contract_clause": {
            "name": {"de": "Klausel 12b: Stiller Teilhaber", "en": "Clause 12b: Silent Partner"},
            "text": {"de": "Seite 47: 'Im Falle des Todes des CEOs geht die operative Kontrolle an den registrierten stillen Teilhaber.' Registriert: Jonas Krause, Anwalt.", "en": "Page 47: 'In the event of the CEO's death, operational control transfers to the registered silent partner.' Registered: Jonas Krause, attorney."}
        },
        "corporate_structure_chart": {
            "name": {"de": "Organigramm: Echte Struktur", "en": "Org Chart: Real Structure"},
            "text": {"de": "Handgezeichnetes Organigramm aus Jonas' Akte: Magnus (CEO) — Leon (COO) — Jonas (stiller Partner). Darunter: 'Nach Tod CEO: Jonas uebernimmt.' Datum: vor 3 Monaten.", "en": "Hand-drawn org chart from Jonas' file: Magnus (CEO) — Leon (COO) — Jonas (silent partner). Below: 'After CEO death: Jonas takes over.' Date: 3 months ago."}
        },
        "exit_contract_draft": {
            "name": {"de": "Exit-Vertrag: Kai Mehta", "en": "Exit Contract: Kai Mehta"},
            "text": {"de": "Kais Exit-Vertrag: 8 Millionen bei Deal-Abschluss. ABER Klausel: 'Zahlung verfaellt wenn Deal durch Tod des Hauptpartners platzt.' Magnus' Tod = Kais Exit platzt.", "en": "Kai's exit contract: 8 million on deal closing. BUT clause: 'Payment forfeited if deal collapses due to death of main partner.' Magnus' death = Kai's exit collapses."}
        },
        # Affaerenkette
        "affair_whatsapp_screenshot": {
            "name": {"de": "[Screenshot] WhatsApp-Verlauf", "en": "[Screenshot] WhatsApp History"},
            "text": {"de": "WhatsApp-Chat — beide Namen geschwearzt. Letzte sichtbare Nachricht: 'Ich kann nicht mehr so tun als ob nichts waere. Heute Abend sage ich es.' Datum: heute, 14:22.", "en": "WhatsApp chat — both names blacked out. Last visible message: 'I cannot keep pretending nothing is happening. Tonight I will say it.' Date: today, 2:22pm."}
        },
        "company_email_draft": {
            "name": {"de": "[Email-Entwurf] An alle Mitarbeiter", "en": "[Email Draft] To All Employees"},
            "text": {"de": "Magnus' Entwurf, Empfaenger: alle@novatech.ai, Betreff: 'Persoenliches Statement'. Text: 'Ich moechte heute Abend einen Fehler korrigieren...' — Rest geloescht.", "en": "Magnus' draft, recipient: all@novatech.ai, subject: 'Personal Statement'. Text: 'I would like to correct a mistake tonight...' — rest deleted."}
        },
        "pr_server_room_trace": {
            "name": {"de": "Serverraum-Spur: Kuenstlicher Nagel", "en": "Server Room Trace: Artificial Nail"},
            "text": {"de": "Auf dem Serverraum-Boden: Ein einzelner kuenstlicher Fingernagel. Persikofarbene Lackierung. Lara Vogel ist die Einzige mit kuenstlichen Naegeln in dieser Farbe.", "en": "On the server room floor: a single artificial fingernail. Peach varnish. Lara Vogel is the only one with artificial nails in this color."}
        },
        "cofounder_knows_affair_clue": {
            "name": {"de": "[Slack] Co-Founder wusste davon", "en": "[Slack] Co-Founder Knew"},
            "text": {"de": "Im Slack-Export: DM Leon → anonym, 19:02: 'Weisst du was heute Abend passiert? Magnus macht Schluss mit Lara. Vor allen.' Antwort: 'Serious?'", "en": "In Slack export: DM Leon → anonymous, 7:02pm: 'Do you know what happens tonight? Magnus is ending things with Lara. In front of everyone.' Reply: 'Serious?'"}
        },
        # Betrugskette
        "data_theft_report_draft": {
            "name": {"de": "Datenbetrug-Report: Entwurf", "en": "Data Fraud Report: Draft"},
            "text": {"de": "Dr. Chens interner Report: Datenbetrug NovaTech. 60% gestohlene Trainingsdaten. GDPR-Verletzung. Schadenspotenzial: 30 Millionen. Nie veroeffentlicht. Warum?", "en": "Dr. Chen's internal report: data fraud NovaTech. 60% stolen training data. GDPR violation. Damage potential: 30 million. Never published. Why?"}
        },
        "anonymous_source_document": {
            "name": {"de": "Anonyme Quelle: Kontoauszug", "en": "Anonymous Source: Bank Statement"},
            "text": {"de": "Tim hat anonym erhalten: Kontoauszuege zeigen NovaTech-Gelder auf ein Privatkonto. Kontonummer beginnt mit DE — nicht Magnus'. Wessen Konto?", "en": "Tim received anonymously: bank statements showing NovaTech funds to a private account. Account number starts with DE — not Magnus'. Whose account?"}
        },
        "investigative_notes": {
            "name": {"de": "Recherche-Notizen (Journalist)", "en": "Investigative Notes (Journalist)"},
            "text": {"de": "Tims Notizbuch: 'Betrug bestaetigt. Brauche noch: 1. Kontoinhaber. 2. Bestaetigung von innen. 3. Magnus-Statement.' Zwei hat er. Eine fehlt.", "en": "Tim's notebook: 'Fraud confirmed. Still need: 1. Account holder. 2. Inside confirmation. 3. Magnus statement.' He has two. One is missing."}
        },
        "lka_surveillance_notes": {
            "name": {"de": "LKA-Observationsnotizen", "en": "LKA Surveillance Notes"},
            "text": {"de": "Ninas Dienstnotizen: 'NovaTech — 6 Wochen Observierung. Verdacht: Datenmissbrauch, Investorenbetrug. Hauptverdaechtige: CEO, CTO, Lead-Investorin.' Beweissicherung geplant fuer heute.", "en": "Nina's duty notes: 'NovaTech — 6 weeks surveillance. Suspicion: data misuse, investor fraud. Main suspects: CEO, CTO, lead investor.' Evidence collection planned for today."}
        },
        "bankruptcy_hidden_traces": {
            "name": {"de": "Versteckte Bankrott-Spuren", "en": "Hidden Bankruptcy Traces"},
            "text": {"de": "Kais Telefon (falls zugaenglich): Drei Mahnungen. SMS vom Steuerberater: 'Kai, du musst jetzt handeln. Die Fristen laufen ab.' Datum: heute Mittag.", "en": "Kai's phone (if accessible): three dunning notices. SMS from tax advisor: 'Kai, you need to act now. Deadlines expiring.' Date: today at noon."}
        },
        # Sonderkarten
        "novatech_investigation_file": {
            "name": {"de": "NovaTech-Ermittlungsakte", "en": "NovaTech Investigation File"},
            "text": {"de": "Ninas Akte: Fuenf Verdaechtige. Fotos. Hintergrundchecks. Ein Name rot unterstrichen. Und: Eine Person an diesem Tisch ist Ninas inoffizielle Quelle — ohne es zu wissen.", "en": "Nina's file: five suspects. Photos. Background checks. One name underlined in red. And: one person at this table is Nina's unofficial source — without knowing it."}
        },
        "original_code_usb": {
            "name": {"de": "[USB-Stick] Originalcode", "en": "[USB Stick] Original Code"},
            "text": {"de": "Finns USB-Stick: Originalcode mit Zeitstempeln aus 2018 — drei Jahre vor NovaTech-Gruendung. Git-Kommentare: '// Finn Bauer, 2018-09-12'. Sein Name. Ueberall.", "en": "Finn's USB stick: original code with timestamps from 2018 — three years before NovaTech was founded. Git comments: '// Finn Bauer, 2018-09-12'. His name. Everywhere."}
        },
        "termination_contract_unfair": {
            "name": {"de": "Kuendigungsvertrag: Ungerecht", "en": "Termination Contract: Unfair"},
            "text": {"de": "Finns Abfindung: 50.000 Euro fuer 6 Jahre Arbeit und die Kernidee. Bei 50 Millionen Investitionsvolumen waere sein fairer Anteil 10-15 Millionen. Magnus zahlte: 50.000.", "en": "Finn's severance: 50,000 euros for 6 years of work and the core idea. At 50 million investment volume his fair share would be 10-15 million. Magnus paid: 50,000."}
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PHYSISCHE AUFGABEN (62 Stueck)
    # ─────────────────────────────────────────────────────────────────────────
    "physical_tasks": {

        # ── EROEFFNUNG ────────────────────────────────────────────────────────

        "task_party_crash": {
            "trigger_phase": 1, "trigger_condition": "game_started_immediately",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Host sagt: Ihr seid auf der NovaTech Funding-Party. Rooftop Berlin. Champagner. 50 Millionen kurz vor Abschluss. Dann: Ein Schrei aus dem Serverraum. Magnus Frey ist tot. Niemand verlaesst das Gebaeude.",
                "en": "Host says: You are at the NovaTech funding party. Berlin rooftop. Champagne. 50 million about to close. Then: a scream from the server room. Magnus Frey is dead. Nobody leaves the building.",
            }, "game_effect": "murder_announced"
        },

        "task_nametags": {
            "trigger_phase": 1, "trigger_condition": "game_started_1min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle schreiben ihren Rollennamen + Job-Titel auf einen Zettel als Startup-Namensschild. Finn Bauer traegt keins — er war nicht eingeladen.",
                "en": "Everyone writes their role name + job title on a note as a startup name badge. Finn Bauer wears none — he was not invited.",
            }, "game_effect": "roles_visible"
        },

        "task_champagner_toast": {
            "trigger_phase": 1, "trigger_condition": "game_started_2min",
            "assigned_to": "investor_lead",
            "instruction": {
                "de": "Steh auf. Hebe dein Champagnerglas. Sag: 'Auf NovaTech AI — und auf die Zukunft.' Alle trinken. Beobachte wer sein Glas nur andeutet. Wer trinkt als erstes?",
                "en": "Stand up. Raise your champagne glass. Say: 'To NovaTech AI — and to the future.' Everyone drinks. Observe who only gestures. Who drinks first?",
            }, "game_effect": "opening_toast"
        },

        "task_badge_shown": {
            "trigger_phase": 2, "trigger_condition": "body_discovered",
            "assigned_to": "detective",
            "instruction": {
                "de": "Steh auf. Zeig deine Dienstmarke. Sag: 'LKA Berlin. Niemand verlaesst diesen Raum. Alle Handys bleiben sichtbar auf dem Tisch. Und alle reden.' Dann setz dich.",
                "en": "Stand up. Show your badge. Say: 'LKA Berlin. Nobody leaves this room. All phones stay visible on the table. And everyone talks.' Then sit.",
            }, "game_effect": "authority_established"
        },

        "task_cto_preemptive": {
            "trigger_phase": 2, "trigger_condition": "body_discovered_plus_2min",
            "assigned_to": "cto",
            "instruction": {
                "de": "Steh auf. Sag: 'Ich war als letzte im Serverraum. Ich kann das erklaeren.' Dann setz dich — ohne die Erklaerung zu geben. Warte ob jemand nachfragt.",
                "en": "Stand up. Say: 'I was last in the server room. I can explain that.' Then sit — without giving the explanation. Wait to see if anyone asks.",
            }, "game_effect": "cto_statement"
        },

        "task_recorder_out": {
            "trigger_phase": 1, "trigger_condition": "game_started_8min",
            "assigned_to": "journalist",
            "instruction": {
                "de": "Leg dein 'Aufnahmegeraet' (einen Stift oder dein Handy) demonstrativ auf den Tisch. Wenn jemand fragt ob du aufnimmst: 'Kommt darauf an ob ihr etwas Interessantes sagt.'",
                "en": "Place your 'recorder' (a pen or your phone) demonstratively on the table. If asked if you're recording: 'Depends on whether you say something interesting.'",
            }, "game_effect": "recorder_visible"
        },

        "task_finn_usb": {
            "trigger_phase": 1, "trigger_condition": "game_started_5min",
            "assigned_to": "ex_partner",
            "instruction": {
                "de": "Wenn dich jemand anspricht: 'Ich war nicht eingeladen. Aber ich habe ein Recht hier zu sein.' Zeig den USB-Stick kurz. Wenn gefragt was drauf ist: 'Alles.' Steck ihn weg.",
                "en": "When someone speaks to you: 'I was not invited. But I have a right to be here.' Briefly show the USB stick. If asked what's on it: 'Everything.' Put it away.",
            }, "game_effect": "usb_noticed"
        },

        "task_burner_phone_show": {
            "trigger_phase": 1, "trigger_condition": "game_started_6min",
            "assigned_to": "hacker",
            "instruction": {
                "de": "Halte das Burner-Handy (Zettel) sichtbar in der Hand — aber zeig es niemandem. Wenn jemand fragt was das ist: 'Nichts.' Wenn jemand es sehen will: 'Nein.'",
                "en": "Hold the burner phone (note) visibly in your hand — but show it to nobody. If asked what it is: 'Nothing.' If someone wants to see it: 'No.'",
            }, "game_effect": "burner_phone_visible"
        },

        "task_pitch_deck_empty": {
            "trigger_phase": 2, "trigger_condition": "investigation_begins",
            "assigned_to": "investor_lead",
            "instruction": {
                "de": "Geh zum Pitch-Deck-Umschlag. Oeffne ihn. Schau hinein. Dreh dich um. Sag laut: 'Das Pitch Deck. Es ist weg.' Zeige den leeren Umschlag. Wer reagiert nervoes?",
                "en": "Go to the pitch deck envelope. Open it. Look inside. Turn around. Say aloud: 'The pitch deck. It is gone.' Show the empty envelope. Who reacts nervously?",
            }, "game_effect": "pitch_deck_theft_revealed"
        },

        "task_laptop_message": {
            "trigger_phase": 2, "trigger_condition": "body_discovered_plus_5min",
            "assigned_to": "detective",
            "instruction": {
                "de": "Geh zum 'Laptop' (Zettel). Lies vor: 'Bildschirm gesperrt. Letzte Aktion: Datei geloescht 21:47. Auf einem Post-it: Ich weiss was du getan hast.' Dann: 'Das ist keine zufaellige Nachricht.'",
                "en": "Go to the 'laptop' (note). Read aloud: 'Screen locked. Last action: file deleted 9:47pm. On a Post-it: I know what you did.' Then: 'That is not a random message.'",
            }, "game_effect": "laptop_message_revealed"
        },

        "task_slack_log_read": {
            "trigger_phase": 2, "trigger_condition": "investigation_5min",
            "assigned_to": "cofounder",
            "instruction": {
                "de": "Hole den Slack-Log-Zettel heraus. Lies laut vor: '#general, 21:04 Magnus: Wir muessen reden. Alle. Serverraum. Jetzt. 21:09 Magnus: Ich weiss wer es war.' Dann leg ihn weg.",
                "en": "Take out the Slack log note. Read aloud: '#general, 9:04pm Magnus: We need to talk. Everyone. Server room. Now. 9:09pm Magnus: I know who it was.' Then put it away.",
            }, "game_effect": "slack_log_revealed"
        },

        "task_phones_on_table": {
            "trigger_phase": 2, "trigger_condition": "investigation_10min",
            "assigned_to": "detective",
            "instruction": {
                "de": "Steh auf. Sag: 'Alle Handys. Auf den Tisch. Jetzt. Ich sage nicht dass ich sie durchsuche. Ich sage nur: Wer sein Handy versteckt hat etwas zu verbergen.' Warte 10 Sekunden.",
                "en": "Stand up. Say: 'All phones. On the table. Now. I'm not saying I will search them. I'm just saying: whoever hides their phone has something to hide.' Wait 10 seconds.",
            }, "game_effect": "phone_check"
        },

        "task_secret_vote": {
            "trigger_phase": 2, "trigger_condition": "midgame_20min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle schreiben auf einen Zettel: Wer war heute Abend im Serverraum? Falten. Dem Host geben. Kein Ergebnis — aber der Vergleich am Ende wird interessant.",
                "en": "Everyone writes on a note: who was in the server room tonight? Fold. Give to host. No result — but the comparison at the end will be interesting.",
            }, "game_effect": "server_room_vote"
        },

        "task_designer_photo": {
            "trigger_phase": 2, "trigger_condition": "investigation_12min",
            "assigned_to": "designer",
            "instruction": {
                "de": "Du hast das Foto. Jetzt ist der Moment. Zeigst du es — oder wartest du noch? Je laenger du wartest desto mehr Details koennten verloren gehen. Aber je frueher du es zeigst desto mehr koennte jemand luegen was er sieht.",
                "en": "You have the photo. Now is the moment. Do you show it — or wait? The longer you wait the more details might be lost. But the earlier you show it the more someone might lie about what they see.",
            }, "game_effect": "designer_photo_decision"
        },

        "task_all_silence": {
            "trigger_phase": 2, "trigger_condition": "random_investigation",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Host sagt: 'Alle Notifications aus. 30 Sekunden keine Geraeusche.' Stille. Dann sagt jeder einen Satz was er in dieser Stille gedacht hat.",
                "en": "Host says: 'All notifications off. 30 seconds no sounds.' Silence. Then everyone says one sentence about what they thought in this silence.",
            }, "game_effect": "digital_silence"
        },

        "task_post_social": {
            "trigger_phase": 2, "trigger_condition": "pr_wants_to_act",
            "assigned_to": "pr_manager",
            "instruction": {
                "de": "Du kannst jetzt deinen Social Media Post nutzen. Steh auf. Sag: 'Ich poste jetzt etwas.' Lies dann laut vor was du 'postest'. Es gilt als oeffentlich. Wahr oder falsch — deine Entscheidung.",
                "en": "You can use your Social Media Post now. Stand up. Say: 'I am posting something now.' Then read aloud what you 'post'. It counts as public. True or false — your decision.",
            }, "game_effect": "social_post_made"
        },

        # ── TRINK-AUFGABEN (10 Stueck) ────────────────────────────────────────

        "task_first_champagner": {
            "trigger_phase": 1, "trigger_condition": "game_started_3min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle heben das Glas. Lead-Investorin sagt: 'Auf NovaTech AI und auf Magnus Frey.' Alle trinken gleichzeitig. Wer zoegert? Wer trinkt am meisten?",
                "en": "Everyone raises their glass. Lead investor says: 'To NovaTech AI and to Magnus Frey.' Everyone drinks simultaneously. Who hesitates? Who drinks the most?",
            }, "game_effect": "first_toast_reactions"
        },

        "task_murderer_drinks_first": {
            "trigger_phase": 1, "trigger_condition": "opening_toast",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Beim ersten Toast: Trinke als ERSTER und demonstrativ viel. Du hast keine Angst vor dem Champagner. Das klingt unschuldig. Das soll so klingen.",
                "en": "At the first toast: drink FIRST and demonstratively much. You have no fear of the champagne. That sounds innocent. It is meant to.",
            }, "game_effect": "murderer_drinks_first"
        },

        "task_group_drink_silicon": {
            "trigger_phase": 2, "trigger_condition": "investigation_10min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Host sagt: 'Silicon-Valley-Tradition — wenn ein Deal platzt, trinkt man trotzdem.' Alle trinken gleichzeitig. Wer NICHT trinkt hat etwas im Kopf das ihn ablenkt.",
                "en": "Host says: 'Silicon Valley tradition — when a deal falls through, you drink anyway.' Everyone drinks simultaneously. Whoever does NOT drink has something on their mind.",
            }, "game_effect": "group_drink"
        },

        "task_kai_drinks_fast": {
            "trigger_phase": 1, "trigger_condition": "game_started_7min",
            "assigned_to": "angel_investor",
            "instruction": {
                "de": "Trink jetzt schnell — zu schnell. Dann bestell nach. Wenn jemand fragt: 'Langer Abend.' Das faellt auf. Das soll auffallen.",
                "en": "Drink quickly now — too quickly. Then order another. If asked: 'Long evening.' This will be noticed. It is meant to be.",
            }, "game_effect": "kai_nervous_drinking"
        },

        "task_journalist_wine_clue": {
            "trigger_phase": 2, "trigger_condition": "random_post_murder",
            "assigned_to": "journalist",
            "instruction": {
                "de": "Hebe dein Glas. Sag ohne Einleitung: 'Magnus hatte heute Abend einen Kaffee auf seinem Schreibtisch. Wer hat ihm den gebracht? Das frage ich mich.'",
                "en": "Raise your glass. Say without preamble: 'Magnus had a coffee on his desk tonight. Who brought it to him? That is what I am wondering.'",
            }, "game_effect": "coffee_attention"
        },

        "task_ronja_no_drink": {
            "trigger_phase": 1, "trigger_condition": "first_toast",
            "assigned_to": "hacker",
            "instruction": {
                "de": "Beim ersten Toast: Trinke NICHT. Wenn jemand fragt: 'Ich trinke nie auf der Arbeit.' Wenn jemand darauf besteht: 'Heute bin ich auf der Arbeit.'",
                "en": "At the first toast: do NOT drink. If asked: 'I never drink on the job.' If someone insists: 'Tonight I am on the job.'",
            }, "game_effect": "hacker_no_drink"
        },

        "task_investor_drinks_toast2": {
            "trigger_phase": 2, "trigger_condition": "investigation_20min",
            "assigned_to": "investor_lead",
            "instruction": {
                "de": "Fuelle nochmals Glaeser nach — aber nur bestimmten Personen. Geh zu zwei die du verdaechtigst. Schau ihnen dabei in die Augen.",
                "en": "Refill glasses — but only for specific people. Go to two you suspect. Look them in the eyes while doing so.",
            }, "game_effect": "investor_selection"
        },

        "task_last_drink_magnus": {
            "trigger_phase": 3, "trigger_condition": "reckoning_near",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle trinken nochmals. Auf Magnus Frey — wer auch immer ihn getoedet hat. Wer nicht trinkt ehrt ihn nicht. Wer zu schnell trinkt hat ein schlechtes Gewissen.",
                "en": "Everyone drinks once more. To Magnus Frey — whoever killed him. Whoever does not drink does not honour him. Whoever drinks too quickly has a guilty conscience.",
            }, "game_effect": "final_drink"
        },

        "task_finn_whisky": {
            "trigger_phase": 2, "trigger_condition": "random_25min",
            "assigned_to": "ex_partner",
            "instruction": {
                "de": "Bestell einen Whisky — pur, kein Eis. Sag laut: 'Magnus hat immer Whisky getrunken wenn er jemanden rausgeworfen hat. Ich weiss das aus Erfahrung.'",
                "en": "Order a whisky — neat, no ice. Say aloud: 'Magnus always drank whisky when he fired someone. I know that from experience.'",
            }, "game_effect": "finn_whisky_comment"
        },

        "task_champagner_clue": {
            "trigger_phase": 2, "trigger_condition": "random_30min",
            "assigned_to": "random",
            "instruction": {
                "de": "Trinke demonstrativ. Sage dann: 'Der Champagner schmeckt gut. Magnus' Kaffee soll heute Abend anders geschmeckt haben — laut jemandem der dabei war.' Beobachte wer aufhorcht.",
                "en": "Drink demonstratively. Then say: 'The champagne tastes good. Magnus' coffee is said to have tasted different tonight — according to someone who was there.' Observe who perks up.",
            }, "game_effect": "coffee_taste_clue"
        },

        # ── KETTENAUFGABEN (12 Stueck) ─────────────────────────────────────────

        "chain_a1_journalist_cto": {
            "trigger_phase": 2, "trigger_condition": "ai_fraud_mentioned",
            "assigned_to": "journalist",
            "instruction": {
                "de": "Geh zur CTO. Sag leise aber hoerbar: 'Ich weiss dass die KI kein echtes Sprachmodell ist. Ich kann das beweisen. Sie koennten mir helfen — oder ich veroeffentliche es ohne Ihre Seite der Geschichte.'",
                "en": "Go to the CTO. Say quietly but audibly: 'I know the AI is not a real language model. I can prove it. You could help me — or I publish it without your side of the story.'",
            }, "game_effect": "chain_journalist_cto",
            "triggers_chain": "chain_a2_cto_response"
        },

        "chain_a2_cto_response": {
            "trigger_phase": 2, "trigger_condition": "journalist_confronts_cto",
            "assigned_to": "cto",
            "instruction": {
                "de": "Der Journalist konfrontiert dich. Entscheide: Kooperiere ('Ich erklaere dir was wirklich passiert ist') oder weise ihn ab. Beide Optionen haben Konsequenzen.",
                "en": "The journalist confronts you. Decide: cooperate ('I will explain what really happened') or reject him. Both options have consequences.",
            }, "game_effect": "cto_journalist_decision"
        },

        "chain_b1_designer_shows": {
            "trigger_phase": 2, "trigger_condition": "investigation_15min",
            "assigned_to": "designer",
            "instruction": {
                "de": "Zeige jetzt das Foto — oder sag 'Ich zeige es noch nicht.' Wenn du es zeigst: Gib es dem Host der es rumzeigt. Alle sagen was sie sehen. Wer luegt?",
                "en": "Show the photo now — or say 'I am not showing it yet.' If you show it: give it to the host who shows it around. Everyone says what they see. Who lies?",
            }, "game_effect": "chain_designer_photo",
            "triggers_chain": "chain_b2_murderer_reacts_photo"
        },

        "chain_b2_murderer_reacts_photo": {
            "trigger_phase": 2, "trigger_condition": "photo_shown",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Das Foto wird herumgegeben. Wenn du dran bist: Sage was du siehst — aber sag etwas anderes als was wirklich drauf ist. Oder sage die Wahrheit und erklaere warum du deinen Namen auf einem Laptop haettest sehen sollen.",
                "en": "The photo is being passed around. When it's your turn: say what you see — but say something different from what is really on it. Or tell the truth and explain why you would have seen your name on a laptop.",
            }, "game_effect": "murderer_photo_reaction"
        },

        "chain_c1_cofounder_slack": {
            "trigger_phase": 2, "trigger_condition": "cofounder_under_pressure",
            "assigned_to": "cofounder",
            "instruction": {
                "de": "Lies jetzt einen Slack-Log vor — du entscheidest welchen (echt oder manipuliert). Aber: Was auch immer du vorliest gilt als offiziell im Spiel.",
                "en": "Read a Slack log now — you decide which (real or manipulated). But: whatever you read aloud counts as officially in the game.",
            }, "game_effect": "chain_cofounder_slack",
            "triggers_chain": "chain_c2_inspector_questions"
        },

        "chain_c2_inspector_questions": {
            "trigger_phase": 2, "trigger_condition": "slack_log_read",
            "assigned_to": "detective",
            "instruction": {
                "de": "Der Co-Founder hat einen Slack-Log vorgelesen. Stelle jetzt GENAU EINE Frage dazu. Nur eine. Praezise. Deine Frage muss zeigen dass du dem Log nicht vollstaendig glaubst.",
                "en": "The co-founder read a Slack log. Now ask EXACTLY ONE question about it. Only one. Precise. Your question must show you don't fully believe the log.",
            }, "game_effect": "inspector_challenges_log"
        },

        "chain_d1_hacker_pressured": {
            "trigger_phase": 2, "trigger_condition": "pitch_deck_discussed",
            "assigned_to": "hacker",
            "instruction": {
                "de": "Du wirst unter Druck gesetzt. Jemand will das Burner-Handy sehen. Entscheide: Zeig es (riskant aber aufklaerend) oder weigere dich (verdaechtiger aber sicherer).",
                "en": "You are being put under pressure. Someone wants to see the burner phone. Decide: show it (risky but clarifying) or refuse (more suspicious but safer).",
            }, "game_effect": "chain_hacker_burner",
            "triggers_chain": "chain_d2_client_nervous"
        },

        "chain_d2_client_nervous": {
            "trigger_phase": 2, "trigger_condition": "burner_phone_shown",
            "assigned_to": "hacker_client",
            "instruction": {
                "de": "Das Burner-Handy wurde gezeigt oder diskutiert. Du bist derjenige der die Hackerin beauftragt hat. Reagiere jetzt — aber nicht zu offensichtlich. Eine kleine Reaktion. Eine Mikrogeste.",
                "en": "The burner phone was shown or discussed. You are the one who hired the hacker. React now — but not too obviously. A small reaction. A microgesture.",
            }, "game_effect": "client_nervous_reaction"
        },

        "chain_e1_investor_lawyer": {
            "trigger_phase": 2, "trigger_condition": "contract_discussed",
            "assigned_to": "lawyer",
            "instruction": {
                "de": "Geh zur Lead-Investorin. Sag leise: 'Seite 47. Lesen Sie Seite 47.' Mehr nicht. Setz dich wieder. Lass sie reagieren.",
                "en": "Go to the lead investor. Say quietly: 'Page 47. Read page 47.' Nothing more. Sit back down. Let her react.",
            }, "game_effect": "chain_lawyer_investor",
            "triggers_chain": "chain_e2_investor_clause"
        },

        "chain_e2_investor_clause": {
            "trigger_phase": 2, "trigger_condition": "lawyer_hints_page47",
            "assigned_to": "investor_lead",
            "instruction": {
                "de": "Der Anwalt hat dich auf Seite 47 hingewiesen. Du weisst was dort steht. Entscheide: Sage es oeffentlich ('Da ist eine Klausel...') oder tue als hast du es nicht gehoert.",
                "en": "The lawyer pointed you to page 47. You know what is there. Decide: say it publicly ('There is a clause...') or pretend you didn't hear.",
            }, "game_effect": "investor_clause_decision"
        },

        "chain_f1_questioning": {
            "trigger_phase": 2, "trigger_condition": "investigation_midpoint",
            "assigned_to": "detective",
            "instruction": {
                "de": "Ruf jetzt die offizielle Befragung aus. Alle verlassen den Raum. Du redest 3 Minuten allein mit einer Person. Danach sagen alle ob sie kooperativ war.",
                "en": "Call the official questioning now. Everyone leaves the room. You talk alone with one person for 3 minutes. Afterwards everyone says if they were cooperative.",
            }, "game_effect": "interrogation_called",
            "triggers_chain": "chain_f2_post_questioning"
        },

        "chain_f2_post_questioning": {
            "trigger_phase": 2, "trigger_condition": "interrogation_done",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Die Inspektor kehrt zurueck. Jeder sagt nacheinander: War die befragte Person 'kooperativ' oder 'ausweichend'? Kein Herumreden. Ein Satz.",
                "en": "The inspector returns. Everyone says in turn: was the questioned person 'cooperative' or 'evasive'? No talking around it. One sentence.",
            }, "game_effect": "post_questioning"
        },

        # ── MOERDER-AUFGABEN (8 Stueck) ────────────────────────────────────────

        "murderer_task_alibi_server": {
            "trigger_phase": 2, "trigger_condition": "murder_announced",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Wenn nach dem Serverraum gefragt wird: Du warst NICHT dort. Erklaere spontan und praezise wo du stattdessen warst — mit einer Person als Zeugen (ohne vorher zu fragen).",
                "en": "When the server room is discussed: you were NOT there. Explain spontaneously and precisely where you were instead — with one person as witness (without asking first).",
            }, "game_effect": "murderer_alibi"
        },

        "murderer_task_pitch_distraction": {
            "trigger_phase": 2, "trigger_condition": "pitch_deck_theft_discussed",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Lenke auf den Pitch-Deck-Diebstahl als separates Verbrechen. 'Vielleicht war die Hackerin auch der Moerder?' Das ist falsch — aber klingt logisch.",
                "en": "Redirect to the pitch deck theft as a separate crime. 'Maybe the hacker was also the murderer?' This is wrong — but sounds logical.",
            }, "game_effect": "red_herring_hacker"
        },

        "murderer_task_sympathy": {
            "trigger_phase": 2, "trigger_condition": "death_confirmed",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Reagiere mit uebertriebener Betroffenheit. 'Magnus war mehr als ein Chef — er war...' Lass den Satz offen. Emotionen wirken echt wenn alle unter Schock stehen.",
                "en": "React with exaggerated distress. 'Magnus was more than a boss — he was...' Leave the sentence open. Emotions seem real when everyone is in shock.",
            }, "game_effect": "murderer_sympathy"
        },

        "murderer_task_question": {
            "trigger_phase": 2, "trigger_condition": "investigation_5min",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Stelle eine Frage die Verdacht ablenkt. Gut: 'Wer hatte heute Abend Zugang zur Gast-Chip-Karte?' Oder: 'Wer wusste wann Magnus allein im Serverraum war?'",
                "en": "Ask a question that deflects suspicion. Good: 'Who had access to the guest chip card tonight?' Or: 'Who knew when Magnus was alone in the server room?'",
            }, "game_effect": "murderer_deflection"
        },

        "murderer_task_helps": {
            "trigger_phase": 3, "trigger_condition": "investigation_later",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Hilf der Inspektor aktiv. 'Sollten wir die Chip-Karten-Zugangsliste systematisch durchgehen?' Wer bei der Aufklaerung hilft steht nicht im Verdacht.",
                "en": "Actively help the inspector. 'Should we systematically go through the chip card access list?' Whoever helps the investigation is not suspected.",
            }, "game_effect": "murderer_helper"
        },

        "murderer_task_accuse": {
            "trigger_phase": 3, "trigger_condition": "suspicion_rising_on_murderer",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Beschuldige jetzt konkret eine andere Person mit einem wahren Detail das du weisst. Schaffe Chaos. Je mehr gleichzeitig redet desto besser fuer dich.",
                "en": "Concretely accuse another person now with a true detail you know. Create chaos. The more everyone talks simultaneously the better for you.",
            }, "game_effect": "murderer_accusation"
        },

        "murderer_task_designer": {
            "trigger_phase": 2, "trigger_condition": "designer_about_to_show_photo",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Jess will das Foto zeigen. Handle zuerst. Geh zu ihr. Sag leise: 'Das Foto ist unscharf. Du weisst selbst nicht was drauf ist. Moechtest du jemanden falsch beschuldigen?'",
                "en": "Jess wants to show the photo. Act first. Go to her. Say quietly: 'The photo is blurry. You yourself don't know what is on it. Do you want to falsely accuse someone?'",
            }, "game_effect": "murderer_doubts_designer"
        },

        "murderer_panic": {
            "trigger_phase": 3, "trigger_condition": "someone_gets_close",
            "assigned_to": "murderer", "private": True,
            "time_limit_seconds": 60,
            "instruction": {
                "de": "PANIKMOMENT — 60 SEKUNDEN — NUR FUER DICH:\n\nA — ALIBI: Bekraeftige deinen Zeugen nochmals. Direkt. Persoenlich.\n\nB — DER LAPTOP: 'Die Nachricht auf dem Laptop war schon da als ich ankam. Magnus war bereits tot.'\n\nC — DIE HACKERIN: 'Die Hackerin war im Serverraum. Sie hat das Pitch Deck gestohlen. Warum nicht auch mehr?'\n\nD — EMOTIONEN: Werde emotional. Lass es aus dir heraus. Niemand verdaechtigt jemanden der wirklich bewegt scheint.\n\nE — GEGENANKLAGE: Beschuldige sofort jemand anderen mit einem echten Detail. Kein Zoegern.\n\n60 Sekunden. Jetzt.",
                "en": "PANIC MOMENT — 60 SECONDS — ONLY FOR YOU:\n\nA — ALIBI: Reinforce your witness once more. Directly. Personally.\n\nB — THE LAPTOP: 'The message on the laptop was already there when I arrived. Magnus was already dead.'\n\nC — THE HACKER: 'The hacker was in the server room. She stole the pitch deck. Why not more?'\n\nD — EMOTIONS: Become emotional. Let it out. Nobody suspects someone who seems truly moved.\n\nE — COUNTER-ACCUSATION: Immediately accuse someone else with a real detail. No hesitation.\n\n60 seconds. Now.",
            }, "game_effect": "panic_triggered"
        },

        # ── STANDARD-AUFGABEN ──────────────────────────────────────────────

        "task_lawyer_dense_answer": {
            "trigger_phase": 1, "trigger_condition": "game_started_10min",
            "assigned_to": "lawyer",
            "instruction": {
                "de": "Wenn dich jemand direkt fragt: Antworte immer mit 'Das kommt darauf an...' — und dann einem langen juristischen Satz. Wenn jemand sagt 'Ja oder Nein?': 'Das ist rechtlich nicht so einfach.'",
                "en": "When someone asks you directly: always answer with 'That depends...' — then a long legal sentence. If someone says 'Yes or no?': 'That is not legally straightforward.'",
            }, "game_effect": "lawyer_behavior"
        },

        "task_finn_sits_wrong": {
            "trigger_phase": 1, "trigger_condition": "game_started_4min",
            "assigned_to": "ex_partner",
            "instruction": {
                "de": "Setze dich nicht an den Haupttisch. Setze dich an den Rand. Wenn jemand sagt du sollst an den Tisch kommen: 'Ich bin hier wo ich bin.' Bleib am Rand.",
                "en": "Do not sit at the main table. Sit at the edge. If someone says you should come to the table: 'I am where I am.' Stay at the edge.",
            }, "game_effect": "finn_edge_behavior"
        },

        "task_kai_bathroom": {
            "trigger_phase": 1, "trigger_condition": "game_started_12min",
            "assigned_to": "angel_investor",
            "instruction": {
                "de": "Steh jetzt auf. Sag: 'Kurz Luft holen.' Geh fuer 2 Minuten aus dem Raum (Toilette oder Flur). Komm zurueck und sag nichts darueber.",
                "en": "Stand up now. Say: 'Getting some air.' Leave the room for 2 minutes (bathroom or hallway). Return and say nothing about it.",
            }, "game_effect": "kai_leaves_first_time"
        },

        "task_pr_three_phones": {
            "trigger_phase": 1, "trigger_condition": "game_started_9min",
            "assigned_to": "pr_manager",
            "instruction": {
                "de": "Lege demonstrativ alle drei deiner 'Handys' (Zettel oder echte Handys) auf den Tisch. Wenn jemand fragt warum drei: 'Arbeit. Privat. Krisenmanagement.' Schweig danach.",
                "en": "Demonstratively place all three of your 'phones' (notes or real phones) on the table. If asked why three: 'Work. Private. Crisis management.' Silence afterwards.",
            }, "game_effect": "three_phones_noticed"
        },

        "task_detective_voice_note": {
            "trigger_phase": 2, "trigger_condition": "investigation_8min",
            "assigned_to": "detective",
            "instruction": {
                "de": "Mache eine Sprachnotiz auf deinem Telefon — sichtbar fuer alle. Sag dabei laut: 'Person X verhielt sich auffaellig als das Pitch Deck erwaehnt wurde.' Lass alle hoeren dass du aufnimmst.",
                "en": "Make a voice note on your phone — visible to everyone. Say aloud: 'Person X behaved strangely when the pitch deck was mentioned.' Let everyone hear you're recording.",
            }, "game_effect": "voice_note_made"
        },

        "task_all_alibis": {
            "trigger_phase": 2, "trigger_condition": "investigation_25min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle nennen nochmals wo sie zwischen 21:30 und 22:00 Uhr waren. Eine Aussage. Kein Herumreden. Die Inspektor schreibt es auf.",
                "en": "Everyone states once more where they were between 9:30 and 10pm. One statement. No talking around it. The inspector writes it down.",
            }, "game_effect": "alibi_round"
        },

        "task_finn_usb_pressure": {
            "trigger_phase": 2, "trigger_condition": "usb_stake_high",
            "assigned_to": "ex_partner",
            "instruction": {
                "de": "Der Druck steigt. Zeigst du jetzt den USB-Stick? Wenn ja: Steh auf. Sag: 'Ich habe den Originalcode von NovaTech. Aus dem Jahr 2018. Mit meinem Namen drin.' Dann zeig den Zettel.",
                "en": "The pressure is rising. Do you show the USB stick now? If yes: Stand up. Say: 'I have the original code from NovaTech. From 2018. With my name in it.' Then show the note.",
            }, "game_effect": "usb_revealed"
        },

        # ── ZUFALLS-MOMENTE (9 Stueck) ────────────────────────────────────────

        "random_notification_sound": {
            "trigger_phase": 2, "trigger_condition": "random_any_time",
            "assigned_to": "random",
            "instruction": {
                "de": "Lass dein Telefon kurz klingeln oder vibrieren. Schau drauf. Reagiere mit einem kurzen Gesichtsausdruck — Ueberraschung, Sorge, oder Erleichterung. Dann weg damit.",
                "en": "Let your phone briefly ring or vibrate. Look at it. React with a brief expression — surprise, worry, or relief. Then put it away.",
            }, "game_effect": "mystery_notification"
        },

        "random_server_alarm": {
            "trigger_phase": 2, "trigger_condition": "random_post_murder",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Host sagt: 'Der Server-Alarm geht los. Ein System-Alert. Jemand versucht gerade sich remote einzuloggen.' 10 Sekunden Stille. Wer schaut auf sein Telefon?",
                "en": "Host says: 'The server alarm goes off. A system alert. Someone is trying to log in remotely right now.' 10 seconds silence. Who looks at their phone?",
            }, "game_effect": "server_alarm"
        },

        "random_wifi_drops": {
            "trigger_phase": 2, "trigger_condition": "atmosphere_trigger",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Host sagt: 'Das WLAN des Buerogebaeudes wurde deaktiviert. Niemand kann mehr Daten hochladen. Oder herunterladen.' Pause. Wer wird nervoes?",
                "en": "Host says: 'The building's WiFi has been deactivated. Nobody can upload or download data.' Pause. Who gets nervous?",
            }, "game_effect": "wifi_down"
        },

        "random_phone_call": {
            "trigger_phase": 2, "trigger_condition": "random_investigation",
            "assigned_to": "random",
            "instruction": {
                "de": "Tu als ob dein Telefon klingelt. Nimm ab. Sag nur: 'Ja. Ich verstehe. Ich rufe zurueck.' Leg auf. Wenn gefragt wer das war: 'Mein Anwalt.' Oder: 'Jemand.'",
                "en": "Pretend your phone is ringing. Answer. Say only: 'Yes. I understand. I will call back.' Hang up. If asked who it was: 'My lawyer.' Or: 'Someone.'",
            }, "game_effect": "mystery_call"
        },

        "random_lights_flicker": {
            "trigger_phase": 2, "trigger_condition": "atmosphere_trigger_2",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Licht kurz aus (2-3 Sekunden) und wieder an. Der Host sagt: 'Der Server-Shutdown hat das Stromnetz kurz ueberlastet.' Wer bewegt sich in der Dunkelheit?",
                "en": "Light briefly off (2-3 seconds) and back on. Host says: 'The server shutdown briefly overloaded the grid.' Who moves in the darkness?",
            }, "game_effect": "lights_flicker"
        },

        "random_update_arrives": {
            "trigger_phase": 2, "trigger_condition": "random_30min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Host sagt: 'Ich habe gerade eine anonyme Email erhalten. Abgesendet von einem Temp-Mail-Account. Inhalt: Eine einzige Zahl. 4-7-1-9-3-1.' Was ist das? Wer weiss es?",
                "en": "Host says: 'I just received an anonymous email. Sent from a temp mail account. Content: a single number. 4-7-1-9-3-1.' What is that? Who knows?",
            }, "game_effect": "safe_code_hint"
        },

        "random_police_text": {
            "trigger_phase": 3, "trigger_condition": "reckoning_near",
            "assigned_to": "detective",
            "instruction": {
                "de": "Schau auf dein Telefon. Sag: 'Verstaerkung ist in 20 Minuten hier. Was auch immer hier passiert — entscheidet sich jetzt.' Das erhoeht den Druck auf alle.",
                "en": "Look at your phone. Say: 'Reinforcements are 20 minutes away. Whatever happens here — decides itself now.' This increases pressure on everyone.",
            }, "game_effect": "police_incoming"
        },

        "random_slack_ping": {
            "trigger_phase": 1, "trigger_condition": "game_started_14min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Host sagt: 'Auf eurem Slack-Kanal erscheint gerade eine neue Nachricht von einem geloeschten Account: Nur ein Emoji. Ein Auge.' Wer hat einen geloeschten Account?",
                "en": "Host says: 'A new message appears on your Slack channel from a deleted account: just one emoji. An eye.' Who has a deleted account?",
            }, "game_effect": "mysterious_slack_message"
        },

        "random_pre_vote": {
            "trigger_phase": 3, "trigger_condition": "reckoning_soon",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle schreiben auf einen Zettel: Moerder, Pitch-Deck-Dieb, Auftraggeber des Diebs. Drei Antworten. Falten. Dem Host geben. Wird am Ende verglichen.",
                "en": "Everyone writes on a note: murderer, pitch deck thief, person who hired the thief. Three answers. Fold. Give to host. Will be compared at the end.",
            }, "game_effect": "pre_final_vote"
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # 14 VERBINDUNGEN
    # ─────────────────────────────────────────────────────────────────────────
    "role_connections": {
        "investor_cto_fraud": {
            "roles": ["investor_lead", "cto"],
            "connection": "Beide wissen vom KI-Betrug. Beide schwiegen. Aus verschiedenen Gruenden.",
            "tension": "mutual_complicity"
        },
        "cofounder_cto_cameras": {
            "roles": ["cofounder", "cto"],
            "connection": "Beide haben NAS-Zugang. Einer hat die Kameraaufnahmen geloescht. Wer?",
            "tension": "shared_access"
        },
        "designer_murderer_photo": {
            "roles": ["designer", "murderer"],
            "connection": "Jess hat ein Foto von Magnus' Laptop. Darauf: ein Name. Der Moerder weiss nicht was genau drauf ist.",
            "tension": "dramatic_irony"
        },
        "journalist_investor_leak": {
            "roles": ["journalist", "investor_lead"],
            "connection": "Tim bekam anonym Dokumente. Von wem? Dr. Chen hat Motive — und Dokumente.",
            "tension": "suspected_source"
        },
        "pr_cofounder_affair": {
            "roles": ["pr_manager", "cofounder"],
            "connection": "Leon wusste von der Affaere zwischen Magnus und Lara. Er schwieg. Das war sein Druckmittel.",
            "tension": "leverage"
        },
        "hacker_cto_hired": {
            "roles": ["hacker", "cto"],
            "connection": "Jemand hat Ronja beauftragt. Die CTO hatte Motiv und Mittel. Und sie weiss wo das Pitch Deck inhaltlich luegt.",
            "tension": "suspected_employer"
        },
        "lawyer_investor_clause": {
            "roles": ["lawyer", "investor_lead"],
            "connection": "Dr. Chen hat den Vertrag unterschrieben ohne Seite 47 zu lesen. Jonas weiss es. Und er haelt die Klappe.",
            "tension": "one_sided_knowledge"
        },
        "inspector_cofounder_brother": {
            "roles": ["detective", "cofounder"],
            "connection": "Ninas Bruder arbeitet bei NovaTech. Er ist Ninas inoffizielle Quelle. Er weiss es nicht.",
            "tension": "dramatic_irony"
        },
        "expartner_journalist_code": {
            "roles": ["ex_partner", "journalist"],
            "connection": "Finn hat den Originalcode. Tim braucht einen Insider-Beweis. Zusammen waeren sie gefaehrlich.",
            "tension": "potential_alliance"
        },
        "kai_lawyer_exit": {
            "roles": ["angel_investor", "lawyer"],
            "connection": "Kais Exit-Vertrag laeuft ueber Jonas' Buero. Jonas weiss von Kais finanzieller Situation. Kai weiss es nicht.",
            "tension": "one_sided_leverage"
        },
        "murderer_designer_unknowing": {
            "roles": ["murderer", "designer"],
            "connection": "Der Moerder weiss nicht was genau auf Jess' Foto ist. Jess weiss nicht dass der Name auf dem Foto sie zur wichtigsten Zeugin macht.",
            "tension": "mutual_ignorance"
        },
        "pr_hacker_server_room": {
            "roles": ["pr_manager", "hacker"],
            "connection": "Beide waren im Serverraum — zu verschiedenen Zeiten. Keiner weiss vom anderen. Ronja war nach dem Tod dort. Lara vorher.",
            "tension": "timeline_overlap"
        },
        "investor_expartner_code": {
            "roles": ["investor_lead", "ex_partner"],
            "connection": "Dr. Chen investierte in NovaTech obwohl sie wusste dass die Kernidee moeglicherweise gestohlen war. Finn weiss das noch nicht.",
            "tension": "investor_liability"
        },
        "journalist_detective_parallel": {
            "roles": ["journalist", "detective"],
            "connection": "Tim recherchiert. Nina observiert. Beide wollen dasselbe herausfinden. Beide aus verschiedenen Gruenden. Kooperation koennte beiden nuetzen — oder beiden schaden.",
            "tension": "parallel_investigation"
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # EREIGNISKETTEN (7 Stueck)
    # ─────────────────────────────────────────────────────────────────────────
    "event_chains": [
        {
            "id": "chain_photo_pressure",
            "trigger": "photo_shown",
            "message_to_murderer": {
                "de": "Das Foto wird herumgegeben. Was sieht die Person die am genauesten hinschaut? Handle bevor sie es sagt.",
                "en": "The photo is being passed around. What does the person looking most carefully see? Act before they say it.",
            }
        },
        {
            "id": "chain_slack_exposed",
            "trigger": "slack_export_shown",
            "message_to_all": {
                "de": "Der Slack-Export liegt auf dem Tisch. Darin: alle Nachrichten von heute Abend. Wer hat etwas zu verbergen?",
                "en": "The Slack export is on the table. Inside: all messages from tonight. Who has something to hide?",
            }
        },
        {
            "id": "chain_wifi_reactivated",
            "trigger": "wifi_restored",
            "message_to_hacker": {
                "de": "Das WLAN ist wieder aktiv. Der Upload ist abgeschlossen — oder wird er es? Du hast 2 Minuten um dich zu entscheiden.",
                "en": "The WiFi is back. The upload is complete — or will it be? You have 2 minutes to decide.",
            }
        },
        {
            "id": "chain_clause_revealed",
            "trigger": "clause_12b_mentioned",
            "message_to_all": {
                "de": "Klausel 12b ist bekannt. Magnus' Tod macht jemanden in diesem Raum zum Hauptnutzniesser. Wer?",
                "en": "Clause 12b is known. Magnus' death makes someone in this room the main beneficiary. Who?",
            }
        },
        {
            "id": "chain_ai_exposed",
            "trigger": "ai_fakery_confirmed",
            "message_to_cto": {
                "de": "Der KI-Betrug ist oeffentlich. Jetzt entscheidet sich ob du Teil des Problems oder Teil der Loesung bist. Noch ist es nicht zu spaet.",
                "en": "The AI fraud is public. Now it is decided whether you are part of the problem or part of the solution. It is not too late yet.",
            }
        },
        {
            "id": "chain_finn_ultimatum",
            "trigger": "usb_stick_shown",
            "message_to_all": {
                "de": "Finn hat den Originalcode. Wenn das echt ist — dann ist NovaTechs Kernprodukt auf gestohlener Arbeit gebaut. Das veraendert alles.",
                "en": "Finn has the original code. If this is real — then NovaTech's core product is built on stolen work. That changes everything.",
            }
        },
        {
            "id": "chain_police_coming",
            "trigger": "two_hours_left",
            "message_to_murderer": {
                "de": "In weniger als zwei Stunden kommt die echte Polizei. Was bis dahin nicht geklaert ist — klaert sich anders.",
                "en": "In less than two hours the real police arrive. What is not resolved by then — resolves itself differently.",
            }
        }
    ],

    # ─────────────────────────────────────────────────────────────────────────
    # ATMOSPHAEREN-NACHRICHTEN
    # ─────────────────────────────────────────────────────────────────────────
    "atmosphere_messages": [
        {"trigger": "game_start_immediately", "text": {
            "de": "Berlin, 2024. Rooftop-Bar, 9. Etage. Champagner. 50 Millionen. Und dann: ein Schrei aus dem Serverraum.",
            "en": "Berlin, 2024. Rooftop bar, 9th floor. Champagne. 50 million. And then: a scream from the server room."}},
        {"trigger": "investigation_begins", "text": {
            "de": "Das Pitch Deck ist weg. Der Laptop ist gesperrt. Und jemand in diesem Raum war im Serverraum.",
            "en": "The pitch deck is gone. The laptop is locked. And someone in this room was in the server room."}},
        {"trigger": "investigation_10min", "text": {
            "de": "Die KI war kein Sprachmodell. Der Deal war Betrug. Und Magnus wusste es alles.",
            "en": "The AI was not a language model. The deal was fraud. And Magnus knew all of it."}},
        {"trigger": "investigation_20min", "text": {
            "de": "In zwei Stunden kommt die echte Polizei. Was bis dahin nicht geklaert ist — klaert sich anders.",
            "en": "In two hours the real police arrive. What is not resolved by then — resolves itself differently."}},
        {"trigger": "tension_high", "text": {
            "de": "50 Millionen Euro. Eine tote KI-Demo. Ein toter CEO. Und irgendwo — ein Laptop der noch laeuft.",
            "en": "50 million euros. A dead AI demo. A dead CEO. And somewhere — a laptop still running."}},
        {"trigger": "reckoning_soon", "text": {
            "de": "Noch ein letztes Mal Champagner. Auf die Wahrheit — die immer ans Licht kommt. Auch in Berlin.",
            "en": "One last champagne. To the truth — which always comes to light. Even in Berlin."}}
    ],

    # ─────────────────────────────────────────────────────────────────────────
    # SPIELENDEN (5 Stueck)
    # ─────────────────────────────────────────────────────────────────────────
    "endings": {
        "murderer_caught": {
            "condition": "majority_names_murderer_correctly",
            "title": {"de": "Breaking News", "en": "Breaking News",
                      "fr": "Breaking News", "it": "Breaking News",
                      "es": "Ultima hora", "pt": "Ultima hora"},
            "text": {"de": "Der Moerder wurde entlarvt. TechCrunch wird morgen berichten. NovaTech wird es nicht ueberleben — aber die Wahrheit schon.\n\nGewonnen: Alle die korrekt anklagten.", "en": "The murderer was exposed. TechCrunch will report tomorrow. NovaTech will not survive — but the truth will.\n\nWon: Everyone who correctly accused."}
        },
        "murderer_escapes": {
            "condition": "wrong_person_convicted",
            "title": {"de": "404: Moerder nicht gefunden", "en": "404: Murderer Not Found",
                      "fr": "404: Meurtrier introuvable", "it": "404: Assassino non trovato",
                      "es": "404: Asesino no encontrado", "pt": "404: Assassino nao encontrado"},
            "text": {"de": "Ein Unschuldiger wurde beschuldigt. Der Moerder ist weg — mit dem richtigen Laptop-Passwort und dem richtigen Alibi. {murderer_name} hat gewonnen.", "en": "An innocent was accused. The murderer is gone — with the right laptop password and the right alibi. {murderer_name} has won."}
        },
        "hacker_wins": {
            "condition": "hacker_escapes_with_pitch_deck",
            "title": {"de": "Upload abgeschlossen", "en": "Upload Complete"},
            "text": {"de": "Waehrend alle den Moerder suchten — verschwand das Pitch Deck ins Netz. Die Hackerin hat gewonnen. Das Pitch Deck ist jetzt oeffentlich. NovaTech ist Geschichte.", "en": "While everyone searched for the murderer — the pitch deck disappeared onto the internet. The hacker has won. The pitch deck is now public. NovaTech is history."}
        },
        "journalist_wins": {
            "condition": "journalist_uncovers_everything",
            "title": {"de": "Story des Jahres", "en": "Story of the Year"},
            "text": {"de": "Tim Reuter hat alles aufgedeckt: Moerder, KI-Betrug, Pitch-Deck-Diebstahl, anonymer Informant. TechCrunch wird es als Geschichte des Jahres publishen. Tim hat allein gewonnen.", "en": "Tim Reuter uncovered everything: murderer, AI fraud, pitch deck theft, anonymous informant. TechCrunch will publish it as story of the year. Tim won alone."}
        },
        "finn_vindicated": {
            "condition": "finn_original_idea_acknowledged",
            "title": {"de": "Git Blame", "en": "Git Blame"},
            "text": {"de": "Der Originalcode mit Finns Namen wurde als echt anerkannt. Magnus hat die Kernidee gestohlen. Finn gewinnt — auch ohne den Moerder gefasst zu haben. Die Wahrheit ueber NovaTech ist groesser als ein einzelner Mord.", "en": "The original code with Finn's name was acknowledged as genuine. Magnus stole the core idea. Finn wins — even without the murderer being caught. The truth about NovaTech is bigger than a single murder."}
        }
    }
}
