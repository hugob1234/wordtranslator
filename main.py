x = True
while x == True:
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!/napisz end jak chcesz przestac): ")
    library = {
    "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
    "LOL": "Częsta reakcja na coś zabawnego",
    "ROFL": "odpowiedź na żart",
    "SHEESH" : "lekka dezaprobata",
    "CREEPY": "straszny, złowieszczy",
    "AGGRO": "stać się agresywnym/zły",
    }
    if word in library.keys():
        print(library[word])
    else:
        print("ERROR")
