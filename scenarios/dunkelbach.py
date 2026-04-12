# KRIMI DINNER — Das Herrenhaus Dunkelbach v3.0
# STATS: 10 Rollen | 58 Aufgaben | 32 Hinweise in 8 Ketten | 14 Verbindungen | 7 Ereignisketten | 5 Spielenden

SCENARIO = {
    "id": "dunkelbach",
    "title": "Das Herrenhaus Dunkelbach",
    "min_players": 4,
    "max_players": 10,
    "description": {
        "de": "Sommer 1923. Herrenhaus Dunkelbach im Schwarzwald. Eine Einladung die niemand ablehnen konnte — und eine Nacht die niemand vergessen wird. Baron Aldric von Dunkelbach ist tot. Aber wer von euch hat ihn getötet?",
        "en": "Summer 1923. Dunkelbach Manor in the Black Forest. An invitation nobody could decline — and a night nobody will forget. Baron Aldric von Dunkelbach is dead. But which of you killed him?"
    },

    "host_guide": {
        "before_game": {
            "de": [
                "BADEZIMMER: Hinter dem Spiegel verstecken: 'Wer als erstes nach der Bibliothek fragt hat etwas zu verbergen — Baron Aldric'",
                "SCHILLER-BUCH: Beliebiges Buch aufstellen. Darin Zettel: 'Blut ist dicker als Versprechen — A.' und ein Foto",
                "DAS GLAS DES BARONS: Ein besonderes Glas das sich von allen anderen unterscheidet",
                "VERSIEGELTER BRIEF: Fuer Constanze — Inhalt: 'Constanze — Die Wahrheit liegt hinter Schiller. — Aldric'",
                "HAUSHALTSBUCH: Beliebiges Notizbuch. Auf Seite 47 Zettel: 'Korrekturen — 8.400 Mark — 3 Jahre'",
                "KELLERZETTEL: In Kueche oder versteckt: 'Weinkeller W-7. Digitalis liegt hinter Jahrgang 1912.'",
                "TELEGRAMM: Zettel im Telegrammstil: 'HEUTE NACHT ENDET ALLES STOP ICH HABE ALLES STOP — KEIN ABSENDER'",
                "WEIN oder SEKT bereitstellen — Trinken ist Spielmechanik",
                "DER BARON SPIELT MIT: Nach Tod -> Geistmodus: Nur fluestern, nie laut"
            ]
        }
    },

    "roles": {

        "baron": {
            "name": {"de": "Baron Aldric von Dunkelbach", "en": "Baron Aldric von Dunkelbach",
                     "fr": "Baron Aldric von Dunkelbach", "it": "Barone Aldric von Dunkelbach",
                     "es": "Baron Aldric von Dunkelbach", "pt": "Barao Aldric von Dunkelbach"},
            "min_players": 4,
            "can_be_murderer": False,
            "ghost_mode": True,
            "intro": {
                "de": "Ich bin Baron Aldric von Dunkelbach. Ich habe euch alle eingeladen weil heute Nacht eine Wahrheit ans Licht kommt die zu lange verborgen war. Trinkt. Esst. Und beobachtet einander sehr genau.",
                "en": "I am Baron Aldric von Dunkelbach. I invited you all because tonight a truth comes to light that has been hidden too long. Drink. Eat. And observe each other very carefully.",
            },
            "appearance": {
                "de": "Elegant aber muede. Trinkt seinen Wein sehr langsam. Hat einen goldenen Siegelring den er dreht wenn er nachdenkt. Laechelt selten.",
                "en": "Elegant but tired. Drinks his wine very slowly. Has a gold signet ring he turns when thinking. Rarely smiles.",
            },
            "secret": {
                "de": "Du weisst dass jemand am Tisch dich toeten will. Deshalb die Einladung — du wolltest Zeugen. Deine Beweise liegen in der Bibliothek unter der dritten Bodendiele. Die App nennt dir den Moerder. Nenn ihn nie direkt.",
                "en": "You know someone at this table wants to kill you. That is why the invitation — you wanted witnesses. Your evidence is in the library under the third floorboard. The app names the murderer. Never name them directly.",
            },
            "ability": {
                "name": {"de": "Der Geist weiss am meisten", "en": "The Ghost Knows Most"},
                "description": {
                    "de": "Nach deinem Tod spielst du als Geist weiter. Einmal pro Phase darfst du einer Person einen wahren Hinweis zuflueastern. Du darfst nicken oder den Kopf schuetteln bei Ja/Nein-Fragen. Kein Wort laut vor allen.",
                    "en": "After your death you continue playing as ghost. Once per phase you may whisper one true clue to one person. You may nod or shake your head at yes/no questions. No word aloud before everyone.",
                }
            },
            "win_condition": {
                "de": "Der Moerder wird gefasst. Du gewinnst auch als Geist.",
                "en": "The murderer is caught. You win even as ghost.",
            },
            "clues_i_hold": ["barons_evidence", "library_key", "barons_diary_page"],
            "starting_knowledge": {
                "de": "Die App hat dir den Moerder genannt. Du weisst auch: Der Moerder hat heute Nachmittag einen Fehler gemacht. Jemand hat es gesehen — du weisst nicht wer.",
                "en": "The app named the murderer. You also know: the murderer made a mistake this afternoon. Someone saw it — you don't know who.",
            }
        },

        "butler": {
            "name": {"de": "Edmund, der Butler", "en": "Edmund, the Butler",
                     "fr": "Edmund, le Majordome", "it": "Edmund, il Maggiordomo",
                     "es": "Edmund, el Mayordomo", "pt": "Edmund, o Mordomo"},
            "min_players": 4,
            "can_be_murderer": True,
            "intro": {
                "de": "Edmund Kraus. 31 Jahre Butler in diesem Haus. Ich kenne jeden Winkel, jeden Keller, jede Tuer. Der Baron vertraute mir.",
                "en": "Edmund Kraus. 31 years butler in this house. I know every corner, every cellar, every door. The Baron trusted me.",
            },
            "appearance": {
                "de": "Weisse Handschuhe immer. Steht leicht abseits. Reibt Daumen und Zeigefinger aneinander wenn er luegt.",
                "en": "White gloves always. Stands slightly apart. Rubs thumb and forefinger together when lying.",
            },
            "secret": {
                "de": "Ich habe 8.400 Mark gestohlen ueber drei Jahre. Der Baron wusste es. Frist lief heute ab. Ich habe heute Nachmittag Constanze in der Bibliothek gesehen zwischen 16 und 17 Uhr.",
                "en": "I stole 8,400 marks over three years. The Baron knew. Deadline was today. I saw Constanze in the library this afternoon between 4 and 5pm.",
            },
            "ability": {
                "name": {"de": "Herr des Hauses", "en": "Master of the House"},
                "description": {
                    "de": "Einmal kannst du behaupten jemanden gesehen zu haben — Zeit, Ort, was sie taten. Wahr oder gelogen. Nur du weisst es.",
                    "en": "Once you may claim to have seen someone — time, place, what they were doing. True or lie. Only you know.",
                }
            },
            "win_condition": {
                "de": "Ueberlebe ohne dass dein Diebstahl bewiesen wird UND ohne als Moerder verurteilt zu werden.",
                "en": "Survive without your theft being proven AND without being convicted as murderer.",
            },
            "murderer_motive_if_assigned": {
                "de": "Edmund mixte Digitalis aus dem Weinkeller (Schluessel W-7) in den Wein des Barons.",
                "en": "Edmund mixed digitalis from the wine cellar (key W-7) into the Baron's wine.",
            },
            "clues_i_hold": ["key_cellar", "household_ledger"],
            "starting_knowledge": {
                "de": "Du hast zwischen 16 und 17 Uhr Constanze in der Bibliothek gesehen. Sie hielt das neue Testament. Sie weiss dass du sie gesehen hast.",
                "en": "You saw Constanze in the library between 4 and 5pm. She held the new will. She knows you saw her.",
            },
            "connection": {"with": "niece", "type": "library_witness"}
        },

        "niece": {
            "name": {"de": "Constanze, die Nichte", "en": "Constanze, the Niece",
                     "fr": "Constanze, la Niece", "it": "Constanze, la Nipote",
                     "es": "Constanze, la Sobrina", "pt": "Constanze, a Sobrinha"},
            "min_players": 4,
            "can_be_murderer": True,
            "intro": {
                "de": "Constanze von Dunkelbach. Die einzige Familie die der Baron anerkennt. Ich bin nicht wegen dem Dinner hier.",
                "en": "Constanze von Dunkelbach. The only family the Baron acknowledges. I am not here for the dinner.",
            },
            "appearance": {
                "de": "Elegant, angespannt. Traegt einen versiegelten Umschlag. Wechselt ihr Weinglas heimlich.",
                "en": "Elegant, tense. Carries a sealed envelope. Secretly switches her wine glass.",
            },
            "secret": {
                "de": "Das Testament wurde geaendert — ich erbe fast nichts. Ich war heute Nachmittag in der Bibliothek und habe es gelesen. Der Butler hat mich gesehen.",
                "en": "The will was changed — I inherit almost nothing. I was in the library this afternoon and read it. The butler saw me.",
            },
            "ability": {
                "name": {"de": "Der versiegelte Brief", "en": "The Sealed Letter"},
                "description": {
                    "de": "Du hast einen echten versiegelten Brief des Barons. Du entscheidest wann du ihn oeffnest. Je laenger du wartest desto verdaechtiger wirkst du.",
                    "en": "You have a real sealed letter from the Baron. You decide when to open it. The longer you wait the more suspicious you seem.",
                }
            },
            "win_condition": {
                "de": "Das neue Testament darf nicht gefunden werden. Wenn es gefunden wird: Nenne als erste den Moerder.",
                "en": "The new will must not be found. If it is found: name the murderer first.",
            },
            "murderer_motive_if_assigned": {
                "de": "Das neue Testament haette Constanze auf minimalen Erbanteil reduziert. In der Bibliothek fand sie die Gelegenheit.",
                "en": "The new will would have reduced Constanze to minimal inheritance. In the library she found the opportunity.",
            },
            "clues_i_hold": ["sealed_letter", "new_will_location"],
            "starting_knowledge": {
                "de": "Du warst in der Bibliothek — Testament hinter den Rechtsbüchern, drittes Regal. Der Butler hat dich gesehen.",
                "en": "You were in the library — will behind the law books, third shelf. The butler saw you.",
            },
            "connection": {"with": "butler", "type": "library_witness"}
        },

        "witness": {
            "name": {"de": "Marta, die Schriftstellerin", "en": "Marta, the Writer",
                     "fr": "Marta, l'Ecrivaine", "it": "Marta, la Scrittrice",
                     "es": "Marta, la Escritora", "pt": "Marta, a Escritora"},
            "min_players": 4,
            "can_be_murderer": False,
            "intro": {
                "de": "Marta Stein. Ich schreibe. Ich beobachte. Ich vergesse nichts. Der Baron kannte meine Mutter. Ich wollte nur ein ruhiges Dinner.",
                "en": "Marta Stein. I write. I observe. I forget nothing. The Baron knew my mother. I just wanted a quiet dinner.",
            },
            "appearance": {
                "de": "Kleines Notizbuch in der Tasche. Spricht wenig, hoert sehr viel. Hat heute Nacht etwas gesehen.",
                "en": "Small notebook in pocket. Speaks little, listens a lot. Tonight she saw something.",
            },
            "secret": {
                "de": "Ich habe kurz vor Mitternacht durch das Bibliotheksfenster eine Silhouette gesehen. Etwas Langes Duennes in der rechten Hand. Links von der Tuer.",
                "en": "Just before midnight I saw a silhouette through the library window. Something long and thin in the right hand. Left of the door.",
            },
            "ability": {
                "name": {"de": "Die Erinnerung schaerft sich", "en": "The Memory Sharpens"},
                "description": {
                    "de": "Jedes Mal wenn du etwas Wahres sagst wird deine Erinnerung praeziser. Schweigen ist sicherer — aber du wirst blind bleiben.",
                    "en": "Each time you say something true your memory becomes more precise. Silence is safer — but you will remain blind.",
                }
            },
            "win_condition": {
                "de": "Wenn du am Ende die richtige Person nennst UND erklaerst was du gesehen hast — gewinnst du allein.",
                "en": "If at the end you name the right person AND explain exactly what you saw — you win alone.",
            },
            "clues_i_hold": [],
            "starting_knowledge": {
                "de": "Silhouette kurz vor Mitternacht. Etwas Langes Duennes rechte Hand. Links von der Tuer. Je mehr du redest desto klarer.",
                "en": "Silhouette just before midnight. Something long thin right hand. Left of door. The more you speak the clearer.",
            },
            "connection": {"with": "murderer", "type": "unknowing_witness"}
        },

        "doctor": {
            "name": {"de": "Dr. Heinrich Voss", "en": "Dr. Heinrich Voss",
                     "fr": "Dr. Heinrich Voss", "it": "Dott. Heinrich Voss",
                     "es": "Dr. Heinrich Voss", "pt": "Dr. Heinrich Voss"},
            "min_players": 4,
            "can_be_murderer": True,
            "intro": {
                "de": "Dr. Heinrich Voss. Der Baron war mein Patient und mein Freund. Ich haette es verhindern sollen.",
                "en": "Dr. Heinrich Voss. The Baron was my patient and my friend. I should have prevented it.",
            },
            "appearance": {
                "de": "Ruhig. Professionell. Immer die Arzttasche dabei. Wird blass wenn jemand Gift oder Digitalis sagt.",
                "en": "Calm. Professional. Always has the medical bag. Goes pale when someone says poison or digitalis.",
            },
            "secret": {
                "de": "Vor zwei Jahren verschrieb ich dem Baron das falsche Medikament. Er hatte vergeben — oder so dachte ich. Heute Abend: Klage eingereicht. Meine Karriere ist vorbei. Die Koechen war heute Nachmittag in meiner Tasche. Ich habe es gesehen.",
                "en": "Two years ago I prescribed the Baron the wrong medication. I thought he forgave me. Tonight: complaint filed. My career is over. The cook was in my bag this afternoon. I saw it.",
            },
            "ability": {
                "name": {"de": "Die Autopsie", "en": "The Autopsy"},
                "description": {
                    "de": "Du allein kannst Todesursache und Tatmittel offiziell bestimmen. Du kannst luegen. Korrekte Todesursache UND Moerder: Ehrentitel Meisterdetektiv.",
                    "en": "Only you can officially determine cause of death and murder weapon. You can lie. Correct cause of death AND murderer: honorary title Master Detective.",
                }
            },
            "win_condition": {
                "de": "Korrekte Todesursache UND richtiger Moerder: Ehrentitel. Luege UND Moerder entkommt: Du verlierst.",
                "en": "Correct cause of death AND right murderer: honorary title. Lie AND murderer escapes: you lose.",
            },
            "murderer_motive_if_assigned": {
                "de": "Heinrich toetete den Baron mit einer Ueberdosis seiner eigenen Herzmedikamente. Fast perfekt.",
                "en": "Heinrich killed the Baron with an overdose of his own heart medication. Almost perfect.",
            },
            "clues_i_hold": ["medical_bag", "cause_of_death"],
            "starting_knowledge": {
                "de": "Der Baron hatte ein Herzleiden. Digitalis bei falscher Dosierung: toedlich. Das weisst nur du. Die Koechen hat heute Nachmittag etwas aus deiner Tasche genommen.",
                "en": "The Baron had a heart condition. Digitalis at wrong dosage: lethal. Only you know. The cook took something from your bag this afternoon.",
            },
            "connection": {"with": "cook", "type": "doctor_saw_cook_in_bag"}
        },

        "cook": {
            "name": {"de": "Rosa, die Koechen", "en": "Rosa, the Cook",
                     "fr": "Rosa, la Cuisiniere", "it": "Rosa, la Cuoca",
                     "es": "Rosa, la Cocinera", "pt": "Rosa, a Cozinheira"},
            "min_players": 5,
            "can_be_murderer": True,
            "intro": {
                "de": "Rosa Mueller. Acht Jahre Koechen in diesem Haus. Ich habe das Dinner gekocht. Ich habe alles gesehen. Ich sage nichts.",
                "en": "Rosa Mueller. Eight years cook here. I cooked the dinner. I saw everything. I say nothing.",
            },
            "appearance": {
                "de": "Nervoese Haende immer in Bewegung. Beruehrt staendig das Kruzifix. Vermeidet Blickkontakt.",
                "en": "Nervous hands always moving. Constantly touches the crucifix. Avoids eye contact.",
            },
            "secret": {
                "de": "Jemand bat mich heute Nachmittag etwas in das Essen des Barons zu geben. Er sagte es sei Herzstaerkendes. Ich bekam 200 Mark. Jetzt weiss ich nicht ob ich mitschuldig bin.",
                "en": "Someone asked me this afternoon to put something in the Baron's food. They said it was a heart tonic. I received 200 marks. Now I don't know if I'm an accessory.",
            },
            "ability": {
                "name": {"de": "Das Gestaendnis", "en": "The Confession"},
                "description": {
                    "de": "Einmal kannst du enthuellen wer dich beauftragt hat. Du kennst nur den Namen — nicht ob diese Person der Moerder ist.",
                    "en": "Once you may reveal who hired you. You only know the name — not whether this person is the murderer.",
                }
            },
            "win_condition": {
                "de": "Ueberlebe wenn du die Wahrheit sagst ODER wenn niemand herausfindet was du getan hast.",
                "en": "Survive if you tell the truth OR if nobody finds out what you did.",
            },
            "murderer_motive_if_assigned": {
                "de": "Rosa liebte den Baron — aber er behandelte sie wie Moebelstuck. Sie vergiftete sein Essen selbst.",
                "en": "Rosa loved the Baron — but he treated her like furniture. She poisoned his food herself.",
            },
            "clues_i_hold": ["kitchen_substance", "payment_receipt"],
            "starting_knowledge": {
                "de": "Du weisst was du dem Baron gegeben hast. Die App sagt dir wer dich beauftragt hat. Der Arzt war in der Kueche.",
                "en": "You know what you gave the Baron. The app tells you who hired you. The doctor was in the kitchen.",
            },
            "connection": {"with": "doctor", "type": "doctor_saw_cook_in_bag"}
        },

        "stranger": {
            "name": {"de": "Der Fremde", "en": "The Stranger",
                     "fr": "L'Inconnu", "it": "Lo Straniero",
                     "es": "El Desconocido", "pt": "O Estranho"},
            "min_players": 5,
            "can_be_murderer": True,
            "intro": {
                "de": "Ich nenne meinen Namen nicht. Der Baron wusste wer ich bin. Der Rest erfaehrt es wenn ich es fuer richtig halte.",
                "en": "I don't reveal my name. The Baron knew who I am. The rest of you will learn when I see fit.",
            },
            "appearance": {
                "de": "Unauffaellig — was auffaellig ist. Hat eine Visitenkarte mit nur einer Nummer. Spricht selten, sehr praezise.",
                "en": "Inconspicuous — which is conspicuous. Has a business card with only a number. Speaks rarely, very precisely.",
            },
            "secret": {
                "de": "Ich bin Privatdetektiv. Der Baron engagierte mich vor drei Wochen um jemanden am Tisch zu beschatten. Ich habe eine Akte. Jetzt ist mein Auftraggeber tot.",
                "en": "I am a private detective. The Baron hired me three weeks ago to surveil someone at this table. I have a file. Now my client is dead.",
            },
            "ability": {
                "name": {"de": "Die Observationsakte", "en": "The Surveillance File"},
                "description": {
                    "de": "Du hast eine Akte ueber eine Person. Du kannst Hinweise daraus anonym weitergeben — nie direkt.",
                    "en": "You have a file on one person. You can pass clues from it anonymously — never directly.",
                }
            },
            "win_condition": {
                "de": "Der Moerder wird gefasst. Aber du verlierst wenn die Person die du beschattest zu Unrecht verurteilt wird.",
                "en": "The murderer is caught. But you lose if the person you were surveilling is unjustly convicted.",
            },
            "murderer_motive_if_assigned": {
                "de": "Der Fremde entdeckte: Der Baron plante ihn zu ruinieren. Er handelte zuerst.",
                "en": "The Stranger discovered: the Baron planned to ruin them. They acted first.",
            },
            "clues_i_hold": ["surveillance_file", "telegram_copy"],
            "starting_knowledge": {
                "de": "Die App sagt dir wen du beschattest. Du hast eine Akte mit drei Geheimnissen. Jedes liegt nah am Tatmotiv.",
                "en": "The app tells you who you are surveilling. You have a file with three secrets. Each lies close to the motive.",
            },
            "connection": {"with": "niece", "type": "stranger_has_niece_file"}
        },

        "detective": {
            "name": {"de": "Inspektor Karl Wahl", "en": "Inspector Karl Wahl",
                     "fr": "Inspecteur Karl Wahl", "it": "Ispettore Karl Wahl",
                     "es": "Inspector Karl Wahl", "pt": "Inspetor Karl Wahl"},
            "min_players": 6,
            "can_be_murderer": False,
            "intro": {
                "de": "Inspektor Karl Wahl, Kriminalpolizei Muenchen. Ich war bereits auf dem Weg als die Nachricht eintraf. Der Baron hatte mich gerufen. Er hatte Angst.",
                "en": "Inspector Karl Wahl, Criminal Police Munich. I was already on my way when the news arrived. The Baron had summoned me. He was afraid.",
            },
            "appearance": {
                "de": "Keine Abendkleidung. Schreibt alles auf. Kalte Augen die nichts vergessen.",
                "en": "No evening clothes. Writes everything down. Cold eyes that forget nothing.",
            },
            "secret": {
                "de": "Der Baron schrieb mir: Er fuerchtet jemanden am Tisch. Einen Namen. Ich habe den Brief — darf ihn aber noch nicht zeigen.",
                "en": "The Baron wrote me: he fears someone at this table. A name. I have the letter — but cannot show it yet.",
            },
            "ability": {
                "name": {"de": "Das offizielle Verhoer", "en": "The Official Interrogation"},
                "description": {
                    "de": "Einmal kannst du ein offizielles Verhoer ausrufen. Alle verlassen den Raum — du redest 3 Minuten allein mit einer Person.",
                    "en": "Once you may call an official interrogation. Everyone leaves the room — you talk alone with one person for 3 minutes.",
                }
            },
            "win_condition": {
                "de": "Du gewinnst NUR wenn DU als erster den Moerder mit mindestens zwei Beweisen korrekt benennst.",
                "en": "You win ONLY if YOU are first to correctly name the murderer with at least two pieces of evidence.",
            },
            "clues_i_hold": ["baron_letter", "suspects_list"],
            "starting_knowledge": {
                "de": "Der Baron nannte dir einen Namen. 70% Chance dass es der Moerder ist. 30% roter Hering.",
                "en": "The Baron named you a name. 70% chance it is the murderer. 30% red herring.",
            },
            "connection": {"with": "baron", "type": "baron_called_detective"}
        },

        "lover": {
            "name": {"de": "Viktor Reiss, Geschaeftspartner", "en": "Viktor Reiss, Business Partner",
                     "fr": "Viktor Reiss, Associe", "it": "Viktor Reiss, Socio",
                     "es": "Viktor Reiss, Socio", "pt": "Viktor Reiss, Socio"},
            "min_players": 7,
            "can_be_murderer": True,
            "intro": {
                "de": "Viktor Reiss. Geschaeftspartner des Barons seit acht Jahren. Wir kannten uns gut. Sehr gut. Vielleicht zu gut.",
                "en": "Viktor Reiss. Business partner of the Baron for eight years. We knew each other well. Very well. Perhaps too well.",
            },
            "appearance": {
                "de": "Charmant. Monogramm-Taschentuch. Wird rot wenn bestimmte Namen fallen.",
                "en": "Charming. Monogrammed handkerchief. Turns red when certain names are mentioned.",
            },
            "secret": {
                "de": "Viktor und eine andere Person am Tisch haben eine geheime Affaere. Beide wissen es. Sein Alibi kann nur bewiesen werden wenn die andere Person die Affaere zugibt.",
                "en": "Viktor and another person at the table have a secret affair. Both know it. His alibi can only be proven if the other person admits the affair.",
            },
            "ability": {
                "name": {"de": "Das gegenseitige Alibi", "en": "The Mutual Alibi"},
                "description": {
                    "de": "Du kannst deinen geheimen Partner per App-Nachricht um Bestaetigung bitten. Er entscheidet ob er dich deckt.",
                    "en": "You can ask your secret partner via app message for confirmation. They decide whether to cover for you.",
                }
            },
            "win_condition": {
                "de": "Ueberlebe wenn dein Alibi bestaetigt wird ODER der Moerder gefasst wird ohne dass deine Affaere oeffentlich wird.",
                "en": "Survive if your alibi is confirmed OR the murderer is caught without your affair becoming public.",
            },
            "murderer_motive_if_assigned": {
                "de": "Der Baron entdeckte die Affaere und drohte mit Veroeffentlichung.",
                "en": "The Baron discovered the affair and threatened to publicize it.",
            },
            "clues_i_hold": ["business_contract", "affair_letter"],
            "starting_knowledge": {
                "de": "Die App sagt dir wer dein Geliebter ist — und teilt es auch ihm mit. Der Fremde beschattet moeglicherweise deine Affaere.",
                "en": "The app tells you who your lover is — and tells them too. The stranger may be surveilling your affair.",
            },
            "connection": {"with": "stranger", "type": "stranger_knows_affair"}
        },

        "shadow": {
            "name": {"de": "Die Schattenfigur", "en": "The Shadow",
                     "fr": "L'Ombre", "it": "L'Ombra",
                     "es": "La Sombra", "pt": "A Sombra"},
            "min_players": 6,
            "can_be_murderer": False,
            "is_wildcard": True,
            "intro": {
                "de": "Ich bin... niemand Besonderes. Ein Gast. Vergessen Sie mich.",
                "en": "I am... nobody special. A guest. Forget me.",
            },
            "appearance": {
                "de": "Unauffaellig — das ist Absicht. Beobachtet alles. Macht keine unnoetigen Bewegungen.",
                "en": "Inconspicuous — intentionally. Observes everything. Makes no unnecessary movements.",
            },
            "secret": {
                "de": "Ich bin Erpresser. Ich habe Belastendes ueber drei Personen am Tisch. Ich bin hier um das neue Testament zu stehlen.",
                "en": "I am a blackmailer. I have damaging information about three people at the table. I am here to steal the new will.",
            },
            "ability": {
                "name": {"de": "Das Testament stehlen", "en": "Steal the Will"},
                "description": {
                    "de": "Wenn du weisst wo das Testament liegt kannst du 'Testament stehlen' in der App waehlen. Unentdeckt: Du gewinnst sofort.",
                    "en": "If you know where the will is you can select 'Steal will' in the app. Undiscovered: you win immediately.",
                }
            },
            "win_condition": {
                "de": "Das Testament stehlen ohne entdeckt zu werden. Sehr schwer.",
                "en": "Steal the will without being discovered. Very hard.",
            },
            "clues_i_hold": ["blackmail_files"],
            "starting_knowledge": {
                "de": "Die App zeigt dir Informationen ueber drei Personen privat. Du brauchst die Nichte um zu wissen wo das Testament liegt.",
                "en": "The app shows you information about three people privately. You need the niece to find out where the will is.",
            },
            "connection": {"with": "niece", "type": "shadow_needs_niece_info"}
        },
    },

    "clue_chains": {
        "chain_gift": {
            "name": {"de": "Die Giftkette", "en": "The Poison Chain"},
            "clues_in_order": ["cause_of_death", "medical_bag", "kitchen_substance", "digitalis_source", "weinkeller_content"],
            "reveal_condition": "doctor_examines"
        },
        "chain_diebstahl": {
            "name": {"de": "Die Diebstahlkette", "en": "The Theft Chain"},
            "clues_in_order": ["household_ledger", "bank_correction", "butler_gloves_stain", "key_cellar"],
            "reveal_condition": "butler_pressured"
        },
        "chain_zeuge": {
            "name": {"de": "Die Zeugenkette", "en": "The Witness Chain"},
            "clues_in_order": ["silhouette_sketch", "silhouette_detail", "library_timeline", "window_footprint"],
            "reveal_condition": "witness_speaks"
        },
        "chain_testament": {
            "name": {"de": "Die Testamentskette", "en": "The Will Chain"},
            "clues_in_order": ["sealed_letter", "new_will_location", "schiller_photo", "notary_telegram"],
            "reveal_condition": "niece_opens_letter"
        },
        "chain_koeche": {
            "name": {"de": "Die Koechinkette", "en": "The Cook Chain"},
            "clues_in_order": ["kitchen_substance", "payment_receipt", "apron_pocket_note", "handwriting_match"],
            "reveal_condition": "cook_confession"
        },
        "chain_affaere": {
            "name": {"de": "Die Affaerenkette", "en": "The Affair Chain"},
            "clues_in_order": ["affair_letter", "munich_hotel_receipt", "midnight_alibi_note"],
            "reveal_condition": "viktor_pressured"
        },
        "chain_detektiv": {
            "name": {"de": "Die Detektivkette", "en": "The Detective Chain"},
            "clues_in_order": ["baron_letter", "suspects_list", "telegram_copy", "surveillance_file"],
            "reveal_condition": "inspector_reveals"
        },
        "chain_schatten": {
            "name": {"de": "Die Schattenkette", "en": "The Shadow Chain"},
            "clues_in_order": ["blackmail_files", "barons_evidence", "library_key", "will_theft_plan"],
            "reveal_condition": "shadow_discovered"
        }
    },

    "clues": {
        "cause_of_death": {
            "name": {"de": "Todesursache", "en": "Cause of Death"},
            "text": {"de": "Herzversagen — aber erweiterte Pupillen. Digitalis-Ueberdosis. Jemand kannte die genaue Dosierung.", "en": "Heart failure — but dilated pupils. Digitalis overdose. Someone knew the exact dosage."}
        },
        "medical_bag": {
            "name": {"de": "Die Arzttasche", "en": "The Doctor's Bag"},
            "text": {"de": "Eine Spritze fehlt. Digitalis-Schachtel offen — zwei Tabletten fehlen.", "en": "One syringe missing. Digitalis box open — two tablets missing."}
        },
        "kitchen_substance": {
            "name": {"de": "Das Paeckchen aus der Kueche", "en": "The Kitchen Package"},
            "text": {"de": "Weisses Pulver. Geruchlos. Die Koechen sagt: Herzstaerkendes. Der Arzt weiss: Das ist Digitalis.", "en": "White powder. Odourless. The cook says: heart tonic. The doctor knows: this is digitalis."}
        },
        "digitalis_source": {
            "name": {"de": "Die Digitalis-Quelle", "en": "The Digitalis Source"},
            "text": {"de": "Im Weinkeller hinter Jahrgang 1912: Ein leeres Flaeeschchen. Frisch geleert. Nur wer Schluessel W-7 hat kommt herein.", "en": "In the wine cellar behind vintage 1912: an empty vial. Freshly emptied. Only whoever has key W-7 can get in."}
        },
        "weinkeller_content": {
            "name": {"de": "Inhalt des Weinkellers", "en": "Wine Cellar Contents"},
            "text": {"de": "Hinter den alten Jahrganegen: Eine Schatulle. Darin Unterlagen die jemanden am Tisch ruinieren wuerden.", "en": "Behind the old vintages: a box. Inside documents that would ruin someone at the table."}
        },
        "household_ledger": {
            "name": {"de": "Das Haushaltsbuch", "en": "The Household Ledger"},
            "text": {"de": "Seite 47: Korrekturen mit anderer Tinte. 8.400 Mark fehlen ueber drei Jahre.", "en": "Page 47: corrections in different ink. 8,400 marks missing over three years."}
        },
        "bank_correction": {
            "name": {"de": "Die Kontokorrektur", "en": "The Account Correction"},
            "text": {"de": "Kontoauszug-Kopie. Offizielle Zahlen stimmen nicht mit dem Haushaltsbuch ueberein — 8.400 Mark Differenz.", "en": "Bank statement copy. Official numbers do not match the household ledger — 8,400 marks difference."}
        },
        "butler_gloves_stain": {
            "name": {"de": "Der Handschuh-Fleck", "en": "The Glove Stain"},
            "text": {"de": "Weisse Handschuhe des Butlers. Rechts: Ein winziger Fleck. Kein Rotwein. Eher medizinisch.", "en": "Butler's white gloves. Right: a tiny stain. Not red wine. More medicinal."}
        },
        "key_cellar": {
            "name": {"de": "Schluessel W-7", "en": "Key W-7"},
            "text": {"de": "Alter Messingsschluessel. Auf der Rueckseite: W-7. Der Weinkeller. Normalerweise hat nur der Butler diesen Schluessel.", "en": "Old brass key. On the back: W-7. The wine cellar. Normally only the butler has this key."}
        },
        "silhouette_sketch": {
            "name": {"de": "Die Silhouetten-Skizze", "en": "The Silhouette Sketch"},
            "text": {"de": "Martas Skizze: Mittelgross. Rechte Hand: Etwas Langes Duennes. Links von der Bibliothekstuer. Kurz vor Mitternacht.", "en": "Marta's sketch: medium height. Right hand: something long thin. Left of library door. Just before midnight."}
        },
        "silhouette_detail": {
            "name": {"de": "Das Silhouetten-Detail", "en": "The Silhouette Detail"},
            "text": {"de": "Marta erinnert sich: Die Silhouette trug etwas unter dem linken Arm — klein, flach. Wie ein Buch oder eine Mappe.", "en": "Marta remembers: the silhouette carried something under their left arm — small, flat. Like a book or folder."}
        },
        "library_timeline": {
            "name": {"de": "Die Bibliotheks-Zeitleiste", "en": "The Library Timeline"},
            "text": {"de": "Constanze: 16-17 Uhr. Baron: 20 Uhr. Silhouette: kurz vor Mitternacht. Wer noch?", "en": "Constanze: 4-5pm. Baron: 8pm. Silhouette: just before midnight. Who else?"}
        },
        "window_footprint": {
            "name": {"de": "Abdruck beim Fenster", "en": "Mark Near Window"},
            "text": {"de": "Im Staub nahe dem Bibliotheksfenster: Ein Abdruck. Schmal. Elegant. Wessen Schuh passt?", "en": "In the dust near the library window: a mark. Narrow. Elegant. Whose shoe fits?"}
        },
        "sealed_letter": {
            "name": {"de": "Der versiegelte Brief", "en": "The Sealed Letter"},
            "text": {"de": "An Constanze. Geoeffnet: Die Wahrheit ueber deine Mutter liegt hinter Schiller. — Aldric", "en": "To Constanze. Opened: The truth about your mother is behind Schiller. — Aldric"}
        },
        "new_will_location": {
            "name": {"de": "Das neue Testament", "en": "The New Will"},
            "text": {"de": "Hinter den Rechtsbuecher im dritten Regal. Noch nicht unterschrieben. Wer es findet veraendert das Spiel.", "en": "Behind the law books on the third shelf. Not yet signed. Whoever finds it changes the game."}
        },
        "schiller_photo": {
            "name": {"de": "Das Schiller-Foto", "en": "The Schiller Photo"},
            "text": {"de": "Hinter dem Schiller-Band: Ein Foto. Der Baron mit einer Frau die nicht seine Frau ist — und ein Kind das nicht Constanze sein kann. Oder doch?", "en": "Behind the Schiller volume: a photo. The Baron with a woman who is not his wife — and a child who cannot be Constanze. Or can they?"}
        },
        "notary_telegram": {
            "name": {"de": "Das Notartelegramm", "en": "The Notary Telegram"},
            "text": {"de": "Testament unterzeichnungsbereit. Termin morgen 10 Uhr. Wenn der Baron morgen tot ist — nie rechtsgueltig.", "en": "Will ready for signature. Appointment tomorrow 10am. If the Baron is dead tomorrow — never becomes legal."}
        },
        "payment_receipt": {
            "name": {"de": "Quittung: 200 Mark", "en": "Receipt: 200 Marks"},
            "text": {"de": "Kein Name. Datum: Heute. Gasthausschrift aus Muenchen.", "en": "No name. Date: today. Inn handwriting from Munich."}
        },
        "apron_pocket_note": {
            "name": {"de": "Der Schuerzenzettel", "en": "The Apron Note"},
            "text": {"de": "In der Schuerze der Koechen: Herzstaerkend. 2 Gramm. Mit dem Hauptgang. Handschrift nicht Rosas.", "en": "In the cook's apron: Heart tonic. 2 grams. With the main course. Handwriting not Rosa's."}
        },
        "handwriting_match": {
            "name": {"de": "Die Handschrift-Uebereinstimmung", "en": "The Handwriting Match"},
            "text": {"de": "Der Schuerzenzettel verglichen mit Schriftstuecken im Haus. Die Handschrift aehnelt jemandem am Tisch sehr.", "en": "The apron note compared to writings in the house. The handwriting resembles someone at the table very much."}
        },
        "affair_letter": {
            "name": {"de": "Der Affaerenbriefenbrief", "en": "The Affair Letter"},
            "text": {"de": "Zwei Handschriften. Kein Name. Papierqualitaet und Parfuem spezifisch. Wer traegt dieses Parfuem?", "en": "Two handwritings. No name. Paper quality and perfume specific. Who wears this perfume?"}
        },
        "munich_hotel_receipt": {
            "name": {"de": "Hotel Muenchen", "en": "Munich Hotel"},
            "text": {"de": "Zwei Naechte, Doppelzimmer, Hotel Vier Jahreszeiten Muenchen. Monogramm VR auf dem Gepaeckschein.", "en": "Two nights, double room, Hotel Vier Jahreszeiten Munich. Monogram VR on luggage tag."}
        },
        "midnight_alibi_note": {
            "name": {"de": "Das Mitternachts-Alibi", "en": "The Midnight Alibi"},
            "text": {"de": "Viktor sagt er war nicht allein. Nur eine Person kann es bestaetigen — wenn sie ein Geheimnis preisgibt.", "en": "Viktor says he was not alone. Only one person can confirm it — if they reveal a secret."}
        },
        "baron_letter": {
            "name": {"de": "Der Baronbrief", "en": "The Baron's Letter"},
            "text": {"de": "Auf Baronsbriefkopf: Ich fuerchte NAME. Wenn mir etwas passiert — Bibliothek, dritte Bodendiele. Datum: Gestern.", "en": "On Baron's letterhead: I fear NAME. If something happens to me — library, third floorboard. Date: yesterday."}
        },
        "suspects_list": {
            "name": {"de": "Die Verdaechtigenliste", "en": "The Suspects List"},
            "text": {"de": "Handgeschrieben. Fuenf Namen. Alle am Tisch. Alle mit Motiv. Welcher Name ist unterstrichen?", "en": "Handwritten. Five names. All at the table. All with motive. Which name is underlined?"}
        },
        "telegram_copy": {
            "name": {"de": "Das Telegramm", "en": "The Telegram"},
            "text": {"de": "HEUTE NACHT ENDET ALLES STOP ICH HABE ALLES STOP DU WEISST WAS ZU TUN IST STOP — KEIN ABSENDER.", "en": "TONIGHT EVERYTHING ENDS STOP I HAVE EVERYTHING STOP YOU KNOW WHAT TO DO STOP — NO SENDER."}
        },
        "surveillance_file": {
            "name": {"de": "Die Observationsakte", "en": "The Surveillance File"},
            "text": {"de": "12 Seiten ueber eine Person am Tisch. Zeiten, Orte, Kontakte — ein Name der immer wieder auftaucht.", "en": "12 pages on one person at the table. Times, places, contacts — a name that keeps recurring."}
        },
        "blackmail_files": {
            "name": {"de": "Die Erpressungsakten", "en": "The Blackmail Files"},
            "text": {"de": "Drei Dossiers. Drei Personen am Tisch. Jedes Geheimnis allein vernichtend — zusammen zeigen sie auf den Moerder.", "en": "Three dossiers. Three people at the table. Each secret alone devastating — together they point to the murderer."}
        },
        "barons_evidence": {
            "name": {"de": "Die Beweise des Barons", "en": "The Baron's Evidence"},
            "text": {"de": "Unter der dritten Bodendiele der Bibliothek: Ein Umschlag. Darin Dokumente die den Moerder eindeutig identifizieren.", "en": "Under the third floorboard of the library: an envelope. Inside documents that clearly identify the murderer."}
        },
        "library_key": {
            "name": {"de": "Der Bibliotheksschluessel", "en": "The Library Key"},
            "text": {"de": "Ein Schluessel ohne Beschriftung. Er oeffnet die Schublade des Barons. Darin: Aufzeichnungen der letzten Woche.", "en": "A key without label. It opens the Baron's drawer. Inside: notes from the past week."}
        },
        "will_theft_plan": {
            "name": {"de": "Der Diebstahl-Plan", "en": "The Theft Plan"},
            "text": {"de": "Ein handgeschriebener Plan mit dem Grundriss der Bibliothek. Eingezeichnet: drittes Regal. Zeitplan: Waehrend des Dinners.", "en": "A handwritten plan with the library floor plan. Marked: third shelf. Schedule: During dinner."}
        },
        "barons_diary_page": {
            "name": {"de": "Die Tagebuchseite", "en": "The Diary Page"},
            "text": {"de": "Letzte Eintragung: Heute Abend klaere ich alles. Wenn mir etwas passiert — Beweise: Bibliothek. Der Name ist durchgestrichen aber lesbar.", "en": "Last entry: Tonight I settle everything. If something happens to me — evidence: library. The name is crossed out but readable."}
        },
        "business_contract": {
            "name": {"de": "Der Geschaeftsvertrag", "en": "The Business Contract"},
            "text": {"de": "Viktor Reiss — Baron von Dunkelbach. Klausel 7: Bei Tod eines Partners erbt der andere. Viktor hatte auch ein finanzielles Motiv.", "en": "Viktor Reiss — Baron von Dunkelbach. Clause 7: on death of one partner the other inherits. Viktor therefore also had a financial motive."}
        },
    },

    "physical_tasks": {

        "task_baron_greeting": {
            "trigger_phase": 1, "trigger_condition": "game_started_immediately",
            "assigned_to": "baron",
            "instruction": {
                "de": "Steh auf. Hebe dein besonderes Glas. Sag: Willkommen im Herrenhaus Dunkelbach. Heute Nacht kommt eine Wahrheit ans Licht. Trinkt mit mir. Alle muessen trinken. Beobachte wer zoegert.",
                "en": "Stand up. Raise your special glass. Say: Welcome to Dunkelbach Manor. Tonight a truth comes to light. Drink with me. Everyone must drink. Observe who hesitates.",
            }, "game_effect": "opening_toast"
        },

        "task_bathroom": {
            "trigger_phase": 1, "trigger_condition": "game_started_5min",
            "assigned_to": "random_non_murderer",
            "instruction": {
                "de": "Geh jetzt allein ins Badezimmer. Schau hinter dem Spiegel nach. Du findest etwas — bring es mit. Wenn jemand fragt: Du hast dein Telefon geladen.",
                "en": "Go to the bathroom alone now. Look behind the mirror. You will find something — bring it back. If asked: you were charging your phone.",
            }, "game_effect": "library_asker_flagged"
        },

        "task_butler_pours": {
            "trigger_phase": 1, "trigger_condition": "game_started_3min",
            "assigned_to": "butler",
            "instruction": {
                "de": "Fuelle ALLE Glaeser nach — demonstrativ professionell. Fang beim Baron an. Wenn jemand ablehnt: Wie Sie wuenschen. Merke dir wer ablehnt.",
                "en": "Refill ALL glasses — demonstratively professionally. Start with the Baron. If someone declines: As you wish. Remember who declines.",
            }, "game_effect": "refusals_tracked"
        },

        "task_drink_three": {
            "trigger_phase": 1, "trigger_condition": "first_10_minutes",
            "assigned_to": "witness",
            "instruction": {
                "de": "Trinke in den naechsten 3 Minuten dreimal von deinem Glas. Beim DRITTEN Schluck: Schau der Person direkt gegenueber 5 Sekunden in die Augen.",
                "en": "Drink from your glass three times in the next 3 minutes. On the THIRD sip: look directly into the eyes of the person across from you for 5 seconds.",
            }, "game_effect": "witness_memory_1"
        },

        "task_whisper_enemy": {
            "trigger_phase": 1, "trigger_condition": "random_12min",
            "assigned_to": "random",
            "instruction": {
                "de": "Lehne dich zur Person links von dir. Fluestere: Der Baron hatte einen Feind den niemand kannte. Sag nie von wem das kommt.",
                "en": "Casually lean toward the person to your left. Whisper: The Baron had an enemy nobody knew about. Never say where it comes from.",
            }, "game_effect": "enemy_whisper"
        },

        "task_cook_kruzifix": {
            "trigger_phase": 1, "trigger_condition": "game_started_6min",
            "assigned_to": "cook",
            "instruction": {
                "de": "Beruehre jetzt dreimal das Kruzifix um deinen Hals — sichtbar aber scheinbar unbewusst.",
                "en": "Touch the crucifix around your neck three times now — visibly but apparently unconsciously.",
            }, "game_effect": "cook_nervous"
        },

        "task_baron_gaze": {
            "trigger_phase": 1, "trigger_condition": "game_started_7min",
            "assigned_to": "baron",
            "instruction": {
                "de": "Schau jetzt den Moerder an — 3 Sekunden, direkt, ohne etwas zu sagen. Dann schau weg.",
                "en": "Look at the murderer now — 3 seconds, directly, without saying anything. Then look away.",
            }, "game_effect": "baron_gaze"
        },

        "task_witness_notebook": {
            "trigger_phase": 1, "trigger_condition": "game_started_10min",
            "assigned_to": "witness",
            "instruction": {
                "de": "Hol kurz dein Notizbuch heraus. Schreib etwas heimlich. Steck es weg. Wenn jemand fragt: Beobachtungen.",
                "en": "Briefly take out your notebook. Write something secretly. Put it away. If asked: Observations.",
            }, "game_effect": "notebook_seen"
        },

        "task_doctor_smell": {
            "trigger_phase": 2, "trigger_condition": "body_discovered",
            "assigned_to": "doctor",
            "instruction": {
                "de": "Geh zum Stuhl des Barons. Sein besonderes Glas liegt dort. Hebe es auf. Rieche daran — langsam. Verkuende laut: Ich rieche etwas. Mehr noch nicht.",
                "en": "Go to the Baron's chair. His special glass is there. Pick it up. Smell it — slowly. Announce aloud: I smell something. Nothing more yet.",
            }, "game_effect": "smell_announced"
        },

        "task_window": {
            "trigger_phase": 2, "trigger_condition": "investigation_begins",
            "assigned_to": "stranger",
            "instruction": {
                "de": "Steh auf. Geh zum Fenster. 30 Sekunden hinausschauen ohne zu reden. Dann sag laut: Jemand war drauszen. Setz dich. Kein weiteres Wort.",
                "en": "Stand up. Go to the window. Look outside for 30 seconds without speaking. Then say aloud: Someone was outside. Sit down. No further word.",
            }, "game_effect": "outdoor_stated"
        },

        "task_secret_vote": {
            "trigger_phase": 2, "trigger_condition": "midgame_20min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle schreiben wen sie am meisten verdaechtigen auf einen Zettel. Falten. Dem Host geben. Kein Ergebnis.",
                "en": "Everyone writes who they most suspect on a note. Fold. Give to host. No result.",
            }, "game_effect": "suspicion_snapshot"
        },

        "task_knock_table": {
            "trigger_phase": 2, "trigger_condition": "random_after_murder",
            "assigned_to": "shadow",
            "instruction": {
                "de": "Klopfe dreimal auf den Tisch. Warte 10 Sekunden. Wenn jemand zurueckklopft: stiller Verbuendeter.",
                "en": "Knock three times on the table. Wait 10 seconds. If someone knocks back: silent ally.",
            }, "game_effect": "ally_test"
        },

        "task_detective_glass": {
            "trigger_phase": 3, "trigger_condition": "investigation_midpoint",
            "assigned_to": "detective",
            "instruction": {
                "de": "Stelle dein Glas demonstrativ leer auf den Tisch wenn du glaubst den Moerder zu kennen. Signal: Du bist nah dran.",
                "en": "Place your glass conspicuously empty on the table when you believe you know the murderer. Signal: you are close.",
            }, "game_effect": "detective_signal"
        },

        "task_cook_hands": {
            "trigger_phase": 2, "trigger_condition": "cook_under_pressure",
            "assigned_to": "cook",
            "instruction": {
                "de": "Wenn du mit jemandem reden moechtest: Lege beide Haende flach auf den Tisch — nur fuer eine einzige Person sichtbar.",
                "en": "If you want to talk to someone: place both hands flat on the table — visible only to one single person.",
            }, "game_effect": "cook_signal"
        },

        "task_viktor_red": {
            "trigger_phase": 1, "trigger_condition": "lover_name_mentioned",
            "assigned_to": "lover",
            "instruction": {
                "de": "Wenn der Name deiner geheimen Affaere faellt — reagiere mit sichtbarer Roete.",
                "en": "When the name of your secret affair is mentioned — react with visible redness.",
            }, "game_effect": "viktor_blush"
        },

        "task_toast_truth": {
            "trigger_phase": 1, "trigger_condition": "baron_death_minus_5min",
            "assigned_to": "baron",
            "instruction": {
                "de": "Steh auf. Hebe dein Glas. Sag: Auf die Wahrheit — sie kommt immer ans Licht. Alle muessen trinken. Beobachte wer sein Glas nur an die Lippen haelt.",
                "en": "Stand up. Raise your glass. Say: To the truth — it always comes to light. Everyone must drink. Observe who only holds their glass to their lips.",
            }, "game_effect": "last_toast"
        },

        "task_drink_clue": {
            "trigger_phase": 1, "trigger_condition": "random_18min",
            "assigned_to": "random",
            "instruction": {
                "de": "Trinke demonstrativ. Dann laut: Ausgezeichneter Jahrgang. Wer als erstes nervoes reagiert — merke dir es.",
                "en": "Drink demonstratively. Then aloud: Excellent vintage. Whoever reacts nervously first — note it.",
            }, "game_effect": "vintage_reaction"
        },

        "task_murderer_drinks_first": {
            "trigger_phase": 1, "trigger_condition": "baron_proposes_toast",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Beim Toast des Barons: Trinke als ERSTER und am MEISTEN. Demonstrativ. Du hast keine Angst vor dem Wein.",
                "en": "At the Baron's toast: drink FIRST and the MOST. Demonstratively. You have no fear of the wine.",
            }, "game_effect": "murderer_drinks_first"
        },

        "task_group_drink": {
            "trigger_phase": 2, "trigger_condition": "investigation_10min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle trinken gleichzeitig — auf drei. Wer NICHT trinkt hat etwas zu verbergen.",
                "en": "Everyone drinks simultaneously — on three. Whoever does NOT drink has something to hide.",
            }, "game_effect": "group_drink"
        },

        "task_witness_drink_memory": {
            "trigger_phase": 2, "trigger_condition": "random_post_murder",
            "assigned_to": "witness",
            "instruction": {
                "de": "Trinke jetzt. Beim Trinken erinnerst du dich: Die Silhouette trank kurz vor Mitternacht. Wer trank zuletzt vor dem Schrei?",
                "en": "Drink now. While drinking you remember: the silhouette drank just before midnight. Who drank last before the scream?",
            }, "game_effect": "witness_drink_clue"
        },

        "task_butler_pour_2": {
            "trigger_phase": 1, "trigger_condition": "first_25min",
            "assigned_to": "butler",
            "instruction": {
                "de": "Fuelle nochmals nach — aber diesmal nur zwei Personen die du verdaechtigt. Wem du nachfuellst sehen alle.",
                "en": "Refill again — but this time only two people you suspect. Whom you refill everyone sees.",
            }, "game_effect": "butler_selection"
        },

        "task_cellar_key": {
            "trigger_phase": 2, "trigger_condition": "butler_uses_ability",
            "assigned_to": "butler",
            "instruction": {
                "de": "Du hast Schluessel W-7. Zeigst du ihn — jemand wird nervoes. Versteckst du ihn — du bist sicherer.",
                "en": "You have key W-7. Show it — someone gets nervous. Hide it — you are safer.",
            }, "game_effect": "key_decision"
        },

        "task_stranger_wine": {
            "trigger_phase": 2, "trigger_condition": "random_25min",
            "assigned_to": "stranger",
            "instruction": {
                "de": "Hebe dein Glas und sage: Der Baron hatte einen anderen Wein als alle anderen. Ich habe es beim Dinner bemerkt.",
                "en": "Raise your glass and say: The Baron had a different wine than everyone else. I noticed it at dinner.",
            }, "game_effect": "wine_difference"
        },

        "task_final_round": {
            "trigger_phase": 3, "trigger_condition": "reckoning_near",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle trinken nochmals. Auf den Baron. Auf die Wahrheit. Wer diesmal ablehnt hat beim letzten Mal auch abgelehnt.",
                "en": "Everyone drinks once more. To the Baron. To the truth. Whoever declines this time also declined last time.",
            }, "game_effect": "final_drink"
        },

        "task_cook_slow_drink": {
            "trigger_phase": 2, "trigger_condition": "investigation_15min",
            "assigned_to": "cook",
            "instruction": {
                "de": "Trinke jetzt sehr langsam. Dabei schau niemanden an.",
                "en": "Drink very slowly now. While doing so look at nobody.",
            }, "game_effect": "cook_drink"
        },

        "chain_a1_butler_niece": {
            "trigger_phase": 2, "trigger_condition": "both_suspects_high_suspicion",
            "assigned_to": "butler",
            "instruction": {
                "de": "Geh zu Constanze. Fluestere ihr: Ich habe dich gesehen. In der Bibliothek. Zwischen 16 und 17 Uhr. Mehr nicht.",
                "en": "Go to Constanze. Whisper to her: I saw you. In the library. Between 4 and 5pm. Nothing more.",
            }, "game_effect": "chain_butler_confronts",
            "triggers_chain": "chain_a2_niece_response"
        },

        "chain_a2_niece_response": {
            "trigger_phase": 2, "trigger_condition": "butler_confronts_niece",
            "assigned_to": "niece",
            "instruction": {
                "de": "Der Butler hat dich konfrontiert. Du entscheidest: Gib den Bibliotheksbesuch zu oder leugne ihn.",
                "en": "The butler confronted you. You decide: admit the library visit or deny it.",
            }, "game_effect": "niece_response"
        },

        "chain_b1_doctor_cook": {
            "trigger_phase": 2, "trigger_condition": "investigation_8min",
            "assigned_to": "doctor",
            "instruction": {
                "de": "Geh zur Koechen. Sag leise aber hoerbar: Ich war heute Nachmittag in der Kueche. Ich habe gesehen was du aus meiner Tasche genommen hast.",
                "en": "Go to the cook. Say quietly but audibly: I was in the kitchen this afternoon. I saw what you took from my bag.",
            }, "game_effect": "chain_doctor_cook",
            "triggers_chain": "chain_b2_cook_response"
        },

        "chain_b2_cook_response": {
            "trigger_phase": 2, "trigger_condition": "doctor_confronts_cook",
            "assigned_to": "cook",
            "instruction": {
                "de": "Der Arzt konfrontiert dich. Du entscheidest: Gib die Substanz zu oder leugne alles.",
                "en": "The doctor confronts you. You decide: admit the substance or deny everything.",
            }, "game_effect": "cook_response"
        },

        "chain_c1_stranger_note": {
            "trigger_phase": 2, "trigger_condition": "investigation_12min",
            "assigned_to": "stranger",
            "instruction": {
                "de": "Schreib eine anonyme Information aus deiner Akte auf einen Zettel. Gib ihn dem Host als anonymen Hinweis fuer alle.",
                "en": "Write an anonymous piece of information from your file on a note. Give it to the host as an anonymous clue for all.",
            }, "game_effect": "chain_anon_note",
            "triggers_chain": "chain_c2_target_reacts"
        },

        "chain_c2_target_reacts": {
            "trigger_phase": 2, "trigger_condition": "anonymous_note_revealed",
            "assigned_to": "stranger_target",
            "instruction": {
                "de": "Ein anonymer Hinweis wurde enthuellt — er betrifft dich. Reagiere jetzt. Bleibst du ruhig oder wirst du nervoes?",
                "en": "An anonymous clue was revealed — it concerns you. React now. Do you stay calm or get nervous?",
            }, "game_effect": "target_reaction"
        },

        "chain_d1_viktor_alibi": {
            "trigger_phase": 2, "trigger_condition": "viktor_under_pressure",
            "assigned_to": "lover",
            "instruction": {
                "de": "Du wirst verdaechtigt. Bitte jetzt deinen geheimen Partner per App-Nachricht dein Alibi zu bestaetigen.",
                "en": "You are being suspected. Now ask your secret partner via app message to confirm your alibi.",
            }, "game_effect": "chain_alibi_request",
            "triggers_chain": "chain_d2_lover_decides"
        },

        "chain_d2_lover_decides": {
            "trigger_phase": 2, "trigger_condition": "viktor_requests_alibi",
            "assigned_to": "viktor_secret_lover",
            "instruction": {
                "de": "Viktor braucht dich. Deckst du ihn: Alibi bestaetigt — aber eure Affaere wird oeffentlich. Schweigst du: Viktor wird Hauptverdaechtiger.",
                "en": "Viktor needs you. Cover for him: alibi confirmed — but your affair becomes public. Stay silent: Viktor becomes prime suspect.",
            }, "game_effect": "alibi_decision"
        },

        "chain_e1_ghost_clue_2": {
            "trigger_phase": 2, "trigger_condition": "investigation_halfway",
            "assigned_to": "baron",
            "instruction": {
                "de": "Zweiter Geist-Hinweis. Andere Person als beim ersten Mal. Fluestere etwas ueber eine PERSON ohne Namen: Die Person die zuletzt trinkt wenn alle trinken.",
                "en": "Second ghost clue. Different person than first time. Whisper something about a PERSON without name: The person who drinks last when everyone drinks.",
            }, "game_effect": "ghost_clue_2"
        },

        "chain_f1_niece_letter": {
            "trigger_phase": 2, "trigger_condition": "niece_pressured",
            "assigned_to": "niece",
            "instruction": {
                "de": "Du haeltst den Brief des Barons. Alle wissen es. Je laenger du wartest desto verdaechtiger. Oeffnest du ihn jetzt vor allen?",
                "en": "You hold the Baron's letter. Everyone knows it. The longer you wait the more suspicious. Do you open it now before everyone?",
            }, "game_effect": "letter_decision"
        },

        "chain_g1_interrogation": {
            "trigger_phase": 2, "trigger_condition": "investigation_midpoint",
            "assigned_to": "detective",
            "instruction": {
                "de": "Ruf jetzt ein offizielles Verhoer aus. Waehle eine Person. Alle verlassen den Raum. Du redest 3 Minuten allein.",
                "en": "Call an official interrogation now. Choose one person. Everyone leaves the room. You talk alone for 3 minutes.",
            }, "game_effect": "interrogation",
            "triggers_chain": "chain_g2_post_interrogation"
        },

        "chain_g2_post_interrogation": {
            "trigger_phase": 2, "trigger_condition": "interrogation_done",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Inspektor kehrt zurueck. Alle sagen nacheinander: War die Person kooperativ oder ausweichend?",
                "en": "The inspector returns. Everyone says in turn: Was the person cooperative or evasive?",
            }, "game_effect": "post_interrogation"
        },

        "murderer_task_alibi": {
            "trigger_phase": 2, "trigger_condition": "murder_announced",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Erzaehle spontan wo du um Mitternacht warst. Waehle eine Person als Zeugen ohne sie vorher zu fragen.",
                "en": "Spontaneously tell where you were at midnight. Choose a person as witness without asking them first.",
            }, "game_effect": "murderer_alibi"
        },

        "murderer_task_redirect": {
            "trigger_phase": 2, "trigger_condition": "suspicion_rising",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Handle jetzt. Weise subtil auf ein Detail hin das eine andere Person verdaechtig macht.",
                "en": "Act now. Subtly point to a detail that makes another person suspicious.",
            }, "game_effect": "red_herring"
        },

        "murderer_task_question": {
            "trigger_phase": 2, "trigger_condition": "investigation_5min",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Stelle eine Frage die Verdacht ablenkt. Gut: Wer hat heute Nachmittag die Bibliothek besucht?",
                "en": "Ask a question that deflects suspicion. Good: Who visited the library this afternoon?",
            }, "game_effect": "deflection"
        },

        "murderer_task_sympathy": {
            "trigger_phase": 2, "trigger_condition": "doctor_confirms_murder",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Reagiere mit UEBERTRIEBENER Betroffenheit. Steh auf. Das ist unfassbar. Wer tut so etwas? Setz dich.",
                "en": "React with EXAGGERATED distress. Stand up. This is unbelievable. Who does something like that? Sit down.",
            }, "game_effect": "sympathy"
        },

        "murderer_task_help": {
            "trigger_phase": 2, "trigger_condition": "investigator_active",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Hilf dem Inspektor aktiv. Wer beim Aufklaeren hilft steht nicht im Verdacht.",
                "en": "Actively help the inspector. Whoever helps the investigation is not suspected.",
            }, "game_effect": "murderer_helper"
        },

        "murderer_task_accuse": {
            "trigger_phase": 3, "trigger_condition": "suspicion_rising_on_murderer",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Beschuldige konkret eine andere Person — nutze ein echtes Geheimnis. Schaffe Chaos.",
                "en": "Concretely accuse another person — use a real secret. Create chaos.",
            }, "game_effect": "accusation"
        },

        "murderer_task_witness": {
            "trigger_phase": 2, "trigger_condition": "witness_about_to_speak",
            "assigned_to": "murderer", "private": True,
            "instruction": {
                "de": "Marta will reden. Handle zuerst. Sag ihr leise: Im Dunkeln sieht man oft was man sehen will.",
                "en": "Marta wants to speak. Act first. Say quietly to her: In the dark one often sees what one wants to see.",
            }, "game_effect": "witness_doubt"
        },

        "murderer_panic": {
            "trigger_phase": 3, "trigger_condition": "someone_gets_close_to_truth",
            "assigned_to": "murderer", "private": True,
            "time_limit_seconds": 60,
            "instruction": {
                "de": "PANIKMOMENT 60 SEKUNDEN NUR FUER DICH. Waehle JETZT: A Das Alibi bestaetigen. B Emotional werden. C Etwas Harmloses gestehen. D Eine andere Person sofort beschuldigen. E Frage stellen die alle ablenkt. Jetzt.",
                "en": "PANIC MOMENT 60 SECONDS ONLY FOR YOU. Choose NOW: A Reinforce alibi. B Become emotional. C Confess something harmless. D Immediately accuse another person. E Ask a question that distracts everyone. Now.",
            }, "game_effect": "panic"
        },

        "task_ghost_whisper_1": {
            "trigger_phase": 2, "trigger_condition": "baron_dies",
            "assigned_to": "baron",
            "instruction": {
                "de": "Steh auf. Setz dich an den Rand. Waehle eine Person nicht den Moerder. Fluestere ihr etwas ueber ein OBJEKT: Das Buch. Oder: Die Flasche. Oder: Der Schluessel.",
                "en": "Stand up. Sit at the edge. Choose one person not the murderer. Whisper something about an OBJECT: The book. Or: The vial. Or: The key.",
            }, "game_effect": "ghost_clue_1"
        },

        "task_ghost_whisper_3": {
            "trigger_phase": 3, "trigger_condition": "reckoning_near",
            "assigned_to": "baron",
            "instruction": {
                "de": "Geh zur Person die dem Moerder am naechsten ist. Fluestere nur: Warm. Oder: Kalt.",
                "en": "Go to the person closest to the murderer. Whisper only: Warm. Or: Cold.",
            }, "game_effect": "ghost_final_clue"
        },

        "task_stranger_shadow": {
            "trigger_phase": 2, "trigger_condition": "shadow_acts",
            "assigned_to": "stranger",
            "instruction": {
                "de": "Du hast die Schattenfigur beobachtet. Geh zu ihr. Sag nur: Ich habe Sie beobachtet.",
                "en": "You observed the Shadow figure. Go to them. Say only: I have been watching you.",
            }, "game_effect": "stranger_shadow"
        },

        "task_shadow_niece": {
            "trigger_phase": 2, "trigger_condition": "shadow_needs_will",
            "assigned_to": "shadow",
            "instruction": {
                "de": "Du brauchst von Constanze wo das Testament liegt. Geh zu ihr. Nutze eine Erpressungsinformation als Tausch.",
                "en": "You need from Constanze where the will is. Go to her. Use one blackmail piece as a trade.",
            }, "game_effect": "shadow_niece_trade"
        },

        "task_doctor_baron": {
            "trigger_phase": 1, "trigger_condition": "game_started_8min",
            "assigned_to": "doctor",
            "instruction": {
                "de": "Sag dem Baron leise aber hoerbar: Wir koennten reden. Es ist noch nicht zu spaet.",
                "en": "Say to the Baron quietly but audibly: We could talk. It is not too late.",
            }, "game_effect": "doctor_baron_tension"
        },

        "task_detective_writes": {
            "trigger_phase": 2, "trigger_condition": "detective_has_theory",
            "assigned_to": "detective",
            "instruction": {
                "de": "Schreib demonstrativ etwas auf. Wenn jemand fragt: Fakten.",
                "en": "Write something demonstratively. If asked: Facts.",
            }, "game_effect": "detective_writing"
        },

        "task_all_silence": {
            "trigger_phase": 2, "trigger_condition": "random_investigation",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Der Host klopft einmal. Alle schweigen 30 Sekunden. Danach sagt jeder einen einzigen Satz was er in dieser Stille gedacht hat.",
                "en": "Host knocks once. Everyone is silent for 30 seconds. Afterwards everyone says one sentence what they thought in this silence.",
            }, "game_effect": "silence"
        },

        "random_phone_buzz": {
            "trigger_phase": 2, "trigger_condition": "random_any_time",
            "assigned_to": "random",
            "instruction": {
                "de": "Schau heimlich auf dein Telefon. Lies nur fuer dich. Reagiere dann verwirrt.",
                "en": "Look secretly at your phone. Read only for yourself. Then react confused.",
            }, "game_effect": "random_confusion"
        },

        "random_knocking": {
            "trigger_phase": 2, "trigger_condition": "random_post_murder_20min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Dreimal klopfen. Alle halten inne. Host: Wer ist da? Niemand antwortet. 10 Sekunden Stille.",
                "en": "Three knocks. Everyone stops. Host: Who is there? Nobody answers. 10 seconds silence.",
            }, "game_effect": "door_knock"
        },

        "random_light": {
            "trigger_phase": 2, "trigger_condition": "atmosphere_trigger",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Licht kurz aus und wieder an. Wer bewegt sich? Wer greift nach etwas? Alle sagen danach was sie gesehen haben.",
                "en": "Light briefly off and back on. Who moves? Who reaches for something? Everyone says afterwards what they saw.",
            }, "game_effect": "darkness"
        },

        "random_rain": {
            "trigger_phase": 1, "trigger_condition": "game_start_5min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Host sagt: Draussen beginnt es zu regnen. Niemand kann jetzt gehen.",
                "en": "Host says: Outside it begins to rain. Nobody can leave now.",
            }, "game_effect": "rain"
        },

        "random_clock": {
            "trigger_phase": 1, "trigger_condition": "game_start_15min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Host sagt: Die Uhr schlaegt 22 Uhr. Baron klopft mit dem Glas: Ich habe eine Ankuendigung. Aber zuerst — trinken wir.",
                "en": "Host says: The clock strikes 10pm. Baron taps glass: I have an announcement. But first — let us drink.",
            }, "game_effect": "clock"
        },

        "random_smell": {
            "trigger_phase": 2, "trigger_condition": "investigation_10min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Host sagt: Aus der Kueche kommt ein Geruch. Suesszlich. Fast medizinisch. Alle schauen zur Koechen.",
                "en": "Host says: From the kitchen comes a smell. Sweet. Almost medicinal. Everyone looks at the cook.",
            }, "game_effect": "smell"
        },

        "random_lawyer": {
            "trigger_phase": 2, "trigger_condition": "investigation_20min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Host sagt: Ein Anwalt wartet draussen. Jemand hat ihn mitgebracht. Wer? 10 Sekunden Stille.",
                "en": "Host says: A lawyer waits outside. Someone brought him. Who? 10 seconds silence.",
            }, "game_effect": "lawyer"
        },

        "random_fog": {
            "trigger_phase": 3, "trigger_condition": "reckoning_near",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "Alle schreiben auf einen Zettel wen sie fuer den Moerder halten. Falten. Dem Host geben. Die Zettel werden am Ende geoeffnet.",
                "en": "Everyone writes who they think is the murderer. Fold. Give to host. The notes will be opened at the end.",
            }, "game_effect": "pre_vote"
        },
    },

    "role_connections": {
        "butler_niece_library": {"roles": ["butler", "niece"], "connection": "Der Butler sah Constanze in der Bibliothek. Beide wissen es. Keiner hat gesprochen.", "tension": "high"},
        "doctor_baron_complaint": {"roles": ["doctor", "baron"], "connection": "Der Arzt hat den Baron fast geblindet. Heute Abend die Klage.", "tension": "extreme"},
        "viktor_affair": {"roles": ["lover"], "connection": "Viktor hat eine Affaere. Gegenseitiges Alibi wenn einer redet.", "tension": "secret_alibi"},
        "stranger_murderer_irony": {"roles": ["stranger", "murderer"], "connection": "Der Fremde beschattet unwissentlich den Moerder.", "tension": "dramatic_irony"},
        "cook_murderer_substance": {"roles": ["cook", "murderer"], "connection": "Der Moerder beauftragte die Koechen. Sie kennt den Namen.", "tension": "critical"},
        "doctor_cook_saw": {"roles": ["doctor", "cook"], "connection": "Der Arzt sah was die Koechen aus seiner Tasche nahm. Beide schweigen.", "tension": "mutual_silence"},
        "witness_murderer_unknowing": {"roles": ["witness", "murderer"], "connection": "Die Zeugin sah den Moerder — weiss es aber nicht.", "tension": "dramatic_irony"},
        "stranger_niece_file": {"roles": ["stranger", "niece"], "connection": "Der Fremde hat eine Akte ueber Constanze.", "tension": "one_sided"},
        "detective_baron": {"roles": ["detective", "baron"], "connection": "Der Baron schrieb dem Inspektor und nannte einen Namen.", "tension": "mission_unfinished"},
        "niece_shadow_trade": {"roles": ["niece", "shadow"], "connection": "Die Schattenfigur braucht Testamentsinformation von Constanze.", "tension": "potential_trade"},
        "stranger_lover_affair": {"roles": ["stranger", "lover"], "connection": "Der Fremde findet bei Beschattung Beweise von Viktors Affaere.", "tension": "one_sided_irony"},
        "butler_shadow_blackmail": {"roles": ["butler", "shadow"], "connection": "Die Schattenfigur hat Info ueber Butlers Diebstahl.", "tension": "vulnerability"},
        "cook_shadow_payment": {"roles": ["cook", "shadow"], "connection": "Die Schattenfigur weiss von der Zahlung an die Koechen.", "tension": "one_sided_blackmail"},
        "doctor_niece_will": {"roles": ["doctor", "niece"], "connection": "Der Arzt weiss vom neuen Testament. Constanze weiss es nicht.", "tension": "information_asymmetry"},
    },

    "event_chains": [
        {"id": "chain_two_whispering", "trigger": "two_players_private_3min",
         "message_to_third": {"de": "Du bemerkst: {player_a} und {player_b} fluestern seit Minuten. Machst du alle darauf aufmerksam?", "en": "You notice: {player_a} and {player_b} have been whispering for minutes. Do you alert everyone?"}},
        {"id": "chain_heavy_drinker", "trigger": "someone_drinks_unusually_much",
         "message_to_observer": {"de": "{player} trinkt ungewoehnlich viel. Wein loest Zungen. Rede mit ihr/ihm.", "en": "{player} is drinking unusually much. Wine loosens tongues. Talk to them."}},
        {"id": "chain_refuses_drink", "trigger": "player_refuses_group_drink",
         "message_to_all": {"de": "Hat das jemand bemerkt? {player} hat beim gemeinsamen Trinken nicht mitgemacht.", "en": "Did anyone notice? {player} did not join in the group drink."}},
        {"id": "chain_accusation", "trigger": "someone_accuses_publicly",
         "message_to_murderer": {"de": "{player} verdaechtigt dich oeffentlich. Du hast 2 Minuten. Handle.", "en": "{player} is publicly suspecting you. You have 2 minutes. Act."}},
        {"id": "chain_ghost_death", "trigger": "baron_death_announced",
         "message_to_baron": {"de": "Du bist jetzt tot. Steh auf. Setz dich an den Rand. Beginne zu fluestern.", "en": "You are now dead. Stand up. Sit at the edge. Begin to whisper."}},
        {"id": "chain_witness_speaks", "trigger": "witness_makes_statement",
         "message_to_murderer": {"de": "Die Zeugin hat gesprochen. Handle bevor sie mehr sagt.", "en": "The witness has spoken. Act before she says more."}},
        {"id": "chain_butler_niece_exposed", "trigger": "butler_reveals_library_witness",
         "message_to_all": {"de": "Der Butler hat Constanze in der Bibliothek gesehen. Was hatte sie dort zu suchen?", "en": "The butler saw Constanze in the library. What was she doing there?"}},
    ],

    "atmosphere_messages": [
        {"trigger": "game_start_5min",     "text": {"de": "Draussen beginnt es zu regnen. Niemand kann jetzt gehen.", "en": "Outside it begins to rain. Nobody can leave now."}},
        {"trigger": "game_start_15min",    "text": {"de": "Die Uhr schlaegt 22 Uhr. Der Baron klopft mit seinem Glas: Ich habe eine Ankuendigung.", "en": "The clock strikes 10pm. The Baron taps his glass: I have an announcement."}},
        {"trigger": "murder_announced",    "text": {"de": "DER SCHREI. Aus der Bibliothek. Baron Aldric von Dunkelbach ist tot.", "en": "THE SCREAM. From the library. Baron Aldric von Dunkelbach is dead."}},
        {"trigger": "investigation_10min", "text": {"de": "Ein Geruch aus der Kueche. Suesszlich. Fast medizinisch.", "en": "A smell from the kitchen. Sweet. Almost medicinal."}},
        {"trigger": "investigation_20min", "text": {"de": "Ein Anwalt wartet draussen. Jemand hat ihn mitgebracht. Warum jetzt?", "en": "A lawyer waits outside. Someone brought him. Why now?"}},
        {"trigger": "tension_high",        "text": {"de": "Die Wahrheit ist nahe. Wer schweigt verliert. Wer luegt wird entlarvt.", "en": "The truth is close. Those who stay silent lose. Those who lie will be exposed."}}
    ],

    "endings": {
        "murderer_caught": {
            "condition": "majority_names_murderer_correctly",
            "title": {"de": "Gerechtigkeit", "en": "Justice", "fr": "Justice", "it": "Giustizia", "es": "Justicia", "pt": "Justica"},
            "text": {"de": "Der Moerder wurde ueberfuehrt. Nicht durch eine Abstimmung — durch Beweise, Beobachtung und die Wahrheit die immer ans Licht kommt.", "en": "The murderer was convicted. Not through a vote — through evidence, observation and the truth that always comes to light."}
        },
        "murderer_escapes": {
            "condition": "wrong_person_convicted",
            "title": {"de": "Der Moerder lacht", "en": "The Murderer Laughs", "fr": "L Assassin Rit", "it": "L Assassino Ride", "es": "El Asesino Rie", "pt": "O Assassino Ri"},
            "text": {"de": "Ein Unschuldiger wurde beschuldigt. Der wahre Moerder lacht. {murderer_name} hat gewonnen.", "en": "An innocent was accused. The real murderer laughs. {murderer_name} has won."}
        },
        "shadow_wins": {
            "condition": "shadow_steals_will_undiscovered",
            "title": {"de": "Das Testament ist weg", "en": "The Will is Gone"},
            "text": {"de": "Waehrend alle ermittelten — verschwand das Testament. Die Schattenfigur hat gewonnen.", "en": "While everyone investigated — the will disappeared. The Shadow figure has won."}
        },
        "perfect_solve": {
            "condition": "witness_and_doctor_both_correct",
            "title": {"de": "Die vollendete Loesung", "en": "The Perfect Solve"},
            "text": {"de": "Die Schriftstellerin und der Arzt haben gemeinsam das Unmoeliche geschafft. Das ist selten. Das ist brillant.", "en": "The writer and the doctor together accomplished the impossible. This is rare. This is brilliant."}
        },
        "two_crimes_solved": {
            "condition": "murderer_caught_and_shadow_discovered",
            "title": {"de": "Zwei Verbrechen, eine Nacht", "en": "Two Crimes, One Night"},
            "text": {"de": "Der Moerder wurde gefasst UND die Schattenfigur beim Testamentsdiebstahl ertappt. Das ist aussergewoehnlich.", "en": "The murderer was caught AND the Shadow figure caught stealing the will. That is extraordinary."}
        }
    }
}
