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
  <h2>Lisää tai poista ruokalaji</h2>
</article>
<article>
<div id="raportti"></div>

<form>
 <p> <label for="Nimi">Nimi</label> <br /><input type="text" name="Nimi" id="Nimi" /> <span id="Nimip" >*</span></p>
<p> <label for="Kuvaus">Kuvaus</label> <br /><input type="text" name="Kuvaus" id="Kuvaus" /> <span id="Kuvausp">*</span></p>
 <p id="ruokalajip"> <label>Ruokalaji</label><br /><span id="ruokalaji" > <img src="ajax-loader2.gif" alt="loaderimg" /></span></p>
  </form>
  <p><input type="submit" name="lisaaruokalaji" value="Lisaa" id="lisaaruokalaji" /></p>
 <p><input type="submit" name="poistaruokalaji" value="Poista" id="poistaruokalaji" /></p>
</article>
</section>
</div>
"""


def index(req):
    req.content_type =  'text/plain; charset=UTF-8'

    try:
        req.write(palautus)
        return
    except:
        return "vika"

