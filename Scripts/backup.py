import os
from datetime import datetime

data = datetime.now().strftime("%Y-%m-%d")
directori_backup = "/backups/" + data

os.makedirs(directori_backup, exist_ok=True)

os.system("slapcat -l " + directori_backup + "/ldap.ldif")
os.system("tar -czf " + directori_backup + "/samba.tar.gz /srv/empresa")
os.system("tar -czf " + directori_backup + "/configs.tar.gz /etc/samba /etc/ldap /etc/wireguard /etc/ssh")

print("Backup fet")
