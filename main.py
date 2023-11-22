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
    "L": ["7F", "01", "01", "01"],
    "M": ["7F", "20", "18", "20", "7F"],
    "N": ["7F", "20", "10", "08", "7F"],
    "O": ["3E", "41", "41", "41", "3E"],
    "P": ["7F", "48", "48", "48", "30"],
    "Q": ["3E", "41", "45", "43", "3F"],
    "R": ["7F", "48", "48", "48", "37"],
    "S": ["31", "49", "49", "49", "46"],
    "T": ["40", "40", "7F", "40", "40"],
    "U": ["7E", "01", "01", "01", "7E"],
    "V": ["7C", "02", "01", "02", "7C"],
    "W": ["7F", "02", "0C", "02", "7F"],
    "X": ["63", "14", "08", "14", "63"],
    "Y": ["70", "08", "07", "08", "70"],
    "Z": ["43", "45", "49", "51", "61"],

    "0": ["3E", "45", "49", "51", "3E"],
    "1": ["41", "7F", "01"],
    "2": ["27", "49", "49", "49", "31"],
    "3": ["22", "41", "49", "49", "36"],
    "4": ["78", "08", "08", "7F", "08"],
    "5": ["79", "49", "49", "49", "46"],
    "6": ["3e", "49", "49", "49", "46"],
    "7": ["40", "47", "48", "48", "70"],
    "8": ["36", "49", "49", "49", "36"],
    "9": ["32", "49", "49", "49", "3E"],

    " ": ["00", "00", "00"],
    ".": ["01"],
    "!": ["7D"],
    "-": ["08", "08", "08"],
    "_": ["01", "01", "01", "01", "01"],
    ",": ["05", "06"],
    ";": ["01", "13"],
    ":": ["12"],
    "?":["20", "40", "4D", "48", "30"],
    "+":["08", "08", "3E", "08", "08"],
    "/":["03", "04", "08", "10", "60"],
    "\\":["60", "10", "08", "04", "03"],
    "*":["08", "2A", "1C", "2A", "08"],
    "#":["14", "7F", "14", "7F", "14"],
    "=":["14", "14", "14"],
    "(":["3E", "41", "41"],
    ")":["41", "41", "3E"],
    "[":["7F", "41", "41"],
    "]":["41", "41", "7F"],
    "{":["08", "36", "41", "22"],
    "}":["22", "41", "36", "08"],
    "<":["08", "14", "22", "22"],
    ">":["22", "22", "14", "08"],
    "'":["60"],
    '"':["60", "00", "60"],
    "^":["10", "20","40", "20", "10"],
    "~":["04", "08", "04", "08"],
    "|":["7F"],
    "`":["40", "20"],
    "$":["12", "2A", "7F", "2A", "24"],
    "€":["3E", "55", "55", "41", "22"],
    "@":["3E", "4D", "53", "52", "3E"],
    "&":["36", "49", "4D", "36", "09"],
    "%":["73", "54", "6B", "15", "67"]
}

NB_BITS = 8
MEMORY_SIZE = 2**NB_BITS
MAX_JUMP_SIZE = 2**(NB_BITS - 3)
NB_NOPS = 2

message = input("Enter your text:\n> ")
modes = ["once", "cycle", "repeat"]
mode = ""
while mode not in modes:
    mode = input(f"Choose your mode ({', '.join(modes)}):\n> ")

filepath = "memory.hex"

message = message.upper()

cells = ["0x00" for _ in range(MEMORY_SIZE)]
i_actual_cell = 0
too_big = False
for letter in message:
    if letter not in symbols:
        letter = "#"

    if i_actual_cell + len(symbols[letter]) * (NB_NOPS + 1) + NB_NOPS + 2 >= MEMORY_SIZE:
        too_big = True
        break
    
    for code in symbols[letter]:
        cells[i_actual_cell] = "0x" + code
        i_actual_cell += 1
    
        for _ in range(NB_NOPS):
            cells[i_actual_cell] = hex(2**(NB_BITS-1) + 1)  # Nop (Jump +1)
            i_actual_cell += 1

    # Small space between caracters
    # cells[i_actual_cell] = "0x00"
    i_actual_cell += 1
    
    for _ in range(NB_NOPS):
        cells[i_actual_cell] = hex(2**(NB_BITS-1) + 1)  # Nop (Jump +1)
        i_actual_cell += 1

if mode == "once" and not too_big:
    if i_actual_cell + 1 < MEMORY_SIZE:
        cells[i_actual_cell] = hex(2**(NB_BITS-1))  # Jump 0
        i_actual_cell += 1
    else:
        too_big = True

if mode == "repeat" and not too_big:
    if i_actual_cell + 1 < MEMORY_SIZE:
        cells[i_actual_cell] = hex(2**(NB_BITS) - 1)  # Clear
        i_actual_cell += 1
    else:
        too_big = True

if mode == "cycle" or mode == "repeat" and not too_big:
    while i_actual_cell != MEMORY_SIZE:
        if i_actual_cell + MAX_JUMP_SIZE - 1 < MEMORY_SIZE:
            cells[i_actual_cell] = hex(2**(NB_BITS-1) + MAX_JUMP_SIZE - 1)  # Jump +(MAX_JUMP_SIZE - 1)
            i_actual_cell += MAX_JUMP_SIZE - 1
        else:
            jump_size = MEMORY_SIZE - i_actual_cell
            cells[i_actual_cell] = hex(2**(NB_BITS-1) + jump_size)  # Jump +jump_size
            i_actual_cell += jump_size

if not too_big:
    string = "v2.0 raw\n" + "\n".join(cells)

    with open(filepath, "w") as file:
        file.write(string)
        print(f"File created/modified ({filepath})")

else:
    print("⚠️ Text too big for the memory size")
