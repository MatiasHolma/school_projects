

var Reseptilista = React.createClass({

  //componentDidMount
  componentDidMount : function(){
    var json = {}

    $.ajax({
      async : false,
      url: "src/reseptitjson.py",
      success: function(data){
        for(var key in data){
          json[key+"."] = data[key]
        }
      },
      dataType: "json"
    })



    var json2 = {}
    $.ajax({
      async : false,
      url: "src/reseptinruokalajijson.py",
      success: function(data){
        for(var key in data){
          json2[key+"."] = data[key]

        }
      },
      dataType: "json"
    })
    //json = this.jarjestataulukko(json2)
    this.setState({ruokalajit:json2})
    json = this.jarjestataulukko(json)
    this.setState({reseptinimet:json})



    //this.setState({reseptinimet:json2})


  },


  //Intitial State
  getInitialState : function(){
    return {
      reseptinimet : {},
      ruokalajit : {},
      ruokaaineet : [],
      suunta : false,
    }
  },


  teespan : function(key){
    return (
        <li id="key" className="reseptili">{this.state.reseptinimet[key + "."]} <ul><li>{this.state.ruokalajit[key + "."]} </li></ul>{this.teelista2(key + ".")}</li>

    )


  },

  teelista : function() {
    var listanosat = []
    var dict = this.jarjestataulukko(this.state.reseptinimet)
    for (var key in dict){
        avain = key.substr(0,key.length-1);
        listanosat.push(this.teespan(avain));
    }

    return (
    {listanosat}
    )
  }
  ,

  teelista2 : function(key) {
    avain = key.substr(0,key.length-1);


    return (
    <ol>{this.teeainelista(avain)}</ol>
    )
  }
  ,
      teesisalista : function(json, avain2) {
  lista = []
        for (var key in json[avain2]) {
          apu = ""
          for (var key2 in json[avain2][key]) {
            apu += json[avain2][key][key2] + " "


          }
          lista.push(this.
              teeapu(apu))

        }


    return (
    {lista}
    )
  }
  ,

  teeapu : function(json, avain2) {


    return (
    <li>{apu}</li>
    )
  }
  ,




  teeainelista : function(avain) {



      json = {}
      $.ajax({
        async: false,
        url: "src/palvelingetjson.py?Resepti=" + avain,
        success: function (data) {
          for (var key in data) {
          json[key +  "." + "avain"] = data[key];
            avain2 = key +  "." + "avain"
            break;
          }
        },
        dataType: "json"
      })

    lista = this.state.ruokaaineet
    lista.push(json)


    /*this.setState({ruokaaineet:lista})
    for (var key in dict){
      avain = key.substr(0,key.length-1);
      listanosat.push(this.teeainelista(avain));
    }*/
    return (
        this.teesisalista(json, avain2)
    )
  }
  ,


  listaa : function(){
    return(
        <ul>{this.teelista()}</ul>
    )
  },


  jarjestataulukko : function(json){



    var suunta = this.state.suunta;
    var kokoelma = {};
    var lista = [];



    for (var key in json){
      lista.push(json[key])
    }


    lista.sort();
    if(!suunta) {
      for (var i = 0; i < lista.length; i++) {
        for (var key in json) {
          if (lista[i] == json[key]) {
            kokoelma[key] = lista[i]
          }
        }
      }
    }
    else{
      for (var i = lista.length-1; 0 <= i; i--) {
        for (var key in json) {
          if (lista[i] == json[key]) {
            kokoelma[key] = lista[i]
          }
        }
      }
    }

    return kokoelma
  },


  kaanna : function(event){
    if(this.state.suunta == true){
      this.setState({suunta : false})
    }
    else{
      this.setState({suunta : true})
    }

  },


  render : function(){
    return(
        <div>
          <label for="vaihda">Käännä</label><input onChange={this.kaanna}  type="checkbox" id="vaihda"></input>
          <div>
            {this.listaa()}
          </div>
        </div>
    )
  }

});


var Reseptit = React.createClass({
  getInitialState : function(){
    return {
      iteraator : 1
    }
  },
  render : function(){
    return(
        <div id="Reseptit" className="Respetit">
          <h2>Reseptit</h2>
          <Reseptilista />
        </div>
    )
  }
});


var LisaaResepti = React.createClass({

  render : function(){
    return(
        <div id="lisaaResepti" className="lisaaResepti">
            <p> <label for="Nimi">Nimi</label> <br /><input name="Nimi" id="Nimi" className="kentta"> </input></p>
            <p> <label for="Kuvaus">Kuvaus</label> <br /><input name="Kuvaus" id="Kuvaus" className="kentta"></input> </p>
            <p> <label for="henmaara">Henkilömäärä</label> <br /> <input name="henmaara" min="1" max="100" step="1" value="1" id="henmaara" type="number"></input></p><p id="henmaarap"></p>
            <p id="ruokalajip"> <label>Ruokalaji</label><br /><select id="ruokalaji" name="ruokalaji"><option value="7">Makea leivonnainen</option><option value="5">Jälkiruoka</option><option value="6">Suolainen leivonnainen</option><option value="2">Pääruoka</option><option value="4">Väli - tai iltapala</option><option value="1">Alkuruoka</option><option value="3">Lisäkeruoka</option></select></p>
        </div>
      )
  }
});







var Reseptisivu = React.createClass({
  render : function(){
    return(
        <div id="content">
          <div id="vasen"><Reseptit/></div>
            <div id="oikea"><LisaaResepti/></div>
        </div>
    )
  }
});


React.render(
    <Reseptisivu/>,
    document.getElementById("main")
);