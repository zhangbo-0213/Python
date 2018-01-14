from random import choice

'''
print'this is a game ,chose one direction to shoot (left,center,or right)'
yourdirection=raw_input()
direction=['left','center','right']
goal=choice(direction)
print goal
if(goal==yourdirection):
    print 'Oh ,no'
else:
    print 'Yes,Goal'
'''
you_score=0
com_score=0
direction=['left','center','right']

def RoundKickOrSave(str_kickOrSave,num_math):
    global you_score,com_score
    print '=====Round %d:You %s!=====' % (num_math,str_kickOrSave)
    print 'One side to %s:(left,center,right)' % str_kickOrSave
    YouDirection=raw_input()
    print 'Your Direction:%s' % YouDirection
    comDirection=choice(direction)
    print 'Com Direction:%s' % comDirection
    if(str_kickOrSave=='Kick'):
        if YouDirection==comDirection:
            print ('Com Win!')
            com_score+=1
        else :
            print('You Win')
            you_score+=1
    if(str_kickOrSave=='Save'):
        if(YouDirection==comDirection):
            print ('You Win!')
            you_score+=1
        else :
            print('Com Win')
            com_score+=1
    print '=====Round %d Score,You:%d VS Com:%d=====' %(num_math,you_score,com_score)

#RoundKickOrSave('Kick',1)
        
for num in range(0,5):
    RoundKickOrSave('Kick',num+1)
    RoundKickOrSave('Save',num+1)
