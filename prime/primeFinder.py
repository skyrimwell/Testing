class PrimeChecker:
    def Checker(self, a):
        # Checking that given number is more than 1
        if a > 1:
            # Iterating over the given number with for loop
            for j in range(2, int(a/2) + 1):
                # If the given number is divisible or not
                if (a % j) == 0:
                    print(a, "Не простое число")
                    return 0
            # Else it is a prime number
            else:
                print(a, "Простое число")
                return 1
        # If the given number is 1
        else:
            print(a, "Не простое число")
            return 0


def main():
    print("Добро пожаловать в программу проверки числа на простоту" + "\n" + "")
    a = int(input("Enter an input number:"))
    PrimeChecker.Checker(a)


if __name__ == '__main__':
    main()
# A default function for Prime checking conditions
# Taking an input number from the user

# Printing result
