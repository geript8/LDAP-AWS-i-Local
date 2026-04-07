**1. Fase de planificació**  
- Definir els objectius generals del projecte.  
- Identificar les necessitats del sector i de les empreses tipus.  
- Dissenyar l’esquema del sistema: LDAP/Samba, usuaris, grups i permisos.  
- Elaborar el cronograma de treball i el guió d’execució.  
**2. Fase d’instal·lació i configuració inicial**  
- Instal·lació del sistema operatiu (Ubuntu Server).  
- Instal·lació i configuració de Samba 4 i OpenLDAP.  
- Preparació dels entorns local i al núvol (AWS).  
- Configuració inicial de xarxa i seguretat bàsica.  
**3. Fase de configuració del sistema**  
- Creació d’usuaris, grups i unitats organitzatives (OU).  
- Assignació de permisos automàtica segons grups.  
- Configuració de polítiques de seguretat (contrasenyes, restriccions, MFA).  
- Configuració de recursos compartits via Samba.  
**4. Fase de seguretat i xarxa**
- Configuració de firewall (UFW).  
- Implementació de VPN per accés remot segur (OpenVPN).  
- Control d’accessos i restriccions segons departament i rol.  
**5. Fase de replicació i alta disponibilitat**  
- Replicació del servei LDAP entre servidor local i AWS.  
- Garantia de continuïtat del servei en cas de fallada.  
- Configuració de servidors en rèplica per redundància.  
**6. Fase de còpies de seguretat**  
- Configuració de backups automatitzats (dades i configuració LDAP).  
- Scripts automatitzats en Bash o Python.  
- Proves de restauració ràpida.  
**7. Fase de monitoratge i control**  
- Instal·lació d’eines de monitoratge (Nagios o Zabbix).  
- Configuració d’alertes en cas de fallada dels serveis (LDAP, Samba, VPN).  
- Control del rendiment i disponibilitat del sistema.  
**8. Fase de proves**  
- Verificació del correcte funcionament dels serveis.  
- Proves d’autenticació d’usuaris en Windows i Linux.  
- Proves de replicació, accés remot i restauració de dades.  
- Correcció d’errors detectats durant les proves.  
**9. Fase de documentació i presentació**  
- Elaboració de la documentació tècnica del projecte.  
- Redacció de la memòria del projecte.   
- Preparació de la presentació final amb esquemes, diagrames i captures de pantalla.  
