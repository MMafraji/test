
#Q3/write a function that count how many the given character repeated in a given string?
#Ans
def fcount(word):
    ch={}
    for x in word:
        if x in ch:
            ch[x]+=1
        else:
            ch[x]=1
    return ch
word = 'Artificial Intelligence'
vh = fcount(word)
for x,count in fcount('Artificial Intelligence').items():
    print(f'{x}:{count}')