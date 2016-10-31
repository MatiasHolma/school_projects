from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape


sqlpoisto = """
DELETE FROM Ohje
WHERE ReseptiID = :reseptiID and
Vaihenro = :vaihenro;
"""

sqlpaivitys = """
UPDATE Ohje
SET Vaihenro = (Vaihenro - 1)
WHERE Vaihenro > :vaihenro and ReseptiID = :reseptiID;
"""






def index(req):
    resepti = str(req.form.getfirst("resepti"))
    resepti = escape(resepti)
    vaihe = str(req.form.getfirst("vaiheet"))
    vaihe = escape(vaihe)

    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()


    try:
        cur.execute( sqlpoisto, {"reseptiID":resepti, "vaihenro":vaihe})
        cur.execute( sqlpaivitys, {"reseptiID":resepti, "vaihenro":vaihe})
        con.commit()
        req.write("""<h3 id="raportti">Poisto onnistui!</h3>""")
    except:
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
        con.rollback()

    con.close()

    req.content_type =  'text; charset=UTF-8'

    return