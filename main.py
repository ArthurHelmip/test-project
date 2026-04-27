def main():
    print("Hello from test-project!")

vector = [100,13,21,5,6,4]

def sum(vetorzin):
    soma = 0
    for k in range(1, len(vetorzin)):
        soma += vetorzin[k]
    return soma


if __name__ == "__main__":
    print(sum(vector))
    print(len(vector))    
    main()
