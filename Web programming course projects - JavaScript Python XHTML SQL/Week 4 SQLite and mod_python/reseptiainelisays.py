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

sql3 = """
SELECT Nimi, AineID
FROM Aine;
"""

sql4 = """
SELECT lyhenne
FROM Yksikko;
"""

sql5 = """
 select a.nimi, l.maara, y.lyhenne
  from resepti r, aine a, liittyy l, yksikko y
  where r.reseptiid like l.resepti_reseptiid and
  l.aine_aineid like a.aineid and
  l.yksikko_lyhenne like y.lyhenne and
  r.reseptiID like :ReseptiID;
"""


sql6 = """
 select count(*)
  from resepti r, aine a, liittyy l, yksikko y
  where r.reseptiid like l.resepti_reseptiid and
  l.aine_aineid like a.aineid and
  l.yksikko_lyhenne like y.lyhenne and
  r.reseptiID like :ReseptiID;

"""

sqllisays = """
UPDATE Liittyy
SET Maara=:Maara
WHERE Resepti_ReseptiID=:ReseptiID and Aine_AineID=:AineID and Yksikko_Lyhenne=:Lyhenne;
"""
#SET Maara=:1, Aine_AineID=:9, Yksikko_Lyhenne=:dl
#WHERE Resepti_ReseptiID=:6
sqllisays2 = """
INSERT INTO Liittyy (Maara, Resepti_ReseptiID, Aine_AineID, Yksikko_Lyhenne)
VALUES (:Maara, :ReseptiID, :AineID, :Lyhenne);
"""


def index(req):
    error = False
    lista = []
    ainelista = []
    yksikkolista = []
    nykyainelista = []
    nykyyksikkolista = []
    nimilista = []
    nykyiset = []
    kokoelma = {}
	#alkuvalmistelut
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()
    req.content_type = "text/html ;charset=utf-8"
    pohja = os.path.join(os.path.dirname(req.filename), 'reseptiainelisays.xhtml')
    dom = parse(pohja)
    uri = req.uri
    form = find_element(dom, "form", "form")
    maara = req.form.getfirst("maara", 1)
    maaraint = int (maara)




    try:
        resepti = req.form.getfirst("Resepti", "")
        resepti = escape(resepti)
        apu = int(resepti)
        apu = apu + 0
        resepti = str(apu)
    except:
        error = True
        resepti = ""


    try:
        cur.execute(sql2) #Haetaan reseptien nimet ja IDt.
        ruokalajit = find_element(dom, "Resepti", "select")
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                lista.append(str(rivi[i]).decode("UTF-8"))
        ii=0
        u=0
        while ii<len(lista):
            option = dom.createElement("option")
            option.setAttribute("value", lista[ii+1].decode("UTF-8"))

            if lista[ii+1] == resepti:
                option.setAttribute("selected", "selected")
            txt = dom.createTextNode(lista[ii])
            option.appendChild(txt)
            ruokalajit.appendChild(option)
            kokoelma[lista[ii]] = lista[ii+1]
            ii = ii + 2

    except: #jos tulee virhe...
        # vaatii koodin alkuun rivin: import sys
        error = True



    if req.form.getfirst("Valitse", "") == "Valitse" or len(resepti) > 0:
        if len(resepti):
            error = True
        cur.execute(sql5, {"ReseptiID":resepti})
        #test(dom, resepti)
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                nykyiset.append(str(rivi[i]).decode("UTF-8"))
####################################################################
        #ii = 0
        #while ii < len(nykyiset):
        #    nykyiset[ii] = "" + escape(nykyiset[ii])
        #    test(dom, nykyiset[ii])
        #    ii = ii + 3
        #ii = 0
