from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape

sql1 = """SELECT re.nimi as resepti, ru.nimi as ruokalaji, re.reseptiID
FROM Resepti re, Ruokalaji ru
WHERE re.ruokalajiID=ru.ruokalajiID
order by re.nimi;
"""



sql2="""select aine.nimi, liittyy.maara, liittyy.yksikko_lyhenne
From aine, liittyy
Where liittyy.aine_aineID=aine.aineID
and liittyy.resepti_reseptiid = :reseptiID;"""


def index(req):
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()
    Resepti = str(req.form.getfirst("Resepti"))
    Resepti = escape(Resepti)

    cur.execute( sql2, {"reseptiID":Resepti})
    lista2 = []

    for rivi in cur:  #saadaan yksi tietue dict-muodossa
        for u in rivi.keys(): #käydään tietue läpi
            lista2.append(str(rivi[u]))
    u = 0
    if len(lista2)<1:
        return ""
    palautus = "{"
    palautus = palautus + """"aineet":["""
    while u < len(lista2):
        palautus += """ {"ainenimi": "%s","""% lista2[u]
        u = u + 1
        palautus += """ "maara": "%s","""% lista2[u]
        u = u + 1
        palautus += """ "yksikko": "%s" """ %lista2[u]
        palautus = palautus + """}"""
        u = u + 1
        if u<len(lista2):
            palautus = palautus + """,
		    """
        else:
            palautus += "]"


    
    palautus = palautus + """}"""
    req.content_type = 'application/json; charset=UTF-8'
    return palautus