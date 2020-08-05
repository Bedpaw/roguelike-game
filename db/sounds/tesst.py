# import pygame
# import os
#
#
#
# class Pause(object):
#
#     def __init__(self):
#         self.paused = pygame.mixer.music.get_busy()
#
#     def toggle(self):
#         if self.paused:
#             pygame.mixer.music.unpause()
#         if not self.paused:
#             pygame.mixer.music.pause()
#         self.paused = not self.paused
#
# path = 'board_music_forest.mp3'
# path2 = 'board_music_inferno.mp3'
# pygame.mixer.init()
# pygame.mixer.music.load(path)
# pygame.mixer.music.play()
# # s_goblin = pygame.mixer.Sound('battle/sword_attack.wav')
#
# def l_dir(dir_path):
#     f = os.listdir(dir_path)
#     for sound in f:
#         path = sound
#         print(path)
#         s = pygame.mixer.Sound(f'{dir_path}/{path}')
#         s.play()
#         input()
#
# l_dir('monsters')