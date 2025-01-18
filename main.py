import matplotlib.pyplot as plt
import math

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes

def goldbach_conjecture(min_val, max_val):
    primes = sieve_of_eratosthenes(max_val)
    prime_set = set(primes)
    even_numbers = range(min_val, max_val + 1, 2)
    results = {}
    for even in even_numbers:
        for prime in primes:
            if prime > even // 2:
                break
            if (even - prime) in prime_set:
                results[even] = (prime, even - prime)
                break
    return results

def draw_graph(results):
    x = list(results.keys())
    y1 = [results[key][0] for key in results]
    y2 = [results[key][1] for key in results]
    plt.scatter(x, y1, label='Prime 1', alpha=0.5)
    plt.scatter(x, y2, label='Prime 2', alpha=0.5)
    plt.xlabel('Even Numbers')
    plt.ylabel('Prime Numbers')
    plt.title('Goldbach Conjecture')
    plt.legend()
    plt.show()

def draw_symmetry_graph(results):
    primes1 = [results[key][0] for key in results]
    primes2 = [results[key][1] for key in results]
    plt.scatter(primes1, [0] * len(primes1), c='blue', alpha=0.5, label='Prime 1')
    plt.scatter([0] * len(primes2), primes2, c='red', alpha=0.5, label='Prime 2')
    for i in range(len(primes1)):
        plt.plot([primes1[i], 0], [0, primes2[i]], 'gray', alpha=0.5)
    plt.xlabel('Prime 1')
    plt.ylabel('Prime 2')
    plt.title('Symmetry of Prime Pairs')
    plt.legend()
    plt.show()

def draw_prime_gaps(results):
    prime_gaps = [results[even][1] - results[even][0] for even in sorted(results.keys())]
    plt.plot(prime_gaps, 'bo-', alpha=0.5)
    plt.xlabel('Index')
    plt.ylabel('Prime Gaps (Prime2 - Prime1)')
    plt.title('Gaps Between Prime Pairs')
    plt.show()
    
if __name__ == "__main__":
    min_val = int(input("Enter the minimum value: "))
    max_val = int(input("Enter the maximum value: "))
    results = goldbach_conjecture(min_val, max_val)
    for even, primes in results.items():
        print(f"{even} = {primes[0]} + {primes[1]}")
    draw_graph(results)
    draw_symmetry_graph(results)
    draw_prime_gaps(results)

    
    