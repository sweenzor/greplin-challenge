def fib(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return fib(num-1)+fib(num-2)

def isprime(num):
	for ind in range(2, int((num**0.5)+1)):
		if num % ind == 0:
			return False
	return True

largerthan = 227000
fibindex = 0
currentfib = 0

while True:
	currentfib = fib(fibindex)
	print currentfib, isprime(currentfib)
	if (currentfib > largerthan) & (isprime(currentfib)):
		break
	fibindex = fibindex + 1

x = currentfib+1
print x
sum = 0
for i in range(2,x):
	if isprime(i):
		if x % i == 0:
			print i
			sum = sum + i

print 'sum=',sum