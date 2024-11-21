
print("============= Binomial Distribution Program =============")


# Factorial Function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Combination function 

def combination (n,r) :
    if n > r :
        nr = n - r
        return factorial(n)/(factorial(r)*factorial(nr))
    else :
        print("n must bigger than r")


# Binomial Distribution based on user input 

while True: 

    n = int(input("n (number of trials): "))
    x = int(input("x (number of successes): "))
    p = float(input("p (probability of success): "))
    q = 1 - p 


    if n < 0 or x < 0 or x > n:
        print("Error: Ensure that n >= 0, x >= 0, and x <= n.")
        exit()

    if p < 0 or p > 1:
        print("Error: Probability p must be between 0 and 1.")
        exit()


# Formula 

    binom_dist = combination(n,x) * (p**x) * (q**(n-x))

    print(f"Result (decimal): {binom_dist:.4f}")
    print(f"Result (percentage): {binom_dist * 100:.2f}%")


    repeat = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if repeat != "yes":
        print("Thank you for using the Binomial Distribution Program!")
        break



    





 