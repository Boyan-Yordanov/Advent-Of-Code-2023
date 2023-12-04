"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

def calculate(word):
    for character in word:
        if character in ["1","2","3","4","5","6","7","8","9"]:
            return character

def swap(word):
    return word.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")


def main():
    calibrations = []
    ans = 0

    with open("input.txt") as my_file:
        for line in my_file:
            calibrations.append(line)

    for word in calibrations:
        word = swap(word)
        a = calculate(word)
        b = calculate(word[::-1])
        number = a+b
        ans += int(number)
    
    return ans


if __name__ == "__main__":
    print(main())
