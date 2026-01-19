class parent(object):
    def overide(self):
        print('parent_overide()')
    def implicit(self):
        print('other_implicit()')
    def altered(self):
        print('other_altered')

class child(object):
    def __init__(self):
        self.parent = parent()
    def implicit(self):
        self.parent.implicit()
    def overide(self):
        print('before_parent_overide()')
        self.parent.overide()    
    

child().implicit()