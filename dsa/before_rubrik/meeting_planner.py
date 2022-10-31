'''
10------------50  60--------     
     15----30 80-------      
     
'''
def meeting_planner(slotsA, slotsB, dur):
  def two_slots_agree(top, bot):
    return max(top[0], bot[0]) + dur <= min(top[1], bot[1])
   
  itop = ibot = 0
  while itop < len(slotsA) and ibot < len(slotsB):
    top, bot = slotsA[itop], slotsB[ibot]
    if two_slots_agree(top, bot):
      return [max(top[0], bot[0]), max(top[0], bot[0]) + dur]
    if bot[1] < top[1]:
      ibot += 1
    else:
      itop += 1
  return []  