# Project Euler
# Problem 10
# https://projecteuler.net/problem=10

#this function determines the number of prime numbers up to N
def findPrimes(N):
	counter = 0;
	for i in range(2, N):
		if (isPrime(i) == True):
			counter = counter + i;
	return counter;

#this function checks if the given integer p is prime number
def isPrime(p):
	check = False;

	if (p==2):
		check = True;
	elif (p %2 == 0 or ((p > 7) and ((p %3 == 0) or (p%5==0) or (p%7==0)))):
		check = False;
	else: 
		for j in range(2, (p+1)/2 + 1):
			if (p %j == 0):
				check = False;
				break;
			else: 
				check = True;
	return check;


N_TEST = input();

for n in range(0,N_TEST):
	N = input();
	print(findPrimes(N+1));
