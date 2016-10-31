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
SELECT MAX(ReseptiID) FROM Resepti;
"""

sqllisays = """
INSERT INTO resepti (Nimi, Kuvaus, Henkilomaara, RuokalajiID, ReseptiID)
VALUES (:nimi, :kuvaus, :henkilomaara, :ruokalaji, :reseptiid)
"""


#henkiloerror = False
#eiNumero = False
#seuraavaID = 0;
#


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
    pohja = os.path.join(os.path.dirname(req.filename), 'lisayspohja.xhtml')
    dom = parse(pohja)
    uri = req.uri
    form = find_element(dom, "form", "form")


    try:
        cur.execute(sql2) #Haetaan reseptien nimet ja IDt.
        ruokalajit = find_element(dom, "Ruokalaji", "select")
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #k‰yd‰‰n tietue l‰pi
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
    
    
    if req.form.getfirst("laheta", "") == "Laheta": #kun lis‰t‰‰n    and len(str(req.form.getfirst("Nimi")))>0
        try:
            
            nimi = req.form.getfirst("Nimi")
            #haetaan kenttien tiedot
            
            nimi = escape(nimi)
            kuvaus = req.form.getfirst("Kuvaus")
            kuvaus = escape(kuvaus)
            henkilomaara = req.form.getfirst("Henkilomaara")
            henkilomaara = escape(henkilomaara)
            
            try:
                ruokalaji = req.form.getfirst("Ruokalaji")
                ruokalaji = escape(ruokalaji)
                apu = int(ruokalaji)
                apu = apu + 0
                ruokalaji = str(apu)
            except:
                ruokalaji = ""
		
            #test(dom)
            
            error = False
            if len(nimi)<1:
                #span = find_element(dom, "nimispan", "span")
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
                i=0
            if len(henkilomaara)<1:
                p = find_element(dom, "henkilomaarap", "p")
                span = dom.createElement("span")
                txt = dom.createTextNode("Lisaa henkilomaara")
                span.appendChild(txt)
                p.appendChild(span)
                error = True
            try:
                if int(henkilomaara)<1:
                    p = find_element(dom, "henkilomaarap", "p")
                    span = dom.createElement("span")
                    txt = dom.createTextNode("Virheellinen henkilomaara")
                    span.appendChild(txt)
                    p.appendChild(span)
                    error = True

            except:
                error = True
            if len(ruokalaji)<1:
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
            cur.execute(sql3)
			#lasketaan seuraava ID
            for rivi in cur:  #saadaan yksi tietue dict-muodossa
                for i in rivi.keys(): #k‰yd‰‰n tietue l‰pi
                    nexID = (int(rivi[i]))
                    nexID = nexID + 1
                    break
                break
		    #lis‰t‰‰n tiedot
            cur.execute( sqllisays, {"nimi":nimi, "kuvaus":kuvaus, "henkilomaara":henkilomaara, "ruokalaji":str(ruokalaji), "reseptiid":str(nexID)})
            con.commit()

        except:
            con.rollback()

			
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