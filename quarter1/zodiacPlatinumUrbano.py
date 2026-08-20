def chinese_zodiac(a, b):
    c = 0
    c = (b - 1900) % 12
    print("Your Zodiac sign is:", a[c])
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
    'Pig (猪 / Zhū)']



X = input("Enter your birth year(must be above or equal to 1900): ")
try:
    year = int(X)
    if year < 1900:
        print("Error: Age entered is below 1900,", year, "is not a valid input.")
    else:
        chinese_zodiac(zodiacs, year)
except ValueError:
    print("Please enter an integer.")

