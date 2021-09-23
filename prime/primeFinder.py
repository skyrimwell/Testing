class PrimeChecker:
    def checker(self, a):
        if a <= 0:
            return -1
        if a > 1:
            for j in range(2, int(a/2) + 1):
                if (a % j) == 0:
                    return 0
            else:
                return 1
        else:
            return 0

def main():
    print("Добро пожаловать в программу проверки числа на простоту" + "\n" + "")
    a = int(input("Enter an input number:"))
    pc = PrimeChecker()
    if pc.checker(a) == 1:
        print(str(a) + "- простое число")

if __name__ == '__main__':
    main()

