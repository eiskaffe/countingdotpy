import random
RANDOM_MODE = False
PRINT_TO_FILE = False
DISCORD_NITRO = True

def convert(A: str, length: int = 0) -> str:
    t = str(bin(int(A)))[2:]
    return "0" * (length - len(t)) + t

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
    max_value = 2 ** len(convert(N)) - 1
    if RANDOM_MODE: I = input(f"Give the desired numbers with spaces between! (n <= {max_value})! > ").split()
    else: I = random_integers(int(input(f"Set the number of desired random numbers! (n <= {max_value - 1}) > ")), max_value)

    base = 0
    for mod in I:
        base ^= mod
    difference = base ^ int(N)

    factors = [trial_division(n) for n in I + [difference]]
    factors = [[splitter(f) for f in factor] for factor in factors if factor]

    printed = printing(factors)
    if len(printed) > 2000:
        print("Discord Nitro is required")
    elif len(printed) > 300 and PRINT_TO_FILE:
        with open(f"{N}_{len(factors)}.txt", "a") as outf:
            print(printed, file=outf)
    else:
        print(printed)

            
    input("\nPress enter to exit...")

if __name__ == "__main__":
    main()