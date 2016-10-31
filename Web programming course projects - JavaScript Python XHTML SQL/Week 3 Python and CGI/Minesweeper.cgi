#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgitb
cgitb.enable()
import cgi
import time
import datetime
import random
import os
from xml.dom.minidom import getDOMImplementation, parse, parseString

x = 0
askenx = -1
askeny = 0
oliolist = []
alustettu = False
arvottu = False
laskettu = False
pommipainettu = False
tuplaklikattu = False
pommeja = 0
vaihdettu = False

class Ruutuolio(object):

    def __init__(self, ys, xs, painettu, pommejavieressa):
        self.ys = ys
        self.xs = xs
        self.painettu = painettu
        self.pommejavieressa = pommejavieressa

def chekstring(stekattava):
    for c in stekattava:
        if c == '<' or c == '>' or c == '&' or c == 'ä' or c == 'ö':
            stekattava = ""
            return stekattava
    return stekattava

def chekstring2(stekattava):
    return stekattava.decode("UTF-8")


def findOlio(yi,xi):
    global oliolist
    i=0
    while(i<len(oliolist)):
        if(oliolist[i].ys==yi and oliolist[i].xs==xi):
            return oliolist[i]
        i=i+1

def teeRuudukko(x):
    global alustettu
    global oliolist
    global pommipainettu

    if True:
        alustettu = True
        yi=0
        xi=0
        zi=0
        formm = dom1.getElementsByTagName("form")
        #tehdään table
        table = dom1.createElement("table")
        formm = dom1.getElementsByTagName("form")
        formm[0].appendChild( table )

        #formm[0].appendChild( table )
        while yi<x:
            tr = dom1.createElement("tr")
            table.appendChild(tr)
            while xi<x:
                name = str(yi) + "a" + str(xi)
                input = dom1.createElement("input")
                #olio = findOlio(yi,xi)
                olio = oliolist[zi]
                input.setAttribute("type", "hidden")
                input.setAttribute("name", name)
                #lisätään 0, jos nappia ei ole painettu, 1 jos sitä on painettu
                input.setAttribute("value", str(olio.painettu))
                name2 = str(yi) + "aa" + str(xi)
                input2 = dom1.createElement("input")
                input2.setAttribute("type", "hidden")
                input2.setAttribute("name", name2)
                #pommeja. Lisätään joku ympäröivien pommien määrä, tai -1 jos kyseisessä ruudussa on pommi
                input2.setAttribute("value", str(olio.pommejavieressa))
                name3 = str(yi) + "aaa" + str(xi)
                input3 = dom1.createElement("input")
                input3.setAttribute("type", "hidden")
                input3.setAttribute("name", name3)
                #listätään 1, jos tätä nappia klikattiin äsken. Muuten lisätään 0
                input3.setAttribute("value", "0")
                td = dom1.createElement("td")
                pt = dom1.createElement("p")
                span = dom1.createElement("span")
                td.appendChild(pt)
                pt.appendChild(input)
                pt.appendChild(input2)
                pt.appendChild(input3)
                tr.appendChild(td)
                a = dom1.createElement("a")

                linkki = teelinkki(yi,xi)
                a.setAttribute("href", linkki)
                txt = dom1.createTextNode(str(olio.pommejavieressa))



                #tila on 1, jos tätä nappia klikattiin äsken. Muuten 0
                if olio.painettu == 1:
                    if olio.pommejavieressa == -1:#lisää myöhemmin
                        pommiapainettu = True
                        img = dom1.createElement("img")
                        img.setAttribute("src", "mine.svg")
                        img.setAttribute("alt", "miina")
                        img.setAttribute("class", "img")
                        span.appendChild( img )
                        td.appendChild(span)
                    else: #lisää myöhemmin
                        span.setAttribute("class", "klikattutyhja")
                        span.appendChild( txt )
                        td.appendChild(span)
                else:
                    span.setAttribute("class", "klikkaamaton")
                    #a.appendChild( txt )
                    a.appendChild(span)
                    td.appendChild(a)
                xi = xi+1
                zi=zi+1
            yi = yi + 1
            xi = 0
    #if pommipainettu == True:
    #    rajahti()

