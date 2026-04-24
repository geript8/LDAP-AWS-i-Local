fitxer = open("usuaris.ldif", "r")
sortida = open("usuaris_processats.ldif", "w")

for linia in fitxer:
    dades = linia.strip().split(",")

    nom = dades[0]
    usuari = dades[1]
    password = dades[2]

    sortida.write("dn: uid=" + usuari + ",dc=empresa,dc=local\n")
    sortida.write("objectClass: inetOrgPerson\n")
    sortida.write("cn: " + nom + "\n")
    sortida.write("sn: " + nom + "\n")
    sortida.write("uid: " + usuari + "\n")
    sortida.write("userPassword: " + password + "\n\n")

fitxer.close()
sortida.close()
