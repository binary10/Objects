class Null:
    """ 
    Null objects always and reliably "do nothing." 
    https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch05s24.html
    """

    def _ _init_ _(self, *args, **kwargs): pass
    def _ _call_ _(self, *args, **kwargs): return self
    def _ _repr_ _(self): return "Null(  )"
    def _ _nonzero_ _(self): return 0

    def _ _getattr_ _(self, name): return self
    def _ _setattr_ _(self, name, value): return self
    def _ _delattr_ _(self, name): return self

    

"""
def compute(x, y):
    try: "lots of computation here to return some appropriate object"
    except SomeError: return Null(  )

for x in xs:
    for y in ys:
        compute(x, y).somemethod(y, x)
"""