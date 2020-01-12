str_=input('Введите слово: ')
print(str_[2].lower())

str_2=input('Введите второе слово: ')
print(str_2[1].lower())
print(str_2[-1].lower())

str_3= input('Введите третье слово: ')
print(str_3[:6].lower())

str_4 = input('Введите четвертое слово: ')
print(str_4[:-2].lower())

def string(str):
    result = ''
    for i in range(len(str)):
        if i % 2 != 0:
            result = result + str[i]
    return result
print(string('python'))

def string(str):
    result = ''
    for index in range(len(str)):
        if index % 2 == 0:
            result = result + str[index]
    return result
print(string('python'))

str_7 = input('Введите седьмое слово: ')
print(str_7[::-1].lower())

str_8 = input('Введите восьмое слово: ')
print(str_8[::-2].lower())

str_9 = input('Введите девятое слово: ')
print(len(str_9))