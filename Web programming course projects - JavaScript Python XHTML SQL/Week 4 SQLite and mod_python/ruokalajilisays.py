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
SELECT MAX(RuokalajiID) FROM Ruokalaji;
"""


sqllisays = """
INSERT INTO Ruokalaji (Nimi, Kuvaus, RuokalajiID)
VALUES (:nimi, :kuvaus, :ruokalajiID);
"""

sqlpoisto = """
DELETE FROM Ruokalaji
WHERE ruokalajiID = :ruokalajiID;
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
    pohja = os.path.join(os.path.dirname(req.filename), 'ruokalajilisayspohja.xhtml')
    dom = parse(pohja)
    uri = req.uri
    form = find_element(dom, "form", "form")
    

    if req.form.getfirst("Lisaa") == "Lisaa": #kun lisätään
        try:
            nimi = req.form.getfirst("Nimi")
            nimi = escape(nimi)
            kuvaus = req.form.getfirst("Kuvaus")
            kuvaus = escape(kuvaus)

            if len(nimi)<1:
                p = find_element(dom, "nimip", "p")
                span = dom.createElement("span")
                txt = dom.createTextNode("Lisaa nimi")
                span.appendChild(txt)
                p.appendChild(span)
                error = True
            if len(kuvaus)<1:
                p = find_element(dom, "kuvausp", "p")
                span = dom.createElement("span")
                txt = dom.createTextNode("Lisaa kuvaus")
                span.appendChild(txt)
                p.appendChild(span)

        except:
            error = True
        if error == False:
            try:
                cur.execute(sql3)
	    		#lasketaan seuraava ID
                for rivi in cur:  #saadaan yksi tietue dict-muodossa
                    for i in rivi.keys(): #käydään tietue läpi
                        nexID = (int(rivi[i]))
                        nexID = nexID + 1
                        break
                    break
            
                cur.execute( sqllisays, {"nimi":nimi,  "kuvaus":kuvaus, "ruokalajiID":str(nexID)})
                #test(dom)
                con.commit()
            except:
                test(dom)
                con.rollback()

    if req.form.getfirst("Poista") == "Poista": #kun lisätään

        try:
            try:
                ruokalajiID = req.form.getfirst("Ruokalaji")
                ruokalajiID = escape(ruokalajiID)
                apu = int(ruokalajiID)
                apu = apu + 0
                ruokalajiID = str(apu)

            except:
                ruokalajiID = ""
            if len(ruokalajiID)<1:
                p = find_element(dom, "ruokalajip", "p")
                span = dom.createElement("span")
                txt = dom.createTextNode("Valitse ruokalaji")
                span.appendChild(txt)
                p.appendChild(span)
                error = True

        except:
            error = True
        if error == False:
            
            try:
                #test(dom)
                #test(dom)
                cur.execute( sqlpoisto, {"ruokalajiID":ruokalajiID})
                
                con.commit()
            except:
                test(dom)

                con.rollback()
    try:
        cur.execute(sql2) #Haetaan reseptien nimet ja IDt.
        ruokalajit = find_element(dom, "Ruokalaji", "select")
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                lista.append(str(rivi[i]).decode("UTF-8"))
        ii=0
        while ii<len(lista):
            option = dom.createElement("option")
            option.setAttribute("value", lista[ii+1])
            txt = dom.createTextNode(lista[ii])
            option.appendChild(txt)
            ruokalajit.appendChild(option)
            kokoelma[lista[ii]] = lista[ii+1]
            ii = ii + 2

    except: #jos tulee virhe...
        # vaatii koodin alkuun rivin: import sys
        error = True

		
    con.close()
    return dom.toxml('UTF-8')

	
def find_element(root, id, element="*"):
    for e in root.getElementsByTagName(element):
      if e.hasAttribute("id") and e.getAttribute("id") == id:
         return e
    return None
	
def test(dom):
    p = find_element(dom, "nimip", "p")
    span = dom.createElement("span")
    txt = dom.createTextNode("error")
    span.appendChild(txt)
    p.appendChild(span)
