'''
2 50 100 120 1000
2
190-- 188
cg = 47
'''
def find_grants_cap(grantsArray, newBudget):
  currentgrant = None
  for idx, initgrant in enumerate(sorted(grantsArray)):
    currentgrant = newBudget / float(len(grantsArray) - idx)
    if initgrant > currentgrant:
      break
    newBudget -= initgrant
  return currentgrant
  
grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190
print(find_grants_cap(grantsArray, newBudget))
