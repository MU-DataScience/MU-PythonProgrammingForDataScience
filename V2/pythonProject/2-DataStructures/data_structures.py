##########################################################################
# VERİ YAPILARI (DATA STRUCTURES)
##########################################################################
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar(Numbers): int, float, complex
# - Karakter Dizileri(Strings) : str
# - Boolean(TRUE-FALSE): bool
# - Liste(List)
# - Sözlük(Dictionary)
# - Demet(Tuple)
# - Set

###################################################
# Veri Yapılarına Giriş ve Hızlı Özet
###################################################

# Sayılar: integer
x = 46
type(x)

# Sayılar: float
x = 10.3
type(x)

# Sayılar: complex
x = 2j + 1
type(x)

# String
x = "Hello ai era"
type(x)

# Boolean
True
False
type(True)
5 == 4
3 == 2
1 == 1
type(3 == 2)

# Liste
x = ["btc", "eth", "xrp"]
type(x)

# Sözlük (dictionary)
x = {"name": "Peter", "Age": 36}
type(x)

# Tuple
x = ("python", "ml", "ds")
type(x)

# Set
x = {"python", "ml", "ds"}
type(x)

# Not: List, tuple, set ve dictionary veri yapıları aynı zamanda python collections (Arrays) olaarak geçmektedir.

###################################################
# Sayılar (Numbers): int, float, complex
###################################################

a = 5
b = 10.5

a * 3
a / 7
a * b / 10
a ** 2

#######################
# Tipleri Değiştirmek
#######################

int(b)
float(a)

int(a * b / 10)

c = a * b / 10
int(c)

###################################################
# Karakter Dizileri (Strings)
###################################################

print("John")
print('John')

"John"
name = "John"

#######################
# Çok Satırlı Karakter Dizileri
#######################

long_str = """Veri Yapıları: Hızlı Özet,
Sayılar(Numbers) : int, float, complex
Karakter Dizileri(Strings) : str,
List Dictionary, Tuple, Set
Boolean(TRUE-FALSE): bool"""

#######################
# Karakter Dizilerinin Elemanlarına Erişmek
#######################

name
name[0]
name[3]
name[2]

#######################
# Karakter Dizilerinde Slice İşlemi
#######################

name[0:2]

long_str[0:10]

#######################
# String içerisinde Karakter Sorgulamak
#######################

long_str

"veri" in long_str

"Veri" in long_str

"bool" in long_str

###################################################
# String (Karakter Dizisi) Metotları
###################################################

dir(int)
dir(str)

#######################
# len
#######################

name = "john"
type(name)
type(len)

len(name)
len("musauyumaz")
len("miuul")

#######################
# upper() & lower(): küçük-büyük dönüşümleri
#######################

"miuul".upper()
"MIUUL".lower()

# type(upper)
# type(upper())

#######################
# replace: karakter değiştirir
#######################
hi = "Hello Ai Era"
hi.replace("l", "p")

#######################
# split: böler
#######################
"Hello Ai Era".split()

#######################
# strip: kırpar
#######################

" ofofo ".strip()
"ofofo".strip("o")

#######################
# capitalize: ilk harfi büyütür.
#######################

"foo".capitalize()

dir("foo")

"foo".startswith("f")

###################################################
# Liste (List)
###################################################

# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir
# - Kapsayıcıdır.

notes = [1, 2, 3, 4]
type(notes)

names = ["a", "b", "v", "d"]

not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]

not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]

type(not_nam[6])
type(not_nam[6][1])

notes[0] = 99

not_nam[0:4]

#######################
# Liste Metodları (List Methods)
#######################

dir(notes)

#######################
# len: builtin python fonksiyonu, boyut bilgisi
#######################

len(notes)
len(not_nam)

#######################
# append: eleman ekler
#######################

notes
notes.append(100)

#######################
# pop: index'e göre siler
#######################

notes.pop(0)

#######################
# insert: index'e ekler
#######################

notes.insert(2, 99)

