import pygame
from util import Util
from define import *

class Text:
    def  __init__(self) -> None:
        self.font_text = pygame.font.Font(link_text , 25)
        self.font_tittle = pygame.font.Font(link_text , 50)

    def show_score(self, surface , score):
        score_text = Util.format_score(score)
        surface.blit(self.font_text.render("Score: " + score_text, True , COLOR_YELLOW),(WINDOW_WIDTH-100 , 10))

    def show_game_over(self, surface):
        text = self.font_tittle.render("GAME OVER" ,True, COLOR_RED)
        text_rect = text.get_rect(center=(POPUP_WIDTH/2, POPUP_HEIGHT/2 - 60))
        surface.blit(text, text_rect)

    def show_game_over_description(self, surface):
        text = self.font_text.render("Space to play again" ,True, COLOR_RED)
        text_rect = text.get_rect(center=(POPUP_WIDTH/2, POPUP_HEIGHT/2))
        surface.blit(text, text_rect)