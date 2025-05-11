import time
import random
import os
from colorama import init, Fore, Style

# colorama başlat
init()

# bekleme için
def bekle():
    time.sleep(1)

# daktilo gibi yaz
def yavas_yaz(yazi):
    for harf in yazi:
        print(harf, end='', flush=True)
        time.sleep(0.03) # yavaş yazsın
    print()

# ekranı temizle
def ekran_temiz():
    os.system("cls")

# oyuncu bilgilerini göster
def bilgi_yaz(oyuncu):
    ekran_temiz()
    print(Fore.CYAN + "=================================")
    print(Fore.CYAN + "      OYUNCU BİLGİLERİ         ")
    print(Fore.CYAN + "=================================")
    print(Fore.RED + "İsim: " + oyuncu["isim"] + Style.RESET_ALL) # ismi yaz
    print(Fore.YELLOW + "Sınıf: " + oyuncu["sinif"] + Style.RESET_ALL) # sınıfı yaz
    print(Fore.GREEN + "Can: " + str(oyuncu["can"]) + "/" + str(oyuncu["maxcan"]) + Style.RESET_ALL) # canı yaz
    print(Fore.BLUE + "Mana: " + str(oyuncu["mana"]) + "/" + str(oyuncu["maxmana"]) + Style.RESET_ALL) # manayı yaz
    print(Fore.MAGENTA + "Saldırı: " + str(oyuncu["saldiri"]) + Style.RESET_ALL) # saldırıyı yaz
    print(Fore.WHITE + "Savunma: " + str(oyuncu["savunma"]) + Style.RESET_ALL) # savunmayı yaz
    print(Fore.YELLOW + "Altın: " + str(oyuncu["altin"]) + Style.RESET_ALL) # altını yaz
    print(Fore.GREEN + "Seviye: " + str(oyuncu["seviye"]) + " (Tecrübe: " + str(oyuncu["tecrube"]) + "/" + str(oyuncu["tecrubesinir"]) + ")" + Style.RESET_ALL) # seviyeyi yaz
    print(Fore.BLUE + "Envanter: " + str(oyuncu["envanter"]) + Style.RESET_ALL) # envanteri yaz
    print(Fore.RED + "Görevler: " + str(oyuncu["gorevler"]) + Style.RESET_ALL) # görevleri yaz
    print(Fore.CYAN + "=================================" + Style.RESET_ALL)
    print()

# seviye atlat
def seviye_yuksel(oyuncu):
    if oyuncu["tecrube"] >= oyuncu["tecrubesinir"]: # tecrübe sınırı geçti mi
        oyuncu["seviye"] = oyuncu["seviye"] + 1
        oyuncu["tecrube"] = 0
        oyuncu["tecrubesinir"] = oyuncu["tecrubesinir"] + 50
        oyuncu["maxcan"] = oyuncu["maxcan"] + 20
        oyuncu["maxmana"] = oyuncu["maxmana"] + 10
        oyuncu["can"] = oyuncu["maxcan"]
        oyuncu["mana"] = oyuncu["maxmana"]
        oyuncu["saldiri"] = oyuncu["saldiri"] + 5
        oyuncu["savunma"] = oyuncu["savunma"] + 2
        bilgi_yaz(oyuncu)
        yavas_yaz("🎉 Seviye atladın! Yeni seviye: " + str(oyuncu["seviye"]))

