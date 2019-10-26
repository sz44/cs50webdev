val = 20
root = 1.0
diff = val - root*root

while diff > 0.00000001 or diff < -0.00000001:
    print(root, 'squared is ', root*root, ' diff is ', diff)
    root = (root + val/root)/2
    
    #print(diff)
    diff = val - root*root


print('the square root of ',val, ' is ', root)