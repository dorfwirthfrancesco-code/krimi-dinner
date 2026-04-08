"""
Dunkelbach Scenario Translations — FR, IT, ES, PT
Applied on top of the base scenario (DE/EN already in dunkelbach.py)
"""

ROLE_TRANSLATIONS = {
    "baron": {
        "name": {
            "fr": "Baron Aldric von Dunkelbach",
            "it": "Barone Aldric von Dunkelbach",
            "es": "Barón Aldric von Dunkelbach",
            "pt": "Barão Aldric von Dunkelbach",
        },
        "intro": {
            "fr": "Je suis le Baron Aldric von Dunkelbach. Je vous ai tous invités parce que ce soir, une vérité longtemps cachée sera révélée. Buvez. Mangez. Et observez-vous.",
            "it": "Sono il Barone Aldric von Dunkelbach. Vi ho invitati tutti perché stanotte una verità nascosta troppo a lungo verrà alla luce. Bevete. Mangiate. E osservatevi.",
            "es": "Soy el Barón Aldric von Dunkelbach. Los he invitado a todos porque esta noche saldrá a la luz una verdad que ha estado oculta demasiado tiempo. Beban. Coman. Y obsérvense.",
            "pt": "Sou o Barão Aldric von Dunkelbach. Convidei todos vocês porque esta noite uma verdade que esteve escondida por muito tempo virá à luz. Bebam. Comam. E observem uns aos outros.",
        },
        "appearance": {
            "fr": "Élégant mais fatigué. Boit son vin très lentement. Porte une bague à sceau qu'il tourne parfois. Sourit rarement — et quand il le fait, seulement avec les yeux.",
            "it": "Elegante ma stanco. Beve il suo vino molto lentamente. Ha un anello con sigillo che a volte gira. Sorride raramente — e quando lo fa, solo con gli occhi.",
            "es": "Elegante pero cansado. Bebe su vino muy lentamente. Lleva un anillo de sello que a veces gira. Sonríe raramente — y cuando lo hace, solo con los ojos.",
            "pt": "Elegante mas cansado. Bebe o seu vinho muito lentamente. Tem um anel com sinete que às vezes gira. Raramente sorri — e quando o faz, apenas com os olhos.",
        },
        "secret": {
            "fr": "Vous savez que quelqu'un à cette table veut vous tuer. C'est pourquoi l'invitation — vous vouliez des témoins. Vos preuves sont dans la bibliothèque. L'app vous dit qui est le meurtrier.",
            "it": "Sai che qualcuno a questo tavolo vuole ucciderti. Ecco perché l'invito — volevi testimoni. Le tue prove sono in biblioteca. L'app ti dice chi è l'assassino.",
            "es": "Sabes que alguien en esta mesa quiere matarte. Por eso la invitación — querías testigos. Tus pruebas están en la biblioteca. La app te dice quién es el asesino.",
            "pt": "Você sabe que alguém nesta mesa quer te matar. É por isso o convite — você queria testemunhas. Suas provas estão na biblioteca. O app te diz quem é o assassino.",
        },
        "ability": {
            "name": {"fr": "Le Fantôme en sait plus", "it": "Il Fantasma sa di più", "es": "El Fantasma sabe más", "pt": "O Fantasma sabe mais"},
            "description": {
                "fr": "Après votre mort, vous continuez à jouer comme fantôme. Vous pouvez murmurer un indice à chaque joueur. Vous pouvez hocher la tête ou la secouer quand on vous pose des questions. Mais jamais un mot à voix haute.",
                "it": "Dopo la tua morte continui a giocare come fantasma. Puoi sussurrare un indizio a ogni giocatore. Puoi annuire o scuotere la testa quando qualcuno ti fa domande. Ma mai una parola ad alta voce.",
                "es": "Después de tu muerte sigues jugando como fantasma. Puedes susurrar una pista a cada jugador. Puedes asentir o negar con la cabeza cuando alguien te pregunta. Pero nunca una palabra en voz alta.",
                "pt": "Após a sua morte você continua jogando como fantasma. Você pode sussurrar uma pista para cada jogador. Você pode acenar com a cabeça ou negar quando alguém te pergunta. Mas nunca uma palavra em voz alta.",
            }
        },
        "win_condition": {
            "fr": "Le meurtrier est arrêté. Vous gagnez même en tant que fantôme.",
            "it": "L'assassino viene catturato. Vinci anche come fantasma.",
            "es": "El asesino es atrapado. Ganas incluso como fantasma.",
            "pt": "O assassino é capturado. Você ganha mesmo como fantasma.",
        },
        "starting_knowledge": {
            "fr": "L'app vous a communiqué le nom du meurtrier. Souvenez-vous-en. Vous ne pouvez jamais le nommer directement. Mais en tant que fantôme vous pouvez murmurer des indices.",
            "it": "L'app ti ha comunicato il nome dell'assassino. Ricordatelo. Non puoi mai nominarlo direttamente. Ma come fantasma puoi sussurrare indizi.",
            "es": "La app te ha comunicado el nombre del asesino. Recuérdalo. Nunca puedes nombrarlo directamente. Pero como fantasma puedes susurrar pistas.",
            "pt": "O app comunicou o nome do assassino. Lembre-se. Você nunca pode nomeá-lo diretamente. Mas como fantasma você pode sussurrar pistas.",
        },
    },
    "butler": {
        "name": {"fr": "Edmund, le Majordome", "it": "Edmund, il Maggiordomo", "es": "Edmund, el Mayordomo", "pt": "Edmund, o Mordomo"},
        "intro": {
            "fr": "Edmund Kraus. Majordome dans cette maison depuis 31 ans. Je connais chaque recoin. Le Baron me faisait confiance. Me faisait confiance.",
            "it": "Edmund Kraus. Maggiordomo in questa casa da 31 anni. Conosco ogni angolo. Il Barone si fidava di me. Si fidava.",
            "es": "Edmund Kraus. Mayordomo en esta casa durante 31 años. Conozco cada rincón. El Barón confiaba en mí. Confiaba.",
            "pt": "Edmund Kraus. Mordomo nesta casa há 31 anos. Conheço cada canto. O Barão confiava em mim. Confiava.",
        },
        "appearance": {
            "fr": "Impeccable. Gants blancs. Se tient toujours légèrement en retrait. Frotte pouce et index ensemble quand il ment.",
            "it": "Impeccabile. Guanti bianchi. Si tiene sempre leggermente in disparte. Strofina pollice e indice insieme quando mente.",
            "es": "Impecable. Guantes blancos. Siempre se mantiene ligeramente apartado. Se frota el pulgar y el índice cuando miente.",
            "pt": "Impecável. Luvas brancas. Sempre se mantém ligeiramente afastado. Esfrega o polegar e o indicador quando mente.",
        },
        "secret": {
            "fr": "J'ai volé 8.400 marks. Le Baron le savait — délai expiré aujourd'hui. J'ai vu quelqu'un dans la bibliothèque cet après-midi qui n'avait rien à y faire.",
            "it": "Ho rubato 8.400 marchi. Il Barone lo sapeva — scadenza oggi. Ho visto qualcuno in biblioteca questo pomeriggio che non aveva niente da fare lì.",
            "es": "Robé 8.400 marcos. El Barón lo sabía — plazo vencido hoy. Vi a alguien en la biblioteca esta tarde que no tenía nada que hacer allí.",
            "pt": "Roubei 8.400 marcos. O Barão sabia — prazo venceu hoje. Vi alguém na biblioteca esta tarde que não tinha nada a fazer lá.",
        },
        "ability": {
            "name": {"fr": "Le Témoin", "it": "Il Testimone", "es": "El Testigo", "pt": "A Testemunha"},
            "description": {
                "fr": "Une fois vous pouvez prétendre avoir 'vu' quelqu'un — heure et lieu. Vrai ou mensonge. Seul vous le savez.",
                "it": "Una volta puoi affermare di aver 'visto' qualcuno — ora e luogo. Vero o bugia. Solo tu lo sai.",
                "es": "Una vez puedes afirmar haber 'visto' a alguien — hora y lugar. Verdad o mentira. Solo tú lo sabes.",
                "pt": "Uma vez você pode afirmar ter 'visto' alguém — hora e lugar. Verdade ou mentira. Só você sabe.",
            }
        },
        "win_condition": {
            "fr": "Survivez sans que votre vol soit prouvé et sans être condamné comme meurtrier.",
            "it": "Sopravvivi senza che il tuo furto venga provato e senza essere condannato come assassino.",
            "es": "Sobrevive sin que tu robo sea probado y sin ser condenado como asesino.",
            "pt": "Sobreviva sem que seu roubo seja provado e sem ser condenado como assassino.",
        },
        "starting_knowledge": {
            "fr": "Vous avez vu quelqu'un dans la bibliothèque entre 16h et 17h. L'app vous dit qui.",
            "it": "Hai visto qualcuno in biblioteca tra le 16 e le 17. L'app ti dice chi.",
            "es": "Viste a alguien en la biblioteca entre las 16 y las 17. La app te dice quién.",
            "pt": "Você viu alguém na biblioteca entre 16h e 17h. O app te diz quem.",
        },
        "murderer_motive_if_assigned": {
            "fr": "Edmund a mélangé de la digitaline du cellier dans le vin du Baron. Clé W-7.",
            "it": "Edmund ha mescolato digitalina dalla cantina nel vino del Barone. Chiave W-7.",
            "es": "Edmund mezcló digitalina de la bodega en el vino del Barón. Llave W-7.",
            "pt": "Edmund misturou digitalina da adega no vinho do Barão. Chave W-7.",
        },
    },
    "niece": {
        "name": {"fr": "Constanze, la Nièce", "it": "Constanze, la Nipote", "es": "Constanze, la Sobrina", "pt": "Constanze, a Sobrinha"},
        "intro": {
            "fr": "Constanze von Dunkelbach. La seule famille que le Baron reconnaît. Je suis ici pour ce qui m'a été promis.",
            "it": "Constanze von Dunkelbach. L'unica famiglia che il Barone riconosce. Sono qui per quello che mi è stato promesso.",
            "es": "Constanze von Dunkelbach. La única familia que el Barón reconoce. Estoy aquí por lo que me fue prometido.",
            "pt": "Constanze von Dunkelbach. A única família que o Barão reconhece. Estou aqui pelo que me foi prometido.",
        },
        "appearance": {
            "fr": "Élégante, tendue. Porte une enveloppe cachetée. Change discrètement de verre.",
            "it": "Elegante, tesa. Porta una busta sigillata. Cambia segretamente bicchiere.",
            "es": "Elegante, tensa. Lleva un sobre sellado. Cambia su copa discretamente.",
            "pt": "Elegante, tensa. Carrega um envelope selado. Muda secretamente de copo.",
        },
        "secret": {
            "fr": "Le testament a changé — j'hérite presque rien. J'étais dans la bibliothèque et je l'ai lu. Le majordome m'a vue.",
            "it": "Il testamento è cambiato — eredito quasi niente. Ero in biblioteca e l'ho letto. Il maggiordomo mi ha visto.",
            "es": "El testamento cambió — heredo casi nada. Estuve en la biblioteca y lo leí. El mayordomo me vio.",
            "pt": "O testamento mudou — herdo quase nada. Estava na biblioteca e li. O mordomo me viu.",
        },
        "ability": {
            "name": {"fr": "La Lettre", "it": "La Lettera", "es": "La Carta", "pt": "A Carta"},
            "description": {
                "fr": "Vous avez une vraie lettre cachetée. Vous décidez quand l'ouvrir. Plus vous attendez, plus vous semblez suspect.",
                "it": "Hai una vera lettera sigillata. Decidi quando aprirla. Più aspetti, più sembri sospettoso.",
                "es": "Tienes una carta sellada real. Decides cuándo abrirla. Cuanto más esperas, más sospechoso pareces.",
                "pt": "Você tem uma carta selada real. Você decide quando abri-la. Quanto mais espera, mais suspeito parece.",
            }
        },
        "win_condition": {
            "fr": "Le nouveau testament ne doit pas être trouvé. S'il est trouvé: nommez le meurtrier en premier.",
            "it": "Il nuovo testamento non deve essere trovato. Se viene trovato: nomina l'assassino per primo.",
            "es": "El nuevo testamento no debe ser encontrado. Si es encontrado: nombra al asesino primero.",
            "pt": "O novo testamento não deve ser encontrado. Se for encontrado: nomeie o assassino primeiro.",
        },
        "starting_knowledge": {
            "fr": "Vous étiez dans la bibliothèque — le testament est derrière les livres de droit, troisième étagère. Le majordome vous a vue.",
            "it": "Eri in biblioteca — il testamento è dietro i libri di diritto, terzo scaffale. Il maggiordomo ti ha visto.",
            "es": "Estuviste en la biblioteca — el testamento está detrás de los libros de derecho, tercer estante. El mayordomo te vio.",
            "pt": "Você estava na biblioteca — o testamento está atrás dos livros de direito, terceira prateleira. O mordomo te viu.",
        },
        "murderer_motive_if_assigned": {
            "fr": "Le nouveau testament aurait détruit Constanze. Dans la bibliothèque elle a trouvé l'occasion.",
            "it": "Il nuovo testamento avrebbe distrutto Constanze. In biblioteca ha trovato l'occasione.",
            "es": "El nuevo testamento habría destruido a Constanze. En la biblioteca encontró la oportunidad.",
            "pt": "O novo testamento teria destruído Constanze. Na biblioteca ela encontrou a oportunidade.",
        },
    },
    "witness": {
        "name": {"fr": "Marta, l'Écrivaine", "it": "Marta, la Scrittrice", "es": "Marta, la Escritora", "pt": "Marta, a Escritora"},
        "intro": {
            "fr": "Marta Stein. J'écris, j'observe, je n'oublie rien. Le Baron connaissait ma mère. Je voulais juste un dîner tranquille.",
            "it": "Marta Stein. Scrivo, osservo, non dimentico niente. Il Barone conosceva mia madre. Volevo solo una cena tranquilla.",
            "es": "Marta Stein. Escribo, observo, no olvido nada. El Barón conocía a mi madre. Solo quería una cena tranquila.",
            "pt": "Marta Stein. Escrevo, observo, não esqueço nada. O Barão conhecia minha mãe. Eu só queria um jantar tranquilo.",
        },
        "appearance": {
            "fr": "Petit carnet dans la poche. Parle peu. Écoute beaucoup. A vu quelque chose qu'elle ne peut pas expliquer.",
            "it": "Piccolo taccuino in tasca. Parla poco. Ascolta molto. Ha visto qualcosa che non riesce a spiegare.",
            "es": "Pequeño cuaderno en el bolsillo. Habla poco. Escucha mucho. Vio algo que no puede explicar.",
            "pt": "Pequeno caderno no bolso. Fala pouco. Ouve muito. Viu algo que não consegue explicar.",
        },
        "secret": {
            "fr": "Juste avant minuit j'ai vu quelque chose par la fenêtre de la bibliothèque. Une silhouette. Quelque chose dans la main. J'ai peur de dire ce que j'ai vu.",
            "it": "Poco prima di mezzanotte ho visto qualcosa attraverso la finestra della biblioteca. Una sagoma. Qualcosa in mano. Ho paura di dire cosa ho visto.",
            "es": "Justo antes de medianoche vi algo por la ventana de la biblioteca. Una silueta. Algo en la mano. Tengo miedo de decir lo que vi.",
            "pt": "Logo antes da meia-noite vi algo pela janela da biblioteca. Uma silhueta. Algo na mão. Tenho medo de dizer o que vi.",
        },
        "ability": {
            "name": {"fr": "La Mémoire s'aiguise", "it": "La Memoria si affina", "es": "La Memoria se agudiza", "pt": "A Memória se aguça"},
            "description": {
                "fr": "Chaque fois que vous dites quelque chose de vrai, votre mémoire s'affine. L'app vous donne automatiquement des indices plus précis. Le silence vous protège mais vous rend aveugle.",
                "it": "Ogni volta che dici qualcosa di vero, la tua memoria si affina. L'app ti dà automaticamente indizi più precisi. Il silenzio ti protegge ma ti rende cieco.",
                "es": "Cada vez que dices algo verdadero, tu memoria se agudiza. La app te da automáticamente pistas más precisas. El silencio te protege pero te vuelve ciego.",
                "pt": "Cada vez que você diz algo verdadeiro, sua memória se aguça. O app automaticamente te dá pistas mais precisas. O silêncio te protege mas te torna cego.",
            }
        },
        "win_condition": {
            "fr": "Si vous nommez la bonne personne à la fin ET prouvez ce que vous avez vu, vous gagnez seul.",
            "it": "Se alla fine nomini la persona giusta E provi quello che hai visto, vinci da solo.",
            "es": "Si al final nombras a la persona correcta Y pruebas lo que viste, ganas solo.",
            "pt": "Se no final você nomear a pessoa certa E provar o que viu, você ganha sozinho.",
        },
        "starting_knowledge": {
            "fr": "Vous avez vu une silhouette. Quelque chose de long et mince dans la main droite. Vous ne savez pas encore qui c'était.",
            "it": "Hai visto una sagoma. Qualcosa di lungo e sottile nella mano destra. Non sai ancora chi era.",
            "es": "Viste una silueta. Algo largo y delgado en la mano derecha. Aún no sabes quién era.",
            "pt": "Você viu uma silhueta. Algo longo e fino na mão direita. Você ainda não sabe quem era.",
        },
    },
    "doctor": {
        "name": {"fr": "Dr. Heinrich Voss", "it": "Dr. Heinrich Voss", "es": "Dr. Heinrich Voss", "pt": "Dr. Heinrich Voss"},
        "intro": {
            "fr": "Dr. Heinrich Voss. Le Baron était mon patient et mon ami. J'aurais dû l'empêcher.",
            "it": "Dr. Heinrich Voss. Il Barone era il mio paziente e il mio amico. Avrei dovuto impedirlo.",
            "es": "Dr. Heinrich Voss. El Barón era mi paciente y mi amigo. Debería haberlo impedido.",
            "pt": "Dr. Heinrich Voss. O Barão era meu paciente e meu amigo. Eu deveria ter impedido.",
        },
        "appearance": {
            "fr": "Calme. Professionnel. Toujours sa sacoche médicale. Pâlit quand quelqu'un mentionne le poison.",
            "it": "Calmo. Professionale. Ha sempre la sua borsa medica. Diventa pallido quando qualcuno menziona il veleno.",
            "es": "Tranquilo. Profesional. Siempre tiene su maletín médico. Palidece cuando alguien menciona veneno.",
            "pt": "Calmo. Profissional. Sempre tem sua bolsa médica. Fica pálido quando alguém menciona veneno.",
        },
        "secret": {
            "fr": "Il y a deux ans j'ai prescrit le mauvais médicament au Baron. Ce soir il m'a informé: il a déposé une plainte. Ma carrière est terminée — sauf s'il la retire.",
            "it": "Due anni fa ho prescritto il farmaco sbagliato al Barone. Stasera mi ha informato: ha presentato un reclamo. La mia carriera è finita — a meno che non lo ritiri.",
            "es": "Hace dos años prescribí el medicamento equivocado al Barón. Esta noche me informó: ha presentado una queja. Mi carrera ha terminado — a menos que la retire.",
            "pt": "Há dois anos prescrevi o medicamento errado para o Barão. Esta noite ele me informou: apresentou uma queixa. Minha carreira acabou — a menos que ele a retire.",
        },
        "ability": {
            "name": {"fr": "Le Diagnostic", "it": "La Diagnosi", "es": "El Diagnóstico", "pt": "O Diagnóstico"},
            "description": {
                "fr": "Seul vous pouvez déterminer la cause du décès. Votre déclaration est officielle. Vous pouvez mentir.",
                "it": "Solo tu puoi determinare la causa della morte. La tua dichiarazione è ufficiale. Puoi mentire.",
                "es": "Solo tú puedes determinar la causa de la muerte. Tu declaración es oficial. Puedes mentir.",
                "pt": "Só você pode determinar a causa da morte. Sua declaração é oficial. Você pode mentir.",
            }
        },
        "win_condition": {
            "fr": "Nommez la bonne cause et le bon meurtrier: titre honorifique Grand Détective.",
            "it": "Nomina la causa corretta e il giusto assassino: titolo onorario Grande Detective.",
            "es": "Nombra la causa correcta y el asesino correcto: título honorífico Gran Detective.",
            "pt": "Nomeie a causa correta e o assassino correto: título honorário Grande Detetive.",
        },
        "starting_knowledge": {
            "fr": "Le Baron avait une maladie cardiaque. Ses médicaments — à mauvaise dose — pourraient être mortels. Seul vous savez cela.",
            "it": "Il Barone aveva una malattia cardiaca. I suoi farmaci — a dosaggio sbagliato — potrebbero essere letali. Solo tu lo sai.",
            "es": "El Barón tenía una enfermedad cardíaca. Sus medicamentos — a dosis incorrecta — podrían ser letales. Solo tú sabes esto.",
            "pt": "O Barão tinha uma doença cardíaca. Seus medicamentos — na dosagem errada — poderiam ser letais. Só você sabe disso.",
        },
        "murderer_motive_if_assigned": {
            "fr": "Heinrich a tué le Baron avec une surdose de ses propres médicaments cardiaques. Presque parfait.",
            "it": "Heinrich ha ucciso il Barone con una sovradose dei suoi farmaci cardiaci. Quasi perfetto.",
            "es": "Heinrich mató al Barón con una sobredosis de sus propios medicamentos cardíacos. Casi perfecto.",
            "pt": "Heinrich matou o Barão com uma overdose dos seus próprios medicamentos cardíacos. Quase perfeito.",
        },
    },
    "cook": {
        "name": {"fr": "Rosa, la Cuisinière", "it": "Rosa, la Cuoca", "es": "Rosa, la Cocinera", "pt": "Rosa, a Cozinheira"},
        "intro": {
            "fr": "Rosa Müller. Cuisinière ici depuis huit ans. J'ai cuisiné le dîner. J'ai tout vu. Je ne dis rien.",
            "it": "Rosa Müller. Cuoca qui da otto anni. Ho cucinato la cena. Ho visto tutto. Non dico niente.",
            "es": "Rosa Müller. Cocinera aquí desde hace ocho años. Cociné la cena. Vi todo. No digo nada.",
            "pt": "Rosa Müller. Cozinheira aqui há oito anos. Cozinhei o jantar. Vi tudo. Não digo nada.",
        },
        "appearance": {
            "fr": "Nerveuse. Mains toujours en mouvement. Touche constamment le crucifix autour de son cou. Évite le contact visuel.",
            "it": "Nervosa. Mani sempre in movimento. Tocca costantemente il crocifisso al collo. Evita il contatto visivo.",
            "es": "Nerviosa. Manos siempre en movimiento. Toca constantemente el crucifijo alrededor de su cuello. Evita el contacto visual.",
            "pt": "Nervosa. Mãos sempre em movimento. Toca constantemente o crucifixo ao redor do pescoço. Evita contato visual.",
        },
        "secret": {
            "fr": "Quelqu'un m'a demandé cet après-midi de mettre quelque chose dans la nourriture du Baron. Je pensais que c'était sans danger. J'ai reçu 200 marks.",
            "it": "Qualcuno mi ha chiesto questo pomeriggio di mettere qualcosa nel cibo del Barone. Pensavo fosse innocuo. Ho ricevuto 200 marchi.",
            "es": "Alguien me pidió esta tarde que pusiera algo en la comida del Barón. Pensé que era inofensivo. Recibí 200 marcos.",
            "pt": "Alguém me pediu esta tarde para colocar algo na comida do Barão. Pensei que era inofensivo. Recebi 200 marcos.",
        },
        "ability": {
            "name": {"fr": "La Confession", "it": "La Confessione", "es": "La Confesión", "pt": "A Confissão"},
            "description": {
                "fr": "Une fois vous pouvez révéler qui vous a engagé. Mais vous ne connaissez que le nom — pas s'il est le vrai meurtrier.",
                "it": "Una volta puoi rivelare chi ti ha assunto. Ma conosci solo il nome — non se è il vero assassino.",
                "es": "Una vez puedes revelar quién te contrató. Pero solo conoces el nombre — no si es el verdadero asesino.",
                "pt": "Uma vez você pode revelar quem te contratou. Mas você só conhece o nome — não se é o verdadeiro assassino.",
            }
        },
        "win_condition": {
            "fr": "Survivez si vous dites la vérité OU si personne ne découvre ce que vous avez fait.",
            "it": "Sopravvivi se dici la verità O se nessuno scopre cosa hai fatto.",
            "es": "Sobrevive si dices la verdad O si nadie descubre lo que hiciste.",
            "pt": "Sobreviva se disser a verdade OU se ninguém descobrir o que você fez.",
        },
        "starting_knowledge": {
            "fr": "Vous savez ce que vous avez donné au Baron. Vous ne savez pas si ça l'a tué. L'app vous dit qui vous a engagé.",
            "it": "Sai cosa hai dato al Barone. Non sai se l'ha ucciso. L'app ti dice chi ti ha assunto.",
            "es": "Sabes lo que le diste al Barón. No sabes si lo mató. La app te dice quién te contrató.",
            "pt": "Você sabe o que deu ao Barão. Você não sabe se o matou. O app te diz quem te contratou.",
        },
        "murderer_motive_if_assigned": {
            "fr": "Rosa aimait le Baron mais il la traitait comme un meuble. Elle a empoisonné sa nourriture elle-même.",
            "it": "Rosa amava il Barone ma lui la trattava come un mobile. Ha avvelenato il suo cibo da sola.",
            "es": "Rosa amaba al Barón pero él la trataba como un mueble. Envenenó su comida ella misma.",
            "pt": "Rosa amava o Barão mas ele a tratava como mobília. Ela envenenou a comida dele sozinha.",
        },
    },
    "stranger": {
        "name": {"fr": "L'Inconnu", "it": "Lo Straniero", "es": "El Desconocido", "pt": "O Estranho"},
        "intro": {
            "fr": "Je ne révèle pas mon nom. Le Baron savait qui je suis. Les autres l'apprendront quand je le jugerai bon.",
            "it": "Non rivelo il mio nome. Il Barone sapeva chi sono. Gli altri lo scopriranno quando lo riterrò opportuno.",
            "es": "No revelo mi nombre. El Barón sabía quién soy. Los demás lo sabrán cuando lo considere oportuno.",
            "pt": "Não revelo meu nome. O Barão sabia quem eu sou. Os outros vão descobrir quando eu julgar adequado.",
        },
        "appearance": {
            "fr": "Discret — ce qui est remarquable. A une carte de visite avec seulement un numéro. Parle rarement, très précisément.",
            "it": "Discreto — il che è notevole. Ha un biglietto da visita con solo un numero. Parla raramente, molto precisamente.",
            "es": "Discreto — lo cual es llamativo. Tiene una tarjeta de visita con solo un número. Habla raramente, muy precisamente.",
            "pt": "Discreto — o que é notável. Tem um cartão de visita com apenas um número. Fala raramente, muito precisamente.",
        },
        "secret": {
            "fr": "Je suis détective privé. Le Baron m'a engagé pour surveiller quelqu'un à cette table. Je ne peux pas nommer mon client.",
            "it": "Sono un detective privato. Il Barone mi ha assunto per sorvegliare qualcuno a questo tavolo. Non posso nominare il mio cliente.",
            "es": "Soy detective privado. El Barón me contrató para vigilar a alguien en esta mesa. No puedo nombrar a mi cliente.",
            "pt": "Sou detetive particular. O Barão me contratou para vigiar alguém nesta mesa. Não posso nomear meu cliente.",
        },
        "ability": {
            "name": {"fr": "Le Dossier", "it": "Il Fascicolo", "es": "El Expediente", "pt": "O Dossiê"},
            "description": {
                "fr": "Vous avez un dossier sur une personne. Vous pouvez transmettre des indices anonymement — mais jamais directement.",
                "it": "Hai un fascicolo su una persona. Puoi trasmettere indizi anonimamente — ma mai direttamente.",
                "es": "Tienes un expediente sobre una persona. Puedes transmitir pistas anónimamente — pero nunca directamente.",
                "pt": "Você tem um dossiê sobre uma pessoa. Você pode transmitir pistas anonimamente — mas nunca diretamente.",
            }
        },
        "win_condition": {
            "fr": "Le vrai meurtrier est arrêté. Mais vous perdez si la personne que vous surveillez est injustement condamnée.",
            "it": "Il vero assassino viene catturato. Ma perdi se la persona che stavi sorvegliando viene ingiustamente condannata.",
            "es": "El verdadero asesino es atrapado. Pero pierdes si la persona que vigilabas es injustamente condenada.",
            "pt": "O verdadeiro assassino é capturado. Mas você perde se a pessoa que estava vigiando for injustamente condenada.",
        },
        "starting_knowledge": {
            "fr": "L'app vous dit qui vous surveillez. Vous avez un dossier avec trois secrets sur cette personne.",
            "it": "L'app ti dice chi stai sorvegliando. Hai un fascicolo con tre segreti su questa persona.",
            "es": "La app te dice a quién estás vigilando. Tienes un expediente con tres secretos sobre esa persona.",
            "pt": "O app te diz quem você está vigiando. Você tem um dossiê com três segredos sobre essa pessoa.",
        },
        "murderer_motive_if_assigned": {
            "fr": "L'Inconnu a découvert que le Baron planifiait de le ruiner. Il a agi en premier.",
            "it": "Lo Straniero ha scoperto che il Barone pianificava di rovinarlo. Ha agito per primo.",
            "es": "El Desconocido descubrió que el Barón planeaba arruinarlo. Actuó primero.",
            "pt": "O Estranho descobriu que o Barão planejava arruiná-lo. Agiu primeiro.",
        },
    },
    "detective": {
        "name": {"fr": "Inspecteur Karl Wahl", "it": "Ispettore Karl Wahl", "es": "Inspector Karl Wahl", "pt": "Inspetor Karl Wahl"},
        "intro": {
            "fr": "Inspecteur Karl Wahl, Police Criminelle Munich. J'étais déjà en route quand j'ai reçu la nouvelle. Le Baron m'avait convoqué. Il avait peur.",
            "it": "Ispettore Karl Wahl, Polizia Criminale Monaco. Ero già in viaggio quando ho ricevuto la notizia. Il Barone mi aveva convocato. Aveva paura.",
            "es": "Inspector Karl Wahl, Policía Criminal de Múnich. Ya estaba en camino cuando recibí la noticia. El Barón me había convocado. Tenía miedo.",
            "pt": "Inspetor Karl Wahl, Polícia Criminal de Munique. Já estava a caminho quando recebi a notícia. O Barão tinha me convocado. Ele estava com medo.",
        },
        "appearance": {
            "fr": "Pas de tenue de soirée. Note tout. Des yeux froids qui n'oublient rien.",
            "it": "Niente abito da sera. Scrive tutto. Occhi freddi che non dimenticano niente.",
            "es": "Sin traje de noche. Anota todo. Ojos fríos que no olvidan nada.",
            "pt": "Sem traje de noite. Anota tudo. Olhos frios que não esquecem nada.",
        },
        "secret": {
            "fr": "Le Baron m'a écrit: il craint quelqu'un à cette table. Un nom. J'ai la lettre — mais je ne peux pas encore la montrer.",
            "it": "Il Barone mi ha scritto: teme qualcuno a questo tavolo. Un nome. Ho la lettera — ma non posso ancora mostrarla.",
            "es": "El Barón me escribió: teme a alguien en esta mesa. Un nombre. Tengo la carta — pero aún no puedo mostrarla.",
            "pt": "O Barão me escreveu: ele teme alguém nesta mesa. Um nome. Tenho a carta — mas ainda não posso mostrá-la.",
        },
        "ability": {
            "name": {"fr": "L'Interrogatoire", "it": "L'Interrogatorio", "es": "El Interrogatorio", "pt": "O Interrogatório"},
            "description": {
                "fr": "Une fois vous pouvez convoquer un interrogatoire officiel. Tout le monde quitte la pièce — vous parlez seul avec une personne pendant 2 minutes.",
                "it": "Una volta puoi convocare un interrogatorio ufficiale. Tutti escono dalla stanza — parli da solo con una persona per 2 minuti.",
                "es": "Una vez puedes convocar un interrogatorio oficial. Todos salen de la habitación — hablas solo con una persona durante 2 minutos.",
                "pt": "Uma vez você pode convocar um interrogatório oficial. Todos saem da sala — você fala sozinho com uma pessoa por 2 minutos.",
            }
        },
        "win_condition": {
            "fr": "Vous gagnez seulement si VOUS êtes le premier à nommer officiellement et correctement le meurtrier — avec des preuves.",
            "it": "Vinci solo se SEI il primo a nominare ufficialmente e correttamente l'assassino — con prove.",
            "es": "Ganas solo si TÚ eres el primero en nombrar oficial y correctamente al asesino — con pruebas.",
            "pt": "Você ganha apenas se VOCÊ for o primeiro a nomear oficial e corretamente o assassino — com provas.",
        },
        "starting_knowledge": {
            "fr": "Le Baron vous a écrit un nom. L'app vous le montre — mais ce nom n'est pas forcément le meurtrier. 70% de chance.",
            "it": "Il Barone ti ha scritto un nome. L'app te lo mostra — ma questo nome non è necessariamente l'assassino. 70% di probabilità.",
            "es": "El Barón te escribió un nombre. La app te lo muestra — pero ese nombre no es necesariamente el asesino. 70% de probabilidad.",
            "pt": "O Barão escreveu um nome para você. O app te mostra — mas esse nome não é necessariamente o assassino. 70% de chance.",
        },
    },
    "lover": {
        "name": {"fr": "Viktor Reiss, l'Associé", "it": "Viktor Reiss, il Socio", "es": "Viktor Reiss, el Socio", "pt": "Viktor Reiss, o Sócio"},
        "intro": {
            "fr": "Viktor Reiss. Associé commercial du Baron. Nous nous connaissions très bien. Trop bien peut-être.",
            "it": "Viktor Reiss. Socio commerciale del Barone. Ci conoscevamo molto bene. Forse troppo.",
            "es": "Viktor Reiss. Socio comercial del Barón. Nos conocíamos muy bien. Quizás demasiado.",
            "pt": "Viktor Reiss. Sócio comercial do Barão. Nos conhecíamos muito bem. Talvez bem demais.",
        },
        "appearance": {
            "fr": "Charmant. A un mouchoir monogrammé. Rougit quand certains noms sont mentionnés.",
            "it": "Affascinante. Ha un fazzoletto con monogramma. Diventa rosso quando vengono menzionati certi nomi.",
            "es": "Encantador. Tiene un pañuelo con monograma. Se ruboriza cuando se mencionan ciertos nombres.",
            "pt": "Charmoso. Tem um lenço monogramado. Fica vermelho quando certos nomes são mencionados.",
        },
        "secret": {
            "fr": "Viktor et une autre personne à table ont une liaison secrète. Son alibi — il n'était pas seul à minuit — ne peut être prouvé que si l'autre personne avoue.",
            "it": "Viktor e un'altra persona al tavolo hanno una relazione segreta. Il suo alibi — non era solo a mezzanotte — può essere provato solo se l'altra persona ammette la relazione.",
            "es": "Viktor y otra persona en la mesa tienen una aventura secreta. Su coartada — no estaba solo a medianoche — solo puede probarse si la otra persona admite la aventura.",
            "pt": "Viktor e outra pessoa na mesa têm um caso secreto. Seu álibi — ele não estava sozinho à meia-noite — só pode ser provado se a outra pessoa admitir o caso.",
        },
        "ability": {
            "name": {"fr": "L'Alibi", "it": "L'Alibi", "es": "La Coartada", "pt": "O Álibi"},
            "description": {
                "fr": "Vous pouvez demander à votre partenaire secret via message app de confirmer votre alibi — une fois. Il décide s'il vous couvre.",
                "it": "Puoi chiedere al tuo partner segreto tramite messaggio nell'app di confermare il tuo alibi — una volta. Lui decide se coprirti.",
                "es": "Puedes pedir a tu pareja secreta a través de mensaje en la app que confirme tu coartada — una vez. Él/ella decide si te cubre.",
                "pt": "Você pode pedir ao seu parceiro secreto via mensagem no app para confirmar seu álibi — uma vez. Ele decide se vai te cobrir.",
            }
        },
        "win_condition": {
            "fr": "Survivez si votre alibi est confirmé OU si le vrai meurtrier est arrêté sans que votre liaison soit révélée.",
            "it": "Sopravvivi se il tuo alibi è confermato O se il vero assassino viene catturato senza che la tua relazione sia rivelata.",
            "es": "Sobrevive si tu coartada es confirmada O si el verdadero asesino es atrapado sin que tu aventura sea revelada.",
            "pt": "Sobreviva se seu álibi for confirmado OU se o verdadeiro assassino for capturado sem que seu caso seja revelado.",
        },
        "starting_knowledge": {
            "fr": "L'app vous dit à vous et à votre amant(e) qui est votre partenaire mutuel. Gardez-le secret.",
            "it": "L'app dice a te e al tuo amante chi è il vostro partner reciproco. Tenetelo segreto.",
            "es": "La app les dice a ti y a tu amante quién es su pareja mutua. Mantenlo en secreto.",
            "pt": "O app diz a você e ao seu amante quem é o parceiro mútuo de vocês. Mantenha em segredo.",
        },
        "murderer_motive_if_assigned": {
            "fr": "Le Baron a découvert la liaison et a menacé de la rendre publique. Viktor ne pouvait pas le permettre.",
            "it": "Il Barone ha scoperto la relazione e ha minacciato di renderla pubblica. Viktor non poteva permetterlo.",
            "es": "El Barón descubrió la aventura y amenazó con hacerla pública. Viktor no podía permitirlo.",
            "pt": "O Barão descobriu o caso e ameaçou torná-lo público. Viktor não podia permitir isso.",
        },
    },
    "shadow": {
        "name": {"fr": "L'Ombre", "it": "L'Ombra", "es": "La Sombra", "pt": "A Sombra"},
        "intro": {
            "fr": "Je suis... personne de spécial. Un invité. Oubliez-moi.",
            "it": "Sono... nessuno di speciale. Un ospite. Dimenticatemi.",
            "es": "Soy... nadie especial. Un invitado. Olvídenme.",
            "pt": "Sou... ninguém especial. Um convidado. Esqueçam-me.",
        },
        "appearance": {
            "fr": "Discret — intentionnellement. Observe tout très attentivement.",
            "it": "Discreto — intenzionalmente. Osserva tutto molto attentamente.",
            "es": "Discreto — intencionalmente. Observa todo muy atentamente.",
            "pt": "Discreto — intencionalmente. Observa tudo muito atentamente.",
        },
        "secret": {
            "fr": "Vous êtes un maître chanteur. Vous avez des informations compromettantes sur trois personnes à table. Vous voulez voler le testament.",
            "it": "Sei un ricattatore. Hai informazioni compromettenti su tre persone al tavolo. Vuoi rubare il testamento.",
            "es": "Eres un chantajista. Tienes información comprometedora sobre tres personas en la mesa. Quieres robar el testamento.",
            "pt": "Você é um chantagista. Tem informações comprometedoras sobre três pessoas na mesa. Quer roubar o testamento.",
        },
        "ability": {
            "name": {"fr": "Voler le Testament", "it": "Rubare il Testamento", "es": "Robar el Testamento", "pt": "Roubar o Testamento"},
            "description": {
                "fr": "Si vous savez où est le testament, vous pouvez sélectionner 'Voler le testament' dans l'app. Non découvert: vous gagnez immédiatement.",
                "it": "Se sai dove si trova il testamento, puoi selezionare 'Ruba il testamento' nell'app. Non scoperto: vinci immediatamente.",
                "es": "Si sabes dónde está el testamento, puedes seleccionar 'Robar testamento' en la app. Sin ser descubierto: ganas inmediatamente.",
                "pt": "Se você sabe onde está o testamento, pode selecionar 'Roubar testamento' no app. Sem ser descoberto: você ganha imediatamente.",
            }
        },
        "win_condition": {
            "fr": "Voler le testament sans être découvert. C'est très difficile.",
            "it": "Rubare il testamento senza essere scoperto. È molto difficile.",
            "es": "Robar el testamento sin ser descubierto. Es muy difícil.",
            "pt": "Roubar o testamento sem ser descoberto. É muito difícil.",
        },
        "starting_knowledge": {
            "fr": "Vous avez des informations sur trois personnes. L'app vous les montre en privé.",
            "it": "Hai informazioni su tre persone. L'app te le mostra in privato.",
            "es": "Tienes información sobre tres personas. La app te la muestra en privado.",
            "pt": "Você tem informações sobre três pessoas. O app te mostra em privado.",
        },
    },
}

