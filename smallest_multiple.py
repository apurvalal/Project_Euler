def check_divisible(number):
    for divisor in range(2, 20):
        if (number%divisor==0):
            continue
        else:
            return False
    return True

number=2
flag = True
while(flag):
    if check_divisible(number):
        flag = False
    else:
        number+=1

print(number)