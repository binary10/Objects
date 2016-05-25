class Null:
    """ 
    Null objects always and reliably "do nothing." 
    https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch05s24.html
    """

    def __init__(self, *args, **kwargs): pass
    def __call__(self, *args, **kwargs): return self
    def __repr__(self): return "Null(  )"
    def __nonzero__(self): return 0

    def __getattr__(self, name): return self
    def __setattr__(self, name, value): return self
    def __delattr__(self, name): return self

    

"""
def compute(x, y):
    try: "lots of computation here to return some appropriate object"
    except SomeError: return Null(  )

for x in xs:
    for y in ys:
        compute(x, y).somemethod(y, x)
"""