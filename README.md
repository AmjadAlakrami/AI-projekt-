# AI-projekt-
## Syftet
syftet med projektet är att använda bildigenkänning och webkamran för att kontrollera några funktioner i Spotify så som spela nästa och förgående låt och lägga till låtar till en spellista.
## Metod 
### Skapa datasetet
Det jag först började med i det här projektet var att samla in bilder på vinkande händer och tummen upp, och då använde jag ett chrom tillägg som heter [Fatkun Batch](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=sv) som hjälpte mig att ladda ner fleratals bilder på en och samma gång. 
Efter det så började jag med att skapa annotation till alla bilder jag hade. Sedan behövde jag konvertera alla labels jag fick ut från annotering till xml filler. ([Hur man skapar annotation](https://github.com/AmjadAlakrami/AI-dataset/tree/master/Hj%C3%A4lpmedel)).
Efter det så är [datasetet](https://github.com/AmjadAlakrami/AI-dataset/tree/master/Dataset) färdig och då kan man börja med träningen i [google colab](https://colab.research.google.com/drive/1PtKLwonDkTzI1cz0AFbjkxgROJ2IIjff#scrollTo=px4fIT-E1gUO). 

### Spotify API
<video src="Video&Images/SpotifyaApi.mp4" width="320" height="200" controls preload></video>

Programmet kan kännigen öppnahänder och tummenup  
