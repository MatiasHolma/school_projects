var map;
var vlat =  62.23333
var vlng =  25.73333
var linkki;
var jsonString;
var realJson;
function initMap() {
	
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: vlat, lng: vlng},
    zoom: 12
  });
  


}
window.onload = function() {
	var selectbar = document.createElement('select');
	selectbar.setAttribute('id','valikko');
	var option1 = document.createElement('option');
	option1.setAttribute('value','Jyväskylä');
	
	var text1 = document.createTextNode('Jyväskylä');
	option1.appendChild(text1);
	var option2 = document.createElement('option');
	option2.setAttribute('value','Tampere');
	var text2 = document.createTextNode('Tampere');
	option1.setAttribute('selected','selected');
	option2.appendChild(text2);
	var option3 = document.createElement('option');
	option3.setAttribute('value','Helsinki');
	var text3 = document.createTextNode('Helsinki');
	option3.appendChild(text3);
	//var divi = document.getElementById('ennuste');
	//divi.appendChild(selectbar);
	var kaupunkitd = document.getElementById('kaupunki');
	kaupunkitd.appendChild(selectbar);
	selectbar.appendChild(option1);
	selectbar.appendChild(option2);
	selectbar.appendChild(option3);
	option1.addEventListener('click', statechanged, false);
	option2.addEventListener('click', statechanged, false);
	option3.addEventListener('click', statechanged, false);
	
	
	
	var kaupunkitd = document.getElementById('kaupunki');
	//kaupunkitd.removeChild(kaupunkitd.childNodes[0]);
	//var kaupunkitxt = document.createTextNode(document.getElementById('valikko').value);
	//kaupunkitd.appendChild(kaupunkitxt);
	statechanged();
}

function statechanged() {
	switch( document.getElementById('valikko').value) {
    case "Jyväskylä":
        var vlat =  62.23333
		var vlng =  25.73333
		linkki = "http://api.openweathermap.org/data/2.5/weather?lon=25.7333&lat=62.2333&mode=json"
        break;
    case "Tampere":
        var vlat =  61.49911
		var vlng =  23.78712
		linkki = "http://api.openweathermap.org/data/2.5/weather?lon=23.78712&lat=61.49911&mode=json"
        break;
    case "Helsinki":
        var vlat =  60.17556
		var vlng =  24.93417
		linkki = "http://api.openweathermap.org/data/2.5/weather?lon=24.93417&lat=60.17556&mode=json"
        break;
    default:
        break;


	
} 
 map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: vlat, lng: vlng},
    zoom: 12
  });
  
  httpGet(linkki);
 realJson = JSON.parse(jsonString);
 //  realJson = eval(jsonString);
  
	var aint = parseFloat(realJson.main.temp);
	var celsiusint = aint - 273.15;
	var celsius = celsiusint.toString();
	celsius = celsius.substring(0, 4);
	var lampotd = document.getElementById('lampotila');
	lampotd.removeChild(lampotd.childNodes[0]);
	var lampotila = document.createTextNode(celsius);
	lampotd.appendChild(lampotila);
	
	var paine = realJson.main.pressure;
	var painetd = document.getElementById('ilmanpaine');
	painetd.removeChild(painetd.childNodes[0]);
	var ilmanpaine = document.createTextNode(paine);
	painetd.appendChild(ilmanpaine);
	
	

	
	
	var ilmankosteus = realJson.main.humidity;
	var kosteustd = document.getElementById('kosteus');
	kosteustd.removeChild(kosteustd.childNodes[0]);
	var kosteustxt = document.createTextNode(ilmankosteus);
	kosteustd.appendChild(kosteustxt);
	
	
	var tuulennopeus = realJson.wind.speed;
	var nopeustd = document.getElementById('tuulennopeus');
	nopeustd.removeChild(nopeustd.childNodes[0]);
	var nopeustxt = document.createTextNode(tuulennopeus);
	nopeustd.appendChild(nopeustxt);
	
	var tuulensuunta = realJson.wind.deg;
    if (!tuulensuunta) tuulensuunta = "ei mitattu"
	var suuntatd = document.getElementById('tuulensuunta');
	suuntatd.removeChild(suuntatd.childNodes[0]);
	var suuntatxt = document.createTextNode(tuulensuunta);
	suuntatd.appendChild(suuntatxt);

	
	$.ajax({
        async: true,
        url: "py/xmlnapu.py",
        data: {"kaupunki": document.getElementById('valikko').value},
//      data: {"postinro": $('#postinro').val() },
        processData: true,
        dataType: "text",
        type: "GET",
        success: alusta,
        error: ajax_virhe
});

  
  
  
}

function alusta(data, textStatus, request) {
	
	var halkaistu = data.split("T");
	var pvm = halkaistu[0].split("-");

	//alert(halkaistu[0]);
	
	var paivatd = document.getElementById('viimeksipaivitettu');
	paivatd.removeChild(paivatd.childNodes[0]);
	paivastr =  pvm[2] + "." + pvm[1] + "." + pvm[0] + " Klo: " + halkaistu[1];
	var paivitettu = document.createTextNode(paivastr);
	
	paivatd.appendChild(paivitettu);
	
}


function httpGet(theUrl)
{
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
			jsonString=xmlhttp.responseText;
            return xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET", theUrl, false );
    xmlhttp.send();    
}

function ajax_virhe(event, jqxhr, settings, exception) {
	 console.log( exception );
}


/*
  <script>
  $.get("http://api.openweathermap.org/data/2.5/weather?lon=25.7333&lat=62.2333&mode=json", function(data) {
	 document.write(data);
	 //var m = eval(
  });
  </script>*/