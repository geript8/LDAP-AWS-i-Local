fitxer = open("usuaris.ldif", "r")
sortida = open("usuaris_processats.ldif", "w")
uid_base = 1000
for linia in fitxer:
    dades = linia.strip().split(",")

    nom = dades[0]
    usuari = dades[1]
    password = dades[2]

    sortida.write("dn: uid=" + usuari + ",dc=empresa,dc=local\n")
    sortida.write("objectClass: inetOrgPerson\n")
    sortida.write("objectClass: posixAccount\n")
    sortida.write("objectClass: shadowAccount\n")
    sortida.write("cn: " + nom + "\n")
    sortida.write("sn: " + nom + "\n")
    sortida.write("uid: " + usuari + "\n")
    sortida.write("uidNumber: " + str(uid_base) + "\n")
    sortida.write("gidNumber: 5000\n")
    sortida.write("homeDirectory: /home/" + usuari + "\n")
    sortida.write("loginShell: /bin/bash\n")
    sortida.write("userPassword: " + password + "\n\n")

    uid_base += 1
fitxer.close()
sortida.close()
