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
SELECT Ohjeteksti, Vaihenro
FROM Ohje
WHERE ReseptiID = :ReseptiID;
"""

sql3 = """
SELECT distinct a.Nimi, a.AineID
FROM Aine a, liittyy l
WHERE l.Resepti_ReseptiID = :ReseptiID and
a.AineID = l.Aine_AineID;
"""


sqlpoisto2 = """
DELETE FROM Ohje
WHERE ReseptiID = :reseptiID and
Vaihenro = :vaihenro;
"""

sqlpoisto3 = """
DELETE FROM Liittyy
WHERE Resepti_ReseptiID = :reseptiID and
Aine_AineID = :aineID;
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
    pohja = os.path.join(os.path.dirname(req.filename), 'poistareseptistapohja.xhtml')
    dom = parse(pohja)
    uri = req.uri
    form = find_element(dom, "form", "form")
    try:
        Resepti = req.form.getfirst("Resepti")
        Resepti = escape(Resepti)
        apu = int(Resepti)
        apu = apu + 0
        Resepti = str(apu)
    except:
        Resepti = ""
    try:
        cur.execute(sql1) #Haetaan reseptien nimet ja IDt.
        reseptit = find_element(dom, "Resepti", "select")
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #k‰yd‰‰n tietue l‰pi
                lista.append(str(rivi[i]).decode("UTF-8"))
        ii=0
        while ii<len(lista):
            option = dom.createElement("option")
            option.setAttribute("value", lista[ii+1])
            txt = dom.createTextNode(lista[ii])
            if lista[ii + 1] == Resepti:
                option.setAttribute("selected", "selected")
            option.appendChild(txt)
            reseptit.appendChild(option)
            kokoelma[lista[ii]] = lista[ii+1]
            ii = ii + 2

    except: #jos tulee virhe...
        # vaatii koodin alkuun rivin: import sys
        error = True

    if req.form.getfirst("Valitse", "") == "Valitse": #kun lis‰t‰‰nvaihe


        try:
            lista = []
            cur.execute(sql2, {"ReseptiID":Resepti}) #Haetaan reseptien nimet ja IDt.
            vaihep = find_element(dom, "vaihep", "p")
            vaiheet = dom.createElement("select")
            vaiheet.setAttribute("name", "Vaihe")
            vaiheet.setAttribute("id", "Vaihe")
            vaiheet.setAttribute("size", "12")
            vaihep.appendChild(vaiheet)


            for rivi in cur:  #saadaan yksi tietue dict-muodossa
                for i in rivi.keys(): #k‰yd‰‰n tietue l‰pi
                    lista.append(str(rivi[i]).decode("UTF-8"))
            ii=0
            while ii<len(lista):
                option = dom.createElement("option")
                option.setAttribute("value", lista[ii+1])
                txt = dom.createTextNode(lista[ii])
                option.appendChild(txt)
                vaiheet.appendChild(option)
                kokoelma[lista[ii]] = lista[ii+1]
                ii = ii + 2
        except: #jos tulee virhe...
        # vaatii koodin alkuun rivin: import sys
            error = True

        try:
            lista = []
            cur.execute(sql3, {"ReseptiID":Resepti}) #Haetaan reseptien nimet ja IDt.
            ainep = find_element(dom, "ainep", "p")
            aineet = dom.createElement("select")
            aineet.setAttribute("name", "Aine")
            aineet.setAttribute("id", "Aine")
            aineet.setAttribute("size", "12")
            ainep.appendChild(aineet)


            for rivi in cur:  #saadaan yksi tietue dict-muodossa
                for i in rivi.keys(): #k‰yd‰‰n tietue l‰pi
                    lista.append(str(rivi[i]).decode("UTF-8"))
            ii=0
            while ii<len(lista):
                option = dom.createElement("option")
                option.setAttribute("value", lista[ii+1])
                txt = dom.createTextNode(lista[ii])
                option.appendChild(txt)
                aineet.appendChild(option)
                kokoelma[lista[ii]] = lista[ii+1]
                ii = ii + 2
        except: #jos tulee virhe...
        # vaatii koodin alkuun rivin: import sys
            error = True
            test(dom, "nyt tuli virhe: %s" % sys.exc_info()[0])

    if req.form.getfirst("PoistaVaihe", "") == "PoistaVaihe": #kun lis‰t‰‰nvaihe
        try:
            Resepti = req.form.getfirst("Resepti")
            Resepti = escape(Resepti)
            apu = int(Resepti)
            apu = apu + 0
            Resepti = str(apu)

            vaihenro = req.form.getfirst("Vaihe")
            vaihenro = escape(vaihenro)
            apu = int(vaihenro)
            apu = apu + 0
            vaihenro = str(apu)
            test(dom, "vaihe "+ vaihenro)
            test(dom, "resepti " + Resepti)
            cur.execute(sqlpoisto2, {"reseptiID":Resepti, "vaihenro":vaihenro}) #Haetaan reseptien nimet ja IDt
            con.commit()
        except: #jos tulee virhe...
        # vaatii koodin alkuun rivin: import sys
            error = True
            con.rollback()
            test(dom, "nyt tuli virhe: %s" % sys.exc_info()[0])

    if req.form.getfirst("PoistaAine", "") == "PoistaAine": #kun lis‰t‰‰nvaihe
        try:
            Resepti = req.form.getfirst("Resepti")
            Resepti = escape(Resepti)
            apu = int(Resepti)
            apu = apu + 0
            Resepti = str(apu)

            aineID = req.form.getfirst("Aine")
            aineID = escape(aineID)
            apu = int(aineID)
            apu = apu + 0
            aineID = str(apu)
            test(dom, "aine "+ aineID)
            test(dom, "resepti " + Resepti)
            cur.execute(sqlpoisto3, {"reseptiID":Resepti, "aineID":aineID}) #Haetaan reseptien nimet ja IDt
            con.commit()
        except: #jos tulee virhe...
        # vaatii koodin alkuun rivin: import sys
            error = True
            con.rollback()
            test(dom, "nyt tuli virhe: %s" % sys.exc_info()[0])



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
