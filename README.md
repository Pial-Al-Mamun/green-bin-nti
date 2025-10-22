<h1 align="center"> ♻️ GreenBin – AI-baserad avfallssortering </h1> 
 <h2>   </h2>
<h2 align="center">Syfte</h2>
Att använda AI och datorseende för att känna igen och sortera olika typer av skräp. Projektet syftar till att minska felsortering, öka återvinning och öka förståelsen för hur teknik kan bidra till hållbarhet.
Koppling till FN:s mål: #11 Hållbara städer och samhällen och #12 Hållbar konsumtion och produktion.
<h2 align="center">Motivation</h2>
Vi vill lära oss praktiskt hur AI fungerar genom att bygga ett system som gör nytta i vardagen. Felsortering är ett konkret problem vi själva ser dagligen i skolmiljöer. GreenBin blir både en teknisk och pedagogisk lösning.
<h2 align="center">Teknik</h2>
Hårdvara: Raspberry Pi, USB-kamera, LED-lampor (röd/grön), 3D-printad eller kartongprototyp.
Mjukvara: Python, Pytorch (för AI), OpenCV (bildhantering), GPIO (ljusstyrning).
Modell: MobileNetV2 via Transfer Learning.
<h2 align="center">Funktion</h2>
När skräp hålls framför kameran:
Bild tas och analyseras av AI-modellen.
Om rätt kategori → Grön lampa tänds.
Om fel kategori → Röd lampa tänds.
<h2 align="center">Mål</h2>
Minst 60% träffsäkerhet på klassificering.
Stöd för minst 4 skräpkategorier.
Färdig fysisk prototyp för demonstration.
