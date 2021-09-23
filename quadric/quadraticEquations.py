import math

class QuadraticEquations:
    def solve(self, a, b, c):
        dis_form = b * b - 4 * a * c
        sqrt_val = math.sqrt(abs(dis_form))

        if (a == 0):
            return[-1, -1, -1]
        elif (dis_form > 0):
            return [(-b + sqrt_val) / (2 * a), (-b - sqrt_val) / (2 * a), 1]
        elif (dis_form == 0):
            return [(-b / (2 * a)), 0]
        else:
            return [f"{- b / (2 * a)}+i {sqrt_val}", f"{- b / (2 * a)}-i {sqrt_val}", -1]


def main():
    qe = QuadraticEquations().solve(int(input("Введите значение коэф. А: ")), int(input("Введите значение коэф. B: ")), int(input("Введите значение коэф. C: ")))

    if (qe == [-1, -1, -1]):
        print("Коэффициент А не может равняться нулю!")
        return
    elif (qe[2] == 1):
        print("Корни уравнения разные.")
    elif (qe[2] == 0):
        print("Корни уравнения равны.")
    else:
        print("Комплексные корни.")

    print(f"Первый корень = {qe[0]}")
    print(f"Второй корень = {qe[1]}")
    print(qe)


if __name__=='__main__':
    main()