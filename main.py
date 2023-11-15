symbols = {
    "A": ["3F", "48", "48", "48", "3F"],
    "B": ["7F", "49", "49", "49", "36"],
    "C": ["3E", "41", "41", "41", "22"],
    "D": ["7F", "41", "41", "41", "3E"],
    "E": ["7F", "49", "49", "49", "41"],
    "F": ["7F", "48", "48", "48", "40"],
    "G": ["3E", "41", "49", "49", "2E"],
    "H": ["7F", "08", "08", "08", "7F"],
    "I": ["41", "41", "7F", "41", "41"],
    "J": ["46", "41", "41", "7F", "40"],
    "K": ["7F", "08", "08", "14", "63"],
    "L": ["7F", "01", "01", "01", "01"],
    "M": ["7F", "20", "18", "20", "7F"],
    "N": ["7F", "20", "10", "08", "7F"],
    "O": ["3E", "41", "41", "41", "3E"],
    "P": ["7F", "48", "48", "48", "30"],
    "Q": ["3E", "41", "45", "43", "3F"],
    "R": ["7F", "48", "48", "48", "37"],
    "S": ["31", "49", "49", "49", "46"],
    "T": ["40", "40", "7F", "40", "40"],
    "U": ["7E", "01", "01", "01", "7E"],
    "V": ["7E", "02", "01", "02", "7E"],
    "W": ["7F", "02", "0C", "02", "7F"],
    "X": ["63", "14", "08", "14", "63"],
    "Y": ["70", "08", "07", "08", "70"],
    "Z": ["43", "45", "49", "51", "61"],

    "0": ["3e", "45", "49", "51", "3e"],
    "1": ["41", "7f", "01"],
    "2": ["27", "49", "49", "49", "31"],
    "3": ["22", "41", "49", "49", "36"],
    "4": ["78", "08", "08", "7f", "08"],
    "5": ["79", "49", "49", "49", "46"],
    "6": ["3e", "49", "49", "49", "46"],
    "7": ["40", "47", "48", "48", "70"],
    "8": ["36", "49", "49", "49", "36"],
    "9": ["32", "49", "49", "49", "3e"],

    " ": ["00", "00", "00"],
    ".": ["01"],
    "!": ["7D"],
    "-": ["08", "08", "08"],
    "_": ["01", "01", "01"],
    ",": ["05", "06"],
    ";": ["01", "13"],
    ":": ["12"],
    "?":["20", "40", "4d", "48", "30"],
    "+":["08", "08", "3e", "08", "08"],
    "/":["03", "04", "08", "10", "60"],
    "\\":["60", "10", "08", "04", "03"],
    "*":["28", "70", "28"],
    "#":["24", "7f", "24", "7f", "24"],
    "=":["12", "12", "12"],
    "(":["3e", "41", "41", "41"],
    ")":["41", "41", "41", "3e"],
    "[":["7f", "41", "41", "41"],
    "]":["41", "41", "41", "7f"],
    "{":["08", "36", "41", "41", "22"],
    "}":["22", "41", "41", "36", "08"],
    "<":["08", "14", "22", "22"],
    ">":["22", "22", "14", "08"],
    "'":["60"],
    '"':["60", "00", "60"],
    "^":["20","40", "20"],
    "~":["04", "08", "04", "04", "08"],
    "|":["7f"],
    "`":["40", "20"],
    "$":["12", "2a", "7f", "2a", "24"],
    "€":["3e", "55", "55", "41", "22"],
    "@":["3e", "4d", "53", "52", "3e"],
    "&":["36", "49", "49", "3e", "09"],
    "%":["33", "54", "7b", "15", "67"],

    "NaC": ["7F", "7F", "7F", "7F", "7F"]
}

# message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = input("Enter your text\n> ")
filepath = "memory.hex"

message = message.upper()

string = "v2.0 raw\n"
for letter in message:
    if letter not in symbols:
        letter = "NaC"
    
    for code in symbols[letter]:
        string += "0x" + code + "\n"

    # Small space between caracters
    string += "0x00" + "\n"

with open(filepath, "w") as file:
    file.write(string)
    print(f"File created / modified ({filepath})")

    