### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###
def chocolatePrice(ali_budget,bashir_budget):
    if ali_budget > bashir_budget:
        n= bashir_budget
    else :
        n= ali_budget
    i = 1   
    while i<=n:
        if ali_budget%i==0 and bashir_budget%i==0:
            candy_price= i
        i+=1    
    return candy_price
#### End OF MARKER

### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###

def calculateProfit(ali_budget,bashir_budget) :
    if type(ali_budget) == float:
        x =  ali_budget - (ali_budget//1)
        if x>=0.5 :
            ali_budget= (ali_budget//1) +1
            ali_budget = int(ali_budget)
        else :
            ali_budget= (ali_budget//1)
            ali_budget= int(ali_budget)
    if type(bashir_budget) == float:
        x =  bashir_budget - (bashir_budget//1)
        if x>=0.5 :
            bashir_budget = (bashir_budget//1) +1
            bashir_budget = int(bashir_budget)
        else :
            bashir_budget= (bashir_budget//1)
            bashir_budget = int(bashir_budget)
            
    if type(ali_budget) != int or type(bashir_budget) != int  or ali_budget <= 0 or bashir_budget <= 0:
        return "Not Possible"
    else:
        price = chocolatePrice(ali_budget, bashir_budget)
        if ali_budget > bashir_budget:
            pb = 2*price*(bashir_budget/price) - bashir_budget
            pa = 3/2*price*(ali_budget/price) - ali_budget
        else:
            pa = 2*price*(ali_budget/price) - ali_budget
            pb = 3/2*price*(bashir_budget/price) - bashir_budget
        if  pa>pb :  
            return pa
        else:
            return pb

#### End OF MARKER
