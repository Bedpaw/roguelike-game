from mock.Board_mock import BoardMock


class MyObject:
    """
    Object:
    name:
    symbol_on_map = "X" # items and hero CAPS, monsters lowercase
    position_x = 1
    position_y = 3
    is_on_board = Boolean
    delete_from_board()
    create_on_board()  ????
    """

    def __init__(self, name, symbol_on_map, position_x, position_y):
        self.name = name
        self.symbol_on_map = symbol_on_map
        self.position_x = position_x
        self.position_y = position_y

    field_move_possible = True
    Board = BoardMock()
    is_on_board = True

    def delete_from_board(self):
        self.is_on_board = False