#aloitetaan tekemällä oliotaulukko
def teeOliotaulukko():
    #Globaalit muuttujat
    global x #taulukon leveys
    global askenx #asken painetun ruudun x-koordinaatti
    global askeny #asken painetun ruudun y-koordinaatti
    global oliolist #lista, mihin tehdään ruutuja symbolisoivia apu-oliota
    global alustettu #boolen, onko ruudut alustettu ja pommit arvottu
    global laskettu #boolean onko ruutujen viereisiä pommeja laskettu
    global tuplaklikattu
    global arvottu
    global pommeja
    global vaihdettu
    xi=0 #iteraattori x
    yi=0 #iteraattori x
    zi=0
    form = cgi.FieldStorage()
    #esitellään olioita valmiiksi
    tila = ""
    pommi = ""
    painettu = False

    #jos ensimmäinen piilotettu arvo antaa jonkun muun, kuin "" arvon, on jonkinmoinen taulukko jo tehty
    #Tässä tapauksessa taulukkoa ei ole vielä tehty
    if form.getfirst(str(yi)+"a"+str(xi), "")=="..." or form.getfirst(str(yi)+"a"+str(xi), "")=="" or vaihdettu == True:
        #alustetaan
        alustettu = False #ruudukkoa ei siis vielä ole alustettu


        while yi<x:


            while xi<x:
            #Annetaan olioille tyhjät arvot
                oliolist.append(Ruutuolio(yi, xi, 0, 0))
                xi = xi+1
            yi = yi + 1
            xi = 0
    #Jos taulukko on tehty, haetaan siihen asetetut piilotetut arvot.
    else:
        alustettu = True #ruudukko on alustettu, koska sieltä saatiin jokin arvo

        while yi<x:
            while xi<x:
                name = str(yi)+"aaa"+str(xi)
                if(form.getfirst(name, "")=="1"):
                    askeny = yi
                    askenx = xi
                #selvitetään onko pommia painettu. 1 tarjoittaa on, ja 0 ei
                tila = form.getfirst(str(yi)+"a"+str(xi), "")
                if tila=="1":
                    painettu = True
                else:
                    painettu = False
                #selvitetään onko ruudussa pommia, tai sen vieressä pommia
                pommi = (form.getfirst(str(yi)+"aa"+str(xi), ""))
                if (len(pommi)==0):
                    pommi = "0"
                #Jos jossain ruudussa on pommi. Pommit ovat selvästi arvottu
                if(pommi=="-1"):
                    arvottu = True
                    #Jos äskenklikattu on pommi. siirrytaan toiseen aliohjelmaan
                    if yi==askeny and xi == askenx:
                        pommiapainettu = True
                #tallennetaan nappi, mihin äsken klikattiin.

                pommiint = int(pommi)
                #Jos jokin ruutu tietää, montako pommia sen vieressä on. Se on laskettu
                if pommiint > 0:
                    laskettu = True
                oliolist.append(Ruutuolio(yi, xi, painettu, pommiint))
                xi = xi+1
            yi = yi + 1
            xi = 0


