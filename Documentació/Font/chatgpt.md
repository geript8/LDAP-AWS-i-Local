# Implementació d’un entorn LDAP centralitzat local i al núvol (AWS) per a la gestió d’usuaris, permisos i polítiques de seguretat
## Problema a resoldre

Moltes petites i mitjanes empreses no disposen d’un sistema centralitzat que permeti administrar de manera eficient els usuaris, els permisos d’accés i les polítiques de seguretat dins de la seva infraestructura informàtica. Aquesta manca de centralització genera diversos problemes operatius i de seguretat que poden afectar directament la productivitat, la protecció de la informació i la continuïtat del negoci.

Entre els principals problemes detectats destaquen els següents:

1. **Gestió manual i poc eficient dels usuaris**   
    L’alta, modificació i baixa de comptes d’usuari s’ha de realitzar de manera individual en cada equip o servei, fet que incrementa el temps de gestió, dificulta l’administració i augmenta la probabilitat d’errors humans.

1. **Riscos elevats de seguretat**    
    L’absència d’un control centralitzat dels accessos impedeix aplicar criteris homogenis de seguretat i pot provocar accessos indeguts a recursos sensibles, fuites d’informació i una major exposició a vulnerabilitats internes o externes.

    Dificultats en la recuperació davant incidències i en la continuïtat del negoci
    En cas de fallada del servidor, corrupció de dades o pèrdua d’informació, la recuperació pot ser lenta, parcial o complexa, especialment si no existeixen mecanismes de redundància, còpies de seguretat i sincronització entre entorns.

    Manca de polítiques de seguretat homogènies
    Sense una infraestructura centralitzada, resulta difícil aplicar de forma consistent polítiques com restriccions de contrasenya, permisos d’accés, scripts d’inici de sessió, configuracions d’entorn o restriccions sobre els dispositius dels usuaris.

1. **Escalabilitat limitada**    
    A mesura que l’empresa creix i augmenta el nombre d’usuaris, equips i serveis, la gestió descentralitzada esdevé cada cop més difícil de mantenir, menys eficient i més costosa en termes tècnics i organitzatius.

1. **Manca de traçabilitat i auditoria**    
    Sense un sistema centralitzat, és complicat registrar, supervisar i auditar qui accedeix a cada recurs, quan ho fa i amb quins permisos, fet que dificulta el compliment de requisits de seguretat i normativa.

1. **Dependència excessiva d’equips o administracions locals**    
    Quan la gestió d’usuaris depèn de configuracions locals en cada màquina o servidor, es genera una infraestructura poc robusta, difícil de mantenir i molt dependent del coneixement tècnic puntual de cada administrador.
1. **Integració deficient entre entorn local i serveis al núvol**    
    Moltes organitzacions treballen amb recursos híbrids, però no disposen d’un mecanisme unificat d’autenticació i control d’accés entre la infraestructura local i els serveis desplegats al núvol, fet que complica la gestió i incrementa els riscos operatius.

