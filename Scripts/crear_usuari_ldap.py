fitxer = open("usuaris.ldif", "w")

resposta = "s"

while resposta == "s":
    nom = input("Nom: ")
    usuari = input("Usuari: ")
    password = input("Password: ")

    fitxer.write(nom + "," + usuari + "," + password + "\n")

    resposta = input("Vols crear mes usuaris? (s/n): ")

fitxer.close()
