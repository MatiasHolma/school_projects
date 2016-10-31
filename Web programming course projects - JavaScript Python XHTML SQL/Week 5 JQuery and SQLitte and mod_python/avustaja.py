from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from xml.dom.minidom import getDOMImplementation, parse, parseString
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape

sql1 = """
SELECT Nimi, ReseptiID
FROM Resepti
ORDER BY Nimi;
"""

sql4 = """
SELECT Ohjeteksti
FROM Ohje
Where ReseptiID LIKE :ReseptiID;
"""


sql2 = """
SELECT Nimi, RuokalajiID
FROM Ruokalaji;
"""

sql3 = """
SELECT MAX(RuokalajiID) FROM Ruokalaji;
"""


html1 = """<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fi" lang="fi">
<head>
<title>Reseptit</title>
</head>
<body>
<form action="" method="post">"""

kentat = """
<h2>Lisaa uusi resepti</h2>
<p> <label for="Nimi">Nimi</label> <br /><input type="text" name="Nimi" id="Nimi" /> </p>
<p> <label for="Kuvaus">Kuvaus</label> <br /><input type="text" name="Kuvaus" id="Kuvaus" /> </p>
<p> <label for="Henkilomaara">Henkilomaara</label> <br /><input type="text" name="Henkilomaara" id="Henkilomaara" /> </p>
<p> <label for="Ruokalaji">Ruokalaji</label><br /> <select name="Ruokalaji" id="Ruokalaji" size="12"></p>
"""

html2 = """
</select>
    <input type="submit" name="laheta" value="Laheta" />

</form>
</body>
</html>"""

sqllisays = """
INSERT INTO resepti (Nimi, Kuvaus, Henkilomaara, RuokalajiID, ReseptiID)
VALUES (:nimi, :kuvaus, :henkilomaara, :ruokalaji, :reseptiid)
"""


#postinumero = req.form.getfirst("postinro")


def index(req):



    
	
    palautettava = palautanimet(req)
    return palautettava

	

	
	
def palautanimet(req):
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()
    cur.execute( sql1 )
    
    kokoelma = {}
    lista = []
    #postitoimipaikka = cur.fetchone()
	 
    kaikkinimet = """<ul id="lista">"""
    for rivi in cur:  #saadaan yksi tietue dict-muodossa
        for i in rivi.keys(): #käydään tietue läpi
            lista.append(rivi[i])
            #kaikkinimet = kaikkinimet + "<li>" + rivi[i] + "</li>"
	ii = 0
    while ii < len(lista):
        kaikkinimet = kaikkinimet + "<li>" + lista[ii] + "</li><ol>"
        ii = ii + 1
        resepti = lista[ii]
        cur.execute( sql4, {"ReseptiID":resepti} )
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                kaikkinimet = kaikkinimet + "<li>" + rivi[i] + "</li>"
        kaikkinimet = kaikkinimet + "</ol>"
        ii = ii + 1
    kaikkinimet = kaikkinimet + "</ul>"
    con.close()

    req.content_type =  'text/plain; charset=UTF-8'

    try: 
        req.write(kaikkinimet)
        return 
    except:
        return "vika"	
		
