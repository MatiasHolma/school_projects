from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from xml.dom.minidom import getDOMImplementation, parse, parseString
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape


sql2 = """
SELECT Nimi, RuokalajiID
FROM Ruokalaji;
"""

sql3 = """
SELECT MAX(AineID) FROM Aine;
"""

sqllisays = """
INSERT INTO Aine (Nimi, Kuvaus, AineID)
VALUES (:nimi, :kuvaus, :aineID)
"""

def index(req):
    error = False
    lista = []
    kokoelma = {}
	#alkuvalmistelut
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()
    req.content_type = "text/html ;charset=utf-8"
    pohja = os.path.join(os.path.dirname(req.filename), 'ruokaainelisayspohja.xhtml')
    dom = parse(pohja)
    uri = req.uri
    form = find_element(dom, "form", "form")
    
    if req.form.getfirst("Lisaa", "") == "Lisaa": #kun lisätäänvaihe
        try:
            Ruokaaine = req.form.getfirst("Ruokaaine")
            Ruokaaine = escape(Ruokaaine).decode("UTF-8")
            Kuvaus = req.form.getfirst("Kuvaus")
            Kuvaus = escape(Kuvaus).decode("UTF-8")
        except:
            Ruokaaine = ""
        if len(Ruokaaine) > 0:
            cur.execute(sql3)
			#lasketaan seuraava ID
            for rivi in cur:  #saadaan yksi tietue dict-muodossa
                for i in rivi.keys(): #käydään tietue läpi
                    nexID = (int(rivi[i]))
                    nexID = nexID + 1
                    break
                break
		    #lisätään tiedot
            cur.execute( sqllisays, {"nimi":Ruokaaine, "kuvaus":Kuvaus, "aineID":str(nexID)})
            con.commit()

    
    con.close()
    return dom.toxml('UTF-8')
	
def test(dom):
    p = find_element(dom, "ruokalajip", "p")
    span = dom.createElement("span")
    txt = dom.createTextNode("Tanne paastiin")
    span.appendChild(txt)
    p.appendChild(span)


def find_element(root, id, element="*"):
    for e in root.getElementsByTagName(element):
      if e.hasAttribute("id") and e.getAttribute("id") == id:
         return e
    return None