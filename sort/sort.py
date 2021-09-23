class InsertionSort:
    def sort(self, arr):
        for i in range(len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr




def main():
    insSort = InsertionSort()
    arr = []

    n = int(input("Введите размер массива: "))

    for i in range(n):
        arr.append(int(input(f"Введите элемент массива №{i}: ")))

    print("\nВведенный массив: ")
    print(arr)

    insSort.sort(arr)

    print ("\nРезультат сортировки:")
    print(arr)


if __name__=='__main__':
    main()