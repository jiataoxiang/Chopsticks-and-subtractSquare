"""
Module for various games
"""
from typing import List, Any


class CurrentState:
    """
    A game state which can get possible moves, get current player's name, make
    a move and tell whether a move is valid.

    === Attributes ===
    @type movement: int
        the number of moves the game proceed
    """

    def __init__(self, movement):
        """
        Create a new game state self
        """
        self.movement = movement

    def __str__(self):
        """
        Return a user-friendly string representation of game state self
        """
        raise NotImplementedError

    def __eq__(self, other: Any):
        """
        Return whether this game state is equal to other.
        """
        raise NotImplementedError

    def is_valid_move(self, move_to_make):
        """
        Return True if the move move_to_make is valid, otherwise return False
        """
        raise NotImplementedError

    def get_possible_moves(self):
        """
        Return a list of possible move
        """
        raise NotImplementedError

    def get_current_player_name(self):
        """
        Return player's name who is currently making a move

        >>> s = CurrentState(1)
        >>> s.get_current_player_name()
        'p1'
        >>> s = CurrentState(2)
        >>> s.get_current_player_name()
        'p2'
        """
        if self.movement % 2 == 1:
            return "p1"
        return "p2"

    def make_move(self, move_to_make):
        """
        Return a updated move information
        """
        raise NotImplementedError


