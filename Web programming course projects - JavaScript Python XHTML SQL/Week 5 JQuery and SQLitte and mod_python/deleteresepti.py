from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape

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
    ReseptiID = str(req.form.getfirst("ReseptiID"))
    ReseptiID = escape(ReseptiID)

    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()


    try:
        cur.execute( sqlpoisto3, {"reseptiID":ReseptiID})
        cur.execute( sqlpoisto2, {"reseptiID":ReseptiID})
        cur.execute( sqlpoisto1, {"reseptiID":ReseptiID})
        con.commit()
        req.write("""<h3 id="raportti">Poisto onnistui!</h3>""")
    except:
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
        con.rollback()

    con.close()

    req.content_type =  'text; charset=UTF-8'

    return