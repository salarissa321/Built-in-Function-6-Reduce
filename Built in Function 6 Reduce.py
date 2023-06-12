

#--------------------------------------------------------------
#------- Built in Function 6 .=> Reduce ---------
#--------------------------------------------------------
# [1] Reduce Take  A Function + iterator
# [2] Reduce run A Function on First And Second Element and Give Result
# [3] Then Run Function on Result and Third Element
# [4] hen Run Function on Result and fourth Elment And so on
# [5] Till One Element is Left and This is The Result of The Reduce 
# [6] The Function Can be Pre-defined Function or Lambda Function
#-----------------------------------------------------------


 # normal function

from functools import reduce


def sumAll(num1 , num2) :

    return num1 + num2 

numbers = [1,8,9,12,100]
result = reduce(sumAll, numbers) 

print(result) # 130

# ((((1+8)+9)+12)+100)

print("-" * 50) # --------------------------------------------------

# function with lambda

from functools import reduce

numbers = [1,8,9,12,100]
result = reduce(lambda num1, num2 : num1 +num2 , numbers) 
print(result) # 130

# ((((1+8)+9)+12)+100)


