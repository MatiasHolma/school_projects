var vaihelisaysalustettu = false;
var ainelisaysalustettu = false;
var reseptinmuokkausalustettu = false;
var muutosalustettu = false;
window.onload = function(){
    $( "#kirjaudu" ).on("click",function(){
	$('#lataus').replaceWith($.parseHTML("<div id='lataus'></div><div id='ajax1'><img src='19-0.gif' alt='loaderimg' /></div>" ));

	//<div id="lataus"></div>

		
        $.ajax({
            async: true,
            url: "autentikointi.py",
            data:  {"tunnus": $('#tunnus').val(),  "salasana": $('#salasana').val()},
//      data: {"postinro": $('#postinro').val() },
            processData: true,
            dataType: "text",
            type: "POST",
            success: autentikoi,
            error: ajax_virhe
		});
		$('#body').replaceWith($.parseHTML("<div id='body'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

	});


}

 function autentikoi(data, textStatus, request) {
	 $('#body').replaceWith($.parseHTML(data));
	 if ($( "#Laheta").val() == null) {
		 $( "#kirjaudu" ).on("click",function(){
	$('#lataus').replaceWith($.parseHTML("<div id='lataus'></div><div id='ajax2'><img src='19-0.gif' alt='loaderimg' /></div>" ));


			 $.ajax({
				 async: true,
				 url: "autentikointi.py",
				 data:  {"tunnus": $('#tunnus').val(),  "salasana": $('#salasana').val()},
//      data: {"postinro": $('#postinro').val() },
				 processData: true,
				 dataType: "text",
				 type: "POST",
				 success: autentikoi,
				 error: ajax_virhe
			 });
			 $('#body').replaceWith($.parseHTML("<div id='body'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));
		 });

	 }
	 else {
		 kirjauduttu();

	 }

 }

 function kirjauduttu() {
	 paivitalista();
	 //paivitavalikko();

	 $( ".kentta" ).on("change",function(){
		 if ( $(this).val() !=null){

			 if ( $(this).val().length < 3){

				 tulivirhe(this);
			 }

			 else {
				 var id = $(this).attr("id");
				 $( "#" + id + "p" ).text("");
			 }


			 //tarkistaKaikki();
		 }
		 else {
			 tulivirhe(this);
		 }

	 });

	 $( "#Laheta" ).on("click",function(){
		 $('#raportti').replaceWith($.parseHTML("<div id='raportti'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));
		 var virhe = false;

		 if( $( "#" + "Nimi" ).val()  == null){
			 virhe = true;

		 }
		 else {
			 if ( $( "#" + "Nimi" ).val().length < 3)
				 virhe = true;
		 }


		 if( $( "#" + "Kuvaus" ).val()  == null){
			 virhe = true;

		 }
		 else {
			 if ( $( "#" + "Kuvaus" ).val().length < 3)
				 virhe = true;
		 }

		 if( $( "#" + "henmaara" ).val()  == null){
			 virhe = true;

		 }
		 else {
			 if ( $( "#" + "henmaara" ).val().length < 1)
				 virhe = true;
		 }


		 if (virhe == false) {
			 $('#ruokalajit').replaceWith($.parseHTML("<div id='ruokalajit'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));
			 $('#lista').replaceWith($.parseHTML("<div id='lista'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));
				$('#lataus').replaceWith($.parseHTML("<div id='lataus'></div><div id='ajax3'><img src='19-0.gif' alt='loaderimg' /></div>" ));

			 $.ajax({

				 async: true,
				 url: "lisays.py",
				 data:  {"Nimi": $('#Nimi').val(),  "Kuvaus": $('#Kuvaus').val(), "henmaara": $('#henmaara').val(), "ruokalaji": $('#ruokalaji').val()},
//      data: {"postinro": $('#postinro').val() },
				 processData: true,
				 dataType: "text",
				 type: "POST",
				 success: lisatty,
				 error: ajax_virhe
			 });





		 }


	 });

	 $( '#Etusivu' ).on("click",function(){
		 $('#sisalto').empty();
		 $('#sisalto').replaceWith($.parseHTML("<div id='sisalto'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		 $.ajax({
			 async: true,
			 url: "etusivu.py",
			 data:  $('Etusivu'),
//      data: {"postinro": $('#postinro').val() },
			 processData: true,
			 dataType: "text",
			 type: "POST",
			 success: paivitaetusivu,
			 error: ajax_virhe

		 });

	 });





	 $( '#Lisaataipoistaruokalaji').on("click",function(){
		 $('#sisalto').replaceWith($.parseHTML("<div id='sisalto'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));
		 $.ajax({
			 async: true,
			 url: "lisaapoistaruokalaji.py",
			 data:  $('ruokalaji'),
//      data: {"postinro": $('#postinro').val() },
			 processData: true,
			 dataType: "text",
			 type: "POST",
			 success: paivitalisaapoistaruokalajisivu,
			 error: ajax_virhe

		 });

	 });






	 $( '#Lisaareseptinvaiheet').on("click",function(){
		 $('#sisalto').empty();
		 $('#sisalto').replaceWith($.parseHTML("<div id='sisalto'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		 vaihelisaysalustettu = false;
		 $.ajax({
			 async: true,
			 url: "lisaaohje.py",
			 data:  $('Lisaaohje'),
//      data: {"postinro": $('#postinro').val() },
			 processData: true,
			 dataType: "text",
			 type: "POST",
			 success: paivitalisaareseptinvaiheetsivu,
			 error: ajax_virhe

		 });


	 });




	 $( '#Muokkaareseptia' ).on("click",function(){
		 $('#sisalto').empty();
		 $('#sisalto').replaceWith($.parseHTML("<div id='sisalto'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		 reseptinmuokkausalustettu = false;
		 $.ajax({
			 async: true,
			 url: "muokkaareseptia.py",
			 data:  $('Muokkaareseptia'),
//      data: {"postinro": $('#postinro').val() },
			 processData: true,
			 dataType: "text",
			 type: "POST",
			 success: paivitamuokkaareseptiasivu,
			 error: ajax_virhe

		 });

	 });






	 $( '#Lisaaruoka-aine' ).on("click",function(){
		 $('#sisalto').empty();
		 $('#lataus').replaceWith($.parseHTML("<div id='lataus'></div><div id='ajax13'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		 $.ajax({
			 async: true,
			 url: "lisaaruokaaine.py",
			 data:  $('Lisaaruokaaine'),
//      data: {"postinro": $('#postinro').val() },
			 processData: true,
			 dataType: "text",
			 type: "POST",
			 success: paivitalisaaruokaainesivu,
			 error: ajax_virhe

		 });

	 });




	 $( '#Lisaareseptilleaineet' ).on("click",function(){
		 $('#sisalto').empty();
		 $('#sisalto').replaceWith($.parseHTML("<div id='sisalto'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		 ainelisaysalustettu = false;
		 $.ajax({
			 async: true,
			 url: "lisaareseptilleaineet.py",
			 data:  $('Lisaareseptilleaineet'),
//      data: {"postinro": $('#postinro').val() },
			 processData: true,
			 dataType: "text",
			 type: "POST",
			 success: paivitalisaareseptilleaineetsivu,
			 error: ajax_virhe

		 });

	 });




	 $( '#Poistareseptinainetaivaihe' ).on("click",function(){
		 $('#sisalto').empty();
		 $('#sisalto').replaceWith($.parseHTML("<div id='sisalto'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		 muutosalustettu = false;
		 $.ajax({
			 async: true,
			 url: "poistareseptinainetaivaihe.py",
			 data:  $('Poistareseptinainetaivaihe'),
//      data: {"postinro": $('#postinro').val() },
			 processData: true,
			 dataType: "text",
			 type: "POST",
			 success: paivitapoistareseptiainetaivaihesivu,
			 error: ajax_virhe

		 });


	 });



	 $( '#Kirjauduulos' ).on("click",function(){
		 $('#body').empty();
		 $('#body').replaceWith($.parseHTML("<div id='body'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		 $.ajax({
			 async: true,
			 url: "kirjautumissivu.py",
			 data:  $('Kirjauduulos'),
//      data: {"postinro": $('#postinro').val() },
			 processData: true,
			 dataType: "text",
			 type: "POST",
			 success: loggedout,
			 error: ajax_virhe

		 });


	 });


 }

function loggedout(data, textStatus, request) {
	$('#body').replaceWith($.parseHTML(data));

	$( "#kirjaudu" ).on("click",function(){
		$('#lataus').replaceWith($.parseHTML("<div id='lataus'></div><div id='ajax5'><img src='19-0.gif' alt='loaderimg' /></div>" ));

		$.ajax({

			async: true,
			url: "autentikointi.py",
			data:  {"tunnus": $('#tunnus').val(),  "salasana": $('#salasana').val()},
//      data: {"postinro": $('#postinro').val() },
			processData: true,
			dataType: "text",
			type: "POST",
			success: autentikoi,
			error: ajax_virhe
		});
		$('#body').replaceWith($.parseHTML("<div id='body'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));


	});

}

function paivitapoistareseptiainetaivaihesivu(data, textStatus, request) {
	$('#sisalto').replaceWith($.parseHTML(data));

	//TODO: toiminnot napeille
	$('#poistavaihe').on("click",function(){
		$('#raportti').replaceWith($.parseHTML("<div id='raportti'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		$.ajax({
			async: true,
			url: "deletereseptinvaihe.py",
			data: {"resepti": $('#resepti').val(), "vaiheet": $('#vaiheet').val()},
//      data: {"postinro": $('#postinro').val() },
			processData: true,
			dataType: "text",
			type: "GET",
			success: aineentaivaiheenpoistoonnistui,
			error: ajax_virhe
		});

	});

	$('#poistaaine').on("click",function(){
		$('#raportti').replaceWith($.parseHTML("<div id='raportti'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		$.ajax({
			async: true,
			url: "deletereseptinaine.py",
			data: {"resepti": $('#resepti').val(), "aineet": $('#aineet').val()},
//      data: {"postinro": $('#postinro').val() },
			processData: true,
			dataType: "text",
			type: "GET",
			success: aineentaivaiheenpoistoonnistui,
			error: ajax_virhe
		});

	});



	paivitareseptit4();
}

function paivitalisaareseptilleaineetsivu(data, textStatus, request) {
	$('#sisalto').replaceWith($.parseHTML(data));
	//TODO

	$( "#Tallenna" ).on("click",function() {
		$('#raportti').replaceWith($.parseHTML("<div id='raportti'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		var yhtmaara = parseInt($("#Lisaa").val());
		var x = document.getElementsByClassName("aineet");

		var y = document.getElementsByClassName("uudetaineet");
		var vanhataineetlista = []
		var vanhatmaaratlista = [];
		var vanhatyksikotlista = [];

		var id = "";
		for (i = 0; i < x.length; i++) {
			id = "aine" + i.toString();
			vanhataineetlista.push(document.getElementById(id).value);
			id = "maara" + i.toString();
			vanhatmaaratlista.push(document.getElementById(id).value);
			id = "yksikko" + i.toString();
			vanhatyksikotlista.push(document.getElementById(id).value);

		}

		if (x.length > 0) {

		$.ajax({

			async: true,
			url: "editreseptinaineet.py",
			//data: {"Nimi": $('#Nimi').val(), "Kuvaus": $('#Kuvaus').val()},
			data: {
				"resepti": $('#resepti').val(),
				"ainelista": vanhataineetlista,
				"maaralista": vanhatmaaratlista,
				"yksikkolista": vanhatyksikotlista
			},
			//      data: {"postinro": $('#postinro').val() },
			processData: true,
			dataType: "text",
			type: "POST",
			success: vaiheetonnistui,
			error: ajax_virhe

		});

	}

		var uudetaineetlista = []
		var uudetmaaratlista = [];
		var uudetyksikotlista = [];

		var id = "";
		var max = x.length + y.length;
		for (i = x.length; i < max; i++) {
			id = "aine" + i.toString();
			uudetaineetlista.push(document.getElementById(id).value);
			id = "maara" + i.toString();
			uudetmaaratlista.push(document.getElementById(id).value);
			id = "yksikko" + i.toString();
			uudetyksikotlista.push(document.getElementById(id).value);

		}

		if (y.length > 0) {
			$.ajax({
				async: true,
				url: "addreseptinaineet.py",
				//data: {"Nimi": $('#Nimi').val(), "Kuvaus": $('#Kuvaus').val()},
				data: {
					"resepti": $('#resepti').val(),
					"ainelista": uudetaineetlista,
					"maaralista": uudetmaaratlista,
					"yksikkolista": uudetyksikotlista
				},
				//      data: {"postinro": $('#postinro').val() },
				processData: true,
				dataType: "text",
				type: "POST",
				success: vaiheetonnistui,
				error: ajax_virhe
			});
		}
		else {
			$('#raportti').replaceWith($.parseHTML("<h3 id='raportti'>Lisäys onnistui!</h3>" ));
		}
	});
	paivitareseptit2();
}
	
function paivitalisaaruokaainesivu(data, textStatus, request) {
	$('#sisalto').replaceWith($.parseHTML(data));
	$('#ajax13').replaceWith($.parseHTML("" ));

	paivitalista();
	$('#lisaaruokaaine').on("click",function(){
		$('#lataus').replaceWith($.parseHTML("<div id='lataus'></div><div id='ajax12'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		$.ajax({
        async: true,
        url: "addruokaaine.py",
        data: {"Nimi": $('#Nimi').val(), "Kuvaus": $('#Kuvaus').val()},
//      data: {"postinro": $('#postinro').val() },
        processData: true,
        dataType: "text",
        type: "GET",
        success: ruokaainemuutosonnistui,
        error: ajax_virhe
});
	});

}

function ruokaainemuutosonnistui(data, textStatus, request) {
	$('#ajax12').replaceWith($.parseHTML("" ));

	$('#raportti').replaceWith($.parseHTML(data));
}

function vaiheetonnistui(data, textStatus, request) {
	$('#raportti').replaceWith($.parseHTML(data));
}

function ruokalajimuutosonnistui(data, textStatus, request) {
	$('#raportti').replaceWith($.parseHTML(data));
	paivitavalikko();
}

function aineentaivaiheenpoistoonnistui(data, textStatus, request) {
	$('#raportti').replaceWith($.parseHTML(data));
	paivitareseptit4();
}



		
function paivitamuokkaareseptiasivu(data, textStatus, request) {
	$('#sisalto').replaceWith($.parseHTML(data));
	paivitareseptit5();
}
	
		
function paivitalisaareseptinvaiheetsivu(data, textStatus, request) {
	$('#sisalto').replaceWith($.parseHTML(data));


	$( "#Tallenna" ).on("click",function() {
		$('#raportti').replaceWith($.parseHTML("<div id='raportti'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		var yhtmaara = parseInt($("#Lisaa").val());
		var x = document.getElementsByClassName("vanhatvaiheet");

		var y = document.getElementsByClassName("uvaiheet");
		var vanhatvaiheetlista = []

		var id = "";
		for (i = 0; i < x.length; i++) {
			id = "vaihe" + i.toString();
			vanhatvaiheetlista.push(document.getElementById(id).value);
		}

		if (x.length > 0) {

			$.ajax({

				async: true,
				url: "editvaihe.py",
				data: {
					"resepti": $('#resepti').val(),
					"vaihelista": vanhatvaiheetlista
				},
				processData: true,
				dataType: "text",
				type: "POST",
				success: vaiheetonnistui,
				error: ajax_virhe

			});

		}

		var uudetvaiheetlista = [];

		var id = "";
		var max = x.length + y.length;
		for (i = x.length; i < max; i++) {
			id = "vaihe" + i.toString();
			uudetvaiheetlista.push(document.getElementById(id).value);

		}

		if (y.length > 0) {

			$.ajax({

				async: true,
				url: "addvaihe.py",
				//data: {"Nimi": $('#Nimi').val(), "Kuvaus": $('#Kuvaus').val()},
				data: {
					"vaiheita": x.length.toString(),
					"resepti": $('#resepti').val(),
					"vaihelista": uudetvaiheetlista
				},
				//      data: {"postinro": $('#postinro').val() },
				processData: true,
				dataType: "text",
				type: "POST",
				success: vaiheetonnistui,
				error: ajax_virhe

			});

		}






	});


	paivitareseptit3();
}
	
function paivitalisaapoistaruokalajisivu(data, textStatus, request) {
	$('#sisalto').replaceWith($.parseHTML(data));
	paivitalista();
	



	
	$('#lisaaruokalaji').on("click",function(){
		$('#raportti').replaceWith($.parseHTML("<div id='raportti'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		$.ajax({
        async: true,
        url: "addruokalaji.py",
        data: {"Nimi": $('#Nimi').val(), "Kuvaus": $('#Kuvaus').val()},
//      data: {"postinro": $('#postinro').val() },
        processData: true,
        dataType: "text",
        type: "GET",
        success: ruokalajimuutosonnistui,
        error: ajax_virhe
});

	});
	
    $('#poistaruokalaji').on("click",function(){
		$('#raportti').replaceWith($.parseHTML("<div id='raportti'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

	$.ajax({
        async: true,
        url: "deleteruokalaji.py",
        data: { "ruokalaji": $('#ruokalaji').val()},
//      data: {"postinro": $('#postinro').val() },
        processData: true,
        dataType: "text",
        type: "GET",
        success: ruokalajimuutosonnistui,
        error: ajax_virhe
});

	});




	}
	
		
function paivitaetusivu(data, textStatus, request) {
	$('#sisalto').replaceWith($.parseHTML(data));
	paivitalista();
	//TODO: L?heta-nappi

	$( ".kentta" ).on("change",function(){
		if ( $(this).val() !=null){

			if ( $(this).val().length < 3){

				tulivirhe(this);
			}

			else {
				var id = $(this).attr("id");
				$( "#" + id + "p" ).text("");
			}


			//tarkistaKaikki();
		}
		else {
			tulivirhe(this);
		}

	});

	$( "#Laheta" ).on("click",function(){

		var virhe = false;

		if( $( "#" + "Nimi" ).val()  == null){
			virhe = true;

		}
		else {
			if ( $( "#" + "Nimi" ).val().length < 3)
				virhe = true;
		}


		if( $( "#" + "Kuvaus" ).val()  == null){
			virhe = true;

		}
		else {
			if ( $( "#" + "Kuvaus" ).val().length < 3)
				virhe = true;
		}

		if( $( "#" + "henmaara" ).val()  == null){
			virhe = true;

		}
		else {
			if ( $( "#" + "henmaara" ).val().length < 1)
				virhe = true;
		}


		if (virhe == false) {
			$('#raportti').replaceWith($.parseHTML("<div id='raportti'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

			$.ajax({

				async: true,
				url: "lisays.py",
				data:  {"Nimi": $('#Nimi').val(),  "Kuvaus": $('#Kuvaus').val(), "henmaara": $('#henmaara').val(), "ruokalaji": $('#ruokalaji').val()},
//      data: {"postinro": $('#postinro').val() },
				processData: true,
				dataType: "text",
				type: "POST",
				success: lisatty,
				error: ajax_virhe
			});





		} else {
			$('#raportti').replaceWith($.parseHTML("<h3>Ei lisätty!</h3>" ));

		}


	});

}

function lisatty(kentta) {
	$('#ajax3').replaceWith($.parseHTML("" ));

	$('#raportti').replaceWith($.parseHTML("<h3 id='raportti'>Lisäys onnistui!</h3>" ));

	paivitalista();
	
	var u = 0;
}

function tulivirhe(kentta) {

	var id = $(kentta).attr("id");
	$( "#" + id + "p" ).text("virhe");
}

function paivitalista() {
		//$('#raportti').replaceWith($.parseHTML("<div id='raportti'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		$.ajax({
        async: true,
        url: "avustaja.py",
        data: $('getreseptit'),
//      data: {"postinro": $('#postinro').val() },
        processData: true,
        dataType: "text",
        type: "GET",
        success: alusta,
        error: ajax_virhe
});
	
}


function paivitareseptit() {
	$('#lataus').replaceWith($.parseHTML("<div id='lataus'></div><div id='ajax6'><img src='19-0.gif' alt='loaderimg' /></div>" ));

	$.ajax({
		async: true,
		url: "getreseptilista.py",
		data: $('getresepti'),
//      data: {"postinro": $('#postinro').val() },
		processData: true,
		dataType: "text",
		type: "GET",
		success: paivitareseptilista,
		error: ajax_virhe
	});

}

function paivitareseptit4() {
	$('#lataus').replaceWith($.parseHTML("<div id='lataus'></div><div id='ajax7'><img src='19-0.gif' alt='loaderimg' /></div>" ));

	$.ajax({
		async: true,
		url: "getreseptilista.py",
		data: $('getresepti'),
//      data: {"postinro": $('#postinro').val() },
		processData: true,
		dataType: "text",
		type: "GET",
		success: paivitareseptilista4,
		error: ajax_virhe
	});

}

function paivitareseptit5() {
	$('#lataus').replaceWith($.parseHTML("<div id='lataus'></div><div id='ajax8'><img src='19-0.gif' alt='loaderimg' /></div>" ));

	$.ajax({
		async: true,
		url: "getreseptilista.py",
		data: $('getresepti'),
//      data: {"postinro": $('#postinro').val() },
		processData: true,
		dataType: "text",
		type: "GET",
		success: paivitareseptilista5,
		error: ajax_virhe
	});

}

function paivitareseptit3() {
	$('#lataus').replaceWith($.parseHTML("<div id='lataus'></div><div id='ajax9'><img src='19-0.gif' alt='loaderimg' /></div>" ));

	$.ajax({
		async: true,
		url: "getreseptilista.py",
		data: $('getresepti'),
//      data: {"postinro": $('#postinro').val() },
		processData: true,
		dataType: "text",
		type: "GET",
		success: paivitareseptilista3,
		error: ajax_virhe
	});

}

function paivitareseptilista(data, textStatus, request) {
	$('#ajax6').replaceWith($.parseHTML("" ));

	$('#resepti').replaceWith($.parseHTML(data));
}

function paivitareseptit2() {
	$('#reseptinaineet').replaceWith($.parseHTML("<div id='reseptinaineet'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

	
	$.ajax({
		async: true,
		url: "getreseptilista.py",
		data: $('getresepti'),
//      data: {"postinro": $('#postinro').val() },
		processData: true,
		dataType: "text",
		type: "GET",
		success: paivitareseptilista2,
		error: ajax_virhe
	});

}

function paivitareseptilista2(data, textStatus, request) {
	$('#resepti').replaceWith($.parseHTML(data));
	$( '#resepti' ).on("change",function(){
		$('#reseptinaineet').replaceWith($.parseHTML("<div id='reseptinaineet'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		$.ajax({
        async: true,
        url: "getreseptinaineet.py",
        data:  {"resepti": $('#resepti').val()},
//      data: {"postinro": $('#postinro').val() },
        processData: true,
        dataType: "text",
        type: "POST",
        success: paivitaaineet,
        error: ajax_virhe
});
		});
		$('#lataus').replaceWith($.parseHTML("<div id='lataus'></div><div id='ajax10'><img src='19-0.gif' alt='loaderimg' /></div>" ));

		$.ajax({
        async: true,
        url: "getreseptinaineet.py",
        data:  {"resepti": $('#resepti').val()},
//      data: {"postinro": $('#postinro').val() },
        processData: true,
        dataType: "text",
        type: "POST",
        success: paivitaaineet,
        error: ajax_virhe
});

}


function paivitareseptilista5(data, textStatus, request) {
	$('#ajax8').replaceWith($.parseHTML("" ));

	$('#resepti').replaceWith($.parseHTML(data));
	$( '#resepti' ).on("change",function(){
		$.ajax({
			async: true,
			url: "getmuokattavaresepti.py",
			data:  {"resepti": $('#resepti').val()},
//      data: {"postinro": $('#postinro').val() },
			processData: true,
			dataType: "text",
			type: "POST",
			success: paivitareseptimuuokkaus,
			error: ajax_virhe
		});
	});


	$( "#Poista" ).on("click",function(){
		$('#raportti').replaceWith($.parseHTML("<div id='raportti'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));

		$.ajax({
			async: true,
			url: "deleteresepti.py",
			data:  {"ReseptiID": $('#resepti').val()},
//      data: {"postinro": $('#postinro').val() },
			processData: true,
			dataType: "text",
			type: "POST",
			success: reseptinmuokkausonnistui(),
			error: ajax_virhe

		});
	});


	$.ajax({
			async: true,
			url: "getmuokattavaresepti.py",
			data:  {"resepti": $('#resepti').val()},
//      data: {"postinro": $('#postinro').val() },
			processData: true,
			dataType: "text",
			type: "POST",
			success: paivitareseptimuuokkaus,
			error: ajax_virhe
		});

}

function paivitareseptilista3(data, textStatus, request) {
	$('#ajax9').replaceWith($.parseHTML("" ));

	$('#resepti').replaceWith($.parseHTML(data));
	$( '#resepti' ).on("change",function(){
		$.ajax({
        async: true,
        url: "getreseptinvaiheet.py",
        data:  {"resepti": $('#resepti').val()},
//      data: {"postinro": $('#postinro').val() },
        processData: true,
        dataType: "text",
        type: "POST",
        success: paivitavaiheet,
        error: ajax_virhe
});
		});
		




		
		$.ajax({
        async: true,
        url: "getreseptinvaiheet.py",
        data:  {"resepti": $('#resepti').val()},
//      data: {"postinro": $('#postinro').val() },
        processData: true,
        dataType: "text",
        type: "POST",
        success: paivitavaiheet,
        error: ajax_virhe
});

}

function paivitareseptilista4(data, textStatus, request) {
	$('#ajax7').replaceWith($.parseHTML("" ));

	$('#resepti').replaceWith($.parseHTML(data));
	if (muutosalustettu == false) {
		muutosalustettu = true;
	$( '#resepti' ).on("change",function(){
		$.ajax({
        async: true,
        url: "getvaihelista.py",
        data:  {"resepti": $('#resepti').val()},
//      data: {"postinro": $('#postinro').val() },
        processData: true,
        dataType: "text",
        type: "POST",
        success: paivitavaihelista,
        error: ajax_virhe
});

		$.ajax({
        async: true,
        url: "getreseptinainelista.py",
        data:  {"resepti": $('#resepti').val()},
        processData: true,
        dataType: "text",
        type: "POST",
        success: paivitaainelista,
        error: ajax_virhe
});
		});
	}
		
				$.ajax({
        async: true,
        url: "getvaihelista.py",
        data:  {"resepti": $('#resepti').val()},
//      data: {"postinro": $('#postinro').val() },
        processData: true,
        dataType: "text",
        type: "POST",
        success: paivitavaihelista,
        error: ajax_virhe
});

		$.ajax({
        async: true,
        url: "getreseptinainelista.py",
        data:  {"resepti": $('#resepti').val()},
        processData: true,
        dataType: "text",
        type: "POST",
        success: paivitaainelista,
        error: ajax_virhe
});


}

function paivitavaihelista(data, textStatus, request) {
	$('#vaihep').replaceWith($.parseHTML(data));
}
function paivitaainelista(data, textStatus, request) {
	$('#ainep').replaceWith($.parseHTML(data));
	//paivitapoistareseptiainetaivaihesivu();
}

function paivitareseptimuuokkaus(data, textStatus, request) {
	$('#muokkauskentat').replaceWith($.parseHTML(data));
	if (reseptinmuokkausalustettu == true) return;
	reseptinmuokkausalustettu = true;
	$("#Muokkaa").on("click", function () {
		$.ajax({
			async: true,
			url: "editresepti.py",
			data: {
				"resepti": $('#resepti').val(),
				"Nimi": $('#Nimi').val(),
				"Kuvaus": $('#Kuvaus').val(),
				"Henkilomaara": $('#Henkilomaara').val(),
				"Ruokalaji": $('#ruokalaji').val()
			},
//      data: {"postinro": $('#postinro').val() },
			processData: true,
			dataType: "text",
			type: "POST",
			success: reseptinmuokkausonnistui,
			error: ajax_virhe

		});
	});
}
function reseptinmuokkausonnistui(data, textStatus, request) {
	$('#raportti').replaceWith($.parseHTML(data));

	$( '#resepti' ).on("change",function(){
		$.ajax({
			async: true,
			url: "getmuokattavaresepti.py",
			data:  {"resepti": $('#resepti').val()},
//      data: {"postinro": $('#postinro').val() },
			processData: true,
			dataType: "text",
			type: "POST",
			success: paivitareseptimuuokkaus,
			error: ajax_virhe
		});
	});

}


function paivitavaiheet(data, textStatus, request) {
	$('#vaiheet').replaceWith($.parseHTML(data));
	var x = document.getElementsByClassName("vanhatvaiheet");
	var maara = x.length;
	$('#Lisaa').val( maara.toString() )
	if (vaihelisaysalustettu == true) return;
	vaihelisaysalustettu = true;
	$( "#Lisaa" ).on("click",function(){
		$('#uudetvaiheet').replaceWith($.parseHTML("<div id='uudetvaiheet'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));
		$.ajax({
			async: true,
			url: "getuusivaihe.py",
			data:  {"Lisaa": $('#Lisaa').val()},
//      data: {"postinro": $('#postinro').val() },
			processData: true,
			dataType: "text",
			type: "POST",
			success: lisaavaihe,
			error: ajax_virhe

		});
	});
}

function paivitaaineet(data, textStatus, request) {
	$('#ajax10').replaceWith($.parseHTML("" ));

	$('#reseptinaineet').replaceWith($.parseHTML(data));
	var x = document.getElementsByClassName("aineet");
	var maara = x.length;
	$('#Lisaavaihe').val( maara.toString() )
	if (ainelisaysalustettu == true) return;
	ainelisaysalustettu = true;

	$( "#Lisaavaihe" ).on("click",function(){
		$('#lisaaineet').replaceWith($.parseHTML("<div id='lisaaineet'><img src='ajax-loader2.gif' alt='loaderimg' /></div>" ));
		$.ajax({
			async: true,
			url: "getainelista.py",
			data:  {"Lisaavaihe": $('#Lisaavaihe').val()},
//      data: {"postinro": $('#postinro').val() },
			processData: true,
			dataType: "text",
			type: "POST",
			success: lisaaaine,
			error: ajax_virhe

		});
	});
}

function lisaavaihe(data, textStatus, request) {
	$('#uudetvaiheet').replaceWith($.parseHTML(data));
	var x = document.getElementsByClassName("vanhatvaiheet");
	var maara1 = x.length;
	var y = document.getElementsByClassName("uvaiheet");
	var maara2 = y.length;
	var maara = maara1 + maara2
	$('#Lisaa').val( maara.toString() )

}
function lisaaaine(data, textStatus, request) {
	$('#lisaaineet').replaceWith($.parseHTML(data));
	var x = document.getElementsByClassName("aineet");
	var maara1 = x.length;
	var y = document.getElementsByClassName("uudetaineet");
	var maara2 = y.length;
	var maara = maara1 + maara2
	$('#Lisaavaihe').val( maara.toString() )

}



function paivitavalikko() {
		$('#lataus').replaceWith($.parseHTML("<div id='lataus'></div><div id='ajax11'><img src='19-0.gif' alt='loaderimg' /></div>" ));

		$.ajax({
        async: true,
        url: "getlista.py",
        data: $('getlist'),
//      data: {"postinro": $('#postinro').val() },
        processData: true,
        dataType: "text",
        type: "GET",
        success: valusta,
        error: ajax_virhe
});
	
}



function alusta(data, textStatus, request) {
	paivitavalikko();
    $('#lista').replaceWith($.parseHTML(data));

	var i = 0;
}


function valusta(data, textStatus, request) {
	$('#ajax11').replaceWith($.parseHTML("" ));

    $('#ruokalaji').replaceWith($.parseHTML(data));
	var i = 0;
}


function ajax_virhe(event, jqxhr, settings, exception) {
	
	 console.log( exception );
}
