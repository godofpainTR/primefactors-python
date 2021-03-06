import time
import math


def main(number):
	counter = 0
	primesraw = []
	i = 2

	def elapsedtime(r,x,y):
		if not r:
			elapsed = round(time.process_time(), 2)
		elif r:
			elapsed = round(time.process_time()*((y**0.5)-x)/x, 2)
		if elapsed >= 31536000:
			elapsed = str(round(elapsed/31536000)) + " years 		"
		elif elapsed >= 86400:
			elapsed = str(round(elapsed/86400)) + " days 		"
		elif elapsed >= 3600:
			elapsed = str(math.floor(elapsed/3600))+" hours "+str(round(math.floor((elapsed - math.floor(elapsed/3600)*3600)/60)))+" minutes"
		elif elapsed >= 60:
			elapsed = str(math.floor(elapsed/60))+" minutes "+str(round(elapsed - math.floor(elapsed/60)*60))+" seconds"
		else:
			elapsed = str(elapsed) + " seconds 		"
		return elapsed

	def percgraph(perc):
		scale = 5
		return "*"*int(perc//scale)+"-"*int((100//scale)-(perc//scale))
	while i <= number**0.5:
		if number % i == 0:
			number = int(number//i)
			counter += 1
			primesraw.append(i)
		elif i > 2:
			i += 2
		else:
			i += 1
		percentage = round(i*100/number**0.5, 2)
		if i % 50001 == 0:
			print(f"{percgraph(percentage)} {percentage}% | {elapsedtime(True,i,number)} left", end="\r", flush=True)
	primesraw.append(number)
	counter += 1
	percentage = 100
	print("{}% done in {}.".format(percentage, elapsedtime(False,None,None)), flush=True)
	print(counter, " prime factors")
	primes = list(dict.fromkeys(primesraw))
	for a in primes:
			print("{}^{}".format(a, primesraw.count(a)))


if __name__ == "__main__":
	getnumber = int(input("enter number:"))
	main(getnumber)
