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
  <h2>Lisaa ruoka-aine</h2>

</article>

<article>
<div id="raportti"></div>

<form>
<p id="nimip"> <label for="Nimi">Nimi</label> <br/>
<input id="Nimi" name="Nimi" type="text"/>   </p>
<p id="test"> </p>
<p id="kuvausp"> <label for="Kuvaus">Kuvaus</label> <br/>
<input id="Kuvaus" name="Kuvaus" type="text"/> </p>
</form>



<p><input id="lisaaruokaaine" name="Lisaa" type="submit" value="Lisaa"/></p>


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

