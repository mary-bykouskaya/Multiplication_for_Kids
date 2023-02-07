from random import seed, randint

if __name__ == '__main__':
    count = 0
    test_passed = 8
    for i in range(10):
        first = randint(1, 10)
        second = randint(1, 10)
        result = first * second
        print(f"Question: {first} * {second} = ? ", end="")
        try:
            answer = int(input())
        except ValueError:
            answer = None
        if (answer == result):
            print("Right!")
            count += 1
        else:
            print(f"Wrong! The right answer is {result}")
    print(f"Right answer is {count}")
    if (count >= test_passed):
        print("Test is passed! Congratulations!!! ")
    else:
        print("Test is failed!!! ")