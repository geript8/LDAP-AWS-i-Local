import os

LDAP_ADMIN    = "cn=admin,dc=empresa,dc=local"
LDAP_PASSWORD = "Patata123*"
FITXER_CSV    = "usuaris.csv"
FITXER_LDIF   = "usuaris_processats.ldif"

csv  = open(FITXER_CSV, "r")
ldif = open(FITXER_LDIF, "w")

uid = 1000

for linia in csv:
    dades    = linia.strip().split(",")
    nom      = dades[0]
    usuari   = dades[1]
    password = dades[2]

    ldif.write("dn: uid=" + usuari + ",dc=empresa,dc=local\n")
    ldif.write("objectClass: inetOrgPerson\n")
    ldif.write("objectClass: posixAccount\n")
    ldif.write("objectClass: shadowAccount\n")
    ldif.write("cn: " + nom + "\n")
    ldif.write("sn: " + nom + "\n")
    ldif.write("uid: " + usuari + "\n")
    ldif.write("uidNumber: " + str(uid) + "\n")
    ldif.write("gidNumber: 5000\n")
    ldif.write("homeDirectory: /home/" + usuari + "\n")
    ldif.write("loginShell: /bin/bash\n")
    ldif.write("userPassword: " + password + "\n\n")

    uid += 1

csv.close()
ldif.close()

print("Pas 1 completat: fitxer LDIF generat correctament.")

os.system("ldapadd -x -D 'cn=admin,dc=empresa,dc=local' -w Patata123* -f usuaris_processats.ldif")

print("Fet! Tots els usuaris del CSV ja estan creats.")
