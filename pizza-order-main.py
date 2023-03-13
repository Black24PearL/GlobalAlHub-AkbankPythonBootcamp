# Pizza Menüsü
menu = {
    1: {"isim": "Klasik", "fiyat": 10},
    2: {"isim": "Margarita", "fiyat": 12},
    3: {"isim": "Türk Pizza", "fiyat": 9},
    4: {"isim": "Sade Pizza", "fiyat": 11}
}

# Sos Menüsü
soslar = {
    11: {"isim": "Zeytin", "fiyat": 1.5},
    12: {"isim": "Mantarlar", "fiyat": 2},
    13: {"isim": "Keçi Peyniri", "fiyat": 2},
    14: {"isim": "Et", "fiyat": 2.5},
    15: {"isim": "Soğan", "fiyat": 1},
    16: {"isim": "Mısır", "fiyat": 1.5}
}

# Kullanıcıya Pizza ve Sos seçtirme
print("Merhaba, Pizza Siparişi vermek için Menüden Pizza ve Sos seçin: ")
print("Menü: ")
for key, value in menu.items():
    print(key, ":", value["isim"], " - ", value["fiyat"], "TL")

pizza = int(input("Pizza seçin (1-4): "))
while pizza not in menu:
    pizza = int(input("Geçersiz seçim. Lütfen Menüden bir Pizza seçin (1-4): "))

print("Sos Menüsü: ")
for key, value in soslar.items():
    print(key, ":", value["isim"], " - ", value["fiyat"], "TL")
sos = int(input("Sos seçin (11-16): "))
while sos not in soslar:
    sos = int(input("Geçersiz seçim. Lütfen Sos Menüsünden bir Sos seçin (11-16): "))

# Toplam Hesaplama
fiyat = menu[pizza]["fiyat"] + soslar[sos]["fiyat"]

# Kredi Kartı Bilgileri
print("Toplam tutar: ", fiyat, "TL")
print("Lütfen ödeme için aşağıdaki kredi kartı bilgilerinizi girin.")

isim = input("Kart Sahibinin Adı: ")
kart_numarası = input("Kredi Kartı Numarası: ")
son_kullanma_tarihi = input("Son Kullanma Tarihi (AA/YY): ")
CVV = input("CVV Kodu: ")

# Sipariş Tamamlandı
print("Siparişiniz başarıyla tamamlandı! Seçtiğiniz pizza {} ve sos {} için toplam tutar {} TL'dir.".format(menu[pizza]["isim"], soslar[sos]["isim"], fiyat))
