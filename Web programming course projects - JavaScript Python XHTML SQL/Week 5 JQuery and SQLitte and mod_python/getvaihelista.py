from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from xml.dom.minidom import getDOMImplementation, parse, parseString
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape

sql4 = """
SELECT o.Ohjeteksti, vaihenro
FROM Ohje o, Resepti r
WHERE r.ReseptiID LIKE :ReseptiID and
o.ReseptiID LIKE r.ReseptiID;
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
    palautettava = ""
    kokoelma = {}
    lista = []
    resepti = req.form.getfirst("resepti", "")
    resepti = escape(resepti)

    try:
        cur.execute(sql4, {"ReseptiID":resepti})

        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #k‰yd‰‰n tietue l‰pi
                lista.append(str(rivi[i]))
        ii=0
    except:
        # vaatii koodin alkuun rivin: import sys
        req.write("nyt tuli virhe1: %s" % sys.exc_info()[0])
    try:
        while ii<len(lista):
            kokoelma[lista[ii]] = lista[ii+1]
            ii = ii + 2
    except:
        # vaatii koodin alkuun rivin: import sys
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
    try:
        palautus = """<p id="vaihep"><select id="vaiheet" name="vaiheet">"""
        for osa in kokoelma.keys():
            palautus = palautus + """<option value="%s""" %kokoelma[osa]
            palautus = palautus + """">"""
            palautus = palautus + osa
            palautus = palautus +"""</option>"""

        palautus = palautus + "</select></p>"
        req.content_type = 'text/plain; charset=UTF-8'
        req.write(palautus)
        con.close()
    except:
        # vaatii koodin alkuun rivin: import sys
        req.write("nyt tuli virhe3: %s" % sys.exc_info()[0])
