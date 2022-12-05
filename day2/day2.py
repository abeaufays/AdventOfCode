file = open("day2/data.txt", "r")

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = -1
DRAW = 0
WIN = 1

score_compute = {
    ROCK: {
        ROCK: DRAW,
        PAPER: WIN,
        SCISSORS: LOSE
    },
    PAPER: {
        ROCK: LOSE,
        PAPER: DRAW,
        SCISSORS: WIN
    },
    SCISSORS: {
        ROCK: WIN,
        PAPER: LOSE,
        SCISSORS: DRAW
    }
}

choice_compute = {
    ROCK: {
        WIN: PAPER,
        DRAW: ROCK,
        LOSE: SCISSORS
    },
    PAPER: {
        WIN: SCISSORS,
        DRAW: PAPER,
        LOSE: ROCK
    },
    SCISSORS: {
        WIN: ROCK,
        DRAW: SCISSORS,
        LOSE: PAPER
    },
}


input_conversion = {"A": ROCK, "B": PAPER, "C": SCISSORS,
                    "X": LOSE, "Y": DRAW, "Z": WIN}

score = 0

for line in file.readlines():
    opponent_input, guide_input = line.split()

    opponent = input_conversion[opponent_input]

    guide_result = input_conversion[guide_input]
    guide = choice_compute[opponent][guide_result]

    score += guide
    score += (guide_result + 1) * 3

print(score)
