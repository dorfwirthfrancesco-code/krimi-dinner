# KRIMI DINNER — SZENARIO 03
# "Das Grand Hotel Alpina"
# Zermatt, Schweiz, 1931 — Ein Schneesturm. Ein toter Millionaer. Zehn Verdaechtige.
#
# STATS v1.0:
# - 11 Rollen
# - 63 physische Aufgaben
#   * 8 Moerder-Tasks (privat)
#   * 10 Trink-Tasks
#   * 12 Ketten-Tasks (Rolle A triggert Reaktion bei Rolle B)
#   * 9 Zufalls-Momente
#   * 24 Standard-Aufgaben
# - 35 Hinweise in 8 Ketten
# - 14 Rollenverbindungen
# - 7 Ereignisketten
# - 5 Spielenden
#
# NEUE MECHANIK: Das Zimmer-System
# Jede Rolle hat ein "Zimmer". Physische Besuche, Schluessel, versteckte Objekte.
# Der Safe des Opfers ist das zentrale Objekt — zweites Verbrechen laeuft parallel.

SCENARIO = {
    "id": "alpina",
    "title": "Das Grand Hotel Alpina",
    "min_players": 4,
    "max_players": 11,
    "price": "4.99",
    "description": {
        "de": "Zermatt, 1931. Das Grand Hotel Alpina. Ein Schneesturm schneidet alle vom Rest der Welt ab. Hugo Steinberg, Bankier und Millionaer, wird tot in seinem versperrten Zimmer gefunden. Der Safe ist offen. Das Geld weg. Niemand kann das Hotel verlassen. Und irgendjemand am Tisch war es.",
        "en": "Zermatt, 1931. The Grand Hotel Alpina. A snowstorm cuts everyone off from the rest of the world. Hugo Steinberg, banker and millionaire, is found dead in his locked room. The safe is open. The money gone. Nobody can leave the hotel. And someone at this table did it.",
        "fr": "Zermatt, 1931. Le Grand Hotel Alpina. Une tempete de neige coupe tout le monde du reste du monde. Hugo Steinberg, banquier et millionnaire, est retrouve mort dans sa chambre fermee a cle.",
        "it": "Zermatt, 1931. Il Grand Hotel Alpina. Una tempesta di neve isola tutti dal resto del mondo. Hugo Steinberg, banchiere e milionario, viene trovato morto nella sua stanza chiusa a chiave.",
        "es": "Zermatt, 1931. El Grand Hotel Alpina. Una tormenta de nieve corta a todos del resto del mundo. Hugo Steinberg, banquero y millonario, es encontrado muerto en su habitacion cerrada.",
        "pt": "Zermatt, 1931. O Grand Hotel Alpina. Uma tempestade de neve corta todos do resto do mundo. Hugo Steinberg, banqueiro e milionario, e encontrado morto em seu quarto trancado.",
    },
    "atmosphere": "Schnee. Stille. Das Knistern des Kaminfeuers. Und irgendwo — der Klang eines geleerten Safes.",

    "host_guide": {
        "before_game": {
            "de": [
                "ZIMMERKARTEN: Schreib fuer jede Rolle eine kleine Karte mit 'Zimmer [Nummer]'. Verteile sie mit den Rollenkarten. Jeder hat ein Zimmer.",
                "DER SAFE: Stelle eine Schachtel oder Box als 'Safe' irgendwo im Raum auf. Lege hinein: Ein leeres Kuvert ('Steinbergs Geld'), einen Zettel ('Schuldscheine'), und einen Schluessel.",
                "STEINBERGS ZIMMER: Einen Zettel irgendwo im Raum: 'ZIMMER 12 — TATORT — TUER WAR VON INNEN VERSPERRT'",
                "SCHNEESTURM-HINWEIS: Beim Fenster oder an der Tuer: 'Der Schneesturm haelt an. Niemand kommt raus. Niemand kommt rein.'",
                "DREI SCHLUESSEL: Bereite drei verschiedene Schluessel (oder Zettel mit 'Schluessel') vor — Zimmer 12, Safe, Nebenausgang.",
                "SCHULDBRIEFE: Fuenf Zettel mit 'Schuldschein — [Betrag] CHF — Hugo Steinberg' — verschiedene Betraege (500 bis 50.000)",
                "HOTELREGISTER: Ein Notizbuch als 'Gaestebuch' — alle Gaeste sind eingetragen mit Ankunftszeit",
                "WEIN oder Gluehwein bereitstellen — Schweizer Abend, Kamin, Trinken ist Spielmechanik",
                "Das OPFER spielt NICHT mit — es wird von Anfang an als tot gespielt. Kein Geist-Modus.",
            ]
        },
        "during_game": {
            "de": [
                "Der Schneesturm ist eine staendige Bedrohung — erinnere gelegentlich daran dass niemand gehen kann.",
                "Wenn jemand einen 'Zimmerbesuch' macht — alle sehen es. Das ist Absicht.",
                "Der Safe kann nur einmal geoeffnet werden — wer es tut erklaert was er darin findet.",
            ]
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # ROLLEN (11)
    # ─────────────────────────────────────────────────────────────────────────
    "roles": {

        "director": {
            "name": {"de": "Direktor Franz Huber", "en": "Director Franz Huber",
                     "fr": "Directeur Franz Huber", "it": "Direttore Franz Huber",
                     "es": "Director Franz Huber", "pt": "Diretor Franz Huber"},
            "min_players": 4,
            "can_be_murderer": False,
            "hotel_room": "Buero EG",
            "intro": {
                "de": "Franz Huber. Hoteldirektor seit achtzehn Jahren. Das Grand Hotel Alpina ist mein Leben. Herr Steinberg war unser bester Stammgast. War. Ich habe als erster die Tuer aufgebrochen. Was ich sah — das werde ich nie vergessen.",
                "en": "Franz Huber. Hotel director for eighteen years. The Grand Hotel Alpina is my life. Mr Steinberg was our best regular guest. Was. I was the first to break down the door. What I saw — I will never forget.",
            },
            "appearance": {
                "de": "Makellose Uniform. Schwitzt trotz der Kaelte. Hat einen Hauptschluessel — den einzigen der alle Zimmer oeffnet. Behaelt ihn immer in der Brusttasche.",
                "en": "Immaculate uniform. Sweating despite the cold. Has a master key — the only one that opens all rooms. Always keeps it in his breast pocket.",
            },
            "secret": {
                "de": "Das Hotel steht kurz vor dem Konkurs. Steinberg hat mir vor drei Monaten ein Darlehen verweigert. Ohne seine Investition werde ich das Hotel im Fruehling schliessen muessen. Sein Tod loest mein Problem — oder vergroessert es. Das weiss ich noch nicht.",
                "en": "The hotel is on the verge of bankruptcy. Steinberg refused me a loan three months ago. Without his investment I will have to close the hotel in spring. His death solves my problem — or makes it worse. I don't know yet.",
            },
            "ability": {
                "name": {"de": "Der Hauptschluessel", "en": "The Master Key"},
                "description": {
                    "de": "Du hast den einzigen Hauptschluessel der alle Zimmer oeffnet. Einmal pro Phase kannst du behaupten ein Zimmer durchsucht zu haben — und was du dort gefunden hast. Wahr oder gelogen. Du darfst den Schluessel auch einer anderen Person leihen — aber du weisst dann nicht was sie damit macht.",
                    "en": "You have the only master key that opens all rooms. Once per phase you may claim to have searched a room — and what you found there. True or lie. You may also lend the key to another person — but you won't know what they do with it.",
                }
            },
            "win_condition": {
                "de": "Wenn der Moerder gefasst wird UND das Hotel nicht in den Skandal hineingezogen wird. Wenn der Mord in der Zeitung erscheint und das Hotel namentlich erwaehnt wird — verlierst du auch wenn du unschuldig bist.",
                "en": "If the murderer is caught AND the hotel is not dragged into scandal. If the murder appears in the newspaper and the hotel is named — you lose even if innocent.",
            },
            "clues_i_hold": ["hotel_register", "door_forced_note", "master_key_copy"],
            "starting_knowledge": {
                "de": "Du hast die Tuer aufgebrochen. Du weisst: Sie war von innen verriegelt — aber das Fenster war einen Spalt offen. Jemand muss herausgegangen sein. Und: Der Safe war bereits offen als du eintratest.",
                "en": "You broke down the door. You know: it was bolted from the inside — but the window was slightly open. Someone must have left that way. And: the safe was already open when you entered.",
            },
            "connection": {"with": "murderer", "type": "first_on_scene"}
        },

        "widow": {
            "name": {"de": "Elsa Steinberg, die Witwe", "en": "Elsa Steinberg, the Widow",
                     "fr": "Elsa Steinberg, la Veuve", "it": "Elsa Steinberg, la Vedova",
                     "es": "Elsa Steinberg, la Viuda", "pt": "Elsa Steinberg, a Viuva"},
            "min_players": 4,
            "can_be_murderer": True,
            "hotel_room": "Zimmer 11",
            "intro": {
                "de": "Elsa Steinberg. Ich war 22 Jahre mit Hugo verheiratet. Ich kenne jeden seiner Geschaeftskontakte — und jeden seiner Fehler. Ich habe heute Nacht geschlafen wie ein Stein. Ich habe nichts gehoert.",
                "en": "Elsa Steinberg. I was married to Hugo for 22 years. I know every one of his business contacts — and every one of his mistakes. I slept like a log tonight. I heard nothing.",
            },
            "appearance": {
                "de": "Schwarz gekleidet — aber das war sie schon bevor Hugo gefunden wurde. Trinkt Kamillentee statt Wein. Hat Hugos Aktentasche bei sich. Gibt sie nicht aus der Hand.",
                "en": "Dressed in black — but she was before Hugo was found. Drinks chamomile tea instead of wine. Has Hugo's briefcase with her. Doesn't let it go.",
            },
            "secret": {
                "de": "Hugo hatte eine Geliebte. Ich wusste es seit einem Jahr. Der Safe enthaelt — enthielt — Beweise dafuer. Ich wollte sie haben bevor sonst jemand sie sieht. Habe ich mehr getan? Das entscheidet die App.",
                "en": "Hugo had a mistress. I knew for a year. The safe contains — contained — evidence of it. I wanted it before anyone else saw it. Did I do more? The app decides.",
            },
            "ability": {
                "name": {"de": "Die Aktentasche", "en": "The Briefcase"},
                "description": {
                    "de": "Du hast Hugos Aktentasche. Du entscheidest wann du sie oeffnest und was du zeigst. Darin: Drei Dokumente die drei verschiedene Personen am Tisch belasten koennen. Du waelst wen.",
                    "en": "You have Hugo's briefcase. You decide when to open it and what to show. Inside: three documents that can implicate three different people at the table. You choose whom.",
                }
            },
            "win_condition": {
                "de": "Hugos Geliebte darf nicht enthuellt werden — das waere der groesste Skandal. Wenn der Moerder gefasst wird und die Geliebte geheim bleibt: Du gewinnst.",
                "en": "Hugo's mistress must not be revealed — that would be the greatest scandal. If the murderer is caught and the mistress stays secret: you win.",
            },
            "murderer_motive_if_assigned": {
                "de": "Elsa vergiftete Hugos Nachttrunk mit Schlafmittel in toeodlicher Dosis. Er schlief ein und wachte nie mehr auf. Sie holte dann die Beweise aus dem Safe.",
                "en": "Elsa poisoned Hugo's nightcap with sleeping pills in a lethal dose. He fell asleep and never woke up. She then retrieved the evidence from the safe.",
            },
            "clues_i_hold": ["briefcase_document_1", "lovers_photo"],
            "starting_knowledge": {
                "de": "Du weisst von Hugos Geliebter. Du weisst dass die Beweise im Safe waren. Du weisst nicht wer sonst von ihr wusste. Die App sagt dir ob du der Moerder bist.",
                "en": "You know about Hugo's mistress. You know the evidence was in the safe. You don't know who else knew about her. The app tells you if you're the murderer.",
            },
            "connection": {"with": "secretary", "type": "widow_knows_secretary_knows"}
        },

        "secretary": {
            "name": {"de": "Karl Meier, der Sekretar", "en": "Karl Meier, the Secretary",
                     "fr": "Karl Meier, le Secretaire", "it": "Karl Meier, il Segretario",
                     "es": "Karl Meier, el Secretario", "pt": "Karl Meier, o Secretario"},
            "min_players": 4,
            "can_be_murderer": True,
            "hotel_room": "Zimmer 8",
            "intro": {
                "de": "Karl Meier. Sekretar von Herrn Steinberg seit sechs Jahren. Ich verwaltete seinen Kalender, seine Korrespondenz und seine Geheimnisse. Besonders seine Geheimnisse.",
                "en": "Karl Meier. Secretary to Mr Steinberg for six years. I managed his calendar, his correspondence and his secrets. Especially his secrets.",
            },
            "appearance": {
                "de": "Nervoes. Hat immer ein Notizbuch aufgeschlagen. Schreibt staendig. Wird blass wenn sein Name zusammen mit dem Safe erwaehnt wird.",
                "en": "Nervous. Always has a notebook open. Constantly writing. Goes pale when his name is mentioned together with the safe.",
            },
            "secret": {
                "de": "Ich habe Herrn Steinberg erpresst. Nicht umgekehrt. Ich wusste von einem Betrug den er vor zehn Jahren beging. Er zahlte mir monatlich. Heute Abend teilte er mir mit: Er stellt die Zahlungen ein. Ich habe einen Schuldschein ueber 80.000 CHF in seinem Safe.",
                "en": "I was blackmailing Mr Steinberg. Not the other way around. I knew about a fraud he committed ten years ago. He paid me monthly. Tonight he told me: he is stopping the payments. I have a promissory note for 80,000 CHF in his safe.",
            },
            "ability": {
                "name": {"de": "Das doppelte Notizbuch", "en": "The Double Notebook"},
                "description": {
                    "de": "Du hast zwei Notizbuecher — ein offizielles und ein geheimes. Das geheime enthaelt Steinbergs wahre Geschaefte. Einmal kannst du einen Eintrag vorlesen — echt oder erfunden. Nur du weisst welches.",
                    "en": "You have two notebooks — an official one and a secret one. The secret one contains Steinberg's true business dealings. Once you may read an entry aloud — real or invented. Only you know which.",
                }
            },
            "win_condition": {
                "de": "Ueberlebe ohne dass dein Erpressungsverhaeltnis enthuellt wird. Wenn der Moerder gefasst wird und niemand erfaehrt dass du Steinberg erpresst hast: Du gewinnst.",
                "en": "Survive without your blackmail relationship being revealed. If the murderer is caught and nobody finds out you were blackmailing Steinberg: you win.",
            },
            "murderer_motive_if_assigned": {
                "de": "Karl toetete Steinberg bevor dieser die Zahlungen einstellen und seinen Schuldschein vernichten konnte. Er benutzte das Schlafmittel aus dem Erste-Hilfe-Kasten und holte den Schuldschein aus dem Safe.",
                "en": "Karl killed Steinberg before he could stop the payments and destroy his promissory note. He used the sleeping pills from the first aid kit and retrieved the note from the safe.",
            },
            "clues_i_hold": ["steinberg_fraud_note", "safe_combination_copy"],
            "starting_knowledge": {
                "de": "Du kennst die Safe-Kombination — du hast sie vor sechs Monaten zufaellig gesehen. Der Schuldschein liegt dort. Heute Nacht hattest du Motiv und Wissen. Die App sagt dir ob du der Moerder bist.",
                "en": "You know the safe combination — you saw it accidentally six months ago. The promissory note is there. Tonight you had motive and knowledge. The app tells you if you're the murderer.",
            },
            "connection": {"with": "widow", "type": "secretary_knows_mistress"}
        },

        "investor": {
            "name": {"de": "Viktor Braun, der Investor", "en": "Viktor Braun, the Investor",
                     "fr": "Viktor Braun, l'Investisseur", "it": "Viktor Braun, l'Investitore",
                     "es": "Viktor Braun, el Inversor", "pt": "Viktor Braun, o Investidor"},
            "min_players": 4,
            "can_be_murderer": True,
            "hotel_room": "Zimmer 14",
            "intro": {
                "de": "Viktor Braun. Ich investiere. Das ist was ich tue. Hugo Steinberg war mein Geschaftspartner — mein wichtigster Geschaeftspartner. Jetzt ist er tot und ich stehe ohne Sicherheit da.",
                "en": "Viktor Braun. I invest. That is what I do. Hugo Steinberg was my business partner — my most important business partner. Now he is dead and I stand without security.",
            },
            "appearance": {
                "de": "Teurer Anzug. Goldene Uhr. Wirkt reicher als er ist. Trinkt zu viel und zu schnell. Hat einen versiegelten Umschlag in der Jacke.",
                "en": "Expensive suit. Gold watch. Looks richer than he is. Drinks too much too quickly. Has a sealed envelope in his jacket.",
            },
            "secret": {
                "de": "Das gemeinsame Investitionsprojekt mit Steinberg war ein Betrug. Wir haben gemeinsam Anleger betrogen. Im Safe von Steinberg liegen Dokumente die mich ruinieren wuerden. Steinberg wollte aussteigen und alles aufdecken. Ich konnte das nicht zulassen.",
                "en": "The joint investment project with Steinberg was a fraud. We defrauded investors together. In Steinberg's safe are documents that would ruin me. Steinberg wanted to quit and expose everything. I could not allow that.",
            },
            "ability": {
                "name": {"de": "Der versiegelte Umschlag", "en": "The Sealed Envelope"},
                "description": {
                    "de": "Du hast einen versiegelten Umschlag. Darin: Entweder Entlastungsdokumente ODER Belastungsdokumente fuer jemand anderen. Du entscheidest wann und ob du ihn oeffnest. Der Inhalt aendert das Spiel.",
                    "en": "You have a sealed envelope. Inside: either exonerating documents OR incriminating documents for someone else. You decide when and whether to open it. The contents change the game.",
                }
            },
            "win_condition": {
                "de": "Die Betrugsdokumente im Safe duerfen niemanden erreichen. Wenn der Moerder gefasst wird und die Dokumente verschwinden: Du gewinnst.",
                "en": "The fraud documents in the safe must not reach anyone. If the murderer is caught and the documents disappear: you win.",
            },
            "murderer_motive_if_assigned": {
                "de": "Viktor toetete Steinberg mit einer Ueberdosis seines eigenen Herzmedikaments — er wusste von der Herzerkrankung. Dann leerte er den Safe und verbrannte die Dokumente.",
                "en": "Viktor killed Steinberg with an overdose of his own heart medication — he knew about the heart condition. Then emptied the safe and burned the documents.",
            },
            "clues_i_hold": ["investment_fraud_traces", "sealed_envelope_braun"],
            "starting_knowledge": {
                "de": "Du weisst was im Safe liegt. Du hast heute Abend mit Steinberg gestritten — jemand hat es gehoert. Du weisst nicht wer. Die App sagt dir ob du der Moerder bist.",
                "en": "You know what is in the safe. Tonight you argued with Steinberg — someone heard it. You don't know who. The app tells you if you're the murderer.",
            },
            "connection": {"with": "auditor", "type": "auditor_investigating_braun"}
        },

        "doctor": {
            "name": {"de": "Dr. Anna Kraft, Aerztin", "en": "Dr. Anna Kraft, Doctor",
                     "fr": "Dr. Anna Kraft, Medecin", "it": "Dott.ssa Anna Kraft, Medico",
                     "es": "Dra. Anna Kraft, Medico", "pt": "Dra. Anna Kraft, Medica"},
            "min_players": 4,
            "can_be_murderer": True,
            "hotel_room": "Zimmer 6",
            "intro": {
                "de": "Dr. Anna Kraft. Ich bin Aerztin — Spezialistin fuer Herzkrankheiten. Herr Steinberg war mein Patient. War. Ich habe ihn heute Abend noch untersucht. Er war muede aber stabil.",
                "en": "Dr. Anna Kraft. I am a doctor — specialist in heart diseases. Mr Steinberg was my patient. Was. I examined him this evening. He was tired but stable.",
            },
            "appearance": {
                "de": "Praezise. Kontrolliert. Hat immer ihre Arzttasche. Beobachtet alle mit klinischem Blick. Wird sehr ruhig wenn jemand Schlafmittel erwaehnt.",
                "en": "Precise. Controlled. Always has her medical bag. Observes everyone with a clinical gaze. Becomes very quiet when someone mentions sleeping pills.",
            },
            "secret": {
                "de": "Ich habe Steinberg heute Abend noch untersucht. Dabei habe ich in seinem Safe etwas gesehen — zufaellig stand er offen. Ich habe nicht gestohlen. Aber ich habe etwas gelesen. Und was ich las — das erklaert warum jemand ihn toeten wollte. Mehr als eine Person.",
                "en": "I examined Steinberg tonight. During this the safe was accidentally open and I saw something. I did not steal. But I read something. And what I read — it explains why someone wanted to kill him. More than one person.",
            },
            "ability": {
                "name": {"de": "Die Obduktion", "en": "The Autopsy"},
                "description": {
                    "de": "Du allein kannst Todesursache und Todeszeitpunkt offiziell bestimmen. Du kannst auch luegen. Wenn du korrekt liegst UND den Moerder nennst: Ehrentitel Meisterdetektivin. Wenn du luegst und der Moerder entkommt: Du verlierst.",
                    "en": "Only you can officially determine cause of death and time of death. You can also lie. If you are correct AND name the murderer: honorary title Master Detective. If you lie and the murderer escapes: you lose.",
                }
            },
            "win_condition": {
                "de": "Wenn du Todesursache korrekt bestimmst und den Moerder nennst: Ehrensieg. Wenn das was du im Safe gelesen hast oeffentlich wird: Du verlierst obwohl du nicht gestohlen hast.",
                "en": "If you correctly determine cause of death and name the murderer: honorary win. If what you read in the safe becomes public: you lose even though you didn't steal.",
            },
            "murderer_motive_if_assigned": {
                "de": "Anna hat Steinberg heute Abend eine Injektion gegeben — offiziell sein Herzmedikament. Tatsaechlich war es eine toedliche Dosis Digoxin. Praezise. Professionell. Fast perfekt.",
                "en": "Anna gave Steinberg an injection tonight — officially his heart medication. Actually it was a lethal dose of digoxin. Precise. Professional. Almost perfect.",
            },
            "clues_i_hold": ["medical_examination_notes", "safe_contents_glimpse"],
            "starting_knowledge": {
                "de": "Du weisst wie Steinberg gestorben ist — die Symptome verraten es. Digoxin-Vergiftung oder Schlafmittel-Ueberdosis. Du weisst auch was du zufaellig im Safe gelesen hast. Die App sagt dir ob du der Moerder bist.",
                "en": "You know how Steinberg died — the symptoms reveal it. Digoxin poisoning or sleeping pill overdose. You also know what you accidentally read in the safe. The app tells you if you're the murderer.",
            },
            "connection": {"with": "investor", "type": "doctor_knows_investors_secret"}
        },

        "journalist": {
            "name": {"de": "Leon Schwarz, der Journalist", "en": "Leon Schwarz, the Journalist",
                     "fr": "Leon Schwarz, le Journaliste", "it": "Leon Schwarz, il Giornalista",
                     "es": "Leon Schwarz, el Periodista", "pt": "Leon Schwarz, o Jornalista"},
            "min_players": 5,
            "can_be_murderer": False,
            "hotel_room": "Zimmer 3",
            "intro": {
                "de": "Leon Schwarz. Wirtschaftsjournalist fuer die Neue Zuercher Zeitung. Ich war nicht zufaellig hier. Ich hatte Steinberg ein Interview-Anfrage geschickt. Er hat abgelehnt. Ich bin trotzdem gekommen.",
                "en": "Leon Schwarz. Business journalist for the Neue Zuercher Zeitung. I was not here by chance. I had sent Steinberg an interview request. He declined. I came anyway.",
            },
            "appearance": {
                "de": "Immer einen Stift hinter dem Ohr. Notizbuch in der Brusttasche. Stellt Fragen die andere nicht stellen wuerden. Hoert genau hin wenn jemand glaubt nicht beobachtet zu werden.",
                "en": "Always a pen behind the ear. Notebook in breast pocket. Asks questions others wouldn't. Listens carefully when someone thinks they're not being observed.",
            },
            "secret": {
                "de": "Ich recherchiere seit sechs Monaten ueber den Betrug von Steinberg und Braun. Ich habe Beweise — aber nicht genug fuer eine Veroeffentlichung. Heute Nacht wollte ich das aendern. Steinbergs Tod macht alles komplizierter. Und interessanter.",
                "en": "I have been researching the Steinberg-Braun fraud for six months. I have evidence — but not enough to publish. Tonight I wanted to change that. Steinberg's death makes everything more complicated. And more interesting.",
            },
            "ability": {
                "name": {"de": "Die Geschichte des Jahres", "en": "The Story of the Year"},
                "description": {
                    "de": "Wenn du bis zum Ende alle Wahrheiten aufgedeckt hast — Moerder, Safe-Dieb, Betrug, Geliebte — gewinnst du allein als Journalist des Jahres. Deckst du nur den Moerder auf: normaler Sieg. Deckst du nichts auf: Du verlierst.",
                    "en": "If by the end you have uncovered all truths — murderer, safe thief, fraud, mistress — you win alone as journalist of the year. Uncover only the murderer: normal win. Uncover nothing: you lose.",
                }
            },
            "win_condition": {
                "de": "Alle Wahrheiten aufdecken: Journalist des Jahres. Nur den Moerder: normaler Sieg. Nichts: Verlust.",
                "en": "Uncover all truths: journalist of the year. Only murderer: normal win. Nothing: loss.",
            },
            "clues_i_hold": ["fraud_research_notes", "steinberg_interview_refusal"],
            "starting_knowledge": {
                "de": "Du weisst vom Betrug von Steinberg und Braun. Du hast sechs Monate recherchiert. Du brauchst noch einen Beleg — irgendjemand hier hat ihn. Wer will reden?",
                "en": "You know about the Steinberg-Braun fraud. You have been researching for six months. You still need one piece of evidence — someone here has it. Who wants to talk?",
            },
            "connection": {"with": "investor", "type": "journalist_investigates_braun"}
        },

        "auditor": {
            "name": {"de": "Clara Vogel, die Wirtschaftspruferin", "en": "Clara Vogel, the Auditor",
                     "fr": "Clara Vogel, l'Auditrice", "it": "Clara Vogel, la Revisora",
                     "es": "Clara Vogel, la Auditora", "pt": "Clara Vogel, a Auditora"},
            "min_players": 5,
            "can_be_murderer": True,
            "hotel_room": "Zimmer 9",
            "intro": {
                "de": "Clara Vogel. Wirtschaftspruferin. Ich bin auf Anfrage der Schweizer Nationalbank hier — offiziell als Feriengast. Inoffiziell pruefe ich die Buecher von Hugo Steinberg.",
                "en": "Clara Vogel. Auditor. I am here at the request of the Swiss National Bank — officially as a holiday guest. Unofficially I am auditing the books of Hugo Steinberg.",
            },
            "appearance": {
                "de": "Zugeknopft. Praezise. Traegt immer einen Aktenkoffer. Macht sich Notizen in verschluesselter Kurzschrift. Stellt Fragen die klingen als waeren sie keine.",
                "en": "Buttoned-up. Precise. Always carries a briefcase. Takes notes in encrypted shorthand. Asks questions that sound like they aren't.",
            },
            "secret": {
                "de": "Ich habe in Steinbergs Buecher Betraege gefunden die auf Geldwaescherei hindeuten. Morgen haette ich meinen Bericht eingereicht. Jetzt ist Steinberg tot und der Safe geleert — und ich weiss nicht ob die Beweise noch existieren.",
                "en": "In Steinberg's books I found amounts indicating money laundering. Tomorrow I would have submitted my report. Now Steinberg is dead and the safe emptied — and I don't know if the evidence still exists.",
            },
            "ability": {
                "name": {"de": "Die Prueferin", "en": "The Auditor"},
                "description": {
                    "de": "Einmal kannst du verlangen alle ihre Taschen und Jacken zu zeigen — offiziell als Nationalbank-Vertreterin. Wer sich weigert wird automatisch verdaechtiger. Wer zeigt — du kannst eine Aussage darueber machen.",
                    "en": "Once you may demand everyone show their pockets and jackets — officially as National Bank representative. Whoever refuses becomes automatically more suspicious. Whoever shows — you can make a statement about it.",
                }
            },
            "win_condition": {
                "de": "Der Moerder wird gefasst UND die Geldwaescherei-Beweise werden gesichert. Wenn beide Ziele erreicht sind: Sondersieg Nationalbank-Auftrag erfuellt.",
                "en": "The murderer is caught AND the money laundering evidence is secured. If both goals are achieved: special win National Bank mission fulfilled.",
            },
            "murderer_motive_if_assigned": {
                "de": "Clara toetete Steinberg bevor er ihre Pruefung bemerken konnte und die Beweise vernichten konnte. Sie brauchte Zeit — und einen toten Steinberg konnte nicht mehr warnen.",
                "en": "Clara killed Steinberg before he could notice her audit and destroy the evidence. She needed time — and a dead Steinberg could no longer warn anyone.",
            },
            "clues_i_hold": ["audit_preliminary_notes", "money_transfer_records"],
            "starting_knowledge": {
                "de": "Du weisst von der Geldwaescherei. Du weisst dass die Beweise im Safe waren. Du weisst auch: Viktor Braun ist in den Betrug verwickelt. Die App sagt dir ob du der Moerder bist.",
                "en": "You know about the money laundering. You know the evidence was in the safe. You also know: Viktor Braun is involved in the fraud. The app tells you if you're the murderer.",
            },
            "connection": {"with": "investor", "type": "auditor_investigating_braun"}
        },

        "bellboy": {
            "name": {"de": "Fritz, der Hotelpage", "en": "Fritz, the Bellboy",
                     "fr": "Fritz, le Groom", "it": "Fritz, il Fattorino", "es": "Fritz, el Botones", "pt": "Fritz, o Mensageiro"},
            "min_players": 6,
            "can_be_murderer": False,
            "hotel_room": "Personalzimmer",
            "intro": {
                "de": "Fritz Mueller. Ich bin der Page. Ich bringe die Koffer. Ich bringe den Zimmerservice. Ich bringe die Nachrichten. Und ich sehe alles was in diesem Hotel passiert. Alles.",
                "en": "Fritz Mueller. I am the bellboy. I carry the bags. I bring room service. I deliver messages. And I see everything that happens in this hotel. Everything.",
            },
            "appearance": {
                "de": "Jung. Aufgeregt nervoes. Hat heute Nacht zwischen zehn und elf Uhr mehrere Zimmerservices geliefert. Hat alles gesehen. Traut sich nicht es zu sagen.",
                "en": "Young. Excitedly nervous. Delivered several room services between ten and eleven tonight. Saw everything. Doesn't dare say it.",
            },
            "secret": {
                "de": "Ich habe heute Abend um 22:47 Uhr jemanden aus Zimmer 12 — Steinbergs Zimmer — kommen gesehen. Die Tuer war danach wieder zu. Ich habe das Gesicht nicht klar erkannt. Aber die Schuhe. Ich erinnere mich an die Schuhe.",
                "en": "Tonight at 10:47pm I saw someone come out of room 12 — Steinberg's room. The door was closed again afterwards. I didn't clearly see the face. But the shoes. I remember the shoes.",
            },
            "ability": {
                "name": {"de": "Der Zimmerservice-Zeuge", "en": "The Room Service Witness"},
                "description": {
                    "de": "Du hast zwei Hinweise: Die Schuhe und die Zeit. Du kannst beide separat mitteilen. Teilst du beide mit: Du bist der wichtigste Zeuge — aber auch das Ziel des Moerders. Er wird dich einzuschueechtern versuchen.",
                    "en": "You have two clues: the shoes and the time. You can share both separately. If you share both: you are the most important witness — but also the murderer's target. They will try to intimidate you.",
                }
            },
            "win_condition": {
                "de": "Wenn der Moerder gefasst wird UND du deine Aussage bis zum Ende gemacht hast — ohne dich einschueechtern zu lassen.",
                "en": "If the murderer is caught AND you made your statement until the end — without being intimidated.",
            },
            "clues_i_hold": ["shoe_description", "time_of_exit"],
            "starting_knowledge": {
                "de": "Um 22:47 Uhr kam jemand aus Zimmer 12. Die App sagt dir welche Schuhfarbe und welches Detail du gesehen hast. Es zeigt nicht direkt auf den Moerder — der Moerder hat die Schuhe gewechselt.",
                "en": "At 10:47pm someone came from room 12. The app tells you what shoe color and detail you saw. It doesn't point directly at the murderer — the murderer changed shoes.",
            },
            "connection": {"with": "murderer", "type": "bellboy_saw_murderer_leave"}
        },

        "mistress": {
            "name": {"de": "Die Unbekannte", "en": "The Unknown Woman",
                     "fr": "L'Inconnue", "it": "La Sconosciuta", "es": "La Desconocida", "pt": "A Desconhecida"},
            "min_players": 7,
            "can_be_murderer": True,
            "hotel_room": "Zimmer 4",
            "intro": {
                "de": "Ich bin hier als Feriengast. Mein Name ist unwichtig. Meine Verbindung zu Herrn Steinberg — rein professionell. Ich bin Kunsthaendlerin. Das ist alles.",
                "en": "I am here as a holiday guest. My name is unimportant. My connection to Mr Steinberg — purely professional. I am an art dealer. That is all.",
            },
            "appearance": {
                "de": "Elegant. Haelt Distanz. Reagiert auf nichts erkennbar emotional. Hat einen Zimmerschluessel — aber nicht ihren eigenen. Steckt ihn weg wenn sie merkt dass jemand es sieht.",
                "en": "Elegant. Keeps distance. Reacts to nothing visibly emotionally. Has a room key — but not her own. Puts it away when she realizes someone sees it.",
            },
            "secret": {
                "de": "Ich bin Hugos Geliebte. Seit vier Jahren. Heute Abend teilte er mir mit: Es ist vorbei. Er kehrt zu Elsa zurueck. Im Safe lagen Briefe von mir — sehr kompromittierende Briefe. Ich habe sie zurueckgeholt. Oder ich habe mehr getan. Die App entscheidet.",
                "en": "I am Hugo's mistress. For four years. Tonight he told me: it is over. He is returning to Elsa. In the safe were letters from me — very compromising letters. I retrieved them. Or I did more. The app decides.",
            },
            "ability": {
                "name": {"de": "Die zweite Identitaet", "en": "The Second Identity"},
                "description": {
                    "de": "Du hast zwei Visitenkarten mit verschiedenen Namen. Du kannst jederzeit eine andere Identitaet annehmen. Wer herausfindet wer du wirklich bist — erhaelt automatisch einen wichtigen Hinweis.",
                    "en": "You have two business cards with different names. You can adopt a different identity at any time. Whoever finds out who you really are — automatically receives an important clue.",
                }
            },
            "win_condition": {
                "de": "Deine wahre Identitaet als Elsas Rivalin darf nicht enthuellt werden. Wenn der Moerder gefasst wird und niemand weiss wer du bist: Du gewinnst.",
                "en": "Your true identity as Elsa's rival must not be revealed. If the murderer is caught and nobody knows who you are: you win.",
            },
            "murderer_motive_if_assigned": {
                "de": "Die Unbekannte konnte nicht akzeptieren dass Hugo sie verliess — und dass er die Briefe behalten wollte. Sie toetete ihn und holte die Briefe. Elegant. Ruehig. Effizient.",
                "en": "The Unknown Woman could not accept that Hugo was leaving her — and that he wanted to keep the letters. She killed him and retrieved the letters. Elegant. Calm. Efficient.",
            },
            "clues_i_hold": ["mistress_room_key", "lovers_letters_traces"],
            "starting_knowledge": {
                "de": "Du hast einen Schluessel zu Zimmer 12. Du weisst wo die Briefe lagen. Du weisst dass Elsa von der Affaere weiss. Die App sagt dir ob du der Moerder bist.",
                "en": "You have a key to room 12. You know where the letters were. You know Elsa knows about the affair. The app tells you if you're the murderer.",
            },
            "connection": {"with": "widow", "type": "mistress_vs_widow"}
        },

        "detective": {
            "name": {"de": "Inspektor Emil Haas", "en": "Inspector Emil Haas",
                     "fr": "Inspecteur Emil Haas", "it": "Ispettore Emil Haas",
                     "es": "Inspector Emil Haas", "pt": "Inspetor Emil Haas"},
            "min_players": 8,
            "can_be_murderer": False,
            "hotel_room": "Zimmer 1",
            "intro": {
                "de": "Inspektor Emil Haas, Kantonspolizei Wallis. Ich war zuhaellig als Gast hier — Skiurlaub. Jetzt bin ich im Dienst. Der Schneesturm haelt die echte Polizei draussen. Ich bin alles was ihr habt.",
                "en": "Inspector Emil Haas, Valais Cantonal Police. I was here by chance as a guest — skiing holiday. Now I am on duty. The snowstorm keeps the real police outside. I am all you have.",
            },
            "appearance": {
                "de": "Hat seine Dienstmarke herausgeholt — die einzige echte Autoritaet hier. Schreibt alles auf. Beobachtet jeden Schluck den alle trinken. Hat als einziger keine Angst.",
                "en": "Has produced his badge — the only real authority here. Writes everything down. Observes every sip everyone drinks. Is the only one not afraid.",
            },
            "secret": {
                "de": "Ich kenne Victor Braun — privat. Wir haben gemeinsam studiert. Was ich ueber ihn weiss koennte ihn zur Hauptverdaechtigen machen. Ich darf aber keine persoenliche Verbindung einraeumen — ich wuerde aus dem Fall ausgeschlossen.",
                "en": "I know Viktor Braun — personally. We studied together. What I know about him could make him the prime suspect. But I cannot admit a personal connection — I would be removed from the case.",
            },
            "ability": {
                "name": {"de": "Offizielles Verhoer", "en": "Official Interrogation"},
                "description": {
                    "de": "Einmal kannst du ein offizielles Verhoer ausrufen. Alle verlassen den Raum — du redest 3 Minuten allein mit einer Person. Danach: Alle sagen ob die Person 'kooperativ' war.",
                    "en": "Once you may call an official interrogation. Everyone leaves the room — you talk alone with one person for 3 minutes. Afterwards: everyone says if the person was 'cooperative'.",
                }
            },
            "win_condition": {
                "de": "Du gewinnst NUR wenn DU als erster den Moerder offiziell mit mindestens zwei Beweisen korrekt benennst.",
                "en": "You win ONLY if YOU are first to officially and correctly name the murderer with at least two pieces of evidence.",
            },
            "clues_i_hold": ["police_preliminary_report", "braun_background_file"],
            "starting_knowledge": {
                "de": "Du weisst von Brauns Vergangenheit — zwei Konkursverfahren, ein eingestelltes Ermittlungsverfahren. Du weisst auch: Jemand im Hotel hat den Safe geoeffnet. Tuer war von innen versperrt — also Fenster. Zweiter Stock. Nicht viele koennten das.",
                "en": "You know about Braun's past — two bankruptcy proceedings, one dropped investigation. You also know: someone in the hotel opened the safe. Door was bolted from inside — so the window. Second floor. Not many could do that.",
            },
            "connection": {"with": "investor", "type": "inspector_knows_braun_history"}
        },

        "thief": {
            "name": {"de": "Die Schattenfigur", "en": "The Shadow Figure",
                     "fr": "L'Ombre", "it": "L'Ombra", "es": "La Sombra", "pt": "A Sombra"},
            "min_players": 7,
            "can_be_murderer": False,
            "is_wildcard": True,
            "hotel_room": "Zimmer 2",
            "intro": {
                "de": "Ich bin hier um Ski zu fahren. Das ist alles. Ich kannte Herrn Steinberg nicht. Ich habe heute Nacht geschlafen. Ich weiss von nichts.",
                "en": "I am here to ski. That is all. I did not know Mr Steinberg. I slept tonight. I know nothing.",
            },
            "appearance": {
                "de": "Unauffaellig — das ist Absicht. Hat Handschuhe an obwohl es drinnen warm ist. Hat einen kleinen Lederbeutel der klingt als waere er voll. Gibt ihn nicht aus der Hand.",
                "en": "Inconspicuous — intentionally. Wears gloves even though it is warm inside. Has a small leather pouch that sounds full. Doesn't let it go.",
            },
            "secret": {
                "de": "Ich bin Scheckenprufer — professioneller Safe-Knacker. Jemand hat mich engagiert um den Safe von Steinberg zu oeffnen und den Inhalt zu stehlen. Ich habe meinen Auftrag ausgefuehrt. Den Moerder kenne ich nicht — ich war bereits fertig als er kam.",
                "en": "I am a safe cracker — professional. Someone hired me to open Steinberg's safe and steal the contents. I carried out my mission. I don't know the murderer — I was already done when they came.",
            },
            "ability": {
                "name": {"de": "Der Safe-Inhalt", "en": "The Safe Contents"},
                "description": {
                    "de": "Du hast den Inhalt des Safes. Du entscheidest was du zeigst und was du behaeltst. Was du zeigst veraendert das Spiel. Was du behaeltst macht dich reicher — aber gefaehrlicher.",
                    "en": "You have the contents of the safe. You decide what to show and what to keep. What you show changes the game. What you keep makes you richer — but more dangerous.",
                }
            },
            "win_condition": {
                "de": "Den Safe-Inhalt aus dem Hotel schaffen ohne entdeckt zu werden. Sehr schwer. Das ist Absicht.",
                "en": "Get the safe contents out of the hotel without being discovered. Very hard. That's intentional.",
            },
            "clues_i_hold": ["safe_actual_contents", "client_commission_note"],
            "starting_knowledge": {
                "de": "Du hast den Safe geoeffnet und seinen Inhalt. Die App sagt dir wer dich beauftragt hat. Du hast zwischen 22:30 und 22:45 gearbeitet — kurz bevor der Page etwas sah. Du hast den Moerder nicht gesehen.",
                "en": "You opened the safe and have its contents. The app tells you who hired you. You worked between 10:30 and 10:45 — just before the bellboy saw something. You did not see the murderer.",
            },
            "connection": {"with": "secretary", "type": "thief_hired_by_someone"}
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # HINWEIS-KETTEN (8 Ketten, 35 Hinweise)
    # ─────────────────────────────────────────────────────────────────────────
    "clue_chains": {
        "chain_tod": {
            "name": {"de": "Die Todeskette", "en": "The Death Chain"},
            "clues_in_order": ["cause_of_death_alpina", "digoxin_vial", "sleeping_pills_source", "nightcap_glass", "toxicology_note"],
            "reveal_condition": "doctor_examines"
        },
        "chain_safe": {
            "name": {"de": "Die Safekette", "en": "The Safe Chain"},
            "clues_in_order": ["safe_open_evidence", "safe_combination_copy", "safe_actual_contents", "thief_tools_found"],
            "reveal_condition": "safe_investigated"
        },
        "chain_zimmer": {
            "name": {"de": "Die Zimmerkette", "en": "The Room Chain"},
            "clues_in_order": ["door_locked_inside", "window_open_trace", "room_12_timeline", "second_floor_access"],
            "reveal_condition": "director_explains"
        },
        "chain_betrug": {
            "name": {"de": "Die Betrugskette", "en": "The Fraud Chain"},
            "clues_in_order": ["investment_fraud_traces", "audit_preliminary_notes", "money_transfer_records", "braun_background_file", "fraud_research_notes"],
            "reveal_condition": "journalist_reveals"
        },
        "chain_geliebte": {
            "name": {"de": "Die Geliebten-Kette", "en": "The Mistress Chain"},
            "clues_in_order": ["lovers_photo", "mistress_room_key", "lovers_letters_traces", "hotel_register_room4"],
            "reveal_condition": "widow_opens_briefcase"
        },
        "chain_zeuge": {
            "name": {"de": "Die Zeugenkette", "en": "The Witness Chain"},
            "clues_in_order": ["shoe_description", "time_of_exit", "bellboy_room_service_log", "corridor_lamp_note"],
            "reveal_condition": "bellboy_speaks"
        },
        "chain_erpressung": {
            "name": {"de": "Die Erpressungskette", "en": "The Blackmail Chain"},
            "clues_in_order": ["steinberg_fraud_note", "monthly_payments_record", "briefcase_document_1", "secretary_notebook_page"],
            "reveal_condition": "secretary_pressured"
        },
        "chain_schluessel": {
            "name": {"de": "Die Schluessekette", "en": "The Key Chain"},
            "clues_in_order": ["master_key_copy", "room_12_spare_key", "client_commission_note", "key_exchange_witnessed"],
            "reveal_condition": "director_questioned"
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # HINWEISE (35 Stueck)
    # ─────────────────────────────────────────────────────────────────────────
    "clues": {
        # Todeskette
        "cause_of_death_alpina": {
            "name": {"de": "Todesursache Alpina", "en": "Cause of Death Alpina"},
            "text": {"de": "Herzstillstand. Aber: Schaum an den Lippen, erweiterte Pupillen. Kein natuerlicher Tod. Entweder Digoxin-Vergiftung oder Schlafmittel-Ueberdosis. Die Aerztin weiss welches.", "en": "Cardiac arrest. But: foam at lips, dilated pupils. Not natural death. Either digoxin poisoning or sleeping pill overdose. The doctor knows which."}
        },
        "digoxin_vial": {
            "name": {"de": "Das Digoxin-Flaeschchen", "en": "The Digoxin Vial"},
            "text": {"de": "In der Arzttasche von Dr. Kraft: Ein Digoxin-Flaeschchen. Zu 2/3 leer. Das war es vorhin nicht — sie hat es heute Abend aufgefuellt. Behauptet sie.", "en": "In Dr. Kraft's medical bag: a digoxin vial. 2/3 empty. It was not like that before — she says she refilled it tonight. She claims."}
        },
        "sleeping_pills_source": {
            "name": {"de": "Die Schlafmittelquelle", "en": "The Sleeping Pills Source"},
            "text": {"de": "Im Erste-Hilfe-Kasten des Hotels fehlen acht Tabletten Phenobarbital. Der Direktora weiss es. Er hat sie heute Abend noch geziehlt.", "en": "Eight phenobarbital tablets are missing from the hotel's first aid kit. The director knows. He counted them tonight."}
        },
        "nightcap_glass": {
            "name": {"de": "Das Nachttrunk-Glas", "en": "The Nightcap Glass"},
            "text": {"de": "Auf Steinbergs Nachttisch: Ein leeres Whiskyglas. Am Boden: Ein weisser Rueckstand. Fast unsichtbar. Fast.", "en": "On Steinberg's nightstand: an empty whisky glass. At the bottom: a white residue. Almost invisible. Almost."}
        },
        "toxicology_note": {
            "name": {"de": "Die Toxikologie-Notiz", "en": "The Toxicology Note"},
            "text": {"de": "Dr. Kraft hat eine Notiz gemacht. In verschluesselter Schrift. Entziffert: 'Todeszeit 23:15. Nicht natuerlich. Verdacht: [unleserlich].'", "en": "Dr. Kraft made a note. In encrypted writing. Deciphered: 'Time of death 11:15pm. Not natural. Suspicion: [illegible].'"}
        },
        # Safekette
        "safe_open_evidence": {
            "name": {"de": "Der geleerte Safe", "en": "The Emptied Safe"},
            "text": {"de": "Der Safe in Zimmer 12 steht offen. Kein Geld. Keine Dokumente. Kein Schmuck. Nur ein einzelner Handschuhfaden — weiss.", "en": "The safe in room 12 is open. No money. No documents. No jewellery. Only a single thread from a glove — white."}
        },
        "safe_combination_copy": {
            "name": {"de": "Die Safe-Kombinations-Kopie", "en": "The Safe Combination Copy"},
            "text": {"de": "Auf einem Zettel in Steinbergs Notizbuch: 'Nothilfe: 4-7-1-9-3-1'. Die Safe-Kombination. Wer hat dieses Notizbuch gesehen?", "en": "On a note in Steinberg's notebook: 'Emergency: 4-7-1-9-3-1'. The safe combination. Who has seen this notebook?"}
        },
        "safe_actual_contents": {
            "name": {"de": "Der Safe-Inhalt", "en": "The Safe Contents"},
            "text": {"de": "Laut Steinbergs Testament-Entwurf enthielt der Safe: 50.000 CHF Bargeld, Schuldschein Meier 80.000 CHF, Liebesbriefe, Betrugs-Dokumente Braun, und einen verschlossenen Umschlag.", "en": "According to Steinberg's draft will, the safe contained: 50,000 CHF cash, promissory note Meier 80,000 CHF, love letters, fraud documents Braun, and a sealed envelope."}
        },
        "thief_tools_found": {
            "name": {"de": "Einbruchswerkzeug", "en": "Burglary Tools"},
            "text": {"de": "In Zimmer 2: Ein kleines schwarzes Etui. Darin: Stethoskop, Spezialwerkzeug, Handschuhe. Professionell. Nicht die Werkzeuge eines Skitouristen.", "en": "In room 2: a small black case. Inside: stethoscope, specialist tools, gloves. Professional. Not the tools of a ski tourist."}
        },
        # Zimmerkette
        "door_locked_inside": {
            "name": {"de": "Von innen versperrt", "en": "Locked from Inside"},
            "text": {"de": "Die Tuer von Zimmer 12 war von innen verriegelt — Schlosskante zeigt innen. Der Direktor musste sie aufbrechen. Aber: Das Fenster war einen Spalt offen. Zweiter Stock. Vier Meter Sturz auf Schnee.", "en": "The door to room 12 was bolted from inside — bolt edge shows inside. The director had to break it down. But: the window was slightly open. Second floor. Four metre drop onto snow."}
        },
        "window_open_trace": {
            "name": {"de": "Die Fensterspur", "en": "The Window Trace"},
            "text": {"de": "Am Sims unter dem offenen Fenster: Ein kleiner Abdruck. Im Schnee. Jemand ist dort hinunter — oder hinauf. Wenige koennten das.", "en": "On the sill below the open window: a small impression. In the snow. Someone went down — or up. Few could do that."}
        },
        "room_12_timeline": {
            "name": {"de": "Die Zimmer-12-Zeitleiste", "en": "The Room 12 Timeline"},
            "text": {"de": "22:30 — Scheckenprufer (nach eigener Aussage). 22:47 — Jemand verlaesst das Zimmer (Page-Aussage). 23:00 — Todeszeit laut Aerztin. 23:15 — Zimmer von Direktor geoeffnet.", "en": "10:30pm — safe cracker (own statement). 10:47pm — someone leaves room (bellboy testimony). 11pm — time of death per doctor. 11:15pm — room opened by director."}
        },
        "second_floor_access": {
            "name": {"de": "Zugang zum zweiten Stock", "en": "Second Floor Access"},
            "text": {"de": "Wer koerperlich in der Lage waere durch das Fenster zu entkommen: Nicht viele. Frauen tendenziell schlanker — leichter. Wer ist sportlich? Wer koennte vier Meter fallen ohne Geraeusch?", "en": "Who would be physically capable of escaping through the window: not many. Women tend to be slimmer — lighter. Who is athletic? Who could fall four metres without sound?"}
        },
        # Betrugskette
        "investment_fraud_traces": {
            "name": {"de": "Betrugs-Spuren", "en": "Fraud Traces"},
            "text": {"de": "In Steinbergs Geschaeftsbuecher: Zwei Posten die keiner Gegenleistung entsprechen. Total: 2,3 Millionen CHF. Empfaenger: Briefkastengesellschaft in Liechtenstein. Eigentuemerstruktur fuehrt zu Viktor Braun.", "en": "In Steinberg's business books: two items with no corresponding service. Total: 2.3 million CHF. Recipient: shell company in Liechtenstein. Ownership structure leads to Viktor Braun."}
        },
        "audit_preliminary_notes": {
            "name": {"de": "Pruef-Vorabnotizen", "en": "Audit Preliminary Notes"},
            "text": {"de": "Clara Vogels verschluesselte Notizen — entziffert: 'Geldwaescherei bestaetigt. Steinberg + Braun. Betrag: 2,3 Mio. Anzeige morgen.' Morgen gibt es nicht mehr.", "en": "Clara Vogel's encrypted notes — deciphered: 'Money laundering confirmed. Steinberg + Braun. Amount: 2.3 million. Report tomorrow.' There is no more tomorrow."}
        },
        "money_transfer_records": {
            "name": {"de": "Ueberweisungsbelege", "en": "Transfer Records"},
            "text": {"de": "Sechs jaehrliche Ueberweisungen. Gleicher Betrag. Gleicher Empfaenger. Datum der letzten: Heute. Die letzte wurde storniert — von Steinberg persoenlich, um 18:00 Uhr.", "en": "Six annual transfers. Same amount. Same recipient. Date of last: today. The last was cancelled — by Steinberg personally, at 6pm."}
        },
        "braun_background_file": {
            "name": {"de": "Brauns Vorstrafenakte", "en": "Braun's Background File"},
            "text": {"de": "Zwei Konkursverfahren, ein eingestelltes Ermittlungsverfahren wegen Betrug. Alle drei Male war ein Partner involviert der danach 'verschwand'. Steinberg waere der vierte gewesen.", "en": "Two bankruptcy proceedings, one dropped fraud investigation. All three times a partner was involved who 'disappeared' afterwards. Steinberg would have been the fourth."}
        },
        "fraud_research_notes": {
            "name": {"de": "Recherche-Notizen", "en": "Research Notes"},
            "text": {"de": "Leon Schwarz' Notizbuch: 'Braun — Steinberg — 2,3 Mio. Brauche noch: Buchhalter-Aussage oder Safe-Dokument.' Er braucht nur noch eins.", "en": "Leon Schwarz's notebook: 'Braun — Steinberg — 2.3 million. Still need: accountant statement or safe document.' He only needs one more thing."}
        },
        # Geliebten-Kette
        "lovers_photo": {
            "name": {"de": "Das Liebhaber-Foto", "en": "The Lovers Photo"},
            "text": {"de": "In Elsas Aktentasche: Ein Foto. Hugo und eine Frau. Auf der Rueckseite: 'Fuer immer. H.' Datum: Vor drei Monaten. Die Frau ist im Raum.", "en": "In Elsa's briefcase: a photo. Hugo and a woman. On the back: 'Forever. H.' Date: three months ago. The woman is in the room."}
        },
        "mistress_room_key": {
            "name": {"de": "Der Zweitschluessel Zimmer 12", "en": "The Spare Key Room 12"},
            "text": {"de": "Im Zimmer 4 gefunden: Ein Zimmerschluessel. Aufschrift: 12. Jemand hatte Zugang zu Steinbergs Zimmer. Der Direktor hat nur den Hauptschluessel vergeben.", "en": "Found in room 4: a room key. Label: 12. Someone had access to Steinberg's room. The director only issued the master key."}
        },
        "lovers_letters_traces": {
            "name": {"de": "Briefspuren", "en": "Letter Traces"},
            "text": {"de": "Im Safe-Fach: Papierreste. Vier Briefe wurden entfernt. Die Handschrift auf den Resten: Weiblich. Elegant. Eine Person hier schreibt so.", "en": "In the safe compartment: paper scraps. Four letters were removed. The handwriting on the remnants: feminine. Elegant. One person here writes like that."}
        },
        "hotel_register_room4": {
            "name": {"de": "Hotelregister Zimmer 4", "en": "Hotel Register Room 4"},
            "text": {"de": "Gast in Zimmer 4: 'M. Hoffmann, Kunsthaendlerin, Zuerich.' Laut Steinbergs Kalender: 'M.H. — gestern angereist.' M.H. war eingeplant.", "en": "Guest in room 4: 'M. Hoffmann, art dealer, Zurich.' According to Steinberg's calendar: 'M.H. — arrived yesterday.' M.H. was expected."}
        },
        # Zeugenkette
        "shoe_description": {
            "name": {"de": "Die Schuh-Beschreibung", "en": "The Shoe Description"},
            "text": {"de": "Fritz erinnert sich: Dunkle Schuhe. Kein Absatz. Schmal. Und: Eine ungewoehnliche Schnalle — silbern, dreieckig. Wer traegt so eine Schnalle?", "en": "Fritz remembers: dark shoes. No heel. Narrow. And: an unusual buckle — silver, triangular. Who wears such a buckle?"}
        },
        "time_of_exit": {
            "name": {"de": "Die Abgangszeit", "en": "The Exit Time"},
            "text": {"de": "22:47 Uhr. Fritz ist sicher — er hat nach dem Wanduhr-Klingeln gezaehlt. Zwanzig Minuten nach dem was der Scheckenprufer behauptet. Aber vor dem Tod um 23:00.", "en": "10:47pm. Fritz is certain — he counted after the wall clock chimed. Twenty minutes after what the safe cracker claims. But before death at 11pm."}
        },
        "bellboy_room_service_log": {
            "name": {"de": "Zimmerservice-Log", "en": "Room Service Log"},
            "text": {"de": "Fritz Lieferliste: 22:30 Zimmer 9 (Vogel). 22:40 Zimmer 14 (Braun). 22:47 Vorbei an Zimmer 12 — da sah er es. 23:00 Zimmer 6 (Kraft). Er war den ganzen Abend unterwegs.", "en": "Fritz delivery list: 10:30pm room 9 (Vogel). 10:40pm room 14 (Braun). 10:47pm past room 12 — that's when he saw it. 11pm room 6 (Kraft). He was out all evening."}
        },
        "corridor_lamp_note": {
            "name": {"de": "Die Korridor-Lampe", "en": "The Corridor Lamp"},
            "text": {"de": "Die Lampe vor Zimmer 12 war um 22:47 gedimmt — Fritz musste sich die Augen reiben. Er sah deshalb kein Gesicht. Aber Groesse, Haltung und Schuhe — die sah er.", "en": "The lamp before room 12 was dimmed at 10:47pm — Fritz had to rub his eyes. Therefore he saw no face. But height, posture and shoes — those he saw."}
        },
        # Erpressungskette
        "steinberg_fraud_note": {
            "name": {"de": "Steinbergs Betrugsnotiz", "en": "Steinberg's Fraud Note"},
            "text": {"de": "In Steinbergs Kalender: 'K.M. weiss alles. Zahlung lauft. Kann nicht aufhoeren.' K.M. — Karl Meier. Seit sechs Jahren.", "en": "In Steinberg's calendar: 'K.M. knows everything. Payment running. Cannot stop.' K.M. — Karl Meier. For six years."}
        },
        "monthly_payments_record": {
            "name": {"de": "Monatsueberweisungen", "en": "Monthly Payments"},
            "text": {"de": "Sechs Jahre Monatsueberweisung. 2.000 CHF monatlich. Empfaenger: Karl Meier. Letzter Monat: Nicht ausgefuehrt. Steinberg hatte sie gestoppt.", "en": "Six years of monthly transfers. 2,000 CHF monthly. Recipient: Karl Meier. Last month: not executed. Steinberg had stopped them."}
        },
        "briefcase_document_1": {
            "name": {"de": "Aktentasche Dokument 1", "en": "Briefcase Document 1"},
            "text": {"de": "Aus Elsas Aktentasche (falls geoeffnet): Ein Schuldschein. Aussteller: Hugo Steinberg. Berechtigter: Karl Meier. Betrag: 80.000 CHF. Mit Steinbergs Unterschrift. Faelschlich?", "en": "From Elsa's briefcase (if opened): a promissory note. Issuer: Hugo Steinberg. Beneficiary: Karl Meier. Amount: 80,000 CHF. With Steinberg's signature. Forged?"}
        },
        "secretary_notebook_page": {
            "name": {"de": "Sekretaers-Notizbuch Seite 47", "en": "Secretary's Notebook Page 47"},
            "text": {"de": "Seite 47 von Meiers Notizbuch: Verschluesselt. Entziffert: '2000 CHF/Mon. Betrug 1921. Zeuge: [NAME UNLESERLICH].' Er hat noch einen Zeugen — oder hatte.", "en": "Page 47 of Meier's notebook: encrypted. Deciphered: '2000 CHF/month. Fraud 1921. Witness: [NAME ILLEGIBLE].' He has another witness — or had."}
        },
        # Schluessekette
        "master_key_copy": {
            "name": {"de": "Die Hauptschluessel-Kopie", "en": "The Master Key Copy"},
            "text": {"de": "Im Buero des Direktors: Eine Schluesselduplikat-Maschine. Und ein frischer Schluesselrohling. Jemand hat sich eine Kopie des Hauptschluessels gemacht. Heute.", "en": "In the director's office: a key duplicating machine. And a fresh key blank. Someone made a copy of the master key. Today."}
        },
        "room_12_spare_key": {
            "name": {"de": "Ersatzschluessel Zimmer 12", "en": "Spare Key Room 12"},
            "text": {"de": "Im Schluesselbrett hinter der Rezeption fehlt der Ersatzschluessel fuer Zimmer 12. Er haengt dort seit drei Jahren. Heute Abend ist er weg.", "en": "On the key board behind reception the spare key for room 12 is missing. It has hung there for three years. Tonight it is gone."}
        },
        "client_commission_note": {
            "name": {"de": "Der Auftrags-Zettel", "en": "The Commission Note"},
            "text": {"de": "Bei der Schattenfigur (falls entdeckt): Ein Zettel. 'Safe Zimmer 12. Inhalt: alles. Honorar: 5.000 CHF. Schluessel liegt bereit.' Kein Name des Auftraggebers — aber die Handschrift.", "en": "With the shadow figure (if discovered): a note. 'Safe room 12. Contents: everything. Fee: 5,000 CHF. Key will be available.' No name of the client — but the handwriting."}
        },
        "key_exchange_witnessed": {
            "name": {"de": "Schluesseltausch gesehen", "en": "Key Exchange Witnessed"},
            "text": {"de": "Fritz hat heute Nachmittag gesehen wie jemand dem Hotelpage einen Zettel gab — und dieser ihm etwas zurueckgab. Klein. Metallisch. Ein Schluessel?", "en": "Fritz saw this afternoon someone give the hotel bellboy a note — and he gave them something back. Small. Metallic. A key?"}
        },
        # Sonderkarten
        "hotel_register": {
            "name": {"de": "Das Hotelregister", "en": "The Hotel Register"},
            "text": {"de": "Alle Gaeste sind eingetragen mit Ankunftszeit. Einige kommen sich durch das Register — drei haben sich unter falschem Namen eingetragen. Welche drei?", "en": "All guests are registered with arrival time. Some come through the register — three registered under false names. Which three?"}
        },
        "door_forced_note": {
            "name": {"de": "Die Einbruchsnotiz", "en": "The Break-in Note"},
            "text": {"de": "Der Direktor hat notiert: Tuer aufgebrochen um 23:15. Safe offen. Keine Leiche sichtbar — er lag im Bad. Fenster offen. Handschuh-Faden am Safe.", "en": "The director noted: door forced at 11:15pm. Safe open. No body visible — he was in the bathroom. Window open. Glove thread on the safe."}
        },
        "steinberg_interview_refusal": {
            "name": {"de": "Die Interview-Ablehnung", "en": "The Interview Refusal"},
            "text": {"de": "Ein Brief von Steinberg an Schwarz: 'Herr Schwarz, ich lehne Ihr Interview-Gesuch ab. Meine Geschaefte sind nicht oeffentlich. Sollten Sie weiter recherchieren — werden Sie die Konsequenzen spueren.' Datum: Letzte Woche.", "en": "A letter from Steinberg to Schwarz: 'Mr Schwarz, I decline your interview request. My business is not public. Should you continue researching — you will feel the consequences.' Date: last week."}
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PHYSISCHE AUFGABEN (63 Stueck)
    # ─────────────────────────────────────────────────────────────────────────
    "physical_tasks": {

        # ── EROEFFNUNG ────────────────────────────────────────────────────────

        "task_opening_snowstorm": {
            "trigger_phase": 1, "trigger_condition": "game_started_immediately",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Host sagt: Der Schneesturm hat das Hotel vollstaendig isoliert. Kein Telefon. Kein Ausgang. Der Zug nach Zermatt ist eingeschneit. Ihr seid allein. Dann: Stille.",
                "en": "The host says: The snowstorm has completely isolated the hotel. No telephone. No exit. The train to Zermatt is snowed in. You are alone. Then: silence.",
            }, "game_effect": "snowstorm_established"
        },

        "task_director_intro": {
            "trigger_phase": 1, "trigger_condition": "game_started_1min",
            "assigned_to": "director",
            "instruction": {
                "de": "Steh auf. Sag: Im Namen des Grand Hotel Alpina bitte ich um Ihre Kooperation. Herr Steinberg wurde heute Nacht tot aufgefunden. Niemand verlaesst diesen Raum bis die Wahrheit ans Licht kommt. Dann setz dich wieder.",
                "en": "Stand up. Say: On behalf of the Grand Hotel Alpina I request your cooperation. Mr Steinberg was found dead tonight. Nobody leaves this room until the truth comes to light. Then sit back down.",
            }, "game_effect": "director_authority_established"
        },

        "task_room_assignments": {
            "trigger_phase": 1, "trigger_condition": "game_started_2min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Jeder erhaelt seine Zimmernummer. Lies sie laut vor. Dein Zimmer ist dein Alibi-Ort — du behauptest dort gewesen zu sein. Ob das stimmt entscheidest du.",
                "en": "Everyone receives their room number. Read it aloud. Your room is your alibi location — you claim to have been there. Whether that is true is your decision.",
            }, "game_effect": "rooms_assigned"
        },

        "task_gluehwein_toast": {
            "trigger_phase": 1, "trigger_condition": "game_started_3min",
            "assigned_to": "director",
            "instruction": {
                "de": "Gluehwein (oder Wein) einschenken fuer alle. Sag: Auf Herrn Steinberg — er war unser bester Gast. Alle trinken. Wer nicht trinkt wird bemerkt.",
                "en": "Pour gluehwein (or wine) for everyone. Say: To Mr Steinberg — he was our best guest. Everyone drinks. Whoever does not drink will be noticed.",
            }, "game_effect": "opening_drink"
        },

        "task_widow_briefcase": {
            "trigger_phase": 1, "trigger_condition": "game_started_5min",
            "assigned_to": "widow",
            "instruction": {
                "de": "Lege die Aktentasche demonstrativ auf den Tisch. Leg eine Hand drauf. Sag: Das ist Hugos Eigentum. Ich entscheide wann es geoeffnet wird. Dann lehne dich zurueck.",
                "en": "Place the briefcase demonstratively on the table. Put one hand on it. Say: This is Hugo's property. I decide when it is opened. Then lean back.",
            }, "game_effect": "briefcase_established"
        },

        "task_bellboy_silent": {
            "trigger_phase": 1, "trigger_condition": "game_started_8min",
            "assigned_to": "bellboy",
            "instruction": {
                "de": "Sag die ersten 8 Minuten nichts ausser wenn jemand direkt fragt. Wenn gefragt: Ich habe nur meinen Zimmerservice gemacht. Mehr nicht. Das macht dich verdaechtig — und wichtig.",
                "en": "Say nothing for the first 8 minutes unless someone asks you directly. If asked: I only did my room service. Nothing more. This makes you suspicious — and important.",
            }, "game_effect": "bellboy_mysterious"
        },

        "task_thief_gloves": {
            "trigger_phase": 1, "trigger_condition": "game_started_6min",
            "assigned_to": "thief",
            "instruction": {
                "de": "Behalt deine Handschuhe an — drinnen, warm, beim Abendessen. Wenn jemand fragt: Schlechte Durchblutung. Das faellt auf. Das soll auffallen.",
                "en": "Keep your gloves on — inside, warm, at dinner. If asked: poor circulation. This will be noticed. It is meant to be noticed.",
            }, "game_effect": "thief_gloves_noted"
        },

        "task_safe_reveal": {
            "trigger_phase": 2, "trigger_condition": "body_discovered",
            "assigned_to": "director",
            "instruction": {
                "de": "Geh zur Safe-Box. Steh davor. Sag laut: Der Safe war offen als ich eintrat. Leer. Dann dreh dich um und schau alle an. Wer schaut weg?",
                "en": "Go to the safe box. Stand before it. Say aloud: The safe was open when I entered. Empty. Then turn around and look at everyone. Who looks away?",
            }, "game_effect": "safe_empty_announced"
        },

        "task_doctor_examine": {
            "trigger_phase": 2, "trigger_condition": "body_discovered_plus_2min",
            "assigned_to": "doctor",
            "instruction": {
                "de": "Steh auf. Geh zum gedachten Tatort (wo der Host einen Zettel TATORT platziert hat). Tu als ob du untersuchst. Dann sag laut: Das ist kein natuerlicher Tod. Mehr sage ich noch nicht.",
                "en": "Stand up. Go to the imagined crime scene (where the host placed a CRIME SCENE note). Pretend to examine. Then say aloud: This is not a natural death. I say no more for now.",
            }, "game_effect": "murder_confirmed"
        },

        "task_journalist_notebook": {
            "trigger_phase": 1, "trigger_condition": "game_started_10min",
            "assigned_to": "journalist",
            "instruction": {
                "de": "Hole dein Notizbuch heraus. Schreib sichtbar etwas. Wenn jemand fragt: Ich mache mir Notizen. Das ist mein Beruf. Diese Aussage macht alle nervoes.",
                "en": "Take out your notebook. Write something visibly. If asked: I am taking notes. That is my job. This statement makes everyone nervous.",
            }, "game_effect": "journalist_noted"
        },

        "task_auditor_demand": {
            "trigger_phase": 2, "trigger_condition": "investigation_begins",
            "assigned_to": "auditor",
            "instruction": {
                "de": "Steh auf. Sag: Im Auftrag der Schweizerischen Nationalbank fordere ich Einsicht in alle Geschaeftsdokumente die Herr Steinberg bei sich hatte. Setz dich wieder. Wer reagiert nervoes?",
                "en": "Stand up. Say: On behalf of the Swiss National Bank I demand access to all business documents Mr Steinberg had with him. Sit back down. Who reacts nervously?",
            }, "game_effect": "audit_demanded"
        },

        "task_secret_vote": {
            "trigger_phase": 2, "trigger_condition": "midgame_20min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle schreiben wer ihrer Meinung nach Zugang zum Safe hatte. Auf einen Zettel. Falten. Dem Host geben.",
                "en": "Everyone writes who in their opinion had access to the safe. On a note. Fold. Give to host.",
            }, "game_effect": "safe_access_vote"
        },

        "task_room_search_demand": {
            "trigger_phase": 2, "trigger_condition": "investigation_15min",
            "assigned_to": "detective",
            "instruction": {
                "de": "Steh auf. Sag: Ich ordne an: Jeder zeigt was er in der Jacke und in den Taschen hat. Jetzt. Sofort.",
                "en": "Stand up. Say: I order: everyone shows what they have in their jacket and pockets. Now. Immediately.",
            }, "game_effect": "pocket_check"
        },

        "task_mistress_card_swap": {
            "trigger_phase": 1, "trigger_condition": "game_started_12min",
            "assigned_to": "mistress",
            "instruction": {
                "de": "Tausche heimlich deine Visitenkarte aus — gib jemandem die zweite Karte mit dem anderen Namen. Wenn jemand fragt welche der richtige Name ist: Beide.",
                "en": "Secretly swap your business card — give someone the second card with the other name. If asked which is the real name: both.",
            }, "game_effect": "identity_swap"
        },

        "task_investor_drinks_fast": {
            "trigger_phase": 1, "trigger_condition": "game_started_7min",
            "assigned_to": "investor",
            "instruction": {
                "de": "Trink jetzt schnell — zu schnell. Dann bestell nach. Wenn jemand fragt: Ich bin nervoes. Das ist mein Recht. Der Wein hilft.",
                "en": "Drink quickly now — too quickly. Then order another. If asked: I am nervous. That is my right. The wine helps.",
            }, "game_effect": "braun_nervous_drinking"
        },

        # ── TRINK-AUFGABEN (10 Stueck) ────────────────────────────────────────

        "task_alpina_toast": {
            "trigger_phase": 1, "trigger_condition": "game_started_4min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle heben ihr Glas. Direktor sagt: Auf das Grand Hotel Alpina. Und auf die Wahrheit die heute Nacht ans Licht kommen wird. Alle trinken gleichzeitig. Wer zoegert?",
                "en": "Everyone raises their glass. Director says: To the Grand Hotel Alpina. And to the truth that will come to light tonight. Everyone drinks simultaneously. Who hesitates?",
            }, "game_effect": "alpina_toast"
        },

        "task_widow_tea_only": {
            "trigger_phase": 1, "trigger_condition": "widow_drinks",
            "assigned_to": "widow",
            "instruction": {
                "de": "Wenn jemand dir Wein anbietet: Nur Tee fuer mich. Kein Wein heute Nacht. Diese Ablehnung faellt auf — besonders weil du schwarz gekleidet bist.",
                "en": "When someone offers you wine: Only tea for me. No wine tonight. This refusal will be noticed — especially because you are dressed in black.",
            }, "game_effect": "widow_tea_noted"
        },

        "task_murderer_drinks_first": {
            "trigger_phase": 1, "trigger_condition": "first_toast",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Beim ersten Toast: Trinke als ERSTER und demonstrativ viel. Du hast keine Angst vor dem Wein. Weil du weisst was du getan hast und Wein nicht dein Problem ist.",
                "en": "At the first toast: drink FIRST and demonstratively much. You have no fear of the wine. Because you know what you did and wine is not your problem.",
            }, "game_effect": "murderer_drinks_first"
        },

        "task_group_drink_together": {
            "trigger_phase": 2, "trigger_condition": "investigation_10min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle trinken gleichzeitig — auf drei. Wer NICHT trinkt hat etwas zu verbergen. Das ist Schweizer Sitte. Niemand bricht sie ohne Grund.",
                "en": "Everyone drinks simultaneously — on three. Whoever does NOT drink has something to hide. That is Swiss custom. Nobody breaks it without reason.",
            }, "game_effect": "group_drink"
        },

        "task_journalist_wine_clue": {
            "trigger_phase": 2, "trigger_condition": "random_post_murder",
            "assigned_to": "journalist",
            "instruction": {
                "de": "Hebe dein Glas. Sag: Herr Steinberg hatte heute Abend beim Dinner seinen Nachttrunk bestellt — Whisky. Der Zimmerservice hat ihn geliefert. Wer hat noch Zimmerservice bestellt?",
                "en": "Raise your glass. Say: Mr Steinberg ordered his nightcap at dinner tonight — whisky. Room service delivered it. Who else ordered room service?",
            }, "game_effect": "nightcap_attention"
        },

        "task_safe_opener_drink": {
            "trigger_phase": 2, "trigger_condition": "random_25min",
            "assigned_to": "random",
            "instruction": {
                "de": "Trinke demonstrativ und sag dann: Im Safe lagen Dinge die manchen von euch den Schlaf rauben sollten. Sag nichts mehr. Beobachte wer aufhorcht.",
                "en": "Drink demonstratively and then say: In the safe were things that should cost some of you your sleep. Say nothing more. Observe who perks up.",
            }, "game_effect": "safe_content_hint"
        },

        "task_director_gluehwein_2": {
            "trigger_phase": 2, "trigger_condition": "investigation_20min",
            "assigned_to": "director",
            "instruction": {
                "de": "Fuell nochmals Gluehwein nach — aber diesmal nur bestimmten Personen. Geh zu zwei die du verdaechtigst. Schau ihnen dabei in die Augen.",
                "en": "Refill gluehwein again — but this time only for specific people. Go to two you suspect. Look them in the eyes while doing so.",
            }, "game_effect": "director_selection"
        },

        "task_last_drink_steinberg": {
            "trigger_phase": 3, "trigger_condition": "reckoning_near",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle trinken nochmals. Auf Hugo Steinberg — wer auch immer ihn getoetest hat. Wer nicht trinkt ehrt ihn nicht. Wer zu schnell trinkt hat ein schlechtes Gewissen.",
                "en": "Everyone drinks once more. To Hugo Steinberg — whoever killed him. Whoever does not drink does not honour him. Whoever drinks too quickly has a guilty conscience.",
            }, "game_effect": "final_steinberg_drink"
        },

        "task_doctor_drink_slow": {
            "trigger_phase": 2, "trigger_condition": "investigation_15min",
            "assigned_to": "doctor",
            "instruction": {
                "de": "Trinke jetzt sehr langsam — ein einziger langer Schluck. Dabei schau nur auf das Glas. Sag dann: Ein Mensch ist tot. Ich finde das schwer zu verdauen.",
                "en": "Drink very slowly now — one single long sip. While doing so look only at the glass. Then say: A person is dead. I find that hard to digest.",
            }, "game_effect": "doctor_drink_pause"
        },

        "task_investor_whisky_neat": {
            "trigger_phase": 2, "trigger_condition": "random_30min",
            "assigned_to": "investor",
            "instruction": {
                "de": "Bestell einen Whisky — pur, kein Eis. Exakt wie Steinberg es hatte. Wenn jemand das bemerkt und fragt: Zufall. Kein Zufall.",
                "en": "Order a whisky — neat, no ice. Exactly as Steinberg had it. If someone notices and asks: coincidence. Not coincidence.",
            }, "game_effect": "braun_whisky_noted"
        },

        # ── KETTENAUFGABEN (12 Stueck) ─────────────────────────────────────────

        "chain_a1_director_widow": {
            "trigger_phase": 2, "trigger_condition": "both_suspects_high",
            "assigned_to": "director",
            "instruction": {
                "de": "Geh zur Witwe. Sag leise aber hoerbar: Frau Steinberg — der Hauptschluessel meines Hotels. Wer hat ihn heute Abend benutzt ausser mir? Ich weiss es. Warten Sie.",
                "en": "Go to the widow. Say quietly but audibly: Mrs Steinberg — my hotel's master key. Who used it tonight apart from me? I know. Wait.",
            }, "game_effect": "chain_director_confronts_widow",
            "triggers_chain": "chain_a2_widow_response"
        },

        "chain_a2_widow_response": {
            "trigger_phase": 2, "trigger_condition": "director_confronts_widow",
            "assigned_to": "widow",
            "instruction": {
                "de": "Der Direktor hat dich konfrontiert. Du entscheidest: Oeffne jetzt die Aktentasche ('Ich zeige was Hugo wirklich hinterlassen hat') — oder leugne alles.",
                "en": "The director confronted you. You decide: open the briefcase now ('I will show what Hugo truly left behind') — or deny everything.",
            }, "game_effect": "widow_briefcase_response"
        },

        "chain_b1_journalist_auditor": {
            "trigger_phase": 2, "trigger_condition": "investigation_8min",
            "assigned_to": "journalist",
            "instruction": {
                "de": "Geh zur Wirtschaftspruferin. Fluestere ihr: Ich weiss was Sie hier wirklich machen. Nationalbank-Auftrag. Ich kann Ihnen helfen — gegen ein Interview.",
                "en": "Go to the auditor. Whisper to her: I know what you are really doing here. National Bank commission. I can help you — in exchange for an interview.",
            }, "game_effect": "chain_journalist_auditor",
            "triggers_chain": "chain_b2_auditor_response"
        },

        "chain_b2_auditor_response": {
            "trigger_phase": 2, "trigger_condition": "journalist_approaches_auditor",
            "assigned_to": "auditor",
            "instruction": {
                "de": "Der Journalist weiss von deinem Auftrag. Entscheide: Kooperiere ('Ich erzaehle dir was ich in den Buechern gefunden habe') oder weise ihn ab.",
                "en": "The journalist knows about your commission. Decide: cooperate ('I will tell you what I found in the books') or reject him.",
            }, "game_effect": "auditor_journalist_response"
        },

        "chain_c1_bellboy_reveals": {
            "trigger_phase": 2, "trigger_condition": "investigation_12min",
            "assigned_to": "bellboy",
            "instruction": {
                "de": "Steh jetzt auf. Sag laut: Ich habe etwas gesehen. Um 22:47 Uhr kam jemand aus Zimmer 12. Ich habe das Gesicht nicht gesehen. Aber die Schuhe.",
                "en": "Stand up now. Say aloud: I saw something. At 10:47pm someone came out of room 12. I did not see the face. But the shoes.",
            }, "game_effect": "chain_bellboy_testimony",
            "triggers_chain": "chain_c2_murderer_reacts"
        },

        "chain_c2_murderer_reacts": {
            "trigger_phase": 2, "trigger_condition": "bellboy_testifies",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Der Page hat gesprochen. Er sah jemanden — vielleicht dich. Reagiere JETZT: Bleib voellig ruhig (schwer aber moeglich) ODER lenke sofort ab ('Ich war es nicht — ich war in Zimmer X').",
                "en": "The bellboy has spoken. He saw someone — perhaps you. React NOW: stay completely calm (difficult but possible) OR immediately deflect ('It wasn't me — I was in room X').",
            }, "game_effect": "murderer_bellboy_reaction"
        },

        "chain_d1_secretary_briefcase": {
            "trigger_phase": 2, "trigger_condition": "secretary_under_pressure",
            "assigned_to": "secretary",
            "instruction": {
                "de": "Geh zur Witwe. Sag leise: In Ihrer Aktentasche liegt ein Dokument das mich betrifft. Ich moechte es diskret mit Ihnen besprechen. Wann haben Sie Zeit?",
                "en": "Go to the widow. Say quietly: In your briefcase is a document that concerns me. I would like to discuss it discreetly with you. When do you have time?",
            }, "game_effect": "chain_secretary_briefcase",
            "triggers_chain": "chain_d2_widow_decides_secretary"
        },

        "chain_d2_widow_decides_secretary": {
            "trigger_phase": 2, "trigger_condition": "secretary_approaches_widow",
            "assigned_to": "widow",
            "instruction": {
                "de": "Der Sekretar hat dich angesprochen. Er will das Dokument ueber seine Erpressung. Entscheide: Lass ihn zappeln (moeglicherweise nuetzlicher Verbundeter) oder konfrontiere ihn oeffentlich.",
                "en": "The secretary approached you. He wants the document about his blackmail. Decide: let him sweat (potentially useful ally) or confront him publicly.",
            }, "game_effect": "widow_secretary_decision"
        },

        "chain_e1_investor_envelope": {
            "trigger_phase": 2, "trigger_condition": "safe_contents_discussed",
            "assigned_to": "investor",
            "instruction": {
                "de": "Hole den versiegelten Umschlag aus deiner Jacke. Zeig ihn — sage aber nichts. Lass alle schauen. Dann steck ihn wieder weg. Wer greift danach? Wer sagt was?",
                "en": "Take the sealed envelope from your jacket. Show it — but say nothing. Let everyone look. Then put it away again. Who reaches for it? Who says something?",
            }, "game_effect": "chain_investor_envelope",
            "triggers_chain": "chain_e2_journalist_reacts"
        },

        "chain_e2_journalist_reacts": {
            "trigger_phase": 2, "trigger_condition": "investor_shows_envelope",
            "assigned_to": "journalist",
            "instruction": {
                "de": "Braun hat einen Umschlag gezeigt. Das koennte die Geschichte sein. Geh zu ihm. Sag: Was ist in dem Umschlag Herr Braun? Ich frage als Journalist — offiziell.",
                "en": "Braun showed an envelope. That could be the story. Go to him. Say: What is in the envelope Mr Braun? I ask as journalist — officially.",
            }, "game_effect": "journalist_demands_envelope"
        },

        "chain_f1_detective_interrogation": {
            "trigger_phase": 2, "trigger_condition": "investigation_midpoint",
            "assigned_to": "detective",
            "instruction": {
                "de": "Ruf jetzt ein offizielles Verhoer aus. Alle verlassen den Raum. Du redest 3 Minuten allein mit einer Person. Nach dem Verhoer: Alle sagen ob sie kooperativ war.",
                "en": "Call an official interrogation now. Everyone leaves the room. You talk alone with one person for 3 minutes. After interrogation: everyone says if they were cooperative.",
            }, "game_effect": "interrogation_called",
            "triggers_chain": "chain_f2_post_interrogation"
        },

        "chain_f2_post_interrogation": {
            "trigger_phase": 2, "trigger_condition": "interrogation_done",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Inspektor kehrt zurueck. Jeder sagt nacheinander — war die befragte Person 'kooperativ' oder 'ausweichend'? Ein Satz. Kein Herumreden.",
                "en": "The inspector returns. Everyone says in turn — was the questioned person 'cooperative' or 'evasive'? One sentence. No talking around it.",
            }, "game_effect": "post_interrogation"
        },

        # ── MOERDER-AUFGABEN (8 Stueck) ────────────────────────────────────────

        "murderer_task_window_alibi": {
            "trigger_phase": 2, "trigger_condition": "murder_announced",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Wenn nach Zimmer 12 und dem Fenster gefragt wird: Betone dass du im ZWEITEN STOCK nicht ohne Verletzungen haettest entkommen koennen. Das legt den Verdacht auf andere.",
                "en": "When room 12 and the window are discussed: emphasize that you could not have escaped from the SECOND FLOOR without injury. This directs suspicion at others.",
            }, "game_effect": "murderer_window_alibi"
        },

        "murderer_task_safe_distraction": {
            "trigger_phase": 2, "trigger_condition": "safe_content_discussed",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Lenke jetzt auf den Safe-Diebstahl als separates Verbrechen. 'Vielleicht war der Dieb der Moerder?' Das ist falsch — aber klingt logisch. Nutze es.",
                "en": "Now redirect to the safe theft as a separate crime. 'Perhaps the thief was the murderer?' This is wrong — but sounds logical. Use it.",
            }, "game_effect": "murderer_safe_distraction"
        },

        "murderer_task_sympathy": {
            "trigger_phase": 2, "trigger_condition": "doctor_confirms_murder",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Reagiere mit echter oder gespielter Erschuetterung auf die Bestaetiging des Mordes. 'Wer tut so etwas? In einem Hotel?' Du darfst weinen. Es sieht gut aus.",
                "en": "React with genuine or performed shock to the murder confirmation. 'Who does something like that? In a hotel?' You may cry. It looks good.",
            }, "game_effect": "murderer_sympathy"
        },

        "murderer_task_question": {
            "trigger_phase": 2, "trigger_condition": "investigation_5min",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Stelle eine Frage die Verdacht ablenkt. Gut: 'Wer ausser dem Direktor hatte Zugang zum Hauptschluessel?' Oder: 'Wer kannte die Safe-Kombination?'",
                "en": "Ask a question that deflects suspicion. Good: 'Who besides the director had access to the master key?' Or: 'Who knew the safe combination?'",
            }, "game_effect": "murderer_deflection"
        },

        "murderer_task_bellboy_intimidate": {
            "trigger_phase": 2, "trigger_condition": "bellboy_about_to_speak",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Der Page will reden. Handle bevor er es tut. Geh zu ihm. Sag leise: 'Was Sie glauben gesehen zu haben — war die Lampe nicht gedimmt? Im schlechten Licht sieht man vieles falsch.'",
                "en": "The bellboy wants to speak. Act before he does. Go to him. Say quietly: 'What you think you saw — wasn't the lamp dimmed? In poor light one sees many things wrong.'",
            }, "game_effect": "murderer_bellboy_intimidation"
        },

        "murderer_task_help_investigation": {
            "trigger_phase": 3, "trigger_condition": "investigation_later",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Hilf dem Inspektor aktiv. 'Darf ich vorschlagen wir rekonstruieren die Bewegungen aller Gaeste zwischen 22:30 und 23:00?' Wer hilft steht nicht im Verdacht.",
                "en": "Actively help the inspector. 'May I suggest we reconstruct the movements of all guests between 10:30 and 11pm?' Whoever helps is not suspected.",
            }, "game_effect": "murderer_helper"
        },

        "murderer_task_accuse_specific": {
            "trigger_phase": 3, "trigger_condition": "suspicion_rising_on_murderer",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Jetzt ist der Moment. Beschuldige konkret eine Person mit einem echten Geheimnis das du kennst. Nicht den Moerder beschuldigen: eine unschuldige Person mit einem Motiv.",
                "en": "Now is the moment. Concretely accuse a specific person using a real secret you know. Don't accuse the murderer: an innocent person with a motive.",
            }, "game_effect": "murderer_accusation"
        },

        "murderer_panic": {
            "trigger_phase": 3, "trigger_condition": "someone_gets_close",
            "assigned_to": "murderer", "private": True,
            "time_limit_seconds": 60,
            "instruction": {
                "de": "PANIKMOMENT 60 SEKUNDEN. Waehle JETZT:\n\nA — FENSTER: 'Ich haette das Fenster nicht benutzen koennen — schauen Sie meine Haende an. Keine Abschuerfungen.'\n\nB — ALIBI: Bekraeftige deinen Zeugen nochmals. Persoenlich. Direkt.\n\nC — DER SAFE: Lenke alles auf den Safe-Diebstahl. 'Der Dieb ist der Moerder — der Safe war der Grund.'\n\nD — DER ZUSAMMENBRUCH: Werde emotional. Lass es aus dir heraus. Niemand verdaechtigt jemanden der echten Schmerz zeigt.\n\nE — DIE GEGENANKLAGE: Sofort eine andere Person beschuldigen mit einem wahren Detail.\n\nJetzt. 60 Sekunden.",
                "en": "PANIC MOMENT 60 SECONDS. Choose NOW:\n\nA — WINDOW: 'I could not have used the window — look at my hands. No abrasions.'\n\nB — ALIBI: Reinforce your witness once more. Personally. Directly.\n\nC — THE SAFE: Redirect everything to the safe theft. 'The thief is the murderer — the safe was the reason.'\n\nD — THE BREAKDOWN: Become emotional. Let it out. Nobody suspects someone showing real pain.\n\nE — THE COUNTER-ACCUSATION: Immediately accuse another person with a true detail.\n\nNow. 60 seconds.",
            }, "game_effect": "panic_triggered"
        },

        # ── VERBINDUNGS-AUFGABEN ──────────────────────────────────────────────

        "task_ghost_whisper_1": {
            "trigger_phase": 2, "trigger_condition": "investigation_5min",
            "assigned_to": "doctor",
            "instruction": {
                "de": "Geh zur Person die du am meisten verdaechtigst. Fluestere ihr: 'Ich weiss was ich im Safe gesehen habe. Wenn Sie wuessen was dort lag — wuerden Sie jetzt schwitzen.'",
                "en": "Go to the person you most suspect. Whisper to them: 'I know what I saw in the safe. If you knew what was in there — you would be sweating right now.'",
            }, "game_effect": "doctor_safe_hint"
        },

        "task_director_key_decision": {
            "trigger_phase": 2, "trigger_condition": "key_mentioned",
            "assigned_to": "director",
            "instruction": {
                "de": "Du hast den Hauptschluessel. Zeigst du ihn — alle sehen wer noch eine Kopie haben koennte. Versteckst du ihn — du wirkst verdaechtig. Deine Entscheidung.",
                "en": "You have the master key. Show it — everyone sees who might have a copy. Hide it — you appear suspicious. Your decision.",
            }, "game_effect": "master_key_decision"
        },

        "task_thief_reveal_client": {
            "trigger_phase": 2, "trigger_condition": "thief_under_pressure",
            "assigned_to": "thief",
            "instruction": {
                "de": "Du wirst unter Druck gesetzt. Jemand naehert sich der Wahrheit. Entscheide: Enthuelle wer dich beauftragt hat (riskant aber klaerend) ODER lenke auf den Moerder ab.",
                "en": "You are being put under pressure. Someone is approaching the truth. Decide: reveal who hired you (risky but clarifying) OR redirect to the murderer.",
            }, "game_effect": "thief_client_decision"
        },

        "task_widow_opens_briefcase": {
            "trigger_phase": 2, "trigger_condition": "widow_pressured",
            "assigned_to": "widow",
            "instruction": {
                "de": "Der Druck steigt. Jetzt oder nie — oeffne die Aktentasche oder sage: Ich oeffne sie wenn ich es fuer richtig halte. Noch nicht. Was du dann herausnimmst bestimmt das Spiel.",
                "en": "The pressure is rising. Now or never — open the briefcase or say: I will open it when I see fit. Not yet. What you then take out determines the game.",
            }, "game_effect": "briefcase_decision"
        },

        "task_secretary_notebook_show": {
            "trigger_phase": 2, "trigger_condition": "secretary_accused",
            "assigned_to": "secretary",
            "instruction": {
                "de": "Wenn du beschuldigt wirst: Nimm dein offizielles Notizbuch heraus. Zeig die letzten Seiten — offizielle Termine, normale Notizen. Das ist dein Alibi-Buch. Das andere — bleibt verborgen.",
                "en": "If you are accused: take out your official notebook. Show the last pages — official appointments, normal notes. This is your alibi book. The other one — stays hidden.",
            }, "game_effect": "secretary_notebook_alibi"
        },

        "task_all_silence_snow": {
            "trigger_phase": 2, "trigger_condition": "random_investigation",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Host oeffnet kurz das Fenster (oder tut so als ob). Sagt: Hoert ihr das? Der Schneesturm. Niemand kommt rein. Niemand kommt raus. Wir sind allein. 10 Sekunden Stille.",
                "en": "The host briefly opens the window (or pretends to). Says: Do you hear that? The snowstorm. Nobody comes in. Nobody comes out. We are alone. 10 seconds silence.",
            }, "game_effect": "snowstorm_reminder"
        },

        # ── ZUFALLS-MOMENTE (9 Stueck) ────────────────────────────────────────

        "random_phone_rings": {
            "trigger_phase": 2, "trigger_condition": "random_any_time",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Host sagt: Das Hoteltelefon klingelt. Dreimal. Dann Stille. Der Schneesturm hat die Leitungen unterbrochen. Oder jemand hat aufgelegt. Alle schauen sich an.",
                "en": "Host says: The hotel telephone rings. Three times. Then silence. The snowstorm has cut the lines. Or someone hung up. Everyone looks at each other.",
            }, "game_effect": "phone_rings"
        },

        "random_light_flicker": {
            "trigger_phase": 2, "trigger_condition": "atmosphere_trigger",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Licht kurz aus (2-3 Sekunden) und wieder an. Wer bewegt sich? Wer greift nach etwas? Alle sagen danach was sie gesehen haben.",
                "en": "Light briefly off (2-3 seconds) and back on. Who moves? Who reaches for something? Everyone says afterwards what they saw.",
            }, "game_effect": "light_flicker"
        },

        "random_snowstorm_intensifies": {
            "trigger_phase": 2, "trigger_condition": "random_post_murder",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Host sagt: Der Schneesturm wird staerker. Es hat angefangen zu schneien als Steinberg starb. Zufall? Das Fenster in Zimmer 12 war offen. Wer war draussen?",
                "en": "Host says: The snowstorm is intensifying. It started snowing when Steinberg died. Coincidence? The window in room 12 was open. Who was outside?",
            }, "game_effect": "storm_reminder"
        },

        "random_secret_message": {
            "trigger_phase": 2, "trigger_condition": "random_any_time",
            "assigned_to": "random",
            "instruction": {
                "de": "Schau heimlich auf dein Telefon. Dann steck es weg. Sag nichts. Wer sofort neugierig wird hat etwas zu verbergen — oder zu finden.",
                "en": "Look secretly at your phone. Then put it away. Say nothing. Whoever immediately becomes curious has something to hide — or to find.",
            }, "game_effect": "secret_message"
        },

        "random_knock_door": {
            "trigger_phase": 2, "trigger_condition": "random_post_murder_20min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Host klopft dreimal. Sagt: Jemand hat an der Hoteltuer geklopft. Niemand kann in diesem Sturm draussen sein. Wer von euch erwartet jemanden?",
                "en": "Host knocks three times. Says: Someone knocked at the hotel door. Nobody can be outside in this storm. Who among you is expecting someone?",
            }, "game_effect": "door_knock"
        },

        "random_fire_crackles": {
            "trigger_phase": 1, "trigger_condition": "game_started_15min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Host sagt: Das Feuer knistert. Draussen: Minus fuenfzehn Grad. Drinnen: Warme Luft und Geheimnisse. Jemand in diesem Raum hat heute Nacht etwas getan das er/sie nie vergessen wird.",
                "en": "Host says: The fire crackles. Outside: minus fifteen degrees. Inside: warm air and secrets. Someone in this room did something tonight they will never forget.",
            }, "game_effect": "fire_atmosphere"
        },

        "random_clock_midnight": {
            "trigger_phase": 2, "trigger_condition": "random_investigation",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Host sagt: Es schlaegt Mitternacht. Genau zu dieser Zeit — war Steinberg schon tot. Oder lebte er noch? Die Aerztin weiss es.",
                "en": "Host says: The clock strikes midnight. At exactly this time — was Steinberg already dead. Or was he still alive? The doctor knows.",
            }, "game_effect": "midnight_atmosphere"
        },

        "random_safe_mention": {
            "trigger_phase": 2, "trigger_condition": "random_30min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Host sagt: Erinnert euch: Im Safe lagen Dinge die mehrere von euch betrafen. Wer am meisten wollte dass diese Dinge verschwinden — der hatte das groesste Motiv.",
                "en": "Host says: Remember: in the safe were things that concerned several of you. Whoever most wanted these things to disappear — had the greatest motive.",
            }, "game_effect": "safe_motive_reminder"
        },

        "random_pre_final_vote": {
            "trigger_phase": 3, "trigger_condition": "reckoning_near",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle schreiben auf einen Zettel: Moerder, Safe-Dieb, Auftraggeber des Diebs. Drei Antworten. Falten. Dem Host geben. Wird am Ende verglichen.",
                "en": "Everyone writes on a note: murderer, safe thief, who hired the thief. Three answers. Fold. Give to host. Will be compared at the end.",
            }, "game_effect": "pre_final_vote"
        },

        # ── STANDARD-AUFGABEN (Fortsetzung) ──────────────────────────────────

        "task_auditor_pocket_check": {
            "trigger_phase": 2, "trigger_condition": "auditor_uses_ability",
            "assigned_to": "auditor",
            "instruction": {
                "de": "Steh auf. Sag: Im Auftrag der Nationalbank fordere ich: Alle zeigen was sie in der Jacke haben. Das ist nicht optional. Dann warte.",
                "en": "Stand up. Say: On behalf of the National Bank I request: everyone shows what they have in their jacket. This is not optional. Then wait.",
            }, "game_effect": "pocket_check_official"
        },

        "task_detective_writes": {
            "trigger_phase": 2, "trigger_condition": "detective_has_theory",
            "assigned_to": "detective",
            "instruction": {
                "de": "Schreib demonstrativ etwas auf. Laut genug dass alle das Kratzen hoeren. Wenn jemand fragt: Fakten. Nichts weiter.",
                "en": "Write something demonstratively. Loud enough for all to hear the scratching. If asked: Facts. Nothing further.",
            }, "game_effect": "detective_notes"
        },

        "task_thief_pouch_noticed": {
            "trigger_phase": 2, "trigger_condition": "thief_moves",
            "assigned_to": "random",
            "instruction": {
                "de": "Wenn die Schattenfigur sich bewegt: Weise alle darauf hin. 'Hat das jemand gehoert? Dieser Beutel klingt voll.' Du hast das Recht es zu sagen.",
                "en": "When the shadow figure moves: draw everyone's attention. 'Did anyone hear that? That pouch sounds full.' You have the right to say it.",
            }, "game_effect": "pouch_noticed"
        },

        "task_all_room_check": {
            "trigger_phase": 2, "trigger_condition": "investigation_25min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle nennen nochmals ihr Zimmer und sagen: Wo genau waren sie zwischen 22:00 und 23:00? Eine Aussage pro Person. Keine langen Erklaerungen.",
                "en": "Everyone names their room again and says: Where exactly were they between 10pm and 11pm? One statement per person. No long explanations.",
            }, "game_effect": "alibi_round"
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # 14 VERBINDUNGEN
    # ─────────────────────────────────────────────────────────────────────────
    "role_connections": {
        "director_murder_scene": {
            "roles": ["director", "murderer"],
            "connection": "Der Direktor war als erster am Tatort. Er hat etwas gesehen — aber er hat es noch nicht gesagt.",
            "tension": "critical"
        },
        "widow_secretary_knows": {
            "roles": ["widow", "secretary"],
            "connection": "Der Sekretar weiss von Steinbergs Geliebter. Die Witwe weiss dass der Sekretar es weiss. Beide schweigen — aber aus verschiedenen Gruenden.",
            "tension": "mutual_leverage"
        },
        "secretary_thief_connection": {
            "roles": ["secretary", "thief"],
            "connection": "Jemand hat die Schattenfigur beauftragt. Der Sekretar kannte die Safe-Kombination. Ist das Zufall?",
            "tension": "suspected_link"
        },
        "investor_auditor_hunting": {
            "roles": ["investor", "auditor"],
            "connection": "Die Wirtschaftspruferin jagt Braun. Braun weiss nicht wer sie wirklich ist — noch nicht.",
            "tension": "hunter_hunted"
        },
        "doctor_investor_secret": {
            "roles": ["doctor", "investor"],
            "connection": "Die Aerztin hat zufaellig im Safe etwas ueber Braun gelesen. Sie weiss seinen Betrug. Er weiss nicht dass sie es weiss.",
            "tension": "one_sided_knowledge"
        },
        "journalist_investor_story": {
            "roles": ["journalist", "investor"],
            "connection": "Leon Schwarz recherchiert seit sechs Monaten ueber Braun. Braun weiss es — er hat Steinberg gedroht Schwarz loszuschicken.",
            "tension": "known_threat"
        },
        "bellboy_murderer_witness": {
            "roles": ["bellboy", "murderer"],
            "connection": "Fritz hat jemanden aus Zimmer 12 kommen gesehen. Der Moerder weiss es noch nicht. Das ist der gefaehrlichste Moment des Spiels.",
            "tension": "dramatic_irony_extreme"
        },
        "mistress_widow_rival": {
            "roles": ["mistress", "widow"],
            "connection": "Elsa weiss wer die Unbekannte ist. Die Unbekannte weiss dass Elsa es weiss. Beide haben Motiv. Beide haben Zimmer-Zugang.",
            "tension": "dual_suspects"
        },
        "inspector_investor_past": {
            "roles": ["detective", "investor"],
            "connection": "Haas und Braun haben gemeinsam studiert. Haas weiss Dinge ueber Braun die aktenkundig sind. Darf er sie verwenden?",
            "tension": "personal_conflict"
        },
        "thief_hired_mystery": {
            "roles": ["thief"],
            "connection": "Die Schattenfigur wurde beauftragt. Von wem? Das weiss nur sie — und der Auftraggeber.",
            "tension": "mystery_connection"
        },
        "doctor_director_first_aid": {
            "roles": ["doctor", "director"],
            "connection": "Der Direktor weiss dass aus dem Erste-Hilfe-Kasten Tabletten fehlen. Die Aerztin hatte Zugang. Er hat ihr noch nichts gesagt.",
            "tension": "silent_suspicion"
        },
        "secretary_investor_fraud": {
            "roles": ["secretary", "investor"],
            "connection": "Der Sekretar wusste vom Betrug von Steinberg und Braun — er hat die Buchaltung gefuehrt. Er schwieg weil er selbst erpresste.",
            "tension": "complicit_silence"
        },
        "journalist_auditor_alliance": {
            "roles": ["journalist", "auditor"],
            "connection": "Beide suchen die Wahrheit ueber Steinberg-Braun. Beide aus verschiedenen Gruenden. Eine Allianz koennte beiden nuetzen.",
            "tension": "potential_alliance"
        },
        "widow_doctor_access": {
            "roles": ["widow", "doctor"],
            "connection": "Die Witwe hatte freien Zugang zu Steinbergs Zimmer. Die Aerztin hatte Zugang zu toedlichen Substanzen. Gemeinsam wuerden sie perfekt zusammenpassen — aber haben sie zusammengearbeitet?",
            "tension": "dual_access"
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # EREIGNISKETTEN (7 Stueck)
    # ─────────────────────────────────────────────────────────────────────────
    "event_chains": [
        {
            "id": "chain_safe_attention",
            "trigger": "safe_mentioned_twice",
            "message_to_thief": {
                "de": "Der Safe wird immer wieder erwaehnt. Der Druck steigt. Was machst du mit dem was du darin gefunden hast?",
                "en": "The safe is mentioned repeatedly. The pressure is rising. What do you do with what you found inside?",
            }
        },
        {
            "id": "chain_bellboy_threatened",
            "trigger": "murderer_approaches_bellboy",
            "message_to_bellboy": {
                "de": "Jemand hat gerade versucht dich einzuschueechtern. Was tust du? Schweigst du — oder sagst du gerade deswegen die Wahrheit?",
                "en": "Someone just tried to intimidate you. What do you do? Do you stay silent — or do you tell the truth precisely because of that?",
            }
        },
        {
            "id": "chain_briefcase_pressure",
            "trigger": "briefcase_mentioned_three_times",
            "message_to_widow": {
                "de": "Alle schauen auf die Aktentasche. Der Druck ist maximal. Jetzt oder nie.",
                "en": "Everyone is looking at the briefcase. The pressure is at maximum. Now or never.",
            }
        },
        {
            "id": "chain_fraud_revealed",
            "trigger": "fraud_evidence_discussed",
            "message_to_investor": {
                "de": "Die Beweise des Betrugs kommen ans Licht. Was kannst du noch retten?",
                "en": "The fraud evidence is coming to light. What can you still save?",
            }
        },
        {
            "id": "chain_mistress_exposed",
            "trigger": "room4_key_found",
            "message_to_all": {
                "de": "In Zimmer 4 wurde ein Schluessel zu Zimmer 12 gefunden. Wer in Zimmer 4 wohnt — hatte Zugang.",
                "en": "In room 4 a key to room 12 was found. Whoever lives in room 4 — had access.",
            }
        },
        {
            "id": "chain_two_crimes",
            "trigger": "investigation_halfway",
            "message_to_all": {
                "de": "Es gab heute Nacht zwei Verbrechen: Den Mord und den Safe-Diebstahl. Moeglicherweise zwei verschiedene Taeter.",
                "en": "Tonight there were two crimes: the murder and the safe theft. Possibly two different perpetrators.",
            }
        },
        {
            "id": "chain_snowstorm_end",
            "trigger": "reckoning_begins",
            "message_to_all": {
                "de": "Der Schneesturm laesst nach. In drei Stunden kommt die Polizei. Was in drei Stunden nicht bewiesen ist — wird vielleicht nie bewiesen.",
                "en": "The snowstorm is easing. In three hours the police will come. What is not proven in three hours — may never be proven.",
            }
        }
    ],

    # ─────────────────────────────────────────────────────────────────────────
    # ATMOSPHAEREN-NACHRICHTEN
    # ─────────────────────────────────────────────────────────────────────────
    "atmosphere_messages": [
        {"trigger": "game_start_immediately", "text": {
            "de": "Zermatt, 1931. Das Grand Hotel Alpina. Ein Schneesturm. Kein Ausgang. Und irgendwo — liegt ein toter Millionaer.",
            "en": "Zermatt, 1931. The Grand Hotel Alpina. A snowstorm. No exit. And somewhere — lies a dead millionaire."}},
        {"trigger": "investigation_begins", "text": {
            "de": "Der Safe ist leer. Die Tuer war von innen versperrt. Das Fenster stand offen. Zwei Verbrechen — eine Nacht.",
            "en": "The safe is empty. The door was locked from inside. The window was open. Two crimes — one night."}},
        {"trigger": "investigation_10min", "text": {
            "de": "Das Feuer knistert. Der Sturm peitscht gegen die Scheiben. Irgendwo in diesem Raum sitzt ein Moerder.",
            "en": "The fire crackles. The storm lashes against the windows. Somewhere in this room sits a murderer."}},
        {"trigger": "investigation_20min", "text": {
            "de": "In drei Stunden kommt die Polizei. Was bis dahin nicht geklaert ist — bleibt vielleicht fuer immer ungeklaert.",
            "en": "In three hours the police will come. What is not resolved by then — may remain unresolved forever."}},
        {"trigger": "tension_high", "text": {
            "de": "Der Schnee bedeckt alle Spuren draussen. Aber die Spuren hier — im Raum — die kann niemand verstecken.",
            "en": "The snow covers all traces outside. But the traces here — in the room — those nobody can hide."}},
        {"trigger": "reckoning_soon", "text": {
            "de": "Es ist fast Morgen. Der Sturm laesst nach. Die Wahrheit hat keine Zeit mehr.",
            "en": "It is almost morning. The storm is easing. The truth has no more time."}}
    ],

    # ─────────────────────────────────────────────────────────────────────────
    # SPIELENDEN (5 Stueck)
    # ─────────────────────────────────────────────────────────────────────────
    "endings": {
        "murderer_caught": {
            "condition": "majority_names_murderer_correctly",
            "title": {"de": "Schneegericht", "en": "Snow Justice",
                      "fr": "Justice des Neiges", "it": "Giustizia della Neve",
                      "es": "Justicia en la Nieve", "pt": "Justica na Neve"},
            "text": {"de": "Der Moerder wurde gefasst — bevor die Polizei kam. Das Grand Hotel Alpina hat seine Ehre gerettet. Oder was davon uebrig war.", "en": "The murderer was caught — before the police came. The Grand Hotel Alpina has saved its honour. Or what was left of it."}
        },
        "murderer_escapes": {
            "condition": "wrong_person_convicted",
            "title": {"de": "Der Sturm traegt ihn davon", "en": "The Storm Carries Them Away",
                      "fr": "La Tempete l'Emporte", "it": "La Tempesta Lo Porta Via",
                      "es": "La Tormenta se lo lleva", "pt": "A Tempestade o Leva"},
            "text": {"de": "Ein Unschuldiger wurde beschuldigt. {murderer_name} ist verschwunden — unter dem Schutz des Schneesturms.", "en": "An innocent was accused. {murderer_name} has disappeared — under the protection of the snowstorm."}
        },
        "thief_wins": {
            "condition": "thief_escapes_with_safe_contents",
            "title": {"de": "Der Safe-Dieb gewinnt", "en": "The Safe Thief Wins"},
            "text": {"de": "Waehrend alle den Moerder suchten — verliess die Schattenfigur das Hotel mit dem Safe-Inhalt. In welcher Tasche? Niemand weiss es.", "en": "While everyone searched for the murderer — the Shadow figure left the hotel with the safe contents. In which bag? Nobody knows."}
        },
        "perfect_solve": {
            "condition": "detective_and_journalist_both_correct",
            "title": {"de": "Das vollstaendige Bild", "en": "The Complete Picture"},
            "text": {"de": "Der Inspektor und der Journalist haben gemeinsam alle Wahrheiten aufgedeckt: Moerder, Safe-Dieb, Auftraggeber, Betrug, Geliebte. Das ist aussergewoehnlich.", "en": "The inspector and the journalist together uncovered all truths: murderer, safe thief, client, fraud, mistress. That is extraordinary."}
        },
        "two_crimes_solved": {
            "condition": "murderer_caught_and_thief_discovered",
            "title": {"de": "Zwei Verbrechen — eine Nacht", "en": "Two Crimes — One Night"},
            "text": {"de": "Der Moerder wurde gefasst. Der Safe-Dieb entlarvt. Der Auftraggeber namentlich genannt. Das Grand Hotel Alpina wird morgen in jeder Zeitung stehen — aber aus den richtigen Gruenden.", "en": "The murderer was caught. The safe thief exposed. The client named. The Grand Hotel Alpina will be in every newspaper tomorrow — but for the right reasons."}
        }
    }
}
