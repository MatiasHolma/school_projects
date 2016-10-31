from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape


sqllisays = """
INSERT INTO Aine (Nimi, Kuvaus, AineID)
VALUES (:nimi, :kuvaus, :aineid)
"""

sql3 = """
SELECT MAX(AineID) FROM Aine;
"""

def index(req):
    nimi = str(req.form.getfirst("Nimi"))
    nimi = escape(nimi)
    kuvaus = str(req.form.getfirst("Kuvaus"))
    kuvaus = escape(kuvaus)
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()

    cur.execute(sql3)

    for rivi in cur:  #saadaan yksi tietue dict-muodossa
        for i in rivi.keys(): 
            nexID = (int(rivi[i]))
            nexID = nexID + 1
            break
        break

    try:
        cur.execute( sqllisays, {"nimi":nimi, "kuvaus":kuvaus, "aineid":str(nexID)})
        con.commit()
        req.write("""<h3 id="raportti">Lisäys onnistui!</h3>""")
    except:
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
        con.rollback()

    con.close()

    req.content_type =  'text; charset=UTF-8'

    return