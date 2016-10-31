// JavaScript Document

//public-muuttujat
var alustettu = false; //muuttuja, onko ruudukkoa painettu
var pommeja; //pstyleen määrä
var x; //ruudukon leveys
var y; //ruudukon korkeus
var clist = []; //lista pstyleen sijainnista (string)
var cxlist = []; //lista lista pstyleen sijainnin x-arvosta
var cylist = []; //lista lista pstyleen sijainnin y-arvosta
var protolist = []; //prototypelista, mikä auttaa ruutujen tarkistuksessa
var spans = document.getElementsByTagName("span"); //span lista
var peliloppu = false;
var rekfoller = [];

var body = document.getElementsByTagName("body"); 
var table = document.createElement('table');


table.setAttribute('id','table');
var caption = document.createElement('caption'); //tehdään tableen caption, minne imputit voidaan sijoittaa
caption.setAttribute('id','caption');

var label1=document.createElement('label');
var t1 = document.createTextNode('Korkeus');
	//tehdään inputit
var input=document.createElement('input');
input.setAttribute('id','yinput');
input.setAttribute('type','text');
input.setAttribute('size', '3');
input.style.margin = "3px";
var input2=document.createElement('input');
var label2=document.createElement('label');
var t2 = document.createTextNode('Leveys');
input2.setAttribute('id','xinput');
input2.setAttribute('type','text');
input2.setAttribute('size', '3');
input2.style.margin = "3px";
var input3=document.createElement('input');
var label3=document.createElement('label');
var t3 = document.createTextNode('Miinoja');
input3.setAttribute('id','mines');
input3.setAttribute('type','text');
input3.setAttribute('size', '3');
input3.style.margin = "3px";

	//	document.getElementBy("tarkistus").addEventListener('click', tarkista_laskut, false);
	//<button name="tarkista" value="Tarkista" type="submit" id="tarkistus">Tarkista</button>
	
	//tehdään nappi
	var button=document.createElement('button');
	button.setAttribute('id','make');
	button.setAttribute('type','submit');
	button.setAttribute('name', 'make');
	button.setAttribute('size', '3');
	var tet = document.createTextNode('make');
	
	
window.onload = function() {
	y = 8; //oletus y-arvo
	x = 8; //oletus x-arvo
	pommeja = 15; //oletus pstylearvo
	
	//tehdään body ja table
	
	table.appendChild(caption);
	
	label1.appendChild(t1);
	
	

	label1.appendChild(input);
	caption.appendChild(label1);

	label2.appendChild(t2);
	label2.appendChild(input2);
	caption.appendChild(label2);

	label3.appendChild(t3);
	label3.appendChild(input3);
	caption.appendChild(label3);

	caption.appendChild(button);

	button.appendChild(tet);
	button.addEventListener('click', luo_ruudukko, false); //lisätään napille toiminto 
	
	
	body[0].appendChild(table); //laitetaan tehdyt jutut näkyviin
	//luo_ruudukko(x,y);
	
}


//jos ikkunan koko muuttuu
window.onresize = function(event) {
	
	var spanlist = document.getElementsByTagName("span");	
    
	
	//tarkistetaan onko leveys vai korkeus suurempi
	if(window.innerHeight + 200 < window.innerWidth) {
		var kaytettava = window.innerHeight - 200;
	}
	else {
		var kaytettava = window.innerWidth - 200;
	}
	kaytettava = kaytettava / x;
	var kayst = kaytettava.toString() + "px";
	
	//muutetaan palikoiden kokoa näyötn koon mukaiseksi
	for (i=0; i<spanlist.length;i++) {
		spanlist[i].style.width = kayst;
		spanlist[i].style.height = kayst;
	}
	
	var tdlist = document.getElementsByTagName("td");
	
	for (i=0; i<tdlist.length;i++) {
		//tdlist[i].style.borderStyle="outset";
		
	}
	
}

