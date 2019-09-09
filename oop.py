class partyanimal:
    x=0
    name=''
    def __init__(self,nam):
        self.name=nam
        print('constructed')
    def party(self):
        self.x=self.x+1
        print(self.x,'so far')
    def __del__(self):
        print('destructed')

an=partyanimal('john')
# object constructed with this line without printing anything
bn=partyanimal('sally')
an.party()
bn.party()
an.party()
an=24
print(an)
print(bn)
