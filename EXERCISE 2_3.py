# 1*1 + 3*3* + 5*5 . . .+2021*2021
# n*n+(n+2)*(n+2)+...

# Function to calculate sum of series.
def sumOfSeries(n):
	sum = 0;
	i = 1;
	while i<=n:
		sum = sum + i * i
		i = i + 2
	return sum

# Driver code
n = 2021
print(sumOfSeries(n))


