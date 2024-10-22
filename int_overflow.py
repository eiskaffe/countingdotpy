def calc(N) -> str:
    # N = int(input("Adja meg a következő számot!"))
    s = str(N) + "."
    i = 0
    while True:
        if int(float(s + "9")) != N:
            return i
        s += "9"
        i += 1
    
import math
def main():
    print(f"f({0}) = {calc(0)}; log{0} = UNDEFINED")
    for n in range(1, 2**64): 
        print(f"f({n}) = {calc(n)}; log({n}) = {math.floor(math.log2(n))}")
    
if __name__ == "__main__":
    main()