from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape


sqlpaivitys = """
UPDATE Ohje
SET Ohjeteksti =:Ohjeteksti
WHERE Vaihenro =:Ohjenro and ReseptiID =:ReseptiID;
"""

sqllisays = """
INSERT INTO Ohje (Ohjenro, ReseptiID, Ohjeteksti)
VALUES (:Ohjenro, :ReseptiID, :Ohjeteksti)
"""




def index(req):
    ReseptiID = str(req.form.getfirst("resepti"))
    ReseptiID = escape(ReseptiID)
    vaiheet = req.form.getlist("vaihelista[]")
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()



    try:
        i=0
        while(i<len(vaiheet)):
            try:
                cur.execute( sqlpaivitys, {"ReseptiID":ReseptiID, "Ohjenro":str(i+1), "Ohjeteksti":vaiheet[i]})
            except:
                cur.execute( sqllisays, {"ReseptiID":ReseptiID, "Ohjenro":str(i+1), "Ohjeteksti":vaiheet[i]})
            i = i + 1
        con.commit()
        req.write("""<h3 id="raportti">Lisäys onnistui!</h3>""")
    except:

        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
        con.rollback()

    con.close()

    req.content_type =  'text; charset=UTF-8'

    return