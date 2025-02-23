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
add_element(180,10)
