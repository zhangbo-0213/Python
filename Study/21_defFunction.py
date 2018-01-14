from random import randint
def isEqual(num1,num2):
    if num1<num2:
        print 'too small'
        return False;
    elif num1>num2:
        print 'too big'
        return False;
    else :
        print 'bingo'
        return True;

num=randint(1,100)
#print(num)
answer=input('Guess what i think?\n')
result=isEqual(answer,num)
while(result!=True):
    answer=input('Guess what i think?\n')
    result=isEqual(answer,num)
