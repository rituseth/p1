import random 
print('num gussing game')
number=random.randint(1,9)
chances=0
print('guess any num bwt 1 to 9')



while chances<5:
    
    guess=int(input('ek number socho= '))  
    
    if guess==number: 
       print('app jeet gaye!!')
    elif guess>number: 
       print('kaafi kam socha aapne')
    else: 
       print('itna bhi nahi sochna tha')
 