def print_msg(msg):
    # This is the outer enclosing function
    print('b4 print_msg')
    def printer():
        # This is the nested function
        foo = 42
        print(foo)
        print(msg)
    print('after print msg')
    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()