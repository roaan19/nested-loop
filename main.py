string=input("enter the word")
char=input("enter the character")
i=0
count=0

while(i<len(string)):
    if (string[i]==char):
        count=count+1
    i=i+1

print("total time your character is occuring  ",count)

#prime number between any range 
lower=int(input("enetr the lower range "))
upper=int(input("enetr the upper range "))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num% i==0:
                break
        else:
            print(num)