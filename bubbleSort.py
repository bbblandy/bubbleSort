import random

def bubblesort(numbers):
    for n in range(len(numbers) - 1, 0, -1):
        for i in range(n):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

def main():
    numbers = []
    for i in range(0, 5):
        n = random.randint(1, 30)
        numbers.append(n)

    print("Unsorted list is:")
    print(numbers)
    bubblesort(numbers)
    print("Sorted list is: ")
    print(numbers)

if __name__ == '__main__':
    main()