CLUE_TRANSLATIONS = {
    "key_cellar": {
        "name": {"fr": "Clé W-7", "it": "Chiave W-7", "es": "Llave W-7", "pt": "Chave W-7"},
        "text": {
            "fr": "Une vieille clé en laiton. Au dos: 'W-7'. La cave à vin. Pourquoi quelqu'un aurait-il eu besoin de cette clé ce soir?",
            "it": "Una vecchia chiave di ottone. Sul retro: 'W-7'. La cantina del vino. Perché qualcuno avrebbe avuto bisogno di questa chiave stanotte?",
            "es": "Una vieja llave de latón. En la parte trasera: 'W-7'. La bodega. ¿Por qué alguien habría necesitado esta llave esta noche?",
            "pt": "Uma velha chave de latão. No verso: 'W-7'. A adega. Por que alguém precisaria desta chave esta noite?",
        }
    },
    "household_ledger": {
        "name": {"fr": "Le Livre de Comptes", "it": "Il Libro Contabile", "es": "El Libro de Cuentas", "pt": "O Livro de Contas"},
        "text": {
            "fr": "Page 47: corrections à l'encre différente. 8.400 marks manquants sur trois ans.",
            "it": "Pagina 47: correzioni con inchiostro diverso. 8.400 marchi mancanti in tre anni.",
            "es": "Página 47: correcciones con tinta diferente. 8.400 marcos faltantes en tres años.",
            "pt": "Página 47: correções com tinta diferente. 8.400 marcos faltando em três anos.",
        }
    },
    "sealed_letter": {
        "name": {"fr": "La Lettre Cachetée", "it": "La Lettera Sigillata", "es": "La Carta Sellada", "pt": "A Carta Selada"},
        "text": {
            "fr": "Contenu à l'ouverture: 'Constanze — La vérité sur ta mère est derrière Schiller. — Aldric'",
            "it": "Contenuto all'apertura: 'Constanze — La verità su tua madre è dietro Schiller. — Aldric'",
            "es": "Contenido al abrir: 'Constanze — La verdad sobre tu madre está detrás de Schiller. — Aldric'",
            "pt": "Conteúdo ao abrir: 'Constanze — A verdade sobre sua mãe está atrás de Schiller. — Aldric'",
        }
    },
    "cause_of_death": {
        "name": {"fr": "Cause du Décès", "it": "Causa della Morte", "es": "Causa de la Muerte", "pt": "Causa da Morte"},
        "text": {
            "fr": "Insuffisance cardiaque — mais pupilles dilatées. Pas typique. Surdose de digitaline.",
            "it": "Insufficienza cardiaca — ma pupille dilatate. Non tipico. Sovradose di digitalina.",
            "es": "Insuficiencia cardíaca — pero pupilas dilatadas. No típico. Sobredosis de digitalina.",
            "pt": "Insuficiência cardíaca — mas pupilas dilatadas. Não típico. Overdose de digitalina.",
        }
    },
    "kitchen_substance": {
        "name": {"fr": "Le Paquet de la Cuisine", "it": "Il Pacchetto della Cucina", "es": "El Paquete de la Cocina", "pt": "O Pacote da Cozinha"},
        "text": {
            "fr": "Poudre blanche. Inodore. La cuisinière dit: 'Un tonique cardiaque.' Le médecin sait: c'est de la digitaline.",
            "it": "Polvere bianca. Inodore. La cuoca dice: 'Un tonico cardiaco.' Il dottore sa: è digitalina.",
            "es": "Polvo blanco. Inodoro. La cocinera dice: 'Un tónico cardíaco.' El médico sabe: es digitalina.",
            "pt": "Pó branco. Inodoro. A cozinheira diz: 'Um tônico cardíaco.' O médico sabe: é digitalina.",
        }
    },
    "payment_receipt": {
        "name": {"fr": "Reçu: 200 Marks", "it": "Ricevuta: 200 Marchi", "es": "Recibo: 200 Marcos", "pt": "Recibo: 200 Marcos"},
        "text": {
            "fr": "Pas de nom. Date: aujourd'hui. Écriture d'auberge de Munich.",
            "it": "Nessun nome. Data: oggi. Scrittura di locanda di Monaco.",
            "es": "Sin nombre. Fecha: hoy. Escritura de posada de Múnich.",
            "pt": "Sem nome. Data: hoje. Caligrafia de estalagem de Munique.",
        }
    },
    "medical_bag": {
        "name": {"fr": "La Sacoche Médicale", "it": "La Borsa Medica", "es": "El Maletín Médico", "pt": "A Bolsa Médica"},
        "text": {
            "fr": "Une seringue manque. La boîte de digitaline est ouverte — deux comprimés manquants.",
            "it": "Manca una siringa. La scatola di digitalina è aperta — due compresse mancanti.",
            "es": "Falta una jeringa. La caja de digitalina está abierta — faltan dos comprimidos.",
            "pt": "Uma seringa faltando. A caixa de digitalina está aberta — dois comprimidos faltando.",
        }
    },
    "barons_evidence": {
        "name": {"fr": "Les Preuves du Baron", "it": "Le Prove del Barone", "es": "Las Pruebas del Barón", "pt": "As Provas do Barão"},
        "text": {
            "fr": "Dans la bibliothèque sous la troisième latte du plancher: une enveloppe avec des documents pointant vers le meurtrier.",
            "it": "In biblioteca sotto la terza tavola del pavimento: una busta con documenti che indicano l'assassino.",
            "es": "En la biblioteca bajo la tercera tabla del suelo: un sobre con documentos que apuntan al asesino.",
            "pt": "Na biblioteca sob a terceira tábua do chão: um envelope com documentos apontando para o assassino.",
        }
    },
    "new_will_location": {
        "name": {"fr": "Le Nouveau Testament", "it": "Il Nuovo Testamento", "es": "El Nuevo Testamento", "pt": "O Novo Testamento"},
        "text": {
            "fr": "Derrière les livres de droit au troisième rayon. Pas encore signé.",
            "it": "Dietro i libri di diritto al terzo scaffale. Non ancora firmato.",
            "es": "Detrás de los libros de derecho en el tercer estante. Aún no firmado.",
            "pt": "Atrás dos livros de direito na terceira prateleira. Ainda não assinado.",
        }
    },
    "surveillance_file": {
        "name": {"fr": "Le Dossier de Surveillance", "it": "Il Fascicolo di Sorveglianza", "es": "El Expediente de Vigilancia", "pt": "O Dossiê de Vigilância"},
        "text": {
            "fr": "12 pages sur une personne à table. Horaires, lieux, un nom récurrent.",
            "it": "12 pagine su una persona al tavolo. Orari, luoghi, un nome ricorrente.",
            "es": "12 páginas sobre una persona en la mesa. Horarios, lugares, un nombre recurrente.",
            "pt": "12 páginas sobre uma pessoa na mesa. Horários, lugares, um nome recorrente.",
        }
    },
    "blackmail_files": {
        "name": {"fr": "Les Dossiers de Chantage", "it": "I Fascicoli di Ricatto", "es": "Los Expedientes de Chantaje", "pt": "Os Dossiês de Chantagem"},
        "text": {
            "fr": "Trois dossiers. Trois personnes. Trois secrets qui ensemble pointent vers le meurtrier.",
            "it": "Tre fascicoli. Tre persone. Tre segreti che insieme indicano l'assassino.",
            "es": "Tres expedientes. Tres personas. Tres secretos que juntos apuntan al asesino.",
            "pt": "Três dossiês. Três pessoas. Três segredos que juntos apontam para o assassino.",
        }
    },
}

