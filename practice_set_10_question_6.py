from random import randint
class train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo
    def book(shiv,fro,to):
        print(f"Ticket is booked in train No: {shiv.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train  no: {self.trainNo} is running on time .")
    def getFare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is: {randint(220,5500)}")     

t=train(12340)
t.book("Pune","Kolhapur")
t.getStatus()
t.getFare("Pune","Kolhapur")