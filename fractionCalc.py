#Fraction Calculator
#9/11/18
#James Baker
#Home Project
	
def getInput():
	cmd = raw_input("Enter an equation (Type 'q' to quit): ")
	pieces = cmd.split(" ")
	return pieces

def parse(parts):
	operands = []
	operators = []
	for i in range(0, len(parts)):
		if i % 2 == 0:
			operands.append(parts[i])
		else:
			operators.append(parts[i])
	return operands, operators

def splitFraction(fraction):
	nums = fraction.split("/")
	return int(nums[0]), int(nums[1])

def calculate(op, n1, d1, n2, d2):
	#Pick function based on operator
	if op == '+':
		resultN,resultD = add(n1, d1, n2, d2)
	elif op == '-':
		resultN,resultD = subtract(n1, d1, n2, d2)
	elif op == "*":
		resultN,resultD = multiply(n1, d1, n2, d2)
	elif op == "/":
		resultN,resultD = divide(n1, d1, n2, d2)
	else:
		print "Invalid operator: ", op	
		return
	#Simplify and print
	resultN,resultD = simplify(resultN, resultD)
	printResult(resultN, resultD)

def add(n1, d1, n2, d2):
	denom = d1
	if d1 != d2:
		n1 = n1 * d2
		n2 = n2 * d1
		denom = d1 * d2
	sumN = n1 + n2	
	return sumN, denom

def subtract(n1, d1, n2, d2):
	diffN, denom = add(n1, d1, -n2, d2)
	return diffN, denom

def multiply(n1, d1, n2, d2):
	numN = n1 * n2
	denomN = d1 * d2
	return numN, denomN

def divide(n1, d1, n2, d2):
	numN = n1 * d2
	denomN = d1 * n2
	return numN, denomN

def simplify(num, denom):
	if (denom % num == 0) or (num != 1):
		gcd = GCD(num, denom)
		#GCD must be positive
		if num < 0:
			gcd = -gcd
		num = num / gcd
		denom = denom / gcd
	return num, denom

def GCD(a, b):
	if a == 0:
		return b
	return GCD(b % a, a)

def LCD(a, b):
	return (a * b) / GCD(a, b)

def printResult(num, denom):
	print "Your answer is: " + str(num) + "/" + str(denom) + "\n"

def main():
	print "This is a fraction calculator."
	print "Fractions should be written in the form a/b. Use spaces between operator."
	parts = ""
	while(True):
		parts = getInput()
		if "q" in parts:
			break
		operands,operators = parse(parts)

		n1,d1 = splitFraction(operands[0])
		n2,d2 = splitFraction(operands[1])
		calculate(operators[0],n1,d1,n2,d2)
	
main()