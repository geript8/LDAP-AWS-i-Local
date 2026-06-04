import os
from datetime import datetime

data = input("Quina data vols restaurar? (YYYY-MM-DD): ")
dir_backup = "/backups/" + data

if not os.path.exists(dir_backup):
    print("Error: No existeix cap backup de la data " + data)
    exit()

print("Iniciant restauracio del " + data + "...")

os.system("slapadd -l " + dir_backup + "/ldap.ldif")
print("Usuaris LDAP restaurats.")

os.system("tar -xzf " + dir_backup + "/samba.tar.gz -C /")
print("Fitxers Samba restaurats.")

os.system("tar -xzf " + dir_backup + "/configs.tar.gz -C /")
print("Configuracions del sistema restaurades.")

print("Restauracio completada correctament!")
