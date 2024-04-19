#list programs


	l = [15, 18, 2, 22, 181,2,45]
n = len(l)
target = 2
result = 0

for index in range(n):
    if l[index]==target:
        result = result + 1

print("total no of occurrenceis ",result)


output:
	total no of occurrenceis  2




11.
	def findtotaloccurences(listofnumbers, target):
    result = 0
    n = len(listofnumbers)
    for index in range(n):
        if listofnumbers[index] == target:
            result = result + 1
        return result

listofnumbers = [12,34,21,-12,34,55,56,34,12]
target = 35

result = findtotaloccurrences(list2,target2)
print(result)

output: error

