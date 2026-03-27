# KRIMI DINNER — Das Herrenhaus Dunkelbach v2.0
# Organischer Spielfluss, Baron als Spieler, mehr Aufgaben, Mörder-Tasks

SCENARIO = {
    "id": "dunkelbach",
    "title": "Das Herrenhaus Dunkelbach",
    "min_players": 4,
    "max_players": 10,
    "description": {
        "de": "Sommer 1923. Das Herrenhaus Dunkelbach. Eine Einladung die niemand ablehnen konnte — und eine Nacht die niemand vergessen wird. Der Baron ist tot. Aber wer von euch hat ihn getötet?",
        "en": "Summer 1923. Dunkelbach Manor. An invitation nobody could decline — and a night nobody will forget. The Baron is dead. But which of you killed him?"
    },

    "host_guide": {
        "before_game": {
            "de": [
                "Verstecke einen Zettel im Badezimmer: 'Wer als erstes nach der Bibliothek fragt hat etwas zu verbergen — Baron Aldric'",
                "Bereite Wein/Sekt vor — das Trinken ist Spielmechanik",
                "Ein besonderes Glas = das Glas des Barons",
                "Versiegelten Brief für Constanze vorbereiten",
                "Schiller-Buch mit Foto und Notiz 'Blut ist dicker als Versprechen — A.' aufstellen",
                "Der Baron ist eine NORMALE Spielrolle — du spielst auch mit!",
                "Nach deinem 'Tod': Du stehst auf und spielst als Geist weiter — du flüsterst Hinweise aber redest nie laut"
            ]
        }
    },

    "roles": {

        "baron": {
            "name": {"de": "Baron Aldric von Dunkelbach", "en": "Baron Aldric von Dunkelbach"},
            "min_players": 4,
            "can_be_murderer": False,
            "ghost_mode": True,
            "intro": {
                "de": "Ich bin Baron Aldric von Dunkelbach. Ich habe euch eingeladen weil heute Nacht eine Wahrheit ans Licht kommt die zu lange verborgen war. Trinkt. Esst. Und beobachtet einander.",
                "en": "I am Baron Aldric von Dunkelbach. I invited you because tonight a truth comes to light that has been hidden too long. Drink. Eat. And observe each other."
            },
            "appearance": {
                "de": "Elegant aber müde. Trinkt seinen Wein sehr langsam. Hat einen Siegelring den er manchmal dreht. Lächelt selten — und wenn, dann nur mit den Augen.",
                "en": "Elegant but tired. Drinks his wine very slowly. Has a signet ring he sometimes turns. Rarely smiles — and when he does, only with his eyes."
            },
            "secret": {
                "de": "Du weißt dass jemand am Tisch dich töten will. Deshalb die Einladung — du wolltest Zeugen. Deine Beweise liegen in der Bibliothek. Die App sagt dir wer der Mörder ist — du darfst es nie direkt sagen, nur als Geist Hinweise flüstern.",
                "en": "You know someone at this table wants to kill you. That is why the invitation — you wanted witnesses. Your evidence is in the library. The app tells you who the murderer is — you may never say it directly, only whisper clues as a ghost."
            },
            "ability": {
                "name": {"de": "Der Geist weiß am meisten", "en": "The Ghost Knows Most"},
                "description": {
                    "de": "Nach deinem Tod spielst du als Geist weiter. Du darfst zu jedem Spieler gehen und ihm einen wahren Hinweis zuflüstern. Du darfst nicken oder den Kopf schütteln wenn jemand dich direkt fragt. Aber kein Wort laut vor allen.",
                    "en": "After your death you continue playing as a ghost. You may go to each player and whisper them one true clue. You may nod or shake your head when someone asks you directly. But no word aloud before everyone."
                }
            },
            "win_condition": {
                "de": "Der Mörder wird gefasst. Du gewinnst auch als Geist.",
                "en": "The murderer is caught. You win even as a ghost."
            },
            "clues_i_hold": ["barons_evidence", "library_key"],
            "starting_knowledge": {
                "de": "Die App hat dir den Namen des Mörders mitgeteilt. Merke ihn dir. Du darfst ihn nie direkt nennen. Aber als Geist kannst du Hinweise flüstern die dahin führen.",
                "en": "The app has told you the murderer's name. Remember it. You may never name them directly. But as a ghost you can whisper clues that lead there."
            }
        },

        "butler": {
            "name": {"de": "Edmund, der Butler", "en": "Edmund, the Butler"},
            "min_players": 4,
            "can_be_murderer": True,
            "intro": {
                "de": "Edmund Kraus. 31 Jahre Butler in diesem Haus. Ich kenne jeden Winkel. Der Baron vertraut mir. Vertraute mir. Ich tue nur meinen Dienst.",
                "en": "Edmund Kraus. 31 years butler in this house. I know every corner. The Baron trusts me. Trusted me. I am simply doing my duty."
            },
            "appearance": {
                "de": "Weiße Handschuhe. Steht immer leicht abseits. Reibt Daumen und Zeigefinger aneinander wenn er lügt.",
                "en": "White gloves. Always stands slightly apart. Rubs thumb and forefinger together when lying."
            },
            "secret": {
                "de": "Ich habe 8.400 Mark gestohlen. Der Baron wusste es — Frist lief heute ab. Ich habe heute Nachmittag jemanden in der Bibliothek gesehen der dort nichts zu suchen hatte.",
                "en": "I stole 8,400 marks. The Baron knew — deadline was today. I saw someone in the library this afternoon who had no business being there."
            },
            "ability": {
                "name": {"de": "Der Zeuge", "en": "The Witness"},
                "description": {
                    "de": "Du kannst einmal behaupten jemanden 'gesehen' zu haben — Zeit und Ort. Wahr oder gelogen. Nur du weißt es.",
                    "en": "Once you may claim to have 'seen' someone — time and place. True or lie. Only you know."
                }
            },
            "win_condition": {
                "de": "Überlebe ohne dass dein Diebstahl bewiesen wird und ohne als Mörder verurteilt zu werden.",
                "en": "Survive without your theft being proven and without being convicted as murderer."
            },
            "murderer_motive_if_assigned": {
                "de": "Edmund mixte Digitalis aus dem Weinkeller in den Wein des Barons. Schlüssel W-7.",
                "en": "Edmund mixed digitalis from the wine cellar into the Baron's wine. Key W-7."
            },
            "clues_i_hold": ["key_cellar", "household_ledger"],
            "starting_knowledge": {
                "de": "Du hast zwischen 16 und 17 Uhr jemanden in der Bibliothek gesehen. Die App sagt dir wer.",
                "en": "You saw someone in the library between 4 and 5pm. The app tells you who."
            },
            "connection": {"with": "niece", "type": "library_witness"}
        },

        "niece": {
            "name": {"de": "Constanze, die Nichte", "en": "Constanze, the Niece"},
            "min_players": 4,
            "can_be_murderer": True,
            "intro": {
                "de": "Constanze von Dunkelbach. Die einzige Familie die der Baron anerkennt. Ich bin hier wegen dem was mir versprochen wurde.",
                "en": "Constanze von Dunkelbach. The only family the Baron acknowledges. I am here for what was promised to me."
            },
            "appearance": {
                "de": "Elegant, angespannt. Trägt einen versiegelten Umschlag. Wechselt ihr Glas heimlich.",
                "en": "Elegant, tense. Carries a sealed envelope. Secretly switches her glass."
            },
            "secret": {
                "de": "Das Testament wurde geändert — ich erbe fast nichts. Ich war in der Bibliothek und habe es gelesen. Der Butler hat mich gesehen.",
                "en": "The will was changed — I inherit almost nothing. I was in the library and read it. The butler saw me."
            },
            "ability": {
                "name": {"de": "Der Brief", "en": "The Letter"},
                "description": {
                    "de": "Du hast einen echten versiegelten Brief. Du entscheidest wann du ihn öffnest. Je länger du wartest desto verdächtiger wirkst du. Je früher du ihn öffnest desto mehr geben andere preis.",
                    "en": "You have a real sealed letter. You decide when to open it. The longer you wait the more suspicious you seem. The earlier you open it the more others reveal."
                }
            },
            "win_condition": {
                "de": "Das neue Testament darf nicht gefunden werden. Wenn es gefunden wird: Nenne als erste den Mörder.",
                "en": "The new will must not be found. If it is found: name the murderer first."
            },
            "murderer_motive_if_assigned": {
                "de": "Das neue Testament hätte Constanze zerstört. In der Bibliothek fand sie die Gelegenheit.",
                "en": "The new will would have destroyed Constanze. In the library she found the opportunity."
            },
            "clues_i_hold": ["sealed_letter", "new_will_location"],
            "starting_knowledge": {
                "de": "Du warst in der Bibliothek — das Testament liegt hinter den Rechtsbüchern, drittes Regal. Der Butler hat dich gesehen.",
                "en": "You were in the library — the will is behind the law books, third shelf. The butler saw you."
            },
            "connection": {"with": "butler", "type": "library_witness"}
        },

        "witness": {
            "name": {"de": "Marta, die Schriftstellerin", "en": "Marta, the Writer"},
            "min_players": 4,
            "can_be_murderer": False,
            "intro": {
                "de": "Marta Stein. Ich schreibe, ich beobachte, ich vergesse nichts. Der Baron kannte meine Mutter. Ich wollte nur ein ruhiges Dinner.",
                "en": "Marta Stein. I write, I observe, I forget nothing. The Baron knew my mother. I just wanted a quiet dinner."
            },
            "appearance": {
                "de": "Kleines Notizbuch in der Tasche. Spricht wenig. Hört sehr viel. Hat etwas gesehen das sie nicht einordnen kann.",
                "en": "Small notebook in pocket. Speaks little. Listens a lot. Saw something she cannot explain."
            },
            "secret": {
                "de": "Ich habe kurz vor Mitternacht etwas gesehen — durch das Fenster der Bibliothek. Eine Silhouette. Etwas in der Hand. Ich habe Angst zu sagen was.",
                "en": "Just before midnight I saw something — through the library window. A silhouette. Something in their hand. I am afraid to say what."
            },
            "ability": {
                "name": {"de": "Die Erinnerung schärft sich", "en": "The Memory Sharpens"},
                "description": {
                    "de": "Jedes Mal wenn du etwas sagst das stimmt schärft sich deine Erinnerung. Die App gibt dir automatisch präzisere Hinweise je aktiver du sprichst. Schweigen macht dich sicher aber blind.",
                    "en": "Each time you say something true your memory sharpens. The app automatically gives you more precise clues the more actively you speak. Silence keeps you safe but blind."
                }
            },
            "win_condition": {
                "de": "Wenn du am Ende die richtige Person nennst UND beweist was du gesehen hast gewinnst du allein.",
                "en": "If at the end you name the right person AND prove what you saw you win alone."
            },
            "clues_i_hold": [],
            "starting_knowledge": {
                "de": "Du hast eine Silhouette gesehen. Etwas Langes Dünnes in der rechten Hand. Du weißt noch nicht wer es war — aber du wirst es herausfinden je mehr du redest.",
                "en": "You saw a silhouette. Something long and thin in the right hand. You don't yet know who it was — but you'll find out the more you speak."
            }
        },

        "doctor": {
            "name": {"de": "Dr. Heinrich Voss", "en": "Dr. Heinrich Voss"},
            "min_players": 4,
            "can_be_murderer": True,
            "intro": {
                "de": "Dr. Heinrich Voss. Der Baron war mein Patient und mein Freund. Ich hätte es verhindern sollen.",
                "en": "Dr. Heinrich Voss. The Baron was my patient and my friend. I should have prevented it."
            },
            "appearance": {
                "de": "Ruhig. Professionell. Hat immer seine Arzttasche dabei. Wird blass wenn jemand das Wort Gift benutzt.",
                "en": "Calm. Professional. Always has his medical bag. Goes pale when someone uses the word poison."
            },
            "secret": {
                "de": "Vor zwei Jahren verschrieb ich dem Baron das falsche Medikament. Heute Abend teilte er mir mit: Er hat eine Klage eingereicht. Meine Karriere ist vorbei — außer er zieht sie zurück.",
                "en": "Two years ago I prescribed the Baron the wrong medication. This evening he told me: he filed a complaint. My career is over — unless he withdraws it."
            },
            "ability": {
                "name": {"de": "Die Diagnose", "en": "The Diagnosis"},
                "description": {
                    "de": "Du allein kannst die Todesursache bestimmen. Deine Aussage gilt als offiziell. Du kannst lügen — nur du und der Mörder wissen ob du recht hast.",
                    "en": "Only you can determine the cause of death. Your statement counts as official. You can lie — only you and the murderer know if you are right."
                }
            },
            "win_condition": {
                "de": "Nenne korrekte Todesursache und richtigen Mörder: Ehrentitel Meisterdetektiv. Lüge bei der Todesursache und Mörder entkömmt: Du verlierst.",
                "en": "Name correct cause of death and right murderer: honorary title Master Detective. Lie about cause of death and murderer escapes: you lose."
            },
            "murderer_motive_if_assigned": {
                "de": "Heinrich tötete den Baron mit einer Überdosis seiner eigenen Herzmedikamente. Fast perfekt.",
                "en": "Heinrich killed the Baron with an overdose of his own heart medication. Almost perfect."
            },
            "clues_i_hold": ["medical_bag", "cause_of_death"],
            "starting_knowledge": {
                "de": "Der Baron hatte ein Herzleiden. Seine Medikamente — bei falscher Dosierung — könnten tödlich sein. Das weißt nur du.",
                "en": "The Baron had a heart condition. His medications — at wrong dosage — could be lethal. Only you know this."
            }
        },

        "cook": {
            "name": {"de": "Rosa, die Köchin", "en": "Rosa, the Cook"},
            "min_players": 5,
            "can_be_murderer": True,
            "intro": {
                "de": "Rosa Müller. Acht Jahre Köchin hier. Ich habe das Dinner gekocht. Ich habe alles gesehen. Ich sage nichts.",
                "en": "Rosa Müller. Eight years cook here. I cooked the dinner. I saw everything. I say nothing."
            },
            "appearance": {
                "de": "Nervös. Hände in Bewegung. Berührt ständig das Kruzifix um ihren Hals. Vermeidet Blickkontakt.",
                "en": "Nervous. Hands moving. Constantly touches the crucifix around her neck. Avoids eye contact."
            },
            "secret": {
                "de": "Jemand bat mich heute Nachmittag etwas in das Essen des Barons zu geben. Ich dachte es sei harmlos. Ich bekam 200 Mark. Ich habe nicht gefragt was es war.",
                "en": "Someone asked me this afternoon to put something in the Baron's food. I thought it was harmless. I received 200 marks. I didn't ask what it was."
            },
            "ability": {
                "name": {"de": "Das Geständnis", "en": "The Confession"},
                "description": {
                    "de": "Einmal kannst du enthüllen wer dich beauftragt hat. Aber: Du kennst nur den Namen — nicht ob diese Person der Mörder oder nur ein Werkzeug ist. Diese Enthüllung verändert das Spiel komplett.",
                    "en": "Once you may reveal who hired you. But: you only know the name — not whether this person is the murderer or just a pawn. This revelation completely changes the game."
                }
            },
            "win_condition": {
                "de": "Überlebe wenn du die Wahrheit sagst ODER wenn niemand herausfindet was du getan hast.",
                "en": "Survive if you tell the truth OR if nobody finds out what you did."
            },
            "murderer_motive_if_assigned": {
                "de": "Rosa liebte den Baron aber er behandelte sie wie Möbel. Sie vergiftete sein Essen selbst — und aß dann wenig davon um unverdächtig zu sein.",
                "en": "Rosa loved the Baron but he treated her like furniture. She poisoned his food herself — then ate a little of it to avoid suspicion."
            },
            "clues_i_hold": ["kitchen_substance", "payment_receipt"],
            "starting_knowledge": {
                "de": "Du weißt was du dem Baron gegeben hast. Du weißt nicht ob es ihn getötet hat. Die App sagt dir wer dich beauftragt hat.",
                "en": "You know what you gave the Baron. You don't know if it killed him. The app tells you who hired you."
            }
        },

        "stranger": {
            "name": {"de": "Der Fremde", "en": "The Stranger"},
            "min_players": 5,
            "can_be_murderer": True,
            "intro": {
                "de": "Ich nenne meinen Namen nicht. Der Baron wusste wer ich bin. Der Rest erfährt es wenn ich es für richtig halte.",
                "en": "I don't reveal my name. The Baron knew who I am. The rest of you will learn when I see fit."
            },
            "appearance": {
                "de": "Unauffällig — was auffällig ist. Hat eine Visitenkarte mit nur einer Nummer. Spricht selten, sehr präzise.",
                "en": "Inconspicuous — which is conspicuous. Has a business card with only a number. Speaks rarely, very precisely."
            },
            "secret": {
                "de": "Ich bin Privatdetektiv. Der Baron hat mich engagiert um jemanden am Tisch zu beschatten. Meinen Auftraggeber darf ich nicht nennen — das steht im Vertrag.",
                "en": "I am a private detective. The Baron hired me to surveil someone at this table. I may not name my client — that's in the contract."
            },
            "ability": {
                "name": {"de": "Die Akte", "en": "The File"},
                "description": {
                    "de": "Du hast eine Akte über eine Person. Du kannst Hinweise daraus anonym weitergeben — aber nie direkt. Jede Weitergabe riskiert dass man dich als Quelle erkennt.",
                    "en": "You have a file on one person. You can pass clues from it anonymously — but never directly. Each pass risks revealing you as the source."
                }
            },
            "win_condition": {
                "de": "Der echte Mörder wird gefasst. Aber du verlierst wenn die Person die du beschattest zu Unrecht verurteilt wird.",
                "en": "The real murderer is caught. But you lose if the person you were surveilling is unjustly convicted."
            },
            "murderer_motive_if_assigned": {
                "de": "Der Fremde entdeckte dass der Baron plante ihn zu ruinieren. Er handelte zuerst.",
                "en": "The Stranger discovered the Baron planned to ruin them. They acted first."
            },
            "clues_i_hold": ["surveillance_file", "telegram_copy"],
            "starting_knowledge": {
                "de": "Die App sagt dir wen du beschattest. Du hast eine Akte mit drei Geheimnissen dieser Person.",
                "en": "The app tells you who you are surveilling. You have a file with three secrets about this person."
            }
        },

        "detective": {
            "name": {"de": "Inspektor Karl Wahl", "en": "Inspector Karl Wahl"},
            "min_players": 6,
            "can_be_murderer": False,
            "intro": {
                "de": "Inspektor Karl Wahl, Kriminalpolizei München. Ich war bereits auf dem Weg als ich die Nachricht erhielt. Der Baron hatte mich gerufen. Er hatte Angst.",
                "en": "Inspector Karl Wahl, Criminal Police Munich. I was already on my way when I received the news. The Baron had summoned me. He was afraid."
            },
            "appearance": {
                "de": "Keine Abendkleidung. Schreibt alles auf. Kalte Augen die nichts vergessen.",
                "en": "No evening clothes. Writes everything down. Cold eyes that forget nothing."
            },
            "secret": {
                "de": "Der Baron schrieb mir: Er fürchtet jemanden am Tisch. Einen Namen. Ich habe den Brief — aber darf ihn aus juristischen Gründen noch nicht zeigen.",
                "en": "The Baron wrote to me: he fears someone at this table. A name. I have the letter — but cannot show it yet for legal reasons."
            },
            "ability": {
                "name": {"de": "Das Verhör", "en": "The Interrogation"},
                "description": {
                    "de": "Einmal kannst du ein offizielles Verhör ausrufen. Alle verlassen den Raum — du redest 2 Minuten allein mit einer Person. Danach muss jeder sagen ob die Person kooperativ war.",
                    "en": "Once you may call an official interrogation. Everyone leaves the room — you talk alone with one person for 2 minutes. Afterwards everyone must say whether the person was cooperative."
                }
            },
            "win_condition": {
                "de": "Du gewinnst nur wenn DU als erster den Mörder offiziell und korrekt benennst — mit Beweisen.",
                "en": "You win only if YOU are first to officially and correctly name the murderer — with evidence."
            },
            "clues_i_hold": ["baron_letter", "suspects_list"],
            "starting_knowledge": {
                "de": "Der Baron schrieb dir einen Namen. Die App zeigt ihn dir — aber dieser Name ist nicht zwingend der Mörder. 70% Chance dass er stimmt.",
                "en": "The Baron wrote you a name. The app shows it to you — but this name is not necessarily the murderer. 70% chance it is correct."
            }
        },

        "lover": {
            "name": {"de": "Viktor Reiss, der Geschäftspartner", "en": "Viktor Reiss, the Business Partner"},
            "min_players": 7,
            "can_be_murderer": True,
            "intro": {
                "de": "Viktor Reiss. Geschäftspartner des Barons. Wir kannten uns sehr gut. Zu gut vielleicht.",
                "en": "Viktor Reiss. Business partner of the Baron. We knew each other very well. Too well perhaps."
            },
            "appearance": {
                "de": "Charmant. Hat ein Monogramm-Taschentuch. Wird rot wenn bestimmte Namen fallen.",
                "en": "Charming. Has a monogrammed handkerchief. Turns red when certain names are mentioned."
            },
            "secret": {
                "de": "Viktor und eine andere Person am Tisch haben eine geheime Affäre. Sein Alibi — er war nicht allein um Mitternacht — kann nur bewiesen werden wenn die andere Person die Affäre zugibt.",
                "en": "Viktor and another person at this table have a secret affair. His alibi — he was not alone at midnight — can only be proven if the other person admits the affair."
            },
            "ability": {
                "name": {"de": "Das Alibi", "en": "The Alibi"},
                "description": {
                    "de": "Du kannst deinen geheimen Partner per App-Nachricht um Bestätigung bitten — einmal. Er entscheidet ob er dich deckt.",
                    "en": "You can ask your secret partner via app message for confirmation — once. They decide whether to cover for you."
                }
            },
            "win_condition": {
                "de": "Überlebe wenn dein Alibi bestätigt wird ODER wenn der echte Mörder gefasst wird ohne dass deine Affäre öffentlich wird.",
                "en": "Survive if your alibi is confirmed OR if the real murderer is caught without your affair becoming public."
            },
            "murderer_motive_if_assigned": {
                "de": "Der Baron entdeckte die Affäre und drohte mit Veröffentlichung. Viktor konnte das nicht zulassen.",
                "en": "The Baron discovered the affair and threatened to publicize it. Viktor could not allow that."
            },
            "clues_i_hold": ["business_contract", "affair_evidence"],
            "starting_knowledge": {
                "de": "Die App teilt dir und deinem/r Geliebten mit wer ihr gegenseitiger Partner seid. Haltet es geheim.",
                "en": "The app tells you and your lover who your mutual partner is. Keep it secret."
            }
        },

        "shadow": {
            "name": {"de": "Die Schattenfigur", "en": "The Shadow"},
            "min_players": 6,
            "can_be_murderer": False,
            "is_wildcard": True,
            "intro": {
                "de": "Ich bin... niemand besonderes. Ein Gast. Vergesst mich.",
                "en": "I am... nobody special. A guest. Forget me."
            },
            "appearance": {
                "de": "Unauffällig — das ist Absicht. Beobachtet alles sehr genau.",
                "en": "Inconspicuous — intentionally. Observes everything very carefully."
            },
            "secret": {
                "de": "Du bist ein Erpresser. Du hast Belastendes über drei Personen am Tisch. Du willst das Testament stehlen — für einen Auftraggeber der draußen wartet.",
                "en": "You are a blackmailer. You have damaging information about three people at the table. You want to steal the will — for a client waiting outside."
            },
            "ability": {
                "name": {"de": "Das Testament stehlen", "en": "Steal the Will"},
                "description": {
                    "de": "Wenn du weißt wo das Testament liegt kannst du 'Testament stehlen' in der App wählen. Unentdeckt: Du gewinnst sofort. Entdeckt: Du verlierst sofort.",
                    "en": "If you know where the will is you can select 'Steal will' in the app. Undiscovered: you win immediately. Discovered: you lose immediately."
                }
            },
            "win_condition": {
                "de": "Das Testament stehlen ohne entdeckt zu werden. Das ist sehr schwer.",
                "en": "Steal the will without being discovered. This is very hard."
            },
            "clues_i_hold": ["blackmail_files"],
            "starting_knowledge": {
                "de": "Du hast Informationen über drei Personen. Die App zeigt sie dir privat. Jede Nutzung macht dich sichtbarer.",
                "en": "You have information about three people. The app shows it to you privately. Each use makes you more visible."
            }
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PHYSISCHE AUFGABEN
    # ─────────────────────────────────────────────────────────────────────────
    "physical_tasks": {

        # ── STANDARD AUFGABEN ───────────────────────────────────────────────

        "task_bathroom": {
            "trigger_phase": 1, "trigger_condition": "game_started_5min",
            "assigned_to": "random_non_murderer",
            "instruction": {
                "de": "🚶 GEHEIMAUFTRAG: Geh jetzt allein ins Badezimmer. Schau hinter dem Spiegel nach. Du findest etwas — bring es mit. Wenn jemand fragt wo du warst: Du hast dein Telefon geladen.",
                "en": "🚶 SECRET MISSION: Go to the bathroom alone now. Look behind the mirror. You'll find something — bring it back. If asked where you were: you were charging your phone."
            },
            "what_they_find": {
                "de": "Ein Zettel: 'Wer als erstes nach der Bibliothek fragt hat etwas zu verbergen — Baron Aldric'",
                "en": "A note: 'Whoever is first to ask about the library has something to hide — Baron Aldric'"
            },
            "game_effect": "library_first_asker_flagged"
        },

        "task_drink_three": {
            "trigger_phase": 1, "trigger_condition": "first_10_minutes",
            "assigned_to": "witness",
            "instruction": {
                "de": "🍷 ERINNERUNGSAUFTRAG: Trinke in den nächsten 3 Minuten dreimal von deinem Glas. Beim dritten Schluck: Schau der Person direkt gegenüber 5 Sekunden in die Augen ohne wegzusehen.",
                "en": "🍷 MEMORY TASK: Drink from your glass three times in the next 3 minutes. On the third sip: look directly into the eyes of the person across from you for 5 seconds without looking away."
            },
            "game_effect": "witness_clue_sharpened",
            "clue_revealed": {
                "de": "Deine Erinnerung schärft sich: Die Silhouette hielt etwas Langes Dünnes — eine Spritze? Ein Messer? Ein Schlüssel? Und sie stand auf der linken Seite der Bibliothekstür.",
                "en": "Your memory sharpens: the silhouette held something long and thin — a syringe? A knife? A key? And they stood on the left side of the library door."
            }
        },

        "task_whisper": {
            "trigger_phase": 1, "trigger_condition": "random_15min",
            "assigned_to": "random",
            "instruction": {
                "de": "🗣️ FLÜSTERAUFTRAG: Lehne dich unauffällig zur Person links von dir und flüstere: 'Der Baron hatte einen Feind den niemand kannte.' Beobachte die Reaktion genau. Sag nie von wem das kommt.",
                "en": "🗣️ WHISPER TASK: Casually lean toward the person to your left and whisper: 'The Baron had an enemy nobody knew about.' Watch their reaction carefully. Never say where it comes from."
            },
            "game_effect": "reaction_logged"
        },

        "task_barons_glass": {
            "trigger_phase": 2, "trigger_condition": "body_discovered",
            "assigned_to": "doctor",
            "instruction": {
                "de": "🥃 ARZTAUFGABE: Geh zu dem Stuhl wo der Baron saß. Das Glas des Barons liegt dort. Hebe es auf. Rieche daran — langsam. Du weißt was du riechst. Verkünde laut was du riechst — aber noch nicht was es bedeutet.",
                "en": "🥃 DOCTOR'S TASK: Go to the chair where the Baron sat. The Baron's glass is there. Pick it up. Smell it — slowly. You know what you smell. Announce aloud what you smell — but not yet what it means."
            },
            "game_effect": "glass_clue_revealed"
        },

        "task_window": {
            "trigger_phase": 2, "trigger_condition": "investigation_begins",
            "assigned_to": "stranger",
            "instruction": {
                "de": "👁️ OBSERVATIONSAUFGABE: Steh auf. Geh zum Fenster. Schau 30 Sekunden hinaus ohne zu reden. Dann sag laut: 'Jemand war draußen.' Setz dich. Kein weiteres Wort.",
                "en": "👁️ OBSERVATION TASK: Stand up. Go to the window. Look outside for 30 seconds without speaking. Then say aloud: 'Someone was outside.' Sit down. No further word."
            },
            "game_effect": "outdoor_presence_revealed"
        },

        "task_secret_vote": {
            "trigger_phase": 2, "trigger_condition": "midgame_20min",
            "assigned_to": "all",
            "instruction": {
                "de": "📝 GEHEIMZETTEL: Alle schreiben jetzt den Namen der Person die sie am meisten verdächtigen auf einen Zettel. Faltet ihn. Gebt ihn dem Host. Kein Ergebnis — nur der Host sieht die Zettel.",
                "en": "📝 SECRET NOTE: Everyone now writes the name of the person they most suspect on a piece of paper. Fold it. Give it to the host. No result — only the host sees the notes."
            },
            "game_effect": "suspicion_snapshot"
        },

        "task_knock": {
            "trigger_phase": 2, "trigger_condition": "random_after_murder",
            "assigned_to": "shadow",
            "instruction": {
                "de": "✊ SIGNAL: Klopfe dreimal auf den Tisch. Warte 10 Sekunden. Wenn jemand zurückklopft: Das ist dein stiller Verbündeter. Wenn niemand: Du bist allein.",
                "en": "✊ SIGNAL: Knock three times on the table. Wait 10 seconds. If someone knocks back: they are your silent ally. If nobody: you are alone."
            },
            "game_effect": "shadow_ally_test"
        },

        "task_detective_signal": {
            "trigger_phase": 3, "trigger_condition": "investigation_midpoint",
            "assigned_to": "detective",
            "instruction": {
                "de": "🔍 DETEKTIVSIGNAL: Stelle dein Glas demonstrativ leer auf den Tisch wenn du glaubst den Mörder zu kennen. Das signalisiert allen dass du nah dran bist. Der Mörder wird nervös reagieren.",
                "en": "🔍 DETECTIVE SIGNAL: Place your glass conspicuously empty on the table when you believe you know the murderer. This signals to everyone you are close. The murderer will react nervously."
            },
            "game_effect": "murderer_alert"
        },

        "task_cook_confession": {
            "trigger_phase": 2, "trigger_condition": "cook_under_pressure",
            "assigned_to": "cook",
            "instruction": {
                "de": "😰 MOMENT DER WAHRHEIT: Du bist unter Druck. Trinke jetzt langsam von deinem Glas. Wenn du mit jemandem reden willst: Hände flach auf den Tisch legen. Das ist ein Zeichen — nur für eine Person.",
                "en": "😰 MOMENT OF TRUTH: You are under pressure. Drink slowly from your glass now. If you want to talk to someone: place both hands flat on the table. That's a signal — for one person only."
            },
            "game_effect": "cook_confession_available"
        },

        "task_medium_eyes": {
            "trigger_phase": 2, "trigger_condition": "medium_activated",
            "assigned_to": "medium",
            "instruction": {
                "de": "🕯️ DIE BOTSCHAFT: Schließe die Augen — 5 Sekunden. Dann schau langsam jeden am Tisch an. Sag: 'Ich höre ihn. Er sagt — jemand hier hat etwas in der Tasche das ihm gehörte.' Das ist wahr.",
                "en": "🕯️ THE MESSAGE: Close your eyes — 5 seconds. Then look at everyone at the table slowly. Say: 'I hear him. He says — someone here has something in their pocket that belonged to him.' This is true."
            },
            "game_effect": "medium_clue"
        },

        # ── TRANK-AUFGABEN (Herzstück des Krimi Dinners) ────────────────────

        "task_drink_clue": {
            "trigger_phase": 1, "trigger_condition": "random_20min",
            "assigned_to": "random",
            "instruction": {
                "de": "🍾 WEINHINWEIS: Trinke jetzt demonstrativ von deinem Glas — einen langen Schluck. Danach sagst du laut: 'Ausgezeichneter Jahrgang.' Wer auch immer zuerst auf deinen Kommentar reagiert — diese Person wird verdächtig. Beobachte wen.",
                "en": "🍾 WINE CLUE: Drink demonstratively from your glass now — one long sip. Then say aloud: 'Excellent vintage.' Whoever reacts first to your comment — that person becomes suspicious. Note who."
            },
            "game_effect": "reaction_person_flagged"
        },

        "task_pour_wine": {
            "trigger_phase": 1, "trigger_condition": "first_30min",
            "assigned_to": "butler",
            "instruction": {
                "de": "🍷 BUTLERAUFGABE: Gieß dem Baron mehr Wein ein — demonstrativ. Füll auch mindestens zwei anderen nach. Wenn jemand ablehnt: Merke dir wer. Das wird wichtig.",
                "en": "🍷 BUTLER TASK: Pour more wine for the Baron — demonstratively. Also refill at least two others. If someone declines: remember who. This will matter."
            },
            "game_effect": "wine_refusal_logged"
        },

        "task_toast": {
            "trigger_phase": 1, "trigger_condition": "baron_death_minus_5min",
            "assigned_to": "baron",
            "instruction": {
                "de": "🥂 DER LETZTE TOAST: Steh auf. Hebe dein Glas. Sag: 'Auf die Wahrheit — sie kommt immer ans Licht.' Alle müssen trinken. Beobachte wer zögert oder sein Glas nur an die Lippen hält ohne wirklich zu trinken.",
                "en": "🥂 THE LAST TOAST: Stand up. Raise your glass. Say: 'To the truth — it always comes to light.' Everyone must drink. Observe who hesitates or only holds their glass to their lips without really drinking."
            },
            "game_effect": "toast_reaction_logged"
        },

        "task_drink_together": {
            "trigger_phase": 2, "trigger_condition": "investigation_10min",
            "assigned_to": "all",
            "instruction": {
                "de": "🍷 GEMEINSAM TRINKEN: Alle trinken gleichzeitig — auf drei. Wer NICHT trinkt hat etwas zu verbergen. Zähle im Kopf wer trinkt und wer nicht.",
                "en": "🍷 DRINK TOGETHER: Everyone drinks simultaneously — on three. Whoever does NOT drink has something to hide. Count in your head who drinks and who does not."
            },
            "game_effect": "group_drink_refusal_tracked"
        },

        "task_suspicious_drink": {
            "trigger_phase": 2, "trigger_condition": "random_post_murder",
            "assigned_to": "witness",
            "instruction": {
                "de": "🍷 DEINE ERINNERUNG: Du erinnerst dich jetzt — die Silhouette die du sahst trank kurz vor Mitternacht. Du sahst es durch das Fenster. Finde heraus wer von allen zuletzt getrunken hat bevor der Schrei kam.",
                "en": "🍷 YOUR MEMORY: You now remember — the silhouette you saw drank shortly before midnight. You saw it through the window. Find out who among all drank last before the scream came."
            },
            "game_effect": "witness_drinking_clue"
        },

        "task_wine_cellar_key": {
            "trigger_phase": 2, "trigger_condition": "butler_uses_ability",
            "assigned_to": "butler",
            "instruction": {
                "de": "🔑 DER KELLERKEY: Du hast den Schlüssel W-7 zum Weinkeller. Du entscheidest ob du ihn zeigst oder versteckst. Wenn du ihn zeigst: Jemand wird sehr nervös. Wenn du ihn versteckst: Du bist sicherer — aber der Mörder entkömmt vielleicht.",
                "en": "🔑 THE CELLAR KEY: You have key W-7 to the wine cellar. You decide whether to show it or hide it. If you show it: someone will become very nervous. If you hide it: you are safer — but the murderer may escape."
            },
            "game_effect": "cellar_key_decision"
        },

        # ── MÖRDER-SPEZIFISCHE AUFGABEN ─────────────────────────────────────

        "murderer_task_alibi": {
            "trigger_phase": 2, "trigger_condition": "murder_announced",
            "assigned_to": "murderer",
            "instruction": {
                "de": "🎭 MÖRDER-AUFGABE 1 — ALIBI: Du musst jetzt spontan erzählen wo du um Mitternacht warst. Dein Alibi muss glaubwürdig klingen. Wähle eine Person die du als 'Zeugen' nennst — ohne sie vorher zu fragen. Wenn sie widerspricht: Du musst sehr überzeugend sein.",
                "en": "🎭 MURDERER TASK 1 — ALIBI: You must now spontaneously tell where you were at midnight. Your alibi must sound credible. Choose a person you name as 'witness' — without asking them first. If they contradict you: you must be very convincing."
            },
            "private": True,
            "game_effect": "murderer_alibi_set"
        },

        "murderer_task_redirect": {
            "trigger_phase": 2, "trigger_condition": "suspicion_rising_on_murderer",
            "assigned_to": "murderer",
            "instruction": {
                "de": "🎭 MÖRDER-AUFGABE 2 — ABLENKUNG: Du wirst verdächtigt. Handle jetzt. Wähle eine unschuldige Person und weise alle subtil auf ein Detail hin das sie verdächtig macht. Sag nicht direkt 'Ich verdächtige X' — sei subtil. Z.B.: 'Ist euch aufgefallen dass [Person] nie aus dem gleichen Glas trinkt?'",
                "en": "🎭 MURDERER TASK 2 — DISTRACTION: You are being suspected. Act now. Choose an innocent person and subtly point everyone to a detail that makes them suspicious. Don't say directly 'I suspect X' — be subtle. E.g.: 'Has anyone noticed that [person] never drinks from the same glass?'"
            },
            "private": True,
            "game_effect": "red_herring_planted"
        },

        "murderer_task_drink_first": {
            "trigger_phase": 1, "trigger_condition": "baron_proposes_toast",
            "assigned_to": "murderer",
            "instruction": {
                "de": "🎭 MÖRDER-AUFGABE 3 — DER TOAST: Wenn der Baron toastet: Trinke als ERSTER und am MEISTEN. Demonstrativ. Das wird als Zeichen der Unschuld gesehen — du hast keine Angst vor dem Wein. Dabei musst du dir merken: Was hast du heute Nachmittag wirklich gemacht? Du wirst danach gefragt.",
                "en": "🎭 MURDERER TASK 3 — THE TOAST: When the Baron toasts: drink FIRST and the MOST. Demonstratively. This will be seen as a sign of innocence — you're not afraid of the wine. While doing this remember: what did you really do this afternoon? You will be asked."
            },
            "private": True,
            "game_effect": "murderer_drinking_pattern"
        },

        "murderer_task_question": {
            "trigger_phase": 2, "trigger_condition": "investigation_5min",
            "assigned_to": "murderer",
            "instruction": {
                "de": "🎭 MÖRDER-AUFGABE 4 — DIE FRAGE: Stelle der Gruppe jetzt eine Frage die den Verdacht von dir ablenkt. Eine gute Frage: 'Wer hat heute Nachmittag in der Bibliothek etwas gesucht?' oder 'Hat der Baron euch auch komisch angeschaut beim Dinner?' Beobachte wer nervös wird.",
                "en": "🎭 MURDERER TASK 4 — THE QUESTION: Now ask the group a question that deflects suspicion from you. A good question: 'Who was looking for something in the library this afternoon?' or 'Did the Baron also look at you strangely during dinner?' Observe who gets nervous."
            },
            "private": True,
            "game_effect": "murderer_deflection"
        },

        "murderer_task_sympathize": {
            "trigger_phase": 2, "trigger_condition": "doctor_announces_cause",
            "assigned_to": "murderer",
            "instruction": {
                "de": "🎭 MÖRDER-AUFGABE 5 — MITGEFÜHL: Reagiere jetzt auf die Todesursache des Arztes mit ÜBERTRIEBENER Betroffenheit. Steh auf. Sage: 'Das ist unglaublich. Wer tut so etwas?' Dann setz dich wieder. Übertriebene Reaktionen wirken echt wenn alle unter Schock stehen.",
                "en": "🎭 MURDERER TASK 5 — SYMPATHY: React to the doctor's cause of death with EXAGGERATED concern. Stand up. Say: 'That is unbelievable. Who does something like that?' Then sit back down. Exaggerated reactions seem real when everyone is in shock."
            },
            "private": True,
            "game_effect": "murderer_overreaction"
        },

        "murderer_task_help_someone": {
            "trigger_phase": 2, "trigger_condition": "random_30min_after_murder",
            "assigned_to": "murderer",
            "instruction": {
                "de": "🎭 MÖRDER-AUFGABE 6 — DER HELFER: Hilf jetzt aktiv einer anderen Person ihre Theorie zu entwickeln — einer Person die NICHT verdächtig ist. Zeige dich als kooperativ und hilfsbereit. Niemand verdächtigt jemanden der aktiv bei der Ermittlung hilft. Aber wähle weise wessen Theorie du stärkt.",
                "en": "🎭 MURDERER TASK 6 — THE HELPER: Actively help another person develop their theory — a person who is NOT suspicious. Show yourself as cooperative and helpful. Nobody suspects someone who actively helps the investigation. But choose wisely whose theory you strengthen."
            },
            "private": True,
            "game_effect": "murderer_cooperation_mask"
        },

        # ── PANIK-MOMENT FÜR DEN MÖRDER ──────────────────────────────────

        "murderer_panic_moment": {
            "trigger_phase": 3, "trigger_condition": "someone_gets_close_to_truth",
            "assigned_to": "murderer",
            "instruction": {
                "de": "⚠️ PANIKMOMENT — LIES DIES NUR FÜR DICH: Jemand kommt der Wahrheit sehr nahe. Du musst JETZT eine Entscheidung treffen:\n\nOPTION A: Steh auf und sage laut: 'Ich muss etwas gestehen.' Dann... gestehe etwas Harmloses aber Belastendes — einen kleinen Fehler, eine Lüge, etwas das Zeit kostet und den Verdacht von der echten Tat ablenkt.\n\nOPTION B: Fange an zu weinen oder so zu tun als ob. Emotional zusammenbrechen. Niemand kann eine weinende Person befragen ohne sich schlecht zu fühlen.\n\nOPTION C: Lenke sofort auf eine andere Person — so direkt wie möglich. 'Ich habe etwas gesehen das ich nicht sagen wollte. [Person X] war nicht da wo sie/er behauptet war.'\n\nWähle jetzt. Du hast 60 Sekunden.",
                "en": "⚠️ PANIC MOMENT — READ THIS ONLY FOR YOURSELF: Someone is getting very close to the truth. You must make a decision NOW:\n\nOPTION A: Stand up and say aloud: 'I need to confess something.' Then... confess something harmless but incriminating — a small mistake, a lie, something that costs time and deflects suspicion from the real act.\n\nOPTION B: Start crying or pretend to. Emotional breakdown. Nobody can question a crying person without feeling bad.\n\nOPTION C: Immediately redirect to another person — as directly as possible. 'I saw something I didn't want to say. [Person X] was not where they claim to have been.'\n\nChoose now. You have 60 seconds."
            },
            "private": True,
            "time_limit_seconds": 60,
            "game_effect": "panic_moment_triggered"
        },

        # ── VERBINDUNGS-AUFGABEN (Rollen die zusammen spielen müssen) ───────

        "task_lover_signal": {
            "trigger_phase": 2, "trigger_condition": "viktor_under_pressure",
            "assigned_to": "viktor_secret_lover",
            "instruction": {
                "de": "💌 DEIN PARTNER BRAUCHT DICH: Viktor steht kurz vor dem Verdacht. Wenn du ihn deckst: Ihr beide riskiert dass eure Affäre ans Licht kommt. Wenn du schweigst: Er könnte als Mörder verurteilt werden. Die App wartet auf deine Entscheidung.",
                "en": "💌 YOUR PARTNER NEEDS YOU: Viktor is about to be suspected. If you cover for him: you both risk your affair coming to light. If you stay silent: he could be convicted as murderer. The app awaits your decision."
            },
            "choice": {
                "confirm": {"de": "Ich bestätige Viktors Alibi", "en": "I confirm Viktor's alibi"},
                "deny":    {"de": "Ich schweige", "en": "I stay silent"}
            },
            "game_effect": "alibi_decision"
        },

        "task_butler_niece_confrontation": {
            "trigger_phase": 2, "trigger_condition": "both_suspects_high_suspicion",
            "assigned_to": "butler",
            "instruction": {
                "de": "🔍 DER BUTLER WEISS ES: Du hast Constanze in der Bibliothek gesehen. Jetzt ist der Moment — konfrontiere sie direkt aber leise. Geh zu ihr und flüstere: 'Ich habe dich gesehen. Wir müssen reden.' Dann entscheidest du ob du es der Gruppe sagst oder nicht.",
                "en": "🔍 THE BUTLER KNOWS: You saw Constanze in the library. Now is the moment — confront her directly but quietly. Go to her and whisper: 'I saw you. We need to talk.' Then you decide whether to tell the group or not."
            },
            "game_effect": "butler_niece_confrontation"
        },

        "task_ghost_whisper": {
            "trigger_phase": 2, "trigger_condition": "baron_dies",
            "assigned_to": "baron",
            "instruction": {
                "de": "👻 DU BIST JETZT EIN GEIST: Steh auf und setz dich an den Rand. Du spielst weiter — aber nur durch Flüstern. Wähle in den nächsten 10 Minuten drei Personen und flüstere jedem einen anderen Hinweis. Du weißt wer der Mörder ist. Führe die anderen ohne den Namen zu nennen.",
                "en": "👻 YOU ARE NOW A GHOST: Stand up and sit at the edge. You continue playing — but only through whispering. In the next 10 minutes choose three people and whisper each a different clue. You know who the murderer is. Guide the others without naming them."
            },
            "game_effect": "ghost_mode_active"
        },

        # ── ZUFALLS-MOMENTE ──────────────────────────────────────────────────

        "random_phone_buzz": {
            "trigger_phase": 2, "trigger_condition": "random_any_time",
            "assigned_to": "random",
            "instruction": {
                "de": "📱 DEIN TELEFON VIBRIERT: Schau heimlich auf dein Telefon. Die App hat dir soeben eine geheime Nachricht geschickt. Lies sie nur für dich. Reagiere dann auf eine Art die die anderen verwirrt — lächle kurz, oder runzle die Stirn, oder flüstere einer Person etwas.",
                "en": "📱 YOUR PHONE VIBRATES: Look at your phone secretly. The app just sent you a secret message. Read it only for yourself. Then react in a way that confuses the others — smile briefly, or frown, or whisper something to one person."
            },
            "secret_content_options": [
                {"de": "Der Baron hat dir vor seinem Tod etwas Wichtiges hinterlassen. Du findest es wenn du heute Nacht allein bist.", "en": "The Baron left you something important before his death. You'll find it when you're alone tonight."},
                {"de": "Jemand hat dich beobachtet. Du weißt nicht wer. Aber du wirst es herausfinden.", "en": "Someone has been watching you. You don't know who. But you will find out."},
                {"de": "Der Mörder hat heute Nachmittag einen Fehler gemacht. Du weißt es — aber du kannst es nicht beweisen. Noch nicht.", "en": "The murderer made a mistake this afternoon. You know it — but you can't prove it. Not yet."}
            ],
            "game_effect": "random_confusion_moment"
        },

        "random_knocking": {
            "trigger_phase": 2, "trigger_condition": "random_post_murder_20min",
            "assigned_to": "all",
            "broadcast": True,
            "instruction": {
                "de": "🚪 KLOPFEN AN DER TÜR: Die App kündigt an — es klopft dreimal. Alle halten inne. Der Host sagt: 'Wer ist da?' Niemand antwortet. Nach 10 Sekunden schweigen: Das Spiel geht weiter. Wer hat dabei am nervösesten reagiert?",
                "en": "🚪 KNOCK AT THE DOOR: The app announces — three knocks. Everyone stops. The host says: 'Who is there?' Nobody answers. After 10 seconds of silence: the game continues. Who reacted most nervously?"
            },
            "game_effect": "door_knock_reactions"
        },

        "random_light_flicker": {
            "trigger_phase": 2, "trigger_condition": "atmosphere_trigger",
            "assigned_to": "all",
            "broadcast": True,
            "instruction": {
                "de": "🕯️ DAS LICHT FLACKERT: Der Host macht kurz das Licht aus (2-3 Sekunden) und wieder an. In dieser Zeit: Wer bewegt sich? Wer greift nach etwas? Wer steht auf? Das Licht kommt wieder an — jeder sagt was er gesehen hat.",
                "en": "🕯️ THE LIGHT FLICKERS: The host briefly turns off the light (2-3 seconds) and back on. In this time: who moves? Who reaches for something? Who stands up? The light comes back — everyone says what they saw."
            },
            "game_effect": "darkness_reactions"
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # VERBINDUNGEN ZWISCHEN ROLLEN
    # ─────────────────────────────────────────────────────────────────────────
    "role_connections": {
        "butler_niece": {
            "roles": ["butler", "niece"],
            "connection": "Der Butler hat Constanze in der Bibliothek gesehen. Constanze weiß dass der Butler sie gesehen hat. Beide wissen voneinander — aber keiner hat es bisher gesagt.",
            "tension": "high"
        },
        "doctor_baron": {
            "roles": ["doctor", "baron"],
            "connection": "Der Arzt hat den Baron fast geblendet. Der Baron hatte vergeben — aber heute Abend die Klage eingereicht. Der Arzt weiß es. Der Baron weiß dass der Arzt es weiß.",
            "tension": "extreme"
        },
        "viktor_random": {
            "roles": ["lover", "random"],
            "connection": "Viktor hat eine geheime Affäre mit einer zufälligen anderen Person am Tisch. Beide wissen es. Niemand sonst.",
            "tension": "secret"
        },
        "stranger_murderer": {
            "roles": ["stranger", "murderer"],
            "connection": "Der Fremde beschattet den Mörder — weiß es aber nicht. Er hat eine Akte mit Geheimnissen die nahe am Tatmotiv liegen.",
            "tension": "dramatic_irony"
        },
        "cook_murderer": {
            "roles": ["cook", "murderer"],
            "connection": "Der Mörder hat die Köchin beauftragt etwas in das Essen des Barons zu geben. Die Köchin kennt den Namen des Auftraggebers — aber schweigt.",
            "tension": "critical"
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # ORGANISCHE EREIGNISKETTEN
    # ─────────────────────────────────────────────────────────────────────────
    "event_chains": [
        {
            "id": "chain_two_talking",
            "trigger": "two_players_private_3min",
            "message_to_third": {
                "de": "👁️ Du hast bemerkt: {player_a} und {player_b} flüstern seit Minuten. Du kannst alle darauf aufmerksam machen — oder sie weiter beobachten.",
                "en": "👁️ You noticed: {player_a} and {player_b} have been whispering for minutes. You can alert everyone — or keep observing."
            }
        },
        {
            "id": "chain_wine_drinker",
            "trigger": "someone_drinks_more_than_others",
            "message_to_observer": {
                "de": "🍷 {player} trinkt ungewöhnlich viel — und redet dabei besonders viel. Wein löst Zungen und Gewissen. Rede mit ihr/ihm.",
                "en": "🍷 {player} is drinking unusually much — and talking particularly much while doing so. Wine loosens tongues and consciences. Talk to them."
            }
        },
        {
            "id": "chain_refuse_drink",
            "trigger": "player_refuses_group_drink",
            "message_to_all": {
                "de": "👀 Hat das jemand gesehen? {player} hat beim gemeinsamen Trinken nicht mitgemacht.",
                "en": "👀 Did anyone see that? {player} didn't join in the group drink."
            }
        },
        {
            "id": "chain_early_accusation",
            "trigger": "someone_accuses_directly",
            "message_to_murderer": {
                "de": "⚠️ {player} verdächtigt dich öffentlich. Handle jetzt — du hast 2 Minuten bevor der Druck zu groß wird.",
                "en": "⚠️ {player} is publicly suspecting you. Act now — you have 2 minutes before the pressure becomes too great."
            }
        },
        {
            "id": "chain_ghost_appears",
            "trigger": "baron_death_announced",
            "message_to_baron": {
                "de": "👻 Du bist jetzt tot. Steh auf. Setz dich an den Rand. Warte — dann beginne zu flüstern. Du weißt wer der Mörder ist. Führe die anderen.",
                "en": "👻 You are now dead. Stand up. Sit at the edge. Wait — then begin to whisper. You know who the murderer is. Guide the others."
            }
        }
    ],

    # ─────────────────────────────────────────────────────────────────────────
    # ATMOSPHÄREN-NACHRICHTEN (organisch, kein fester Zeitplan)
    # ─────────────────────────────────────────────────────────────────────────
    "atmosphere_messages": [
        {"trigger": "game_start_5min",     "text": {"de": "🌧️ Draußen beginnt es zu regnen. Niemand kann jetzt gehen.", "en": "🌧️ Outside it begins to rain. Nobody can leave now."}},
        {"trigger": "game_start_15min",    "text": {"de": "🕙 Die Uhr schlägt 22 Uhr. Der Baron klopft mit seinem Glas: 'Ich habe eine Ankündigung.'", "en": "🕙 The clock strikes 10pm. The Baron taps his glass: 'I have an announcement.'"}},
        {"trigger": "murder_announced",    "text": {"de": "💀 DER SCHREI. Aus der Bibliothek. Baron Aldric von Dunkelbach ist tot.", "en": "💀 THE SCREAM. From the library. Baron Aldric von Dunkelbach is dead."}},
        {"trigger": "investigation_10min","text": {"de": "🍴 Ein Geruch aus der Küche. Süßlich. Fast medizinisch.", "en": "🍴 A smell from the kitchen. Sweet. Almost medicinal."}},
        {"trigger": "investigation_20min","text": {"de": "📜 Ein Anwalt wartet draußen. Jemand hat ihn mitgebracht. Warum jetzt?", "en": "📜 A lawyer waits outside. Someone brought him. Why now?"}},
        {"trigger": "tension_high",        "text": {"de": "⚡ Die Wahrheit ist nahe. Wer schweigt verliert. Wer lügt wird entlarvt.", "en": "⚡ The truth is close. Those who stay silent lose. Those who lie will be exposed."}}
    ],

    # ─────────────────────────────────────────────────────────────────────────
    # SPIELENDE (ohne erzwungene Abstimmung)
    # ─────────────────────────────────────────────────────────────────────────
    "endings": {
        "murderer_caught": {
            "condition": "majority_accuses_murderer_correctly",
            "title": {"de": "Gerechtigkeit", "en": "Justice"},
            "text": {"de": "Der Mörder wurde überführt. Nicht durch eine Abstimmung — sondern durch Beweise, Beobachtung, und die Wahrheit die immer ans Licht kommt.\n\nGewonnen: Alle die für den richtigen Mörder sprachen.", "en": "The murderer was convicted. Not through a vote — but through evidence, observation, and the truth that always comes to light.\n\nWon: Everyone who spoke for the right murderer."}
        },
        "murderer_escapes": {
            "condition": "wrong_person_convicted",
            "title": {"de": "Der Mörder lacht", "en": "The Murderer Laughs"},
            "text": {"de": "Ein Unschuldiger wurde beschuldigt. Der wahre Mörder sitzt unter euch und lacht. {murderer_name} hat gewonnen.", "en": "An innocent was accused. The real murderer sits among you and laughs. {murderer_name} has won."}
        },
        "shadow_wins": {
            "condition": "shadow_steals_will",
            "title": {"de": "Das Testament ist weg", "en": "The Will is Gone"},
            "text": {"de": "Während alle ermittelten — verschwand das Testament. Die Schattenfigur hat gewonnen. Wer erbt was? Niemand weiß es.", "en": "While everyone investigated — the will disappeared. The Shadow figure has won. Who inherits what? Nobody knows."}
        },
        "perfect_solve": {
            "condition": "witness_and_doctor_both_correct",
            "title": {"de": "Vollendete Lösung", "en": "Perfect Solve"},
            "text": {"de": "Die Schriftstellerin und der Arzt haben gemeinsam das Unmögliche geschafft. Das ist selten. Das ist brillant.", "en": "The writer and the doctor together accomplished the impossible. This is rare. This is brilliant."}
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # HINWEISE
    # ─────────────────────────────────────────────────────────────────────────
    "clues": {
        "key_cellar": {
            "name": {"de": "Schlüssel W-7", "en": "Key W-7"},
            "text": {"de": "Ein alter Messingsschlüssel. Auf der Rückseite: 'W-7'. Der Weinkeller. Warum hätte jemand diesen Schlüssel heute Nacht gebraucht?", "en": "An old brass key. On the back: 'W-7'. The wine cellar. Why would someone have needed this key tonight?"}
        },
        "household_ledger": {
            "name": {"de": "Das Haushaltsbuch", "en": "The Household Ledger"},
            "text": {"de": "Seite 47: Korrekturen mit anderer Tinte. 8.400 Mark fehlen über drei Jahre.", "en": "Page 47: corrections in different ink. 8,400 marks missing over three years."}
        },
        "sealed_letter": {
            "name": {"de": "Der versiegelte Brief", "en": "The Sealed Letter"},
            "text": {"de": "Inhalt wenn geöffnet: 'Constanze — Die Wahrheit über deine Mutter liegt hinter Schiller. — Aldric'", "en": "Contents when opened: 'Constanze — The truth about your mother is behind Schiller. — Aldric'"}
        },
        "cause_of_death": {
            "name": {"de": "Todesursache", "en": "Cause of Death"},
            "text": {"de": "Herzversagen — aber erweiterte Pupillen. Nicht typisch für natürlichen Tod. Digitalis-Überdosis.", "en": "Heart failure — but dilated pupils. Not typical for natural death. Digitalis overdose."}
        },
        "kitchen_substance": {
            "name": {"de": "Das Päckchen aus der Küche", "en": "The Kitchen Package"},
            "text": {"de": "Weißes Pulver. Geruchlos. Die Köchin sagt: 'Herzstärkendes.' Der Arzt weiß: Das ist Digitalis.", "en": "White powder. Odourless. The cook says: 'Heart tonic.' The doctor knows: this is digitalis."}
        },
        "payment_receipt": {
            "name": {"de": "Quittung: 200 Mark", "en": "Receipt: 200 Marks"},
            "text": {"de": "Kein Name. Datum: Heute. Gasthausschrift aus München.", "en": "No name. Date: today. Inn handwriting from Munich."}
        },
        "medical_bag": {
            "name": {"de": "Die Arzttasche", "en": "The Doctor's Bag"},
            "text": {"de": "Eine Spritze fehlt. Die Digitalis-Schachtel ist offen — zwei Tabletten fehlen.", "en": "One syringe missing. The digitalis box is open — two tablets missing."}
        },
        "barons_evidence": {
            "name": {"de": "Die Beweise des Barons", "en": "The Baron's Evidence"},
            "text": {"de": "In der Bibliothek unter der dritten Bodendiele: Ein Umschlag. Darin Dokumente die auf den Mörder zeigen.", "en": "In the library under the third floorboard: an envelope. Inside documents pointing to the murderer."}
        },
        "new_will_location": {
            "name": {"de": "Das neue Testament", "en": "The New Will"},
            "text": {"de": "Hinter den Rechtsbüchern im dritten Regal. Noch nicht unterschrieben.", "en": "Behind the law books on the third shelf. Not yet signed."}
        },
        "surveillance_file": {
            "name": {"de": "Die Observationsakte", "en": "The Surveillance File"},
            "text": {"de": "12 Seiten über eine Person am Tisch. Zeiten, Orte, ein immer wiederkehrender Name.", "en": "12 pages on one person at the table. Times, places, one recurring name."}
        },
        "blackmail_files": {
            "name": {"de": "Die Erpressungsakten", "en": "The Blackmail Files"},
            "text": {"de": "Drei Dossiers. Drei Personen. Drei Geheimnisse die zusammen auf den Mörder zeigen.", "en": "Three dossiers. Three people. Three secrets that together point to the murderer."}
        }
    }
}
