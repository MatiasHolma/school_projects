﻿var bigcount = 0;
var facecount = 0;
var queuecount = 0;




window.onload = function() {



    main = document.getElementById('main');
    var txt=document.createElement('textarea');
    txt.setAttribute('rows','50');
    txt.setAttribute('cols','100');
    txt.setAttribute('id','json');
    txt.setAttribute('name', 'json');
    main.appendChild(txt);

    var txt2=document.createElement('textarea');
    txt2.setAttribute('rows','50');
    txt2.setAttribute('cols','100');
    txt2.setAttribute('id','json');
    txt2.setAttribute('name', 'json');
    main.appendChild(txt2);




    $.ajax({url: "barbers.json", success: function(jsonString){
        json = JSON.parse(jsonString);
        var list=[];
        var citylist=[];
        var cityent={};
       
  	   likes =  { "Oulu": 1078, "Hämeenlinna": 446, "Jyväskylä": 1211, "Turku": 5, "Espoo": 326, "Tampere": 911, "Rovaniemi": 774, "Helsinki": 1062, "Pori": 379, "Lahti": 301 }
        cityname = { "area005": "Alajärvi", "area009": "Alavieska", "area010": "Alavus", "area016": "Asikkala", "area018": "Askola", "area019": "Aura", "area020": "Akaa", "area035": "Brändö", "area043": "Eckerö", "area046": "Enonkoski", "area047": "Enontekiö", "area049": "Espoo", "area050": "Eura", "area051": "Eurajoki", "area052": "Evijärvi", "area060": "Finström", "area061": "Forssa", "area062": "Föglö", "area065": "Geta", "area069": "Haapajärvi", "area071": "Haapavesi", "area072": "Hailuoto", "area074": "Halsua", "area075": "Hamina", "area076": "Hammarland", "area077": "Hankasalmi", "area078": "Hanko", "area079": "Harjavalta", "area081": "Hartola", "area082": "Hattula", "area086": "Hausjärvi", "area090": "Heinävesi", "area091": "Helsinki", "area092": "Vantaa", "area097": "Hirvensalmi", "area098": "Hollola", "area099": "Honkajoki", "area102": "Huittinen", "area103": "Humppila", "area105": "Hyrynsalmi", "area106": "Hyvinkää", "area108": "Hämeenkyrö", "area109": "Hämeenlinna", "area111": "Heinola", "area139": "Ii", "area140": "Iisalmi", "area142": "Iitti", "area143": "Ikaalinen", "area145": "Ilmajoki", "area146": "Ilomantsi", "area148": "Inari", "area149": "Inkoo", "area151": "Isojoki", "area152": "Isokyrö", "area153": "Imatra", "area164": "Jalasjärvi", "area165": "Janakkala", "area167": "Joensuu", "area169": "Jokioinen", "area170": "Jomala", "area171": "Joroinen", "area172": "Joutsa", "area174": "Juankoski", "area176": "Juuka", "area177": "Juupajoki", "area178": "Juva", "area179": "Jyväskylä", "area181": "Jämijärvi", "area182": "Jämsä", "area186": "Järvenpää", "area202": "Kaarina", "area204": "Kaavi", "area205": "Kajaani", "area208": "Kalajoki", "area211": "Kangasala", "area213": "Kangasniemi", "area214": "Kankaanpää", "area216": "Kannonkoski", "area217": "Kannus", "area218": "Karijoki", "area224": "Karkkila", "area226": "Karstula", "area230": "Karvia", "area231": "Kaskinen", "area232": "Kauhajoki", "area233": "Kauhava", "area235": "Kauniainen", "area236": "Kaustinen", "area239": "Keitele", "area240": "Kemi", "area241": "Keminmaa", "area244": "Kempele", "area245": "Kerava", "area249": "Keuruu", "area250": "Kihniö", "area256": "Kinnula", "area257": "Kirkkonummi", "area260": "Kitee", "area261": "Kittilä", "area263": "Kiuruvesi", "area265": "Kivijärvi", "area271": "Kokemäki", "area272": "Kokkola", "area273": "Kolari", "area275": "Konnevesi", "area276": "Kontiolahti", "area280": "Korsnäs", "area283": "Hämeenkoski", "area284": "Koski Tl", "area285": "Kotka", "area286": "Kouvola", "area287": "Kristiinankaupunki", "area288": "Kruunupyy", "area290": "Kuhmo", "area291": "Kuhmoinen", "area295": "Kumlinge", "area297": "Kuopio", "area300": "Kuortane", "area301": "Kurikka", "area304": "Kustavi", "area305": "Kuusamo", "area309": "Outokumpu", "area312": "Kyyjärvi", "area316": "Kärkölä", "area317": "Kärsämäki", "area318": "Kökar", "area319": "Köyliö", "area320": "Kemijärvi", "area322": "Kemiönsaari", "area398": "Lahti", "area399": "Laihia", "area400": "Laitila", "area402": "Lapinlahti", "area403": "Lappajärvi", "area405": "Lappeenranta", "area407": "Lapinjärvi", "area408": "Lapua", "area410": "Laukaa", "area413": "Lavia", "area416": "Lemi", "area417": "Lemland", "area418": "Lempäälä", "area420": "Leppävirta", "area421": "Lestijärvi", "area422": "Lieksa", "area423": "Lieto", "area425": "Liminka", "area426": "Liperi", "area430": "Loimaa", "area433": "Loppi", "area434": "Loviisa", "area435": "Luhanka", "area436": "Lumijoki", "area438": "Lumparland", "area440": "Luoto", "area441": "Luumäki", "area442": "Luvia", "area444": "Lohja", "area445": "Parainen", "area475": "Maalahti", "area476": "Maaninka", "area478": "Maarianhamina", "area480": "Marttila", "area481": "Masku", "area483": "Merijärvi", "area484": "Merikarvia", "area489": "Miehikkälä", "area491": "Mikkeli", "area494": "Muhos", "area495": "Multia", "area498": "Muonio", "area499": "Mustasaari", "area500": "Muurame", "area503": "Mynämäki", "area504": "Myrskylä", "area505": "Mäntsälä", "area507": "Mäntyharju", "area508": "Mänttä-Vilppula", "area529": "Naantali", "area531": "Nakkila", "area532": "Nastola", "area535": "Nivala", "area536": "Nokia", "area538": "Nousiainen", "area541": "Nurmes", "area543": "Nurmijärvi", "area545": "Närpiö", "area560": "Orimattila", "area561": "Oripää", "area562": "Orivesi", "area563": "Oulainen", "area564": "Oulu", "area576": "Padasjoki", "area577": "Paimio", "area578": "Paltamo", "area580": "Parikkala", "area581": "Parkano", "area583": "Pelkosenniemi", "area584": "Perho", "area588": "Pertunmaa", "area592": "Petäjävesi", "area593": "Pieksämäki", "area595": "Pielavesi", "area598": "Pietarsaari", "area599": "Pedersören kunta", "area601": "Pihtipudas", "area604": "Pirkkala", "area607": "Polvijärvi", "area608": "Pomarkku", "area609": "Pori", "area611": "Pornainen", "area614": "Posio", "area615": "Pudasjärvi", "area616": "Pukkila", "area619": "Punkalaidun", "area620": "Puolanka", "area623": "Puumala", "area624": "Pyhtää", "area625": "Pyhäjoki", "area626": "Pyhäjärvi", "area630": "Pyhäntä", "area631": "Pyhäranta", "area635": "Pälkäne", "area636": "Pöytyä", "area638": "Porvoo", "area678": "Raahe", "area680": "Raisio", "area681": "Rantasalmi", "area683": "Ranua", "area684": "Rauma", "area686": "Rautalampi", "area687": "Rautavaara", "area689": "Rautjärvi", "area691": "Reisjärvi", "area694": "Riihimäki", "area697": "Ristijärvi", "area698": "Rovaniemi", "area700": "Ruokolahti", "area702": "Ruovesi", "area704": "Rusko", "area707": "Rääkkylä", "area710": "Raasepori", "area729": "Saarijärvi", "area732": "Salla", "area734": "Salo", "area736": "Saltvik", "area738": "Sauvo", "area739": "Savitaipale", "area740": "Savonlinna", "area742": "Savukoski", "area743": "Seinäjoki", "area746": "Sievi", "area747": "Siikainen", "area748": "Siikajoki", "area749": "Siilinjärvi", "area751": "Simo", "area753": "Sipoo", "area755": "Siuntio", "area758": "Sodankylä", "area759": "Soini", "area761": "Somero", "area762": "Sonkajärvi", "area765": "Sotkamo", "area766": "Sottunga", "area768": "Sulkava", "area771": "Sund", "area777": "Suomussalmi", "area778": "Suonenjoki", "area781": "Sysmä", "area783": "Säkylä", "area785": "Vaala", "area790": "Sastamala", "area791": "Siikalatva", "area831": "Taipalsaari", "area832": "Taivalkoski", "area833": "Taivassalo", "area834": "Tammela", "area837": "Tampere", "area838": "Tarvasjoki", "area844": "Tervo", "area845": "Tervola", "area846": "Teuva", "area848": "Tohmajärvi", "area849": "Toholampi", "area850": "Toivakka", "area851": "Tornio", "area853": "Turku", "area854": "Pello", "area857": "Tuusniemi", "area858": "Tuusula", "area859": "Tyrnävä", "area886": "Ulvila", "area887": "Urjala", "area889": "Utajärvi", "area890": "Utsjoki", "area892": "Uurainen", "area893": "Uusikaarlepyy", "area895": "Uusikaupunki", "area905": "Vaasa", "area908": "Valkeakoski", "area911": "Valtimo", "area915": "Varkaus", "area918": "Vehmaa", "area921": "Vesanto", "area922": "Vesilahti", "area924": "Veteli", "area925": "Vieremä", "area927": "Vihti", "area931": "Viitasaari", "area934": "Vimpeli", "area935": "Virolahti", "area936": "Virrat", "area941": "Vårdö", "area946": "Vöyri", "area976": "Ylitornio", "area977": "Ylivieska", "area980": "Ylöjärvi", "area981": "Ypäjä", "area989": "Ähtäri", "area992": "Äänekoski" }
        citypopulation= {"area738": 3033.0, "area935": 3487.0, "area211": 30126.0, "area781": 4178.0, "area263": 8989.0, "area785": 3250.0, "area700": 5577.0, "area702": 4868.0, "area178": 6783.0, "area707": 2490.0, "area139": 9574.0, "area689": 3784.0, "area545": 9380.0, "area261": 6388.0, "area543": 40719.0, "area541": 8308.0, "area226": 4376.0, "area421": 835.0, "area035": 476.0, "area423": 17023.0, "area425": 9432.0, "area426": 12397.0, "area694": 29215.0, "area989": 6363.0, "area561": 1434.0, "area257": 37567.0, "area265": 1303.0, "area924": 3382.0, "area611": 5137.0, "area981": 2509.0, "area980": 31515.0, "area905": 65674.0, "area593": 19407.0, "area638": 49028.0, "area635": 6838.0, "area925": 3930.0, "area636": 8569.0, "area631": 2199.0, "area170": 4355.0, "area616": 2047.0, "area143": 7346.0, "area142": 6955.0, "area417": 1883.0, "area078": 9267.0, "area309": 7343.0, "area146": 5693.0, "area145": 12022.0, "area854": 3819.0, "area305": 16167.0, "area304": 889.0, "area149": 5538.0, "area148": 6732.0, "area301": 14395.0, "area300": 3849.0, "area704": 5907.0, "area598": 19680.0, "area753": 18739.0, "area250": 2147.0, "area020": 17134.0, "area256": 1764.0, "area790": 25747.0, "area791": 5983.0, "area400": 8460.0, "area857": 2795.0, "area751": 3429.0, "area851": 22489.0, "area850": 2455.0, "area853": 180225.0, "area859": 6613.0, "area783": 4631.0, "area992": 20265.0, "area915": 22340.0, "area508": 11122.0, "area911": 2421.0, "area420": 10274.0, "area403": 3383.0, "area623": 2374.0, "area620": 2931.0, "area684": 39842.0, "area626": 5849.0, "area893": 7531.0, "area624": 5377.0, "area625": 3311.0, "area402": 10289.0, "area151": 2290.0, "area152": 4886.0, "area153": 28294.0, "area407": 2829.0, "area405": 72424.0, "area312": 1469.0, "area408": 14650.0, "area316": 4772.0, "area317": 2760.0, "area858": 37936.0, "area019": 3971.0, "area018": 4988.0, "area563": 7847.0, "area320": 8093.0, "area564": 190847.0, "area318": 245.0, "area240": 22257.0, "area010": 12341.0, "area260": 11341.0, "area399": 7993.0, "area244": 16383.0, "area224": 9119.0, "area016": 8461.0, "area091": 603968.0, "area090": 3742.0, "area092": 205312.0, "area846": 5767.0, "area922": 4437.0, "area097": 2377.0, "area845": 3339.0, "area099": 1832.0, "area098": 22054.0, "area848": 4897.0, "area849": 3426.0, "area921": 2328.0, "area734": 54858.0, "area422": 12399.0, "area580": 5591.0, "area499": 19012.0, "area498": 2394.0, "area710": 28829.0, "area495": 1816.0, "area494": 8948.0, "area491": 54519.0, "area736": 1823.0, "area927": 28674.0, "area275": 2904.0, "area678": 25659.0, "area005": 10268.0, "area169": 5643.0, "area273": 3853.0, "area272": 46773.0, "area165": 16921.0, "area164": 8071.0, "area167": 74168.0, "area759": 2329.0, "area009": 2761.0, "area476": 3826.0, "area475": 5586.0, "area834": 6542.0, "area398": 103016.0, "area576": 3333.0, "area577": 10591.0, "area478": 11345.0, "area746": 5241.0, "area908": 21172.0, "area086": 8866.0, "area918": 2324.0, "area280": 2232.0, "area082": 9720.0, "area081": 3205.0, "area837": 217421.0, "area762": 4493.0, "area761": 9229.0, "area438": 392.0, "area833": 1682.0, "area766": 101.0, "area765": 10682.0, "area936": 7384.0, "area483": 1176.0, "area480": 2017.0, "area481": 9671.0, "area484": 3269.0, "area838": 1959.0, "area072": 986.0, "area071": 7283.0, "area179": 133482.0, "area077": 5453.0, "area076": 1522.0, "area075": 21256.0, "area074": 1248.0, "area172": 4898.0, "area079": 7486.0, "area171": 5291.0, "area176": 5324.0, "area177": 2023.0, "area174": 5093.0, "area433": 8336.0, "area319": 2750.0, "area503": 7978.0, "area500": 9569.0, "area507": 6356.0, "area505": 20478.0, "area504": 1992.0, "area276": 14245.0, "area934": 3205.0, "area771": 1035.0, "area887": 5174.0, "area777": 8813.0, "area778": 7496.0, "area941": 422.0, "area946": 6680.0, "area060": 2531.0, "area061": 17727.0, "area062": 578.0, "area271": 7893.0, "area065": 495.0, "area297": 105136.0, "area069": 7641.0, "area295": 338.0, "area291": 2438.0, "area290": 9240.0, "area217": 5736.0, "area216": 1553.0, "area214": 11957.0, "area213": 5839.0, "area109": 67497.0, "area108": 10500.0, "area106": 45592.0, "area105": 2603.0, "area283": 2096.0, "area103": 2496.0, "area102": 10623.0, "area218": 1514.0, "area186": 39646.0, "area889": 2950.0, "area182": 22354.0, "area181": 1986.0, "area249": 10488.0, "area890": 1285.0, "area529": 18824.0, "area892": 3569.0, "area895": 15499.0, "area630": 1566.0, "area583": 963.0, "area581": 6918.0, "area562": 9571.0, "area749": 21431.0, "area748": 5597.0, "area584": 2923.0, "area747": 1641.0, "area588": 1857.0, "area740": 36584.0, "area743": 59556.0, "area742": 1127.0, "area288": 6666.0, "area977": 14533.0, "area729": 10258.0, "area284": 2450.0, "area285": 54873.0, "area286": 87296.0, "area287": 7055.0, "area051": 5922.0, "area050": 12406.0, "area052": 2686.0, "area204": 3315.0, "area205": 37973.0, "area416": 3059.0, "area140": 22135.0, "area202": 31363.0, "area241": 8585.0, "area680": 24562.0, "area681": 3921.0, "area444": 47516.0, "area445": 15561.0, "area208": 12625.0, "area111": 20051.0, "area440": 4966.0, "area410": 18481.0, "area886": 13470.0, "area683": 4227.0, "area691": 2961.0, "area413": 1916.0, "area686": 3444.0, "area442": 3360.0, "area245": 34491.0, "area592": 4095.0, "area489": 2177.0, "area687": 1813.0, "area595": 4926.0, "area615": 8620.0, "area614": 3738.0, "area560": 16300.0, "area599": 10940.0, "area619": 3203.0, "area441": 5022.0, "area755": 6170.0, "area532": 15082.0, "area322": 7075.0, "area049": 256824.0, "area536": 32354.0, "area739": 3764.0, "area535": 10985.0, "area697": 1450.0, "area043": 960.0, "area538": 4846.0, "area046": 1532.0, "area047": 1880.0, "area732": 3979.0, "area418": 21440.0, "area231": 1382.0, "area230": 2545.0, "area233": 17202.0, "area232": 14167.0, "area235": 8910.0, "area236": 4287.0, "area239": 2476.0, "area430": 16737.0, "area436": 2059.0, "area435": 773.0, "area434": 15519.0, "area578": 3743.0, "area768": 2844.0, "area976": 4556.0, "area844": 1704.0, "area531": 5747.0, "area758": 8834.0, "area601": 4441.0, "area698": 60877.0, "area604": 18128.0, "area607": 4728.0, "area608": 2373.0, "area609": 83285.0, "area931": 6957.0, "area831": 4840.0, "area832": 4313.0};
        for (var prop in citypopulation) {
            cityent[cityname[prop]] = citypopulation[prop];
        }


        for(var i=0;i<json.length;i++)
        {
            var ent={};
            ent.city = json[i]["city"];


            e= json[i]["queue"]["employees"];

            if (json[i]["queue"]["count"] == "full" || json[i]["queue"]["count"] == "closed") {
                var q = 0;
            }
            else {
                q= json[i]["queue"]["count"];
            }


            var ifcity = json[i]["city"];

            if (ifcity == "Tampere" || ifcity == "Jyväskylä" || ifcity == "Rovaniemi" || ifcity == "Lahti" || ifcity == "Espoo" || ifcity == "Helsinki" || ifcity == "Pori" || ifcity == "Hämeenlinna" || ifcity == "Oulu" || ifcity == "Turku") {

				ent.likes = likes[ent.city];
            }
            else {
				ent.likes = 0;
            }
			ent.traffic =e+q;
            ent.population = cityent[json[i]["city"]];
            if (ifcity == "Tampere" || ifcity == "Jyväskylä" || ifcity == "Rovaniemi" || ifcity == "Lahti" || ifcity == "Espoo" || ifcity == "Helsinki" || ifcity == "Pori" || ifcity == "Hämeenlinna" || ifcity == "Oulu" || ifcity == "Turku") {

                list.push(ent);
            }

        }




        results = JSON.stringify(list);
        txt.value = results;


        console.log(list.length);

        ////asgasgöalsghösalhgäas



        json = JSON.parse(jsonString);
        var listt=[];
        var citylist=[];
        var cityent={};
		
		likes = { "Oulu": 1078, "Hämeenlinna": 446, "Jyväskylä": 1211, "Turku": 5, "Espoo": 326, "Tampere": 911, "Rovaniemi": 774, "Helsinki": 1062, "Pori": 379, "Lahti": 301 }
		
        cityname = { "area005": "Alajärvi", "area009": "Alavieska", "area010": "Alavus", "area016": "Asikkala", "area018": "Askola", "area019": "Aura", "area020": "Akaa", "area035": "Brändö", "area043": "Eckerö", "area046": "Enonkoski", "area047": "Enontekiö", "area049": "Espoo", "area050": "Eura", "area051": "Eurajoki", "area052": "Evijärvi", "area060": "Finström", "area061": "Forssa", "area062": "Föglö", "area065": "Geta", "area069": "Haapajärvi", "area071": "Haapavesi", "area072": "Hailuoto", "area074": "Halsua", "area075": "Hamina", "area076": "Hammarland", "area077": "Hankasalmi", "area078": "Hanko", "area079": "Harjavalta", "area081": "Hartola", "area082": "Hattula", "area086": "Hausjärvi", "area090": "Heinävesi", "area091": "Helsinki", "area092": "Vantaa", "area097": "Hirvensalmi", "area098": "Hollola", "area099": "Honkajoki", "area102": "Huittinen", "area103": "Humppila", "area105": "Hyrynsalmi", "area106": "Hyvinkää", "area108": "Hämeenkyrö", "area109": "Hämeenlinna", "area111": "Heinola", "area139": "Ii", "area140": "Iisalmi", "area142": "Iitti", "area143": "Ikaalinen", "area145": "Ilmajoki", "area146": "Ilomantsi", "area148": "Inari", "area149": "Inkoo", "area151": "Isojoki", "area152": "Isokyrö", "area153": "Imatra", "area164": "Jalasjärvi", "area165": "Janakkala", "area167": "Joensuu", "area169": "Jokioinen", "area170": "Jomala", "area171": "Joroinen", "area172": "Joutsa", "area174": "Juankoski", "area176": "Juuka", "area177": "Juupajoki", "area178": "Juva", "area179": "Jyväskylä", "area181": "Jämijärvi", "area182": "Jämsä", "area186": "Järvenpää", "area202": "Kaarina", "area204": "Kaavi", "area205": "Kajaani", "area208": "Kalajoki", "area211": "Kangasala", "area213": "Kangasniemi", "area214": "Kankaanpää", "area216": "Kannonkoski", "area217": "Kannus", "area218": "Karijoki", "area224": "Karkkila", "area226": "Karstula", "area230": "Karvia", "area231": "Kaskinen", "area232": "Kauhajoki", "area233": "Kauhava", "area235": "Kauniainen", "area236": "Kaustinen", "area239": "Keitele", "area240": "Kemi", "area241": "Keminmaa", "area244": "Kempele", "area245": "Kerava", "area249": "Keuruu", "area250": "Kihniö", "area256": "Kinnula", "area257": "Kirkkonummi", "area260": "Kitee", "area261": "Kittilä", "area263": "Kiuruvesi", "area265": "Kivijärvi", "area271": "Kokemäki", "area272": "Kokkola", "area273": "Kolari", "area275": "Konnevesi", "area276": "Kontiolahti", "area280": "Korsnäs", "area283": "Hämeenkoski", "area284": "Koski Tl", "area285": "Kotka", "area286": "Kouvola", "area287": "Kristiinankaupunki", "area288": "Kruunupyy", "area290": "Kuhmo", "area291": "Kuhmoinen", "area295": "Kumlinge", "area297": "Kuopio", "area300": "Kuortane", "area301": "Kurikka", "area304": "Kustavi", "area305": "Kuusamo", "area309": "Outokumpu", "area312": "Kyyjärvi", "area316": "Kärkölä", "area317": "Kärsämäki", "area318": "Kökar", "area319": "Köyliö", "area320": "Kemijärvi", "area322": "Kemiönsaari", "area398": "Lahti", "area399": "Laihia", "area400": "Laitila", "area402": "Lapinlahti", "area403": "Lappajärvi", "area405": "Lappeenranta", "area407": "Lapinjärvi", "area408": "Lapua", "area410": "Laukaa", "area413": "Lavia", "area416": "Lemi", "area417": "Lemland", "area418": "Lempäälä", "area420": "Leppävirta", "area421": "Lestijärvi", "area422": "Lieksa", "area423": "Lieto", "area425": "Liminka", "area426": "Liperi", "area430": "Loimaa", "area433": "Loppi", "area434": "Loviisa", "area435": "Luhanka", "area436": "Lumijoki", "area438": "Lumparland", "area440": "Luoto", "area441": "Luumäki", "area442": "Luvia", "area444": "Lohja", "area445": "Parainen", "area475": "Maalahti", "area476": "Maaninka", "area478": "Maarianhamina", "area480": "Marttila", "area481": "Masku", "area483": "Merijärvi", "area484": "Merikarvia", "area489": "Miehikkälä", "area491": "Mikkeli", "area494": "Muhos", "area495": "Multia", "area498": "Muonio", "area499": "Mustasaari", "area500": "Muurame", "area503": "Mynämäki", "area504": "Myrskylä", "area505": "Mäntsälä", "area507": "Mäntyharju", "area508": "Mänttä-Vilppula", "area529": "Naantali", "area531": "Nakkila", "area532": "Nastola", "area535": "Nivala", "area536": "Nokia", "area538": "Nousiainen", "area541": "Nurmes", "area543": "Nurmijärvi", "area545": "Närpiö", "area560": "Orimattila", "area561": "Oripää", "area562": "Orivesi", "area563": "Oulainen", "area564": "Oulu", "area576": "Padasjoki", "area577": "Paimio", "area578": "Paltamo", "area580": "Parikkala", "area581": "Parkano", "area583": "Pelkosenniemi", "area584": "Perho", "area588": "Pertunmaa", "area592": "Petäjävesi", "area593": "Pieksämäki", "area595": "Pielavesi", "area598": "Pietarsaari", "area599": "Pedersören kunta", "area601": "Pihtipudas", "area604": "Pirkkala", "area607": "Polvijärvi", "area608": "Pomarkku", "area609": "Pori", "area611": "Pornainen", "area614": "Posio", "area615": "Pudasjärvi", "area616": "Pukkila", "area619": "Punkalaidun", "area620": "Puolanka", "area623": "Puumala", "area624": "Pyhtää", "area625": "Pyhäjoki", "area626": "Pyhäjärvi", "area630": "Pyhäntä", "area631": "Pyhäranta", "area635": "Pälkäne", "area636": "Pöytyä", "area638": "Porvoo", "area678": "Raahe", "area680": "Raisio", "area681": "Rantasalmi", "area683": "Ranua", "area684": "Rauma", "area686": "Rautalampi", "area687": "Rautavaara", "area689": "Rautjärvi", "area691": "Reisjärvi", "area694": "Riihimäki", "area697": "Ristijärvi", "area698": "Rovaniemi", "area700": "Ruokolahti", "area702": "Ruovesi", "area704": "Rusko", "area707": "Rääkkylä", "area710": "Raasepori", "area729": "Saarijärvi", "area732": "Salla", "area734": "Salo", "area736": "Saltvik", "area738": "Sauvo", "area739": "Savitaipale", "area740": "Savonlinna", "area742": "Savukoski", "area743": "Seinäjoki", "area746": "Sievi", "area747": "Siikainen", "area748": "Siikajoki", "area749": "Siilinjärvi", "area751": "Simo", "area753": "Sipoo", "area755": "Siuntio", "area758": "Sodankylä", "area759": "Soini", "area761": "Somero", "area762": "Sonkajärvi", "area765": "Sotkamo", "area766": "Sottunga", "area768": "Sulkava", "area771": "Sund", "area777": "Suomussalmi", "area778": "Suonenjoki", "area781": "Sysmä", "area783": "Säkylä", "area785": "Vaala", "area790": "Sastamala", "area791": "Siikalatva", "area831": "Taipalsaari", "area832": "Taivalkoski", "area833": "Taivassalo", "area834": "Tammela", "area837": "Tampere", "area838": "Tarvasjoki", "area844": "Tervo", "area845": "Tervola", "area846": "Teuva", "area848": "Tohmajärvi", "area849": "Toholampi", "area850": "Toivakka", "area851": "Tornio", "area853": "Turku", "area854": "Pello", "area857": "Tuusniemi", "area858": "Tuusula", "area859": "Tyrnävä", "area886": "Ulvila", "area887": "Urjala", "area889": "Utajärvi", "area890": "Utsjoki", "area892": "Uurainen", "area893": "Uusikaarlepyy", "area895": "Uusikaupunki", "area905": "Vaasa", "area908": "Valkeakoski", "area911": "Valtimo", "area915": "Varkaus", "area918": "Vehmaa", "area921": "Vesanto", "area922": "Vesilahti", "area924": "Veteli", "area925": "Vieremä", "area927": "Vihti", "area931": "Viitasaari", "area934": "Vimpeli", "area935": "Virolahti", "area936": "Virrat", "area941": "Vårdö", "area946": "Vöyri", "area976": "Ylitornio", "area977": "Ylivieska", "area980": "Ylöjärvi", "area981": "Ypäjä", "area989": "Ähtäri", "area992": "Äänekoski" }
        citypopulation= {"area738": 3033.0, "area935": 3487.0, "area211": 30126.0, "area781": 4178.0, "area263": 8989.0, "area785": 3250.0, "area700": 5577.0, "area702": 4868.0, "area178": 6783.0, "area707": 2490.0, "area139": 9574.0, "area689": 3784.0, "area545": 9380.0, "area261": 6388.0, "area543": 40719.0, "area541": 8308.0, "area226": 4376.0, "area421": 835.0, "area035": 476.0, "area423": 17023.0, "area425": 9432.0, "area426": 12397.0, "area694": 29215.0, "area989": 6363.0, "area561": 1434.0, "area257": 37567.0, "area265": 1303.0, "area924": 3382.0, "area611": 5137.0, "area981": 2509.0, "area980": 31515.0, "area905": 65674.0, "area593": 19407.0, "area638": 49028.0, "area635": 6838.0, "area925": 3930.0, "area636": 8569.0, "area631": 2199.0, "area170": 4355.0, "area616": 2047.0, "area143": 7346.0, "area142": 6955.0, "area417": 1883.0, "area078": 9267.0, "area309": 7343.0, "area146": 5693.0, "area145": 12022.0, "area854": 3819.0, "area305": 16167.0, "area304": 889.0, "area149": 5538.0, "area148": 6732.0, "area301": 14395.0, "area300": 3849.0, "area704": 5907.0, "area598": 19680.0, "area753": 18739.0, "area250": 2147.0, "area020": 17134.0, "area256": 1764.0, "area790": 25747.0, "area791": 5983.0, "area400": 8460.0, "area857": 2795.0, "area751": 3429.0, "area851": 22489.0, "area850": 2455.0, "area853": 180225.0, "area859": 6613.0, "area783": 4631.0, "area992": 20265.0, "area915": 22340.0, "area508": 11122.0, "area911": 2421.0, "area420": 10274.0, "area403": 3383.0, "area623": 2374.0, "area620": 2931.0, "area684": 39842.0, "area626": 5849.0, "area893": 7531.0, "area624": 5377.0, "area625": 3311.0, "area402": 10289.0, "area151": 2290.0, "area152": 4886.0, "area153": 28294.0, "area407": 2829.0, "area405": 72424.0, "area312": 1469.0, "area408": 14650.0, "area316": 4772.0, "area317": 2760.0, "area858": 37936.0, "area019": 3971.0, "area018": 4988.0, "area563": 7847.0, "area320": 8093.0, "area564": 190847.0, "area318": 245.0, "area240": 22257.0, "area010": 12341.0, "area260": 11341.0, "area399": 7993.0, "area244": 16383.0, "area224": 9119.0, "area016": 8461.0, "area091": 603968.0, "area090": 3742.0, "area092": 205312.0, "area846": 5767.0, "area922": 4437.0, "area097": 2377.0, "area845": 3339.0, "area099": 1832.0, "area098": 22054.0, "area848": 4897.0, "area849": 3426.0, "area921": 2328.0, "area734": 54858.0, "area422": 12399.0, "area580": 5591.0, "area499": 19012.0, "area498": 2394.0, "area710": 28829.0, "area495": 1816.0, "area494": 8948.0, "area491": 54519.0, "area736": 1823.0, "area927": 28674.0, "area275": 2904.0, "area678": 25659.0, "area005": 10268.0, "area169": 5643.0, "area273": 3853.0, "area272": 46773.0, "area165": 16921.0, "area164": 8071.0, "area167": 74168.0, "area759": 2329.0, "area009": 2761.0, "area476": 3826.0, "area475": 5586.0, "area834": 6542.0, "area398": 103016.0, "area576": 3333.0, "area577": 10591.0, "area478": 11345.0, "area746": 5241.0, "area908": 21172.0, "area086": 8866.0, "area918": 2324.0, "area280": 2232.0, "area082": 9720.0, "area081": 3205.0, "area837": 217421.0, "area762": 4493.0, "area761": 9229.0, "area438": 392.0, "area833": 1682.0, "area766": 101.0, "area765": 10682.0, "area936": 7384.0, "area483": 1176.0, "area480": 2017.0, "area481": 9671.0, "area484": 3269.0, "area838": 1959.0, "area072": 986.0, "area071": 7283.0, "area179": 133482.0, "area077": 5453.0, "area076": 1522.0, "area075": 21256.0, "area074": 1248.0, "area172": 4898.0, "area079": 7486.0, "area171": 5291.0, "area176": 5324.0, "area177": 2023.0, "area174": 5093.0, "area433": 8336.0, "area319": 2750.0, "area503": 7978.0, "area500": 9569.0, "area507": 6356.0, "area505": 20478.0, "area504": 1992.0, "area276": 14245.0, "area934": 3205.0, "area771": 1035.0, "area887": 5174.0, "area777": 8813.0, "area778": 7496.0, "area941": 422.0, "area946": 6680.0, "area060": 2531.0, "area061": 17727.0, "area062": 578.0, "area271": 7893.0, "area065": 495.0, "area297": 105136.0, "area069": 7641.0, "area295": 338.0, "area291": 2438.0, "area290": 9240.0, "area217": 5736.0, "area216": 1553.0, "area214": 11957.0, "area213": 5839.0, "area109": 67497.0, "area108": 10500.0, "area106": 45592.0, "area105": 2603.0, "area283": 2096.0, "area103": 2496.0, "area102": 10623.0, "area218": 1514.0, "area186": 39646.0, "area889": 2950.0, "area182": 22354.0, "area181": 1986.0, "area249": 10488.0, "area890": 1285.0, "area529": 18824.0, "area892": 3569.0, "area895": 15499.0, "area630": 1566.0, "area583": 963.0, "area581": 6918.0, "area562": 9571.0, "area749": 21431.0, "area748": 5597.0, "area584": 2923.0, "area747": 1641.0, "area588": 1857.0, "area740": 36584.0, "area743": 59556.0, "area742": 1127.0, "area288": 6666.0, "area977": 14533.0, "area729": 10258.0, "area284": 2450.0, "area285": 54873.0, "area286": 87296.0, "area287": 7055.0, "area051": 5922.0, "area050": 12406.0, "area052": 2686.0, "area204": 3315.0, "area205": 37973.0, "area416": 3059.0, "area140": 22135.0, "area202": 31363.0, "area241": 8585.0, "area680": 24562.0, "area681": 3921.0, "area444": 47516.0, "area445": 15561.0, "area208": 12625.0, "area111": 20051.0, "area440": 4966.0, "area410": 18481.0, "area886": 13470.0, "area683": 4227.0, "area691": 2961.0, "area413": 1916.0, "area686": 3444.0, "area442": 3360.0, "area245": 34491.0, "area592": 4095.0, "area489": 2177.0, "area687": 1813.0, "area595": 4926.0, "area615": 8620.0, "area614": 3738.0, "area560": 16300.0, "area599": 10940.0, "area619": 3203.0, "area441": 5022.0, "area755": 6170.0, "area532": 15082.0, "area322": 7075.0, "area049": 256824.0, "area536": 32354.0, "area739": 3764.0, "area535": 10985.0, "area697": 1450.0, "area043": 960.0, "area538": 4846.0, "area046": 1532.0, "area047": 1880.0, "area732": 3979.0, "area418": 21440.0, "area231": 1382.0, "area230": 2545.0, "area233": 17202.0, "area232": 14167.0, "area235": 8910.0, "area236": 4287.0, "area239": 2476.0, "area430": 16737.0, "area436": 2059.0, "area435": 773.0, "area434": 15519.0, "area578": 3743.0, "area768": 2844.0, "area976": 4556.0, "area844": 1704.0, "area531": 5747.0, "area758": 8834.0, "area601": 4441.0, "area698": 60877.0, "area604": 18128.0, "area607": 4728.0, "area608": 2373.0, "area609": 83285.0, "area931": 6957.0, "area831": 4840.0, "area832": 4313.0};
        for (var prop in citypopulation) {
            cityent[cityname[prop]] = citypopulation[prop];
        }


        for(var i=0;i<json.length;i++)
        {
            var ent={};
            var ifcity = json[i]["city"];

            if (ifcity == "Tampere" || ifcity == "Jyväskylä" || ifcity == "Rovaniemi" || ifcity == "Lahti" || ifcity == "Espoo" || ifcity == "Helsinki" || ifcity == "Pori" || ifcity == "Hämeenlinna" || ifcity == "Oulu" || ifcity == "Turku") {
                ent.facebookpage = true;
				ent.like = likes["ent.facebookpage"];
            }
            else {
                ent.facebookpage = false;
				ent.like = 0;
            }

            if (json[i]["queue"]["count"] == 0) {
                ent.hasqueue = true;
            }
            else {
                ent.hasqueue = false;
            }

            if (cityent[json[i]["city"]] > 100000) {
                ent.bigcity = true;
            }
            else {
                ent.bigcity = false;
            }

            listt.push(ent);
        }

        var BigFaceQueue = 0;
        var BigFaceNotQueue = 0;
        var BigNotFaceQueue = 0;
        var BigNotFaceNotQueue = 0;
        var NotBigFaceQueue = 0;
        var NotBigFaceNotQueue = 0;
        var NotBigNotFaceQueue = 0;
        var NotBigNotFaceNotQueue = 0;


        for (i=0; i<listt.length;i++) {
            if (listt[i]["bigcity"] == true  ) {
                if (listt[i]["facebookpage"] == true  ) {
                    if (listt[i]["hasqueue"] == true  ) {
                        BigFaceQueue++;
                        bigcount++;
                        facecount++;
                        queuecount++;
                    }

                    else {
                        BigFaceNotQueue++;
                        bigcount++;
                        facecount++;

                    }

                }

                else {
                    if (listt[i]["hasqueue"] == true  ) {
                        BigNotFaceQueue++;
                        bigcount++;

                        queuecount++;
                    }

                    else {
                        BigNotFaceNotQueue++;
                        bigcount++;


                    }
                }
            }
            else {
                if (listt[i]["facebookpage"] == true  ) {
                    if (listt[i]["hasqueue"] == true  ) {
                        NotBigFaceQueue++;

                        facecount++;
                        queuecount++;
                    }

                    else {
                        NotBigFaceNotQueue++;

                        queuecount++;
                    }
                }

                else {
                    if (listt[i]["hasqueue"] == true  ) {
                        NotBigNotFaceQueue++;
                        facecount++;

                    }

                    else {
                        NotBigNotFaceNotQueue++;
                    }
                }
            }


        }

        var suhdelis=[];
        for (i=0; i<listt.length;i++) {
            var tasmaa = false;
            for (i2=0; i2<suhdelis.length;i2++) {
                if (suhdelis[i2].tasmaa(listt[i]["bigcity"], listt[i]["facebookpage"], listt[i]["hasqueue"])) {
                    //suhdelis[i2]["count"] ++;
                    tasmaa = true;
                    break;
                }

            }
            if (true){
                var suhdu = new suhde(listt[i]["bigcity"], listt[i]["facebookpage"], listt[i]["hasqueue"]);
                suhdelis.push(suhdu);

            }
            }
	
        console.log( facecount );
        console.log( bigcount );
        console.log( queuecount );

        results = JSON.stringify(suhdelis);
        txt2.value = results;




    }});

}

//JSON.stringify

function suhde(big, face, queue) {
    this.big = big;
    this.face=face;
    this.queue=queue;

    this.bigpre;
    this.facepre;
    this.queuepre;



    //this.count = 1;
    this.tasmaa = function(vbig, vface, vqueue) {

        if (this.big != vbig)return false;
        if (this.face != vface)return false;
        if (this.queue != vqueue)return false;
        return true;




    }


}