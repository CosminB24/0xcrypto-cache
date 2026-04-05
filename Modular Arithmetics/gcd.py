def gcd(a, b):
    a_list = []
    b_list = []
    for i in range(1, a):
        if a % i == 0:
            a_list.append(i)
    
    for i in range(1, b):
        if b % i == 0:
            b_list.append(i)
    
    greatest_common_divisior = max(set(a_list) & set(b_list))
    print("Greatest Common Divisor is: ", greatest_common_divisior)

b = 5
c = 3

gcd(c + 26513, b + 32321)