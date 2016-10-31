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
SELECT Nimi, ReseptiID
FROM Resepti;
"""

sql3 = """
SELECT Nimi, AineID
FROM Aine;
"""

sql4 = """
SELECT Lyhenne
FROM Yksikko;
"""




def index(req):
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()
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
    ainelista = []
    yksikkolista = []
    nykyainelista = []
    palautus = ""

    try:
        cur.execute(sql3) #Haetaan reseptien nimet ja IDt.
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                ainelista.append(str(rivi[i]))
        ii=0
    except:
        req.write("virhe ainelistan kutsussa: %s" % sys.exc_info()[0])
    try:
        cur.execute(sql4) #Haetaan reseptien nimet ja IDt.
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                yksikkolista.append(str(rivi[i]))
        #maaraint = nykyainelista/3
        i = 0

    except:
        req.write("virhe yksikkolistan teossa: %s" % sys.exc_info()[0])
    try:
        maara = str(req.form.getfirst("Lisaavaihe"))
        maaraint = int(maara)
        palautus = palautus + """<div id="reseptinaineet"> """
    except:
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
    while i < 1:
        q = 0
        w = 0
        e = 0
        try:
            palautus = palautus + """<p class="uudetaineet">"""
            palautus += """<select name="aine%s" """% str(maaraint)
            palautus += """id="aine%s">""" % str(maaraint)


            while q < len(ainelista):
                palautus = palautus + """<option value="%s"  """ %str(ainelista[q+1])
                #palautus = palautus + """<option value="r"""
                palautus = palautus + """>"""
                palautus = palautus + ainelista[q]
                q = q + 2

        except:
            req.write("nyt tuli virhe3: %s" % sys.exc_info()[0])
            break
        try:
            palautus = palautus +  """</select>"""
            palautus = palautus + """<input name="maara%s" type="text" """ % str(maaraint)
            palautus = palautus + """id="maara%s" """% str(maaraint)
            palautus = palautus + """value="" """
            palautus = palautus + """ "/>"""
            palautus += """<select id="yksikko%s" """ % str(maaraint)
            palautus = palautus + """>"""
        except:
            req.write("nyt tuli virhe4: %s" % sys.exc_info()[0])
            break
        try:
            while w < len(yksikkolista):
                palautus = palautus + """<option value="%s"  """ %yksikkolista[w]
                palautus = palautus + """>"""
                palautus = palautus + yksikkolista[w]
                palautus += """</option>"""
                w = w + 1
        except:
            req.write("nyt tuli virhe4: %s" % sys.exc_info()[0])
        palautus = palautus +  """</select>"""
        palautus = palautus + "</p>"
        i = i+1
        maaraint = maaraint + 1
    palautus = palautus + """<div id="lisaaineet"></div>"""
    palautus = palautus + "</div>"
    req.content_type = 'text/plain; charset=UTF-8'
    req.write(palautus)
    con.close()


