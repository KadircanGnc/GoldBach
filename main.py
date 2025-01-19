import matplotlib.pyplot as plt
import math

# Sieve of Eratosthenes to generate prime numbers
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

# Goldbach conjecture calculation
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

# Graph of Goldbach results
def draw_graph(results):
    x = list(results.keys())
    y1 = [results[key][0] for key in results]
    y2 = [results[key][1] for key in results]
    plt.scatter(x, y1, label='Smallest Prime', alpha=0.5)
    plt.scatter(x, y2, label='Largest Prime', alpha=0.5)
    plt.xlabel('Even Numbers')
    plt.ylabel('Prime Numbers')
    plt.title('Goldbach Conjecture')
    plt.legend()
    plt.show()

# Symmetry graph of Goldbach pairs
def draw_symmetry_graph(results):
    primes1 = [results[key][0] for key in results]
    primes2 = [results[key][1] for key in results]
    plt.scatter(primes1, [0] * len(primes1), c='blue', alpha=0.5, label='Smallest Prime')
    plt.scatter([0] * len(primes2), primes2, c='red', alpha=0.5, label='Largest Prime')
    for i in range(len(primes1)):
        plt.plot([primes1[i], 0], [0, primes2[i]], 'gray', alpha=0.5)
    plt.xlabel('Smallest Prime')
    plt.ylabel('Largest Prime')
    plt.title('Symmetry of Prime Pairs')
    plt.legend()
    plt.show()

# Prime gaps graph
def draw_prime_gaps(results):
    prime_gaps = [results[even][1] - results[even][0] for even in sorted(results.keys())]
    plt.plot(prime_gaps, 'bo-', alpha=0.5)
    plt.xlabel('Index')
    plt.ylabel('Prime Gaps (Largest Prime - Smallest Prime)')
    plt.title('Gaps Between Prime Pairs')
    plt.show()

# Goldbach density calculation
def goldbach_density(min_val, max_val):
    n = int(math.sqrt(min_val))
    max_n = int(math.sqrt(max_val))
    sieve_limit = max_val + 1
    primes = sieve_of_eratosthenes(sieve_limit)
    prime_set = set(primes)

    densities = {}
    for i in range(n, max_n):
        start = i**2
        end = (i + 1)**2
        even_numbers = list(range(start + (start % 2), end, 2))
        odd_numbers = list(range(start + (1 - start % 2), end, 2))

        # Count Goldbach pairs
        goldbach_count = 0
        for even in even_numbers:
            for prime in primes:
                if prime > even // 2:
                    break
                if (even - prime) in prime_set:
                    goldbach_count += 1
                    break

        # Calculate densities
        total_even = len(even_numbers)
        total_odd = len(odd_numbers)
        odd_to_even_ratio = total_odd / total_even if total_even > 0 else 0
        goldbach_density = goldbach_count / total_even if total_even > 0 else 0

        densities[i] = (odd_to_even_ratio, goldbach_density)

    return densities

    y = list(probabilities.values())
    plt.plot(x, y, 'ro-', alpha=0.7)
    plt.xlabel('n (Square Range: n^2 to (n+1)^2)')
    plt.ylabel('Probability')
    plt.title('Probability of Even Number Being Sum of Two Primes')
    plt.show()
    
    
def theoretical_density(n):
    """Theoretical density for Goldbach pairs."""
    return (n / math.log(n)) ** 2

def experimental_density(results):
    """Experimental density based on Goldbach pair counts."""
    densities = {}
    for even, pairs in results.items():
        pair_count = len(pairs)  
        densities[even] = pair_count / math.log(even)
    return densities


if __name__ == "__main__":
    min_val = int(input("Enter the minimum value: "))
    max_val = int(input("Enter the maximum value: "))
    results = goldbach_conjecture(min_val, max_val)
    primes = sieve_of_eratosthenes(max_val)
    prime_set = set(primes)

    theorical = {even: theoretical_density(even) for even in results.keys()}
    experimental = experimental_density(results)
    plt.plot(theorical.keys(), theorical.values(), label='Theoretical Density', color='red')
    plt.plot(experimental.keys(), experimental.values(), label='Experimental Density', color='blue', linestyle='dashed')
    plt.xlabel('Even Numbers')
    plt.ylabel('Density')
    plt.title('Theoretical vs Experimental Density of Goldbach Pairs')
    plt.legend()
    plt.show()
    for even, primes in results.items():
        print(f"{even} = {primes[0]} + {primes[1]}")
    draw_graph(results)
    draw_symmetry_graph(results)
    draw_prime_gaps(results)

    
