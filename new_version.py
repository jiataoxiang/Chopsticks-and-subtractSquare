
class Current_state():
    def __init__(self, movement):
        self.movement = movement

class Chopsticks_state(Current_state):
    def __init__(self, movement, left1,left2,right1,right2):
        """
        Create a new Chopsticks self
        """
        Current_state.__init__(self,movement)
        self.left1 = left1 % 5
        self.left2 = left2 % 5
        self.right1 = right1 % 5
        self.right2 = right2 % 5

    def __str__(self):
        """
        Return a user-friendly string representation of Chopsticks self
        """
        return "Player1: {}-{}  Player2: {}-{}".format(self.left1,self.right1,
                                                       self.left2,self.right2)

    def is_valid_move(self, move_to_make):
        """
        return True if the move is valid, else return False
        """
        if move_to_make == None:
            return False
        elif self.left1 == 0:
            if move_to_make not in ["rl","rr"]:
                return False
            if self.left2 == 0:
                if move_to_make != "rr":
                    return False
        elif self.right1 == 0:
            if move_to_make not in ["ll","lr"]:
                return False
            if self.right2 == 0:
                if move_to_make != "ll":
                    return False
        elif self.left2 == 0:
            if move_to_make not in ["rr","lr"]:
                return False
            if self.right1 == 0:
                if move_to_make != "lr":
                    return False
        elif self.right2 == 0:
            if move_to_make not in ["ll","rl"]:
                return False
            if self.left1 == 0:
                if move_to_make != "rl":
                    return False
        elif move_to_make not in ["ll","lr","rl","rr"]:
            return False
        return True



    def get_possible_moves(self):
        """
        Return the possible moves
        """
        if self.left1 == 0 and self.left2 * self.right2 != 0:
            if self.movement % 2 == 1:
                return ["rl","rr"]
            else:
                return ["lr","rr"]
        elif self.right1 == 0 and self.left2 * self.right2 != 0:
            if self.movement % 2 == 1:
                return ["ll","lr"]
            else:
                return ["ll","rl"]
        elif self.left2 == 0 and self.left1 * self.right1 != 0:
            if self.movement % 2 == 1:
                return ["lr","rr"]
            else:
                return ["rl","rr"]
        elif self.right2 == 0 and self.left1 * self.right1 != 0:
            if self.movement % 2 == 1:
                return ["ll","lr"]
            else:
                return ["ll","rl"]
        elif self.left1 == 0 and self.left2 == 0:
            return ["rr"]
        elif self.left1 == 0 and self.right2 == 0:
            if self.movement % 2 == 1:
                return ["rl"]
            else:
                return ["lr"]
        elif self.right1 == 0 and self.left2 == 0:
            if self.movement % 2 == 1:
                return ["lr"]
            else:
                return ["rl"]
        elif self.right1 == 0 and self.right2 == 0:
            return ["ll"]
        else:
            return ["ll","lr","rl","rr"]








    def get_current_player_name(self):
        if self.movement % 2 == 1:
            return "p1"
        else:
            return "p2"




    def make_move(self, move_to_make):
        if self.movement % 2 == 1:
            if move_to_make == "ll":
                return Chopsticks_state(self.movement+1, self.left1,
                                        self.left2 + self.left1,
                                        self.right1, self.right2)
        if self.movement % 2 == 1:
            if move_to_make == "lr":
                return Chopsticks_state(self.movement+1, self.left1,
                                        self.left2,self.right1,
                                        self.right2 + self.left1)
        if self.movement % 2 == 1:
            if move_to_make == "rl":
                return Chopsticks_state(self.movement+1, self.left1,
                                        self.left2 + self.right1,
                                        self.right1, self.right2)
        if self.movement % 2 == 1:
            if move_to_make == "rr":
                return Chopsticks_state(self.movement+1, self.left1,
                                        self.left2,self.right1,
                                        self.right2 + self.right1)
        if self.movement % 2 == 0:
            if move_to_make == "ll":
                return Chopsticks_state(self.movement+1,
                                        self.left1 + self.left2,
                                        self.left2,
                                        self.right1, self.right2)
        if self.movement % 2 == 0:
            if move_to_make == "lr":
                return Chopsticks_state(self.movement + 1, self.left1,
                                        self.left2,
                                        self.right1 + self.left2,
                                        self.right2)
        if self.movement % 2 == 0:
            if move_to_make == "rl":
                return Chopsticks_state(self.movement+1,self.left1,
                                        self.left2,
                                        self.right1 + self.left2, self.right2)
        if self.movement % 2 == 0:
            if move_to_make == "rr":
                return Chopsticks_state(self.movement + 1, self.left1,
                                        self.left2,
                                        self.right1 + self.right2,
                                        self.right2)

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
            return "p1"
        else:
            return "p2"


    def make_move(self, move_to_make):
        a = Subtract_state(self.number - move_to_make, self.movement + 1)
        return a



















class Game():
    def __init__(self):
        raise NotImplementedError


class Chopsticks(Game):
    def __init__(self, is_p1_turn):
        self.current_state = Chopsticks_state(1,1,1,1,1)
        if not is_p1_turn:
            self.current_state.movement = 2


    def __str__(self):
        pass

    def is_over(self, current_state: Chopsticks_state):
        return (current_state.left1 + current_state.right1 == 0 or
                current_state.left2 + current_state.right2 == 0)



    def str_to_move(self, a):
        return a





    def is_winner(self, player_name):
        if (self.current_state.left1 + self.current_state.right1 == 0 or
                self.current_state.left2 + self.current_state.right2 == 0):
            if player_name == "p1" and self.current_state.movement % 2 == 0:
                return True
            elif player_name == "p2" and self.current_state.movement % 2 == 1:
                return True
        return False


    def get_instructions(self):
        """
        Return
        """
        return """Players take turns adding the values of one of their hands to 
        one of their opponents(modulo 5). A hand with a total of 5 
        (or 0; 5 modulo 5) is considered 'dead'. The first player to hand 2 
        dead hands is the loser. 
        """


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
        if self.current_state.number == 0:
            if player_name == "p1" and self.current_state.movement % 2 == 0:
                return True
            elif player_name == "p2" and self.current_state.movement % 2 == 1:
                return True
        return False
    def get_instructions(self):
        return"""Players take turns subtracting square numbers from the 
        starting number. The winner is the person who subtract to 0.
        """













