val = input("Entrez votre chaine de caracteres: ")

def word_count(val):
    return val.count(" ") + 1

print("Il y a " + str(word_count(val)) + " mots dans ce que vous avez dit.")