function luo_ruudukko() {
	clist = []; //määritellään clist uudelleen
	cxlist = []; //määritellään cxlist uudelleen
	cylist = [];
	protolist = [];
	alustettu = false;
	peliloppu = false;
	
	//sijoitetaan inputtien arvot
	y = parseInt(document.getElementById('yinput').value); 
	x = parseInt(document.getElementById('xinput').value);
	pommeja = parseInt(document.getElementById('mines').value);
	
	//tehdään lista prototypeista
	makeprotolist(x,y);
	
	//poistetaan mahdolliset vanhat rivit.
	var table = document.getElementsByTagName("table");
	if (table[0].childNodes.length>1){
		var len = table[0].childNodes.length-1;
		for (f=len;f>=1;f--) {
			if (table[0].removeChild(table[0].childNodes[f]));
		}
	}
	
	table = document.getElementById("table");
	
	//tarkistetaan, ettei inputteihin ole syötetty laittomia arvoja
	if (x > 32) return;
	if (y > 32) return;
	if (x < 8) return;
	if (x < 8) return;
	if (pommeja > (x*y)) return;
	if (pommeja < 0) return;
	//var table = document.getElementById("table");
	
	//tehdään muuttujat while-silmukkaan
	var i = 0;
	var o = 0;
	var tr; 
	
	
	//luodaan taulukko
	while (i < y){
		tr = document.createElement('tr');
		tr.setAttribute('id','' + i);
		while (o < x){
			var td = document.createElement('td');
			var span = document.createElement('span');
			span.setAttribute('id','' + i + '.' + o);
			span.className = "tyhja";
			span.addEventListener('click', tarkista, false);
			
			text = document.createTextNode('');
			span.appendChild(text);
			
			
			td.appendChild(span);
			tr.appendChild(td);
			o++;
		}
		o=0;
		i++;
		table.appendChild(tr);
	}
	
	//määritellään tyylit
	make_styles(x,y);
	
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}


function make_styles(){
	var spanlist = document.getElementsByTagName("span");	
    

	
	if(window.innerHeight < window.innerWidth) {
		var kaytettava = window.innerHeight - 240;
	}
	else {
		var kaytettava = window.innerWidth - 240;
	}
	kaytettava = kaytettava / x;
	var kayst = kaytettava.toString() + "px";

	for (i=0; i<spanlist.length;i++) {
		//spanlist[i].style.margin="5px";
		spanlist[i].style.border="4px groove silver";
		spanlist[i].style.padding="0";
		spanlist[i].style.margin="0";
		
		spanlist[i].style.width = kayst;
		spanlist[i].style.height = kayst;
		//spanlist[i].style.minHeight="47px";
		spanlist[i].style.display="block";
		//spanlist[i].style.borderRadius="50%";
		spanlist[i].style.backgroundColor="silver";
	}
	
	var tdlist = document.getElementsByTagName("td");
	
	for (i=0; i<tdlist.length;i++) {
		//tdlist[i].style.borderStyle="outset";
		
	}

	
	
}