#arvotaan pommien paikat
def arvopommit():
    #ruutuja symboloiva aluoliolista
    global oliolist
    global alustettu
    global askenx
    global askeny
    global pommeja
    global x
    global arvottu
    global laskettu
    i = 0
    pommix=0
    pommiy=0
    onnistui = True
    #if tuplaklikattu:
    #    return
    #if askenx == -1:
     #   return
    #arvotaan pommit vasta kun alustus on tehty
    if(alustettu==False):
        return
    #arvontaa ei suoriteta kahta jertaa
    if(arvottu==True):
        if laskettu == False:
            laskeviereiset()
        ekailmoitaviereiselle()
        return
    while (i<pommeja):
        pommiy = random.randint(0,x-1)
        pommix = random.randint(0,x-1)
        #varmistetaan, etttei pommia arvota ensimmäisenä painetun napin päälle tai viereen
        if pommiy == askeny and pommix == askenx:
            continue
        if pommiy == askeny+1 and pommix == askenx-1:
            continue
        if pommiy == askeny+1 and pommix == askenx:
            continue
        if pommiy == askeny+1 and pommix == askenx+1:
            continue
        if pommiy == askeny and pommix == askenx-1:
            continue
        if pommiy == askeny and pommix == askenx+1:
            continue
        if pommiy == askeny-1 and pommix == askenx-1:
            continue
        if pommiy == askeny-1 and pommix == askenx:
            continue
        if pommiy == askeny-1 and pommix == askenx+1:
            continue
        #varmistetaan, ettei pommia arvota paikkaan, missä pommi jo on
        olio = findOlio(pommiy,pommix)
        if olio.pommejavieressa == -1:
            continue
        olio.pommejavieressa = -1
        i=i+1



#aliohjelma mihin mennään, jos pelaaja painaa pommia
def rajahti():
    global oliolist
    global x
    xi=0
    yi=0
    while yi < x:
        while xi<x:
        #pistetään kaikki pommit näkyviin
            olio = findOlio(yi, xi)
            if olio.pommejavieressa==-1:
                olio.painettu=1
            xi = xi + 1
        xi = 0
        yi = yi + 1


def laskeviereiset():
    global laskettu
    global oliolist
    global x
    if laskettu == True:
        return
    yc = 0
    xc = 0
    laskettu = True


    q11 = True
    q12 = True
    q13 = True
    q21 = True
    q23 = True
    q31 = True
    q32 = True
    q33 = True
    while yc<x:
        while xc < x:
            olio = findOlio(yc,xc)
            #jollei ruutu ole pommi, jatketaan
            if olio.pommejavieressa != -1:
                xc = xc + 1
                continue


            olio2 = findOlio(yc-1,xc-1)
            if olio2 is not None:
                if olio2.pommejavieressa != -1:
                    olio2.pommejavieressa = olio2.pommejavieressa + 1


            olio2 = findOlio(yc-1,xc)
            if olio2 is not None:
                if olio2.pommejavieressa != -1:
                    olio2.pommejavieressa = olio2.pommejavieressa + 1


            olio2 = findOlio(yc-1,xc+1)
            if olio2 is not None:
                if olio2.pommejavieressa != -1:
                    olio2.pommejavieressa = olio2.pommejavieressa + 1


            olio2 = findOlio(yc,xc-1)
            if olio2 is not None:
                if olio2.pommejavieressa != -1:
                    olio2.pommejavieressa = olio2.pommejavieressa + 1


            olio2 = findOlio(yc,xc+1)
            if olio2 is not None:
                if olio2.pommejavieressa != -1:
                    olio2.pommejavieressa = olio2.pommejavieressa + 1



            olio2 = findOlio(yc+1,xc-1)
            if olio2 is not None:
                if olio2.pommejavieressa != -1:
                    olio2.pommejavieressa = olio2.pommejavieressa + 1


            olio2 = findOlio(yc+1,xc)
            if olio2 is not None:
                if olio2.pommejavieressa != -1:
                    olio2.pommejavieressa = olio2.pommejavieressa + 1


            olio2 = findOlio(yc+1,xc+1)
            if olio2 is not None:
                if olio2.pommejavieressa != -1:
                    olio2.pommejavieressa = olio2.pommejavieressa + 1



            xc = xc +1


        yc = yc + 1
        xc = 0





