import random
symbol=['!','@','#','$','%','^','&','*']
wordlist=[]

with open("wikipedia.txt",'r') as file:
    data=file.readlines()

    for line in data:
        word=line.split()

        for item in word:
            if len(item) > 5:
                wordlist.append(item.capitalize())
word=random.choice(wordlist)
schar=random.choice(symbol)
num=str(random.randint(10,99))


passw=word + schar + num 
print(passw)