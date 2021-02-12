# def reverse(input_str: str) -> str:
#   Function returns reversed input string
#   >>> reverse("hello") == "olleh"
#   True
#   >>> reverse("o") == "o"
#   True

def reverse(input_str: str) -> str:
    if len(input_str) >= 1:
        print(input_str[::-1])
        return True
    else:
        return False


print(reverse("python"))
print(reverse('o'))
print(reverse(''))
