### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###
def openLocks(number_of_lockers ,number_of_students):
    if number_of_lockers <0 or number_of_students < 0:
        return None
    op=0
    for x in range(1 , number_of_lockers+1):
        c=0
        
        for y in range(1 , number_of_students+1):
            if x%y == 0 :
                c=c+1
                
        if c%2 == 1:
            op = op +1
                   
    return op

#### End OF MARKER

### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###

def mostTouchableLocker(number_of_lockers ,number_of_students):
    if number_of_lockers <0 or number_of_students < 0:
        return None
    
    c=0
    mt=0
    most=0
    for x in range(1 , number_of_lockers+1):     
        c=0
        for y in range(1 , number_of_students+1):
            if x%y == 0 :
                c=c+1            
        if mt <= c:
            mt=c
            if number_of_students != 0:
                most=x
    return most


#### End OF MARKER


