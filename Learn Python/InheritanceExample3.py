class One:
        pass
class Two(One):
        pass
obj=Two()
print(isinstance(obj,One))
