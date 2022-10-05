import Pyro5.api

@Pyro5.api.expose
class Calculator(object):
    def test(text):
        return text + " ok"
   

def main():
    print("Running RMI Server...")
    print("\tCreating Pyro5 deamon...")
    deamon = Pyro5.server.Daemon()
    print("\nFinding the Name Server...")
    ns = Pyro5.api.locate_ns()
    uri = deamon.register(Calculator)
    print("\tRegistering the object...")
    ns.register("example.calculator", uri)
    print("\tWaiting requests...")
    deamon.requestLoop()

if __name__ == "__main__":
    main()