###################################################
        ii = 0
        while ii < len(nykyiset):
            nimilista.append(nykyiset[ii])
            ii = ii+1
            nykyainelista.append(nykyiset[ii])
            ii = ii+1
            nykyyksikkolista.append(nykyiset[ii])
            ii = ii+1
        #if maaraint < len(nykyainelista):
        #    maaraint = len(nykyainelista)
        maaraint = len(nykyainelista)
        if maaraint == 0:
            maaraint = 1
        if req.form.getfirst("Valitse", "") == "Valitse":
            maara = str(maaraint)

    if req.form.getfirst("Lisaavaihe", "") == "Lisaavaihe": #kun lisätäänvaihe
        maaraint = int(maara) + 1
        maara = str(maaraint)

    hidden = find_element(dom, "maara", "input")
    hidden.setAttribute("value", str(maara).decode("UTF-8"))
    p = find_element(dom, "vaiheet", "p")
    i=0
    try:
        cur.execute(sql3) #Haetaan reseptien nimet ja IDt.
        ruokalajit = find_element(dom, "Resepti", "select")
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                ainelista.append(str(rivi[i]).decode("UTF-8"))
        ii=0
        cur.execute(sql4) #Haetaan reseptien nimet ja IDt.
        ruokalajit = find_element(dom, "Resepti", "select")
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                yksikkolista.append(str(rivi[i]).decode("UTF-8"))
        ii=0
    except:
        error = True

    maaraint = int(maara)
    i = 0
    q = 0
    w = 0
    e = 0
    while i<maaraint:
        span = dom.createElement("span")
        txt = dom.createTextNode("aine " + str(i + 1) + ": ")
        span.appendChild(txt)
        p.appendChild(span)
        select1 = dom.createElement("select")
        ii = 0
        while ii < len(ainelista):
            option = dom.createElement("option")
            option.setAttribute("value", ainelista[ii+1].decode("UTF-8"))
            txt = dom.createTextNode(ainelista[ii])
            if len(nykyainelista) > i:
                if nimilista[i] == ainelista[ii]:
                    option.setAttribute("selected", "selected")
                    select1.setAttribute("disabled", "disabled")
            option.appendChild(txt)
            select1.appendChild(option)

            ii = ii + 2
        ii = 0
        select1.setAttribute("name", "aine" + str(q))
        q = q + 1
        select2 = dom.createElement("select")
        while ii < len(yksikkolista):
            option = dom.createElement("option")
            option.setAttribute("value", yksikkolista[ii].decode("UTF-8"))
            txt = dom.createTextNode(yksikkolista[ii])
            if len(nykyyksikkolista) > i:
                if nykyyksikkolista[i] == yksikkolista[ii]:
                    option.setAttribute("selected", "selected")
                    select2.setAttribute("disabled", "disabled")
					

            option.appendChild(txt)
            select2.appendChild(option)
            ii = ii + 1
        p.appendChild(select1)
        select2.setAttribute("name", "yksikko" + str(e))
        e = e + 1

        input = dom.createElement("input")
        input.setAttribute("type", "text")
        input.setAttribute("name", "maara" + str(w))
        w = w + 1
        if len(nykyainelista) > i:
            input.setAttribute("value", nykyainelista[i].decode("UTF-8"))

        br = dom.createElement("br")
        p.appendChild(input)
        p.appendChild(select2)
        p.appendChild(br)
        i = i+1

        #SET Maara=:Maara, Aine_AineID=:AineID, Yksikko_Lyhenne=:Lyhenne
        #WHERE Resepti_ReseptiID=:ReseptiID;
    if req.form.getfirst("Lisaa", "") == "Lisaa":
        try:
            if len(nykyyksikkolista)>0:
                u=0
                ReseptiID1 = req.form.getfirst("Resepti", "")
                ReseptiID = str(ReseptiID1).decode("UTF-8")
                while u<len(nykyainelista):
                    Maara1 = req.form.getfirst("maara"+str(u), "")
                    Maara = str(Maara1).decode("UTF-8")
                    AineID1 = req.form.getfirst("aine"+str(u), "")
                    Lyhenne = req.form.getfirst("yksikko"+str(u), "")
                    AineID = str(AineID1).decode("UTF-8")
                    Lyhenne = Lyhenne.decode("UTF-8")
                    cur.execute(sqllisays, {"Maara":Maara, "AineID":AineID, "Lyhenne":Lyhenne, "ReseptiID":ReseptiID})
                    u = u + 1
                #u = len(nykyyksikkolista)
                while u<maaraint:
                    
                    Maara1 = req.form.getfirst("maara"+str(u), "")
                    Maara = str(Maara1).decode("UTF-8")
                    AineID1 = req.form.getfirst("aine"+str(u), "")
                    AineID = str(AineID1).decode("UTF-8")
                    Lyhenne = req.form.getfirst("yksikko"+str(u), "")
                    Lyhenne = Lyhenne.decode("UTF-8")
                    cur.execute(sqllisays2, {"Maara":Maara, "AineID":AineID, "Lyhenne":Lyhenne, "ReseptiID":ReseptiID})
                    u = u + 1
                con.commit()
            else:
                ReseptiID1 = req.form.getfirst("Resepti", "")
                ReseptiID = str(ReseptiID1).decode("UTF-8")
                u=0
                while u<maaraint:
                    Maara1 = req.form.getfirst("maara"+str(u), "")
                    Maara = str(Maara1).decode("UTF-8")
                    AineID1 = req.form.getfirst("aine"+str(u), "")
                    AineID = str(AineID1).decode("UTF-8")
                    Lyhenne = req.form.getfirst("yksikko"+str(u), "")
                    Lyhenne = Lyhenne.decode("UTF-8")
                    cur.execute(sqllisays2, {"Maara":Maara, "AineID":AineID, "Lyhenne":Lyhenne, "ReseptiID":ReseptiID})
                    u = u + 1
                con.commit()
        except:
            con.rollback()
            test(dom, "nyt tuli virhe: %s" % sys.exc_info()[0])
            error = True

		
    con.close()
    return dom.toxml('UTF-8')

	
#INSERT INTO Liittyy (Maara, Resepti_ReseptiID, Aine_AineID, Yksikko_Lyhenne)
#VALUES (:Maara, :ReseptiID, :AineID, :Lyhenne);
	
#UPDATE Liittyy
#SET Maara=:Maara, Aine_AineID=:AineID, Yksikko_Lyhenne=:Lyhenne
#WHERE Resepti_ReseptiID=:ReseptiID;

def test(dom, str):
    str = str + " | "
    p = find_element(dom, "test", "p")
    span = dom.createElement("span")
    #txt = dom.createTextNode(str.decode("UTF-8"))
    txt = dom.createTextNode(str)
    span.appendChild(txt)
    p.appendChild(span)

	
def find_element(root, id, element="*"):
    for e in root.getElementsByTagName(element):
      if e.hasAttribute("id") and e.getAttribute("id") == id:
         return e
    return None