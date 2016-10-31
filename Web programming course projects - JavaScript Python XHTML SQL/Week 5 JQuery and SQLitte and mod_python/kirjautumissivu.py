palautus = """
<div id="body">

<div id="lataus"></div>

<p><label>Tunnus</label> <input id="tunnus" name="tunnus" type="text"/><span id="vaaratunnus">
<span></p>
<p><label>Salasana </label><input id="salasana" name="salasana" type="password"/><span id="vaarasalasana"></span></p>
<p><input id="kirjaudu" name="kirjaudu" type="submit" value="kirjaudu"/></p>
</div>
"""
def index(req):
    req.content_type =  'text/plain; charset=UTF-8'

    try:
        req.write(palautus)
        return
    except:
        return "vika"