# savaş fonksiyonu
def savas(oyuncu, dusman):
    bilgi_yaz(oyuncu)
    yavas_yaz("⚔️ " + dusman["isim"] + " ile savaş başlıyor!")
    while dusman["can"] > 0 and oyuncu["can"] > 0:
        bilgi_yaz(oyuncu)
        yavas_yaz(Fore.GREEN + "❤️ Senin can: " + str(oyuncu["can"]) + Style.RESET_ALL)
        yavas_yaz(Fore.RED + "😈 " + dusman["isim"] + " can: " + str(dusman["can"]) + Style.RESET_ALL) # düşmanın canını göster
        yavas_yaz("1 - Saldır")
        yavas_yaz("2 - Büyü yap")
        yavas_yaz("3 - Kaç")
        secim = input("Ne yapacaksın: ")
        
        if secim == "1":
            hasar = oyuncu["saldiri"] - dusman["savunma"]
            if hasar < 0:
                hasar = 0
            dusman["can"] = dusman["can"] - hasar # düşmanın canını düşür
            bilgi_yaz(oyuncu)
            yavas_yaz(Fore.GREEN + "🗡️ " + dusman["isim"] + "'e " + str(hasar) + " hasar vurdun!" + Style.RESET_ALL)
        elif secim == "2":
            if oyuncu["mana"] >= 10:
                hasar = oyuncu["saldiri"] * 2
                oyuncu["mana"] = oyuncu["mana"] - 10
                dusman["can"] = dusman["can"] - hasar # düşmanın canını düşür
                bilgi_yaz(oyuncu)
                yavas_yaz(Fore.GREEN + "🔥 Büyüyle " + dusman["isim"] + "'e " + str(hasar) + " hasar vurdun!" + Style.RESET_ALL)
            else:
                bilgi_yaz(oyuncu)
                yavas_yaz("❌ Mana yetmedi!")
        elif secim == "3":
            if random.random() < 0.5:
                bilgi_yaz(oyuncu)
                yavas_yaz(Fore.GREEN + "🏃 Kaçtın!" + Style.RESET_ALL)
                return True
            else:
                bilgi_yaz(oyuncu)
                yavas_yaz(Fore.RED + "❌ Kaçamadın!" + Style.RESET_ALL)
        else:
            bilgi_yaz(oyuncu)
            yavas_yaz("❌ Yanlış seçim!")
        
        if dusman["can"] > 0:
            hasar = dusman["saldiri"] - oyuncu["savunma"]
            if hasar < 0:
                hasar = 0
            oyuncu["can"] = oyuncu["can"] - hasar
            bilgi_yaz(oyuncu)
            yavas_yaz(Fore.RED + "😈 " + dusman["isim"] + " sana " + str(hasar) + " hasar verdi!" + Style.RESET_ALL)
        
        bekle()
    
    if dusman["can"] <= 0:
        bilgi_yaz(oyuncu)
        yavas_yaz(Fore.GREEN + "🏆 " + dusman["isim"] + "'i yendin!" + Style.RESET_ALL)
        oyuncu["tecrube"] = oyuncu["tecrube"] + dusman["tecrube"]
        oyuncu["altin"] = oyuncu["altin"] + dusman["altin"]
        yavas_yaz(Fore.YELLOW + "🎯 " + str(dusman["tecrube"]) + " tecrübe ve " + str(dusman["altin"]) + " altın kazandın!" + Style.RESET_ALL)
        seviye_yuksel(oyuncu)
        return True
    else:
        bilgi_yaz(oyuncu)
        yavas_yaz(Fore.RED + "💀 Öldün... Oyun bitti." + Style.RESET_ALL)
        exit()

# dükkan
def dukkan(oyuncu):
    bilgi_yaz(oyuncu)
    yavas_yaz("🛒 Dükkana hoş geldin!")
    yavas_yaz("💰 Altın: " + str(oyuncu["altin"]))
    yavas_yaz("Kılıç - 20 altın")
    yavas_yaz("Zırh - 15 altın")
    yavas_yaz("İksir - 10 altın")
    if "İksir" in oyuncu["envanter"]:
        yavas_yaz("İksir kullan - 0 altın")
    secim = input("Ne almak istersin (veya çık yaz): ")
    
    if secim == "çık":
        bilgi_yaz(oyuncu)
        yavas_yaz("👋 Dükkandan çıktın.")
        return
    elif secim == "Kılıç":
        if oyuncu["altin"] >= 20:
            oyuncu["altin"] = oyuncu["altin"] - 20
            oyuncu["envanter"].append("Kılıç")
            if oyuncu["sinif"] == "Savaşçı":
                oyuncu["saldiri"] = oyuncu["saldiri"] + 8 # savaşçı için daha çok
            elif oyuncu["sinif"] == "Haydut":
                oyuncu["saldiri"] = oyuncu["saldiri"] + 6 # haydut için orta
            else:
                oyuncu["saldiri"] = oyuncu["saldiri"] + 4 # büyücü için az
            bilgi_yaz(oyuncu)
            yavas_yaz(Fore.GREEN + "✅ Kılıç aldın!" + Style.RESET_ALL)
        else:
            bilgi_yaz(oyuncu)
            yavas_yaz(Fore.RED + "❌ Altın yetmedi!" + Style.RESET_ALL)
    elif secim == "Zırh":
        if oyuncu["altin"] >= 15:
            oyuncu["altin"] = oyuncu["altin"] - 15
            oyuncu["envanter"].append("Zırh")
            if oyuncu["sinif"] == "Savaşçı":
                oyuncu["savunma"] = oyuncu["savunma"] + 5 # savaşçı için daha çok
            elif oyuncu["sinif"] == "Haydut":
                oyuncu["savunma"] = oyuncu["savunma"] + 4 # haydut için orta
            else:
                oyuncu["savunma"] = oyuncu["savunma"] + 2 # büyücü için az
            bilgi_yaz(oyuncu)
            yavas_yaz(Fore.GREEN + "✅ Zırh aldın!" + Style.RESET_ALL)
        else:
            bilgi_yaz(oyuncu)
            yavas_yaz(Fore.RED + "❌ Altın yetmedi!" + Style.RESET_ALL)
    elif secim == "İksir":
        if oyuncu["altin"] >= 10:
            oyuncu["altin"] = oyuncu["altin"] - 10
            oyuncu["envanter"].append("İksir")
            bilgi_yaz(oyuncu)
            yavas_yaz(Fore.GREEN + "✅ İksir aldın!" + Style.RESET_ALL)
        else:
            bilgi_yaz(oyuncu)
            yavas_yaz(Fore.RED + "❌ Altın yetmedi!" + Style.RESET_ALL)
    elif secim == "İksir kullan":
        if "İksir" in oyuncu["envanter"]:
            oyuncu["envanter"].remove("İksir") # bir iksir çıkar
            oyuncu["can"] = oyuncu["can"] + 20
            if oyuncu["can"] > oyuncu["maxcan"]:
                oyuncu["can"] = oyuncu["maxcan"]
            bilgi_yaz(oyuncu)
            yavas_yaz(Fore.GREEN + "💊 İksir kullandın, 20 can doldu!" + Style.RESET_ALL)
        else:
            bilgi_yaz(oyuncu)
            yavas_yaz(Fore.RED + "❌ İksirin yok!" + Style.RESET_ALL)
    else:
        bilgi_yaz(oyuncu)
        yavas_yaz(Fore.RED + "❌ Yanlış eşya!" + Style.RESET_ALL)

