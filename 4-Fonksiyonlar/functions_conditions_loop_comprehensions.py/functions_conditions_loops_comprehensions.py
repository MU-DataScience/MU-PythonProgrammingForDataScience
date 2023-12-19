##############################################
# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER COMPREHENSIONS
##############################################

# - Fonksiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - Comprehensions

##############################################
# FONKSİYONLAR (FUNCTIONS)
##############################################

#######################
# Fonksiyon Okuryazarlığı
#######################

print('a')
?print

print("a", "b")
print("a", "b", sep="__")
help(print)


#######################
# Fonksiyon Tanımlama
#######################

def calculate(x):
    print(x * 2)


calculate(5)


# İki argümanlı/parametreli bir fonksiyon tanımlayalım.

def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)

summer(8, 7)

summer(arg2=8, arg1=7)


#######################
# Docstring
#######################

def summer(arg1, arg2):
    print(arg1 + arg2)


def summer(arg1, arg2):
    """
    Sum of two numbers
    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int, float
    Examples:

    Notes:
        
    """
    print(arg1 + arg2)

?summer
help(summer)

summer(1, 3)
