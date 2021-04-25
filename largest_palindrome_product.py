def largest_palindrome(given_number):
    palindrome = 0
    
    for number1 in range(given_number, 99, -1):
        for  number2 in range(given_number, 99, -1):
            if (str(number1 * number2)) == str(number1 * number2)[::-1]:
                if((number1*number2)>palindrome):
                    palindrome = number1 * number2
                    
                else:
                    continue
        else:
            continue
        break
    return palindrome

print(largest_palindrome(999))