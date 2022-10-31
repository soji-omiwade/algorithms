def go(width, length):
    def square_carpet(width, length):
        nonlocal count
        if length != 0:
            if width < length:
                width, length = length, width
            #now carpet always wider than longer
            count += width // length
            square_carpet(length, width % length)    
    count = 0
    square_carpet(length, width)    
    return count