# oyunu başlat
ekran_temiz()
yavas_yaz("✨ Krallık seni çağırıyor...")
isim = input("🗡️ İsmin ne olacak: ")
ekran_temiz()
yavas_yaz("🔮 Sınıfını seç:")
yavas_yaz("1 - Savaşçı")
yavas_yaz("2 - Büyücü")
yavas_yaz("3 - Haydut")
sinif = input("Seçimin: ")

if sinif == "1":
    oyuncu = {
        "isim": isim,
        "sinif": "Savaşçı",
        "can": 100,
        "maxcan": 100,
        "mana": 20,
        "maxmana": 20,
        "saldiri": 15,
        "savunma": 10,
        "altin": 30,
        "seviye": 1,
        "tecrube": 0,
        "tecrubesinir": 50,
        "envanter": ["Kılıç"],
        "gorevler": []
    }
elif sinif == "2":
    oyuncu = {
        "isim": isim,
        "sinif": "Büyücü",
        "can": 50,
        "maxcan": 50,
        "mana": 80,
        "maxmana": 80,
        "saldiri": 5,
        "savunma": 3,
        "altin": 30,
        "seviye": 1,
        "tecrube": 0,
        "tecrubesinir": 50,
        "envanter": ["Asa"],
        "gorevler": []
    }
else:
    oyuncu = {
        "isim": isim,
        "sinif": "Haydut",
        "can": 70,
        "maxcan": 70,
        "mana": 40,
        "maxmana": 40,
        "saldiri": 10,
        "savunma": 5,
        "altin": 30,
        "seviye": 1,
        "tecrube": 0,
        "tecrubesinir": 50,
        "envanter": ["Hançer"],
        "gorevler": []
    }

bilgi_yaz(oyuncu)
yavas_yaz(Fore.GREEN + "👤 " + isim + ", " + oyuncu["sinif"] + " olarak maceran başlıyor!" + Style.RESET_ALL)

# hikaye
bekle()
bilgi_yaz(oyuncu)
yavas_yaz("🌒 Gece... Rüyanda yanan bir krallık görüyorsun.")
bekle()
bilgi_yaz(oyuncu)
yavas_yaz("🕯️ Bir ses yankılanıyor: Uyan ve kaderini seç!")
bekle()

bilgi_yaz(oyuncu)
yavas_yaz("📍 Gözlerini açtığında bir köy meydanındasın.")
yavas_yaz("👩‍🌾 [Elira]: Sen yabancısın, ama gözlerin kralınki gibi. Yardım eder misin?")
secim = input("1 - Yardım et\n2 - Görmezden gel\nSeçimin: ")

bilgi_yaz(oyuncu)
if secim == "1":
    oyuncu["gorevler"].append("Kralı Kurtar")
    yavas_yaz(Fore.GREEN + "🗺️ Görev alındı: Kralı Kurtar!" + Style.RESET_ALL)
    yavas_yaz("👩‍🌾 [Elira]: Teşekkürler! Kuzeydeki tapınakta ipucu var.")
