class a:
    x = 0
    def __init__(self):
        print("cons")
        self.x=3
        print(self.x)

    def hmm(self):
        print(ob.x)
        self.x += 1

    def __del__(self):
        print("destruc")

ob = a()
ob.hmm( )
ob.hmm()
print(ob.x)
ob =0
print(ob)