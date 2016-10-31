from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from xml.dom.minidom import getDOMImplementation, parse, parseString
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape



sql = """
 SELECT Nimi, Kuvaus, Henkilomaara, RuokalajiID
  FROM Resepti
  WHERE ReseptiID like :ReseptiID;
"""

sql2 = """
SELECT Nimi, RuokalajiID
FROM Ruokalaji;
"""



def index(req):
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()
    palautus = ""
    palautettava = palautalistaobjektit(req)
    return palautettava

def palautalistaobjektit(req):
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()
    kokoelma = {}
    lista = []
    vaihenro = 0

    palautettava = ""

    resepti = req.form.getfirst("resepti", "")
    resepti = escape(resepti)

    lista = []
    lista2 = []


    try:
        cur.execute(sql2)

        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #k‰yd‰‰n tietue l‰pi
                lista.append(str(rivi[i]))
        ii=0
        while ii<len(lista):
            kokoelma[lista[ii]] = lista[ii+1]
            ii = ii + 2
    except:
        # vaatii koodin alkuun rivin: import sys
        req.write("nyt tuli virhe1: %s" % sys.exc_info()[0])

    try:
        cur.execute(sql, {"ReseptiID":resepti})
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #k‰yd‰‰n tietue l‰pi
                lista2.append(str(rivi[i]))
    except:
        # vaatii koodin alkuun rivin: import sys
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
    try:
        palautus = """<div id="muokkauskentat">"""
        palautus = palautus + """<p id="nimip"> <label for="Nimi">Nimi</label> <br/> <input id="Nimi" name="Nimi" type="text" value="%s"/> </p> """ %lista2[0]

        palautus = palautus + """<p id="kuvausp"> <label for="Kuvaus">Kuvaus</label> <br/> <input id="Kuvaus" name="Kuvaus" type="text" value="%s"/> </p> """ %lista2[1]


        palautus = palautus + """<p id="henkilomaarap"> <label for="Henkilomaara">Henkilomaara</label> <br/> <input id="Henkilomaara" name="Henkilomaara" type="text" value="%s"/> </p> """ %lista2[2]

    except:
        # vaatii koodin alkuun rivin: import sys
        req.write("nyt tuli virhe3: %s" % sys.exc_info()[0])
    try:
        palautus = palautus + """<p><select id="ruokalaji" name="ruokalaji">"""
        for osa in kokoelma.keys():
            palautus = palautus + """<option value="%s" """ %kokoelma[osa]
            if kokoelma[osa] == lista2[3]:
                palautus = palautus + """ selected="selected" """
            palautus = palautus + """>"""
            palautus = palautus + osa
            palautus = palautus +"""</option>"""

        palautus = palautus + "</select></p>"
        palautus = palautus + "</div>"
        req.content_type = 'text/plain; charset=UTF-8'
        req.write(palautus)
        con.close()
    except:
        # vaatii koodin alkuun rivin: import sys
        req.write("nyt tuli virhe4: %s" % sys.exc_info()[0])