def ilmoitaviereiselle(yc, xc):
    global oliolist
    global x
    olio = findOlio(yc, xc)
    if olio.pommejavieressa == -1:
        return
    if olio.painettu==1:
        return
    olio.painettu = 1
    if olio.pommejavieressa!=0:
        return
    #olio.pommejavieressa = olio.pommejavieressa + 1

    q11 = True
    q12 = True
    q13 = True
    q21 = True
    q23 = True
    q31 = True
    q32 = True
    q33 = True

    #Tarkistetaan onko klikattu ruutu reunassa
    if yc <= 0:
        q11 = False
        q12 = False
        q13 = False
    if xc <= 0:
        q11 = False
        q21 = False
        q31 = False
    if yc >= x-1:
        q31 = False
        q32 = False
        q33 = False
    if xc >= x-1:
        q13 = False
        q23 = False
        q33 = False
#lasketaan viereiset


#tehdään rekursio
    if q11 == True:
        ilmoitaviereiselle(yc-1,xc-1)
    if q12 == True:
        ilmoitaviereiselle(yc-1,xc)
    if q13 == True:
        ilmoitaviereiselle(yc-1,xc+1)
    if q21 == True:
        ilmoitaviereiselle(yc,xc-1)
    if q23 == True:
        ilmoitaviereiselle(yc,xc+1)
    if q31 == True:
        ilmoitaviereiselle(yc+1,xc-1)
    if q32 == True:
        ilmoitaviereiselle(yc+1,xc)
    if q33 == True:
        ilmoitaviereiselle(yc+1,xc+1)
    q11 = True
    q12 = True
    q13 = True
    q21 = True
    q23 = True
    q31 = True
    q32 = True
    q33 = True


def ekailmoitaviereiselle():
    global oliolist
    global askenx
    global askeny
    global x
    xc = askenx
    yc = askeny
    if askenx == -1:
        return
    olio = findOlio(askeny, askenx)
    if (olio.pommejavieressa==-1):
        rajahti()
    if (olio.painettu!=0):
        return
    #olio.pommejavieressa = olio.pommejavieressa + 1
    olio.painettu = 1
    if olio.pommejavieressa!=0:
        return
    q11 = True
    q12 = True
    q13 = True
    q21 = True
    q23 = True
    q31 = True
    q32 = True
    q33 = True

    #Tarkistetaan onko klikattu ruutu reunassa
    if yc == 0:
        q11 = False
        q12 = False
        q13 = False
    if xc == 0:
        q11 = False
        q21 = False
        q31 = False
    if yc == x-1:
        q31 = False
        q32 = False
        q33 = False
    if xc == x-1:
        q13 = False
        q23 = False
        q33 = False

    if q11 == True:
        ilmoitaviereiselle(yc-1,xc-1)
    if q12 == True:
        ilmoitaviereiselle(yc-1,xc)
    if q13 == True:
        ilmoitaviereiselle(yc-1,xc+1)
    if q21 == True:
        ilmoitaviereiselle(yc,xc-1)
    if q23 == True:
        ilmoitaviereiselle(yc,xc+1)
    if q31 == True:
        ilmoitaviereiselle(yc+1,xc-1)
    if q32 == True:
        ilmoitaviereiselle(yc+1,xc)
    if q33 == True:
        ilmoitaviereiselle(yc+1,xc+1)
    q11 = True
    q12 = True
    q13 = True
    q21 = True
    q23 = True
    q31 = True
    q32 = True
    q33 = True

#    def __init__(self, ys, xs, painettu, pommejavieressa):
#tehdään osoite, minkä linkit lähettää
def teelinkki(yc,xc):
    global x
    global pommeja
    global oliolist
    global askenx
    global askeny
    global tuplaklikattu
    global fviimev
    global fviimex
    global vaihdettu
    tiedostonNimi = "tess.cgi?"
    tiedostonNimi = tiedostonNimi + "x=" + str(x) 
    tiedostonNimi = tiedostonNimi + "&viimeotsikko=" + viimeotsikko
    if vaihdettu == True:
        tiedostonNimi = tiedostonNimi  + "&viimev=" + str(pommeja) + "&viimex=" + str(x)
    if fviimev is not None:
        tiedostonNimi = tiedostonNimi  + "&viimev=" + fviimev + "&viimex=" + fviimex
    yi = 0
    xi = 0
    zi = 0
    #if vaihdettu == True:
    #    return tiedostonNimi
    while yi<x:
        while xi<x:
            olio = findOlio(yi, xi)
            name = str(yi) + "a" + str(xi)
            name2 = str(yi) + "aa" + str(xi)
            name3 = str(yi) + "aaa" + str(xi)
            if (olio.painettu):
                er = "1"
            else:
                er = "0"
            tiedostonNimi =  tiedostonNimi + "&" + name + "=" + er + "&" + name2 + "=" + str(olio.pommejavieressa)
            if (yi == yc and xi == xc):
                tiedostonNimi =  tiedostonNimi + "&" + name3 + "=" + "1"
            else:
                tiedostonNimi =  tiedostonNimi + "&" + name3 + "=" + "0"
            xi = xi+1
            zi = zi+1
        yi = yi + 1
        xi = 0
