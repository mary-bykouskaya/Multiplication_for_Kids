from random import seed, randint

if __name__ == '__main__':
    count = 0
    test_passed = 6
    summary = []
    question_str = ""
    summary_str = ""
    for i in range(10):
        first = randint(1, 10)
        second = randint(1, 10)
        result = first * second
        question_str = f"Q{i+1}: {first} * {second} = ?"
        print(question_str, end=" ")
        try:
            answer = int(input())
            summary_str = f"Student Answer: {answer}"
        except ValueError:
            answer = None
        if (answer == result):
            answer_str = f"Answer: {result}; Status: CORRECT"
            print(summary_str + "; " + answer_str)
            summary_str = str(question_str + "; " + summary_str + "; " + answer_str)
            summary.append(summary_str)
            count += 1
        else:
            answer_str = f"Answer: {result}; Status: WRONG"
            print(summary_str + "; " + answer_str)
            summary_str = str(question_str + "; " + summary_str + "; " + answer_str)
            summary.append(summary_str)
    #print()
    if (count >= test_passed):
        print('\n' + f"Right answer is {count}. " + "Test is passed! Congratulations!!! ")
    else:
        print('\n' + f"Right answer is {count}. " +  "Test is failed!!! ")
    print("*** SUMMARY ***", end='\n')
    for i in range(10):
        print(summary[i], end='\n')
