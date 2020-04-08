# AI-projekt-
## Syftet
syftet med projektet är att använda bildigenkänning och webkamran för att kontrollera några funktioner i Spotify så som spela nästa och förgående låt och lägga till låtar till en spellista.
## Metod 
### Skapa datasetet
Det jag först började med i det här projektet var att samla in bilder på vinkande händer och tummen upp, och då använde jag ett chrom tillägg som heter [Fatkun Batch](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=sv) som hjälpte mig att ladda ner fleratals bilder på en och samma gång. 
Efter det så började jag med att skapa annotation till alla bilder jag hade. Sedan behövde jag konvertera alla labels jag fick ut från annotering till xml filler. ([Hur man skapar annotation](https://github.com/AmjadAlakrami/AI-dataset/tree/master/Hj%C3%A4lpmedel)).
Efter det så är [datasetet](https://github.com/AmjadAlakrami/AI-dataset/tree/master/Dataset) färdig och då kan man börja med träningen i [google colab](https://colab.research.google.com/drive/1PtKLwonDkTzI1cz0AFbjkxgROJ2IIjff#scrollTo=px4fIT-E1gUO). 

### Spotify API
#### (OBS!! det här steget måste man göra för att test köra mitt program.)
För att kunna använda spotify API så måste man skapa en app på [Spotify Developer](https://developer.spotify.com/dashboard/login). När man ska logga in så använder man samma inloggning som man har på spotify kontot. Sedan så trycker man på "Creat an app" och då få man nämna appen precis som man vill och skriva en kort beskrivning om det (ett streck räknas som en kort beskrivning). Efter det så bockar man av "Desktop App" och trycker på next. Sedan tycker man på NON-COMMERCIAL. Efter det så bockar man av alla tre rutor och trycker på submit. Efter det så borde en liknande sida komma upp: 

![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(22).png)

Då trycker man på "Edit setting" längs upp till höger, och då lägger man till "https://www.google.com/" i "Redirect URIs" rutan och trycker sedan på save. Därefter så behöver du kopiera din Client ID och Client Secret som finns under appen namn på vänset sidan (tryck på Show clien secret för att få fram den) och spara de någonstans där du lätt kan komma åt de. Sedan så behöver du ha din spotify användarnamn, och det kan du komma år genom att logga in på din spotify konto på google, sedan så tycker du på profil/konto, och då borde du kunna hitta den längst upp under Kontoöversikt/profil, kopiera den och spara den med tillsammans med din Client ID och Client Secret.

![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(22)_LI.jpg) ![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(24)_LI.jpg)![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(25)_LI.jpg)![](https://github.com/AmjadAlakrami/AI-projekt-/blob/master/Video%26Images/Screenshot%20(27)_LI.jpg)

### Vilka Bibliotek behöver man ladda ner
cv2: pip install opencv-python  
spotipy: pip install spotipy  
numpy: pip install numpy  

### Hur använder man Spotipy

