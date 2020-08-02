#Kütüphaneler
import pandas as pd
import numpy as np

#Karşılaştırma için str oyuncu isimleri
oyuncu_1="TheMustache"
oyuncu_2="TheHeleeee"
oyuncu_3="TheBooyash"
oyuncu_4="Mr.Gold"

#Kullanıcı için oyuncu isimleri
print("-*-Age of Empires Oyunculari-*- \n -->TheMustache\n -->TheHeleeee\n -->TheBooyash\n -->Mr.Gold")

#Kullanıcının skorunu görmek istediği oyuncu adı
oyuncu=str(input("Skorunu merak ettiginiz oyuncunun adini giriniz :"))

#Oyuncuların skorlarının hesaplandığı sınıflar
class TheMustache:
    def skorHesaplama(self):
        #veri_1 kullanıcının belirlediği url içerisindeki veriyi okuyor
        veri_1 = pd.read_csv("http://operations.sparsetechnology.com/public/users/yca/aotstats.txt", sep=",")

        #veri içerisindeki oyuncunun bilgilerini alıyor ve csv uzantılı dosya oluşturuyor
        veri_1[veri_1.player.str.contains("TheMustache")].to_csv("TheMustache.csv")

        #veri_11 oluşturulan yeni dosyayı okuyor
        veri_11 = pd.read_csv("TheMustache.csv")

        #Dosya içerisindeki oyuncunun skorunu belirleyecek olan veriler
        m = veri_11.loc[:, "mils"  ]
        v = veri_11.loc[:, "vils"  ]
        f = veri_11.loc[:, "food"  ]
        w = veri_11.loc[:, "wood"  ]
        g = veri_11.loc[:, "gold"  ]
        s = veri_11.loc[:, "stone" ]

        #skor hesaplaması
        skor1=m*75*0.2+v*50*0.2+(f+w+g+s)*0.2
        print(skor1)

class TheHeleeee:
    def skorHesaplama(self):
        veri_2 = pd.read_csv("http://operations.sparsetechnology.com/public/users/yca/aotstats.txt", sep=",")
        veri_2[veri_2.player.str.contains("TheHeleeee")].to_csv("TheHeleeee.csv")
        veri_22 = pd.read_csv("TheHeleeee.csv")
        m = veri_22.loc[:, "mils"   ]
        v = veri_22.loc[:, "vils"   ]
        f = veri_22.loc[:, "food"   ]
        w = veri_22.loc[:, "wood"   ]
        g = veri_22.loc[:, "gold"   ]
        s = veri_22.loc[:, "stone"  ]
        skor2=m*75*0.2+v*50*0.2+(f+w+g+s)*0.2
        print(skor2)

class TheBooyash:
    def skorHesaplama(self):
        veri_3 = pd.read_csv("http://operations.sparsetechnology.com/public/users/yca/aotstats.txt", sep=",")
        veri_3[veri_3.player.str.contains("TheBooyash")].to_csv("TheBooyash.csv")
        veri_33 = pd.read_csv("TheBooyash.csv")
        m = veri_33.loc[:, "mils"   ]
        v = veri_33.loc[:, "vils"   ]
        f = veri_33.loc[:, "food"   ]
        w = veri_33.loc[:, "wood"   ]
        g = veri_33.loc[:, "gold"   ]
        s = veri_33.loc[:, "stone"  ]
        skor3=m*75*0.2+v*50*0.2+(f+w+g+s)*0.2
        print(skor3)

class MrGold:
    def skorHesaplama(self):
        veri_4 = pd.read_csv("http://operations.sparsetechnology.com/public/users/yca/aotstats.txt", sep=",")
        veri_4[veri_4.player.str.contains("Mr.Gold")].to_csv("MrGold.csv")
        veri_44 = pd.read_csv("MrGold.csv")
        m = veri_44.loc[:, "mils"   ]
        v = veri_44.loc[:, "vils"   ]
        f = veri_44.loc[:, "food"   ]
        w = veri_44.loc[:, "wood"   ]
        g = veri_44.loc[:, "gold"   ]
        s = veri_44.loc[:, "stone"  ]
        skor4=m*75*0.2+v*50*0.2+(f+w+g+s)*0.2
        print(skor4)


#Kullanıcının girdiği isime göre koşullarla sınıf yapılarından veri çekiliyor
if oyuncu == oyuncu_1:
    sonuc1 = TheMustache()
    sonuc=sonuc1.skorHesaplama()
    print("Hazirlayan = Emre CAKIR")

elif oyuncu == oyuncu_2:
    sonuc2 = TheHeleeee()
    sonuc = sonuc2.skorHesaplama()
    print("Hazirlayan = Emre CAKIR")

elif oyuncu == oyuncu_3:
    sonuc3 = TheBooyash()
    sonuc = sonuc3.skorHesaplama()
    print("Hazirlayan = Emre CAKIR")

elif oyuncu == oyuncu_4:
    sonuc4 = MrGold()
    sonuc = sonuc4.skorHesaplama()
    print("Hazirlayan = Emre CAKIR")

else:
    print("Bu isimde bir oyuncu bulunmuyor")
    print("Hazirlayan = Emre CAKIR")