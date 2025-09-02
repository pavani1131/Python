# class calculator:
#     company_name='CASIO'
#     def __init__(self,id1,mnf_date1,mrp_1):
#         self.id=id1
#         self.mnf_date=mnf_date1
#         self.mrp=mrp_1
#         print('An Object is created')

#     def describe(self):
#         print(self.id,self.mnf_date,self.mrp)
# clc1=calculator(2,'2-sep',499)
# clc2=calculator(4,'2-sep',499)
# clc1.describe()
# clc2.describe()
# #  @classmethod
# #      def change_company_name(cls,new_name):
# #     cls.company_name=new_name

# # calculator.change_company_name('New Casio')
# # print("Updated company name",calculator.company_name)

# # #static methods
# # clc1.connect_to_db(1,2)
# # calculator.connect_to_db(2,3)
# @classmethod
# def change_company_name(cls, new_name):
#     cls.company_name = new_name

#     # Static method
#     @staticmethod
#     def connect_to_db(user, password):
#         print(f"Connecting to DB with user={user}, password={password}")


# # Creating objects
# clc1 = calculator(2, '2-sep', 499)
# clc2 = calculator(4, '2-sep', 499)

# # Instance method
# clc1.describe()
# clc2.describe()

# # Class method
# calculator.change_company_name('New Casio')
# print("Updated company name:", calculator.company_name)

# # Static method
# clc1.connect_to_db(1, 2)
# calculator.connect_to_db(2, 3)
class calculator:
    company_name = 'CASIO'   # Class variable

    def __init__(self, id1, mnf_date1, mrp_1):
        self.id = id1
        self.mnf_date = mnf_date1
        self.mrp = mrp_1
        print('An Object is created')

    # Instance method
    def describe(self):
        print(self.id, self.mnf_date, self.mrp)

    # Class method
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

    # Static method
    @staticmethod
    def connect_to_db(user, password):
        print("Connecting to DB with user={user}, password={password}")


# Creating objects
clc1 = calculator(2, '2-sep', 499)
clc2 = calculator(4, '2-sep', 499)

# Instance method
clc1.describe()
clc2.describe()

# Class method
calculator.change_company_name('New Casio')
print("Updated company name:", calculator.company_name)

# Static method
clc1.connect_to_db(1, 2)
calculator.connect_to_db(2, 3)


class Mobile:
    Mobilecompany_name="Vivo"
    def __init__(self,price1,model1,release_date):
        self.price=price1
        self.model=model1
        self.release_date=release_date
        print("An Mobile is Created")
    def describe(self):
        print(self.price,self.model,self.release_date)
    @classmethod
    def changecompany_name(cls,new_name1):
        cls.Mobilecompany_name=new_name1

mob1=Mobile(4000,"S21",'4sep-2000')
mob2=Mobile(5000,"S22","5-sep-2001")

mob1.describe()
mob2.describe()
calculator.change_company_name('Vivo')
print("Updated company name:", Mobile.Mobilecompany_name)
