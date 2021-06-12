def parent():
    yield f"parent yields {1}"
    # for item in child():
        # yield f"parent yields {item}"
    yield from child()
    yield f"parent yields done"
    
def child():
    yield f"child yields {1}"
    gen = grandchild()
    yield f"child yields {next(gen)}"
    yield "child yields done"
    
def grandchild():
    yield "grand child yields done--1"
    yield "grand child yields done--2"
    
for item in parent():
    print(item)