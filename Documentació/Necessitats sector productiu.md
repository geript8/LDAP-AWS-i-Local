# Necessitats sector productiu
**Gestió centralitzada d’usuaris i permisos**  
**Necessitat:** les empreses tenen molts ordinadors i usuaris i gestionar-los un a un és ineficient.  
**Solució del projecte:** LDAP centralitzat + Samba AD per gestionar tots els usuaris i grups des d’un únic lloc.  

**Seguretat en l’accés**  
**Necessitat:** controlar qui pot accedir a dades sensibles i protegir-les d’accessos no autoritzats.  
**Solució del projecte:** autenticació centralitzada, restriccions de permisos per grups i polítiques equivalents a GPO.  

**Accés remot segur**  
**Necessitat:** treballadors que necessiten accedir a la xarxa des de casa o sucursals.  
**Solució del projecte:** VPN + firewall configurat correctament per permetre accés segur.  

**Recuperació davant fallades**
**Necessitat:** si el servidor cau, recuperar dades i configuració ràpidament.  
**Solució del projecte:** replicació LDAP AWS i backups automatitzats.


**Estalvi de temps i reducció d’errors**  
**Necessitat:** evitar errors humans en la creació i modificació de comptes.  
**Solució del projecte:** gestió centralitzada i automatització de permisos i recursos compartits.

**Monitoratge i control** 
**Necessitat:** saber si els serveis funcionen correctament i rebre alertes davant fallades.  
**Solució del projecte:** monitoratge opcional amb Nagios/Zabbix
