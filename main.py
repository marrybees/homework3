#homework1
class Celsius:
   def __init__(self,temperature):
       self.temperature = temperature
   def get_temp(self):
       return  self.__temperature
   def set_temp(self, new_temp):
       self.__temerature = new_temp
   def del_temp(self):
       self.__temperature = temperature
   temperature_prop  = property(get_temp, set_temp, del_temp)
gradusi = Celsius(1)
print(gradusi.temperature_prop)
print(gradusi.temperatuture_prop)
gradusi.set_temp()
print(gradusi.set_temp())
print(gradusi.temperature_prop)
gradusi.del_temp()
del gradusi.temperatuture_prop


# homework2
class Bank_account:
    def __init__(self, account_name,balance = 0):
        self.account_name = account_name
        self.__balance = balance
    def get_accountname(self):
        return self.__account_name
    def set_accountname(self, account):
        self.__balance += account
    def __str__(self):
        return f"gamarjoba,{self.account_name}, angarishze gaqvt: {self.__balance}"
    def deposite(self, tanxa):
        self.__balance += tanxa
        print(f"Sheiyvanet tanxa romlis damatebac gsurt")
    def withdraw(self, gamoakldes):
        self.__balance -= gamoakldes
        print( f"თანხის გამოტანა შეუძლებელია ამჟამად ანგარიშზე გაქვთ {self.__balance} თანხა ")
name = Bank_account("mari beselia")
name.deposite(input())
name.withdraw(input())
print(name)

#homework3
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sigrdze(self):
       return math.sqrt(x**2 + y**2)
