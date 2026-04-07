 Característiques tècniques del projecte

El projecte es basa en la implementació d’un sistema complet amb les següents característiques:

 Autenticació centralitzada
- Implementació d’un servidor LDAP / Samba Active Directory
- Un únic usuari per accedir a tots els equips i serveis
- Gestió centralitzada de comptes, grups i permisos

Estructura d’usuaris i organització
- Creació d’unitats organitzatives (OU) per departaments
- Definició de grups d’usuaris segons rols (administradors, empleats, etc.)
- Assignació de permisos automàtica segons grup

Control d’accés i seguretat
- Sistema de permisos per accedir a recursos i dades
- Polítiques de seguretat:
- Contrasenyes segures
- Restriccions d’accés
- Possibilitat d’afegir autenticació multifactor

 Accés remot segur

- Implementació d’una VPN (OpenVPN)
- Accés a la xarxa des de fora de l’empresa de forma segura
- Protecció mitjançant firewall (UFW)

Compartició de recursos
- Servidor Samba per compartir carpetes
- Permisos assignats segons usuaris i grups
- Accés controlat a documents i recursos interns

 Alta disponibilitat i replicació
- Replicació del servei LDAP entre:
- Servidor local
- Servidor al núvol (AWS)
- Garantia de continuïtat del servei en cas de fallada

Backups automatitzats
- Còpies de seguretat periòdiques de:
Dades
- Configuració LDAP
- Scripts automatitzats (Bash o Python)
- Possibilitat de restauració ràpida

Monitoratge i control
- Supervisió dels serveis amb eines com:
- Nagios o Zabbix
- Alertes en cas de fallada (LDAP, Samba, VPN)
- Control de rendiment del sistema

Infraestructura híbrida (local + núvol)
- Servidor físic o virtual local
- Integració amb AWS (EC2)
- Comunicació segura entre entorns
