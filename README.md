# countingdotpy
A script that makes the discord counting bot more fun <br>
Made for [this](https://discord.bots.gg/bots/510016054391734273) bot

## Usage:
Using default settings (randomized):
* Step 1: Launching the program with python: `python counting.py`
* Step 2: In the prompt write the next number (that comes in the discord server)
* Step 3: Write in the number of desired random numbers
* **Done**, you are done, copy the output and paste it to the server :)
When using the manual settings write the numbers you would like to appear in the output.

## Example usage
```
Input the the next number! > 18
Set the number of desired random numbers! (n <= 254) > 5

(2*3)^((2*2*3)+1)^2*((2*3)+1)^3*((2*3)+1)^2*2*((2*3)+1)^2*3*((2*2)+1)
```

## How is it working?
The counting discord bot has an [XOR operation](https://stackoverflow.com/questions/14526584/what-does-the-xor-operator-do) labeled with this character: ^. <br>
First, the random numbers are generated (see random_integers function). Next step is making a string of zeroes in the length of the input converted to binary.
Then using the calculate function it calculates the aforementioned XOR operation's output. Then the difference between this binary and the target binary is calculated.
Next step is prime factorization. I used trial division for this. It gives me all factors for a given integers. Next I split the factors to (see splitter function) to
multiplications and additions using a recursive algorithm. This way the only numbers in the output are 1, 2 and 3. The way it works is it looks for the nearest compound
number by removing 1 from it. If it was a prime, than it is guaranteed that it is going to be a compound number. Then on this compound number I also make prime 
factorization then i map every integer of the prime factorization to the splitter function making it recursive. For e.g.:<br>
```
Input: 23
Output: ([2, ([2, ([2, 2], 1)], 1)], 1)
```
The next goal is to print it to the discord server. For this I also used a recursive algorithm which type checks the items recursively in a arbitary deep list. 
And finally, we are done with printing it.
