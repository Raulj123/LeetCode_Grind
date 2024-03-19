num = input("Enter a num: ")

def isPalindrome(num:int) -> bool:
    reverse = str(num)[::-1]       #slice will get nums in reverse order [start: end step]   ONLY WORKS WITH STRINGS, LIST AND TUPLES

    if str(num) == reverse:
        return True
    else:
        return False


anw = isPalindrome(num)
print(anw)