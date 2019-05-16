"""
module for various strategy
"""

from typing import Any
from random import randint
# TODO: Adjust the type annotation as needed.


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)

# TODO: Implement a random strategy.


def random_strategy(game: Any) -> Any:
    """
    Reture a move for game through a random input
    """
    move = game.current_state.get_possible_moves()
    return move[randint(0, len(move)-1)]


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