else:
    yavas_yaz(Fore.RED + "👩‍🌾 [Elira]: Zaten umut kalmadı..." + Style.RESET_ALL)
    yavas_yaz("🚶 Köyden ayrılıyorsun.")

# oyun döngüsü
while True:
    bekle()
    bilgi_yaz(oyuncu)
    yavas_yaz("🗺️ Neredesin: Köy Meydanı")
    yavas_yaz("1 - Dükkana git")
    yavas_yaz("2 - Kuzey ormanına git (Tapınak)")
    yavas_yaz("3 - Köyde bilgi topla")
    yavas_yaz("4 - Batı mağarasına git (Mührü bul)")
    yavas_yaz("5 - Bilgileri gör")
    yavas_yaz("6 - Oyunu bitir")
    secim = input("Seçimin: ")

    if secim == "1":
        dukkan(oyuncu)
    elif secim == "2":
        bilgi_yaz(oyuncu)
        yavas_yaz("🌲 Kuzey ormanına gidiyorsun...")
        bekle()
        bilgi_yaz(oyuncu)
        yavas_yaz("🐺 Bir vahşi kurt sürüsü karşına çıktı!")
        kurt = {
            "isim": "Vahşi Kurt",
            "can": 30,
            "saldiri": 8,
            "savunma": 3,
            "tecrube": 20,
            "altin": 10
        }
        savas(oyuncu, kurt)
        bilgi_yaz(oyuncu)
        yavas_yaz("🌲 Kurtları yendin ve tapınağa vardın.")
        yavas_yaz("🏛️ Bir muhafız: Kralın mührünü göster!")
        if "Mührü" in oyuncu["envanter"]:
            bilgi_yaz(oyuncu)
            yavas_yaz(Fore.GREEN + "✅ Mührü gösterdin, içeri girdin!" + Style.RESET_ALL)
            yavas_yaz("🌀 Bir portal açıldı. Mavi ışıklar seni içine çekiyor...")
            yavas_yaz("🌌 Yeni bir dünyaya adım atıyorsun... [Hikaye devam edecek]")
            break
        else:
            bilgi_yaz(oyuncu)
            yavas_yaz(Fore.RED + "❌ Mührün yok, geri dön!" + Style.RESET_ALL)
            yavas_yaz(Fore.YELLOW + "📜 Yeni görev: Mührü bul" + Style.RESET_ALL)
            oyuncu["gorevler"].append("Mührü bul")
    elif secim == "3":
        bilgi_yaz(oyuncu)
        yavas_yaz("👥 Köyde insanlarla konuşuyorsun...")
        bekle()
        bilgi_yaz(oyuncu)
        yavas_yaz("🧙‍♂️ [Bilge]: Mührü batıdaki mağarada bir ejderha koruyor.")
        yavas_yaz(Fore.YELLOW + "📜 Yeni görev: Mührü bul" + Style.RESET_ALL)
        oyuncu["gorevler"].append("Mührü bul")
    elif secim == "4":
        bilgi_yaz(oyuncu)
        yavas_yaz("🪨 Batı mağarasına doğru yola çıkıyorsun...")
        bekle()
        bilgi_yaz(oyuncu)
        yavas_yaz("🐉 Mağaranın derinliklerinde korkunç bir ejderha beliriyor!")
        ejderha = {
            "isim": "Ejderha",
            "can": 50,
            "saldiri": 12,
            "savunma": 5,
            "tecrube": 50,
            "altin": 30
        }
        savas(oyuncu, ejderha)
        bilgi_yaz(oyuncu)
        yavas_yaz(Fore.GREEN + "🎉 Ejderhayı yendin! Mağarada parlayan bir mühür buldun!" + Style.RESET_ALL)
        oyuncu["envanter"].append("Mührü")
        if "Mührü bul" in oyuncu["gorevler"]:
            oyuncu["gorevler"].remove("Mührü bul")
            yavas_yaz(Fore.YELLOW + "📜 Görev tamamlandı: Mührü bul!" + Style.RESET_ALL)
        yavas_yaz("🏛️ Şimdi tapınağa dönüp mührü gösterebilirsin.")
    elif secim == "5":
        bilgi_yaz(oyuncu)
        yavas_yaz("📊 Bilgilerin yukarıda!")
    elif secim == "6":
        bilgi_yaz(oyuncu)
        yavas_yaz("💾 Oyun bitti, görüşürüz!")
        break
    else:
        bilgi_yaz(oyuncu)
        yavas_yaz(Fore.RED + "❌ Yanlış seçim!" + Style.RESET_ALL)