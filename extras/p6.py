word=input("enter a word:")
l=len(word)
c=0
for i in range(0,l):
    for j in range(0,l):
        if(word[j]==word[i]):
                c=c+1
    print('the frequency of', word[i], 'is :', c)


