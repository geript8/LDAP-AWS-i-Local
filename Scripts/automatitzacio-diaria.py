import os
from datetime import datetime

print("Iniciant tasques automatiques diaries...")

os.system("python3 backup.py")
print("Backup diari fet.")

resultat = os.system("systemctl is-active --quiet slapd")
if resultat == 0:
    print("LDAP: actiu.")
else:
    print("LDAP: inactiu! Reiniciant...")
    os.system("systemctl restart slapd")

resultat = os.system("systemctl is-active --quiet smbd")
if resultat == 0:
    print("Samba: actiu.")
else:
    print("Samba: inactiu! Reiniciant...")
    os.system("systemctl restart smbd")
print("Tasques diaries completades: " + datetime.now().strftime("%Y-%m-%d %H:%M"))

