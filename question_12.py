print("Question 12: 20MIM10056")
str = "My Name Is Sakalya Mitra"

flag = 0
for i in range(len(str)):
    if(i==0):
        if(str[i].isupper()):
            continue
        else:
            flag = 1
            break
    else:
        if(i==len(str)-1):
            continue
        if(str[i-1] == " " and str[i+1]!=" "):
            if(not(str[i].isupper())):
                flag = 1
                break

print("The string is: ", str)
if(flag): print("All words are not starting with capital")
else: print("All words are starting with capital")