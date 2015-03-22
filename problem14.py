# Project Euler
# Problem 14
# https://projecteuler.net/problem=14


def collatz(N):
	counter = 0;
	LONGEST = 0;
	whoseSequence = 0;

	for m in range (1, N+1):	
		n = m;
		while (n != 1):
			counter = counter + 1;
			if (counter >= LONGEST):
				LONGEST = counter;
				whoseSequence = m;


			if (n %2 == 0):
				n = n/2;
			else: 
				n = 3*n + 1;
		counter = 0;

	return whoseSequence;

N_TEST = input();

for n in range(0, N_TEST):
	N = input();
	print(collatz(N));