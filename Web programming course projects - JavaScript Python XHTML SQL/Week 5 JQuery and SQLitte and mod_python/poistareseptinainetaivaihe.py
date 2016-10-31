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
  <h2>Poista reseptin aine tai vaihe</h2>

</article>

<article>
<h3 id="raportti"> </h3>
<form>
 <p id="reseptip"> <label>Resepti</label><br /><span id="resepti" > <img src="ajax-loader2.gif" alt="loaderimg" /></span></p>
<p id="vaihep"><label>Vaihe</label><span id="vaihe"> <img src="ajax-loader2.gif" alt="loaderimg" /></span></p>
<p id="ainep"><label>Aine</label><span id="aine"> <img src="ajax-loader2.gif" alt="loaderimg" /></span></p>


</form>
<p><input id="poistavaihe" name="Poista vaihe" type="submit" value="Poista vaihe"/></p>
<p><input id="poistaaine" name="Poista aine" type="submit" value="Poista aine"/></p>

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

