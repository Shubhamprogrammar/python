class Electronic_device:
    parts=34
    def ispart(self):
        return f"The total parts are {self.parts}"

class pocket_device(Electronic_device):
    time=7
    def ishrs(self):
        return f"The time is {self.time}"

printer=Electronic_device()
calc=pocket_device()
print(calc.ishrs())
print(printer.ispart())
    
