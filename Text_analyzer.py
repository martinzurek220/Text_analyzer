"""
projekt_1: první projekt do Engeto Online Python Akademie
Text analyzer.py
author: Martin Žůrek
email: zurek.m@email.cz
discord: MartinZ#0894
"""

# Poznamka pro lektora:
#
# Vim, ze nazvy promennych jsou dlouhe a na zacatku by nemusel byt datovy typ,
# ale tento zapis je pro me vyrazne pochopitelnejsi v tom, co kod dela 
# a urychluje mi to, alespon ted na zacatku, hledani chyb.
#
# Nekde jsem nedodrzel pravidlo 79 znaku na rakek.

# Poznamka:
#
# Cely kod jsem pro pochopitelnost a prehlednost rozdelil do nekolika celku:
#   - Prihlaseni uzivatele
#   - Zadani textu
#   - Uprava zadaneho textu
#   - Vyhodnoceni poctu slov, zjisteni jejich delky a vykresleni grafu


###############################################################################
# Prihlaseni uzivatele                                                        #
###############################################################################

print()
print("$ python projekt1.py")

dict_uzivatele = {
    "uzivatel_1": {"username": "bob", "password": "123"},
    "uzivatel_2": {"username": "ann", "password": "pass123"},
    "uzivatel_3": {"username": "mike", "password": "password123"},
    "uzivatel_4": {"username": "liz", "password": "pass123"}
}

# print(f"dict_uzivatele:{dict_uzivatele}")

str_username_zadany = input("username:")
# str_username_zadany = "bob"
str_password_zadany = input("password:")
# str_password_zadany = "123"

print(f"username:{str_username_zadany}")
print(f"password:{str_password_zadany}")

bool_podminka_pokracovani = False

# Cyklus nacte jednotlive klice slovniku. "Uzivatel_1" az "Uzivatel_4" a pote
# porovnava data jednotlivych uzivatelu s tim, co zadal uzivatel na klavesnici.
for str_uzivatel in dict_uzivatele.keys():

    # Rovna se uzivatelem zadany username usernamu daneho uzivatele?
    if str_username_zadany == dict_uzivatele[str_uzivatel]["username"]:

        # Rovna se uzivatelem zadany password passwordu daneho uzivatele?
        if str_password_zadany == dict_uzivatele[str_uzivatel]["password"]:

            print("-" * 40,"\n",
                "Welcome to the app, ", str_username_zadany , "\n",
                "We have 3 texts to be analyzed.", "\n",
                "-" * 40, sep='')

            # xx_cislo_textu = input("Enter a number btw. 1 and 3 to select:")
            xx_cislo_textu = "3"
            print("Enter a number btw. 1 and 3 to select:", xx_cislo_textu)

            # Jsou uzivatelem zadana cisla textu pouze cisla 0-9?
            if xx_cislo_textu.isdecimal() == True:

                # Je zadane cislo rovno 1 nebo 2 nebo 3?
                if int(xx_cislo_textu) >= 1 and int(xx_cislo_textu) <= 3:

                    print("-" * 40)
                        
                    int_cislo_textu = int(xx_cislo_textu)

                    # Nastaveni podminky pro pokracovani dale na praci s textem.
                    bool_podminka_pokracovani = True
                else:
                    print("You entered a number other than 1, 2, 3, terminating the program..", "\n")
            else:
                print("You did not enter a number, terminating the program..", "\n")            
        else:
            print("Wrong password, terminating the program..", "\n")
        # Pokud jsme uzivatele nasli, vyskoc z cyklu.
        break
else:
    print("Unregistered user, terminating the program..", "\n")


###############################################################################
# Zadani textu                                                                #
###############################################################################

