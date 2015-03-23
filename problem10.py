from math import sqrt
N = 2000000
sum_of_primes = 0

def is_prime(x):
	if x < 2:
		return False
		
	for i in range (2, int(sqrt(x)) + 1):
		if x %i == 0:
			return False
	return True

list_of_primes = [x for x in range(N) if is_prime(x)]

for prime in list_of_primes:
	#print prime
	sum_of_primes += prime


print sum_of_primes