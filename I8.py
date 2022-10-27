## Chinmay D. 10/27/2022 Hg5590
def IssueEight(k):
# Naming and starting the function with a single parameter
    if k == 2: 
        return ": prime"
    if k > 1: 
        for i in range(2, k): 
           if (k % i) == 0: 
               return ": not prime" 
               break
           else: 
               return ": prime" 
    else: 
         return ": not prime"  
num_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# creates and sets a list with the following numbers given in the issues's prompt
for k in num_list :
    print(str(k) + IssueEight(k))
# End of the function and fullfills all the criteria 