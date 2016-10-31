from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape


sqlpoisto = """
DELETE FROM Ruokalaji
WHERE ruokalajiID = :ruokalajiID;
"""


def index(req):
    Ruokalaji = str(req.form.getfirst("ruokalaji"))
    Ruokalaji = escape(Ruokalaji)

    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()


    try:
        cur.execute( sqlpoisto, {"ruokalajiID":Ruokalaji})
        con.commit()
        req.write("""<h3 id="raportti">Poisto onnistui!</h3>""")
    except:
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
        con.rollback()

    con.close()

    req.content_type =  'text; charset=UTF-8'

    return