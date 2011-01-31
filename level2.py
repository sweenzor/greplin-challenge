def fib(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return fib(num-1)+fib(num-2)

def isprime(num):
	for i in range(2, int(num**0.5)+1):
		if num % i == 0:
			return False
		return True


largerthan = 10
fibindex = 0
currentfib = 0

while currentfib < largerthan:
	currentfib = fib(fibindex)
	print currentfib, isprime(currentfib)
	fibindex = fibindex + 1
