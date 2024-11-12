# LiberIPad
Ein trolling "Jailbreak" für dein iPad

## Installation
Um dies auf deinem iPad zu installieren, musst du die Pyto-App öffnen,  
dann zum "PyPI"-Tab navigieren,  
das "dulwich"-Paket installieren,  
und dann eine neue Datei erstellen, sie `install.py` nennen und den folgenden Code hineinkopieren:  
```python
from dulwich import porcelain

porcelain.clone("https://github.com/E3nviction/LiberIPad.git", "LIB")
```


## Was ist das?
Wie funktioniert dieser "Jailbreak" genau?  
Nun, zuerst sollten wir es nicht direkt einen "Jailbreak" nennen,  
es ist eher ein "Hack" (ein Trick, um Funktionen zu umgehen und auf Features zuzugreifen, auf die man eigentlich nicht zugreifen sollte).  
Wir entsperren das iPad also nicht wirklich oder entfernen Beschränkungen,  
wir arbeiten einfach mit den Tools, die uns zur Verfügung stehen, um das iPad  
auf eine Weise zu nutzen, wie es nicht vorgesehen war... z.B. ein Kahoot-Spiel mit Bots zu "spammen" mithilfe eines Skripts.

## Ok. Aber wie funktioniert es jetzt?
Es ist eigentlich ziemlich einfach. Für die Webseite (Das Dashboard) verwenden wir ganz normales HTML, CSS und JavaScript, um eine Website zu erstellen.  
Aber für das Ausführen dieser HTML-Dateien verwenden wir ein Programm namens "Pyto",  
es ist ein Programm, das es uns ermöglicht, Python auf dem iPad zu verwenden,  
wir nutzen dann die pyto_ui-Bibliothek, um ein App-Fenster mit einer Web-Ansicht (einen Mini-Browser in der App) zu erstellen, um die HTML-Datei anzuzeigen.

Alternativ könnten wir (und haben es auch getan) den Python-HTTP-Server-Modus verwenden  
``` python
python -m http.server <port>
```

Beispiel:
``` python
python -m http.server 8000
```

(Update: Der localhost wird jetzt doch verwendet aber + pyto_ui)

Dann können wir einen Webbrowser öffnen und eingeben:  
`localhost:8000 oder 127.0.0.1:8000`

Und um den "Jailbreak" von meinem computer aus zu aktualisieren, verwenden wir das dulwich PyPI-Paket, um auf Git zuzugreifen.