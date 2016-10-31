from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from xml.dom.minidom import getDOMImplementation, parse, parseString
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape

sql1 = """
SELECT Nimi
FROM Resepti;
"""

sql2 = """
SELECT Nimi, RuokalajiID
FROM Ruokalaji;
"""

sql4 = """
SELECT o.Ohjeteksti
FROM Ohje o, Resepti r
WHERE r.nimi LIKE :Resepti and
o.ReseptiID LIKE r.ReseptiID;
"""

sql3 = """
SELECT MAX(ReseptiID) FROM Resepti;
"""

sqllisays = """
INSERT INTO resepti (Nimi, Kuvaus, Henkilomaara, RuokalajiID, ReseptiID)
VALUES (:nimi, :kuvaus, :henkilomaara, :ruokalaji, :reseptiid)
"""


henkiloerror = False
eiNumero = False
seuraavaID = 0;
kokoelma = {}
lista = []

def index(req):
    global henkiloerror #jos tiedot eivät ole hyvä
    global eiNumero #bool jos numerokentästä ei tuu numero
    global seuraavaID #seuraavan lisättävän reseptin ID


	#alkuvalmistelut
    con = sqlite.connect( '/nashome3/mailholm/html/data/resepteja')
    con.text_factory = str
    con.row_factory = sqlite.Row
    cur = con.cursor()
    req.content_type = "text/html ;charset=utf-8"
    pohja = os.path.join(os.path.dirname(req.filename), 'pohja.xhtml')
    dom = parse(pohja)
    uri = req.uri
    #form = find_element(dom, "form", "form")

    if req.form.getfirst("Kirjaudu ulos") == "Kirjaudu ulos": #kun lisätään    and len(str(req.form.getfirst("Nimi")))>0
        req.session["kirjautunut"] = "ko"
        req.session.save()

    #nimi = req.form.getfirst("Nimi")

    lista = find_element(dom, "lista", "div")
    #txt = dom.createTextNode(str(nimi))
    #lista.appendChild(txt)

    list = []
    try:
        cur.execute(sql1)#haetaan ruokalajien nimet
        ul = dom.createElement("ul")
        lista.appendChild(ul)
        for rivi in cur:  #saadaan yksi tietue dict-muodossa
            for i in rivi.keys(): #käydään tietue läpi
                list.append(str(rivi[i]))
                
        
        
        ii = 0
        
        while ii < len(list):
            li = dom.createElement("li")
            txt = dom.createTextNode(list[ii].decode("UTF-8"))
            li.appendChild(txt)
            ul.appendChild(li)
            cur.execute(sql4, {"Resepti":list[ii]})
            alustettu = False
            for rivi in cur:  #saadaan yksi tietue dict-muodossa
                if alustettu == False:
                    li2 = dom.createElement("li")
                    ol = dom.createElement("ol")
                    li2.appendChild(ol)
                    ul.appendChild(li2)
                    alustettu = True
                for i in rivi.keys(): #käydään tietue läpi
                    li = dom.createElement("li")
                    txt = dom.createTextNode(rivi[i].decode("UTF-8"))
                    li.appendChild(txt)
                    ol.appendChild(li)
            ii = ii + 1
    except:
        error = True
    con.close()
    return dom.toxml('UTF-8')

def test(dom, str):
    str = str + " | "
    p = find_element(dom, "test", "p")
    span = dom.createElement("span")
    txt = dom.createTextNode(str.decode("UTF-8"))
    span.appendChild(txt)
    p.appendChild(span)

  #  try:
   #     cur.execute(sql2) #Haetaan reseptien nimet ja IDt.

#        for rivi in cur:  #saadaan yksi tietue dict-muodossa
 #           for i in rivi.keys(): #käydään tietue läpi
 #               lista.append(str(rivi[i]))
 #       ii=0
  #      while ii<len(lista):
  #          kokoelma[lista[ii]] = lista[ii+1]
     #       ii = ii + 2

   # except: #jos tulee virhe...
        # vaatii koodin alkuun rivin: import sys
 #       error = True
     #   req.write("<p>nyt tuli virhe1: %s</p>" % sys.exc_info()[0])
     #   req.write("<p>nyt tuli virhe: %s</p>" % sys.exc_info()[0])
     #   req.write("<p>nyt tuli virhe: %s</p>" % sys.exc_info()[0])



  #  con.close()


    #req.write ( html1 )

		
	
	

    
	
  #  if req.form.getfirst("laheta") == "Laheta" and len(str(req.form.getfirst("Nimi")))>0: #kun lisätään
   #     try:
    #        c = 0
    #        nimi = req.form.getfirst("Nimi")
            #haetaan kenttien tiedot
    #        nimi = escape(nimi)
    #        kuvaus = req.form.getfirst("Kuvaus")
     #       kuvaus = escape(kuvaus)
     #       henkilomaara = req.form.getfirst("Henkilomaara")
     #       henkilomaara = escape(henkilomaara)
     #       ruokalajit = req. form.getlist("Ruokalaji")
     #       ruokalaji = escape(ruokalajit[0])
     #       apu = int(ruokalaji)
     #       apu = apu + 0
     #       ruokalaji = str(apu)
 
        #    if (len(nimi)<1 or len(kuvaus)<1 or len(henkilomaara)<1 or len(ruokalaji)<1):
        #        tyhjakentta=True
            
       #     if (int(henkilomaara)<1):
      #              henkiloerror = True
     #   except:
    #        eiNumero = True

   # if henkiloerror == False and eiNumero == False:
   #     try:
  #          cur.execute(sql3)
#			#lasketaan seuraava ID
    #        for rivi in cur:  #saadaan yksi tietue dict-muodossa
    #            for i in rivi.keys(): #käydään tietue läpi
    #                nexID = (int(rivi[i]))
   #                 nexID = nexID + 1
   #                 break
   #             break
		    #lisätään tiedot
    #        cur.execute( sqllisays, {"nimi":nimi, "kuvaus":kuvaus, "henkilomaara":henkilomaara, "ruokalaji":str(ruokalaji), "reseptiid":str(nexID)})
    #        con.commit()

     #   except:
     #       req.write("<p>Täytä kentät oikein!</p>")
    #        con.rollback()
    #else:
    #    req.write("<p>ei lisätty</p>")
	

    
  #  i=0
    #try:
    #    req.write(kentat)
    #    for osa in kokoelma.keys():
            
    #        req.write("""<option value=" """ ) #tulostetaan valikko
    #        req.write(kokoelma[osa])
    #        req.write("""">""" )
    #        req.write(osa)
    #        req.write("""</option>""" )
    #except:
        # vaatii koodin alkuun rivin: import sys
    #    req.write("<p>nyt tuli virhe4: %s</p>" % sys.exc_info()[0])
    #req.write(html2)
	
def find_element(root, id, element="*"):
    for e in root.getElementsByTagName(element):
      if e.hasAttribute("id") and e.getAttribute("id") == id:
         return e
    return None