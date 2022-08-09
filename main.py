import random
import string
# get user input
num = int(input("Number of words to generate: "))
# read word lists
text = input("Sevdiğiniz şeyler")
#read censor list
with open('blacklist.txt','r') as inline:
    censored = inline.read().strip(' \n').split('\n')
# generate usernames
for i in range(num):

    # construct username
    word1 = random.choice(text)
    word2 = random.choice(text)
    #check if word2 is censored
    if (word2 in censored) | (word1 in censored):
        i -=1
        continue
    elif i == -1:
        print("Kötü kelime bulundu")
        break
    word1 =word1.title()
    word2 =word2.title()
    username = '{}{}{}'.format(word1, word2, random.randint(1, 99))

    # success
    print(username)