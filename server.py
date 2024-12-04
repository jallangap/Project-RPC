import Pyro4

@Pyro4.expose
class Greeting:
    def say_hello(self, name):
        return f"Hello, {name}!"

daemon = Pyro4.Daemon()
uri = daemon.register(Greeting)
print(f"Server URI: {uri}")
daemon.requestLoop()
