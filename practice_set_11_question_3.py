class emp:
    sal=235
    inc=20

    @property
    def SalaryAfterIncrement(self):
        return (self.sal+self.sal*(self.inc/100))
    
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self,sal):
        self.inc=((sal/self.sal)-1)*100

e=emp()
print(e.SalaryAfterIncrement)
e.SalaryAfterIncrement=282
print(e.inc)        