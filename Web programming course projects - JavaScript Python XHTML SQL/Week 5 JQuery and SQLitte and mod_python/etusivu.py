from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from xml.dom.minidom import getDOMImplementation, parse, parseString
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape


palautus = """<div id="sisalto">
<section>

<article>
  <h2>Reseptit</h2>
  <p id="lista"> <img src="ajax-loader2.gif" alt="loaderimg" /> </p>
</article>

<article>



<h2>Lisää resepti</h2>
<div id="raportti"></div>

<form>


 <p> <label for="Nimi">Nimi</label> <br /><input type="text" name="Nimi" id="Nimi" class="kentta" /> <span id="Nimip" >*</span></p>
<p> <label for="Kuvaus">Kuvaus</label> <br /><input type="text" name="Kuvaus" id="Kuvaus" class="kentta" /> <span id="Kuvausp">*</span></p>

 <p> <label for="henmaara">Henkilömäärä</label> <br /> <input type="number" name="henmaara" min="1" max="100" step="1" value="1" id="henmaara"><p id="henmaarap"></p>
 <p id="ruokalajip"> <label>Ruokalaji</label><br /><span id="ruokalaji" >*</span></p>
  </form>

 <p><input id="Laheta" type="submit" name="laheta" value="Laheta" /></p>




</article>

</section>
</div>"""

def index(req):
    req.content_type =  'text/plain; charset=UTF-8'

    try:
        req.write(palautus)
        return
    except:
        return "vika"