TASK_TRANSLATIONS = {
    "task_bathroom": {
        "fr": "🚶 MISSION SECRÈTE: Va maintenant seul aux toilettes. Regarde derrière le miroir. Tu y trouveras quelque chose — rapporte-le. Si on te demande où tu étais: tu chargeais ton téléphone.",
        "it": "🚶 MISSIONE SEGRETA: Vai ora da solo in bagno. Guarda dietro lo specchio. Troverai qualcosa — portalo con te. Se qualcuno chiede dov'eri: stavi caricando il telefono.",
        "es": "🚶 MISIÓN SECRETA: Ve ahora solo al baño. Mira detrás del espejo. Encontrarás algo — tráelo contigo. Si alguien pregunta dónde estabas: estabas cargando tu teléfono.",
        "pt": "🚶 MISSÃO SECRETA: Vá agora sozinho ao banheiro. Olhe atrás do espelho. Você encontrará algo — traga de volta. Se alguém perguntar onde você estava: você estava carregando seu telefone.",
    },
    "task_drink_three": {
        "fr": "🍷 TÂCHE MÉMOIRE: Bois trois fois dans ton verre au cours des 3 prochaines minutes. Au troisième gorgée: regarde dans les yeux de la personne en face de toi pendant 5 secondes sans détourner le regard.",
        "it": "🍷 COMPITO MEMORIA: Bevi tre volte dal tuo bicchiere nei prossimi 3 minuti. Al terzo sorso: guarda negli occhi la persona di fronte a te per 5 secondi senza distogliere lo sguardo.",
        "es": "🍷 TAREA MEMORIA: Bebe tres veces de tu copa en los próximos 3 minutos. En el tercer sorbo: mira a los ojos de la persona frente a ti durante 5 segundos sin apartar la mirada.",
        "pt": "🍷 TAREFA MEMÓRIA: Beba três vezes do seu copo nos próximos 3 minutos. No terceiro gole: olhe nos olhos da pessoa à sua frente por 5 segundos sem desviar o olhar.",
    },
    "task_whisper": {
        "fr": "🗣️ MISSION CHUCHOTEMENT: Penche-toi discrètement vers la personne à ta gauche et chuchote: 'Le Baron avait un ennemi que personne ne connaissait.' Observe attentivement sa réaction.",
        "it": "🗣️ COMPITO SUSSURRO: Inclinati discretamente verso la persona alla tua sinistra e sussurra: 'Il Barone aveva un nemico che nessuno conosceva.' Osserva attentamente la sua reazione.",
        "es": "🗣️ TAREA SUSURRO: Inclínate discretamente hacia la persona a tu izquierda y susurra: 'El Barón tenía un enemigo que nadie conocía.' Observa atentamente su reacción.",
        "pt": "🗣️ TAREFA SUSSURRO: Incline-se discretamente para a pessoa à sua esquerda e sussurre: 'O Barão tinha um inimigo que ninguém conhecia.' Observe atentamente a reação dela.",
    },
    "task_barons_glass": {
        "fr": "🥃 TÂCHE MÉDECIN: Va à la chaise où le Baron était assis. Le verre du Baron est là. Ramasse-le. Sens-le — lentement. Tu sais ce que tu sens. Annonce à voix haute ce que tu sens.",
        "it": "🥃 COMPITO DOTTORE: Vai alla sedia dove era seduto il Barone. Il bicchiere del Barone è lì. Raccoglilo. Annusalo — lentamente. Sai cosa senti. Annuncia ad alta voce cosa senti.",
        "es": "🥃 TAREA MÉDICO: Ve a la silla donde estaba sentado el Barón. El vaso del Barón está ahí. Recógelo. Huélelo — lentamente. Sabes lo que hueles. Anuncia en voz alta lo que hueles.",
        "pt": "🥃 TAREFA MÉDICO: Vá até a cadeira onde o Barão estava sentado. O copo do Barão está lá. Pegue-o. Cheire-o — lentamente. Você sabe o que cheira. Anuncie em voz alta o que cheira.",
    },
    "task_window": {
        "fr": "👁️ TÂCHE D'OBSERVATION: Lève-toi. Va à la fenêtre. Regarde dehors pendant 30 secondes sans parler. Puis dis à voix haute: 'Quelqu'un était dehors.' Assieds-toi. Pas un mot de plus.",
        "it": "👁️ COMPITO DI OSSERVAZIONE: Alzati. Vai alla finestra. Guarda fuori per 30 secondi senza parlare. Poi di' ad alta voce: 'Qualcuno era fuori.' Siediti. Nessuna altra parola.",
        "es": "👁️ TAREA DE OBSERVACIÓN: Levántate. Ve a la ventana. Mira afuera durante 30 segundos sin hablar. Luego di en voz alta: 'Alguien estaba afuera.' Siéntate. Ni una palabra más.",
        "pt": "👁️ TAREFA DE OBSERVAÇÃO: Levante-se. Vá até a janela. Olhe para fora por 30 segundos sem falar. Depois diga em voz alta: 'Alguém estava lá fora.' Sente-se. Nenhuma palavra mais.",
    },
    "task_toast": {
        "fr": "🥂 LE DERNIER TOAST: Lève-toi. Lève ton verre. Dis: 'À la vérité — elle vient toujours à la lumière.' Tout le monde doit boire. Observe qui hésite.",
        "it": "🥂 L'ULTIMO BRINDISI: Alzati. Alza il tuo bicchiere. Di': 'Alla verità — viene sempre alla luce.' Tutti devono bere. Osserva chi esita.",
        "es": "🥂 EL ÚLTIMO BRINDIS: Levántate. Levanta tu copa. Di: 'Por la verdad — siempre sale a la luz.' Todos deben beber. Observa quién duda.",
        "pt": "🥂 O ÚLTIMO BRINDE: Levante-se. Levante seu copo. Diga: 'À verdade — ela sempre vem à luz.' Todos devem beber. Observe quem hesita.",
    },
    "task_drink_together": {
        "fr": "🍷 BOIRE ENSEMBLE: Tout le monde boit simultanément — au signal de trois. Celui qui ne boit PAS a quelque chose à cacher.",
        "it": "🍷 BERE INSIEME: Tutti bevono simultaneamente — al segnale di tre. Chi NON beve ha qualcosa da nascondere.",
        "es": "🍷 BEBER JUNTOS: Todos beben simultáneamente — a la cuenta de tres. Quien NO beba tiene algo que ocultar.",
        "pt": "🍷 BEBER JUNTOS: Todos bebem simultaneamente — no sinal de três. Quem NÃO beber tem algo a esconder.",
    },
    "murderer_task_alibi": {
        "fr": "🎭 TÂCHE MEURTRIER 1 — ALIBI: Tu dois maintenant spontanément raconter où tu étais à minuit. Choisis une personne comme 'témoin' — sans lui demander d'abord.",
        "it": "🎭 COMPITO ASSASSINO 1 — ALIBI: Devi ora spontaneamente raccontare dove eri a mezzanotte. Scegli una persona come 'testimone' — senza chiederle prima.",
        "es": "🎭 TAREA ASESINO 1 — COARTADA: Debes ahora espontáneamente contar dónde estabas a medianoche. Elige a una persona como 'testigo' — sin preguntarle primero.",
        "pt": "🎭 TAREFA ASSASSINO 1 — ÁLIBI: Você deve agora espontaneamente contar onde estava à meia-noite. Escolha uma pessoa como 'testemunha' — sem perguntar primeiro.",
    },
    "murderer_panic_moment": {
        "fr": "⚠️ MOMENT DE PANIQUE: Quelqu'un se rapproche de la vérité. Décide maintenant:\n\nOPTION A: 'Je dois avouer quelque chose.' — avoue quelque chose d'inoffensif mais compromettant.\nOPTION B: Commence à pleurer ou fais semblant. Effondrement émotionnel.\nOPTION C: Redirige immédiatement vers une autre personne.\n\nChoisie maintenant. Tu as 60 secondes.",
        "it": "⚠️ MOMENTO DI PANICO: Qualcuno si sta avvicinando alla verità. Decidi ora:\n\nOPZIONE A: 'Devo confessare qualcosa.' — confessa qualcosa di innocuo ma incriminante.\nOPZIONE B: Inizia a piangere o fingi. Crollo emotivo.\nOPZIONE C: Reindirizza immediatamente su un'altra persona.\n\nScegli ora. Hai 60 secondi.",
        "es": "⚠️ MOMENTO DE PÁNICO: Alguien se está acercando a la verdad. Decide ahora:\n\nOPCIÓN A: 'Debo confesar algo.' — confiesa algo inofensivo pero incriminatorio.\nOPCIÓN B: Empieza a llorar o finge. Colapso emocional.\nOPCIÓN C: Redirige inmediatamente hacia otra persona.\n\nElige ahora. Tienes 60 segundos.",
        "pt": "⚠️ MOMENTO DE PÂNICO: Alguém está se aproximando da verdade. Decida agora:\n\nOPÇÃO A: 'Preciso confessar algo.' — confesse algo inofensivo mas incriminador.\nOPÇÃO B: Comece a chorar ou finja. Colapso emocional.\nOPÇÃO C: Redirecione imediatamente para outra pessoa.\n\nEscolha agora. Você tem 60 segundos.",
    },
}

