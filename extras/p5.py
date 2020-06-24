word=input("enter a word:")
l=len(word)
for i in range(0,l):
    print('the frequency of',word[i] ,'is :',word.count(word[i]))