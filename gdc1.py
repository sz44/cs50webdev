def gcd(num1, num2):
    #select the smaller number
    #reduce by 1 untill reach its next factor
    #iterate the larger number
        #reduce by 1 untill reach its next factor
        #if factor of smaller number = factor of larger number
        #break out of both loops and finish
    
    f1 = num2 if num2 < num1 else num1
    while f1 > 0:
        f2 = num1 if num2 < num1 else num2
        if num1 % f1 == 0:
            print('f1: ', f1)
            while f2 > 0:
                if num2 % f2 == 0:
                    print('f2: ', f2)
                    if f1 == f2:
                        break
                f2 -= 1
        if f1 == f2:
            break
        f1 -= 1
    
    print('f1: ', f1, ' f2: ', f2)
                

gcd(25,150)


