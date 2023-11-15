symbols = {
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
    "%":["33", "54", "7b", "15", "67"]
}

default = "?"


text = input("Rentrez le texte : ")
seq = []
text = text.upper()
for symbol in text:
    if symbol in symbols.keys():
        seq.append(symbols[symbol])
    else:
        print("Le symbole " + symbol + " n'est pas reconnu")
        seq.append(symbols[default])

with open("memory.hex", "w", encoding="utf-8") as f:
    f.write("v2.0 raw\n")
    for i in range(len(seq)):
        for j in range(len(seq[i])):
            f.write("0x" + seq[i][j])
            f.write("\n")
            if j == len(seq[i])-1:
                f.write("0x00\n")
        if i != len(seq)-1:
            f.write("\n")
    print("Fichier crée (memory.hex)")

    