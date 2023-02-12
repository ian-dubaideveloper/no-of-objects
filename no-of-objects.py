class  NoOfObjects:
    count = 0
    def __init__(self):
        NoOfObjects.count += 1
    def display(self):
        print("No of objects created:",NoOfObjects.count)


obj1 = NoOfObjects()
obj2 = NoOfObjects()
obj3 = NoOfObjects()
obj4 = NoOfObjects()

obj5  = NoOfObjects()

