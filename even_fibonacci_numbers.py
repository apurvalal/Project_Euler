def fibonacci(max_number):
    sum_first = 1
    sum_second = 2
    total_sum = 0

    while(sum_first <= max_number):
        
        if(sum_first%2==0):
            total_sum += sum_first
        
        temp = sum_first
        sum_first = sum_second
        sum_second = temp + sum_second

    return total_sum

print(fibonacci(4000000))
