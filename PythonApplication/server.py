import Pyro5.api
import base

def main():
    print("Running RMI Server...")
    print("\tCreating Pyro5 deamon...")
    deamon = Pyro5.server.Daemon()
    print("\nFinding the Name Server...")
    ns = Pyro5.api.locate_ns()
    uri = deamon.register(base.Matriz)
    print("\tRegistering the object...")
    ns.register("Matriz", uri)
    print("\tWaiting requests...")
    deamon.requestLoop()

if __name__ == "__main__":
    main()

