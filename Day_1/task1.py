"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

def calculate(word):
    for character in word:
        if character in ["1","2","3","4","5","6","7","8","9"]:
            return character


def main():
    calibrations = []
    ans = 0

    with open("input.txt") as my_file:
        for line in my_file:
            calibrations.append(line)

    for word in calibrations:
        a = calculate(word)
        b = calculate(word[::-1])
        number = a+b
        ans += int(number)
    
    return ans


if __name__ == "__main__":
    print(main())