
from xml.dom.minidom import parse
import urllib

def index(req):
    linkki = "http://api.openweathermap.org/data/2.5/weather?lon=25.7333&lat=62.2333&mode=xml"
    kaupunki = str(req.form.getfirst("kaupunki"))
    if (kaupunki == "Tampere"):
        linkki = "http://api.openweathermap.org/data/2.5/weather?lon=23.78712&lat=61.49911&mode=xml"
    if (kaupunki == "Helsinki"):
        linkki = "http://api.openweathermap.org/data/2.5/weather?lon=24.93417&lat=60.17556&mode=xml"
    doc = parse(urllib.urlopen(linkki))
    body = doc.getElementsByTagName("lastupdate")
    req.content_type =  'text; charset=UTF-8'
    req.write ( str(body[0].getAttribute('value')) )
    return

#dom1 = parse(pohja)
#body = dom1.getElementsByTagName("body")