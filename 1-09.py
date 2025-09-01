class calculator:
    def add (self,a,b):
        print(a+b)
    def sub (self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        # print(self.id,self.manf_date)
        print(a/b)
    def floor_divi(self,a,b):
        print(a//b)
    def describe(self):
        print(self.id,self.manf_date,self.color,self.discount)
    


clc1=calculator()
clc2=calculator()

clc1.add(4,5)
clc2.sub(5,4)

# clc1.id=45
# clc1.manf_date='1-sept'
# clc1.model_num = 'ABC123'
# clc1.made_in = 'India'
# clc2.color = 'Black'
# clc2.discount = '10%'
# print(clc1.id)
# print(clc1.manf_date)
# clc1.describe()
# print(clc1.model_num)
# print(clc1.made_in)
# print(clc2.color)
# print(clc2.discount)
# clc2.describe()
clc1.id = 45
clc1.manf_date = "1-sept"
clc1.model_num = "ABC123"
clc1.made_in = "India"
clc1.color = "N/A"       
clc1.discount = "N/A"    

clc2.id = "N/A"          
clc2.manf_date = "N/A"   
clc2.model_num = "N/A"  
clc2.made_in = "N/A"     
clc2.color = "Black"
clc2.discount = "10%"
clc1.describe()
clc2.describe()