class bob:
    def speak():
        return "bob is speaking"
class dog(bob):
    def talk():
        return "hiee im bob's dog"
obj1=bob   
obj2=dog
print(obj2.speak())
print(obj2.talk())


class mum:
    def daughter():
        return "hie i'm mother "
class father:
    def son():
        return "hieee im father"
class babu(mum,father):
    def neha():
        return "im the only daughter"
obj=babu
print(obj.neha())
 
class keer():
     def moo():
        return "hi"
class sam(keer):
    def moo():
        return "hello"
class enduku(sam):
    def moo():
        return "vanakkam"
obj1=enduku
print(obj1.moo())