function tarkista(event){
	
	if(peliloppu)return;
	
	//Tarkistetaan onko alustettu
	if(!alustettu) {
		
	alustettu = true;
	var c = 0;
	var t = 0;
	var moka = false; //moka syntyy jos pstyle arvotaan laittomaan paikkaan

	
	//määritellään pstyleruudut
	while(t<pommeja)
	{
		var y1 = getRandomInt(0,y-1); //arvotaan y-koordinaatti
		var x1 = getRandomInt(0,x-1); //arvotaan x-koordinaatti
		var str = "" + y1 + "." + x1; //tehdään strin
		var tsrt = "" + y1 + "." + x1; //tehdään strinistä kopio, mitä voidaan muokata
		if(str==event.target.id)//varmistetaan, painetusta nappulasta tehdä pstylea.
		{
			moka =true;
				
		}
		tsrt = "" + (y1-1) + "." + (x1-1);
		if(tsrt==event.target.id)moka = true;//varmistetaan, ettei pstyle tule napin viereen.
		tsrt = "" + (y1-1) + "." + x1;
		if(tsrt==event.target.id)moka = true;//varmistetaan, ettei pstyle tule napin viereen.
		tsrt = "" + (y1-1) + "." + (x1+1);
		if(tsrt==event.target.id)moka = true;//varmistetaan, ettei pstyle tule napin viereen.
		tsrt = "" + y1 + "." + (x1-1);
		if(tsrt==event.target.id)moka = true;//varmistetaan, ettei pstyle tule napin viereen.
		tsrt = "" + y1 + "." + (x1+1);
		if(tsrt==event.target.id)moka = true;//varmistetaan, ettei pstyle tule napin viereen.
		tsrt = "" + (y1+1) + "." + (x1-1);
		if(tsrt==event.target.id)moka = true;//varmistetaan, ettei pstyle tule napin viereen.
		tsrt = "" + (y1+1) + "." + x1;
		if(tsrt==event.target.id)moka = true;//varmistetaan, ettei pstyle tule napin viereen.
		tsrt = "" + (y1+1) + "." + (x1+1);
		if(tsrt==event.target.id)moka = true;//varmistetaan, ettei pstyle tule napin viereen.
		
		if (moka) { //jos moka sattuu, jatketaan silmukkaa samalla t-arvolla ja arvotaan pstylepaikat uudestaan
			
			moka = false;
			continue; 
		}
		
		//varmistetaan, ettei sama luku arvota kahteen kertaan
		while(c<clist.length) {
			if (str == clist[c]) {
				c = -1; //muutetaan c:arvoa -1:seksi, jotta virhe huomataan helpstylen silmukan jälkeen
				break;
			}
			c++;
		}
		if (c != -1) {
			cxlist.push(x1); //tallennetaan x-koordinaatti
			cylist.push(y1); //tallennetaan y-koordinaatti
			clist.push(str); //tallennetaan koordinaatit
			t++;
		}
		c=0;
	} 
		
		//sijoitetaan pstylet ruutuihin
		for (p=0;p<clist.length;p++)
		{
			document.getElementById(clist[p]).className = "pstyle"; //muutetaan arvotun pstylepaikan luokaksi "pstyle"
		}
		
		
		//lasketaan montako pstylea jokaista ruutua ympäröi
		laske_ymparoivat();
		
		raivaa(event.target);
		return;
	} //if alustettu loppuu
	
	
	
	
	
	
	
	//if(event.target.className != "pstyle")
	
	//jos pelaaja painaa pstylea
	if(event.target.className == "pstyle")
	{
		
		peliloppu=true;
		//muutetaan pstyleruutua
		event.target.style.border="0px groove silver";
		event.target.style.backgroundColor="white";
		
		//tehdään pstylekuva
		var img = document.createElement('img');
		img.src = "mine.svg";
		img.alt = "auki";
		img.style.marginTop = "-10px";
		img.style.padding = "10px";
		img.style.marginBottom = "-15px";
		img.style.minHeight = "40px";
		img.style.minWidth = "40px";
		event.target.appendChild(img);
		var list = document.getElementsByTagName("span");
		
		//laitetaan kaikki pstylen näkyviin
		for (i=0; i<list.length;i++) {
			if (list[i].className == "pstyle"){
				if(list[i] != event.target) {
				img = document.createElement('img');
				img.src = "mine.svg";
				img.alt = "auki";
				img.style.width = event.target.style.width;
				img.style.height = event.target.style.height;
				list[i].appendChild(img);
				list[i].style.border="0px groove silver";
				list[i].style.backgroundColor="white";
				img.style.marginTop = "-10px";
				img.style.padding = "10px";
				img.style.marginBottom = "-15px";
				img.style.minHeight = "40px";
				img.style.minWidth = "40px";
				
			} }
		}

	}
	else {
		raivaa(event.target);
	}
}