#Tehdään return ehto iffiin, koska muuten silmukka jostain syystä pysähtyi returniin, vaikka sisennykset mielestänni oikein.
    if yi == x:
        return tiedostonNimi


#tehdään alkuvalmistelut
print """Content-type: text/html;charset=UTF-8
"""
pohja = os.path.join(os.path.dirname(os.environ['SCRIPT_FILENAME']), 'vk3.html')
dom1 = parse(pohja)
body = dom1.getElementsByTagName("body")

#alustetaan otsikko
viimeotsikko = ""


#haetaaan syötetyt arvot
form = cgi.FieldStorage()
fx = form.getfirst("x", "")


#katsotaan onko jokin otsikko jo olemassa
lasttitleform = form.getfirst("viimeotsikko", "")
lasttitleform = chekstring2(lasttitleform)
if len(lasttitleform)>0:
    viimeotsikko = lasttitleform


#haetaan teksti, mistä halutaan otsikko
fvalittu = form.getfirst("teksti", "")
fvalittu = chekstring2(fvalittu)

#Jos Tekstikenttä on erisuuri kuin tyhjä:
if len(fvalittu)>0:
    viimeotsikko = fvalittu


formm = dom1.getElementsByTagName("form")
tr = dom1.createElement("tr")

#katsotaan x ja y arvoja olemassa
fviimex = form.getfirst("viimex", "")
fviimev = form.getfirst("viimev", "")



#tallennetaan vanha otsikko
inputtxt = dom1.createElement("input")
inputtxt.setAttribute("type", "hidden")
inputtxt.setAttribute("name", "viimeotsikko")
inputtxt.setAttribute("value", viimeotsikko)
pp3 = dom1.createElement("p")
pp3.appendChild(inputtxt)
formm[0].appendChild( pp3 )

if len(fviimex) == 0:
    fviimex = fx
    #fviimev = fvalittu

h1 = dom1.getElementsByTagName("h1")
otsikkotxt = dom1.createTextNode(viimeotsikko)
h1[0].appendChild(otsikkotxt)
if len(viimeotsikko)>0:
    h1[0].removeChild(h1[0].firstChild)


inputx = dom1.createElement("input")
inputx.setAttribute("type", "hidden")
inputx.setAttribute("name", "viimex")
inputx.setAttribute("value", str(fviimex))
pp = dom1.createElement("p")
pp.appendChild( inputx )
formm[0].appendChild( pp )
inputv = dom1.createElement("input")
inputv.setAttribute("type", "hidden")
inputv.setAttribute("name", "viimev")
inputv.setAttribute("value", str(fviimev))
pp2 = dom1.createElement("p")
pp2.appendChild( inputv )
formm[0].appendChild( pp2 )


if fviimex != fx and len(fviimev) > 0:
   vaihdettu = True


if (len(fx)>0):
    x = int(fx)
    pommeja = (x*x)/3
    if x >= 6 and x<= 12:
        teeOliotaulukko()
        arvopommit()
        laskeviereiset()
        ekailmoitaviereiselle()
        teeRuudukko(x)



print dom1.toxml('UTF-8')