class ChopsticksState(CurrentState):
    """
    A game state for game Chopsticks.
    """

    def __init__(self, movement: int, player1: tuple, player2: tuple) -> None:
        """
        Create a new game state Chopsticks self.

        >>> s = ChopsticksState(1, (1, 1), (1, 1))
        >>> print(s)
        Player1: 1-1  Player2: 1-1
        >>> s = ChopsticksState(1, (2, 3), (1, 1))
        >>> print(s)
        Player1: 2-3  Player2: 1-1
        """
        CurrentState.__init__(self, movement)
        self.left1 = player1[0] % 5
        self.left2 = player2[0] % 5
        self.right1 = player1[1] % 5
        self.right2 = player2[1] % 5

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of Chopsticks self

        >>> print(ChopsticksState(1, (1, 1), (1, 1)))
        Player1: 1-1  Player2: 1-1
        >>> print(ChopsticksState(1, (2, 3), (1, 1)))
        Player1: 2-3  Player2: 1-1
        """
        return "Player1: {}-{}  Player2: {}-{}".format(self.left1, self.right1,
                                                       self.left2, self.right2)

    def __eq__(self, other: Any) -> bool:
        """
        Return whether this game state is equal to other.

        >>> a = ChopsticksState(1, (1, 1), (1, 1))
        >>> b = ChopsticksState(1, (1, 1), (1, 1))
        >>> c = ChopsticksState(1, (1, 4), (3, 2))
        >>> a == b
        True
        >>> a == c
        False
        """
        return (type(self) == type(other) and self.movement == other.movement
                and self.left1 == other.left1 and self.left2 == other.left2
                and self.right1 == other.right1 and self.right2 == other.right2)

    def is_valid_move(self, move_to_make: str) -> bool:
        """
        return True if the move is valid, else return False

        >>> s = ChopsticksState(1, (1, 1), (1, 1))
        >>> s.is_valid_move("lr")
        True
        >>> s = ChopsticksState(1, (0, 1), (0, 1))
        >>> s.is_valid_move("lr")
        False
        """
        if move_to_make is None:
            return False
        elif self.left1 == 0:
            if move_to_make not in ["rl", "rr"] and self.movement % 2 == 1:
                return False
            elif move_to_make not in ["lr", "rr"] and self.movement % 2 == 0:
                return False
            if self.left2 == 0:
                if move_to_make != "rr":
                    return False
        elif self.right1 == 0:
            if move_to_make not in ["ll", "lr"] and self.movement % 2 == 1:
                return False
            elif move_to_make not in ["ll", "rl"] and self.movement % 2 == 0:
                return False
            if self.right2 == 0:
                if move_to_make != "ll":
                    return False
        elif self.left2 == 0:
            if move_to_make not in ["rr", "lr"] and self.movement % 2 == 1:
                return False
            elif move_to_make not in ["rr", "rl"] and self.movement % 2 == 0:
                return False
            if self.right1 == 0:
                if move_to_make != "lr":
                    return False
        elif self.right2 == 0:
            if move_to_make not in ["ll", "rl"] and self.movement % 2 == 1:
                return False
            elif move_to_make not in ["ll", "rl"] and self.movement % 2 == 0:
                return False
            if self.left1 == 0:
                if move_to_make != "rl":
                    return False
        elif move_to_make not in ["ll", "lr", "rl", "rr"]:
            return False
        return True

    def get_possible_moves(self) -> List[str]:
        """
        Return the possible moves

        >>> s = ChopsticksState(1, (1, 1), (1, 1))
        >>> s.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        >>> s = ChopsticksState(2, (0, 1), (1, 1))
        >>> s.get_possible_moves()
        ['lr', 'rr']
        """
        if self.left1 == 0 and self.left2 * self.right2 != 0:
            if self.movement % 2 == 1:
                return ["rl", "rr"]
            return ["lr", "rr"]
        elif self.right1 == 0 and self.left2 * self.right2 != 0:
            if self.movement % 2 == 1:
                return ["ll", "lr"]
            return ["ll", "rl"]
        elif self.left2 == 0 and self.left1 * self.right1 != 0:
            if self.movement % 2 == 1:
                return ["lr", "rr"]
            return ["rl", "rr"]
        elif self.right2 == 0 and self.left1 * self.right1 != 0:
            if self.movement % 2 == 1:
                return ["ll", "rl"]
            return ["ll", "lr"]
        elif self.left1 == 0 and self.left2 == 0:
            return ["rr"]
        elif self.left1 == 0 and self.right2 == 0:
            if self.movement % 2 == 1:
                return ["rl"]
            return ["lr"]
        elif self.right1 == 0 and self.left2 == 0:
            if self.movement % 2 == 1:
                return ["lr"]
            return ["rl"]
        elif self.right1 == 0 and self.right2 == 0:
            return ["ll"]
        else:
            return ["ll", "lr", "rl", "rr"]

    def make_move(self, move_to_make: str) -> "ChopsticksState":
        """
        Return a updated moving information

        >>> s = ChopsticksState(1, (1, 1), (1, 1))
        >>> print(s.make_move("ll"))
        Player1: 1-1  Player2: 2-1
        >>> s = ChopsticksState(4, (2, 3), (1, 1))
        >>> print(s.make_move("ll"))
        Player1: 3-3  Player2: 1-1
        """
        if self.movement % 2 == 1:
            if move_to_make == "ll":
                return ChopsticksState(self.movement+1,
                                       (self.left1, self.right1),
                                       (self.left2 + self.left1, self.right2))
            elif move_to_make == "lr":
                return ChopsticksState(self.movement+1,
                                       (self.left1, self.right1),
                                       (self.left2, self.right2 + self.left1))
            elif move_to_make == "rl":
                return ChopsticksState(self.movement+1,
                                       (self.left1, self.right1),
                                       (self.left2 + self.right1, self.right2))
            elif move_to_make == "rr":
                return ChopsticksState(self.movement+1,
                                       (self.left1, self.right1),
                                       (self.left2, self.right2 + self.right1))
        elif self.movement % 2 == 0:
            if move_to_make == "ll":
                return ChopsticksState(self.movement+1,
                                       (self.left1 + self.left2, self.right1),
                                       (self.left2, self.right2))
            elif move_to_make == "lr":
                return ChopsticksState(self.movement + 1,
                                       (self.left1, self.right1 + self.left2),
                                       (self.left2, self.right2))
            elif move_to_make == "rl":
                return ChopsticksState(self.movement+1,
                                       (self.left1 + self.right2, self.right1),
                                       (self.left2, self.right2))
            elif move_to_make == "rr":
                return ChopsticksState(self.movement + 1,
                                       (self.left1, self.right1 + self.right2),
                                       (self.left2, self.right2))
        return self


class SubtractState(CurrentState):
    """
    A game state for game Subtract square.
    """

    def __init__(self, number: int, movement: int) -> None:
        """
        Create a new game state for game subtract square.

        >>> s = SubtractState(3, 1)
        >>> print(s)
        value 3
        >>> s = SubtractState(9, 2)
        >>> print(s)
        value 9
        """
        CurrentState.__init__(self, movement)
        self.number = int(number)

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of Subtract_state self.

        >>> print(SubtractState(2, 1))
        value 2
        >>> print(SubtractState(6, 9))
        value 6
        """
        return "value {}".format(int(self.number))

    def __eq__(self, other: Any) -> bool:
        """
        Return whether this game state is equal to other.

        >>> a = SubtractState(1, 3)
        >>> b = SubtractState(1, 3)
        >>> c = SubtractState(1, 2)
        >>> a == b
        True
        >>> a == c
        False
        """
        return (type(self) == type(other) and self.movement == other.movement
                and self.number == other.number)

    def is_valid_move(self, move_to_make: int or None) -> bool:
        """
        return True if the move is valid, else return False

        >>> s = SubtractState(2, 9)
        >>> s.is_valid_move(None)
        False
        >>> s = SubtractState(2, 9)
        >>> s.is_valid_move(4)
        False
        >>> s = SubtractState(9, 2)
        >>> s.is_valid_move(4)
        True
        """
        if move_to_make is None:
            return False
        elif move_to_make > self.number:
            return False
        elif int(move_to_make ** 0.5) != float(move_to_make) ** 0.5:
            return False
        return True

    def get_possible_moves(self) -> List[int]:
        """
        Return the possible moves

        >>> s = SubtractState(9, 2)
        >>> s.get_possible_moves()
        [1, 4, 9]
        >>> s = SubtractState(65,6)
        >>> s.get_possible_moves()
        [1, 4, 9, 16, 25, 36, 49, 64]
        """
        move = []
        max_value = int(self.number ** 0.5)
        for i in range(1, max_value+1):
            move.append(i ** 2)
        return move

    def make_move(self, move_to_make: int) -> "SubtractState":
        """
        Return a updated moving information

        precondition: move_to_make is a valid move.

        >>> s = SubtractState(1, 2)
        >>> print(s.make_move(1))
        value 0
        >>> s = SubtractState(9, 2)
        >>> print(s.make_move(4))
        value 5
        """
        return SubtractState(self.number - move_to_make, self.movement + 1)


