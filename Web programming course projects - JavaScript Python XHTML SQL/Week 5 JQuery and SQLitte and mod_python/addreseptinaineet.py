from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape




sqllisays = """
INSERT INTO Liittyy (Maara, Resepti_ReseptiID, Aine_AineID, Yksikko_Lyhenne)
VALUES (:Maara, :ReseptiID, :AineID, :Lyhenne);
"""


def index(req):
    ReseptiID = str(req.form.getfirst("resepti"))
    ReseptiID = escape(ReseptiID)

    aineet = req.form.getlist("ainelista[]")

    maarat = req.form.getlist("maaralista[]")

    yksikot = req.form.getlist("yksikkolista[]")




    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()



    try:
        i = 0
        while i < len(aineet):
            cur.execute( sqllisays, {"ReseptiID":ReseptiID, "AineID":aineet[i], "Maara":maarat[i], "Lyhenne":yksikot[i]})
            i = i + 1
        con.commit()
        req.write("""<h3 id="raportti">Lisäys onnistui!</h3>""")
    except:
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
        con.rollback()

    con.close()

    req.content_type =  'text; charset=UTF-8'

    return
