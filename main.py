import prime
import factorialprime
import sys
if len(sys.argv) == 1:
	print("Press 1 for finding primes of an integer")
	print("Press 2 for finding primes of a factorial")
	choice = int(input("Your choice:"))
	if choice == 1:
		number = int(input("enter number:"))
		prime.main(number)
	elif choice == 2:
		number = int(input("enter number:"))
		factorialprime.main(number)
elif len(sys.argv) == 3:
	choice = int(sys.argv[1])
	if choice == 1:
		prime.main(int(sys.argv[2]))
	elif choice == 2:
		factorialprime.main(int(sys.argv[2]))
else:
	print("Wrong argument count")