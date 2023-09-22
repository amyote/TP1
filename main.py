def word_count():
    val = input("Entrez votre chaine de caracteres: ")
    print("Il y a " + str(val.count(" ") + 1) + " mots dans ce que vous avez dit.")

word_count()
