from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from xml.dom.minidom import getDOMImplementation, parse, parseString
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape





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
    maara = req.form.getfirst("Lisaa", "")
    maara = escape(maara)
    kokoelma = {}
    lista = []

    try:
        ii=0
        palautus = ""
        maaraint = int(maara)
        while ii < 1:
            palautus = palautus + """<p class="uvaiheet">"""
            palautus = palautus + """<input name="vaihe%s" type="text" """ % str(maaraint)
            palautus = palautus + """id="vaihe%s" """ % str(maaraint)
            palautus = palautus + """value="" """
            palautus = palautus + """ />"""
            palautus = palautus + "</p>"
            ii = ii + 1
            maaraint = maaraint + 1
    except:
        # vaatii koodin alkuun rivin: import sys
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
    try:
        palautus = palautus + """<div id="uudetvaiheet"></div> """
        req.content_type = 'text/plain; charset=UTF-8'
        req.write(palautus)
        con.close()
    except:
        # vaatii koodin alkuun rivin: import sys
        req.write("nyt tuli virhe3: %s" % sys.exc_info()[0])
