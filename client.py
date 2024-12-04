import Pyro4

uri = input("Enter the server URI: ")
greeting = Pyro4.Proxy(uri)
print(greeting.say_hello("John"))
