# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:11:41 2022

@author: sojeb
"""
import numpy as np
noms = ["Aaliyah","aapeli","Aaron","arón","aatami","aatto","aatu",
                 "abaddon","abbán","Aurèle","Aurelia","aureliano","Aurelie",
                 "Aurélie","Aurelien","Aurélien","aurelio","aurelius","aureole",
                 "Auriane","Jacqueline","jacquelyn","Jacques","jacquetta",
                 "jacquette","jacqui","Jad","jada","Jade","Jaden","jadon",
                 "jadranka","jadranko","jadwiga","jadyn","jadzia","jael","jafar",
                 "jafet","jaffar","jaffe","lindy","Line","linette","linford","ling",
                 "linh","linnaea","linnéa","linnet","linnette","linnie","Lino",
                 "neassa","neculai","ned","Neela","neelam","neely","nefertari",
                 "nefertiti","nehemiah","neifion","Neil","Neïla","neilina",
                 "neirin","nekane","nekoda","nelda","Nelia","Nélia","Nell",
                 "nelle","nellie","Nelly","nels","Nelson","nelu","Nelya",
                 "nemesis","nena","Abdallah", "Abdel", "Abdelah", "Abdelaziz", 
                 "Abdelhalim", "Abderrahim", "Abdoullah", "Abel", "Achille", "Adam", 
                 "Adeline", "Adolf", "Adolphe", "Adrian", "Adriana", "Adrianus", "Adrien", 
                 "Adrienne", "Adelaede", "Agathe", "Aglae", "Agnes", "Ahmad", "Ahmed", 
                 "Aimery", "Aime", "Aimee", "Alain", "Alan", "Alban", "Albert", "Albertine", 
                 "Alberto", "Albin", "Albine", "Albino", "Alberic", "Aldo", "Alec", "Alessandra",
                 "Alessandro", "Alex", "Alexander", "Alexandra", "Alexandre", "Alexandrine", 
                 "Alexia", "Alexis", "Alfred", "Ali", "Alice", "Alicia", "Alida", "Aline", "Alison", 
                 "Alistair", "Allan-David", "Allan", "Allen", "Alphonse", "Amanda", "Amandine", "Amar", 
                 "Amaury", "Ambroise", "Amel", "Amina", "Amelie", "Ana-Maria", "Anna-Maria","Ana", "Anna",
                 "Anaes", "Andrea", "Andreas", "Andrew", "Andre-Clement", "Andre-Jean", "Andre-Louis", 
                 "Andre-Luc", "Andre-Marie", "Andre-Michel", "Andre", "Andree", "Ange", "Angel", "Angelina", 
                 "Angelo", "Angie", "Angele", "Angelique", "Anissa", "Anita", "Ann-Charlotte","Anne-Charlotte", 
                 "Ann", "Anna-Lisa", "Anna-Maria", "Anna", "Annabel", "Annabelle", "Anne-Catherine", "Anne-Charlotte", 
                 "Anne-Claire", "Anne-Clotilde", "Anne-Cecile", "Anne-France", "Anne-Franeoise", "Anne-Gaelle", 
                 "Anne-Josephine", "Anne-Laure", "Anne-Lise", "Anne-Lyse", "Anne-Marie", "Anne-Sophie", "Anne", "Annette", 
                 "Annick", "Annie-Claude", "Annie", "Anny", "Anouchka", "Anouk", "Anthony", "Antoine", "Antoinette", "Antoni", 
                 "Antonio", "Antony", "Ariane", "Ariel", "Arielle", "Aristide", "Arie", "Arlette", "Armand", "Armando", 
                 "Armel", "Armelle", "Armin", "Arnaud", "Arnauld", "Arnault", "Arnold", "Arthur", "Arturo", "Astrid", "Aude", 
                 "Audebert", "Audrey", "Augusta", "Auguste", "Augustin", "Augusto", "Aurore", "Aurelia", "Aureliane", "Aurelie", 
                 "Aurelien", "Axel", "Axelle", "Aymar", "Aymeric", "Aecha", "Bahia", "Baptiste", "Barbara", "Bart", "Barthelemy", 
                 "Basile", "Bastien", "Baudoin", "Benaecha", "Benjamin", "Benjamine", "Benoet-David", "Benoet-Paul", "Benoet", 
                 "Bernadette", "Bernard-Eric", "Bernard", "Bernhard", "Bertrand", "Betty", "Bianca", "Bill", "Bjern", "Blaise", 
                 "Blanche", "Blandine", "Boris", "Brahim", "Brian-John", "Brian", "Brice", "Brigitte", "Bruce", "Bruno", "Beatrice",
                 "Beatrice", "Benedicte", "Berangere", "Berengere", "Cameron", "Camille-Pierre", "Camille", "Candice",
                 "Capucine", "Carine", "Carl", "Carla", "Carlo", "Carlos", "Carmen", "Carmine", "Caro", "Caroline", "Carol", 
                 "Carole", "Caroline", "Carolyn", "Catherine", "Cathie", "Cathy", "Cendrine", "Cerise", "Cesare", "Chantal", 
                 "Charle", "Charles","Charles-Andre", "Charles-Emile", "Charles-Eric", "Charles-Henri", "Charles-Henry", 
                 "Charles-Louis", "Charles-Marie", "Charles", "Charlie", "Charline", "Charlotte", "Charly", "Charlene", 
                 "Chiara", "Chloe", "Christel", "Christelle", "Christian", "Christiane", "Christina", "Christine", "Christo", 
                 "Christophe", "Christoph", "Christophe", "Christopher", "Christele", "Chrystel", "Cindy", "Claire", "Clara", 
                 "Clarisse", "Claude-Henri", "Claude", "Claudette", "Claudia", "Claudie", "Claudine", "Claudio", "Claudius", 
                 "Clotilde", "Clemence", "Clement", "Colette", "Colin", "Concepcion", "Constance", "Constant", "Constantin", 
                 "Coralie", "Corine", "Corinne", "Cynthia", "Cyprien", "Cyril", "Cyrille", "Cecil", "Cecile", "Cecilia", "Cedric", 
                 "Celia", "Celine", "Cesar", "Daisy", "Dalida", "Damien", "Dan", "Daniel-Henri", "Daniel", "Daniela", "Danielle", 
                 "Daniele", "Danny", "Dany", "Daphne", "Dario", "Darlene", "Darren", "David", "Deborah", "Delphine", "Denis", "Denise", 
                 "Dennis", "Denys", "Denyse", "Desmond", "Diana", "Diane-Karine", "Diane", "Didier", "Diego", "Dieter", "Dietrich", 
                 "Dieudonne", "Dimitri", "Diogo", "Djamel", "Djamila", "Dolores", "Domingos", "Dominique", "Dominoco", "Donald", 
                 "Dorothy", "Dorothee", "Douglas", "Dounia", "Eddie", "Eddy", "Edgar", "Edgard", "Edmond", "Edmonde", "Edoardo", 
                 "Edouard", "Eduardo", "Edward", "Edwige", "Edwin", "Elena", "Eliane", "Elisabeth", "Elizabeth", "Eloese", "Elsa", 
                 "Elvire", "Eleonore", "Emannuel", "Emmanuel", "Emannuele", "Emmanuelle", "Emannuelle", "Emmanuelle","Emanuel", 
                 "Emmanuel","Emanuelle", "Emmanuelle","Emily", "Emma", "Emmanuel", "Emmanuelle", "Enrico", "Enzo", "Eric", 
                 "Erick", "Erik", "Erika", "Ernest", "Ernst", "Erwan", "Erwann", "Erwin", "Estelle", "Esther", "Etiennette", 
                 "Eudes", "Eugenio", "Eugene", "Eugenie", "Evangeline", "Eve-Line", "Eve", "Eveline", "Evelyn", "Evelyne", 
                 "Franeois-Xavier", "Fabian", "Fabien", "Fabienne", "Fabio", "Fabiola", "Fabre", "Fabrice", "Fabrizio", 
                 "Fanny", "Farid", "Faridah", "Fatiha", "Fatima", "Fatma", "Faustine", "Ferdinand", "Fernand", "Fernande", 
                 "Fernando", "Ferouz", "Filippo", "Fiona", "Flavie", "Flavien", "Flavio", "Fleur", "Florence", "Florent", 
                 "Florian", "Floriane", "Fran?ois", "Franeois", "Franc-Xavier", "Franeois-Xavier", "France", "Francesca", 
                 "Francesco", "Francine", "Francis", "Francisco", "Franck", "Franco", "Frank", "Frantz", "Franz-Georg", 
                 "Franz", "Franeoi", "Franeois", "Franeois-Xav", "Franeois-Xavier", "Franeois-Xavier", "Franeois", 
                 "Franeoise", "Fred", "Freddy", "Frederica", "Frederick", "Frederico", "Frederik", "Friedrich", "Fritz", 
                 "Frederi", "Frederic", "Frederic", "Frederique", "Felix", "Gabriel", "Gabriele", "Gabriella", 
                 "Gabrielle", "Gaby", "Gad", "Gaetanino", "Gaetano", "Garbriel", "Gabriel", "Gary", "Gaspard", 
                 "Gaston", "Gael", "Gaelle", "Gaetan", "Genevieve", "Geoffrey", "Geoffroy", "Georg", "George",
                 "Georges-Henri", "Georges-Michel", "Georges", "Georgette", "Georgio", "Gerardo", "Gerhard", "Germain", 
                 "Germaine", "Gervais", "Ghislain", "Ghislaine", "Ghuilem", "Gianfranco", "Gianni", "Gil", "Gilbert", 
                 "Gilberte", "Gildas", "Gilles-Marie", "Gilles", "Ginette", "Gino", "Giorgio", "Giovanni", "Giselle", 
                 "Gislain", "Gisele", "Giuseppe", "Gladys", "Gontrand", "Gonzague", "Gordon", "Gottfried", "Graham", "Grece", 
                 "Gregoire", "Gregor", "Gregory", "Guido", "Guillaume", "Guislain", "Gunter", "Gunther", "Gustave", "Guy", "Guylaine", "Gwen", "Gwenael", "Gwenaelle", "Gwendoline", "Gerald", "Geraldine", "Gerard", "Geraud", "Habib", "Hanns", "Hans", "Hans", "Harold", "Hassan", "Hector", "Heinrich", "Helen", "Helmut", "Henri-Charles", "Henri-Pierre", "Henri", "Henriette", "Henry", "Herbert", "Herman", "Hermann", "Herve-Joseph", "Herve", "Honore", "Houria", "Hubert", "Hughes", "Hugues", "Huguette", "Helene", "Helena", "Ian", "Igor", "Ingrid", "Ines", "Irma", "Irene", "Isaac", "Isabel", "Isabelle", "Isidore", "Issam", "Ivan", "J-Franeois", "Jean-Franeois", "JM", "JP", "Jack", "Jackie", "Jacky", "Jacob", "Jacobus", "Jacque", "Jacques","Jacqueline", "Jacques-Olivier", "Jacques", "Jamel", "James", "Jamila", "Jan", "Jane", "Janine", "Jannick", "Jany", "Jason", "Jean-Alain", "Jean-Andre", "Jean-Antoine", "Jean-Audebert", "Jean-Baptiste", "Jean-Bernard", "Jean-Brice", "Jean-Camille", "Jean-Charles", "Jean-Christophe", "Jean-Claude", "Jean-Clement", "Jean-Daniel", "Jean-Didier", "Jean-Dominique", "Jean-Eric", "Jean-Eudes", "Jean-Francis", "Jean-Franeois", "Jean-Frederic", "Jean-Gabriel", "Jean-Georges", "Jean-Gilles", "Jean-Guy", "Jean-Henri", "Jean-Herve", "Jean-Hugues", "Jean-Jacques", "Jean-Joel", "Jean-Laurent", "Jean-Lionel", "Jean-Lou", "Jean-Louis", "Jean-Loup", "Jean-Loec", "Jean-Luc", "Jean-Lucien", "Jean-Leon", "Jean-Manuel", "Jean-Marc", "Jean-Marcel", "Jean-Marie", "Jean-Mary", "Jean-Maurice", "Jean-Max", "Jean-Michel", "Jean-Nicolas", "Jean-Noel", "Jean-Olivier", "Jean-Pascal", "Jean-Patrice", "Jean-Patrick", "Jean-Paul", "Jean-Philippe", "Jean-Pierre", "Jean-Raphael", "Jean-Raymond", "Jean-Rene", "Jean-Robert", "Jean-Roger", "Jean-Sebastien", "Jean-Thomas", "Jean-Yves", "Jean-etienne", "Jean", "JeanLouis", "Jean-Louis", "JeanPierre", "Jean-Pierre", "Jeanine", "Jeanne", "Jeannette", "Jeannie", "Jeannine", "Jehan", "Jennifer", "Jenny", "Jeremy", "Jessica", "Jessie", "Jessy", "Jimmy", "Joachim", "Joanna", "Joao", "Joaquim", "Jocelyne", "Johan", "Johann", "Johanna", "Johanne", "Johannes", "John", "Johnny", "Jonas", "Jonathan", "Jorg", "Jorge", "Jorgen", "Joselaine", "Joseph", "Josephus", "Josette", "Josiane", "Jose-Maria", "Jose", "Josee", "Josephine", "Jozef", "Joel", "Joelle", "Juan", "Judith", "Jules", "Julia", "Juliana", "Julie", "Julien", "Juliette", "Jullien", "Julien", "Jurgen", "Justine", "Jeremie", "Jereme", "Jesus", "Kadyja", "Kamel", "Karen", "Karim", "Karima", "Karin", "Karina", "Karine", "Karl-Otto", "Karl", "Katerine", "Kathleen", "Katia", "Katy", "Keith", "Kelly", "Kenneth", "Kenny", "Kevin", "Khaled", "Klaus-Werner", "Klaus", "Kristel", "Kurt", "Laetitia", "Lamia", "Lana", "Lars", "Laura", "Laure", "Laureline", "Laurence", "Laurencia", "Laurent-Benoet", "Laurent", "Lauretta", "Lauriane", "Laurie", "Lawrence", "Leila", "Lelia", "Leonardo", "Leslie", "Lia", "Lila", "Lilian", "Liliane", "Lilliane", "Liliane", "Lina", "Linda", "Line", "Linette", "Lionel", "Lisa", "Lise", "Lorenzo", "Loriane", "Lorianne", "Lorraine", "Louis-Gerard", "Louis-Marie", "Louis", "Louisa", "Louise", "Louisette", "Loec", "Luc", "Luca", "Lucas", "Lucette", "Lucia", "Luciano", "Lucie", "Lucien", "Lucienne", "Lucile", "Lucille", "Lucio", "Lucy", "Ludivine", "Ludiwine", "Ludovic", "Luigi", "Luis", "Lydia", "Lydie", "Lylia", "Lyliane", "Lyna", "Lynda", "Lysiane", "Lea", "Leo", "Leon", "Leonard", "Leone", "Leonie", "Leopold", "Macha", "Madeleine", "Madeline", "Madiha", "Magali", "Magalie", "Magaly", "Magdeleine", "Maggaly", "Magaly", "Maggy", "Magnus", "Malcolm", "Malcom", "Malik", "Malika", "Manfred", "Manon", "Manuel", "Manuela", "Marc-Aurele", "Marc", "Marcel", "Marcelino", "Marcelle", "Marcellin", "Marcello", "Marco", "Margaret", "Margareth", "Margaux", "Marguerite", "Margueritte", "Marguerite", "Maria-Lisa", "Maria", "Mariana", "Marianna", "Marianne", "Marie-Agnes", "Marie-Alice", "Marie-Amelie", "Marie-Andree", "Marie-Ange", "Marie-Angele", "Marie-Anne", "Marie-Aude", "Marie-Chantal", "Marie-Christine", "Marie-Claire", "Marie-Claude", "Marie-Cecile", "Marie-Dominique", "Marie-Evelyn", "Marie-Florence", "Marie-France", "Marie-Franeoise", "Marie-Gabrielle", "Marie-Helene", "Marie-Isabelle", "Marie-Jeanne", "Marie-Jo", "Marie-Joseph", "Marie-Josephe", "Marie-Jose", "Marie-Josee", "Marie-Joelle", "Marie-Julie", "Marie-Juliette", "Marie-Laure", "Marie-Lou", "Marie-Louise", "Marie-Madeleine", "Marie-Michelle", "Marie-Noelle", "Marie-Odile", "Marie-Pascale", "Marie-Paule", "Marie-Pierre", "Marie-Reine", "Marie-Rose", "Marie-Regine", "Marie-Sophie", "Marie-Therese", "Marie-edith", "Marie-emilie", "Marie", "Marielle", "Marieva", "Marilyn", "Marina", "Marine", "Marinette", "Mario", "Marion", "Marius", "Marjolaine", "Marjorie", "Mark", "Markus", "Marlene", "Marta", "Marthe", "Martial", "Martin", "Martine", "Martino", "Mary", "Marylaine", "Maryline", "Marylise", "Marylou", "Marylene", "Maryse", "Maryvonne", "Massimiliano", "Massimo", "Mathias", "Mathieu", "Mathilde", "Matthew", "Matthias", "Matthieu", "Maud", "Maurice", "Mauricette", "Mauro", "Max", "Maxence", "Maxime", "Maximilien", "Maya", "Maeva", "Maete", "Medeiros", "Melinda", "Mercedes", "Messaoud", "Messaouda", "Michael", "Michel-Ange", "Michel-Philippe", "Michel", "Micheline", "Michelle", "Michele", "Mickael", "Miguel", "Mikael", "Miloud", "Mireille", "Mohamed", "Mohammad", "Mohammed", "Monica", "Monique", "Morgan", "Morgane", "Mounia", "Mounir", "Mourad", "Moese", "Muguette", "Muriel", "Murielle", "Mustapha", "Mylene", "Myriam", "Myrna", "Melanie", "Melodie", "Nadia", "Nadine", "Nadege", "Nancy", "Nasser", "Natacha", "Natanael", "Nathalie", "Nathan", "Nathanael", "Nathaniel", "Neil", "Nelly", "Nicaise", "Nicholas", "Nick", "Nico", "Nicolas","Nicola", "Nicolas", "Nicolas", "Nicole", "Nicolle", "Nicole", "Niels", "Nigel", "Nina", "Nino", "Nissim", "Nolwenn", "Nora", "Norbert", "Norman", "Nourdine", "Noemie", "Noel", "Noelle", "Octave", "Oceane", "Odette", "Odile", "Ola", "Olga", "Oliver", "Olivia", "Olivier", "Olympia", "Omar", "Oriane", "Oscar", "Oswald", "Otto", "Oussama", "Paco", "Pamela", "Paola", "Paolo", "Pascal", "Pascale", "Pascaline", "Patrice", "Patricia", "Patrick-James", "Patrick", "Patrizia", "Paul-Antoine", "Paul", "Paula", "Paule", "Paulette", "Pauline", "Paulo", "Pedro", "Peggy", "Peguy", "Perrine", "Peter", "Petrus", "Philip", "Philipp", "Philippe"
                     ]

universitesVilles = {"Université de Bourgogne":"Dijon",
"Université de Bordeaux":"Bordeaux",
"Université de Toulouse 3 — Paul Sabatier":"Toulouse",
"Université de Reims Champagne-Ardenne":"Reims",
"Université Rennes 2":"Rennes",
"Université d’Orléans":"Orléans",
"Université Paris Descartes":"Paris",
"Université Sorbonne Nouvelle — Paris 3":"Paris",
"Université de Picardie Jules-Verne":"Toulon",
"Université de Pau et des Pays de l’Adour":"Nantes",
"Université du Littoral Côte d’Opale":"Nice",
"Université de Haute-Alsace":"Strasbourg",
"Université Clermont Auvergne":"Clermont",
"Université des Antilles":"Antilles",
"Université de Guyane":"Guyane",
"Université Paris-Est Marne-la-Vallée":"Paris",
"Université Paris 1 Panthéon-Sorbonne":"Paris",
"Sorbonne Université":"Paris",
"Université de Limoges":"Limoges",
"Université du Mans":"Mans",
"Université de Rouen":"Rouen",
"Université Savoie Mont Blanc":"Paris",
"Université Polytechnique Hauts-de-France":"Lille",
"Université Paris 2 Panthéon Assas":"Paris",
"Université Paris Nanterre":"Paris",
"Université de Versailles Saint-Quentin-en-Yvelines":"Saint-Quentin-en-Yvelines",
"Université de Rennes 1":"Rennes",
"Université de La Rochelle":"Rennes",
"Université de Franche-Comté":"Cresot",
"Université de Bretagne Occidentale":"Bretagne",
"Université Toulouse — Jean Jaurès":"Toulouse",
"Université Côte d’Azur":"Marseille",
"Université de Grenoble Alpes":"Grenoble",
"Université de Tours":"Tours",
"Université Jean Moulin Lyon 3":"Lyon",
"Université Paul-Valéry Montpellier 3":"Montpellier",
"Université de Nantes":"Nantes",
"Université Paris-Est Créteil":"Paris",
"Université Paris 13":"Paris",
"Université Paris-Saclay":"Paris",
"Université de Toulon":"Toulon",
"Université Paris 8":"Paris",
"Université du Havre":"Havre",
"Aix-Marseille Université":"Marseille",
"Université Toulouse 1 Capitole":"Toulouse",
"Université de Nîmes":"Nîmes",
"Université de Strasbourg":"Strasbourg",
"Université d’Artois":"Artois",
"Université Claude Bernard Lyon 1":"Lyon",
"Université Jean Monnet":"Paris",
"Université Bretagne Sud":"Bretagne",
"Université d’Angers":"Angers",
"Université de Poitiers":"Poitiers",
"Université de Corse Pasquale Paoli":"Corse",
"Université de Cergy-Pontoise":"Cergy",
"Université de Perpignan":"Perpignan",
"Université de Montpellier":"Montpellier",
"Avignon Université":"Avignon",
"Université d’Évry":"Évry",
"Université de Caen Normandie":"Caen",
"Université Lumière Lyon 2":"Lyon",
"Université Bordeaux Montaigne":"Bordeaux",
"Université de Paris":"Paris",
"Institut Catholique de Paris":"Paris",
"Université Catholique de Lyon":"Lyon",
"Université Catholique de Lille":"Lille",
"Université de Lorraine":"Lorraine",
"Université de technologie de Compiègne":"Compiègne",
"Université Catholique de l’Ouest":"Paris",
"Université Technologique de Belfort Montbéliard":"Belfort",
"Institut National Universitaire Champollion":"Paris",
"Université Pierre et Marie Curie":"Paris",
"Université Lille 3 Charles-de-Gaulle":"Lille",
"Université Lille 2 Droit et Santé":"Lille",
"Université Lille 1 Sciences technologies":"Lille"}
vaccinsHepatite = ["Avaxim 160", "Avaxim 80","HBVAXPRO 10","HBVAXPRO 5","Havrix 720"]
vaccinsCovid = ["Novavax", "Pfizer","Janssen","AstraZeneca"]
vaccins=["Priorix","Rabipur","Repevax","Tyavax"]
maladiesGrave = ["Mucoviscidose", "Hémophilie","Epilepsie","Psychose","Diabete", "Drépanocytose"]
maladiesGenetique = ["Phénylcétonurie", "Mitochondrial","Phénylcétonurie"]
maladies = ["Choléra", "Fièvre jaune","Coqueluche", "Toux", "Gastroentérite à rotavirus", "Nodules", "Acné", "Teigne"]
hopitaux = {"CHU Dijon":"Dijon"} #, "CHU Paris":"Paris"


universites = np.unique(list(universitesVilles.keys()))
villes = np.unique(list(universitesVilles.values()))
serviceOphtalmologie = ["Service Ophtalmologique"]
serviceDermatologie = ["Service Dermatologique"]
serviceCardiologie = ["Service Cardiologique"]

import unidecode
from random import randrange,randint,choice
from datetime import timedelta
def supprimerAccent(s):
    return unidecode.unidecode(s)


def get_radom_name():
    return noms[randint(0,len(noms)-1)].capitalize()

