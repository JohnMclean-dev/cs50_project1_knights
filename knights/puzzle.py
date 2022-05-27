from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."

knowledge0 = And(
    Or(AKnight, AKnave),                            # must be a knight or a knave
    
    Not(And(AKnight, AKnave)),                      # the statement must be a lie, it can't be both
    
    Implication(AKnight, And(AKnight, AKnave)),     # the knight would tell the truth about the statement
    Implication(AKnave, Not(And(AKnight, AKnave)))  # the knave would like about the statement
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.

knowledge1 = And(
    Or(AKnight, AKnave),                            # A must be a knight or knave
    Or(BKnight, BKnave),                            # B must be a knight or knave
    
    Not(And(AKnave, BKnave)),                       # the statement must be a lie, a knave would not tell this truth
    Implication(AKnight, And(AKnave, BKnave)),      # A would tell the truth if they are a knight
    Implication(AKnave, Not(And(AKnave, BKnave)))   # A would lie if they are the knave
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

knowledge2 = And(
    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
