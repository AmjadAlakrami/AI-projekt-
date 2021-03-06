# AI-projekt-
## Syftet
syftet med projektet är att använda bildigenkänning och webkamran för att kontrollera några funktioner i Spotify så som spela nästa och förgående låt och lägga till låtar till en spellista.
## Metod 
### Skapa datasetet
Det jag först började med i det här projektet var att samla in bilder på vinkande händer och tummen upp, och då använde jag ett chrom tillägg som heter [Fatkun Batch](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=sv) som hjälpte mig att ladda ner fleratals bilder på en och samma gång. 
Efter det så började jag med att skapa annotation till alla bilder jag hade. Sedan behövde jag konvertera alla labels jag fick ut från annotering till xml filler. ([Hur man skapar annotation](https://medium.com/@manivannan_data/yolo-annotation-tool-new-18c7847a2186)).
Efter det så är [datasetet](https://github.com/AmjadAlakrami/AI-dataset/tree/master/Dataset) färdig och då kan man börja med träningen i [google colab](https://colab.research.google.com/drive/1PtKLwonDkTzI1cz0AFbjkxgROJ2IIjff#scrollTo=px4fIT-E1gUO). 

### Spotify API
För att kunna använda spotify API så måste man skapa en app på [Spotify Developer](https://developer.spotify.com/dashboard/login). När man ska logga in så använder man samma inloggning som man har på spotify kontot. Sedan så trycker man på "Creat an app" och då få man nämna appen precis som man vill och skriva en kort beskrivning om det (ett streck räknas som en kort beskrivning). Efter det så bockar man av "Desktop App" och trycker på next. Sedan tycker man på NON-COMMERCIAL. Efter det så bockar man av alla tre rutor och trycker på submit. Efter det så borde en liknande sida komma upp: 

![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(22).png)

Då trycker man på "Edit setting" längs upp till höger, och då lägger man till "https://www.google.com/" i "Redirect URIs" rutan och trycker sedan på save. Därefter så behöver du kopiera din Client ID och Client Secret som finns under appen namn på vänset sidan (tryck på Show clien secret för att få fram den) och spara de någonstans där du lätt kan komma åt de. Sedan så behöver du ha din spotify användarnamn, och det kan du komma åt genom att logga in på din spotify konto på google, sedan så tycker du på profil/konto, och då borde du kunna hitta den längst upp under Kontoöversikt/profil, kopiera den och spara den med tillsammans med din Client ID och Client Secret. Om du inte hittar ditt användarnamn så kan du gå in på spotify appen på dator, sedan så trycker du på din profilbild högst upp till höger, sedan tycker du på de tryck prickar uneder profilbilden, efter det så trycker du på share/copy profile link. Där efter går du in på din webläsare och klistrar in länken, och då kopierar du allt som finns mellan forward slash som är efter user och frågetecknet.  (bilderna nedan förtydligar var alla knappar finns ifall något var otydlig i beskrivningen) 

![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(22)_LI.jpg) ![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(24)_LI.jpg)
Första sättet att hämta användernamnet![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(25)_LI.jpg)![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(27)_LI.jpg)
Andra sättet att hämtar användarnamnet ![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(30)_LI.jpg)![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(31)_LI.jpg)![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(32)_LI.jpg)

### evaluate.py
#### Vilka Bibliotek behöver man ladda ner:
#### (OBS!! det här steget måste man göra för att test köra mitt program.)
cv2: pip install opencv-python  
spotipy: pip install spotipy  
numpy: pip install numpy  
socket: pip install socket.py  

#### Hur använder man Spotipy:
Först så behöver man importera Biblioteket  
```python  
import spotipy  
import spotipy.util as util  (Det här gör man för enkelhetens skull och man kan strunta i det om man vill)  
```  
Sedan måste man skapa ett token och ansluta till den.  
```python   
token_1= util.prompt_for_user_token(username=, scope=, client_id=, redirect_uri=, client_secret=)
spotifyObject_1 = spotipy.Spotify(auth=token_1)
``` 
prompt_for_user_token funktionen tar 8 arugment, men det man behöver anväda är de 5 som står i koden ovan. usernam, client_id och client_secret är de information som du borde ha spart sedan innan, redirect_uri är då "https://www.google.com/". scope argument är lite mer specill, då det finns en mängd olika scope man kan ha beroende på vilken funktion man vill köra från spotipy biblioteket, och då kan man läsa deras [dokumentation](https://developer.spotify.com/documentation/web-api/reference/). Men de scopes man behöver för detta projekt är  "user-modify-playback-state user-read-currently-playing playlist-modify-private playlist-modify-public playlist-read-private user-read-playback-state". Och för att använda flera scope så ska man har de i samma string men man ska separera de med mellanslag.   
En viktig sak och ha i bakhuvudet är att spotify token upphöra efter en timme, och då kommer programmet att kracha varje gång man kör den, det jag gör för att undvika det här problemet är att jag tar bort den gammla token och skapar en ny varje gång programmet körs. 
```python
    if os.path.isfile(".cache-"+ config["spotify_config"]["USERNAME"]):
        os.remove(".cache-"+ config["spotify_config"]["USERNAME"])
```
Jag försökte använda "try except" men det gick inte, och jag tror att det beror på att det är ett api error som kommer upp när token upphör. 

#### Beskrivning av alla funktioner i programmet:
##### Connect_to_token():
Det är där jag skapar spotify token och ansluter till den, men jag har även en en if-sats som kollar om programmet har blivit använd på användarens dator förut, om inte så ber den användaren användaren att mata in spotify användarnamnet för att skapa en token åt användaren.  
  
##### creat_list():
Det som den funktionen gör är att skapa en spellista åt användaren, där programmet kommer lägga låtar till när Add_tp_list funktionen körs. 
  
##### Add_to_list():
Den här funktionen körs när programmet detekterar en tumme upp. En tumme upp indikerar att användaren tyckte om låten som spelas, då kommer den att lägga till låten till spellistan som skapades av funktionen ovan.  
  
##### Change_song_puse_play():
Den här funktinen körs när programmet detekterar en vinkande hand. Sedan beroende på handens postion så kommer funktionen att utföra olika saker. Om hand rör sig högeråt så kommer funktionen att spela nästa låt, om handen rör sig vänsteråt så kommer funktione att spela föregånde låt, och om hand står still så kommer funktionen beronde på låtens status att spela eller pausa den. 

### config.json:
I config.json så har jag olika variabler som jag vill spara långsiktig, alltså i hårdisken och inte i ram minnet, som till exempel en bool variabel som och det är för att göra programmet mer effektiv. Jag har även olika konfigurationer för min model.   

### Få en bättre förstålse:
För att få en bättre förstålse för koden, så kan du kika på evaluate.py, där finns all kod kommenterad.  

## Hur test kör man programmet: 
Först så behöver spotify appen nedladd på dator. Sedan så ska du gå igenom " "Vilka Bibliotek behöver man ladda ner" sedan ladda ner image_det folder och öppna hela foldern i Visual studio eller ett liknande code editor, och sedan kör du evaluate koden. När du kör programmet så kommer du behöva fylla i ditt spotify användarnamn, detta steget kommer du behöva göra det bara första gången du kör programmet. Efter det så kommer en spotify sida att komma upp, då trycker du på agree ![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(28)_LI.jpg) sedna kommer en google sida att dyka upp då kopierar du l länken till den sidan och klistra in det i terminalen. Och då är du redo att testa. 

### Vilka funktioner finns i programmet och hur man använder de:
Pausa/spela: Den funktionen använder du genom att hålla handen på samma plats framför kammran i ca 2sekunder.
Spela nästa låt: Den funktionen använder du genom att slida handen till höger framför kammran.
Spela förra låt: Den funktionen använder du genom att slida handen till vänster framför kammran.
Lägg till låten till en spel lista: Den funktionen använder du genom att hålla en tumme upp framför kammran. 

## Utvädering:
### Vilka svårigheter har uppståt under projektet:
* Datasetet: En av de största utmaningar i det här projektet var att fixa en fungerande dataset, och det var på grund av att jag inte kunde hitta bilder som jag vill att min model ska träna på. Och jag skulle säga att det är det som tog mest tid av det här projektet.
* Spotify API: Att använda spotify APi var också ganska utmanande och det var på grund av att jag inte kunde hitta några dokumentationer just för Python. Så jag fick gå igenom källkoden och letade efter de funktionerna jag vill använda, och sedan läsa vilka argument som behövs osv. 

### Vilka problem som finns i programmet: 
Ett problem som programmet har är att man måste ha Spotify premium för att kunna använda (spela nästa/förra låt) funktionen. 
Ett till problem är att om programmet inte kännerigen handen under rörlsen så uppstår fel i postionering funktion och därmed kommer programmet att utföra gör funktion, som till exempel spela nästa låt istället för förra låt. 

### Om jag fick gör om projektet: 
Om jag fick gör om projektet så hade jag först och främst haft flera bilder i datasetet, och även ha bilder som är lite olika vinklade, och det är för att få ännu bättre model.   
Jag hade också gjort programmet grafisk (i Tkinter).   
Jag hade även jobbat lite mer med error handling.  
Jag skulle även vilja hitta på ett bättre sätt att refresha token. 




