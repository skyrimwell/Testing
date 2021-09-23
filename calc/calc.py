class Calculator:
    def add(self, num1: int, num2: int) -> int:
        return num1 + num2

    def subtract(self, num1: int, num2: int) -> int:
        return num1 - num2
  
    def multiply(self, num1: int, num2: int) -> int:
        return num1 * num2
    
    def divide(self, num1: int, num2: int) -> int:
        return num1 / num2

  
def main():
    calc = Calculator()
  
    select = int(input("Please select operation -\n" \
            "1. Add\n" \
            "2. Subtract\n" \
            "3. Multiply\n" \
            "4. Divide\n \
            Select operations form 1, 2, 3, 4: "))
    
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    
    if select == 1:
        print(number_1, "+", number_2, "=",
                        calc.add(number_1, number_2))
    
    elif select == 2:
        print(number_1, "-", number_2, "=",
                        calc.subtract(number_1, number_2))
    
    elif select == 3:
        print(number_1, "*", number_2, "=",
                        calc.multiply(number_1, number_2))
    
    elif select == 4:
        print(number_1, "/", number_2, "=",
                        calc.divide(number_1, number_2))
    else:
        print("Invalid input")

if __name__=='__main__':
    main()
