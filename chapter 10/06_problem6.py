from random import randint

class Train:

    def __init__(slf,trainNo):
        slf.trainNo=trainNo

    def Book(Milan,fro,to):
        print(f"Train is book in train no {Milan.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running sucessfully")
    
    def getFare(self,fro,to):
        print(f"Ticket fare no:{self.trainNo} from {fro} to {to} is {randint(1000,9000)}")

t=Train(13999)
t.Book("Pokhara" ,"Kathmandu")
t.getStatus()
t.getFare("Pokhara" ,"Kathmandu")
