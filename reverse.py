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

def evaluate(expression) -> int:
    print(expression)
    return eval(expression)

A = reversed(input("Adja meg a stringet! > ").split("^"))
B = list(map(evaluate, A))
l = len(convert(B[0]))
current = "0"*l
for mod in map(lambda x: convert(x, l), B):
    current = calculate(current, mod)
print(current)

