import Pyro5.api

def rmi():
    print("Running RMI client...")
    print("\tGetting remote object...")
    return Pyro5.api.Proxy("PYRONAME:Matriz")