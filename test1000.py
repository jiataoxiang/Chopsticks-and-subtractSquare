class Current_state():
    def __init__(self, movement):
        self.movement = movement



class Subtract_state(Current_state):

    def __init__(self,number, movement):
        Current_state.__init__(self,movement)
        self.number = int(number)
    def __str__(self):
        return "value {}".format(int(self.number))

    def is_valid_move(self, move_to_make):
        """
        return True if the move is valid, else return False
        """
        if move_to_make == None:
            return False
        elif move_to_make > self.number:
            return False
        elif int(move_to_make ** 0.5) != float(move_to_make) ** 0.5:
            return False
        return True

    def get_possible_moves(self):
        move = []
        max_value = int(self.number ** 0.5)
        for i in range(1, max_value+1):
            move.append(i ** 2)
        return move


    def get_current_player_name(self):
        if self.movement % 2 == 1:
            return "P1"
        else:
            return "P2"


    def make_move(self, move_to_make):
        a = Subtract_state(self.number - move_to_make, self.movement + 1)
        return a


















class Game():
    def __init__(self):
        raise NotImplementedError

class Subtract_square(Game):
    def __init__(self, is_p1_turn):
        self.start_number = input("choose the start_number: ")
        self.current_state = Subtract_state(self.start_number, 1)
        if not is_p1_turn:
            self.current_state.movement = 2

    def __str__(self):
        pass
    def is_over(self, current_state: Subtract_state):
        return current_state.number == 0

    def str_to_move(self, a):
        return int(a)



    def is_winner(self, player_name):
        if player_name == "p1" and self.current_state.movement % 2 == 0:
            return True
        elif player_name == "p2" and self.current_state.movement % 2 == 1:
            return True
        return False
    def get_instructions(self):
        return"""Players take turns subtracting square numbers from the 
        starting number. The winner is the person who subtract to 0.
        """
