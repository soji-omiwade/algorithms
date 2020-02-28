class NonSearchBT:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

tree=NonSearchBT(
        2,
        NonSearchBT(1,None,None),
        NonSearchBT(3,NonSearchBT(5,None,None),None)
     )
assert tree.value==2
assert tree.left.value==1
assert tree.left.right is tree.right.right is None
assert tree.right.value==3
assert tree.right.left.value == 5