function laske_ymparoivat()
{
	//tehdään bool-muuttujan symbolisoimaan jokaista ruudun viereistä ruutua.
	var p11 = true;
	var p12 = true;
	var p13 = true;
	var p21 = true;
	var p23 = true;
	var p31 = true;
	var p32 = true;
	var p33 = true;
	
	//tehdään apumuuttujat
	var cx = 0;
	var cy = 0;
	var kasiteltava;
	var kasproto;
	
	//käydään lä'pi kaikki pstylepaikat, ja "ilmoitetaan sen viereisille ruuduille
	for(i=0;i<cxlist.length;i++) {
		
		 p11 = true;
		 p12 = true;
		 p13 = true;
		 p21 = true;
		 p23 = true;
		 p31 = true;
		 p32 = true;
		 p33 = true;
		 cx = cxlist[i];
		 cy = cylist[i];
		
		
		//katsotaan onko käsiteltava ruutu reunalla
		if (cxlist[i]+1 >= x) {
			p13 = false;
			p23 = false;
			p33 = false;
		}
		if (cylist[i]+1 >= y) {
			p31 = false;
			p32 = false;
			p33 = false;
		}
		
		if (cxlist[i]-1 < 0)  {
			p11 = false;
			p21 = false;
			p31 = false;
		}
		if (cylist[i]-1 < 0) {
			p11 = false;
			p12 = false;
			p13 = false;
		}
		
		
		//tehdään operaatio, jos ruutu ei ole reunalla
		if(p11) {
			cy = cylist[i]-1;
			cx = cxlist[i]-1;
			kasproto = etsiproto(cy,cx);
			kasproto.v = kasproto.v+1;

			
			cx = 0;
			cy = 0;
			//luku = 0;
		}
		
		if(p12) {
			cy = cylist[i]-1;
			cx = cxlist[i];
			kasproto = etsiproto(cy,cx);
			kasproto.v = kasproto.v+1;

			
			cx = 0;
			cy = 0;
			//luku = 0;
		}
		
		if(p13) {
			cy = cylist[i]-1;
			cx = cxlist[i]+1;
			kasproto = etsiproto(cy,cx);
			kasproto.v = kasproto.v+1;

			
			cx = 0;
			cy = 0;
			//luku = 0;
		}
		
		if(p21) {
			cy = cylist[i];
			cx = cxlist[i]-1;
			kasproto = etsiproto(cy,cx);
			kasproto.v = kasproto.v+1;

			cx = 0;
			cy = 0;

		}
		
		if(p23) {
			cy = cylist[i];
			cx = cxlist[i]+1;
			kasproto = etsiproto(cy,cx);
			kasproto.v = kasproto.v+1;

			
			cx = 0;
			cy = 0;
			//luku = 0;
		}
		
		if(p31) {
			cy = cylist[i]+1;
			cx = cxlist[i]-1;
			kasproto = etsiproto(cy,cx);
			kasproto.v = kasproto.v+1;

			
			cx = 0;
			cy = 0;
			//luku = 0;
		}
		
		if(p32) {
			cy = cylist[i]+1;
			cx = cxlist[i];
			kasproto = etsiproto(cy,cx);
			kasproto.v = kasproto.v+1;

			cx = 0;
			cy = 0;

		}
		
		if(p33) {
			cy = cylist[i]+1;
			cx = cxlist[i]+1;
			kasproto = etsiproto(cy,cx);
			kasproto.v = kasproto.v+1;

			
			cx = 0;
			cy = 0;
			//luku = 0;
		}
		
		
		
	}
}

//tehdään lista ruutua edustavista protypeista
function makeprotolist(x,y)
{
	var o = 0;
	var t = 0;
	
	while (o<y) {
		while (t<x) {
			var proto = new ruutu(o,t,0);
			protolist.push(proto);
			t++;
		}
		t=0;
		o++;
	}
}

//luodaan prototyype;
function ruutu(ys,xs,v) {
    this.ys = ys; //ruudun y-arvo
	this.xs = xs; //ruudun x-arvo
	this.v = v; //montako pstylea sen vieressä on
	this.state = true; //onko sitä painettu
}


//etsitään tietty prototype
function etsiproto(ye,xe) {
	for (q=0; q<protolist.length;q++) {
		if (protolist[q].ys == ye && protolist[q].xs == xe) return protolist[q];	
	}
	var testerror = true;
}


//paljastetaan turvallinen ruutu
function numeronakyviin(nproto) {
	var kasiteltava =  document.getElementById('' + nproto.ys + '.' + nproto.xs);
	if (nproto.v!=0)kasiteltava.textContent = "" + nproto.v;
	kasiteltava.parentNode.style.borderWidth="0.1px";
	kasiteltava.style.backgroundColor = "#FFFFFF";
	nproto.state = false;
}



function raivaa(klikattu) {
	
	//etsitään oikeaa ruutua vastaava prototype ja käsketaan sen kutsua vieressä olevia ruutuja
	for(s=0;s<protolist.length;s++) {
		var st = "" + protolist[s].ys + "." + protolist[s].xs;
		if (klikattu.id == st) {
			ekakutsuvieresta(protolist[s]);
			break;	
		}
	}
}


