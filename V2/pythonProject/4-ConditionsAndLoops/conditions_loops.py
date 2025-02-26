###################################################
# KOŞULLAR (CONDITIONS)
###################################################

# True-False'u hatırlayalım
1 == 1
1 == 2

# if
if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

number = 11
if number == 10:
    print("number is 10")

number = 10
number = 20


def number_check(number):
    if number == 10:
        print("number is 10")


number_check(12)


#########################################
# else
#########################################

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")


number_check(12)


#########################################
# elif
#########################################

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")


number_check(10)
number_check(12)
number_check(6)

###################################################
# DÖNGÜLER (LOOPS)
###################################################

# for loop

students = ["John", "Mark", "Vanessa", "Mariam"]
students[0]
students[1]
students[2]

for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary * 20 / 100 + salary))


def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)


new_salary(1500, 10)
new_salary(2000, 20)

for salary in salaries:
    print(new_salary(salary, 10))

salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(new_salary(salary, 15))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))

#######################################
# Uygulama - Mülakat Sorusu
#######################################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

# region My Answer
text = "hi my name is john and i am learning python"
new_text = ""

i = 0
for char in "hi my name is john and i am learning python":
    if (i % 2 == 0):
        new_text += char.upper()
    else:
        new_text += char

    i = i + 1

print(new_text)

# endregion

range(len("miuul"))
range(0, 5)

for i in range(0, 5):
    print(i)

for i in range(len("miuul")):
    print(i)


# region Answer
def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez.
    for string_index in range(len(string)):
        # index çift ise büyük harfe çevir.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # index tek ise küçük harfe çevir.
        else:
            new_string += string[string_index].lower()
    print(new_string)


alternating("miuul")
alternating("hi my name is john and i am learning python")

# endregion

#######################################
# break & continue & while
#######################################

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)

for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

# while
number = 1
while number < 5:
    print(number)
    number += 1

#######################################
# Enumerate: Otomatik Counter/Indexer ile for loop
#######################################

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

for index, student in enumerate(students, 1):
    print(index, student)

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

#######################################
# Uygulama - Mülakat Sorusu
#######################################
# divide_students fonksiyonu yazınız.
# Çift index'te yer alan öğrencileri bir listeye alınız
# Tek indexte yer alan öğrencileri bir listeye alınız.
# Fakat b iki liste tek bir liste olarak return olsun

# region My Answer
students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(students):
    a = []
    b = []
    c = []
    for index, student in enumerate(students):
        if index % 2 == 0:
            a.append(student)
        else:
            b.append(student)

    c.append(a)
    c.append(b)
    return c


divide_students(students)
# endregion
# region Answer
students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)

    return groups


st = divide_students(students)
st[0]
st[1]


# endregion


#######################################
# alternating fonksiyonunun enumerate ile yazılması
#######################################
# "hi my name is john and i am learning python"

def alternating_with_enumarate(string):
    new_str = ""
    for index, char in enumerate(string):
        if index % 2 == 0:
            new_str += char.upper()
        else:
            new_str += char.lower()

    print(new_str)


alternating_with_enumarate("hi my name is john and i am learning python")
