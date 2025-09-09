'''
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''

def orderSort(s:str) -> str:
    string = s.split(" ")
    correctstr = [""]*len(string)
    
    for word in string:
        for char in word:
            if ord('0')<=ord(char)<=ord('9'): #or char.isdigit()
                correctstr[int(char)-1] = word
    
    return " ".join(correctstr)


def main():
    print(orderSort("4of Fo1r pe6ople g3ood th5e the2"))

if __name__ == "__main__":
    main()


'''
another solution

def extract_position(word):
    for c in word:
        if c.isdigit():
            return int(c)
    return -1  # Fallback, shouldn't happen as per problem statement

def order(sentence):
    if not sentence:
        return ""

    words = sentence.split()
    sorted_words = sorted(words, key=extract_position)
    return " ".join(sorted_words)

By default, sorted() compares the elements directly. But when you use key=..., you're saying:

“Don’t sort by the element itself — instead, 
sort by the result of applying this function to the element.”

'''
