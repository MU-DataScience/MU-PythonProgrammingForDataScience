#########################################################################
# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPREHENSIONS
#########################################################################
# - Fonksiyonlar(Functions)
# - Koşullar(Conditions)
# - Döngüler(Loops)
# - Comprehensions

##########################################
# FONKSİYONLAR(FUNCTIONS)
##########################################

#########################
# Fonksiyon Okuryazarlığı
#########################
# Parametre fonksiyon tanımlanması esnasıdan ifade edilen değişkenlerdir. Argüman ise bu fonksiyonlar çağırıldığında bu parametre değerlerine karşılık girilen değerlerdir.


print("a")
# ?print

print("a", "b")
print("a", "b", sep="__")

help(print)


#########################
# Fonksiyon Tanımlama
#########################

def calculate(x):
    print(x * 2)


calculate(5)


# İki argümanlı/parametreli bir fonksiyon tanımlayalım

def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)
summer(8, 7)
summer(arg2=8, arg1=7)


#########################
# Docstring
#########################

def summer(arg1, arg2):
    print(arg1 + arg2)


def summer(arg1, arg2):
    """
    Sum of two numbers
    Args:
        arg1: int,float
        arg2: int,float

    Returns:
            int,float

    Examples:

    Notes:


    """
    print(arg1 + arg2)


summer(1, 3)

help(summer)


##########################################
# Fonksiyonların Statement/Body Bölümü
##########################################

# def function_name(parameters/arguments):
#               statements(function body)

def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")


say_hi("miuul")


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10, 9)

# girilen değerleri bir liste içinde saklayacak fonksiyon

list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 8)
add_element(18, 8)
add_element(180, 10)


##########################################
# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)
##########################################

def divide(a, b):
    print(a / b)


divide(1, 2)


def divide(a, b=1):
    print(a / b)


divide(1)


def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")


say_hi()

##########################################
# Ne Zaman Fonksiyon Yazma İhtiyacımız Olur?
##########################################

# varm, moisture, charge

(56 + 15) / 80
(17 + 45) / 70
(52 + 45) / 80


# DRY

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(98, 12, 78)


##########################################
# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
##########################################

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


# calculate(98, 12, 78) * 10


def calculate(varm, moisture, charge):
    return ((varm + moisture) / charge)


calculate(98, 12, 78) * 10

a = calculate(98, 12, 78)


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = ((varm + moisture) / charge)

    return varm, moisture, charge, output


calculate(98, 12, 78)
type(calculate(98, 12, 78))

varm, moisture, charge, output = calculate(98, 12, 78)


##########################################
# Fonksiyon İçerisinden Fonksiyon Çağırmak
##########################################

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


calculate(90, 12, 12) * 10


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(45, 1)


def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 12)


def all_calculation(varm, moisture, charge, a, p):
    print(calculate(varm, moisture, charge))
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 19, 12)

##########################################
# Local & Global Değişkenler (Local & Global Variables)
##########################################

list_store = [1, 2]


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 9)
