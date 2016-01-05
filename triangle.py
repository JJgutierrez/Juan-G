class Triangle():
    def ___init___(self,number,char):
        self.number=0
        self.char=char
        char=int(char)
        
   
    def triangle(self):
        count  = 1
        for i in range(self.number+1):
            for j in range(0, i):
	            print (self.char, end='')
	            count = count + 1
            print()
    def upsidedowntriangle(self):
        for i in range (self.number,0,-1):
            print (self.char*i)
         
t = triangle(4,6)