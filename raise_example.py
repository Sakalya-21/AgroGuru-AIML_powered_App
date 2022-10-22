n = int(input("Enter number of numbers to enter:"))
ans = 0

for i in range(n):
	x = int(input("Enter Number:"))
	if x < 0:
  		raise Exception("Negative Numbers not allowed")
	else:
		ans += x
print(ans)