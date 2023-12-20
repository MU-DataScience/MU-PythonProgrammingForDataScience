#################################################
# KOŞULLAR (CONDITIONS)
#################################################

# True-False'u hatırlayalım.
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


number_check(10)
number_check(12)


##############################
# else
##############################

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")


number_check(12)


##############################
# elif
##############################

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal 10")


number_check(10)
number_check(12)
number_check(6)

#################################################
# DÖNGÜLER (LOOPS)
#################################################

# for loop

students = ["John", "Mark", "Venessa", "Mariam"]

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

for salary in salaries:
    print(int(salary * 30 / 100 + salary))

for salary in salaries:
    print(int(salary * 50 / 100 + salary))


def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)


new_salary(1500, 10)
new_salary(2000, 20)

for salary in salaries:
    print(new_salary(salary, 10))

for salary in salaries:
    print(new_salary(salary, 20))

salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(new_salary(salary, 15))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))


#######################
# Uygulama - Mülakat Sorusu
#######################

# Amaç : Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

# region Çözümüm
def alternating(string):
    a = 0
    new_text = ""
    for i in string:
        if a % 2 == 0:
            new_text += i.upper()
        else:
            new_text += i.lower()
        a = a + 1
    return new_text


print(alternating("hi my name is john and i am learning python"))
# endregion
# region Hocanın Çözümü
len("miuul")
range(len("miuul"))

for i in range(0, 5):
    print(i)


def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez.
    for string_index in range(len(string)):
        # index çif ise büyük harfe çevir.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # index tek ise küçük harfe çevir.
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("miuul")
# endregion
