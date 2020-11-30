#!/usr/bin/env python3
import cgi # Модуль для связи скрипта с вэб сервером

# Словарь с древнеегипетскими иероглафами:
# (ключ - разряд числа; 
#  значение - представление числа в формате html кода)
egopet_dictionary={'1':'&#78820;','10':'&#78726;','100':'&#78690;',
                   '1000':'&#78268;','10000':'&#77997;',
                   '100000':'&#78223;','1000000':'&#77928;'}

# Объект для работы с данными html формы:
form = cgi.FieldStorage()

# Число в десятичном формате, переданное из формы ввода в виде строки:
decimal_number_string = form.getfirst("number", "")

# Переводим число в строковом формате в целое:
decimal_number=int(decimal_number_string)

# Вывод заголовка html страницы:
print("Content-type: text/html\n")

print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="cp1251">""")
print("<title>Перевод числа в древнеегипетский формат</title>")
print("""<link href="../style.css" rel="stylesheet" type="text/css"/>
        </head>
        <body>""")

if decimal_number<=9999999: # Числа больще, чем 9 999 999 наш стрипт не обрабатывает
    
# Вывод шапки html страницы:
    print(u"""<div class="inp"> 
        <div class="cap">
            <strong>Перевод числа в древнеегипетский формат:</strong>
        </div>""")
    print("     <strong>Десятичное число: {}</strong> <br /> <br />".format(decimal_number))
    print("     <strong>Древнеегипетское число: </strong> <br /> <br />")
    x=decimal_number
    i=1000000
    while i>0:
        x1=x//i
        if x1>0:
            string_egypet=""
            # В цикле получаем из словаря значения соответствующих представлений иероглифов:
            for j in range(x1):
                string_egypet=string_egypet+egopet_dictionary[str(i)] 
            if string_egypet!="":
                print("""<div class="egypet">""")
                print(format(string_egypet)+"<br />")
                print("</div>")
                x=x-x1*i        
        i=int(i/10)
    print("""</div>""")
else:
    print("""<div class="inp"> 
        <div class="cap">
            <strong>Введенное число больше, чем 9 999 999, расчет невозможен.</strong>
        </div>""")

print("""</body>
</html>""")
