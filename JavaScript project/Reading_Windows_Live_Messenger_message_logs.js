
function readXml(xmlFile){

var xmlDoc;

if(typeof window.DOMParser != "undefined") {
    xmlhttp=new XMLHttpRequest();
    xmlhttp.open("GET",xmlFile,false);
    if (xmlhttp.overrideMimeType){
        xmlhttp.overrideMimeType('text/xml');
    }//if1.1
    xmlhttp.send();
    xmlDoc=xmlhttp.responseXML;
}//if1
else{
    xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
    xmlDoc.async="false";
    xmlDoc.load(xmlFile);
}//else1
var tagObj=xmlDoc.getElementsByTagName("Message");
var i = 0;
  var table="<tr><th>Lahettaja</th><th>Viesti</th></tr>";
	var kayttajat = []
  for (i = 0; i <tagObj.length; i++) { 
	   table += "<tr><td>" +
    tagObj[i].childNodes[0].childNodes[0].getAttribute('FriendlyName') +
    "</td><td>" +
	tagObj[i].getAttribute('Date') + 
"</td><td>" +
tagObj[i].getAttribute('Time') + 
"</td><td>" +
    tagObj[i].childNodes[2].childNodes[0].nodeValue +
    "</td></tr>";
	var v = tagObj[i].childNodes[2];
	if (kayttajat.length == 0) {
		var kayttaja2 = new kayttaja(0,0);
		kayttaja2.nimi = tagObj[i].childNodes[0].childNodes[0].getAttribute('FriendlyName');
		kayttaja2.viesteja =kayttaja2.viesteja +1;
		kayttaja2.viestienpituus = kayttaja2.viestienpituus + tagObj[i].childNodes[2].childNodes[0].nodeValue.length;
		kayttajat.push(kayttaja2);
	}//if3
	else {
	var loytyi = false;
	for (u=0; u<kayttajat.length; u++) {
		if (kayttajat[u].nimi == tagObj[i].childNodes[0].childNodes[0].getAttribute('FriendlyName')) {
			kayttajat[u].viesteja =kayttajat[u].viesteja +1;
			kayttajat[u].viestienpituus = kayttajat[u].viestienpituus + tagObj[i].childNodes[2].childNodes[0].nodeValue.length;
			loytyi = true;
		}
		}//for
	}//else
	if (loytyi == false) {
		var kayttaja1 = new kayttaja(0,0);
		kayttaja1.nimi = tagObj[i].childNodes[0].childNodes[0].getAttribute('FriendlyName');
		kayttaja1.viesteja =kayttaja1.viesteja +1;
		kayttaja1.viestienpituus = kayttaja1.viestienpituus + tagObj[i].childNodes[2].childNodes[0].nodeValue.length;
		kayttajat.push(kayttaja1);
	}//if
	
	}
  var table2 = "<table><tr><td>Nimi</td><td>Viestien maara</td><td>Viestien pituus</td></tr>"
  for (i = 0; i < kayttajat.length; i++) {
    table2 = table2 + "<tr><td>" + kayttajat[i].nimi + "</td><td>" + String(kayttajat[i].viesteja) + "</td><td>" + String(kayttajat[i].viestienpituus) +	"</td></tr>";

  }
  table2 = table2 + "</table>"
  document.getElementById("lokit").innerHTML = table2;
  document.getElementById("demo").innerHTML = table;
  }




window.onload = function() {
	readXml("XML-file-name.xml"); //Change the name to corrert file's name
	
}

function kayttaja(x, y)
{
	this.nimi = "";
	this.viesteja = x;
	this.viestienpituus = y;	
}
// JavaScript Document