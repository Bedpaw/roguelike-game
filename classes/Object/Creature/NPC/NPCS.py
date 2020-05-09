from classes.Object.Item.Item import Item
from classes.Object.Creature.NPC.NPC import NPC
from macros import DIFFICULTY_LEVEL, MOVES_TYPES
from macros.COLORS import *


class Troll_king(NPC):
    def dialog_path(self, hero):
        if hero.quest_taken_by_name("TROLL KING"):
            self.dialog_index = 1
            hero.backpack.append(Item.quest_item('Troll brain'))  # MOCK
        else:
            self.dialog_index = 0

        dialog_path = self.dialogs_path[self.dialog_index]
        return self.read_dialog_from_file(dialog_path)

    def change_dialog_path(self):
        self.dialogs_path = [
            f'{self.conversation_folder_path}troll_king_before_quest.txt',
            f'{self.conversation_folder_path}troll_king.txt'
        ]

    @classmethod
    def troll_king(cls, pos_x, pos_y, dif_lvl=DIFFICULTY_LEVEL.NORMAL):
        dif_dep = cls.difficulty_depends  # shortcut only
        troll_king = cls(name="Troll king",
                         position_x=pos_x,
                         position_y=pos_y,
                         symbol_on_map="T",
                         strength=dif_dep(70, dif_lvl),
                         max_hp=dif_dep(500, dif_lvl),
                         hp=dif_dep(500, dif_lvl),
                         move_type=MOVES_TYPES.RANDOM_STRAIGHT,

                         exp=300,
                         loot={
                             'coins': 500,
                             'quest': Item.quest_item('Troll brain')
                         },
                         color_on_board=COLOR.CYAN,
                         conversation_file_name='troll_king.txt',
                         on_fight_message="UGA HA!",
                         on_die_message='Ughh, yough bum bum troll kingo... yough ken eat his braaajn nowww'

                         )
        troll_king.change_dialog_path()
        return troll_king


class Fake_wall(NPC):

    def dialog_path(self, hero):
        if hero.quest_taken_by_name("GOLDEN RING") and not hero.quest_done_by_name("GOLDEN RING"):
            self.dialog_index = 1
        else:
            self.dialog_index = 0
        dialog_path = self.dialogs_path[self.dialog_index]
        return self.read_dialog_from_file(dialog_path)

    def change_dialog_path_and_quests(self, quest0):
        self.dialogs_path = [
            f'{self.conversation_folder_path}troll_cave_hole_dialog1.txt',
            f'{self.conversation_folder_path}troll_cave_hole_dialog2.txt'
        ]
        self.quest_func = [quest0]

    @staticmethod
    def quest0(hero):
        for quest in hero.quests:
            if quest['name'] == "GOLDEN RING":
                quest['COMPLETED'] = True
                hero.backpack.append(Item.quest_item("Golden ring"))
                hero.add_to_message_box(f'That was disgusting, but you have found golden ring')

    @classmethod
    def fake_wall(cls, pos_x, pos_y, name):
        fake_wall = cls(
            name=name,
            position_x=pos_x,
            position_y=pos_y,
            symbol_on_map='|',
            field_color=BG_COLOR.LIGHTGREY)

        fake_wall.change_dialog_path_and_quests(cls.quest0)

        return fake_wall


def trade(hero):
    if hero.is_in_backpack("King's store patent"):
        hero.add_to_message_box("Sorry, I don't have items for sell in this game version")
    else:
        hero.add_to_message_box("You need store patent if you want to trade with me")
    print(hero.game.current_board().last_move_message)


class King(NPC):
    def dialog_path(self, hero):
        GOLDEN_RING_TAKEN = hero.quest_taken_by_name('GOLDEN RING')
        TROLL_KING_TAKEN = hero.quest_taken_by_name('TROLL KING')
        TROLL_KING_DONE = hero.quest_done_by_name('TROLL KING')

        if not TROLL_KING_TAKEN and not GOLDEN_RING_TAKEN:
            self.dialog_index = 0
        elif hero.is_in_backpack('Golden ring'):
            self.dialog_index = 1
        elif hero.is_in_backpack('Troll brain'):
            self.dialog_index = 2
        elif TROLL_KING_TAKEN and not GOLDEN_RING_TAKEN and not TROLL_KING_DONE:
            self.dialog_index = 3
        elif not TROLL_KING_TAKEN and GOLDEN_RING_TAKEN:
            self.dialog_index = 4
        elif TROLL_KING_DONE and not GOLDEN_RING_TAKEN:
            self.dialog_index = 5
        elif TROLL_KING_TAKEN and GOLDEN_RING_TAKEN and not TROLL_KING_DONE:
            self.dialog_index = 6
        elif TROLL_KING_DONE and GOLDEN_RING_TAKEN:
            self.dialog_index = 7

        dialog_path = self.dialogs_path[self.dialog_index]
        return self.read_dialog_from_file(dialog_path)

    @staticmethod
    def quest0(hero):
        if hero.quest_taken_by_name("GOLDEN RING"):
            hero.coins += 1000
            hero.remove_from_backpack('Golden ring')
            hero.backpack.append(Item.quest_item("King's store patent"))
            return
        hero.quests.append({
            'name': "GOLDEN RING",
            'description': "King Andrei lost his ring, when he was fighting with trolls."
                           "Probably one one them hide it somewhere in Troll cave - find it and bring to king "
                           "Andrei",
            'COMPLETED': False,
            'reward': {
                'quest': "King's store patent",
                'gold': 1000
            }
        })

    @staticmethod
    def quest1(hero):
        if hero.quest_taken_by_name("TROLL KING") and not hero.quest_done_by_name("TROLL KING"):
            hero.coins += 1000
            hero.remove_from_backpack('Troll brain')
            hero.backpack.append(Item.quest_item("King's brave patent"))
            for quest in hero.quests:
                if quest['name'] == "TROLL KING":
                    quest["COMPLETED"] = True
            cprint(hero.backpack, wait_after=1)
            return
        hero.quests.append({
            'name': "TROLL KING",
            'description': "King Andrei has been wounded in fight with Troll King,"
                           "kill this monster to show King that you are brave enough to go east!",
            'COMPLETED': False,
            'reward': {
                'quest': "King's brave patent",
                'sword': Item.sword(50),  # TODO add item
                'gold': 1000
            }
        })

    def change_dialog_path_and_quests(self, quest0, quest1):
        self.dialogs_path = [
            f'{self.conversation_folder_path}king/king_before_quest.txt',
            f'{self.conversation_folder_path}king/king_get_rin0g.txt',
            f'{self.conversation_folder_path}king/king_get_troll_brain.txt',
            f'{self.conversation_folder_path}king/king_before_golden_ring_quest.txt',
            f'{self.conversation_folder_path}king/king_before_troll_king_quest.txt',
            f'{self.conversation_folder_path}king/king_before_GR_after_kill_Troll.txt',
            f'{self.conversation_folder_path}king/king_after_quests_before_kill_Troll.txt',
            f'{self.conversation_folder_path}king/king_after_quests.txt',
        ]
        self.quest_func = [quest0, quest1]
        self.trade = trade

    @classmethod
    def king(cls, pos_x, pos_y):
        king = cls(
            name="King Andrei",
            position_x=pos_x,
            position_y=pos_y,
            symbol_on_map='#',
            color_on_board=COLOR.YELLOW,
        )

        king.change_dialog_path_and_quests(King.quest0, King.quest1)
        return king


class NPCS:
    troll_king = Troll_king.troll_king
    fake_wall = Fake_wall.fake_wall
    king = King.king

