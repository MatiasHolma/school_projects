from pysqlite2 import dbapi2 as sqlite
from mod_python import util
import hashlib
import os
import os.path
import sys
from xml.dom.minidom import getDOMImplementation, parse, parseString
from cgi import escape
import time



sisalto = """
<div id="body">
<div id="lataus"></div>
<header>
  <p><input id="Kirjauduulos" type="submit" name="Kirjauduulos" value="Kirjaudu ulos" /></p>
  <h1>Reseptitietokanta</h1>
  <P><input id="Etusivu" type="submit" name="Etusivu" value="Etusivu" /><input id="Lisaataipoistaruokalaji" type="submit" name="Lisaa tai poista ruokalaji" value="Lisaa tai poista ruokalaji" /><input id="Lisaareseptinvaiheet" type="submit" name="Lisaa reseptin vaiheet" value="Lisaa reseptin vaiheet" /><input id="Muokkaareseptia" type="submit" name="Muokkaa reseptia" value="Muokkaa reseptia" /><input id="Lisaaruoka-aine" type="submit" name="Lisaa ruoka-aine" value="Lisaa ruoka-aine" /><input id="Lisaareseptilleaineet" type="submit" name="Lisaa reseptille aineet" value="Lisaa reseptille aineet" /><input id="Poistareseptinainetaivaihe" type="submit" name="Poista reseptin aine tai vaihe" value="Poista reseptin aine tai vaihe" /></p>

</header>

<div id="sisalto">
<section>

<article>
  <h2>Reseptit</h2>
  <p id="lista"> <img src="ajax-loader2.gif" alt="loaderimg" /></p>
</article>

<article>



<h2>Lisää resepti</h2>

<div id="raportti"></div>
<form>


 <p> <label for="Nimi">Nimi</label> <br /><input type="text" name="Nimi" id="Nimi"  class="kentta"/> <span id="Nimip" >*</span></p>
<p> <label for="Kuvaus">Kuvaus</label> <br /><input type="text" name="Kuvaus" id="Kuvaus"  class="kentta"/> <span id="Kuvausp">*</span></p>

 <p> <label for="henmaara">Henkilömäärä</label> <br /> <input type="number" name="henmaara" min="1" max="100" step="1" value="1" id="henmaara" ><p id="henmaarap"></p>
 <p id="ruokalajip"> <label>Ruokalaji</label><br /><span id="ruokalaji" >*</span></p>
  </form>

 <p><input id="Laheta" type="submit" name="laheta" value="Laheta" /></p>
</article>

</section>
</div>

</div>
"""

failsisalto = """
<div id="body">
<p><label>Tunnus</label> <input id="tunnus" name="tunnus" type="text"/><span id="vaaratunnus">


"""

failsisalto2 = """<span></p>
<p><label>Salasana </label><input id="salasana" name="salasana" type="password"/><span id="vaarasalasana">"""

failsisalto3 = """</span></p>
<p><input id="kirjaudu" name="kirjaudu" type="submit" value="kirjaudu"/></p>
</div>
"""

shared_private_key = "ABCDEF"

def index(req):
    
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

    salasana = req.form.getfirst("salasana", "")
    tunnus = req.form.getfirst("tunnus", "")
    if salis1 == str(hashlib.sha1(repr(salasana) + "," + shared_private_key).hexdigest()) and kayttis1 == tunnus == kayttis1:
        req.content_type =  'text/plain; charset=UTF-8'
        req.write(sisalto)
    if tunnus != kayttis1:
        palautus = failsisalto + "tunnusta ei löytynyt" + failsisalto2 + failsisalto3
        req.content_type =  'text/plain; charset=UTF-8'
        req.write(palautus)
    if tunnus == kayttis1 and salis1 != str(hashlib.sha1(repr(salasana) + "," + shared_private_key).hexdigest()) and kayttis1 == tunnus == kayttis1:
        palautus = failsisalto + failsisalto2 + "Käyttäjätunnus oikein, mutta salasana väärin" + failsisalto3
        req.content_type =  'text/plain; charset=UTF-8'
        req.write(palautus)

    return
