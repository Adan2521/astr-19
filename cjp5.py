import math

def generate_table():
    
    num_points = 1000
    step = (2 * math.pi) / (num_points - 1)
    table = []

    for i in range(num_points):
        x = i * step
        y = math.sin(x)
        table.append((x, y))

    return table

def main():
    table = generate_table()
    print("x\t\t sin(x)")
    print("-" * 25)
    for x, y in table:
        print(f"{x:.5f}\t {y:.5f}")


if __name__ == "__main__":
    main()