//samanlainen kun "kutsuvieresta, muttei sisällä ehtoa if(kproto.v>1) return;
function ekakutsuvieresta(kproto) {
	
	if(!kproto.state) return;
	//var table = document.getElementById("table");
	//if(kproto.v>1) return;
	var tdd = document.getElementById("" + kproto.ys + "." + kproto.xs);
	if (tdd.className == "pstyle") return;
	
	numeronakyviin(kproto);
	var q11 = true;
	var q12 = true;
	var q13= true;
	var q21 = true;
	var q23 = true;
	var q31 = true;
	var q32 = true;
	var q33 = true;
	
	if (kproto.ys == 0) {
		q11 = false;
		q12 = false;
		q13 = false;
	}
	
	if (kproto.xs == 0) {
		q11 = false;
		q21 = false;
		q31 = false;
	}
	
	if (kproto.ys == y-1) {
		q31 = false;
		q32 = false;
		q33 = false;
	}
	
	if (kproto.xs == x-1) {
		q13 = false;
		q23 = false;
		q33 = false;
	}
	
	var vika = false;
	
	if(null == (etsiproto(kproto.ys-1,kproto.xs-1)))vika = true;;
	if(null == (etsiproto(kproto.ys-1,kproto.xs)))vika = true;
	if(null == (etsiproto(kproto.ys-1,kproto.xs+1)))vika = true;
	if(null == (etsiproto(kproto.ys,kproto.xs-1)))vika = true;
	if(null == (etsiproto(kproto.ys,kproto.xs+1)))vika = true;
	if(null == (etsiproto(kproto.ys+1,kproto.xs-1)))vika = true;
	if(null == (etsiproto(kproto.ys+1,kproto.xs)))vika = true;
	if(null == (etsiproto(kproto.ys+1,kproto.xs+1)))vika = true;
	
	
	if (vika) {
		var err=0;	
	}
	
	if(q11)kutsuvieresta(etsiproto(kproto.ys-1,kproto.xs-1));
	if(q12)kutsuvieresta(etsiproto(kproto.ys-1,kproto.xs));
	if(q13)kutsuvieresta(etsiproto(kproto.ys-1,kproto.xs+1));
	if(q21)kutsuvieresta(etsiproto(kproto.ys,kproto.xs-1));
	if(q23)kutsuvieresta(etsiproto(kproto.ys,kproto.xs+1));
	if(q31)kutsuvieresta(etsiproto(kproto.ys+1,kproto.xs-1));
	if(q32)kutsuvieresta(etsiproto(kproto.ys+1,kproto.xs));
	if(q33)kutsuvieresta(etsiproto(kproto.ys+1,kproto.xs+1));
	
	q11 = true;
	q12 = true;
	q13 = true;
	q21 = true;
	q23 = true;
	q31 = true;
	q32 = true;
	q33 = true;
	
	return;
}


//paljastaa ruudun, ja sen viereiset turvalliset ruudut
function kutsuvieresta(kproto) {
	
	//lisätään rekursionseurantaan alkio. Helpottaa debuggausta
	rekfoller.push("" + kproto.ys + "." + kproto.xs);
	
	
	
	
	if(!kproto.state) {
		
		 return;
	}
	
	//haetaan protoa vastaava span ja tarkistetaan, ettei siinä ole pstylea
	var tdd = document.getElementById("" + kproto.ys + "." + kproto.xs);
	if (tdd.className == "pstyle") return;
	numeronakyviin(kproto);
	//var table = document.getElementById("table");
	if(kproto.v>0) {
		 return;
	}
	
	
	//jokainen boolean symbolisoi vieressä olevaa ruutua. Tarekistetaan, onko ruutu jollain reunalla
	var q11 = true;
	var q12 = true;
	var q13= true;
	var q21 = true;
	var q23 = true;
	var q31 = true;
	var q32 = true;
	var q33 = true;
	
	if (kproto.ys == 0) {
		q11 = false;
		q12 = false;
		q13 = false;
	}
	
	if (kproto.xs == 0) {
		q11 = false;
		q21 = false;
		q31 = false;
	}
	
	if (kproto.ys == y-1) {
		q31 = false;
		q32 = false;
		q33 = false;
	}
	
	if (kproto.xs == x-1) {
		q13 = false;
		q23 = false;
		q33 = false;
	}
	

	
	
	if(q11)kutsuvieresta(etsiproto(kproto.ys-1,kproto.xs-1));
	if(q12)kutsuvieresta(etsiproto(kproto.ys-1,kproto.xs));
	if(q13)kutsuvieresta(etsiproto(kproto.ys-1,kproto.xs+1));
	if(q21)kutsuvieresta(etsiproto(kproto.ys,kproto.xs-1));
	if(q23)kutsuvieresta(etsiproto(kproto.ys,kproto.xs+1));
	if(q31)kutsuvieresta(etsiproto(kproto.ys+1,kproto.xs-1));
	if(q32)kutsuvieresta(etsiproto(kproto.ys+1,kproto.xs));
	if(q33)kutsuvieresta(etsiproto(kproto.ys+1,kproto.xs+1));
	
	q11 = true;
	q12 = true;
	q13 = true;
	q21 = true;
	q23 = true;
	q31 = true;
	q32 = true;
	q33 = true;
	

}