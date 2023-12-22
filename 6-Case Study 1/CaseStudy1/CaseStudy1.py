# region Görev 1
# Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"name": "Jake",
     "Age": 27,
     "Address": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

# Çözüm
type(x)
type(y)
type(z)
type(a)
type(b)
type(c)
type(l)
type(d)
type(t)
type(s)

# endregion
# region Görev 2
# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
text = "The goal is to turn data into information, and information into insight."

# Çözüm
text.upper().replace(",", " ").replace(".", " ").split()

# endregion
# region Görev 3
# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.
lst = ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E']
# Adım 1: Verilen listenin eleman sayısına bakınız.
len(lst)

# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
lst[0:4]

# Adım 4: Sekizinci indeksteki elemanı siliniz.
lst.pop(8)
# Adım 5: Yeni bir eleman ekleyiniz.
lst.append("D")

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz
lst.insert(8, 'N')
# endregion
# region Görev 4
# Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}
# Adım 1: Key değerlerine erişiniz.
dict.keys()

# Adım 2: Value'lara erişiniz.
dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict.get("Daisy")[1] = 13

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({"Ahmet": ["Turkey", 24]})

# Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop('Antonio')

# endregion
# region Görev 5
# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]


def EvenOdd(list):
    odd = []
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd, even


EvenOdd(l)
# endregionr
# region Görev 6
# Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, ogrenci in enumerate(ogrenciler, 1):
    if index < 4:
        print(f"Mühendislik Fakültesi {index}. öğrenci: {ogrenci}")
    else:
        print(f"Tıp Fakültesi {index}. öğrenci: {ogrenci}")

# endregion
# region Görev 7
# Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for i in list(zip(kredi, ders_kodu, kontenjan)):
    print(f"Kredisi {i[0]} olan {i[1]} kodlu dersin kontenjanı {i[2]} kişidir")

# endregion
# region Görev 8
# Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def IsSuperSet(list1, list2):
    if list1.issuperset(list2):
        print(list1.intersection(list2))
    elif list1.issuperset(list2) != True:
        print(list2.difference(list1))


IsSuperSet(kume1, kume2)
# endregion
