from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape


sqllisays = """
INSERT INTO Ohje (Vaihenro, ReseptiID, Ohjeteksti)
VALUES (:Ohjenro, :ReseptiID, :Ohjeteksti);
"""

sql3 = """
SELECT MAX(Vaihenro) FROM Ohje WHERE ReseptiID =:ReseptiID;
"""


def index(req):
    strvaiheita = str(req.form.getfirst("vaiheita"))
    vaiheita = int(strvaiheita)
    ReseptiID = str(req.form.getfirst("resepti"))
    ReseptiID = escape(ReseptiID)
    vaiheet = req.form.getlist("vaihelista[]")
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()



    try:
        i=vaiheita
        u = 0
        max = len(vaiheet) + vaiheita
        while(i<max):
            try:
                cur.execute( sqllisays, {"Ohjenro":str(i + 1), "ReseptiID":ReseptiID, "Ohjeteksti":vaiheet[u]})
            except:
                try:
                    cur.execute(sql3, {"ReseptiID":ReseptiID})
                    for rivi in cur:  #saadaan yksi tietue dict-muodossa
                        for i in rivi.keys():
                            nexID = (int(rivi[i]))
                            nexID = nexID + 1
                            break
                        break
                    cur.execute( sqllisays, {"Ohjenro":str(nexID), "ReseptiID":ReseptiID, "Ohjeteksti":vaiheet[u]})
                except:
                    req.write("nyt tuli virhe1: %s" % sys.exc_info()[0])
            u = u + 1
            i = i + 1

        con.commit()
        req.write("""<h3 id="raportti">Lisäys onnistui!</h3>""")
    except:
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
        con.rollback()

    con.close()

    req.content_type =  'text; charset=UTF-8'

    return