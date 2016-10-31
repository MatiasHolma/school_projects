from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape



sqllisays = """
UPDATE Resepti
SET Nimi=:Nimi, Kuvaus=:Kuvaus, Henkilomaara=:Henkilomaara, RuokalajiID=:RuokalajiID
WHERE ReseptiID=:ReseptiID;
"""


def index(req):
    ReseptiID = str(req.form.getfirst("resepti"))
    ReseptiID = escape(ReseptiID)
    Nimi = str(req.form.getfirst("Nimi"))
    Nimi = escape(Nimi)
    Kuvaus = str(req.form.getfirst("Kuvaus"))
    Kuvaus = escape(Kuvaus)
    Henkilomaara = str(req.form.getfirst("Henkilomaara"))
    Henkilomaara = escape(Henkilomaara)
    RuokalajiID = str(req.form.getfirst("Ruokalaji"))
    RuokalajiID = escape(RuokalajiID)



    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()



    try:
        cur.execute( sqllisays, {"ReseptiID":ReseptiID, "Nimi":Nimi, "Kuvaus":Kuvaus, "Henkilomaara":Henkilomaara, "RuokalajiID":RuokalajiID})
        con.commit()
        req.write("""<h3 id="raportti">Lisäys onnistui!</h3>""")
    except:
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
        con.rollback()

    con.close()

    req.content_type =  'text; charset=UTF-8'

    return

