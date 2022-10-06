import Pyro5.errors
import Pyro5.api

def main():
    #print("Running RMI client...")
    #print("\tGetting remote object...")
    #calc = Pyro5.api.Proxy("PYRONAME:Calculadora")
    uri = input("Type the Pyro uri: ").strip()
    calc = Pyro5.api.Proxy(uri)
    try:
        calc.printar()
    except Exception:
        print(Pyro5.errors.get_pyro_traceback())

if __name__ == "__main__":
    main()