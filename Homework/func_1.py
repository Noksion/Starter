# Написать вечный цикл, внутри котого у пользователя запрашивается строка.
# Специальная функция должна проверить, есть ли в веденной пользователем строке цифры
# Если есть, выходить из программы.


def dig_check(string):
    for i in string:
        if i.isdigit():
            return False
    return True


while True:
    msg = input(" Please enter the message." +
                "\n Note that entering a number in your message" +
                " will stop the program: ")
    if not dig_check(msg):
        break
    print(msg)
