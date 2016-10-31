from mod_python import apache, Session
from mod_python import util
import hashlib
import os
import os.path
import sys
from xml.dom.minidom import getDOMImplementation, parse, parseString
from mod_python import apache, Cookie
from mod_python import apache, Session
from cgi import escape


shared_private_key = "ABCDEF"

def handler(req):
    req.content_type = "text/html ;charset=utf-8"
    pohja = os.path.join(os.path.dirname(req.filename), 'kirjautumispohja.xhtml')
    dom = parse(pohja)
    uri = req.uri
    form = find_element(dom, "form", "form")


    #haetaan tiedostojen sisällöt
    f = open(os.path.join(os.path.dirname(req.filename), 'salasana.txt'), 'r')
    if os.path.isfile(str(os.path.join(os.path.dirname(req.filename), 'salasana.txt'))) == True:
        for rivi in f:
            salis1 = str(rivi)
        f.close()
    f.close()
	
    f = open(os.path.join(os.path.dirname(req.filename), 'kayttajatunnus.txt'), 'r')
    if os.path.isfile(str(os.path.join(os.path.dirname(req.filename), 'kayttajatunnus.txt'))) == True:
        for rivi in f:
            kayttis1 = rivi
        f.close()
    f.close()
	
    
	
    try:
        if req.session["kirjautunut"] == "ok":
            #req.write(dom.toxml('UTF-8'))
            return apache.OK
        else:
            form = util.FieldStorage(req)
            if form.getfirst("kirjaudu", "") == "kirjaudu": #kun lisätään
                tunnus = form.getfirst("tunnus")#haetaam kentät
                salasana = form.getfirst("salasana")
                if tunnus == kayttis1:
                    if str(salis1) == str(hashlib.sha1(repr(salasana) + "," + shared_private_key).hexdigest()): #verrataan kenttiä salattuihin kenttiin
                        req.session["kirjautunut"] = "ok"
                        req.session.save()
                        req.content_type = "text/html"
                        #req.write(dom.toxml('UTF-8'))
                        return apache.OK
                    else:
                        span = find_element(dom, "vaarasalasana", "span")
                        txt = dom.createTextNode("Tunnus on oikea mutta salasana ei")
                        span.appendChild(txt)
                else:
                    span = find_element(dom, "vaaratunnus", "span")
                    txt = dom.createTextNode("Tunnusta ei ole oikea")
                    span.appendChild(txt)
            req.write(dom.toxml('UTF-8'))
            return apache.DONE
    except:
        form = util.FieldStorage(req)
        if form.getfirst("kirjaudu", "") == "kirjaudu": #kun lisätään
            tunnus = form.getfirst("tunnus")#haetaam kentät
            salasana = form.getfirst("salasana") 
            if tunnus == kayttis1:
                if str(salis1) == str(hashlib.sha1(repr(salasana) + "," + shared_private_key).hexdigest()): #verrataan kenttiä salattuihin kenttiin
                    req.session["kirjautunut"] = "ok"
                    req.session.save()
                    req.content_type = "text/html"
                    #req.write(dom.toxml('UTF-8'))
                    return apache.OK
                else:
                    span = find_element(dom, "vaarasalasana", "span")
                    txt = dom.createTextNode("Tunnus on oikea mutta salasana ei")
                    span.appendChild(txt)
            else:
                span = find_element(dom, "vaaratunnus", "span")
                txt = dom.createTextNode("Tunnusta ei ole oikea")
                span.appendChild(txt)
            #    req.content_type = "text/html" \
        req.write(dom.toxml('UTF-8'))
        return apache.DONE


        #req.write ( sisalto1 )
        #req.write( "<p>Et ole kirjautunut</p>" )
        #req.write( sisalto2 )
    #req.write(dom.toxml('UTF-8'))

    return apache.DONE



def find_element(root, id, element="*"):
    for e in root.getElementsByTagName(element):
      if e.hasAttribute("id") and e.getAttribute("id") == id:
         return e
    return None