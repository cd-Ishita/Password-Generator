a = list(input())
count = 0
for i in range(len(a)):
    if(a[i]==a[len(a)-i-1]):
        count = count + 1

if(count == len(a)/2):
    print("Is a palindrome")
else:
    print("Not a palindrome")