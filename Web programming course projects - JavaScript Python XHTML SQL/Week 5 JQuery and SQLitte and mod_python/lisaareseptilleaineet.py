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
  <h2>Lisaa reseptille aineet</h2>

</article>

<article>
<p id="raportti" />
<form>
 <p id="reseptip"> <label>Resepti</label><br /><span id="resepti" > <img src="ajax-loader2.gif" alt="loaderimg" /></span></p>


<div id="reseptinaineet"> <img src="ajax-loader2.gif" alt="loaderimg" /></div>

</form>
<p><input name="Lisaavaihe" id="Lisaavaihe" type="submit" value="0"/></p>
<p><input id="Tallenna" name="Tallenna" type="submit" value="Tallenna"/></p>

<p><input id="maara" name="maara" type="hidden" value="1"/></p>


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

