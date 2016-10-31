from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape

sql1 = """SELECT ru.nimi,  re.reseptiID
FROM Resepti re, ruokalaji ru
WHERE re.ruokalajiID LIKE ru.ruokalajiID
;
"""




def index(req):
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()
    cur.execute( sql1 )
    lista = []
    testpalautus = ""
    for rivi in cur:  #saadaan yksi tietue dict-muodossa
        for i in rivi.keys(): #k‰yd‰‰n tietue l‰pi
            lista.append(str(rivi[i]))
    i=0
    palautus = """{"""
    while i<len(lista):
        palautus += '"' + lista[i+1] + '": "' + lista[i] + '"'
        i += 2
        if i<len(lista):
            palautus += ","



    palautus = palautus + """}"""
    req.content_type = 'application/json; charset=UTF-8'
    return palautus