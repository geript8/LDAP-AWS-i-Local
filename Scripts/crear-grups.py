import os

LDAP_ADMIN    = "cn=admin,dc=empresa,dc=local"
LDAP_PASSWORD = "Patata123*"
FITXER_CSV    = "grups.csv"
FITXER_LDIF   = "grups_processats.ldif"

csv  = open(FITXER_CSV, "r")
ldif = open(FITXER_LDIF, "w")

for linia in csv:
    dades = linia.strip().split(",")
    grup  = dades[0]
    gid   = dades[1]
    ldif.write("dn: cn=" + grup + ",ou=Administracio,dc=empresa,dc=local\n")
    ldif.write("objectClass: posixGroup\n")
    ldif.write("cn: " + grup + "\n")
    ldif.write("gidNumber: " + gid + "\n\n")
csv.close()
ldif.close()

print("Pas 1 completat: fitxer LDIF de grups generat correctament.")

os.system("ldapadd -x -D 'cn=admin,dc=empresa,dc=local' -w Patata123* -f grups_processats.ldif")

print("Fet! Tots els grups del CSV ja estan creats.")
