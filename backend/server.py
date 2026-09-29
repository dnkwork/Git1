def calculate_bmi():
    print("=== Калькулятор ИМТ ===")
    weight = float(input("Введите ваш вес (кг): "))
    height = float(input("Введите ваш рост (метры, например 1.75): "))
    
    bmi = weight / (height ** 2)
    print(f"Ваш индекс массы тела: {bmi:.2f}")
    
    if bmi < 18.5:
        print("Статус: Дефицит массы тела")
    elif 18.5 <= bmi < 25:
        print("Статус: Нормальный вес")
    else:
        print("Статус: Избыточный вес")

if __name__ == "__main__":
    calculate_bmi()
