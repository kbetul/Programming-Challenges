
def readFile(filepath: str) -> list[str]:
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return lines

def checkSafety(line: list[str]) -> bool:
    differences = []
    for num in range(len(line)-1):
        differences.append(int(line[num])-int(line[num+1]))
    
    check = True
    for i in differences:
        


def main():
    lines = readFile("./input.txt")
    print(lines)

if __name__ == "__main__":
    main()
    