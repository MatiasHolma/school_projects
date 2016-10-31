from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape


sqllisays = """
INSERT INTO resepti (Nimi, Kuvaus, Henkilomaara, RuokalajiID, ReseptiID)
VALUES (:nimi, :kuvaus, :henkilomaara, :ruokalaji, :reseptiid)
"""

sql3 = """
SELECT MAX(ReseptiID) FROM Resepti;
"""

def index(req):
    nimi = str(req.form.getfirst("Nimi"))
    kuvaus = str(req.form.getfirst("Kuvaus"))
    henkilomaara = str(req.form.getfirst("henmaara"))
    ruokalajit = req.form.getlist("ruokalaji")
    ruokalaji = escape(ruokalajit[0])
            #ruokalaji = "" + str(ruokalaji)
    #apu = int(ruokalaji)
    #apu = apu + 0
    #ruokalaji = str(apu)
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()
	
    cur.execute(sql3)
			
    for rivi in cur:  #saadaan yksi tietue dict-muodossa
        for i in rivi.keys(): #käydään tietue läpi
            nexID = (int(rivi[i]))
            nexID = nexID + 1
            break
        break
    try:
        cur.execute( sqllisays, {"nimi":nimi, "kuvaus":kuvaus, "henkilomaara":henkilomaara, "ruokalaji":str(ruokalaji), "reseptiid":str(nexID)} )
        con.commit()
    except:
        req.write("nyt tuli virhe2: %s" % sys.exc_info()[0])
        con.rollback()
	
    con.close()

    req.content_type =  'text; charset=UTF-8'

    return