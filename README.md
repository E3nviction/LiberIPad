# LiberIPad
A trolling "jailbreak" for my Ipad

## Installation
To install this on your Ipad, you'll need to go into the Pyto app,  
then navigate to the "PyPI" tab,  
install the "gitpython" package,  
and run the command.

## What is it?
So, how exactly does this "jailbreak" work.  
Well first of all we shouln't directly call it a "jailbreak",  
it's more of a "hack" (a trick to bypass and access features that you weren't meant to access).  
We aren't actually unlocking the Ipad or removing restrictions,  
we're just working with the tools we have, to be able to use the Ipad  
in ways we weren't supposed to... e.g. being able to "spam" a kahoot game full with bots using a script.  

## Ok. But now how does it work?
It's actually quite simple, for the webpage (The Dashboard) we just use normal html, css, and javascript to create a website  
But for the Running of these html files, we use a program called "Pyto" it's a program that allows us to use python on the Ipad,  
we then use the pyto_ui library to create an app window with a web view (a mini-browser in the app) to display the html file.  

Alternatively we could (and did) use the python http server mod  
``` python
python -m http.server <port>
```

example:
``` python
python -m http.server 8000
```

then we can go onto a web browser and type:  
`localhost:8000 or 127.0.0.1:8000`

And to update the "Jailbreak" from my computer we use gitpython PyPI pip package to access git
