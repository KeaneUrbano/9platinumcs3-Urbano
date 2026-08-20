## Requirements
1. Ask the user to enter a year of birth.  The baseline year 1900.
2. Validate user input that it should not be earlier than 1900.
3.  If the user enters an invalid year then display an appropriate message then stop or abort the program.
4. Otherwise determine the chinese zodiac sign based on the following starting from 1900.  Note: A zodiac sign will recur after each 12 years.

## Python Source Code ('zodiacPlatinumUrbano.py')

def chinese_zodiac(a, b):
    c = 0
    c = (b - 1900) % 12
    print("Your Zodiac sign is:", a[c])

X = int(input("Enter your birth year(must be above or equal to 1900): "))
if X < 1900:
    print("Error: Age entered is below 1900,", X ,"is not a valid input.")
elif X >= 1900:

    zodiacs = ['Rat (鼠 / Shǔ)',
    'Ox (牛 / Niú)',
    'Tiger (虎 / Hǔ)',
    'Rabbit (兔 / Tù)',
    'Dragon (龙 / Lóng)',
    'Snake (蛇 / Shé)',
    'Horse (马 / Mǎ)',
    'Goat (羊 / Yáng)',
    'Monkey (猴 / Hóu)',
    'Rooster (鸡 / Jī)',
    'Dog (狗 / Gǒu)'
    'Pig (猪/ Zhū)']

    chinese_zodiac(zodiacs, X)

## Screenshots

![Zodiac Program Output](<img width="1322" height="307" alt="image" src="https://github.com/user-attachments/assets/d6802e04-6418-4070-a94e-966bfa8e2e46" />
)
