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
SELECT lyhenne, lyhenne
FROM Yksikko;
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
    try:
        cur.execute(sql2)
			
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                lista.append(str(rivi[i]))
        ii=0
        while ii<len(lista):
            kokoelma[lista[ii]] = lista[ii+1]
            ii = ii + 2
        palautus = """<select id="lyhenne%s" name="lyhenne">""" %vaihenro
        for osa in kokoelma.keys():    
            palautus = palautus + """<option value="%s""" %kokoelma[osa]
           # palautus = palautus + 
            palautus = palautus + """">""" 
            palautus = palautus + osa
            palautus = palautus +"""</option>""" 
			
        palautus = palautus + "</select>"
        req.content_type = 'text/plain; charset=UTF-8'
        req.write(palautus)
        con.close()
    except: 
        # vaatii koodin alkuun rivin: import sys
        req.write("nyt tuli virhe1: %s" % sys.exc_info()[0])	