ENDING_TRANSLATIONS = {
    "murderer_caught": {
        "title": {"fr": "Justice", "it": "Giustizia", "es": "Justicia", "pt": "Justiça"},
        "text": {
            "fr": "Le meurtrier a été confondu. Pas par un vote — mais par des preuves, l'observation et la vérité qui vient toujours à la lumière.\n\nGagnants: Tous ceux qui ont désigné le bon meurtrier.",
            "it": "L'assassino è stato smascherato. Non da un voto — ma da prove, osservazione e la verità che viene sempre alla luce.\n\nVincitori: Tutti coloro che hanno indicato il giusto assassino.",
            "es": "El asesino fue expuesto. No por una votación — sino por pruebas, observación y la verdad que siempre sale a la luz.\n\nGanadores: Todos los que señalaron al asesino correcto.",
            "pt": "O assassino foi exposto. Não por votação — mas por provas, observação e a verdade que sempre vem à luz.\n\nVencedores: Todos os que apontaram o assassino correto.",
        }
    },
    "murderer_escapes": {
        "title": {"fr": "L'Assassin Rit", "it": "L'Assassino Ride", "es": "El Asesino Ríe", "pt": "O Assassino Ri"},
        "text": {
            "fr": "Un innocent a été accusé. Le vrai meurtrier est parmi vous et rit. {murderer_name} a gagné.",
            "it": "Un innocente è stato accusato. Il vero assassino è tra voi e ride. {murderer_name} ha vinto.",
            "es": "Un inocente fue acusado. El verdadero asesino está entre ustedes y ríe. {murderer_name} ganó.",
            "pt": "Um inocente foi acusado. O verdadeiro assassino está entre vocês e ri. {murderer_name} ganhou.",
        }
    },
    "shadow_wins": {
        "title": {"fr": "Le Testament a Disparu", "it": "Il Testamento è Scomparso", "es": "El Testamento Desapareció", "pt": "O Testamento Desapareceu"},
        "text": {
            "fr": "Pendant que tout le monde enquêtait — le testament a disparu. L'Ombre a gagné.",
            "it": "Mentre tutti indagavano — il testamento è scomparso. L'Ombra ha vinto.",
            "es": "Mientras todos investigaban — el testamento desapareció. La Sombra ganó.",
            "pt": "Enquanto todos investigavam — o testamento desapareceu. A Sombra ganhou.",
        }
    },
    "perfect_solve": {
        "title": {"fr": "Solution Parfaite", "it": "Soluzione Perfetta", "es": "Solución Perfecta", "pt": "Solução Perfeita"},
        "text": {
            "fr": "L'écrivaine et le médecin ont accompli l'impossible ensemble. C'est rare. C'est brillant.",
            "it": "La scrittrice e il dottore hanno compiuto insieme l'impossibile. È raro. È brillante.",
            "es": "La escritora y el médico lograron juntos lo imposible. Esto es raro. Esto es brillante.",
            "pt": "A escritora e o médico realizaram juntos o impossível. Isso é raro. Isso é brilhante.",
        }
    },
}
