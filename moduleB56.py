field = [[" "] * 3 for i in range(3)]
def object():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {field [i] [0]} {field [i] [1]} {field [i] [2]}")
def step():
    while True:
        cords = input("Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue
        x, y = cords
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue
        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue
        return x, y
def win():
    win_comb = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_comb:
        symbols = []
        for a in cord:
            symbols.append(field[a[0]][a[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Крестик")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл Нолик")
            return True
    return False

num = 0
while True:
    num += 1
    object()
    if num % 2 == 1:
        print(" Ход крестика")
    else:
        print("Ход нолика")
    x, y = step()
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if win():
        break
    if num == 9:
        print("Ничья")
        break
object()