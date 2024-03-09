
def printName(name):
    print("Hi ",name)


def celToFah(cel):
    fah=(cel*1.8)+32
    return fah


def discriminant(a,b,c):
    d=(b**2)-4*a*c
    return d


def triArea(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c)) ** 0.5  
    return area


def swap(a,b):
    a,b=b,a
    print(a,b)
    


def starPattern(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")




def revStr(str):   
    print(str[::-1])




def vowelCount(word):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    count=0
    for i in word:
        if i in vowels:
            count+=1
    print(count)



def consCount(word):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    count=0
    for i in word:
        if i not in vowels:
            count+=1
    print(count)


def charOccurances(word,character):
    count=0
    for i in word:
        if i==character:
            count+=1
    return count