class Game:
    """
    A game instruction which can get instruction for specific game, tell who is
    the winner and whether a game is over.
    """
    def __init__(self) -> None:
        """
        Create a game self.
        """
        raise NotImplementedError

    def is_over(self, current_state) -> bool:
        """
        Return True if the game is over, otherwise return False
        """
        raise NotImplementedError

    def str_to_move(self, a):
        """
        Return a suitable move representation of string move.
        """
        raise NotImplementedError

    def is_winner(self, player_name: str) -> bool:
        """
        Return true if the player player_name is winner.
        """
        raise NotImplementedError

    def get_instructions(self) -> str:
        """
        Return the specific game instruction.
        """
        raise NotImplementedError


class Chopsticks(Game):
    """
    A game instruction for game Chopsticks
    """

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Create a chopsticks game self
        """
        self.current_state = ChopsticksState(1, (1, 1), (1, 1))
        if not is_p1_turn:
            self.current_state.movement = 2

    def is_over(self, current_state: ChopsticksState) -> bool:
        """
        Return True if the game is over, otherwise return False.
        """
        return (current_state.left1 + current_state.right1 == 0 or
                current_state.left2 + current_state.right2 == 0)

    def str_to_move(self, a: str) -> str:
        """
        Return a suitable move representation of string move.
        """
        return a

    def is_winner(self, player_name: str) -> bool:
        """
        Return true if the player player_name is winner.
        """
        if (self.current_state.left1 + self.current_state.right1 == 0 or
                self.current_state.left2 + self.current_state.right2 == 0):
            if player_name == "p1" and self.current_state.movement % 2 == 0:
                return True
            elif player_name == "p2" and self.current_state.movement % 2 == 1:
                return True
        return False

    def get_instructions(self) -> str:
        """
        Return chopsticks game instruction
        """
        return """Players take turns adding the values of one of their hands to 
        one of their opponents(modulo 5). A hand with a total of 5 
        (or 0; 5 modulo 5) is considered 'dead'. The first player to hand 2 
        dead hands is the loser. 
        """


class SubtractSquare(Game):
    """
    A game instruction for game Substruct square.
    """
    def __init__(self, is_p1_turn: bool) -> None:
        """
        Create a subtract square game self.
        """
        self.start_number = input("choose the start_number: ")
        self.current_state = SubtractState(int(self.start_number), 1)
        if not is_p1_turn:
            self.current_state.movement = 2

    def is_over(self, current_state: SubtractState) -> bool:
        """
        Return True if the game is over, otherwise return False.
        """
        return current_state.number == 0

    def str_to_move(self, a: str) -> int:
        """
        Return a suitable move representation of string move.
        """
        return int(a)

    def is_winner(self, player_name: str) -> bool:
        """
        Return true if the player player_name is winner.
        """
        if self.current_state.number == 0:
            if player_name == "p1" and self.current_state.movement % 2 == 0:
                return True
            elif player_name == "p2" and self.current_state.movement % 2 == 1:
                return True
        return False

    def get_instructions(self) -> str:
        """
        Return subtract square game instruction
        """
        return"""Players take turns subtracting square numbers from the 
        starting number. The winner is the person who subtract to 0.
        """


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")

