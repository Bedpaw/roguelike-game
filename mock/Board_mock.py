class BoardMock:
    board = [[""], [""], [""]], [[""], ["X"], [""]], [[""], [""], [""]]
    taken_positions = [[1, 1]]

    def check_move_possibility(self, caller, position):
        # position is where i want to move:
        # caller is monster/Hero who call this function

        # caller.type = "Monster"
        # return False if monster, item or wall
        # start fight if Hero, return True
        # else True

        # caller.type = "Hero"
        # return False if wall
        # start fight if monster, return True
        # add item to Hero inventory if item, return True
        # else True

        if position == self.taken_positions[0]:
            return False
        else:
            return True


