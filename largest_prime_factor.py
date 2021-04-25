def largest_prime(given_number):
    
    if(given_number%2==0):
        largest_number = 2
    
    for number in range(3, int(given_number**0.5)+1, 2):
        if(given_number%number==0):
            for number_check in range(3, int(number ** 0.5)+1, 2):
                if(number % number_check==0):
                    break
            else:
                largest_number = number
    return largest_number

print(largest_prime(600851475143))