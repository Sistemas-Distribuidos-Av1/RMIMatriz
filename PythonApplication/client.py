import Pyro5.api

def main():
    print("Running RMI client...")
    print("\tGetting remote object...")
    calc = Pyro5.api.Proxy("PYRONAME:example.calculator")
    print("test")


if __name__ == "__main__":
    main()