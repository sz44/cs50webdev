#print all the variations of ABCD
count =0
for a in "ABCD":
    for b in "ABCD":
        if b != a:
            for c in "ABCD":
                if c != a and c != b:
                    for d in "ABCD":
                        if d !=a and d != b and d != c:
                            print(a+b+c+d)
                            count+=1
                            print(count)





