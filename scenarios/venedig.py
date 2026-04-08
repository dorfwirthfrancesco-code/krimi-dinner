"""
KRIMI DINNER — SZENARIO 02
"Die Maske des Verräters"
Venedig, 1895 — Palazzo Marzano — Ein Maskenball

ERWEITERTE VERSION v2.0
- 11 Rollen
- 52 physische Aufgaben (davon 8 Mörder-Tasks, 10 Trink-Tasks, 8 Zufalls-Momente)
- 35 Hinweise in 8 Ketten
- 14 Rollenverbindungen
- 5 Spielenden
- Masken als zentrale Spielmechanik
"""

SCENARIO = {
    "id": "venedig",
    "title": "Die Maske des Verräters",
    "title_en": "The Mask of the Traitor",
    "min_players": 4,
    "max_players": 11,
    "price": "4.99",
    "description": {
        "de": "Venedig, 1895. Palazzo Marzano. Ein Maskenball der in Blut endet. Graf Marzano ist tot — seine Gäste tragen noch immer Masken. Niemand hat ein sicheres Alibi. Zwei Verbrechen, ein Abend, elf Verdächtige.",
        "en": "Venice, 1895. Palazzo Marzano. A masquerade ball that ends in blood. Count Marzano is dead — his guests still wear their masks. Nobody has a certain alibi. Two crimes, one evening, eleven suspects.",
    },
    "atmosphere": "Kerzenlicht. Masken. Gondeln auf dem Canal Grande. Jeder lügt. Jeder hat einen Grund.",
    "host_guide": {
        "before_game": {
            "de": [
                "MASKEN: Für jeden Spieler eine Maske (Papier reicht). Jede in anderer Farbe/Symbol. Rückseite beschriften mit Rollenfarbe. WICHTIG: Mache zwei Extra-Masken in dunklen Farben — die werden später relevant.",
                "DAS GEMÄLDE: Leerer Bilderrahmen oder Zettel 'La Serenissima — Tizian 1573' irgendwo sichtbar aufstellen.",
                "TATORT: Einen Zettel 'ARBEITSZIMMER — TATORT' irgendwo im Raum oder Flur platzieren.",
                "GONDOLIER-NOTIZ: Im Badezimmer verstecken: 'Ich sah um 23:15 eine Person mit DUNKLER Maske und einer goldenen rechteckigen Schnalle an den Schuhen den Palazzo verlassen. — Marco il Gondoliere'",
                "MACHIAVELLI-BUCH: Ein Buch irgendwo hinstellen. Darin Zettel: 'Wer dieses Buch öffnet — prüfe den Boden. — E.M.'",
                "BRIEF FÜR ERBIN: Einen versiegelten Umschlag vorbereiten mit Text: 'Viola — du bist meine Tochter. Nicht meine Nichte. Das Testament liegt im Arbeitszimmer, dritte Schublade. — Emilio'",
                "DREI VISITENKARTEN: Für die Agentin drei Karten mit je einem anderen Namen vorbereiten.",
                "DER GRAF IST VON ANFANG AN TOT. Sein Spieler setzt sich sofort an den Rand und flüstert nur.",
                "CHAMPAGNER oder Sekt bereitstellen — wird Spielmechanik.",
            ]
        },
        "during_game": {
            "de": [
                "Als Host bist du der Zeremonienmeister — du kündest Ereignisse an aber spielst keine Rolle.",
                "Wenn die App 'Dunkelheit' anzeigt: Licht aus für exakt 5 Sekunden.",
                "Wenn die App 'Gondel klopft' anzeigt: Dreimal ans Fenster oder die Tür klopfen.",
                "Die Masken bleiben solange auf bis der Inspektor 'Masken ab' ausruft.",
            ]
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # ROLLEN
    # ─────────────────────────────────────────────────────────────────────────
    "roles": {

        "count": {
            "name": {"de": "Graf Emilio Marzano", "en": "Count Emilio Marzano",
                     "fr": "Comte Emilio Marzano", "it": "Conte Emilio Marzano",
                     "es": "Conde Emilio Marzano", "pt": "Conde Emilio Marzano"},
            "min_players": 4,
            "can_be_murderer": False,
            "ghost_mode": True,
            "intro": {
                "de": "Ich war Graf Emilio Marzano. Ich habe diesen Ball gegeben um eine Wahrheit ans Licht zu bringen. Jemand hat das verhindert. Aber ich bin noch hier. Ich flüstere. Ich führe euch.",
                "en": "I was Count Emilio Marzano. I gave this ball to bring a truth to light. Someone prevented that. But I am still here. I whisper. I guide you.",
            },
            "appearance": {
                "de": "Keine Maske — du brauchst keine mehr. Sitzt abseits. Schwarzer Schal. Spricht nie laut.",
                "en": "No mask — you no longer need one. Sits apart. Black scarf. Never speaks loudly.",
            },
            "secret": {
                "de": "Du weißt wer dich getötet hat — die App teilt dir den Namen mit. Du weißt auch: Es gibt zwei Verbrechen diese Nacht. Der Mörder und der Dieb sind nicht zwingend dieselbe Person.",
                "en": "You know who killed you — the app tells you the name. You also know: there are two crimes tonight. The murderer and the thief are not necessarily the same person.",
            },
            "ability": {
                "name": {"de": "Der Geist", "en": "The Ghost"},
                "description": {
                    "de": "Du flüsterst. Nur einer Person gleichzeitig, nie laut. Einmal pro 15 Minuten darfst du einer Person einen wahren Hinweis geben. Du darfst nicken oder den Kopf schütteln bei Ja/Nein-Fragen. Du kennst den Mörder — nenne ihn nie direkt. Führe durch Andeutungen.",
                    "en": "You whisper. Only to one person at a time, never aloud. Once every 15 minutes you may give one person a true clue. You may nod or shake your head at yes/no questions. You know the murderer — never name them directly. Guide through hints.",
                }
            },
            "win_condition": {
                "de": "Der Mörder wird gefasst. Du gewinnst auch als Geist — Ehrentitel: Der Gerechte Graf.",
                "en": "The murderer is caught. You win even as a ghost — honorary title: The Just Count.",
            },
            "clues_i_hold": ["machiavelli_evidence", "palazzo_key", "second_crime_note"],
            "starting_knowledge": {
                "de": "Die App hat dir den Namen des Mörders mitgeteilt. Du weißt auch: Das Gemälde wurde von jemand anderem gestohlen als der der dich tötete. Zwei Täter, eine Nacht.",
                "en": "The app has told you the murderer's name. You also know: the painting was stolen by someone other than the one who killed you. Two culprits, one night.",
            }
        },

        "contessa": {
            "name": {"de": "Contessa Isabella Marzano", "en": "Contessa Isabella Marzano",
                     "fr": "Comtesse Isabella Marzano", "it": "Contessa Isabella Marzano",
                     "es": "Condesa Isabella Marzano", "pt": "Condessa Isabella Marzano"},
            "min_players": 4,
            "can_be_murderer": True,
            "intro": {
                "de": "Isabella Marzano, geborene Falcone. Ich kannte Emilio. Zu gut. Ich weiß wessen Blut an wessen Händen klebt. Ich warte noch mit dem Reden.",
                "en": "Isabella Marzano, born Falcone. I knew Emilio. Too well. I know whose blood is on whose hands. I'm waiting before speaking.",
            },
            "appearance": {
                "de": "Schwarz gekleidet — schon vor dem Tod. Goldene Brosche die sie ständig berührt. Ihre Augen folgen allen. Weint nicht.",
                "en": "Dressed in black — before the death. Golden brooch she constantly touches. Eyes follow everyone. Doesn't cry.",
            },
            "secret": {
                "de": "Ich liebte Emilio nicht mehr. Seit Jahren nicht. Affäre mit jemandem in diesem Raum. Emilio wusste es — und drohte mit Scheidung und öffentlichem Skandal. Ich hatte Motiv. Ich hatte Mittel. Ich hatte Gelegenheit. Ob ich es tat — entscheidet die App.",
                "en": "I no longer loved Emilio. Haven't for years. Affair with someone in this room. Emilio knew — and threatened divorce and public scandal. I had motive. I had means. I had opportunity. Whether I did it — the app decides.",
            },
            "ability": {
                "name": {"de": "Die Maske der Trauer", "en": "The Mask of Grief"},
                "description": {
                    "de": "Einmal kannst du eine dramatische Szene spielen — Tränen, Wut oder Zusammenbruch. Für 2 Minuten darf niemand dich befragen. Wer dein Schauspiel laut durchschaut erhält einen Bonus-Hinweis. Wer schweigt — zweifelt weiter.",
                    "en": "Once you may play a dramatic scene — tears, anger or breakdown. For 2 minutes nobody may question you. Whoever loudly sees through your performance receives a bonus clue. Whoever stays silent — continues to doubt.",
                }
            },
            "win_condition": {
                "de": "Überlebe ohne dass deine Affäre öffentlich wird. Wenn der Mörder gefasst wird und deine Affäre geheim bleibt — gewinnst du. Wenn deine Affäre enthüllt wird — verlierst du.",
                "en": "Survive without your affair becoming public. If the murderer is caught and your affair stays secret — you win. If your affair is revealed — you lose.",
            },
            "murderer_motive_if_assigned": {
                "de": "Isabella vergiftete den Wein des Grafen mit Arsen — gestohlen aus dem Labor der Ärztin während des Balls. Ein langsamer Tod. Sie stand dabei und sah zu. Dann kehrte sie zum Ball zurück.",
                "en": "Isabella poisoned the Count's wine with arsenic — stolen from the doctor's laboratory during the ball. A slow death. She stood and watched. Then returned to the ball.",
            },
            "clues_i_hold": ["affair_letters", "arsenic_trace"],
            "starting_knowledge": {
                "de": "Deine Affäre ist mit einer bestimmten Person in diesem Raum — die App nennt dir ihren Rollennamen. Ihr beide wisst es. Keiner darf es sagen. Aber: Wenn du in Not bist kannst du die Affäre nutzen um ein Alibi zu bekommen.",
                "en": "Your affair is with a specific person in this room — the app tells you their role name. You both know. Nobody may say it. But: if in need you can use the affair to get an alibi.",
            },
            "connection": {"with": "spy", "type": "affair_secret"}
        },

        "art_dealer": {
            "name": {"de": "Signor Benedetto Crane, Kunsthändler", "en": "Signor Benedetto Crane, Art Dealer",
                     "fr": "Signor Benedetto Crane, Marchand d'Art", "it": "Signor Benedetto Crane, Mercante d'Arte",
                     "es": "Signor Benedetto Crane, Comerciante de Arte", "pt": "Signor Benedetto Crane, Comerciante de Arte"},
            "min_players": 4,
            "can_be_murderer": True,
            "intro": {
                "de": "Benedetto Crane. Kunsthändler. Ich kam wegen 'La Serenissima'. Das Gemälde ist weg. Mein Geschäftspartner ist tot. Das ist... sehr ungünstig.",
                "en": "Benedetto Crane. Art dealer. I came for 'La Serenissima'. The painting is gone. My business partner is dead. This is... very unfortunate.",
            },
            "appearance": {
                "de": "Elegante Maske, goldener Rand. Hat immer eine Ledertasche. Schaut zu oft dorthin wo das Gemälde hing. Trinkt schnell.",
                "en": "Elegant mask, golden rim. Always has a leather bag. Looks too often toward where the painting hung. Drinks quickly.",
            },
            "secret": {
                "de": "Das Gemälde an der Wand war eine Fälschung — ich habe das Original vor drei Monaten gegen eine Kopie ausgetauscht, mit Wissen des Grafen. Teil eines komplizierten Betrugs. Jetzt will der Graf mehr Geld. Wollte. Hatte ich genug Grund ihn zu töten? Vielleicht. Das Original liegt noch im Palazzo — irgendwo.",
                "en": "The painting on the wall was a forgery — I exchanged the original for a copy three months ago, with the Count's knowledge. Part of a complicated fraud. Now the Count wants more money. Wanted. Did I have enough reason to kill him? Perhaps. The original is still in the palazzo — somewhere.",
            },
            "ability": {
                "name": {"de": "Der Experte", "en": "The Expert"},
                "description": {
                    "de": "Einmal kannst du eine Aussage oder einen Hinweis als 'authentisch' oder 'Fälschung' deklarieren. Deine Einschätzung gilt offiziell. Du kannst lügen. Nur du weißt ob du lügst.",
                    "en": "Once you may declare a statement or clue as 'authentic' or 'forgery'. Your assessment counts officially. You can lie. Only you know if you're lying.",
                }
            },
            "win_condition": {
                "de": "Überlebe. Der Betrug darf nicht ans Licht kommen. Wenn der Mörder gefasst wird und der Betrug geheim bleibt — gewinnst du.",
                "en": "Survive. The fraud must not come to light. If the murderer is caught and the fraud stays secret — you win.",
            },
            "murderer_motive_if_assigned": {
                "de": "Der Graf drohte alles aufzudecken. Crane vergiftete seinen Wein im Arbeitszimmer — dann stahl er die Fälschung vom Haken um eine falsche Spur zu legen.",
                "en": "The Count threatened to expose everything. Crane poisoned his wine in the study — then stole the forgery from the hook to create a false trail.",
            },
            "clues_i_hold": ["painting_receipt", "forgery_tools", "florence_warehouse"],
            "starting_knowledge": {
                "de": "Das Gemälde an der Wand war eine Fälschung. Das Original liegt irgendwo im Palazzo — du weißt nicht genau wo. Die Schattenfigur hat es. Das weißt du noch nicht.",
                "en": "The painting on the wall was a forgery. The original is somewhere in the palazzo — you don't know exactly where. The Shadow figure has it. You don't know that yet.",
            },
            "connection": {"with": "shadow", "type": "painting_unknowing"}
        },

        "gondolier": {
            "name": {"de": "Marco, der Gondoliere", "en": "Marco, the Gondolier",
                     "fr": "Marco, le Gondolier", "it": "Marco, il Gondoliere",
                     "es": "Marco, el Gondolero", "pt": "Marco, o Gondoleiro"},
            "min_players": 4,
            "can_be_murderer": False,
            "intro": {
                "de": "Marco Ricci. Ich bringe und hole die Gäste. Vom Wasser aus sieht man alles. Heute Nacht habe ich etwas gesehen das ich nicht einordnen kann.",
                "en": "Marco Ricci. I bring and collect guests. From the water one sees everything. Tonight I saw something I cannot explain.",
            },
            "appearance": {
                "de": "Keine Maske — er ist kein Gast. Raue Hände. Trinkt nur Wasser. Schaut ständig zur Tür.",
                "en": "No mask — he's not a guest. Rough hands. Drinks only water. Constantly looks toward the door.",
            },
            "secret": {
                "de": "Ich habe um 23:15 jemanden aus dem Palazzo kommen sehen — maskiert, eilig, mit einem Paket. Ich habe die Gondel bereitgestellt OHNE gefragt zu haben wer es bestellt hat. Das ist mein Fehler. Jetzt weiß ich nicht ob ich mitschuldig bin.",
                "en": "At 11:15 I saw someone leave the palazzo — masked, hurrying, with a package. I had the gondola ready WITHOUT asking who ordered it. That is my mistake. Now I don't know if I'm an accessory.",
            },
            "ability": {
                "name": {"de": "Der Wasserzeuge", "en": "The Water Witness"},
                "description": {
                    "de": "Du hast zwei Hinweise: Die Maske und die Schuhe. Du kannst beide separat enthüllen. Enthüllst du beide: Du bist der wichtigste Zeuge — aber auch das Ziel des Mörders. Er/sie wird versuchen dich zum Schweigen zu bringen.",
                    "en": "You have two clues: the mask and the shoes. You can reveal both separately. If you reveal both: you become the most important witness — but also the murderer's target. They will try to silence you.",
                }
            },
            "win_condition": {
                "de": "Du gewinnst wenn der Mörder gefasst wird UND du bis zum Ende geredet hast — nicht eingeschüchtert wurdest.",
                "en": "You win if the murderer is caught AND you spoke until the end — were not intimidated.",
            },
            "clues_i_hold": ["mask_color", "shoe_buckle"],
            "starting_knowledge": {
                "de": "Die App sagt dir welche Maskenfarbe die Person trug. Es ist NICHT die Farbe des echten Mörders — es ist eine Ablenkung. Weil Masken getauscht wurden. Das weißt du noch nicht.",
                "en": "The app tells you which mask color the person wore. It is NOT the real murderer's color — it is a distraction. Because masks were swapped. You don't know that yet.",
            },
            "connection": {"with": "spy", "type": "unknowing_transport"}
        },

        "cardinal": {
            "name": {"de": "Kardinal Sebastiano Ferretti", "en": "Cardinal Sebastiano Ferretti",
                     "fr": "Cardinal Sebastiano Ferretti", "it": "Cardinale Sebastiano Ferretti",
                     "es": "Cardenal Sebastiano Ferretti", "pt": "Cardeal Sebastiano Ferretti"},
            "min_players": 5,
            "can_be_murderer": True,
            "intro": {
                "de": "Kardinal Ferretti. Ich war nicht eingeladen. Trotzdem da. Der Graf und ich hatten ein Arrangement das mit seinem Tod endet — oder vielleicht auch nicht.",
                "en": "Cardinal Ferretti. I was not invited. Here anyway. The Count and I had an arrangement that ends with his death — or perhaps not.",
            },
            "appearance": {
                "de": "Rote Maske — die einzige rote im Raum. Rosenkranz in der Hand. Lächelt zu viel. Kurze Sätze.",
                "en": "Red mask — the only red one in the room. Rosary in hand. Smiles too much. Short sentences.",
            },
            "secret": {
                "de": "Der Graf erpresste mich seit 18 Jahren wegen einer Sünde die ich vor meiner Kardinalswürde beging. Er wollte jetzt dreimal so viel. Ich sagte nein. Heute Nacht war meine letzte Chance. Ich beauftragte jemanden — oder ich tat es selbst. Die App entscheidet.",
                "en": "The Count blackmailed me for 18 years over a sin I committed before my cardinalship. He now wanted three times as much. I said no. Tonight was my last chance. I hired someone — or I did it myself. The app decides.",
            },
            "ability": {
                "name": {"de": "Das Beichtgeheimnis", "en": "The Confessional Secret"},
                "description": {
                    "de": "Du kannst einer Person eine 'private Beichte' anbieten. Was du erfährst darfst du NIE direkt weitersagen — aber du kannst es indirekt nutzen. Wenn du das Beichtgeheimnis brichst verlierst du sofort.",
                    "en": "You may offer one person a 'private confession'. What you learn you may NEVER directly reveal — but you can use it indirectly. If you break the confessional secret you lose immediately.",
                }
            },
            "win_condition": {
                "de": "Überlebe. Deine Sünde und die Erpressungszahlungen dürfen nicht ans Licht kommen.",
                "en": "Survive. Your sin and the blackmail payments must not come to light.",
            },
            "murderer_motive_if_assigned": {
                "de": "Der Kardinal vergiftete den Wein mit einer Substanz aus Vatikaner Klostergärten. Er beichtete danach — sich selbst.",
                "en": "The Cardinal poisoned the wine with a substance from Vatican monastery gardens. He confessed afterwards — to himself.",
            },
            "clues_i_hold": ["blackmail_payments", "vaticanum_substance"],
            "starting_knowledge": {
                "de": "Du hast die Schattenfigur beauftragt das Gemälde zu stehlen — als Ablenkung. Du weißt wer die Schattenfigur ist. Sie weiß dass du hinter dem Auftrag steckst. Das ist eure gemeinsame Verbindung.",
                "en": "You hired the Shadow figure to steal the painting — as a distraction. You know who the Shadow figure is. They know you're behind the commission. That is your shared connection.",
            },
            "connection": {"with": "shadow", "type": "painting_commissioner"}
        },

        "spy": {
            "name": {"de": "Die Agentin", "en": "The Agent",
                     "fr": "L'Agente", "it": "L'Agente", "es": "La Agente", "pt": "A Agente"},
            "min_players": 5,
            "can_be_murderer": True,
            "intro": {
                "de": "Mein Name ist nicht wichtig. Ich habe drei Visitenkarten mit drei Namen. Ich antworte auf alle drei. Warum ich hier bin — das sage ich wenn ich es für richtig halte.",
                "en": "My name doesn't matter. I have three business cards with three names. I respond to all three. Why I'm here — I'll say when I see fit.",
            },
            "appearance": {
                "de": "Drei Visitenkarten. Keine bevorzugte Seite am Tisch. Wechselt Position wenn möglich. Antwortet auf drei verschiedene Namen.",
                "en": "Three business cards. No preferred side at the table. Changes position when possible. Responds to three different names.",
            },
            "secret": {
                "de": "Agentin einer ausländischen Macht. Ich kam um Dokumente zu stehlen — nicht um zu töten. Aber der Graf fand mich in seinem Arbeitszimmer. Was dann passierte — hängt von meiner Rolle ab. Ich hatte auch eine Affäre mit der Contessa. Das ist kompliziert.",
                "en": "Agent of a foreign power. I came to steal documents — not to kill. But the Count found me in his study. What happened then — depends on my role. I also had an affair with the Contessa. That's complicated.",
            },
            "ability": {
                "name": {"de": "Doppelidentität", "en": "Double Identity"},
                "description": {
                    "de": "Du hast drei Visitenkarten mit verschiedenen Namen. Einmal pro Phase kannst du offiziell eine andere Identität annehmen. Alle Aussagen die du als diese Identität machst gelten als von dieser Person gesagt.",
                    "en": "You have three business cards with different names. Once per phase you can officially adopt another identity. All statements you make as that identity count as said by that person.",
                }
            },
            "win_condition": {
                "de": "Überlebe ohne als Agentin entlarvt zu werden. Wenn deine wahre Identität enthüllt wird — verlierst du sofort.",
                "en": "Survive without being exposed as an agent. If your true identity is revealed — you lose immediately.",
            },
            "murderer_motive_if_assigned": {
                "de": "Der Graf sah mein Gesicht. Ich musste handeln. Ich tötete ihn mit dem Briefbeschwerer auf seinem Schreibtisch — dann arrangierte ich es als Vergiftung.",
                "en": "The Count saw my face. I had to act. I killed him with the paperweight on his desk — then arranged it to look like poisoning.",
            },
            "clues_i_hold": ["stolen_documents", "paperweight_evidence"],
            "starting_knowledge": {
                "de": "Du warst im Arbeitszimmer. Du hast Dokumente gestohlen. Du warst dort als der Graf kam. Was danach passierte — die App sagt es dir. Du hast auch eine Affäre mit der Contessa. Ihr Alibi für einander könnte euch beide retten oder beide ruinieren.",
                "en": "You were in the study. You stole documents. You were there when the Count came. What happened then — the app tells you. You also have an affair with the Contessa. Your mutual alibi could save or ruin you both.",
            },
            "connection_multiple": [
                {"with": "contessa", "type": "affair_secret"},
                {"with": "gondolier", "type": "unknowing_transport"},
                {"with": "investigator", "type": "hunter_hunted"}
            ]
        },

        "singer": {
            "name": {"de": "La Cantante — Serafina Luce", "en": "La Cantante — Serafina Luce",
                     "fr": "La Cantatrice — Serafina Luce", "it": "La Cantante — Serafina Luce",
                     "es": "La Cantante — Serafina Luce", "pt": "A Cantora — Serafina Luce"},
            "min_players": 6,
            "can_be_murderer": True,
            "intro": {
                "de": "Serafina Luce. Die Stimme Venedigs. Ich sang bis 23:15 Uhr. Dann machte ich eine Pause. Was in dieser Pause passierte... das erkläre ich vielleicht.",
                "en": "Serafina Luce. The Voice of Venice. I sang until 11:15pm. Then I took a break. What happened in that break... I might explain.",
            },
            "appearance": {
                "de": "Goldene Maske. Champagner statt Wein. Notizbuch mit Texten. Summt manchmal ohne es zu merken.",
                "en": "Golden mask. Champagne instead of wine. Notebook with lyrics. Sometimes hums without noticing.",
            },
            "secret": {
                "de": "In meiner Pause traf ich den Kardinal im Korridor. Wir sprachen kurz. Er gab mir etwas — einen kleinen Zettel. Ich öffnete ihn nicht. Ich trage ihn noch immer bei mir. Der Kardinal weiß was drauf steht. Ich nicht.",
                "en": "During my break I met the Cardinal in the corridor. We spoke briefly. He gave me something — a small note. I didn't open it. I still carry it. The Cardinal knows what's on it. I don't.",
            },
            "ability": {
                "name": {"de": "Die Aufführung", "en": "The Performance"},
                "description": {
                    "de": "Einmal kannst du Stille verlangen und einen kurzen Text singen oder rezitieren. Danach stellst du GENAU EINE Frage an GENAU EINE Person. Diese Person muss mit einem vollständigen Satz antworten — nicht nur Ja/Nein.",
                    "en": "Once you may demand silence and sing or recite a short text. Afterwards you ask EXACTLY ONE question to EXACTLY ONE person. That person must answer with a complete sentence — not just yes/no.",
                }
            },
            "win_condition": {
                "de": "Du gewinnst wenn du bis zum Ende singst — also nicht des Mordes beschuldigt wirst. Den ungeöffneten Zettel musst du irgendwann öffnen — aber du entscheidest wann.",
                "en": "You win if you keep singing until the end — that is, not accused of murder. The unopened note must be opened at some point — but you decide when.",
            },
            "murderer_motive_if_assigned": {
                "de": "Der Graf kannte meine Vergangenheit — eine andere Identität, eine andere Stadt, ein anderes Leben. In meiner Pause tötete ich ihn. Dann kehrte ich zur Bühne zurück und sang die schönste Arie meines Lebens.",
                "en": "The Count knew my past — another identity, another city, another life. During my break I killed him. Then returned to the stage and sang the most beautiful aria of my life.",
            },
            "clues_i_hold": ["cardinals_note_unread", "sheet_music_timing"],
            "starting_knowledge": {
                "de": "Du hast einen ungeöffneten Zettel vom Kardinal. Du weißt nicht was drauf steht. Der Kardinal wird dich bitten ihn NICHT zu öffnen. Das sollte dich misstrauisch machen.",
                "en": "You have an unopened note from the Cardinal. You don't know what's on it. The Cardinal will ask you NOT to open it. That should make you suspicious.",
            },
            "connection": {"with": "cardinal", "type": "secret_note_carrier"}
        },

        "doctor": {
            "name": {"de": "Dr. Lucrezia Neri", "en": "Dr. Lucrezia Neri",
                     "fr": "Dr. Lucrezia Neri", "it": "Dott.ssa Lucrezia Neri",
                     "es": "Dra. Lucrezia Neri", "pt": "Dra. Lucrezia Neri"},
            "min_players": 6,
            "can_be_murderer": True,
            "intro": {
                "de": "Dr. Lucrezia Neri. Ärztin — was 1895 für eine Frau schon etwas bedeutet. Ich habe den Grafen untersucht. Ich sage was ich gefunden habe. Wenn ich es für richtig halte.",
                "en": "Dr. Lucrezia Neri. Doctor — which in 1895 means something for a woman. I examined the Count. I will say what I found. When I see fit.",
            },
            "appearance": {
                "de": "Silberne Maske. Schwarze Arzttasche. Spricht präzise. Keine Geduld für Hysterie.",
                "en": "Silver mask. Black doctor's bag. Speaks precisely. No patience for hysteria.",
            },
            "secret": {
                "de": "Ich erkannte das Tatmittel sofort. Es kam aus MEINER Giftsammlung — zwölf Fläschchen, eines ist leer. Jemand hat es gestohlen. Oder ich habe es selbst benutzt. Ich weiß auch: Die Contessa war heute Nachmittag in meinem Labor. Sie sagte es war wegen Medikamenten für die Migräne.",
                "en": "I recognized the murder weapon immediately. It came from MY poison collection — twelve vials, one is empty. Someone stole it. Or I used it myself. I also know: the Contessa was in my laboratory this afternoon. She said it was for migraine medication.",
            },
            "ability": {
                "name": {"de": "Die Autopsie", "en": "The Autopsy"},
                "description": {
                    "de": "Du allein kannst Todesursache und Tatmittel offiziell bestimmen. Du kannst lügen. Wenn du die Wahrheit sagst und der Mörder gefasst wird: Ehrentitel Meisterdetektivin. Wenn du lügst und der Mörder entkömmt: Du verlierst.",
                    "en": "Only you can officially determine cause of death and murder weapon. You can lie. If you tell the truth and the murderer is caught: honorary title Master Detective. If you lie and the murderer escapes: you lose.",
                }
            },
            "win_condition": {
                "de": "Wenn du Todesursache korrekt benennst und Mörder gefasst wird: Ehrensieg. Wenn deine Giftsammlung entdeckt wird: Du verlierst auch wenn unschuldig.",
                "en": "If you name cause of death correctly and murderer is caught: honorary win. If your poison collection is discovered: you lose even if innocent.",
            },
            "murderer_motive_if_assigned": {
                "de": "Der Graf wollte meine Giftsammlung den Behörden melden — ein Experiment das schiefgelaufen war. Ich benutzte Aconitum. Perfekt für eine Ärztin. Zu perfekt.",
                "en": "The Count wanted to report my poison collection to the authorities — an experiment gone wrong. I used aconitum. Perfect for a doctor. Too perfect.",
            },
            "clues_i_hold": ["poison_collection", "medical_report", "contessa_visit_log"],
            "starting_knowledge": {
                "de": "Aconitum — das ist was du riechst. Oder Arsen. Oder beides — was ungewöhnlich wäre. Die Contessa war heute in deinem Labor. Das verbindet dich mit ihr.",
                "en": "Aconitum — that is what you smell. Or arsenic. Or both — which would be unusual. The Contessa was in your laboratory today. That connects you to her.",
            },
            "connection": {"with": "contessa", "type": "laboratory_visitor"}
        },

        "heiress": {
            "name": {"de": "Signorina Viola Marzano", "en": "Signorina Viola Marzano",
                     "fr": "Signorina Viola Marzano", "it": "Signorina Viola Marzano",
                     "es": "Signorina Viola Marzano", "pt": "Signorina Viola Marzano"},
            "min_players": 7,
            "can_be_murderer": True,
            "intro": {
                "de": "Viola Marzano. Nichte des Grafen. Oder Tochter — das ist kompliziert. Ich erbe alles. Oder ich erbte alles. Emilio hat das Testament heute Nacht geändert. Hatte er Zeit es zu unterschreiben?",
                "en": "Viola Marzano. Niece of the Count. Or daughter — that's complicated. I inherit everything. Or I did. Emilio changed the will tonight. Did he have time to sign it?",
            },
            "appearance": {
                "de": "Weiße Maske — zu viel Unschuld. Rote Augen — geweint oder Schlafmangel. Trinkt gar nicht.",
                "en": "White mask — too much innocence. Red eyes — cried or sleep deprived. Doesn't drink at all.",
            },
            "secret": {
                "de": "Ich bin nicht die Nichte. Ich bin die leibliche Tochter — aus einer nie anerkannten Affäre. Der Graf sagte mir heute Nacht: Er ändert das Testament und hinterlässt mir alles. Dann wurde er tot gefunden. Das sieht sehr schlecht für mich aus.",
                "en": "I am not the niece. I am the biological daughter — from an affair never acknowledged. The Count told me tonight: he's changing the will and leaving me everything. Then he was found dead. This looks very bad for me.",
            },
            "ability": {
                "name": {"de": "Das Testament", "en": "The Will"},
                "description": {
                    "de": "Du hast einen versiegelten Brief des Grafen. Du entscheidest wann du ihn öffnest. Je länger du wartest desto verdächtiger wirkst du. Aber sein Inhalt verändert das Spiel komplett — er benennt jemanden als unerwarteten Erben.",
                    "en": "You have a sealed letter from the Count. You decide when to open it. The longer you wait the more suspicious you appear. But its contents completely change the game — it names someone as an unexpected heir.",
                }
            },
            "win_condition": {
                "de": "Du gewinnst wenn der Mörder gefasst wird UND du als legitime Erbin anerkannt wirst. Du verlierst wenn jemand beweist dass du wusstest dass das Testament sich zu deinen Ungunsten änderte.",
                "en": "You win if the murderer is caught AND you are recognized as legitimate heir. You lose if someone proves you knew the will was changing against your favor.",
            },
            "murderer_motive_if_assigned": {
                "de": "Der Graf änderte seine Meinung — wieder. Die neue Fassung des Testaments hätte mich ausgeschlossen. Der Brief den ich halte ist leer. Den echten habe ich vernichtet.",
                "en": "The Count changed his mind — again. The new version of the will would have excluded me. The letter I hold is blank. The real one I destroyed.",
            },
            "clues_i_hold": ["birth_certificate", "will_envelope"],
            "starting_knowledge": {
                "de": "Du weißt: Es gibt ein altes Testament und ein neues. Das alte begünstigt dich. Das neue auch — oder auch nicht. Die App sagt dir ob du der Mörder bist.",
                "en": "You know: there is an old will and a new one. The old one favors you. The new one also — or perhaps not. The app tells you if you're the murderer.",
            },
            "connection": {"with": "art_dealer", "type": "both_want_estate"}
        },

        "shadow": {
            "name": {"de": "Die Schattenfigur", "en": "The Shadow",
                     "fr": "L'Ombre", "it": "L'Ombra", "es": "La Sombra", "pt": "A Sombra"},
            "min_players": 6,
            "can_be_murderer": False,
            "is_wildcard": True,
            "intro": {
                "de": "Ich bin kein Gast. Ich wurde nicht eingeladen. Ich kam durch ein Fenster. Ich wurde bezahlt. Mehr sage ich nicht.",
                "en": "I am not a guest. I was not invited. I came through a window. I was paid. I say no more.",
            },
            "appearance": {
                "de": "Schwarze Maske, halbes Gesicht bedeckt. Spricht kaum. Antwortet mit Gegenfragen. Hat das Gemälde unter dem Tisch oder in einer Tasche.",
                "en": "Black mask, covers half the face. Barely speaks. Answers with counter-questions. Has the painting under the table or in a bag.",
            },
            "secret": {
                "de": "Ich bin professioneller Dieb. Der Kardinal hat mich bezahlt um das Originalgemälde zu stehlen — als Ablenkung während des Balls. Ich stahl es. Ich tötete niemanden. Ich habe das Original und werde es verkaufen wenn ich den Palazzo verlasse.",
                "en": "I am a professional thief. The Cardinal paid me to steal the original painting — as a distraction during the ball. I stole it. I killed nobody. I have the original and will sell it when I leave the palazzo.",
            },
            "ability": {
                "name": {"de": "Das Original", "en": "The Original"},
                "description": {
                    "de": "Du hast das echte Gemälde. Enthüllst du es: Sofort verdächtig aber du klärst die Gemälde-Frage. Versteckst du es: Du gewinnst wenn niemand es findet. Dein Sieg ist unabhängig vom Mörder.",
                    "en": "You have the real painting. Reveal it: immediately suspicious but you clear the painting question. Hide it: you win if nobody finds it. Your victory is independent from the murderer.",
                }
            },
            "win_condition": {
                "de": "Das echte Gemälde verlässt den Palazzo unentdeckt. Sehr schwer. Das ist Absicht.",
                "en": "The real painting leaves the palazzo undiscovered. Very hard. That's intentional.",
            },
            "clues_i_hold": ["original_painting", "cardinal_commission_note"],
            "starting_knowledge": {
                "de": "Der Kardinal hat dich beauftragt. Du kennst seinen Namen. Er weiß wer du bist. Das verbindet euch — und macht euch beide verletzlich.",
                "en": "The Cardinal commissioned you. You know his name. He knows who you are. That connects you both — and makes you both vulnerable.",
            },
            "connection_multiple": [
                {"with": "cardinal", "type": "painting_commissioner"},
                {"with": "art_dealer", "type": "painting_unknowing"}
            ]
        },

        "investigator": {
            "name": {"de": "Ispettore Carlo Rinaldi", "en": "Inspector Carlo Rinaldi",
                     "fr": "Inspecteur Carlo Rinaldi", "it": "Ispettore Carlo Rinaldi",
                     "es": "Inspector Carlo Rinaldi", "pt": "Inspetor Carlo Rinaldi"},
            "min_players": 8,
            "can_be_murderer": False,
            "intro": {
                "de": "Ispettore Carlo Rinaldi, Questura di Venezia. Ich war zufällig als Gast hier. Jetzt bin ich im Dienst. Alle bleiben. Alle reden. Ich finde die Wahrheit sowieso.",
                "en": "Inspector Carlo Rinaldi, Venice Police. I was here by chance as a guest. Now I'm on duty. Everyone stays. Everyone talks. I'll find the truth anyway.",
            },
            "appearance": {
                "de": "Maske abgenommen nach dem Tod des Grafen. Einziger ohne Maske. Schreibt ständig. Pistole — zeigt er nicht aber alle wissen es.",
                "en": "Mask removed after Count's death. Only one without mask. Constantly writing. Pistol — doesn't show it but everyone knows.",
            },
            "secret": {
                "de": "Ich war nicht zufällig hier. Ich observierte den Grafen seit Wochen — wegen ausländischer Agenten. Ich weiß dass La Colomba in diesem Raum ist. Ich darf sie noch nicht verhaften — ich brauche zuerst den Mörder.",
                "en": "I was not here by chance. I have been surveilling the Count for weeks — because of foreign agents. I know La Colomba is in this room. I cannot arrest them yet — I need the murderer first.",
            },
            "ability": {
                "name": {"de": "Offizielles Verhör", "en": "Official Interrogation"},
                "description": {
                    "de": "Einmal kannst du ein Verhör ausrufen. Alle verlassen den Raum. Du bist 3 Minuten allein mit einer Person. Danach: Alle sagen ob die Person 'kooperativ' war. Du darfst auch lügen über was gesagt wurde.",
                    "en": "Once you may call an interrogation. Everyone leaves the room. You are alone with one person for 3 minutes. Afterwards: everyone says if the person was 'cooperative'. You may also lie about what was said.",
                }
            },
            "win_condition": {
                "de": "Du gewinnst NUR wenn DU als erster den Mörder mit mindestens ZWEI Beweisen korrekt benennst. Kein Bonus-Sieg. Nur Erster.",
                "en": "You win ONLY if YOU are first to correctly name the murderer with at least TWO pieces of evidence. No bonus win. First only.",
            },
            "clues_i_hold": ["surveillance_report", "colomba_file"],
            "starting_knowledge": {
                "de": "La Colomba — das ist der Codename der Agentin. Die App sagt dir wer die Agentin ist. Du weißt auch: Der Graf hatte Kontakte zu fünf Personen am Tisch die alle Motiv hatten. Du hast eine Liste.",
                "en": "La Colomba — that is the agent's code name. The app tells you who the agent is. You also know: the Count had contacts with five people at the table who all had motive. You have a list.",
            },
            "connection": {"with": "spy", "type": "hunter_hunted"}
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # HINWEIS-KETTEN (35 Hinweise in 8 Ketten)
    # ─────────────────────────────────────────────────────────────────────────
    "clue_chains": {
        "chain_gift": {
            "name": {"de": "Die Giftkette", "en": "The Poison Chain"},
            "description": {"de": "Führt zum Tatmittel und zur Quelle", "en": "Leads to the murder weapon and its source"},
            "clues_in_order": ["poison_vial_empty", "pharmacy_label", "contessa_visit_log", "arsenic_trace", "vaticanum_substance", "medical_report"],
            "reveal_condition": "doctor_announces"
        },
        "chain_gemälde": {
            "name": {"de": "Die Gemäldekette", "en": "The Painting Chain"},
            "description": {"de": "Zeigt dass es zwei Gemälde gibt", "en": "Reveals there are two paintings"},
            "clues_in_order": ["painting_receipt", "forgery_tools", "florence_warehouse", "original_painting", "cardinal_commission_note"],
            "reveal_condition": "art_dealer_questioned"
        },
        "chain_agentin": {
            "name": {"de": "Die Agentenkette", "en": "The Agent Chain"},
            "description": {"de": "Enthüllt La Colomba", "en": "Reveals La Colomba"},
            "clues_in_order": ["stolen_documents", "colomba_file", "third_identity_card", "surveillance_report"],
            "reveal_condition": "investigator_pushes"
        },
        "chain_masken": {
            "name": {"de": "Die Maskenkette", "en": "The Mask Chain"},
            "description": {"de": "Zeigt dass Masken getauscht wurden", "en": "Shows masks were swapped"},
            "clues_in_order": ["mask_color", "shoe_buckle", "mask_swap_witness", "real_mask_description"],
            "reveal_condition": "gondolier_speaks"
        },
        "chain_erpressung": {
            "name": {"de": "Die Erpressungskette", "en": "The Blackmail Chain"},
            "description": {"de": "Enthüllt Kardinals Geheimnis", "en": "Reveals Cardinal's secret"},
            "clues_in_order": ["blackmail_payments", "vaticanum_substance", "cardinals_note_unread", "singer_corridor_meeting"],
            "reveal_condition": "singer_opens_note"
        },
        "chain_testament": {
            "name": {"de": "Die Testamentskette", "en": "The Will Chain"},
            "description": {"de": "Zeigt wer wirklich erbt", "en": "Shows who really inherits"},
            "clues_in_order": ["will_envelope", "birth_certificate", "machiavelli_evidence", "palazzo_key"],
            "reveal_condition": "heiress_opens_letter"
        },
        "chain_affäre": {
            "name": {"de": "Die Affärenkette", "en": "The Affair Chain"},
            "description": {"de": "Verbindet Contessa und Agentin", "en": "Connects Contessa and Agent"},
            "clues_in_order": ["affair_letters", "gondola_booking", "corridor_meeting_note"],
            "reveal_condition": "both_pressured"
        },
        "chain_tatort": {
            "name": {"de": "Die Tatortkette", "en": "The Crime Scene Chain"},
            "description": {"de": "Rekonstruiert den Mord", "en": "Reconstructs the murder"},
            "clues_in_order": ["paperweight_evidence", "study_wineglass", "second_crime_note", "time_of_death"],
            "reveal_condition": "investigator_examines"
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # HINWEISE (35 Stück)
    # ─────────────────────────────────────────────────────────────────────────
    "clues": {
        # Giftkette
        "poison_vial_empty": {
            "name": {"de": "Das leere Fläschchen", "en": "The Empty Vial"},
            "text": {"de": "Eines von zwölf Fläschchen in Dr. Neris Tasche ist leer. Frisch geleert. Beschriftung: 'Aconitum napellus — Lethal 2mg'. Das Fläschchen riecht noch.", "en": "One of twelve vials in Dr. Neri's bag is empty. Freshly emptied. Label: 'Aconitum napellus — Lethal 2mg'. The vial still smells."}
        },
        "pharmacy_label": {
            "name": {"de": "Das Apothekenetikett", "en": "The Pharmacy Label"},
            "text": {"de": "Ein Etikett von einer venezianischen Apotheke. Ausgestellt auf Dr. Lucrezia Neri. Aber das Datum ist drei Monate alt — und der Inhalt sollte noch voll sein.", "en": "A label from a Venetian pharmacy. Issued to Dr. Lucrezia Neri. But the date is three months old — and the contents should still be full."}
        },
        "contessa_visit_log": {
            "name": {"de": "Das Besuchsprotokoll", "en": "The Visit Log"},
            "text": {"de": "Dr. Neris Notizbuch: '15:30 — Contessa Marzano. Migräne. Verordnung: Keine. Zugang zum Labor kurz gewährt.' Kurz. Kurz genug.", "en": "Dr. Neri's notebook: '15:30 — Contessa Marzano. Migraine. Prescription: None. Laboratory access briefly granted.' Briefly. Long enough."}
        },
        "arsenic_trace": {
            "name": {"de": "Arsenspur", "en": "Arsenic Trace"},
            "text": {"de": "Im Weinglas des Grafen: Eine weiße Ablagerung. Fast unsichtbar. Fast. Dr. Neri weiss was das bedeutet — die Frage ist ob Arsen oder Aconitum. Vielleicht beides.", "en": "In the Count's wine glass: a white residue. Almost invisible. Almost. Dr. Neri knows what this means — the question is arsenic or aconitum. Perhaps both."}
        },
        "vaticanum_substance": {
            "name": {"de": "Die vatikanische Substanz", "en": "The Vatican Substance"},
            "text": {"de": "Eine Pflanze aus Klostergärten — nur im Vatikan kultiviert. Geruchlos. Imitiert Herzversagen. In früheren Jahrhunderten 'Gottes Instrument' genannt.", "en": "A plant from monastery gardens — only cultivated in the Vatican. Odorless. Mimics heart failure. In earlier centuries called 'God's instrument'."}
        },
        "medical_report": {
            "name": {"de": "Der Befundbericht", "en": "The Medical Report"},
            "text": {"de": "Herzversagen auf den ersten Blick. Genauer: Erweiterte Pupillen, Kribbeln an Extremitäten, Schaum. Klassisches Aconitum — ODER Arsen in sehr hoher Dosis. ODER beides. Selten. Aber möglich.", "en": "Heart failure at first glance. More precisely: dilated pupils, tingling in extremities, foam. Classic aconitum — OR arsenic in very high dose. OR both. Rare. But possible."}
        },
        # Gemäldekette
        "painting_receipt": {
            "name": {"de": "Die Transportquittung", "en": "The Transport Receipt"},
            "text": {"de": "Quittung für Gemäldetransport. Datum: Drei Monate ago. Empfänger: Lagerhaus in Florenz. Absender: 'B.C.' — Benedetto Crane? Oder jemand anderes?", "en": "Receipt for painting transport. Date: three months ago. Recipient: warehouse in Florence. Sender: 'B.C.' — Benedetto Crane? Or someone else?"}
        },
        "forgery_tools": {
            "name": {"de": "Fälscherwerkzeug", "en": "Forgery Tools"},
            "text": {"de": "Pinsel, Pigmente, Lupe. In Cranes Ledertasche. Nicht die Werkzeuge eines normalen Gastes. Er sagte er ist hier wegen Geschäften. Was für Geschäften genau?", "en": "Brushes, pigments, magnifying glass. In Crane's leather bag. Not the tools of a normal guest. He said he's here on business. What kind exactly?"}
        },
        "florence_warehouse": {
            "name": {"de": "Das Florenz-Lager", "en": "The Florence Warehouse"},
            "text": {"de": "Ein Telegramm an Crane: 'Paket angekommen. Original sicher. Zahlung ausstehend. — Florenz.' Datum: Drei Monate alt. Was war das 'Original'?", "en": "A telegram to Crane: 'Package arrived. Original secure. Payment pending. — Florence.' Date: three months ago. What was the 'original'?"}
        },
        "original_painting": {
            "name": {"de": "Das Original-Gemälde", "en": "The Original Painting"},
            "text": {"de": "La Serenissima — das echte Original. Wert: Unschätzbar. Es ist nicht verschwunden. Es ist noch im Raum. Wer es hat bestimmt wer wirklich gewinnt.", "en": "La Serenissima — the real original. Value: priceless. It has not disappeared. It is still in the room. Whoever has it determines who really wins."}
        },
        "cardinal_commission_note": {
            "name": {"de": "Der Auftrag des Kardinals", "en": "The Cardinal's Commission"},
            "text": {"de": "Ein Brief ohne Absender: 'Stehlen Sie das Gemälde während des Balls. Nicht das an der Wand — das andere. Sie wissen wo es liegt. 500 Lire bei Erfolg.' Die Handschrift ist... bischöflich.", "en": "A letter without sender: 'Steal the painting during the ball. Not the one on the wall — the other. You know where it is. 500 lire on success.' The handwriting is... episcopal."}
        },
        # Agentenkette
        "stolen_documents": {
            "name": {"de": "Die gestohlenen Dokumente", "en": "The Stolen Documents"},
            "text": {"de": "Sieben Seiten in einer nicht-italienischen Sprache. Belegen Kontakte zwischen dem Grafen und einer ausländischen Regierung. Die Seiten riechen nach Parfüm. Einem bestimmten Parfüm.", "en": "Seven pages in a non-Italian language. Prove contacts between the Count and a foreign government. The pages smell of perfume. A specific perfume."}
        },
        "colomba_file": {
            "name": {"de": "Die Colomba-Akte", "en": "The Colomba File"},
            "text": {"de": "Codename: La Colomba. Letzte bekannte Mission: Venedig, 1895. Beschreibung: Mehrere Identitäten. Bekannte Kontakte: Venedig, Wien, Paris. Spezialisierung: Dokumentenbeschaffung.", "en": "Code name: La Colomba. Last known mission: Venice, 1895. Description: multiple identities. Known contacts: Venice, Vienna, Paris. Specialization: document acquisition."}
        },
        "third_identity_card": {
            "name": {"de": "Die dritte Visitenkarte", "en": "The Third Business Card"},
            "text": {"de": "Drei Karten. Drei Namen. Einer ist echt. Aber welcher? Und die Parfümwolke die von den Dokumenten kommt — wer in diesem Raum trägt genau dieses Parfüm?", "en": "Three cards. Three names. One is real. But which? And the perfume cloud from the documents — who in this room wears exactly this perfume?"}
        },
        "surveillance_report": {
            "name": {"de": "Der Observationsbericht", "en": "The Surveillance Report"},
            "text": {"de": "Zwei Wochen Observation. Der Graf traf La Colomba regelmäßig. Treffpunkt: Immer nahe Canal Grande. Zeit: Immer nach Mitternacht. Letztes Treffen: Drei Tage ago.", "en": "Two weeks of surveillance. The Count met La Colomba regularly. Meeting place: always near the Grand Canal. Time: always after midnight. Last meeting: three days ago."}
        },
        # Maskenkette
        "mask_color": {
            "name": {"de": "Die Maskenfarbe (Gondoliere)", "en": "The Mask Color (Gondolier)"},
            "text": {"de": "Die Maske war dunkel — schwarz oder sehr dunkles Blau. Mit einer Feder auf der LINKEN Seite. Aber: War die Feder links oder rechts? Der Gondoliere ist nicht mehr sicher.", "en": "The mask was dark — black or very dark blue. With a feather on the LEFT side. But: was the feather left or right? The gondolier is no longer sure."}
        },
        "shoe_buckle": {
            "name": {"de": "Die Schuhschnalle", "en": "The Shoe Buckle"},
            "text": {"de": "Rechteckige goldene Schnalle. Nicht venetianisch — importiert. Möglicherweise aus Wien. Oder Budapest. Jemand in diesem Raum trägt Schuhe mit dieser Schnalle.", "en": "Rectangular gold buckle. Not Venetian — imported. Possibly from Vienna. Or Budapest. Someone in this room is wearing shoes with this buckle."}
        },
        "mask_swap_witness": {
            "name": {"de": "Der Masken-Tausch-Zeuge", "en": "The Mask Swap Witness"},
            "text": {"de": "Jemand hat gesehen wie zwei Personen ihre Masken tauschten — kurz vor Mitternacht, im Korridor. Wer? Das weiß nur die Person die es gesehen hat. Und die erzählt es erst wenn man sie direkt fragt.", "en": "Someone saw two people swap their masks — just before midnight, in the corridor. Who? Only the person who saw it knows. And they'll only say if asked directly."}
        },
        "real_mask_description": {
            "name": {"de": "Die echte Maskenidentität", "en": "The Real Mask Identity"},
            "text": {"de": "Nach dem Masken-Tausch: Wer trug was? Der Gondoliere sah die getauschte Maske — nicht die originale. Das bedeutet: Sein Zeugnis zeigt auf die falsche Person. Absichtlich oder nicht?", "en": "After the mask swap: who wore what? The gondolier saw the swapped mask — not the original. This means: his testimony points to the wrong person. Intentionally or not?"}
        },
        # Erpressungskette
        "blackmail_payments": {
            "name": {"de": "Die Erpressungszahlungen", "en": "The Blackmail Payments"},
            "text": {"de": "Jährliche Überweisung. Absender: Vatikaner Konto. Empfänger: Graf Marzano. Seit 18 Jahren. Gesamt: Über 50.000 Lire. Was war die Sünde die so teuer war?", "en": "Annual transfer. Sender: Vatican account. Recipient: Count Marzano. For 18 years. Total: over 50,000 lire. What was the sin that was so expensive?"}
        },
        "cardinals_note_unread": {
            "name": {"de": "Der ungeöffnete Zettel (Sängerin)", "en": "The Unopened Note (Singer)"},
            "text": {"de": "Der Kardinal gab der Sängerin um 23:15 einen Zettel. Sie hat ihn nicht geöffnet. Der Inhalt könnte den Kardinal überführen — oder entlasten.", "en": "The Cardinal gave the singer a note at 11:15pm. She has not opened it. The contents could implicate — or exonerate — the Cardinal."}
        },
        "singer_corridor_meeting": {
            "name": {"de": "Das Korridor-Treffen", "en": "The Corridor Meeting"},
            "text": {"de": "Die Sängerin traf jemanden im Korridor um 23:15. Wer war es? Und: War der Kardinal allein — oder war noch jemand dabei?", "en": "The singer met someone in the corridor at 11:15pm. Who was it? And: was the Cardinal alone — or was someone else there too?"}
        },
        # Testamentskette
        "will_envelope": {
            "name": {"de": "Der versiegelte Umschlag", "en": "The Sealed Envelope"},
            "text": {"de": "Die Erbin hält einen versiegelten Brief. Was steht drin? Das entscheidet sie. Die Zeit drängt.", "en": "The heiress holds a sealed letter. What is inside? She decides. Time is pressing."}
        },
        "birth_certificate": {
            "name": {"de": "Die Geburtsurkunde", "en": "The Birth Certificate"},
            "text": {"de": "Viola Marzano. Geboren 1871. Vater: Emilio Marzano. Mutter: Eine Frau die nicht Isabella heißt. Nicht Nichte. Tochter. Ein 24 Jahre altes Geheimnis.", "en": "Viola Marzano. Born 1871. Father: Emilio Marzano. Mother: A woman not named Isabella. Not niece. Daughter. A 24-year-old secret."}
        },
        "machiavelli_evidence": {
            "name": {"de": "Der falsche Buchboden", "en": "The False Book Bottom"},
            "text": {"de": "Unter Il Principe: Ein Umschlag. Darin Dokumente die jemanden in diesem Raum ruinieren würden. Den Namen sieht man erst wenn man ihn öffnet.", "en": "Under Il Principe: an envelope. Inside documents that would ruin someone in this room. The name only becomes visible when opened."}
        },
        "palazzo_key": {
            "name": {"de": "Der Palazzo-Schlüssel", "en": "The Palazzo Key"},
            "text": {"de": "Ein eiserner Schlüssel zum Seiteneingang. Nur der Graf und eine weitere Person hatten einen. Wer ist die zweite Person?", "en": "An iron key to the side entrance. Only the Count and one other person had one. Who is the second person?"}
        },
        # Affärenkette
        "affair_letters": {
            "name": {"de": "Die Liebesbriefe", "en": "The Love Letters"},
            "text": {"de": "Drei Briefe. Verschlüsselt — aber die Handschrift verrät Emotion. Zwei verschiedene Handschriften. Beide im Raum. Welche zwei Personen schrieben sich?", "en": "Three letters. Encoded — but the handwriting reveals emotion. Two different handwritings. Both in the room. Which two people wrote to each other?"}
        },
        "gondola_booking": {
            "name": {"de": "Die Gondel-Buchung", "en": "The Gondola Booking"},
            "text": {"de": "Marco führt Buch über alle Fahrten. Eine Buchung vom Nachmittag: Zwei Personen, diskret, ohne Namen. Eine Sonderzahlung. Er kann die Gondel beschreiben.", "en": "Marco keeps records of all rides. A booking from this afternoon: two people, discreet, no names. A special payment. He can describe the gondola."}
        },
        "corridor_meeting_note": {
            "name": {"de": "Die Korridor-Notiz", "en": "The Corridor Note"},
            "text": {"de": "Eine Notiz: 'Um 23:00 — Korridor, zweite Tür links.' Kein Absender. Kein Empfänger. Wer traf wen?", "en": "A note: 'At 11:00pm — corridor, second door left.' No sender. No recipient. Who met whom?"}
        },
        # Tatortkette
        "paperweight_evidence": {
            "name": {"de": "Der Briefbeschwerer", "en": "The Paperweight"},
            "text": {"de": "Auf dem Schreibtisch des Grafen liegt ein schwerer Messing-Briefbeschwerer. Er hat Blut daran — aber der Graf starb angeblich an Gift. Zwei Todesursachen?", "en": "On the Count's desk lies a heavy brass paperweight. It has blood on it — but the Count reportedly died of poison. Two causes of death?"}
        },
        "study_wineglass": {
            "name": {"de": "Das Weinglas im Arbeitszimmer", "en": "The Wine Glass in the Study"},
            "text": {"de": "Im Arbeitszimmer steht ein Weinglas — halb voll. Ein anderes ist umgefallen. Zwei Gläser, zwei Personen. Der Graf hatte Besuch.", "en": "In the study stands a wine glass — half full. Another has fallen over. Two glasses, two people. The Count had a visitor."}
        },
        "second_crime_note": {
            "name": {"de": "Die Notiz zum zweiten Verbrechen", "en": "The Second Crime Note"},
            "text": {"de": "Der Graf schrieb kurz vor seinem Tod: 'Jemand hat das Original. Nicht Crane — jemand anderes. Ich habe es heute Nachmittag bemerkt.' Er schrieb es nicht fertig.", "en": "The Count wrote shortly before his death: 'Someone has the original. Not Crane — someone else. I noticed this afternoon.' He did not finish writing it."}
        },
        "time_of_death": {
            "name": {"de": "Die Todeszeit", "en": "The Time of Death"},
            "text": {"de": "Tod zwischen 23:00 und 23:30 Uhr. Das schränkt den Täterkreis ein. Wer hatte zwischen 23:00 und 23:30 keine nachgewiesene Anwesenheit beim Ball?", "en": "Death between 11pm and 11:30pm. This narrows the suspect pool. Who had no proven attendance at the ball between 11pm and 11:30pm?"}
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PHYSISCHE AUFGABEN (52 Stück)
    # ─────────────────────────────────────────────────────────────────────────
    "physical_tasks": {

        # ── ERÖFFNUNG ────────────────────────────────────────────────────────

        "task_mask_ritual": {
            "trigger_phase": 1, "trigger_condition": "game_started_immediately",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "🎭 MASKENRITUAL: Jeder setzt JETZT seine Maske auf. Ihr tragt sie bis der Ispettore 'Masken ab' ausruft. Die Maske ist dein Alibi — und deine Lüge.",
                "en": "🎭 MASK RITUAL: Everyone puts on their mask NOW. You wear them until the Inspector calls 'masks off'. The mask is your alibi — and your lie.",
            }, "game_effect": "masks_on"
        },

        "task_ghost_entrance": {
            "trigger_phase": 1, "trigger_condition": "game_started_immediately",
            "assigned_to": "count",
            "instruction": {
                "de": "👻 DU BIST TOT: Leg deine Maske langsam ab. Setz dich abseits. Wenn alle vorgestellt sind sagst du einmalig laut: 'Der Graf Marzano ist nicht mehr.' Dann — nur noch Flüstern. Für immer.",
                "en": "👻 YOU ARE DEAD: Slowly remove your mask. Sit apart. When all have been introduced say once aloud: 'Count Marzano is no more.' Then — only whispering. Forever.",
            }, "game_effect": "ghost_active"
        },

        "task_champagne_first": {
            "trigger_phase": 1, "trigger_condition": "introductions_done",
            "assigned_to": "singer",
            "instruction": {
                "de": "🥂 ERSTER TOAST: Steh auf. Singe oder sag: 'Auf den Grafen Marzano — möge seine Wahrheit ans Licht kommen.' Alle müssen trinken. Beobachte wer zögert. Beobachte wer zuerst trinkt.",
                "en": "🥂 FIRST TOAST: Stand up. Sing or say: 'To Count Marzano — may his truth come to light.' Everyone must drink. Observe who hesitates. Observe who drinks first.",
            }, "game_effect": "first_toast"
        },

        "task_three_cards": {
            "trigger_phase": 1, "trigger_condition": "game_started_5min",
            "assigned_to": "spy",
            "instruction": {
                "de": "🃏 IDENTITÄTSWECHSEL: Zeig einer Person am Tisch eine deiner drei Visitenkarten — ohne Erklärung. Wenn sie fragt welcher Name der echte ist: 'Alle.' Wenn sie fragt warum du drei hast: 'Praktisch.'",
                "en": "🃏 IDENTITY SWITCH: Show one person at the table one of your three business cards — without explanation. If they ask which name is real: 'All of them.' If they ask why you have three: 'Practical.'",
            }, "game_effect": "spy_identity_introduced"
        },

        "task_cardinal_rosary": {
            "trigger_phase": 1, "trigger_condition": "game_started_8min",
            "assigned_to": "cardinal",
            "instruction": {
                "de": "📿 DAS GEBET: Leg kurz deinen Rosenkranz sichtbar auf den Tisch. Sag: 'Für den Frieden seiner Seele.' Warte ob jemand auf die Gebetskette reagiert. Wer nervös wird hat etwas mit Religiosität zu tun — oder fürchtet dich.",
                "en": "📿 THE PRAYER: Briefly place your rosary visibly on the table. Say: 'For the peace of his soul.' Wait to see if anyone reacts to the prayer beads. Whoever gets nervous has something to do with religiosity — or fears you.",
            }, "game_effect": "cardinal_religious_signal"
        },

        "task_gondolier_silence": {
            "trigger_phase": 1, "trigger_condition": "game_started_10min",
            "assigned_to": "gondolier",
            "instruction": {
                "de": "🚣 DAS SCHWEIGEN: Sag die ersten 10 Minuten absolut nichts. Wenn jemand dich direkt anspricht sag nur: 'Ich war draußen.' Dann wieder schweigen. Das macht dich interessant — und verdächtig.",
                "en": "🚣 THE SILENCE: Say absolutely nothing for the first 10 minutes. If someone addresses you directly say only: 'I was outside.' Then silence again. This makes you interesting — and suspicious.",
            }, "game_effect": "gondolier_mysterious"
        },

        "task_mask_admire": {
            "trigger_phase": 1, "trigger_condition": "random_first_15min",
            "assigned_to": "random",
            "instruction": {
                "de": "🎭 MASKEN-KOMMENTAR: Geh zu einer Person deiner Wahl und sag: 'Ihre Maske ist wunderschön. Wo haben Sie die her?' Die Person muss antworten. Ihre Antwort könnte wichtig sein — Masken sagen viel.",
                "en": "🎭 MASK COMPLIMENT: Go to a person of your choice and say: 'Your mask is beautiful. Where did you get it?' The person must answer. Their answer could be important — masks say a lot.",
            }, "game_effect": "mask_dialogue"
        },

        # ── TRINK-AUFGABEN (10 Stück) ────────────────────────────────────────

        "task_drink_slow_stare": {
            "trigger_phase": 1, "trigger_condition": "random_15min",
            "assigned_to": "contessa",
            "instruction": {
                "de": "🍷 DER BLICK: Trinke sehr langsam. Beim Trinken: Schau einer anderen Person direkt in die Augen ohne wegzusehen bis du fertig bist. Diese Person fühlt sich beobachtet. Das ist Absicht.",
                "en": "🍷 THE GAZE: Drink very slowly. While drinking: look directly into another person's eyes without looking away until you're done. That person will feel observed. That's intentional.",
            }, "game_effect": "contessa_intimidation"
        },

        "task_champagne_only": {
            "trigger_phase": 1, "trigger_condition": "group_drink_offered",
            "assigned_to": "singer",
            "instruction": {
                "de": "🥂 CHAMPAGNER IMMER: Wenn jemand Wein anbietet sage immer: 'Nur Champagner für mich.' Wenn kein Champagner da ist: 'Dann nichts.' Diese Weigerung fällt auf.",
                "en": "🥂 CHAMPAGNE ALWAYS: When anyone offers wine always say: 'Only champagne for me.' If no champagne is available: 'Then nothing.' This refusal will be noticed.",
            }, "game_effect": "singer_drink_preference_noted"
        },

        "task_poisoned_toast_murder": {
            "trigger_phase": 1, "trigger_condition": "baron_proposes_toast",
            "assigned_to": "murderer",
            "private": True,
            "instruction": {
                "de": "🎭 MÖRDER-TRINKAUFGABE: Beim ersten Toast: Trinke als ERSTER und am demonstrativsten. Zeige keine Angst vor dem Wein. Sage laut: 'Ausgezeichneter Jahrgang.' Das klingt unschuldig. Das ist Absicht.",
                "en": "🎭 MURDERER DRINK TASK: At the first toast: drink FIRST and most demonstratively. Show no fear of the wine. Say aloud: 'Excellent vintage.' This sounds innocent. That's intentional.",
            }, "game_effect": "murderer_drink_signal"
        },

        "task_group_drink_venetian": {
            "trigger_phase": 2, "trigger_condition": "investigation_15min",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "🍷 VENEZIANISCHER BRAUCH: Nach einem Tod trinkt man gemeinsam — für die Seele des Verstorbenen. Alle trinken gleichzeitig auf drei. Wer NICHT trinkt bricht den Brauch. Das ist auffällig.",
                "en": "🍷 VENETIAN CUSTOM: After a death one drinks together — for the soul of the deceased. Everyone drinks simultaneously on three. Whoever does NOT drink breaks the custom. That is conspicuous.",
            }, "game_effect": "group_drink_observed"
        },

        "task_wine_clue_random": {
            "trigger_phase": 2, "trigger_condition": "random_post_murder",
            "assigned_to": "random",
            "instruction": {
                "de": "🍷 WEINBEOBACHTUNG: Trinke demonstrativ. Sage dann: 'Der Wein des Grafen wurde mir heute Abend besonders angeboten — von einer bestimmten Person. Ich lehnte ab.' Wer nervös wird hat einen Grund.",
                "en": "🍷 WINE OBSERVATION: Drink demonstratively. Then say: 'The Count's wine was specifically offered to me tonight — by a specific person. I declined.' Whoever gets nervous has a reason.",
            }, "game_effect": "wine_offer_revealed"
        },

        "task_drink_no_reason": {
            "trigger_phase": 2, "trigger_condition": "investigation_20min",
            "assigned_to": "art_dealer",
            "instruction": {
                "de": "🥃 SCHNELL TRINKEN: Trink jetzt schnell — einen langen Zug. Stelle das Glas ab. Wische dir den Mund ab. Sag nichts. Diese nervöse Geste fällt auf — und sie soll auffallen.",
                "en": "🥃 DRINK FAST: Drink quickly now — one long gulp. Set the glass down. Wipe your mouth. Say nothing. This nervous gesture will be noticed — and it's meant to be.",
            }, "game_effect": "crane_nervous_drinking"
        },

        "task_champagne_clue_speak": {
            "trigger_phase": 2, "trigger_condition": "random_30min",
            "assigned_to": "random",
            "instruction": {
                "de": "🥂 WEINHINWEIS: Hebe dein Glas. Sag: 'Der Graf hatte immer nur den besten Wein. Heute Abend schmeckte seines... anders. Ich saß neben ihm beim Dinner.' Beobachte wer aufhorcht.",
                "en": "🥂 WINE CLUE: Raise your glass. Say: 'The Count always had only the best wine. Tonight his tasted... different. I sat next to him at dinner.' Observe who perks up.",
            }, "game_effect": "wine_taste_clue"
        },

        "task_final_champagne": {
            "trigger_phase": 3, "trigger_condition": "reckoning_begins",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "🥂 DER LETZTE TOAST: Vor der finalen Anklage — alle trinken. Der Ispettore (oder wer es möchte) sagt einen abschließenden Toast. Dann: Die Wahrheit.",
                "en": "🥂 THE FINAL TOAST: Before the final accusation — everyone drinks. The Inspector (or whoever wishes) says a closing toast. Then: the truth.",
            }, "game_effect": "final_toast"
        },

        "task_second_group_drink": {
            "trigger_phase": 3, "trigger_condition": "investigation_midpoint",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "🍷 NOCHMAL: Alle trinken gleichzeitig. Wer diesmal ablehnt hatte auch beim letzten Mal Bedenken. Das ist ein Muster.",
                "en": "🍷 AGAIN: Everyone drinks simultaneously. Whoever declines this time also had reservations last time. That is a pattern.",
            }, "game_effect": "second_group_drink"
        },

        "task_ghost_drink_signal": {
            "trigger_phase": 2, "trigger_condition": "baron_wants_to_hint",
            "assigned_to": "count",
            "instruction": {
                "de": "👻 GEIST-TRINK-SIGNAL: Wenn ein Toast ausgesprochen wird — strecke eine Hand aus als ob du auch trinken würdest. Dann zieht sie sie langsam zurück. Schau die Person an die zuletzt getrunken hat. Das ist ein Hinweis.",
                "en": "👻 GHOST DRINK SIGNAL: When a toast is made — stretch out a hand as if you would also drink. Then slowly pull it back. Look at the person who drank last. That is a clue.",
            }, "game_effect": "ghost_drink_hint"
        },

        # ── STANDARD AUFGABEN ────────────────────────────────────────────────

        "task_candle_signal": {
            "trigger_phase": 2, "trigger_condition": "investigation_begins",
            "assigned_to": "gondolier",
            "instruction": {
                "de": "🕯️ DAS SIGNAL: Steh auf. Geh zu den Kerzen. Lösche EINE aus. Sag nichts. Setz dich. Wenn jemand fragt: 'Ein Zeichen.' Mehr nicht. Du bist bereit zu reden — wenn die richtige Person fragt.",
                "en": "🕯️ THE SIGNAL: Stand up. Go to the candles. Extinguish ONE. Say nothing. Sit back down. If asked: 'A sign.' No more. You are ready to talk — if the right person asks.",
            }, "game_effect": "gondolier_ready"
        },

        "task_private_confession_offer": {
            "trigger_phase": 2, "trigger_condition": "investigation_5min",
            "assigned_to": "cardinal",
            "instruction": {
                "de": "⛪ BEICHTANGEBOT: Geh zu einer Person. Flüstere: 'Möchten Sie beichten? Was Sie mir sagen bleibt unter uns.' Ob sie redet entscheidet sie. Aber dein Angebot macht dich verdächtig.",
                "en": "⛪ CONFESSION OFFER: Go to one person. Whisper: 'Would you like to confess? What you tell me stays between us.' Whether they speak is their choice. But your offer makes you suspicious.",
            }, "game_effect": "confession_offered"
        },

        "task_painting_gone": {
            "trigger_phase": 2, "trigger_condition": "body_discovered",
            "assigned_to": "art_dealer",
            "instruction": {
                "de": "🖼️ DAS GEMÄLDE: Geh zum leeren Rahmen. Schau hin. Dreh dich um. Sag laut: 'Das Gemälde... es ist weg.' Echte oder gespielte Bestürzung. Beide funktionieren.",
                "en": "🖼️ THE PAINTING: Go to the empty frame. Look at it. Turn around. Say aloud: 'The painting... it's gone.' Real or performed distress. Both work.",
            }, "game_effect": "painting_theft_revealed"
        },

        "task_document_hide": {
            "trigger_phase": 2, "trigger_condition": "investigation_10min",
            "assigned_to": "spy",
            "instruction": {
                "de": "📄 DOKUMENT VERSTECKEN: Tu als ob du etwas in deine Tasche steckst. Jemand soll es sehen. Wenn gefragt: 'Nichts wichtiges.' Wenn bestanden: Zeig einen leeren Zettel.",
                "en": "📄 HIDE DOCUMENT: Act as if you're putting something in your bag. Someone should see it. If asked: 'Nothing important.' If pressed: show a blank piece of paper.",
            }, "game_effect": "spy_document_spotted"
        },

        "task_autopsy_smell": {
            "trigger_phase": 2, "trigger_condition": "body_discovered_plus_5min",
            "assigned_to": "doctor",
            "instruction": {
                "de": "🩺 DIE UNTERSUCHUNG: Geh zum Tatort. Knie kurz hin oder tu so als ob. Steh auf. Sag laut: 'Ich rieche etwas. Das ist kein natürlicher Tod.' Mehr sagst du noch nicht.",
                "en": "🩺 THE EXAMINATION: Go to the crime scene. Briefly kneel or pretend to. Stand up. Say aloud: 'I smell something. This is not a natural death.' You say no more for now.",
            }, "game_effect": "murder_confirmed"
        },

        "task_singer_break": {
            "trigger_phase": 1, "trigger_condition": "game_started_15min",
            "assigned_to": "singer",
            "instruction": {
                "de": "🎵 DIE PAUSE: Sag laut: 'Ich muss kurz Luft holen.' Steh auf. Geh zur Tür oder ans Fenster. Bleib 2 Minuten weg (geh auf die Toilette oder steh einfach im Flur). Komm zurück und sag nichts darüber.",
                "en": "🎵 THE BREAK: Say aloud: 'I need a moment of air.' Stand up. Go to the door or window. Stay away 2 minutes (go to bathroom or simply stand in hallway). Return and say nothing about it.",
            }, "game_effect": "singer_absence_noted"
        },

        "task_heiress_letter_pressure": {
            "trigger_phase": 2, "trigger_condition": "midgame_25min",
            "assigned_to": "heiress",
            "instruction": {
                "de": "✉️ DER BRIEF: Du hältst ihn schon eine Weile. Alle wissen es. Jetzt oder nie — oder noch warten? Je länger du wartest desto mehr Augen sind auf dich gerichtet.",
                "en": "✉️ THE LETTER: You've been holding it for a while. Everyone knows. Now or never — or wait more? The longer you wait the more eyes are on you.",
            }, "game_effect": "letter_pressure_moment"
        },

        "task_mask_swap": {
            "trigger_phase": 1, "trigger_condition": "game_started_10min",
            "assigned_to": "spy",
            "instruction": {
                "de": "🎭 MASKEN-TAUSCH: Geh zu einer Person und tausche deine Maske mit ihr — ohne Erklärung. Diese Person muss mitspielen. Durch den Tausch verschieben sich alle Zeugenaussagen über Masken.",
                "en": "🎭 MASK SWAP: Go to a person and swap your mask with them — without explanation. That person must play along. Through the swap all witness statements about masks shift.",
            }, "game_effect": "masks_swapped"
        },

        "task_masks_off": {
            "trigger_phase": 2, "trigger_condition": "investigation_20min",
            "assigned_to": "investigator",
            "instruction": {
                "de": "🔍 MASKEN AB: Steh auf. Sag laut: 'Im Namen der Questura di Venezia — alle nehmen jetzt ihre Masken ab. Für immer.' Alle müssen gehorchen. Jetzt sieht man Gesichter.",
                "en": "🔍 MASKS OFF: Stand up. Say aloud: 'In the name of the Venice Police — everyone removes their masks now. Forever.' Everyone must comply. Now faces can be seen.",
            }, "game_effect": "masks_removed"
        },

        "task_shadow_decision": {
            "trigger_phase": 2, "trigger_condition": "painting_theft_revealed",
            "assigned_to": "shadow",
            "instruction": {
                "de": "🌑 GEMÄLDE-ENTSCHEIDUNG: Du hast das Original. Enthüllst du es oder versteckst du es weiter? Wenn du es enthüllst bist du sofort verdächtig — aber du räumst die Gemälde-Frage auf. Entscheide jetzt. Still.",
                "en": "🌑 PAINTING DECISION: You have the original. Do you reveal it or continue hiding it? If you reveal it you're immediately suspicious — but you clear the painting question. Decide now. Silently.",
            }, "game_effect": "shadow_decision"
        },

        "task_gondolier_testimony": {
            "trigger_phase": 2, "trigger_condition": "gondolier_candle_signal",
            "assigned_to": "gondolier",
            "instruction": {
                "de": "👁️ DIE AUSSAGE: Steh auf. Beschreibe die Person die du sahst: Maske (Farbe, Feder), Schuhe (Schnalle). Sage dann: 'Das ist alles.' Setz dich. Keine weiteren Fragen beantworten bis jemand dir etwas anbietet — Wasser, Information, einen Tausch.",
                "en": "👁️ THE TESTIMONY: Stand up. Describe the person you saw: mask (color, feather), shoes (buckle). Then say: 'That is all.' Sit down. Answer no further questions until someone offers you something — water, information, an exchange.",
            }, "game_effect": "gondolier_testimony"
        },

        "task_cardinal_deny_shadow": {
            "trigger_phase": 2, "trigger_condition": "shadow_mentioned",
            "assigned_to": "cardinal",
            "instruction": {
                "de": "⛪ LEUGNEN: Wenn jemand die Schattenfigur erwähnt oder einen Dieb — reagiere sofort: 'Ich kenne keine solche Person.' Überzeugend. Aber nicht zu schnell. Zu schnelles Leugnen ist selbst ein Verdacht.",
                "en": "⛪ DENY: When someone mentions the Shadow figure or a thief — react immediately: 'I know no such person.' Convincing. But not too fast. Too quick denial is itself suspicious.",
            }, "game_effect": "cardinal_shadow_denial"
        },

        "task_singer_opens_note": {
            "trigger_phase": 2, "trigger_condition": "singer_pressured",
            "assigned_to": "singer",
            "instruction": {
                "de": "🎵 DER ZETTEL: Jemand fragt dich was auf dem Zettel steht den der Kardinal dir gab. Du entscheidest: Öffne ihn jetzt — oder sage 'Den öffne ich erst später'. Was auf dem Zettel steht bestimmt die App.",
                "en": "🎵 THE NOTE: Someone asks you what's on the note the Cardinal gave you. You decide: open it now — or say 'I'll open that later'. What's on the note the app determines.",
            }, "game_effect": "singer_note_decision"
        },

        "task_investigator_interrogation": {
            "trigger_phase": 2, "trigger_condition": "investigation_midpoint",
            "assigned_to": "investigator",
            "instruction": {
                "de": "🔦 OFFIZIELLES VERHÖR: Ruf ein Verhör aus. Alle verlassen den Raum. Du bleibst 3 Minuten allein mit einer Person. Was gesagt wird entscheidet ihr. Danach: Alle sagen ob die Person 'kooperativ' war.",
                "en": "🔦 OFFICIAL INTERROGATION: Call an interrogation. Everyone leaves the room. You remain 3 minutes alone with one person. What's said is up to you. Afterwards: everyone says if the person was 'cooperative'.",
            }, "game_effect": "interrogation_called"
        },

        "task_doctor_vial_reveal": {
            "trigger_phase": 2, "trigger_condition": "doctor_pressured",
            "assigned_to": "doctor",
            "instruction": {
                "de": "🩺 DIE OFFENBARUNG: Zeige die leere Flasche aus deiner Tasche — oder tue so als ob du sie herausnehmen würdest. Sage: 'Eine Substanz fehlt aus meiner Sammlung. Jemand in diesem Raum hat sie gestohlen.' Pause. Schau jeden an.",
                "en": "🩺 THE REVELATION: Show the empty vial from your bag — or pretend to take it out. Say: 'A substance is missing from my collection. Someone in this room stole it.' Pause. Look at everyone.",
            }, "game_effect": "poison_theft_revealed"
        },

        "task_contessa_breakdown": {
            "trigger_phase": 2, "trigger_condition": "contessa_under_pressure",
            "assigned_to": "contessa",
            "instruction": {
                "de": "😭 DER ZUSAMMENBRUCH: Jetzt ist dein Moment. Spiele eine emotionale Szene — Tränen, Wut oder stummen Schmerz. 2 Minuten lang darf niemand dich befragen. Ob es gespielt ist oder nicht — das entscheidest du.",
                "en": "😭 THE BREAKDOWN: Now is your moment. Play an emotional scene — tears, anger or silent pain. For 2 minutes nobody may question you. Whether it's performed or not — that's up to you.",
            }, "game_effect": "contessa_scene"
        },

        "task_ghost_second_whisper": {
            "trigger_phase": 2, "trigger_condition": "investigation_halfway",
            "assigned_to": "count",
            "instruction": {
                "de": "👻 ZWEITER HINWEIS: Wähle eine andere Person als beim ersten Mal. Diesmal: Flüstere etwas über ein OBJEKT — nicht über eine Person. Zum Beispiel: 'Das Buch.' Oder: 'Die Schuhe.' Oder: 'Die Flasche.'",
                "en": "👻 SECOND CLUE: Choose a different person than the first time. This time: whisper something about an OBJECT — not a person. For example: 'The book.' Or: 'The shoes.' Or: 'The vial.'",
            }, "game_effect": "ghost_second_clue"
        },

        "task_ghost_third_whisper": {
            "trigger_phase": 3, "trigger_condition": "reckoning_near",
            "assigned_to": "count",
            "instruction": {
                "de": "👻 LETZTER HINWEIS: Dein letzter Flüster-Hinweis. Wähle die Person die dem Mörder am nächsten ist. Diesmal: Du kannst eine Richtung angeben — 'Warm' oder 'Kalt'. Kein Name. Nie.",
                "en": "👻 FINAL CLUE: Your last whispered clue. Choose the person closest to the murderer. This time: you may give a direction — 'Warm' or 'Cold'. No name. Never.",
            }, "game_effect": "ghost_final_clue"
        },

        # ── KETTENAUFGABEN (Rolle A triggert Reaktion bei Rolle B) ────────────

        "chain_task_a1_cardinal_singer": {
            "trigger_phase": 1, "trigger_condition": "cardinal_gives_note",
            "assigned_to": "cardinal",
            "instruction": {
                "de": "⛪→🎵 KETTENAKTION 1A: Geh zur Sängerin. Gib ihr einen kleinen gefalteten Zettel (nutze einen Zettel aus deiner Tasche). Flüstere: 'Bitte öffne das nicht bis ich es sage.' Dann geh zurück.",
                "en": "⛪→🎵 CHAIN ACTION 1A: Go to the singer. Give her a small folded note (use a piece of paper from your pocket). Whisper: 'Please don't open this until I say so.' Then return.",
            }, "game_effect": "chain_cardinal_note_given",
            "triggers_chain": "chain_task_a2_singer_reaction"
        },

        "chain_task_a2_singer_reaction": {
            "trigger_phase": 1, "trigger_condition": "cardinal_gives_note_to_singer",
            "assigned_to": "singer",
            "instruction": {
                "de": "🎵→⛪ KETTENAKTION 1B: Du hast den Zettel vom Kardinal. Reagiere sichtbar — zeige dass du ihn erhalten hast. Stecke ihn demonstrativ in deine Tasche. Alle sehen dass du etwas hast.",
                "en": "🎵→⛪ CHAIN ACTION 1B: You have the note from the Cardinal. React visibly — show you received it. Demonstratively put it in your pocket. Everyone sees you have something.",
            }, "game_effect": "chain_note_visible_to_all"
        },

        "chain_task_b1_spy_swap_contessa": {
            "trigger_phase": 1, "trigger_condition": "game_started_12min",
            "assigned_to": "spy",
            "instruction": {
                "de": "🕵️→👸 KETTENAKTION 2A: Geh zur Contessa. Tausche deine Maske mit ihr — kurz, heimlich, ohne Worte. Wenn jemand es sieht: 'Meine Maske drückte.' Dann wechselt ihr zurück wenn niemand schaut.",
                "en": "🕵️→👸 CHAIN ACTION 2A: Go to the Contessa. Swap your mask with her — briefly, secretly, without words. If anyone sees it: 'My mask was pressing.' Then switch back when nobody is watching.",
            }, "game_effect": "chain_spy_contessa_swap",
            "triggers_chain": "chain_task_b2_gondolier_sees"
        },

        "chain_task_b2_gondolier_sees": {
            "trigger_phase": 1, "trigger_condition": "spy_contessa_swap_observed",
            "assigned_to": "gondolier",
            "instruction": {
                "de": "🚣→🕵️ KETTENAKTION 2B: Du hast gerade gesehen wie zwei Personen ihre Masken tauschten. Das macht deine Zeugenaussage kompliziert. Sag nichts darüber — noch nicht. Aber merke dir: Du hast es gesehen.",
                "en": "🚣→🕵️ CHAIN ACTION 2B: You just saw two people swap their masks. This complicates your witness testimony. Say nothing about it — not yet. But remember: you saw it.",
            }, "game_effect": "gondolier_sees_swap"
        },

        "chain_task_c1_doctor_contessa": {
            "trigger_phase": 2, "trigger_condition": "investigation_8min",
            "assigned_to": "doctor",
            "instruction": {
                "de": "🩺→👸 KETTENAKTION 3A: Geh zur Contessa. Sag leise aber hörbar für Nachbarn: 'Sie waren heute Nachmittag in meinem Labor. Ich erinnere mich genau.' Warte ihre Reaktion ab.",
                "en": "🩺→👸 CHAIN ACTION 3A: Go to the Contessa. Say quietly but audibly to neighbors: 'You were in my laboratory this afternoon. I remember clearly.' Wait for her reaction.",
            }, "game_effect": "chain_doctor_confronts_contessa",
            "triggers_chain": "chain_task_c2_contessa_respond"
        },

        "chain_task_c2_contessa_respond": {
            "trigger_phase": 2, "trigger_condition": "doctor_mentions_lab_visit",
            "assigned_to": "contessa",
            "instruction": {
                "de": "👸→🩺 KETTENAKTION 3B: Die Ärztin konfrontiert dich. Du entscheidest: Gib den Besuch zu ('Ja, für Migräne-Medizin') oder leugne ihn. Beide Optionen haben Konsequenzen.",
                "en": "👸→🩺 CHAIN ACTION 3B: The doctor confronts you. You decide: admit the visit ('Yes, for migraine medicine') or deny it. Both options have consequences.",
            }, "game_effect": "contessa_lab_response"
        },

        "chain_task_d1_shadow_cardinal": {
            "trigger_phase": 2, "trigger_condition": "painting_mentioned",
            "assigned_to": "shadow",
            "instruction": {
                "de": "🌑→⛪ KETTENAKTION 4A: Wenn das Gemälde erwähnt wird — schau kurz zum Kardinal. Nur einen Moment. Dann schau weg. Das ist eine Andeutung — dein Auftraggeber fühlt sich beobachtet.",
                "en": "🌑→⛪ CHAIN ACTION 4A: When the painting is mentioned — briefly look at the Cardinal. Just a moment. Then look away. This is a hint — your commissioner feels observed.",
            }, "game_effect": "chain_shadow_signals_cardinal",
            "triggers_chain": "chain_task_d2_cardinal_nervous"
        },

        "chain_task_d2_cardinal_nervous": {
            "trigger_phase": 2, "trigger_condition": "shadow_looks_at_cardinal",
            "assigned_to": "cardinal",
            "instruction": {
                "de": "⛪→🌑 KETTENAKTION 4B: Die Schattenfigur hat dich angesehen. Du weißt was das bedeutet. Reagiere mit minimaler Nervosität — ein leises Räuspern, der Griff zum Rosenkranz. Dann Ruhe.",
                "en": "⛪→🌑 CHAIN ACTION 4B: The Shadow figure looked at you. You know what that means. React with minimal nervousness — a quiet throat clearing, reaching for the rosary. Then calm.",
            }, "game_effect": "cardinal_nervous_reaction"
        },

        "chain_task_e1_heiress_artdealer": {
            "trigger_phase": 2, "trigger_condition": "will_mentioned",
            "assigned_to": "heiress",
            "instruction": {
                "de": "👸→🖼️ KETTENAKTION 5A: Wenn das Testament erwähnt wird — schau den Kunsthändler an. Dann sag: 'Das Erbe des Grafen ist komplizierter als Sie denken, Signor Crane.' Schau weg. Lass ihn grübeln.",
                "en": "👸→🖼️ CHAIN ACTION 5A: When the will is mentioned — look at the art dealer. Then say: 'The Count's inheritance is more complicated than you think, Signor Crane.' Look away. Let him wonder.",
            }, "game_effect": "chain_heiress_hints_to_crane",
            "triggers_chain": "chain_task_e2_crane_reacts"
        },

        "chain_task_e2_crane_reacts": {
            "trigger_phase": 2, "trigger_condition": "heiress_addresses_crane",
            "assigned_to": "art_dealer",
            "instruction": {
                "de": "🖼️→👸 KETTENAKTION 5B: Die Erbin sprach dich direkt an. Reagiere vorsichtig: 'Was meinen Sie damit?' Nichts preisgeben. Aber zeige Interesse. Das Erbe und das Gemälde könnten zusammenhängen.",
                "en": "🖼️→👸 CHAIN ACTION 5B: The heiress addressed you directly. React carefully: 'What do you mean by that?' Reveal nothing. But show interest. The inheritance and the painting could be connected.",
            }, "game_effect": "crane_heiress_dialogue"
        },

        "chain_task_f1_investigator_spy": {
            "trigger_phase": 2, "trigger_condition": "investigator_suspects_agent",
            "assigned_to": "investigator",
            "instruction": {
                "de": "🔦→🕵️ KETTENAKTION 6A: Geh zur Agentin. Zeige ihr eine der Visitenkarten die du 'zufällig' gefunden hast (nutze eine eigene Karte oder einen Zettel). Sag: 'Sagt Ihnen dieser Name etwas?' Beobachte ihre Reaktion.",
                "en": "🔦→🕵️ CHAIN ACTION 6A: Go to the agent. Show them one of the business cards you 'accidentally' found (use your own card or a note). Say: 'Does this name mean anything to you?' Observe their reaction.",
            }, "game_effect": "chain_inspector_confronts_agent",
            "triggers_chain": "chain_task_f2_spy_reacts"
        },

        "chain_task_f2_spy_reacts": {
            "trigger_phase": 2, "trigger_condition": "inspector_shows_card",
            "assigned_to": "spy",
            "instruction": {
                "de": "🕵️→🔦 KETTENAKTION 6B: Der Ispettore zeigt dir eine Karte. Das ist ernst. Entscheide: Gib du eine Identität preis ('Das bin ich nicht') oder wechsle jetzt deine aktuelle Identität. Du hast 10 Sekunden.",
                "en": "🕵️→🔦 CHAIN ACTION 6B: The Inspector shows you a card. This is serious. Decide: reveal an identity ('That's not me') or switch your current identity now. You have 10 seconds.",
            }, "game_effect": "spy_identity_pressure"
        },

        # ── MÖRDER-AUFGABEN (8 Stück) ────────────────────────────────────────

        "murderer_task_alibi_mask": {
            "trigger_phase": 2, "trigger_condition": "murder_announced",
            "assigned_to": "murderer",
            "private": True,
            "instruction": {
                "de": "🎭 MÖRDER 1 — MASKE: Dein Alibi ist die Maskenverwirrung. Behaupte du hast eine ANDERE Maske getragen — eine die jemand anderes auch trug. 'Wir haben getauscht.' Die Person muss mitspielen oder widersprechen.",
                "en": "🎭 MURDERER 1 — MASK: Your alibi is the mask confusion. Claim you wore a DIFFERENT mask — one that someone else also wore. 'We swapped.' The person must play along or contradict.",
            }, "game_effect": "murderer_mask_alibi"
        },

        "murderer_task_redirect_painting": {
            "trigger_phase": 2, "trigger_condition": "painting_gone_revealed",
            "assigned_to": "murderer",
            "private": True,
            "instruction": {
                "de": "🎭 MÖRDER 2 — GEMÄLDE: Das gestohlene Gemälde ist deine beste Ablenkung. Sage subtil: 'Wer das Gemälde stahl war auch im Arbeitszimmer.' Das lenkt von dir ab — und auf jemand anderen.",
                "en": "🎭 MURDERER 2 — PAINTING: The stolen painting is your best distraction. Say subtly: 'Whoever stole the painting was also in the study.' This deflects from you — and toward someone else.",
            }, "game_effect": "red_herring_painting"
        },

        "murderer_task_sympathy": {
            "trigger_phase": 2, "trigger_condition": "doctor_confirms_murder",
            "assigned_to": "murderer",
            "private": True,
            "instruction": {
                "de": "🎭 MÖRDER 3 — MITGEFÜHL: Wenn die Ärztin den Mord bestätigt: Reagiere mit ÜBERTRIEBENER Betroffenheit. Steh auf. Sage: 'Das ist unfassbar. Wer tut so etwas?' Setz dich. Übertriebene Reaktionen wirken echt wenn alle im Schock sind.",
                "en": "🎭 MURDERER 3 — SYMPATHY: When the doctor confirms the murder: react with EXAGGERATED distress. Stand up. Say: 'This is unbelievable. Who does something like that?' Sit down. Exaggerated reactions seem genuine when everyone is in shock.",
            }, "game_effect": "murderer_sympathy_performance"
        },

        "murderer_task_question": {
            "trigger_phase": 2, "trigger_condition": "investigation_8min",
            "assigned_to": "murderer",
            "private": True,
            "instruction": {
                "de": "🎭 MÖRDER 4 — FRAGE: Stelle jetzt eine Frage die Verdacht auf jemand anderen lenkt. Gut: 'Wer hat heute Nachmittag das Labor der Ärztin besucht?' Oder: 'Wessen Maske war zwischen 23 und 23:30 nicht eindeutig zuzuordnen?'",
                "en": "🎭 MURDERER 4 — QUESTION: Now ask a question that directs suspicion toward someone else. Good: 'Who visited the doctor's laboratory this afternoon?' Or: 'Whose mask was not clearly identifiable between 11 and 11:30?'",
            }, "game_effect": "murderer_deflection_question"
        },

        "murderer_task_help_investigator": {
            "trigger_phase": 2, "trigger_condition": "investigator_active",
            "assigned_to": "murderer",
            "private": True,
            "instruction": {
                "de": "🎭 MÖRDER 5 — DER HELFER: Hilf dem Ispettore aktiv. Mach einen Vorschlag. 'Was wenn wir systematisch die Bewegungen zwischen 23 und 23:30 rekonstruieren?' Wer beim Aufklären hilft steht nicht im Verdacht.",
                "en": "🎭 MURDERER 5 — THE HELPER: Actively help the Inspector. Make a suggestion. 'What if we systematically reconstruct movements between 11 and 11:30?' Whoever helps with the investigation isn't suspected.",
            }, "game_effect": "murderer_cooperation_mask"
        },

        "murderer_task_accuse_specific": {
            "trigger_phase": 3, "trigger_condition": "suspicion_rising_on_murderer",
            "assigned_to": "murderer",
            "private": True,
            "instruction": {
                "de": "🎭 MÖRDER 6 — ANKLAGE: Jetzt ist der Moment für eine gezielte Beschuldigung. Wähle eine Person mit einem echten Geheimnis. Nutze dieses Geheimnis als Basis. 'Wussten Sie dass [Person] [wahres Geheimnis]?' Sorge für Chaos.",
                "en": "🎭 MURDERER 6 — ACCUSATION: Now is the moment for a targeted accusation. Choose a person with a real secret. Use this secret as the basis. 'Did you know that [person] [true secret]?' Create chaos.",
            }, "game_effect": "red_herring_accusation"
        },

        "murderer_task_gondolier_silence": {
            "trigger_phase": 2, "trigger_condition": "gondolier_about_to_speak",
            "assigned_to": "murderer",
            "private": True,
            "instruction": {
                "de": "🎭 MÖRDER 7 — GONDELZEUGE: Der Gondoliere will reden. Handle bevor er es tut. Geh zu ihm. Sag leise: 'Was Sie zu sagen haben... wäre das wirklich klug? In Ihrem Interesse?' Du darfst nicht drohen — nur andeuten.",
                "en": "🎭 MURDERER 7 — GONDOLIER: The gondolier wants to speak. Act before he does. Go to him. Say quietly: 'What you want to say... would that really be wise? In your interest?' You may not threaten — only hint.",
            }, "game_effect": "murderer_intimidates_gondolier"
        },

        "murderer_panic": {
            "trigger_phase": 3, "trigger_condition": "someone_gets_close_to_truth",
            "assigned_to": "murderer",
            "private": True,
            "time_limit_seconds": 60,
            "instruction": {
                "de": "⚠️ PANIKMOMENT — 60 SEKUNDEN — NUR FÜR DICH:\n\nJemand kommt der Wahrheit sehr nahe. Wähle JETZT:\n\nA — DIE MASKE: 'Das war nicht ich. Meine Maske trug jemand anderes.'\n\nB — DAS GEMÄLDE: Alles auf das gestohlene Gemälde lenken. Aggressiv, schnell, überzeugend.\n\nC — DER ZUSAMMENBRUCH: Emotional werden. Überwältigt sein. Niemand verdächtigt Weinende.\n\nD — DIE GEGENANKLAGE: Sofort eine andere Person beschuldigen — konkret, mit einem wahren Detail.\n\nE — DAS GESTÄNDNIS: Gestehe etwas Harmloses aber Belastendes — ein kleiner Fehler, eine Lüge. Lenk ab.\n\n60 Sekunden. Jetzt.",
                "en": "⚠️ PANIC MOMENT — 60 SECONDS — ONLY FOR YOU:\n\nSomeone is getting very close to the truth. Choose NOW:\n\nA — THE MASK: 'That wasn't me. Someone else wore my mask.'\n\nB — THE PAINTING: Redirect everything to the stolen painting. Aggressive, fast, convincing.\n\nC — THE BREAKDOWN: Become emotional. Overwhelmed. Nobody suspects those who cry.\n\nD — THE COUNTER-ACCUSATION: Immediately accuse someone else — specifically, with a true detail.\n\nE — THE CONFESSION: Confess something harmless but incriminating — a small mistake, a lie. Distract.\n\n60 seconds. Now.",
            }, "game_effect": "panic_triggered"
        },

        # ── ZUFALLS-MOMENTE (8 Stück) ────────────────────────────────────────

        "random_gondola_knock": {
            "trigger_phase": 2, "trigger_condition": "random_post_murder",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "🚣 ES KLOPFT: Der Host klopft dreimal ans Fenster oder die Tür. Alle halten inne. Sag: 'Eine Gondel wartet draußen. Für jemanden.' Stille. Wer steht auf?",
                "en": "🚣 KNOCKING: The host knocks three times on the window or door. Everyone stops. Say: 'A gondola waits outside. For someone.' Silence. Who stands up?",
            }, "game_effect": "gondola_knock"
        },

        "random_all_candles_out": {
            "trigger_phase": 2, "trigger_condition": "atmosphere_trigger",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "🕯️ ALLES DUNKEL: Alle Kerzen aus (oder Licht aus) für genau 5 Sekunden. In der Dunkelheit: Wer bewegt sich? Wer greift nach etwas? Wer steht auf? Wenn das Licht angeht — jeder sagt einen Satz was er gesehen hat.",
                "en": "🕯️ ALL DARK: All candles out (or lights off) for exactly 5 seconds. In the dark: who moves? Who reaches for something? Who stands up? When light returns — everyone says one sentence about what they observed.",
            }, "game_effect": "darkness_moment"
        },

        "random_music_stops": {
            "trigger_phase": 2, "trigger_condition": "random_any_time",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "🎵 DIE MUSIK VERSTUMMT: Der Host stoppt jede Musik oder klopft dreimal. 10 Sekunden Stille. Dann jeder reihum — GENAU EIN SATZ — was er gerade denkt. Kein Herumreden.",
                "en": "🎵 THE MUSIC STOPS: The host stops any music or knocks three times. 10 seconds of silence. Then everyone in turn — EXACTLY ONE SENTENCE — what they are thinking right now. No talking around it.",
            }, "game_effect": "truth_moment"
        },

        "random_phone_buzz": {
            "trigger_phase": 2, "trigger_condition": "random_any_time",
            "assigned_to": "random",
            "instruction": {
                "de": "📱 GEHEIME NACHRICHT: Schau heimlich auf dein Telefon. Dann weg damit. Sage nur: 'Entschuldigung.' Wer sofort neugierig wird hat etwas zu verbergen — oder zu finden.",
                "en": "📱 SECRET MESSAGE: Look secretly at your phone. Then put it away. Say only: 'Excuse me.' Whoever immediately becomes curious has something to hide — or to find.",
            }, "game_effect": "mysterious_message"
        },

        "random_candle_one_out": {
            "trigger_phase": 2, "trigger_condition": "random_investigation",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "🕯️ EINE KERZE ERLISCHT: Der Host lässt eine Kerze erlöschen (Luft drüber). In diesem Moment flüstert jeder der Person neben sich einen Satz. Irgendwas. Was auch immer einem gerade in den Sinn kommt.",
                "en": "🕯️ ONE CANDLE GOES OUT: The host extinguishes one candle (blow air over it). In this moment everyone whispers one sentence to the person next to them. Anything. Whatever comes to mind.",
            }, "game_effect": "candle_whisper_moment"
        },

        "random_water_sound": {
            "trigger_phase": 2, "trigger_condition": "random_late",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "🌊 DAS WASSER: Der Host sagt: 'Stellt euch vor ihr hört die Gondeln auf dem Canal Grande.' 10 Sekunden Stille. Dann: Jeder sagt ob er am Abend irgendwann den Palazzo verlassen hat — kurz oder lang.",
                "en": "🌊 THE WATER: The host says: 'Imagine you hear the gondolas on the Grand Canal.' 10 seconds of silence. Then: everyone says if they left the palazzo at any point during the evening — briefly or long.",
            }, "game_effect": "alibis_checked"
        },

        "random_fog_moment": {
            "trigger_phase": 3, "trigger_condition": "reckoning_near",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "🌫️ DER NEBEL: Der Host sagt: 'Venedig liegt im Nebel. Die Wahrheit auch — fast.' Alle schreiben jetzt auf einen Zettel wer ihrer Meinung nach der Mörder ist. Faltet ihn. Gebt ihn dem Host. Noch kein Ergebnis.",
                "en": "🌫️ THE FOG: The host says: 'Venice lies in fog. So does the truth — almost.' Everyone now writes on a note who they believe the murderer is. Fold it. Give it to the host. No result yet.",
            }, "game_effect": "pre_final_vote"
        },

        "random_final_silence": {
            "trigger_phase": 3, "trigger_condition": "before_accusation",
            "assigned_to": "all", "broadcast": True,
            "instruction": {
                "de": "🕯️ DIE LETZTE STILLE: Alle schweigen 30 Sekunden. Keine Ausnahme. In dieser Stille: Der Mörder darf die Maske mental ablegen. Die anderen dürfen einander ansehen — ohne zu reden.",
                "en": "🕯️ THE FINAL SILENCE: Everyone is silent for 30 seconds. No exceptions. In this silence: the murderer may mentally remove the mask. The others may look at each other — without speaking.",
            }, "game_effect": "final_silence"
        },

    },

    # ─────────────────────────────────────────────────────────────────────────
    # 14 VERBINDUNGEN
    # ─────────────────────────────────────────────────────────────────────────
    "role_connections": {
        "contessa_spy_affair": {
            "roles": ["contessa", "spy"],
            "connection": "Geheime Affäre. Beide wissen es. Das Alibi füreinander könnte sie retten oder beide ruinieren. Der Gondoliere hat sie einmal zusammen gefahren — ohne Namen zu kennen.",
            "tension": "critical"
        },
        "spy_gondolier_transport": {
            "roles": ["spy", "gondolier"],
            "connection": "Der Gondoliere hat die Agentin einmal gefahren ohne es zu wissen — sie saß maskiert mit einem anderen Namen in seiner Gondel. Er könnte das herausfinden.",
            "tension": "dramatic_irony"
        },
        "spy_investigator_hunter": {
            "roles": ["spy", "investigator"],
            "connection": "Der Ispettore weiß dass La Colomba existiert und im Raum ist. Die Agentin weiß dass der Ispettore sie sucht. Beide wissen voneinander — ohne die Identität des anderen zu kennen.",
            "tension": "extreme"
        },
        "cardinal_shadow_commission": {
            "roles": ["cardinal", "shadow"],
            "connection": "Der Kardinal beauftragte die Schattenfigur das Originalgemälde zu stehlen. Beide kennen die Identität des anderen. Das verbindet sie — und macht beide verletzlich.",
            "tension": "mutual_leverage"
        },
        "shadow_artdealer_painting": {
            "roles": ["shadow", "art_dealer"],
            "connection": "Der Kunsthändler weiß dass jemand das Original hat — aber nicht wer. Die Schattenfigur weiß dass Crane die Fälschung kannte. Sie wissen voneinander ohne es zu wissen.",
            "tension": "dramatic_irony"
        },
        "contessa_doctor_lab": {
            "roles": ["contessa", "doctor"],
            "connection": "Die Contessa war heute Nachmittag im Labor der Ärztin. Die Ärztin hat es im Protokoll. Beide wissen was das bedeuten könnte.",
            "tension": "high"
        },
        "cardinal_singer_note": {
            "roles": ["cardinal", "singer"],
            "connection": "Der Kardinal gab der Sängerin einen ungeöffneten Zettel. Sie trägt ihn. Er enthält etwas das den Kardinal belasten könnte. Die Sängerin weiß nicht was drauf steht.",
            "tension": "one_sided_power"
        },
        "count_murderer": {
            "roles": ["count"],
            "connection": "Der Graf weiß wer ihn getötet hat. Er ist der einzige der es mit Sicherheit weiß. Aber er kann nie direkt reden — nur flüstern.",
            "tension": "extreme"
        },
        "heiress_artdealer_estate": {
            "roles": ["heiress", "art_dealer"],
            "connection": "Beide haben Interesse am Erbe des Grafen — die Erbin als Tochter, der Kunsthändler wegen offener Schulden. Beide wissen dass der andere ein Interesse hat.",
            "tension": "competing_interests"
        },
        "gondolier_murderer_unknowing": {
            "roles": ["gondolier"],
            "connection": "Der Gondoliere sah den Mörder — aber durch die getauschte Maske zeigt sein Zeugnis auf die falsche Person. Er ist unwissender roter Hering.",
            "tension": "dramatic_irony"
        },
        "artdealer_cardinal_unknowing": {
            "roles": ["art_dealer", "cardinal"],
            "connection": "Der Kardinal benutzte den Gemäldediebstahl als Ablenkung. Crane kam wegen des Gemäldes. Beide wissen nicht dass der andere involviert ist.",
            "tension": "parallel_schemes"
        },
        "doctor_murderer_evidence": {
            "roles": ["doctor"],
            "connection": "Die Ärztin hat das Tatmittel in ihrer eigenen Sammlung. Sie ist unwissentlich das Werkzeug des Mörders — oder der Mörder selbst.",
            "tension": "critical"
        },
        "heiress_count_secret": {
            "roles": ["heiress", "count"],
            "connection": "Der Graf ist ihr wahrer Vater. Sie wusste es erst seit heute Nacht. Er wollte es ans Licht bringen. Jemand wollte das verhindern.",
            "tension": "tragic"
        },
        "spy_contessa_alibi": {
            "roles": ["spy", "contessa"],
            "connection": "Die Affäre zwischen Agentin und Contessa gibt beiden ein Alibi — aber nur wenn beide es zugeben. Das ist ein Dilemma: Zugeben bedeutet den anderen zu belasten UND die eigene Position zu schwächen.",
            "tension": "mutual_dilemma"
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # EREIGNISKETTEN
    # ─────────────────────────────────────────────────────────────────────────
    "event_chains": [
        {
            "id": "chain_mask_confusion",
            "trigger": "masks_swapped",
            "message_to_gondolier": {
                "de": "⚠️ Du hast gerade gesehen wie zwei Personen ihre Masken tauschten. Deine Zeugenaussage zeigt damit auf die falsche Person. Was machst du mit diesem Wissen?",
                "en": "⚠️ You just saw two people swap their masks. Your testimony therefore points to the wrong person. What do you do with this knowledge?",
            }
        },
        {
            "id": "chain_painting_pressure",
            "trigger": "painting_theft_revealed",
            "message_to_shadow": {
                "de": "🌑 Das Verschwinden wurde bemerkt. Du hast das Original. Der Druck steigt. Wie lange noch?",
                "en": "🌑 The disappearance was noticed. You have the original. The pressure is rising. How much longer?",
            }
        },
        {
            "id": "chain_cardinal_exposed",
            "trigger": "singer_opens_note",
            "message_to_all": {
                "de": "📜 Die Sängerin öffnet den Zettel des Kardinals. Was steht drauf? Das verändert alles.",
                "en": "📜 The singer opens the Cardinal's note. What does it say? That changes everything.",
            }
        },
        {
            "id": "chain_investigator_presses",
            "trigger": "investigator_uses_ability",
            "message_to_murderer": {
                "de": "⚠️ Der Ispettore führt ein Verhör durch. Wenn er dich wählt — bist du vorbereitet?",
                "en": "⚠️ The Inspector is conducting an interrogation. If he chooses you — are you prepared?",
            }
        },
        {
            "id": "chain_gondolier_silenced",
            "trigger": "murderer_approaches_gondolier",
            "message_to_gondolier": {
                "de": "😰 Jemand hat dir gerade gedroht — subtil, aber du hast es verstanden. Was tust du? Schweigst du? Oder redest du trotzdem?",
                "en": "😰 Someone just threatened you — subtly, but you understood. What do you do? Stay silent? Or speak anyway?",
            }
        },
        {
            "id": "chain_affair_pressure",
            "trigger": "both_spy_contessa_pressured",
            "message_to_spy": {
                "de": "💌 Die Contessa steht unter Druck. Wenn du sie nicht deckst fällt sie — und vielleicht auch du. Gibst du die Affäre zu?",
                "en": "💌 The Contessa is under pressure. If you don't cover for her she falls — and perhaps you too. Do you admit the affair?",
            }
        },
        {
            "id": "chain_two_whispers_noticed",
            "trigger": "two_players_whisper_long",
            "message_to_third": {
                "de": "👁️ {player_a} und {player_b} flüstern seit Minuten. Das ist verdächtig. Rufst du alle zusammen oder beobachtest du weiter?",
                "en": "👁️ {player_a} and {player_b} have been whispering for minutes. That is suspicious. Do you call everyone together or keep observing?",
            }
        }
    ],

    # ─────────────────────────────────────────────────────────────────────────
    # ATMOSPHÄREN-NACHRICHTEN
    # ─────────────────────────────────────────────────────────────────────────
    "atmosphere_messages": [
        {"trigger": "game_start_immediately", "text": {
            "de": "🌊 Venedig, 1895. Der Palazzo Marzano. Ein Maskenball. Kerzenlicht auf dem Wasser. Und irgendwo — liegt ein toter Graf.",
            "en": "🌊 Venice, 1895. Palazzo Marzano. A masquerade ball. Candlelight on the water. And somewhere — a dead Count lies."}},
        {"trigger": "investigation_begins", "text": {
            "de": "🎭 Die Musik hat aufgehört. Die Masken verbergen noch immer Gesichter. Und Geheimnisse.",
            "en": "🎭 The music has stopped. The masks still hide faces. And secrets."}},
        {"trigger": "investigation_10min", "text": {
            "de": "🕯️ Jede Maske lügt. Jedes Geheimnis hat seinen Preis.",
            "en": "🕯️ Every mask lies. Every secret has its price."}},
        {"trigger": "investigation_20min", "text": {
            "de": "🌊 Eine Gondel wartet draußen. Sie wartet schon eine Weile.",
            "en": "🌊 A gondola waits outside. It has been waiting for a while."}},
        {"trigger": "tension_high", "text": {
            "de": "⚡ Venedig kennt viele Geheimnisse. Aber heute Nacht kommt eines ans Licht.",
            "en": "⚡ Venice knows many secrets. But tonight one comes to light."}},
        {"trigger": "reckoning_soon", "text": {
            "de": "🕯️ Die letzte Kerze brennt noch. Wer hat Graf Marzano getötet?",
            "en": "🕯️ The last candle still burns. Who killed Count Marzano?"}}
    ],

    # ─────────────────────────────────────────────────────────────────────────
    # SPIELENDEN (5 Stück)
    # ─────────────────────────────────────────────────────────────────────────
    "endings": {
        "murderer_caught": {
            "condition": "majority_names_murderer_correctly",
            "title": {"de": "Venezianische Gerechtigkeit", "en": "Venetian Justice",
                      "fr": "Justice Vénitienne", "it": "Giustizia Veneziana",
                      "es": "Justicia Veneciana", "pt": "Justiça Veneziana"},
            "text": {"de": "Der Mörder wurde entlarvt — durch Masken die lügen aber Wahrheiten verraten. Graf Marzano ist gerächt. Gewonnen: Alle die korrekt anklagten.",
                     "en": "The murderer was unmasked — through masks that lie but reveal truths. Count Marzano is avenged. Won: Everyone who correctly accused."}
        },
        "murderer_escapes": {
            "condition": "wrong_person_convicted",
            "title": {"de": "Die Gondel fährt ab", "en": "The Gondola Departs",
                      "fr": "La Gondole Part", "it": "La Gondola Parte",
                      "es": "La Góndola Parte", "pt": "A Gôndola Parte"},
            "text": {"de": "Während ihr strittet glitt eine Gondel lautlos davon. Der Mörder ist entkommen. {murderer_name} hat gewonnen.",
                     "en": "While you argued a gondola glided away silently. The murderer has escaped. {murderer_name} has won."}
        },
        "shadow_wins": {
            "condition": "shadow_escapes_with_painting",
            "title": {"de": "La Serenissima ist fort", "en": "La Serenissima is Gone"},
            "text": {"de": "Das Gemälde verschwand in der Nacht. Die Schattenfigur hat gewonnen.",
                     "en": "The painting disappeared in the night. The Shadow figure has won."}
        },
        "perfect_solve": {
            "condition": "doctor_and_investigator_both_correct",
            "title": {"de": "La Verità", "en": "La Verità"},
            "text": {"de": "Die Ärztin und der Ispettore haben gemeinsam das Unmögliche erreicht. Venezianische Vollkommenheit.",
                     "en": "The doctor and the inspector together achieved the impossible. Venetian perfection."}
        },
        "agent_exposed": {
            "condition": "spy_identity_revealed",
            "title": {"de": "La Colomba", "en": "La Colomba"},
            "text": {"de": "Die Agentin wurde entlarvt. Venedig verliert ein Geheimnis das besser vergraben geblieben wäre.",
                     "en": "The agent was exposed. Venice loses a secret that would have been better kept buried."}
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # HOST OBJEKTE
    # ─────────────────────────────────────────────────────────────────────────
    "host_objects": [
        {"object": "masks", "instruction": {"de": "Für jeden Spieler eine Maske (Papier reicht). Verschiedene Farben/Symbole. Rückseite: Rollenfarbe. Extra: Zwei dunkle Masken ohne Zuweisung.", "en": "A mask for each player (paper is fine). Different colors/symbols. Back: role color. Extra: two dark masks without assignment."}},
        {"object": "painting_frame", "instruction": {"de": "Leerer Bilderrahmen oder Zettel 'La Serenissima — Tizian 1573' irgendwo sichtbar aufstellen.", "en": "Empty picture frame or paper 'La Serenissima — Titian 1573' placed somewhere visible."}},
        {"object": "gondolier_note", "instruction": {"de": "Im Badezimmer verstecken: 'Ich sah um 23:15 eine Person mit DUNKLER Maske und GOLDENER RECHTECKIGER SCHNALLE an den Schuhen den Palazzo verlassen. — Marco'", "en": "Hide in bathroom: 'At 11:15pm I saw a person with a DARK mask and GOLD RECTANGULAR BUCKLE on their shoes leave the palazzo. — Marco'"}},
        {"object": "machiavelli_book", "instruction": {"de": "Ein Buch irgendwo hinstellen. Darin Zettel: 'Wer dieses Buch öffnet — prüfe den Boden. — E.M.'", "en": "Place a book somewhere. Inside place a note: 'Whoever opens this book — check the bottom. — E.M.'"}},
        {"object": "sealed_letter_heiress", "instruction": {"de": "Versiegelter Umschlag für Viola: 'Du bist meine Tochter, nicht meine Nichte. Das Testament liegt im Arbeitszimmer, dritte Schublade. — Emilio'", "en": "Sealed envelope for Viola: 'You are my daughter, not my niece. The will is in the study, third drawer. — Emilio'"}},
        {"object": "three_cards_spy", "instruction": {"de": "Drei Visitenkarten mit drei verschiedenen Namen für die Agentin vorbereiten.", "en": "Prepare three business cards with three different names for the agent."}},
        {"object": "cardinal_note_for_singer", "instruction": {"de": "Einen Zettel für den Kardinal vorbereiten der ihn der Sängerin übergeben kann. Inhalt erst während des Spiels: 'Ich war nicht allein im Korridor um 23:15. Es war jemand bei mir. Diese Person weiß was ich tat. — S.F.'", "en": "Prepare a note for the Cardinal to give to the singer. Content during play: 'I was not alone in the corridor at 11:15pm. Someone was with me. That person knows what I did. — S.F.'"}}
    ]
}
