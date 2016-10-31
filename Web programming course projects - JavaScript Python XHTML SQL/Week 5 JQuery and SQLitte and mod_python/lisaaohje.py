from pysqlite2 import dbapi2 as sqlite
import os
import os.path
import sys
from xml.dom.minidom import getDOMImplementation, parse, parseString
from mod_python import apache, Cookie
import time
from mod_python import apache, Session
from cgi import escape


palautus = """
<div id="sisalto">
<section>
<article>
  <h2>Lisää reseptin vaiheet</h2>
</article>
<article>
<h3 id="raportti"></h3>
<form>
 <p id="reseptip">  <br /><span id="resepti" > <img src="ajax-loader2.gif" alt="loaderimg" /></span></p>
 <div id="vaiheet"> <img src="ajax-loader2.gif" alt="loaderimg" /></div>

</form>
 <p><input type="submit" name="Lisaa" id="Lisaa" value="0" /></p>
  <p><input id="Tallenna" type="submit" name="Tallenna" value="Tallenna" /></p>

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

