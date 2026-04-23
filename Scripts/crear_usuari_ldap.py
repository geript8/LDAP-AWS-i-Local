import os

usuari = input("Usuari: ")
nom = input("Nom Complet :")
cognom =input("Cognom: ")
password = input("Contrassenya :")

fitxer = open("usuari.ldif", "w")

fitxer.write("dn: uid=" + usuari + ",ou=users,dc=empresa,dc=local\n")
fitxer.write("objectClass: top\n")


fitxer.write("uid: " + usuari + "\n")
fitxer.write("cn: " + nom + "\n")
fitxer.write("sn: " + cognom + "\n")
fitxer.write("uidNumber: 10001\n")
fitxer.write("gidNumber: 10001\n")
fitxer.write("homeDirectory: /home/" + usuari + "\n")
fitxer.write("loginShell: /bin/bash\n")
fitxer.write("userPassword: " + password + "\n")

fitxer.close()

os.system("ldapadd -x -D cn=admin,dc=empresa,dc=local -W -f usuari.ldif")
