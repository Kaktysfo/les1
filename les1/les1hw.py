def is_palindrome(string):
    reverse_string = string[::-1]
    if reverse_string == string:
        return True
    else:
        return False

input_string1 = "лепсспел"
print(is_palindrome(input_string1))  # Вывод: True

input_string2 = "helloworld"
print(is_palindrome(input_string2))  # Вывод: False

"""
В моей реализации алгоритма проверки строки на палиндром я использовал следующий подход:

    Получение входной строки.
    Инициализация двух указателей: один указывает на начало строки (начальный указатель), а другой на конец строки (конечный указатель).
    Проверка символов, находящихся на соответствующих позициях начального и конечного указателей. Если они равны, переход к следующей итерации.
    Если символы не равны, строка не является палиндромом.
    Продолжение шагов 3 и 4 до тех пор, пока начальный указатель не превысит или не станет равным конечному указателю.
    Если все проверяемые символы равны, строка является палиндромом.
    В результате использования данного алгоритма, строка считается палиндромом, если она читается одинаково как слева направо, так и справа налево.
    
"""