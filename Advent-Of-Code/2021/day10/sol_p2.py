def read_file(pathname: str) -> list:
    returnLine = []
    with open(pathname, 'r') as f:  # ✅ Use pathname here
        lines = f.readlines()
    for line in lines:
        returnLine.append(line.strip())
    return returnLine

def syntax_error_score(lines: list) -> int:
    errors = {")": 1, "]": 2, "}": 3, ">": 4}
    opening = {"(": ")", "[": "]", "{": "}", "<": ">"}
    closing = {")": "(", "]": "[", "}": "{", ">": "<"}

    totals = []

    for line in lines:
        total = 0
        stack = []
        corrupted = False

        for char in line:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack or stack[-1] != closing[char]:
                    corrupted = True
                    break
                else:
                    stack.pop()

        if corrupted:
            continue  # skip to next line

        # Line is incomplete (not corrupted), now compute completion score
        missing_closings = []
        while stack:
            a = stack.pop()
            missing_closings.append(opening[a])

        for char in missing_closings:
            total = (total * 5) + errors[char]

        totals.append(total)

    totals.sort()
    return totals[len(totals) // 2]  # Median score

if __name__ == "__main__":
    lines = read_file('input.txt')
    total = syntax_error_score(lines)
    print(total)