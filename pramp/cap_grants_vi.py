'''
input:  grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190

2 50 100 120 1000
2 
^ 
190 / 5 = 38.
188/4 = 47.

problem understanding: 5m if you haven't seen it before
    includes examples
    clarifying questions
'''
def find_grants_cap(grantsArray: List[float], newBudget: float) -> float:
    for idx, initgrant in enumerate(grantsArray):
        newBudget -= min(initgrant, (newBudget / (len(grantsArray) - idx)))
    return grantsArray[-1]

