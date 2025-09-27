#Demo program for Bubble sort
def bubblesort(arr):
    for i in range(len(arr)):
        swaps = 0
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                swaps = 1
                print(arr)  # show progress after each swap
        if swaps == 0:  # already sorted
            break

def main():
    arr = [11, 2, 4, 1, 44, 41, 99, 121]
    print("Array before Sorting:")
    print(arr)

    bubblesort(arr)

    print("Array after Sorting:")
    print(arr)

if __name__ == "__main__":
    main()