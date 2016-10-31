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
FROM Resepti;
"""

sql2 = """
SELECT *
FROM Resepti
Where ReseptiID = :ReseptiID;
"""

sql3 = """
SELECT Nimi, RuokalajiID
FROM Ruokalaji;
"""

sqllisays = """
UPDATE Resepti
SET Nimi=:Nimi, Kuvaus=:Kuvaus, Henkilomaara=:Henkilomaara, RuokalajiID=:RuokalajiID
WHERE ReseptiID=:ReseptiID;
"""

sqlpoisto1 = """
DELETE FROM Resepti
WHERE ReseptiID = :reseptiID;
"""

sqlpoisto2 = """
DELETE FROM Ohje
WHERE ReseptiID = :reseptiID;
"""

sqlpoisto3 = """
DELETE FROM Liittyy
WHERE Resepti_reseptiID = :reseptiID;
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
    pohja = os.path.join(os.path.dirname(req.filename), 'reseptimuokkaus.xhtml')
    dom = parse(pohja)
    uri = req.uri
    form = find_element(dom, "form", "form")
    
    try:
        cur.execute(sql1) #Haetaan reseptien nimet ja IDt.
        reseptit = find_element(dom, "Resepti", "select")
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                lista.append(str(rivi[i]).decode("UTF-8"))
        ii=0
        while ii<len(lista):
            option = dom.createElement("option")
            option.setAttribute("value", lista[ii+1])
            txt = dom.createTextNode(lista[ii])
            option.appendChild(txt)
            reseptit.appendChild(option)
            kokoelma[lista[ii]] = lista[ii+1]
            ii = ii + 2

    except: #jos tulee virhe...
        # vaatii koodin alkuun rivin: import sys
        error = True

    if req.form.getfirst("Valitse", "") == "Valitse": #kun lisätäänvaihe
        try:
            Resepti = req.form.getfirst("Resepti")
            Resepti = escape(Resepti)
            apu = int(Resepti)
            apu = apu + 0
            Resepti = str(apu)
        except:
                Resepti = ""
        try:
            lista = []
            cur.execute(sql2, {"ReseptiID":Resepti}) #Haetaan reseptien nimet ja IDt.
            reseptit = find_element(dom, "Resepti", "select")
            for rivi in cur:  #saadaan yksi tietue dict-muodossa
                for i in rivi.keys(): #käydään tietue läpi
                    lista.append(str(rivi[i]).decode("UTF-8"))
            ii=0
            while ii<len(lista):
                nimi = find_element(dom, "Nimi", "input")
                nimi.setAttribute("value", lista[ii])
                ii = ii + 1
                kuvaus = find_element(dom, "Kuvaus", "input")
                kuvaus.setAttribute("value", lista[ii])
                ii = ii + 1
                Henkilomaara = find_element(dom, "Henkilomaara", "input")
                Henkilomaara.setAttribute("value", lista[ii])
                ii = ii + 1
                reseptitunnus = find_element(dom, "reseptitunnus", "input")
                reseptitunnus.setAttribute("value", lista[ii])
                ii = ii + 1
                ruokalajiID = lista[ii]
                ii = ii + 1

                option.appendChild(txt)
                reseptit.appendChild(option)

        except: #jos tulee virhe...
        # vaatii koodin alkuun rivin: import sys
            error = True
        try:
            lista = []
            cur.execute(sql3) #Haetaan reseptien nimet ja IDt.
            ruokalajip = find_element(dom, "ruokalajip", "p")
            #ruokalajit = find_element(dom, "Ruokalaji", "select")
            ruokalajit = dom.createElement("select")
            ruokalajit.setAttribute("name", "Ruokalaji")
            ruokalajit.setAttribute("id", "Ruokalaji")
            ruokalajit.setAttribute("size", "12")
            ruokalajip.appendChild(ruokalajit)
            for rivi in cur:  #saadaan yksi tietue dict-muodossa
                for i in rivi.keys(): #käydään tietue läpi
                    lista.append(str(rivi[i]).decode("UTF-8"))
            ii=0
            while ii<len(lista):
                option = dom.createElement("option")
                option.setAttribute("value", lista[ii+1])
                if lista[ii+1] == ruokalajiID:
                    option.setAttribute("selected", "selected")
                txt = dom.createTextNode(lista[ii])
                option.appendChild(txt)
                ruokalajit.appendChild(option)
                kokoelma[lista[ii]] = lista[ii+1]
                ii = ii + 2
        except: #jos tulee virhe...
        # vaatii koodin alkuun rivin: import sys
            error = True

    if req.form.getfirst("Poista", "") == "Poista": #kun lisätäänvaihe
        try:
            ReseptiID = req.form.getfirst("Resepti")
            ReseptiID = escape(ReseptiID)
            apu = int(ReseptiID)
            apu = apu + 0
            ReseptiID = str(apu)
            cur.execute( sqlpoisto3, {"reseptiID":ReseptiID})
            cur.execute( sqlpoisto2, {"reseptiID":ReseptiID})

            cur.execute( sqlpoisto1, {"reseptiID":ReseptiID})
            con.commit()
        except:
            test(dom, "fail " + ReseptiID)
            test(dom, "nyt tuli virhe: %s" % sys.exc_info()[0])
            con.rollback()

            #DELETE FROM Resepti
            #WHERE ReseptiID = :reseptiID;

            #DELETE FROM Ohje
            #WHERE ReseptiID = :reseptiID;

            #DELETE FROM Liittyy
            #WHERE Resepti_reseptiID = :reseptiID;

    if req.form.getfirst("Muokkaa", "") == "Muokkaa": #kun lisätäänvaihe
        try:
            nimi = req.form.getfirst("Nimi")
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
            ReseptiID = req.form.getfirst("reseptitunnus")
            ReseptiID = escape(ReseptiID)
            apu = int(ReseptiID)
            apu = apu + 0
            ReseptiID = str(apu)		
            cur.execute( sqllisays, {"Nimi":nimi, "Kuvaus":kuvaus, "Henkilomaara":henkilomaara, "RuokalajiID":str(ruokalaji), "ReseptiID":ReseptiID})
            con.commit()

        except:
            #test(dom)
            con.rollback()



			
    con.close()
    return dom.toxml('UTF-8')

def test(dom, str):
    str = str + " | "
    p = find_element(dom, "test", "p")
    span = dom.createElement("span")
    txt = dom.createTextNode(str.decode("UTF-8"))
    span.appendChild(txt)
    p.appendChild(span)

	
def find_element(root, id, element="*"):
    for e in root.getElementsByTagName(element):
      if e.hasAttribute("id") and e.getAttribute("id") == id:
         return e
    return None
