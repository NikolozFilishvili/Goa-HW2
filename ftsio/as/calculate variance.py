def variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((number - mean) **2 for number in numbers) / len(numbers)

print(variance([2,4,5,6]))
