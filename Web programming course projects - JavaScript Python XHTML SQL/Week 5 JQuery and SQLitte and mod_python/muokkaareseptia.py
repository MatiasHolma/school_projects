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
  <h2>Muokkaa reseptia</h2>

</article>

<article>
<h3 id="raportti"></h3>
<p><input id="Poista" name="Poista" type="submit" value="Poista"/></p>

 <p id="reseptip"> <label>Resepti</label><br /><span id="resepti" > <img src="ajax-loader2.gif" alt="loaderimg" /></span></p>
<div id=muokkauskentat> <img src="ajax-loader2.gif" alt="loaderimg" /></div>

<p><input id="Muokkaa" name="Muokkaa" type="submit" value="Muokkaa"/></p>

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

