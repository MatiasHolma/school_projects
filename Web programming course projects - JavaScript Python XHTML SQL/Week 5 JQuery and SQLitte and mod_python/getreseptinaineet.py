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

sql5 = """
 select a.nimi, l.maara, y.lyhenne
  from resepti r, aine a, liittyy l, yksikko y
  where r.reseptiid like l.resepti_reseptiid and
  l.aine_aineid like a.aineid and
  l.yksikko_lyhenne like y.lyhenne and
  r.reseptiID like :ReseptiID;
"""


sql6 = """
 select count(*)
  from resepti r, aine a, liittyy l, yksikko y
  where r.reseptiid like l.resepti_reseptiid and
  l.aine_aineid like a.aineid and
  l.yksikko_lyhenne like y.lyhenne and
  r.reseptiID like :ReseptiID;

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
    resepti = req.form.getfirst("resepti", "")
    resepti = escape(resepti)
    error = False
    lista = []
    ainelista = []
    yksikkolista = []
    nykyainelista = []
    nykyyksikkolista = []
    nimilista = []
    nykyiset = []
    kokoelma = {}
    maaraint = 0
    palautus = ""
    kokoelma = {}
    lista = []
    vaihenro = 0

    try:
        cur.execute(sql5, {"ReseptiID":resepti})
        #test(dom, resepti)
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                nykyiset.append(str(rivi[i]))
        ii = 0
    except:
        req.write("virhe ekassa sql-kutsussa: %s" % sys.exc_info()[0])
    try:
        while ii < len(nykyiset):
            nimilista.append(nykyiset[ii])
            ii = ii+1
            nykyainelista.append(nykyiset[ii])
            ii = ii+1
            nykyyksikkolista.append(nykyiset[ii])
            ii = ii+1
    except:
        req.write("virhe nimilistan teossa: %s" % sys.exc_info()[0])
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
        q = 0
        w = 0

    except:
        req.write("virhe yksikkolistan teossa: %s" % sys.exc_info()[0])
    try:
        palautus = palautus + """<div id="reseptinaineet"> """
        while i < len(nimilista):
            q = 0
            w = 0
            e = 0
            palautus = palautus + """<p class="aineet">"""
            palautus += """<select name="aine%s" """% str(maaraint)
            palautus += """ id="aine%s">""" % str(maaraint)
            while q < len(ainelista):
                palautus = palautus + """<option value="%s" disabled="disabled" """ %str(ainelista[q+1])
                #palautus = palautus + """<option value="r"""
                if ainelista[q]==nimilista[i]:
                    palautus = palautus + """selected="selected" """
                palautus = palautus + """>"""
                palautus = palautus + ainelista[q]
                #palautus = palautus + "juu"
                palautus += """</option>"""
                q = q + 2

            palautus = palautus +  """</select>"""
            palautus = palautus + """<input name="maara%s" type="text" """ % str(maaraint)
            palautus = palautus + """value="%s" """ %nykyainelista[i]
            palautus = palautus + """id="maara%s" """  % str(maaraint)
            palautus = palautus + """ "/>"""
            palautus += """<select name="yksikko%s" """ % str(maaraint)
            palautus +="""id="yksikko%s">""" % str(maaraint)
            while w < len(yksikkolista):
                palautus = palautus + """<option value="%s" disabled="disabled" """ %yksikkolista[w]
                if yksikkolista[w
                ] == nykyyksikkolista[i]:
                    palautus = palautus + """selected="selected" """
                palautus = palautus + """>"""
                palautus = palautus + yksikkolista[w]
                palautus += """</option>"""
                w = w + 1
            palautus = palautus +  """</select>"""
            palautus = palautus + "</p>"
            i = i+1
            maaraint = maaraint + 1

        palautus = palautus + """<div id="lisaaineet"></div>"""


        palautus = palautus + "</div>"

        #palautus = palautus  + """<p><input name="Lisaa" type="submit" value="%s"/></p>""" %str(maaraint - 1)
        req.content_type = 'text/plain; charset=UTF-8'
        req.write(palautus)
        con.close()

    except:
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
				
