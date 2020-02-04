- [Notions de sécurité](#orgcfb3afd)
  - [Modélisation de la menace (Threat Model)](#orgd6496c4)
  - [Difficultés de la sécurisation](#orge405ebf)
  - [Sécurisation d'une application : Authentification  et Autorisation](#org0debcdc)
  - [Spécificité des technologies web](#org3c693e3)
- [Authentification](#org9d202d4)
  - [Authentification locale](#org0959026)
  - [Authentification externalisée](#orgfdf0211)
  - [Page d'accueil et contrôleur](#org8689510)
  - [Protection basée sur les URL](#org03d8164)
  - [OAuth2](#orgd172acf)
  - [Ajout de javascript côté client](#orgf7fc998)
  - [Extraction d'informations sur l'utilisateur connecté](#orgaedd41a)
  - [Logout](#orgacf2b71)
  - [CSRF](#orga7a92fa)
  - [Sécurisation au niveau des méthodes](#orgdb03f60)
  - [Affectation de rôles en fonction d'information depuis le serveur OAuth 2.0](#orgaa51572)
- [Mise en œuvre](#org9247620)
  - [Protections plus complexes au niveau des méthodes](#orga48ffd0)
  - [CRUD](#org276466a)
  - [Client Angular 6](#orgd2fa4a1)
- [Pour aller plus loin](#orgdf8dbe2)
  - [Content Security Policy](#org118a271)
  - [SSL](#org00c2469)
  - [OWASP](#orgffef12b)



<a id="orgcfb3afd"></a>

# Notions de sécurité


<a id="orgd6496c4"></a>

## Modélisation de la menace (Threat Model)

La première étape d'une démarche de sécurisation est la [modélisation de la menace](https://en.wikipedia.org/wiki/Threat_model). En effet, selon que vous soyez chargé de protéger les secrets nucléaires Français contre la NSA, le GRU et le MSS, ou que vous ayez à protéger les résultats sportifs de votre association locale de tennis de table, les enjeux ne seront pas les mêmes. Il faut donc identifier ce que vous avez à protéger, qui serait intéressé à chercher un accès non autorisé et quel point.


<a id="orge405ebf"></a>

## Difficultés de la sécurisation

On pourrait penser que la sécurisation n'est qu'une partie des spécifications comme les autres et qu'il suffit que son implémentation ne soit pas buggée pour que l'application soit sécurisée.

La différence fondamentale réside dans la classe des bugs à éradiquer. Alors que dans le cadre d'une utilisation normale, l'utilisateur ne rencontrera des bugs qu'accidentellement, un utilisateur hostile recherchera activement des bugs à exploiter.

Pour cette raison, il est essentiel d'être particulièrement vigilant quand à la qualité du code. Non seulement il faut éviter de "réinventer la roue" soi-même, mais il ne faut pas se fier à n'importe quel conseil [trouvé sur internet](https://blog.acolyer.org/2018/06/27/secure-coding-practices-in-java-challenges-and-vulnerabilities/).


<a id="org0debcdc"></a>

## Sécurisation d'une application : Authentification  et Autorisation

On distingue généralement l'[authentification](https://en.wikipedia.org/wiki/Electronic_authentication) et l'[autorisation](https://en.wikipedia.org/wiki/Authorization). L'authentification consiste à l'assurer de l'identité de l'utilisateur, et l'autorisation consiste à déterminer les droits d'accès associés à l'utilisateur en fonction de son identité et plus précisément en fonction des rôles (cf. cas d'utilisation) associés cette identité.


<a id="org3c693e3"></a>

## Spécificité des technologies web

Dans le cadre d'un système client-serveur où le client est un navigateur web, il est essentiel de réaliser que l'on a aucun contrôle sur le code exécuté par le client et donc sur les requêtes que celui-ci envoie au serveur. **Par défaut**, on peut supposer que l'utilisateur se contentera d'envoyer les requêtes prévues lors de la conception du client. Cependant, l'utilisateur garde la possibilité d'exécuter le code de son choix, notamment par la console javascript. Pour cette raison, toutes les validations et restrictions seront au moins implémentées côté serveur. On peut en implémenter côté client pour permettre un retour plus rapide (sans attendre d'aller-retour sur le réseau), mais on ne se contentera **jamais** d'une vérification côté client.

Aussi, toute implémentation réelle devra **évidemment** utiliser SSL pour **toutes** les communications, voire avec en plus du *certificate pinning* (ou [HTTP Public Key Pinning](https://fr.wikipedia.org/wiki/HTTP_Public_Key_Pinning)), même s'il [y a des soucis qui ont amené Chrome à ne plus le supporter](https://news.ycombinator.com/item?id=15572143) et que d'[autres solutions sont explorées](https://en.wikipedia.org/wiki/Certificate_Transparency).


<a id="org9d202d4"></a>

# Authentification

Pour l'authentification, on a principalement deux possibilités : une gestion locale ou une gestion externalisée.


<a id="org0959026"></a>

## Authentification locale

L'authentification est généralement basée sur des association de login et mot de passe. Lors d'une requête de connections, le mot de passe envoyé est validé ou non en fonction du mot de passe déclaré à l'inscription (ou modifié ultérieurement).

Le mot de passe lui-même est considéré comme une information confidentielle, notamment parce qu'il est souvent réutilisé pour des authentifications dans différents systèmes. Pour cette raison, il ne doit **jamais** être stocké en clair dans une base de données. On [utilisera un hachage](https://o7planning.org/en/11705/create-a-login-application-with-spring-boot-spring-security-jpa#a13944416), par exemple avec [BCryptPasswordEncoder](https://docs.spring.io/spring-security/site/docs/4.2.4.RELEASE/apidocs/org/springframework/security/crypto/bcrypt/BCryptPasswordEncoder.html). La fonction de hachage est telle qu'il suffit de comparer les résultats de hachage au lieu de comparer les mots de passe :

\( bcrypt(receivedPassword) = bcrypt(storedPassword) \\ \iff receivedPassword = storedPassword \)

mais il serait impossible (ou prohibitivement coûteux) de retrouver le mot de passe stocké \(storedPassword\) à partir de la valeur stockée en base \(bcrypt(storedPassword)\).

La [simple implémentation d'une authentification locale](https://medium.com/@gustavo.ponce.ch/spring-boot-spring-mvc-spring-security-mysql-a5d8545d837d) requiert d'avoir des tables/repositories/services pour les entités représentant les utilisateurs et pour leurs rôles. De plus, dans on contexte de Système d'Informations interne, on ne voudra généralement pas avoir un profil utilisateur par application. Pour ces raisons, on pourra préférer externaliser l'authentification, notamment par un mécanisme d'[Authentification unique](https://fr.wikipedia.org/wiki/Authentification_unique) (SSO pour *Single Sign On*).


<a id="orgfdf0211"></a>

## Authentification externalisée

[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth#OAuth_2.0) est un protocole largement utilisé pour déléguer l'authentification. On va utiliser son implémentation dans la version la plus récente de spring boot. OAuth 2.0 permet non seulement l'authentification, mais aussi l'autorisation concernant les services directement offerts par le prestataire OAuth 2.0 (par exemple d'accès/modification aux posts pour Facebook, aux dépôts git pour github, etc.). On va utiliser Github comme prestataire OAuth 2.0 pour les exercices suivants.

-   **Exercice:** Créer un nouveau projet Spring boot avec les caractéristiques suivantes :
    -   **package:** co.simplon.oauth2
    -   **version de spring boot:** 2.2.4
    -   **dépendences:** -   Security
        -   Web

-   **Exercice:** Ajouter les dépendances suivantes au projet :
    
    ```xml
        <dependency>
    	<groupId>org.springframework.security.oauth</groupId>
    	<artifactId>spring-security-oauth2</artifactId>
        </dependency>
    
        <dependency>
          <groupId>org.springframework.security.oauth.boot</groupId>
          <artifactId>spring-security-oauth2-autoconfigure</artifactId>
        </dependency>
    ```

-   **Exercice:** Configurer le port du serveur pour qu'il se lance en écoutant sur le port 8090 (ce sera utile pour la suite).

Afin de pouvoir observer des traces des mécanismes de sécurité, définir aussi les propriétés suivantes:

```properties
logging.level.org.springframework.security=DEBUG
logging.level.org.springframework.security.web.FilterChainProxy: DEBUG
```


<a id="org8689510"></a>

## Page d'accueil et contrôleur

-   **Exercice:** -   Créer une page index.html dans le répertoire `src/main/resources/static`
        
        ```html
              <!doctype html>
              <html lang="en">
        	<head>
        	  <meta charset="utf-8" />
        	  <title>Demo spring security OAuth2</title>
        	</head>
        	<body>
        	  Welcome !
        	</body>
              </html>
        ```
    -   Créer une classe annotée `@Controller` (voire `RestController`) avec un `RequestMapping` sur `/np/private` qui retourne la chaîne de caractères `"private"`.
    -   Lancer le programme en regardant les logs.
    -   Aller à l'adresse <http://localhost:8090/> en regardant quelles requêtes sont envoyées par le navigateur et quels cookies sont déposés.
    -   À la page de login, se connecter avec login `user` et le mot de passe généré indiqué dans les logs.
    -   Aller à <http://localhost:8090/np/private/>
    -   Supprimer les cookies associés à ce site et recharger la page.


<a id="org03d8164"></a>

## Protection basée sur les URL

Créer la classe suivante :

```java
  package co.simplon.oauth2;

  import org.springframework.context.annotation.Configuration;
  import org.springframework.security.config.annotation.web.builders.HttpSecurity;
  import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

  @Configuration
  public class SecurityConfiguration extends WebSecurityConfigurerAdapter{

      @Override

      protected void configure(HttpSecurity http) throws Exception {
	  http.antMatcher("/**").authorizeRequests()
	      .antMatchers("/","/login**", "/error**").permitAll()
	      .anyRequest().authenticated();
      }
  }
```

Cette classe, qui doit porter l'annotation `@Configuration` pour être prise en compte dans la configuration de notre application, créer un *filtre* d'autorisation pour toutes les requêtes à partir de la racine (`antMatcher("/**")`) tel que :

1.  les urls de la racine, celles situées sous `/login` et sous `/error` sont autorisées

2.  toutes les autres exigent d'êtres authentifié.

L'ordre des règles est important ! Dès qu'une requête active une règle (dans l'ordre de leurs déclarations), c'est celle-ci qui est activée.

-   **Exercice:** tester l'accès à la racine, puis `/np/private`.
-   **Exercice:** Même chose en intervertissant les deux règles.

-   **Important !:** La formulation (*whitelisting*) qui consiste à indiquer explicitement les page autorisées et interdit par défaut tout le reste est **essentielle**. En effet, en cas d'oubli (ou plus exactement lors d'un oubli), les utilisateurs feront un rapport de bug pour se plaindre de ne pas avoir accès à une page alors que des adversaires ne se plaindront pas d'avoir accès à une page qui devrait être protégée !

Plusieurs classes peuvent ainsi être définies pour décomposer la configuration de sécurisation des URL, mais seule la première règle activée aura un effet. On peut indiquer l'ordre (en utilisant l'annotation [@Order](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/core/annotation/Order.html) sur la classe) dans lequel les différentes classes de configuration doivent être considérées. En pratique, on restreindra souvent les différentes classes de configuration à des chemins différents par l'appel initial à `antMatcher`.


<a id="orgd172acf"></a>

## OAuth2

-   **Exercice:** Configurer les [propriétés OAuth2](https://docs.spring.io/spring-boot/docs/current-SNAPSHOT/reference/htmlsingle/#boot-features-security-oauth2) propriétés suivantes :

```properties
security.oauth2.client.client-id= 7045a59b0f0c7a9dac46
security.oauth2.client.client-secret= 583daf81b2a22782bc9172d7a5a392e2d70a6f62
security.oauth2.client.access-token-uri= https://github.com/login/oauth/access_token
security.oauth2.client.user-authorization-uri= https://github.com/login/oauth/authorize
security.oauth2.client.client-authentication-scheme= form
security.oauth2.resource.user-info-uri= https://api.github.com/user
```

Le couple `client-id` / `client-secret` est celui qui identifie notre application auprès du prestataire de service `OAuth2` (ici Github). Une application [a été enregistrée](https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/) pour l'adresse `localhost:8090` et le couple d'identifiant/secret a été attribué à cette application. Comme le service gratuit est bridé, on pourra avoir intérêt à en enregistrer une autre (avec l'url de la racine comme callback).

-   **Exercice:** -   Ajouter l'annotation `@EnableOAuth2Sso` à la classe `SecurityConfiguration`.
    -   Se déconnecter de github par exemple en allant sur <https://github.com/logout>.
    -   Aller sur la pages d'acceuil et sur `/np/private`.

Pour plus de convivialité, ajouter un lien dans la page d'accueil :

```html
<div class="container unauthenticated">
       <div>
            Login with Github: <a href="/login">click here</a>
        </div>
    </div>
```

-   **Exercice:** Observer les redirections lorsqu'on clique sur le lien ajouté, notamment lorsqu'on efface les cookies associés à <http://localhost:8090> et/ou à <https://github.com>.


<a id="orgf7fc998"></a>

## Ajout de javascript côté client

Pour utiliser javascript côté client, on pourrait charger les bibliothèques depuis un CDN, mais on peut aussi les héberger directement sur notre serveur. Pour les plus répandues, il y a déjà des dépendances maven.

-   **Exercice:** Ajouter les dépendances suivantes :

```xml
  <dependency>
      <groupId>org.webjars</groupId>
      <artifactId>js-cookie</artifactId>
      <version>2.1.0</version>
  </dependency>
  <dependency>
      <groupId>org.webjars</groupId>
      <artifactId>jquery</artifactId>
      <version>2.1.1</version>
  </dependency>
  <dependency>
      <groupId>org.webjars</groupId>
      <artifactId>bootstrap</artifactId>
      <version>3.2.0</version>
  </dependency>
  <dependency>
      <groupId>org.webjars</groupId>
      <artifactId>webjars-locator-core</artifactId>
  </dependency>
```

-   **Exercice:** Modifier la page d'accueil pour inclure les bibliothèques suivantes :

```html
<base href="/" />
<link rel="stylesheet" type="text/css"
    href="/webjars/bootstrap/css/bootstrap.min.css" />
<script type="text/javascript" src="/webjars/jquery/jquery.min.js"></script>
<script type="text/javascript"
    src="/webjars/bootstrap/js/bootstrap.min.js"></script>

```

-   **Exercice:** Modifier la configuration d sécurité pour permettre l'accès aux fichiers javascripts et css.

-   **Exercice:** Modifier la page d'accueil pour indiquer le nom de la personne connectée :

```html
  <div class="container unauthenticated">
    <div>
      Login with Github: <a href="/login">click here</a>
    </div>
  </div>
  <div class="container authenticated" style="display: none">
    Logged in as: <span id="user"></span>
  
  </div>
```


<a id="orgaedd41a"></a>

## Extraction d'informations sur l'utilisateur connecté

-   **Exercice:** Ajouter le code suivant à la page d'accueil :

```html
  <script type="text/javascript">
    $.get("/user", function(data) {
    $("#user").html(data.name);
    $(".unauthenticated").hide();
    $(".authenticated").show();
    });
  </script>
```

Pour implémenter la réponse à l'url `/user`, on va utiliser l'interface [java.security.Principal](https://docs.oracle.com/javase/7/docs/api/java/security/Principal.html). Il suffit pour cela d'ajouter un argument de type [java.security.Principal](https://docs.oracle.com/javase/7/docs/api/java/security/Principal.html) à la méthode associée à l'url `/user`. Dans le code javascript, on accède à un attribut nommé `name` de la donnée reçu en réponse à la requête. Ce peut aussi bien être la valeur associée à une clé `"name"` dans un dictionnaire. Implémenter dans le contrôler une méthode qui retourne (au format JSON) une `Map<String, String>` associant la clé `"name"` au nom contenu dans l'instance de `Principal` reçue en argument.

Si l'on avait voulou d'autres informations que celles fournies par l'interface [java.security.Principal](https://docs.oracle.com/javase/7/docs/api/java/security/Principal.html), on aurait pu de la même façon récupérer un argument de type [Authentication](https://docs.spring.io/spring-security/site/docs/4.2.x/apidocs/index.html?org/springframework/security/core/Authentication.html) à la place.


<a id="orgacf2b71"></a>

## Logout

Côté client, on va ajouter à la page d'accueil un bouton de déconnection.

-   **Exercice:** Ajouter à la page d'acceuil un bouton qui exécute le code javascript suivant :

```javascript
  var logout = function() {
      $.post("/logout", function() {
	  $("#user").html('');
	  $(".unauthenticated").show();
	  $(".authenticated").hide();
      })
      return true;
  }
```

Côté serveur, modifier la classe `SecurityConfiguration` pour ajouter aux appels sur l'argument `HttpSecurity` de la méthode `configure` les appels suivants :

```java
.and().logout().logoutSuccessUrl("/").permitAll();
```

-   **Exercice:** Essayer de se connecter et de se déconnecter. Quel problème y a-t-il à la déconnection ?


<a id="orga7a92fa"></a>

## CSRF

Les site **doivent** être protégés contre le [CSRF](https://fr.wikipedia.org/wiki/Cross-site_request_forgery), et c'est la raison pour laquelle la requête de déconnection est refusée avec la configuration de sécurité par défaut.

-   **Exercice:** Désactiver la protection contre csrf sur tout le site avec les appels de méthodes suivants:
    
    ```java
    	      .csrf().disable()
    ```

Évidemment, on voudra plutôt modifier notre client pour qu'il prenne en compte la protection contre CSRF. C'est d'ailleurs pour cela qu'on avait ajouté la dépendance à la bibliothèque javascript d'accès aux cookies à notre projet.

-   **Exercice:** Ajouter la dépendance à la bibliothèque d'accès aux cookies sur la page d'acceuil :
    
    ```html
    		    <script type="text/javascript" src="/webjars/js-cookie/js.cookie.js"></script>
    ```
    
    et ajouter l'exécution du code suivant :
    
    ```javascript
    		 $.ajaxSetup({
    		     beforeSend : function(xhr, settings) {
    			 if (settings.type == 'POST' || settings.type == 'PUT'
    			     || settings.type == 'DELETE' || settings.type == 'GET' ) {
    			     if (!(/^http:.*/.test(settings.url) || /^https:.*/
    				   .test(settings.url))) {
    				 // Only send the token to relative URLs i.e. locally.
    				 xhr.setRequestHeader("X-XSRF-TOKEN", Cookies
    						      .get('XSRF-TOKEN'));
    				}
    			 }
    		     }
    		 });
    ```
    
    Refaire un cycle de connection / déconnection en ayant enlevé `.csrf().disable()` et en mettant `.and().csrf().csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse())` la place côté serveur et observer les requêtes, notamment au niveau des entêtes.


<a id="orgdb03f60"></a>

## Sécurisation au niveau des méthodes

On peut aussi définir des restrictions d'accès au niveau de méthodes, par exemple au niveau des services. Pour cela il faut d'abord activer cette possibilité avec l'annotation [@EnableGlobalMethodSecurity](https://docs.spring.io/spring-security/site/docs/4.2.6.RELEASE/apidocs/org/springframework/security/config/annotation/method/configuration/EnableGlobalMethodSecurity.html).

-   **Exercice:** -   Mettre l'annotation `@EnableGlobalMethodSecurity(securedEnabled = true)` sur la classe `SecurityConfiguration`.
    -   Rendre accessible sans restriction toutes les url sous `/np` dans la méthode `configure(HttpSecurity)` de cette classe.
    -   Dans un contrôleur, définir les méthodes suivantes :
        
        ```java
            	@RequestMapping("/np/private")
        	public String privateInfo() {
        		return myService.privateInfo();
        	}
        	
        	@RequestMapping("/np/admin")
        	public String adminInfo() {
        		return myService.adminInfo();
        	}
        	@RequestMapping("/np")
        	public String np() {
        		return myService.publicInfo();
        	}
        ```
        
        avec un attribut `MyService myService;` injecté.
    -   Dans une classe `MyService` injectable, définir les méthodes suivantes :
        
        ```java
              public String publicInfo() {
        	  return "for anybody";
              }
              public String adminInfo() {
        	  return "for admin only";
              }
              public String privateInfo() {
        	  return "for user";
              }
        ```
        
        et restreindre l'accès aux deux dernières aux rôles administrateur (`ROLE_ADMIN`) et utilisateur (`ROLE_USER`) grâce l'annotation [@Secured](https://docs.spring.io/spring-security/site/docs/4.2.4.RELEASE/apidocs/org/springframework/security/access/annotation/Secured.html).
    -   Tester l'accès à ces URL.


<a id="orgaa51572"></a>

## Affectation de rôles en fonction d'information depuis le serveur OAuth 2.0

On va donner à l'utilisateur le rôle d'administrateur s'il est membre, **de façon publique**, de l'organisation `simplonco`.

-   **Exercice:** Ajouter les méthodes suivantes à la classe `SecurityConfiguration` :
    
    ```java
    		@Bean
    		public OAuth2RestTemplate oauth2RestTemplate(OAuth2ProtectedResourceDetails resource
    							     , OAuth2ClientContext context) {
    		    return new OAuth2RestTemplate(resource, context);
    		}
    
    		@Bean
    		public AuthoritiesExtractor authoritiesExtractor(OAuth2RestOperations template) {
    		    return new GithubOrgsAuthoritiesExtractor(template);
    		}
    ```
    
    L'annotation [@Bean](https://docs.spring.io/spring-javaconfig/docs/1.0.0.M4/reference/html/ch02s02.html) permet d'utiliser les objets retournés par ces méthodes pour de l'injection de dépendances. Il faut bien sûr aussi définir la classe `GithubOrgsAuthoritiesExtractor` :
    
    ```java
    		class GithubOrgsAuthoritiesExtractor implements AuthoritiesExtractor{
    	
    		    private OAuth2RestOperations template;
    	
    		    GithubOrgsAuthoritiesExtractor(OAuth2RestOperations template){
    			this.template= template;
    		    }
    
    		    @Override
    		    public List<GrantedAuthority> extractAuthorities(Map<String, Object> map) {
    			String url = (String) map.get("organizations_url");
    			System.err.println("url:"+url);
    			@SuppressWarnings("unchecked")
    			    List<Map<String, Object>> orgs = template.getForObject(url, List.class);
    			System.err.println("orgs:"+orgs);
    			for(Map<String, Object> org : orgs) {
    			    if("simplonco".equals(org.get("login"))) {
    				return AuthorityUtils.commaSeparatedStringToAuthorityList("ROLE_USER, ROLE_ADMIN");
    			    }
    			}
    			return AuthorityUtils.commaSeparatedStringToAuthorityList("ROLE_USER");
    			//	throw new BadCredentialsException("Not in required organization");
    
    		    }
    		}
    ```
    
    Tester l'accès à la ressource restreinte au rôle d'administrateur. Éventuellement, créer une autre organisation github, s'y inscrire et rendre publique son appartenance à celle-ci. Modifier le code pour qu'il utilise cette nouvelle organisation et tester nouveau.


<a id="org9247620"></a>

# Mise en œuvre


<a id="orga48ffd0"></a>

## Protections plus complexes au niveau des méthodes

Tester les annotations [@PreAuthorize et @PostAutorize](http://www.baeldung.com/spring-security-method-security).


<a id="org276466a"></a>

## CRUD

Implémenter la sécurisation d'un CRUD


<a id="orgd2fa4a1"></a>

## Client Angular 6

Implémenter la [sécurisation avec un client Angular 6](http://www.baeldung.com/spring-security-oauth-authorization-code-flow).

Pour la protection contre le [CSRF](https://fr.wikipedia.org/wiki/Cross-site_request_forgery) à l'aide d'un token dans les entêtes HTTP qui doit être ajouté par javascript, et qui empêche les simples liens [Vous avez gagné !!!!!](https://mysitesecuredwithcookies.com/send/myMoney) de marcher, on aurait pas gagné grand chose s'il était possible à un adversaire (par exemple <https://evil.com> ) d'envoyer du code javascript qui ferait lui aussi l'ajout du token dans l'entête de la requête vers le site sécurisé. C'est pour empêcher cela que les navigateurs implémentent le [Same Origin Policy (SOP)](https://en.wikipedia.org/wiki/Same-origin_policy) qui interdit à du code javascript chargé depuis un serveur (e.g.<https://evil.com>) d'envoyer des requêtes vers un serveur différent (e.g. <https://my-secured-site.com>).

Évidemment, cela poserait des problèmes non seulement pour l'utilisation de web services, mais aussi pour le développement d'applications Angular qui sont (en cours de développement) servies par un serveur dédié (par exemple en <http://localhost:4200>) différent du serveur backend (par exemple en <http://localhost:8090>).

La solution à ce problème est offerte par le mécanisme de [Cross Origin Resource Sharing (CORS)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) qui permet à un serveur (par exemple le backend en <http://localhost:8090>) d'indiquer aux navigateurs webs quels autres serveurs (par exemple le serveur de développement angular en <http://localhost:4200>)sont autorisés à envoyer du code javascript qui pourra faire des requêtes qui lui sont destinées.

Avec Spring, il est [facile d'activer le CORS](https://spring.io/blog/2015/06/08/cors-support-in-spring-framework) à différents niveaux de granularité, comme pour les autres mécanismes d'autorisation.


<a id="orgdf8dbe2"></a>

# Pour aller plus loin


<a id="org118a271"></a>

## Content Security Policy

La protection en fonction de l'origine du code Javascript exécuté offerte par Same Origin Policy peut aussi être étendue, notamment aux bibliothèques Javascript utilisée. La standardisation des entêtes définissant la [Content Security Policy](https://en.wikipedia.org/wiki/Content_Security_Policy) permet de répondre à ces besoins. Bien sûr, [Spring Security permet de mettre en œuvre ces protections](https://docs.spring.io/spring-security/site/docs/current/reference/html/headers.html).


<a id="org00c2469"></a>

## SSL

Aucune des autres protection ne pourra être efficace si l'attaquant peut intercepter les communications ([Man In the Middle](https://fr.wikipedia.org/wiki/Attaque_de_l%27homme_du_milieu)). Pour éviter cela, il **faut** utiliser HTTPS (et donc un certificat SSL). Dans un environnement *corporate*, cela sera pris en charge au niveau de l'entreprise. Pour un projet personnel, on peut utiliser un certificat délivré par [Let's Encrypt](https://letsencrypt.org/). Le processus [peut être automatisé pour une application Spring Boot](https://github.com/creactiviti/spring-boot-starter-acme).


<a id="orgffef12b"></a>

## OWASP

Dans le domaine de la sécurité encore plus que tout autre, il est indispensable de faire de la veille pour se tenir à jour des dernières vulnérabilité / bonnes pratiques. La lecture régulières des documents publiés par [OWASP](https://www.owasp.org/index.php/Main_Page) (cf. [sécurisation de REST](https://www.owasp.org/index.php/REST_Security_Cheat_Sheet)) est indispensable.
