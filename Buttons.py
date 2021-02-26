import pygame
from Colours import Colors

class Button():
    def __init__(self, x, y, width, height, startcolor, text, border_width, text_color, window):
        self.startcolor = startcolor
        self.color = self.startcolor
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_width = border_width
        self.text = text
        self.hover_text_color = text_color
        self.start_text_color = text_color
        self.text_color = text_color
        self.visible = True
        self.hover_colour = self.startcolor
        self.window = window
        self.game_mode = None

    def set_visible(self, visible):
        self.visible = visible

    def get_mode(self):
        return self.game_mode

    @staticmethod
    def button_draw(*args):
        if type(args[0]) == list:
            for button in args[0]:
                button.draw()
                button.is_over(pygame.mouse.get_pos())
        else:
            for button in args:
                button.draw()
                button.is_over(pygame.mouse.get_pos())

    @staticmethod
    def button_disappear(*args):
        if type(args[0]) == list:
            for button in args[0]:
                button.set_visible(False)
        else:
            for button in args:
                button.set_visible(False)

    def draw(self, outline=None):
        # Call this method to draw the button on the screen
        if self.visible:
            if outline:
                pygame.draw.rect(self.window, outline, (self.x-self.border_width, self.y-self.border_width,
                                                self.width+2*self.border_width, self.height+2*self.border_width), 0)

            pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = pygame.font.SysFont('comicsans', 20)
                text = font.render(self.text, True, self.text_color)
                self.window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y +
                                (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.visible:
            if self.x < pos[0] < self.x + self.width:
                if self.y < pos[1] < self.y + self.height:
                    self.color = self.hover_colour
                    self.text_color = self.hover_text_color
                    return True
        self.color = self.startcolor
        self.text_color = self.start_text_color
        return False

    def clicked(self):
        self.visible = False


class PvPButton(Button):
    def __init__(self, window, window_dimensions):
        self.width, self.height = 75, 40
        x = window_dimensions[0]//2 - self.width//2
        y = window_dimensions[1]//2 - self.height//2
        Button.__init__(self, x, y, self.width, self.height, (50, 50, 50), "PvP", 2, (200, 200, 200), window)
        self.hover_colour = Colors["darkGreen"]
        self.hover_text_color = Colors["paleTurquoise"]
        self.game_mode = "pvp"


class CompButton(Button):
    def __init__(self, window, window_dimensions):
        self.width, self.height = 75, 40
        x = window_dimensions[0]//2 - (self.width*1.75)//1
        y = window_dimensions[1]//2 - self.height//2
        Button.__init__(self, x, y, self.width, self.height, (50, 50, 50), "Comp", 2, (200, 200, 200), window)
        self.hover_colour = Colors["darkPurple"]
        self.hover_text_color = Colors["lightYellow"]
        self.game_mode = "comp"


class PvPOnlineButton(Button):
    def __init__(self, window, window_dimensions):
        self.width, self.height = 75, 40
        x = window_dimensions[0]//2 + (self.width*0.75)//1
        y = window_dimensions[1]//2 - self.height//2
        Button.__init__(self, x, y, self.width, self.height, (50, 50, 50), "Online", 2, (200, 200, 200), window)
        self.hover_colour = Colors["darkPurple"]
        self.hover_text_color = Colors["lightYellow"]
        self.game_mode = "online"
