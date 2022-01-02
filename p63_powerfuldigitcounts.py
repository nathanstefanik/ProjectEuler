prev = False 
good = True
ans = 0
counter = 1
while(good):
    for i in range(1,10):
        if len(str(i**counter)) == counter:
            ans += 1
            prev = True
        elif len(str(i**counter)) >= counter:
            break
        if i == 9 and prev == False:
            good = False
            break
    counter += 1
    prev = False
print(ans)