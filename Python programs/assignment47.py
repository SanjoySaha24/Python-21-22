def find_divisible(start, end):
    return list(filter(lambda x: x % 5 == 0 and x % 7 == 0, range(start, end)))

def divisible():
    start, end = map(int, input("Enter the range: ").split())
    print("All divisible numbers are : ",find_divisible(start, end))

divisible()