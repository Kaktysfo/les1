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
