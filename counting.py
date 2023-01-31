import random
RANDOM_OR_MANUAL = 0 
# 0 for random, 1 for manual

def convert(A: str, length: int = 0) -> str:
    t = str(bin(int(A)))[2:]
    return "0" * (length - len(t)) + t

def XOR(a: int, b: int) -> bool:
    return a + b - 2 * a * b
    
def calculate(A: str, B: str) -> str:
    # Analytical representation of the XOR gate:
    # f(a, b) = |a - b|
    returning = ""
    for a, b in zip(A, B, strict=True):
        if XOR(int(A), int(B)): returning += "1"
        else: returning += "0"
    return returning 

def bin_to_str(A: str) -> str:
    L = len(A)
    c = 0
    for i, a in enumerate(A):
        if int(a): c += 2 ** (L - i - 1)
    return c

def is_prime(n: int) -> bool:
    if n <= 3: return n > 1
    if n % 2 == 0 or n % 3 == 0: return False
    limit = int(n**0.5)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def trial_division(n: int) -> list[int]:
    factors = []
    f = 2
    if n == 1: return [1]         
    while n > 1:       
        if n % f == 0: 
            factors.append(f)
            n //= f    
        else: f += 1
    # Only odd number is possible
    return factors

def splitter(n: int):
    if n <= 3: return n
    k = 1 if is_prime(n) else 0
    factors = list(map(splitter, trial_division(n - k)))
    return factors, 1

def printing(a: list) -> str:
    string = [printing_recurse(x) for x in a]
    return "^".join(string)

def printing_recurse(a) -> str:
    # [[2, ([2, 2], 1)], [2, 3]]  ---->  2*((2*2)+1)*(2*3)
    if isinstance(a, list) and all([isinstance(x, int) for x in a]):
        return f"({'*'.join(map(str, a))})"
    elif isinstance(a, tuple):
        list_part, integer_part = a
        return f"({printing_recurse(list_part)}+{integer_part})"
    elif isinstance(a, list):
        lst = [printing_recurse(x) for x in a]
        return "*".join(lst)
    elif isinstance(a, int):
        return str(a)

def random_integers(N: int, b: int) -> list[int]:
    L = []
    if N > b: raise ValueError("N can not be larger than b")
    while len(L) < N:
        if (a := random.randint(1, b)) not in L: L.append(a)
    return L

def main() -> None:
    N = input("Input the the next number! > ")
    TARGET = convert(N)
    l = len(TARGET)
    I = []
    max_value = 2 ** l - 1
    if RANDOM_OR_MANUAL: I = input(f"Give the desired numbers with spaces between! (n <= {max_value})! > ").split()
    else: I = random_integers(int(input(f"Set the number of desired random numbers! (n <= {max_value - 1}) > ")), max_value)

    current = "0"*l
    for mod in map(lambda x: convert(x, l), I):
        current = calculate(current, mod)
        
    difference = calculate(TARGET, current)
    I += [int(bin_to_str(difference))]
    factors = [trial_division(int(n)) for n in sorted(I)]
    factors = [[splitter(f) for f in factor] for factor in factors if factor]

    printed = printing(factors)
    if len(printed) > 300:
        with open(f"{N}_{len(factors)}.txt", "a") as outf:
            print(printed, file=outf)
    else:
        print(printed)
    # print(printed.replace("*", "\\*"))
            
    input("\nPress enter to exit...")

if __name__ == "__main__":
    main()