# Pokud jsou splneny vsechny podminky pro pokracovani 
# (je spravne zadany login, heslo a zadany text je 1 nebo 2 nebo 3), 
# tak pokracuj dale na praci s textem.
if bool_podminka_pokracovani:

    # Vyber textu.
    dict_TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

    int_cislo_textu = 1

    # Do promenne str_zadany_text se ulozi text podle volby uzivatele.
    if int_cislo_textu == 1:
        str_zadany_text = dict_TEXTS[0]
    elif int_cislo_textu == 2:
        str_zadany_text = dict_TEXTS[1]
    elif int_cislo_textu == 3:
        str_zadany_text = dict_TEXTS[2]

    # print(f"Str_zadany_text:{str_zadany_text}")


    ###########################################################################
    # Uprava zadaneho textu                                                   #
    ###########################################################################

    # Funkce .rsplit() rozdeli text na jednotliva slova jako typ string a ulozi 
    # je do noveho listu list_rozdeleny_text = ["", "", ...]
    list_rozdeleny_text = str_zadany_text.rsplit(" ")

    # print(f"List_rozdeleny_text:{list_rozdeleny_text}")

    # Cyklus orizne zleva, zprava string o znak "\n" a kdyz je na pozici typ 
    # list, tak ho rozdeli na dva stringy v listu.
    # pr.: ['\nwest', 'of', 'Kemmerer,\nFos', 'sil,'] 
    #   -> ['west', 'of', ['Kemmerer,', 'Fos'], 'sil,']
    int_index_listu = 0

    for str_slovo in list_rozdeleny_text:

        # Orizne string zleva o znak "\n"
        str_slovo = str_slovo.lstrip("\n")

        # Orizne string zleva o znak "\n"
        str_slovo = str_slovo.rstrip("\n")

        # Pokud se stale vyskytuje ve stringu znak "\n", tak ho rozdeli na dva
        # stringy a ulozi do listu.
        if str_slovo.count("\n") > 0:
            list_rozdeleny_text[int_index_listu] = str_slovo.rsplit("\n")
        else:
            list_rozdeleny_text[int_index_listu] = str_slovo

        int_index_listu = int_index_listu + 1

    # print(f"List_rozdeleny_text:{list_rozdeleny_text}")

    # cyklus projde list z minule sekce, vytvori novy docastny a postupne 
    # do nej kopiruje stringy tak, aby to byl ciste list stringu a dalo 
    # se s nim dal pracovat.
    # Pr.: ['west', 'of', ['Kemmerer,', 'Fos'], 'sil,'] ->
    #      ['west', 'of', 'Kemmerer,', 'Fos', 'sil,']
    list_docasny = list()

    for str_list_slovo in list_rozdeleny_text:

        if type(str_list_slovo) == list:
            for int_index_listu in range(0, len(str_list_slovo)):
                list_docasny.append(str_list_slovo[int_index_listu])
        else:
            list_docasny.append(str_list_slovo)

    # print(f"list_docasny:{list_docasny}")

    list_rozdeleny_text = list_docasny.copy()

    # print(f"List stringu:{list_rozdeleny_text}")

    # Cyklus odstrani z prave strany vsech stringu znaky ",.?!"
    # Pr.: ['west', 'of', 'Kemmerer,', 'Fos', 'sil,'] -> 
    #      ['west', 'of', 'Kemmerer', 'Fos', 'sil']
    int_index_listu = 0

    for str_slovo in list_rozdeleny_text:

        list_rozdeleny_text[int_index_listu] = str_slovo.rstrip(",.?!")

        int_index_listu = int_index_listu + 1

    # print(f"Text bez znaku napravo:{list_rozdeleny_text}")


    ###########################################################################
    # Vyhodnoceni poctu slov, zjisteni jejich delky a vykresleni grafu        #
    ###########################################################################

    int_pocet_slov = 0
    int_pocet_prvni_velke_pismeno = 0
    int_pocet_velka_pismena = 0
    int_pocet_mala_pismena = 0
    int_pocet_cisel = 0
    int_suma_cisel = 0

    list_graf = []

    # Cyklus, ktery projde vsechna slova v textu a vrati jejich pocty.
    # list_rozdeleny_text = rozdeleny text na jednotlive stringy a vlozeny 
    # do jednoho listu
    for str_slovo in list_rozdeleny_text:

        # Pocita pocet slov = jako slovo se bere neprazdny string.
        if str_slovo != "":
            int_pocet_slov = int_pocet_slov + 1    

        # Overi, jestli je na zacatku stringu velke pismeno a ostatni mala 
        # a ulozi pocet slov.
        if str_slovo.istitle() == True:
            int_pocet_prvni_velke_pismeno = int_pocet_prvni_velke_pismeno + 1
        
        # Overi, jestli jsou vsechny znaky stringu velka pismena a ulozi 
        # pocet slov.
        elif str_slovo.isupper() == True:
            int_pocet_velka_pismena = int_pocet_velka_pismena + 1

        # Overi, jestli jsou vsechny znaky stringu mala pismena a ulozi 
        # pocet slov.
        elif str_slovo.islower() == True:
            int_pocet_mala_pismena = int_pocet_mala_pismena + 1

        # Overi, jestli jsou ve stringu pouze cislice 0-9, ulozi pocet 
        # takovychto stringu a secte jejich hodnoty.
        elif str_slovo.isdecimal() == True:
            int_pocet_cisel = int_pocet_cisel + 1
            int_suma_cisel = int_suma_cisel + int(str_slovo)

        # Zjisti delku jednotlivych slov textu pro vytvoreni sloupcoveho grafu
        # a naplni jimi prazdny list_graf.
        int_delka_slova = len(str_slovo)
        list_graf.append(int_delka_slova)

    print(f"There are {int_pocet_slov} words in the selected text.")
    print(f"There are {int_pocet_prvni_velke_pismeno} titlecase words.")
    print(f"There are {int_pocet_velka_pismena} uppercase words.")
    print(f"There are {int_pocet_mala_pismena} lowercase words.")
    print(f"There are {int_pocet_cisel} numeric strings.")
    print(f"The sum of all the numbers {int_suma_cisel}")

    # Serazeni delek slov v listu list_graf pr.: [2, 3, 2, 1] -> [1, 2, 2, 3]
    list_graf.sort()

    # print(f"Serazeny list:{list_graf}")

    # Vytvori novy list s promennym poctem hodnot nula. Pocet hodnot od 1 do 
    # poctu pismen nejdelsiho slova v textu. Slouzi jako inicializace listu 
    # pro pozdejsi praci s nim. Pr.: [] -> [0, 0, 0, 0, 0, 0, 0]
    novy_list = []

    for _ in range(list_graf[-1] + 1):
        novy_list.append(0)

    # Cyklus secte stejne delky slov a ulozi je do listu. Pocet slov 
    # o velikosti dvou znaku je v listu na pozici 2, pocet slov o velikosti
    # tri znaky je v listu na pozici 3 atd. 
    # Pr.: [0, 0, 0, 0, 0] -> [1, 1, 9, 6, 11]
    for int_idx in list_graf:
        novy_list[int_idx] = novy_list[int_idx] + 1

    # print(f"novy_list: {novy_list}")

    # Cyklus vypocita pocet hvezdicek, mezer a vykresli sloupcovy graf.
    int_odsazeni = 20 # Pocet znaku mezi svislymi carami: x|     |x 

    # Vypocet mezery vlevo od OCCURENCES.
    str_mezera = " " * ((int_odsazeni - 10) // 2)

    # Vypocet mezery vpravo od OCCURENCES.
    str_zbytek = " " * (int_odsazeni - 10 - ((int_odsazeni - 10) // 2))

    print("-" * 40)
    print(f"LEN|{str_mezera}OCCURENCES{str_zbytek}|NR.")
    print("-" * 40)

    for int_idx in range(1, len(novy_list)):
        
        # Doplni pocet hvezdicek podle poctu slov v dane kategorii.
        str_pocet_hvezdicek = "*" * novy_list[int_idx]

        # Dopocita mezeru mezi hvezdickami a poctem slov na konci. 
        # V novy_list[int_idx] je ulozen pocet hvezdicek pro jednotlivy radek.
        str_mezera = " " * (int_odsazeni - novy_list[int_idx])
        
        # Pokud je cislo od 1 do 9 tak posun zobrazeni o tri znak doprava.
        if int_idx <= 9:
            print(f"  {int_idx}|{str_pocet_hvezdicek}{str_mezera}|{novy_list[int_idx]}")     
        else: 
            print(f" {int_idx}|{str_pocet_hvezdicek}{str_mezera}|{novy_list[int_idx]}")