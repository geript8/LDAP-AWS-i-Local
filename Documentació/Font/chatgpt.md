# Implementació d’un entorn LDAP centralitzat local i al núvol (AWS) per a la gestió d’usuaris, permisos i polítiques de seguretat
## Problema a resoldre

**Necessitats del sector productiu i problema a resoldre**  

Actualment, moltes petites i mitjanes empreses (PIME) no disposen d’un sistema centralitzat que permeti administrar de manera eficient els usuaris, els permisos d’accés i les polítiques de seguretat dins de la seva infraestructura informàtica. Aquesta manca de centralització genera problemes operatius, de seguretat i de manteniment que afecten directament la productivitat, la protecció de la informació i la continuïtat del negoci.  

Una de les principals dificultats és la gestió manual i poc eficient dels usuaris, ja que l’alta, modificació i baixa de comptes s’ha de realitzar individualment en cada equip o servei. Això incrementa el temps de gestió, dificulta l’administració i augmenta el risc d’errors humans.  

A més, existeixen riscos elevats de seguretat, ja que sense un control centralitzat resulta complicat aplicar criteris homogenis d’accés. Això pot provocar accessos no autoritzats a dades sensibles, fuites d’informació i una major exposició a vulnerabilitats.  

També es detecten dificultats en la recuperació davant incidències, ja que en cas de fallada del sistema, corrupció de dades o pèrdua d’informació, la recuperació pot ser lenta o incompleta si no existeixen mecanismes adequats de còpia de seguretat i redundància.  

Una altra problemàtica important és la manca de polítiques de seguretat homogènies, fet que impedeix aplicar de forma consistent restriccions de contrasenya, permisos d’accés, configuracions d’entorn o scripts d’inici de sessió.  

A mesura que l’empresa creix, apareix una escalabilitat limitada, ja que la gestió descentralitzada esdevé cada cop més complexa, menys eficient i més costosa.  

A tot això s’hi suma la manca de traçabilitat i auditoria, que dificulta saber qui accedeix als recursos, quan ho fa i amb quins permisos, complicant el compliment de normatives de seguretat.  

Finalment, moltes empreses pateixen una integració deficient entre entorns locals i al núvol, especialment en infraestructures híbrides, així com una dependència excessiva de configuracions locals i coneixements puntuals dels administradors.  

**Solució proposada: Infraestructura centralitzada amb LDAP i AWS**

Per donar resposta a aquestes necessitats, es proposa la implementació d’un entorn LDAP centralitzat tant en local com al núvol (AWS) que permeti gestionar de forma unificada els usuaris, els permisos i les polítiques de seguretat.  

**Aquesta solució es basa en:**  

LDAP centralitzat + Samba Active Directory per gestionar tots els usuaris i grups des d’un únic punt.  
Autenticació única (Single Sign-On) per permetre als usuaris accedir a tots els recursos amb un sol compte.  
Control d’accés segur, mitjançant permisos per grups i polítiques equivalents a GPO.  
Accés remot segur, gràcies a la implementació d’una VPN i configuració adequada de firewall.  
Replicació LDAP al núvol (AWS) per garantir alta disponibilitat i tolerància a fallades.  
Backups automatitzats per assegurar la recuperació de dades en cas d’incidències.  
Automatització de processos, reduint errors humans en la gestió de comptes i permisos.  
Monitoratge del sistema amb eines com Nagios o Zabbix per detectar incidències i rebre alertes.  

**Beneficis per a les PIME**  

Amb aquesta infraestructura, les empreses poden disposar de:  

Gestió centralitzada d’usuaris i permisos  
Autenticació única per a tots els equips i serveis  
Accés segur des de qualsevol ubicació  
Sistemes de backup i recuperació eficients  
Control total sobre recursos compartits i polítiques de seguretat  
Alta disponibilitat gràcies a la replicació al núvol  
Millora en la seguretat, escalabilitat i eficiència operativaol, fet que complica la gestió i incrementa els riscos operatius.

