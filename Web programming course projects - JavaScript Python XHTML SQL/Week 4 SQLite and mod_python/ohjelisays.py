from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from xml.dom.minidom import getDOMImplementation, parse, parseString
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape


sql2 = """
SELECT Nimi, ReseptiID
FROM Resepti;
"""


sqllisays = """
INSERT INTO Ohje (Vaihenro, ReseptiID, Ohjeteksti)
VALUES (:Vaihenro, :ReseptiID, :Ohjeteksti);
"""


def index(req):
    error = False
    lista = []
    kokoelma = {}
	#alkuvalmistelut
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()
    req.content_type = "text/html ;charset=utf-8"
    pohja = os.path.join(os.path.dirname(req.filename), 'ohjelisayspohja.xhtml')
    dom = parse(pohja)
    uri = req.uri
	
    form = find_element(dom, "form", "form")
	
    
	
    try:
        cur.execute(sql2) #Haetaan reseptien nimet ja IDt.
        ruokalajit = find_element(dom, "Resepti", "select")
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                lista.append(str(rivi[i]).decode("UTF-8"))
        ii=0
        while ii<len(lista):
            option = dom.createElement("option")
            option.setAttribute("value", lista[ii+1])
            txt = dom.createTextNode(lista[ii])
            option.appendChild(txt)
            ruokalajit.appendChild(option)
            kokoelma[lista[ii]] = lista[ii+1]
            ii = ii + 2

    except: #jos tulee virhe...
        # vaatii koodin alkuun rivin: import sys
        error = True
    
    maara = req.form.getfirst("maara", 1)
	

    if req.form.getfirst("Lisaavaihe", "") == "Lisaavaihe": #kun lisätäänvaihe
        maaraint = int(maara) + 1
        maara = str(maaraint)
		

    #test(dom, str(maara))
    hidden = find_element(dom, "maara", "input")
    hidden.setAttribute("value", str(maara))
    p = find_element(dom, "vaiheet", "p")
    i=0
    maaraint = int(maara)
    while i<maaraint:
        span = dom.createElement("span")
        txt = dom.createTextNode("vaihe " + str(i + 1) + ": ")
        span.appendChild(txt)
        p.appendChild(span)
        input = dom.createElement("input")
        input.setAttribute("type", "text")
        input.setAttribute("name", "vaihe" + str(i))
        br = dom.createElement("br")
        p.appendChild(input)
        p.appendChild(br)
        i = i+1
		
    if req.form.getfirst("Lisaa", "") == "Lisaa": #kun lisätäänvaihe
        try:
            resepti = req.form.getfirst("Resepti", "")
            resepti = escape(resepti)
            apu = int(resepti)
            apu = apu + 0
            resepti = str(apu)
        except:
            resepti = ""
        try:
            #test(dom, "tryn alkuun päästiin")
            if len(resepti)!=0:
                #test(dom, "iffin sisään päästiin")
                i=0
                maaraint = int(maara)
                while i<maaraint:
                    #test(dom, "whilen sisään päästiin")
                    vaihe = req.form.getfirst("vaihe" + str(i), "")
                    vaihe = vaihe.decode("UTF-8")
                    if len(vaihe)==0:
                        #test(dom, "vaihe" + str(i) + " ei löydy")
                        i = i+1
                        continue
                    #test(dom, "executen alkuun päästiin")
                    #test(dom, str(resepti))
                    cur.execute( sqllisays, {"Vaihenro":str(i+1), "ReseptiID":str(resepti), "Ohjeteksti":vaihe}) #VALUES (:Vaihenro, :ReseptiID, :Ohjeteksti);
                    #test(dom, "execute onnistui")
                    i = i+1
                    con.commit()
            else:
                test(dom, "resepti feilaa")
        except:
            test(dom, "nyt tuli virhe: %s" % sys.exc_info()[0])
            con.rollback()
            


    con.close()
    return dom.toxml('UTF-8')

def test(dom, str):
    str = str + " | "
    p = find_element(dom, "test", "p")
    span = dom.createElement("span")
    txt = dom.createTextNode(str.decode("UTF-8"))
    span.appendChild(txt)
    p.appendChild(span)

	
def find_element(root, id, element="*"):
    for e in root.getElementsByTagName(element):
      if e.hasAttribute("id") and e.getAttribute("id") == id:
         return e
    return None
