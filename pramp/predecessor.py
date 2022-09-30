  def iterative_find_largest_smaller_key(self, num):
    best  = -1
    node = self.root
    while node:
      if node.key >= num:
        node = node.left
      else:
        best = node.key
        node = node.right
    return best
  
  def recursive_find_largest_smaller_key(self, num):
    def helper(best, node):
      if not node:
        return best
      if node.key >= num:
        return helper(best, node.left)
      else:      
        return helper(node.key, node.right)
    best = helper(-1, self.root)
    return best

