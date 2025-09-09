def read_file(pathname:str)->list:
    returnLine = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        returnLine.append(line.strip())
    return returnLine

def syntax_error_score(lines:list)->int:
    '''
    ): 3 points.
    ]: 57 points.
    }: 1197 points.
    >: 25137 points.
    '''
    errors = {")":3, "]":57, "}":1197, ">":25137}
    opening = ("(", "[", "{", "<")
    closing = {")":"(", "]":"[", "}":"{", ">":"<"}

    total = 0
    for line in lines:
        temp = []
        for i in line:
            if i in opening:
                temp.append(i)
            elif i in closing:
                if temp[-1] != closing[i]:
                    total+=errors[i]
                    break
                else:
                    temp.pop()
    return total

if __name__ == "__main__":
    lines = read_file('input.txt')
    #lines = ["<({[})"]
    total = syntax_error_score(lines)
    print(total)
