"""
Starting Template

"""
import arcade
import time
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Potions Class"

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

class TextBox:
    """
    Creates textboxes.
    """
    def __init__(self, text, center_x, center_y):
        self.text = text
        self.center_x = center_x
        self.center_y = center_y

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, len(self.text)*20, 40, arcade.color.WHITE)
        arcade.draw_text(self.text, self.center_x - len(self.text)*5, self.center_y-10, arcade.color.DARK_BROWN, font_size = 18, font_name = "Times", align = "center")

class Question:
    """
    Object to represent a chemistry question.
    """

    def __init__(self):
        self.correct_list = [
        'hydronium', 'dimercury', 'ammonium', 'acetate', 'cyanide',
        'carbonate', 'hydrogen carbonate (bicarbonate)', 'oxalate', 'hypochlorite', 'chlorite',
        'chlorate', 'perchlorate', 'chromate', 'dichromate', 'permanganate',
        'nitrite', 'nitrate', 'peroxide', 'hydroxide', 'phosphate',
        'thiocyanate', 'sulfite', 'sulfate', 'hydrogen sulfate', 'thiosulfate']

        self.correct_dict = {
        'hydronium':'images/q1.png', 'dimercury':'images/q2.png', 'ammonium':'images/q3.png', 'acetate':'images/q4.png', 'cyanide':'images/q5.png',
        'carbonate':'images/q6.png', 'hydrogen carbonate (bicarbonate)':'images/q7.png', 'oxalate':'images/q8.png', 'hypochlorite':'images/q9.png', 'chlorite':'images/q10.png',
        'chlorate':'images/q11.png', 'perchlorate':'images/q12.png', 'chromate':'images/q13.png', 'dichromate':'images/q14.png', 'permanganate':'images/q15.png',
        'nitrite':'images/q16.png', 'nitrate':'images/q17.png', 'peroxide':'images/q18.png', 'hydroxide':'images/q19.png', 'phosphate':'images/q20.png',
        'thiocyanate':'images/q21.png', 'sulfite':'images/q22.png', 'sulfate':'images/q23.png', 'hydrogen sulfate':'images/q24.png', 'thiosulfate':'images/q25.png'
        }
        self.oh_list = ['images/oh1.png', 'images/oh2.png', 'images/oh3.png', 'images/oh4.png', 'images/oh5.png', 'images/oh6.png', 'images/oh7.png', 'images/oh8.png']
        self.coh_list = ['images/coh1.png', 'images/coh2.png', 'images/coh3.png', 'images/coh4.png', 'images/coh5.png', 'images/coh6.png', 'images/coh7.png', 'images/coh8.png', 'images/coh9.png', 'images/coh10.png']
        self.chon_list = ['images/chon1.png', 'images/chon2.png', 'images/chon3.png', 'images/chon4.png', 'images/chon5.png', 'images/chon6.png', 'images/chon7.png', 'images/chon8.png', 'images/chon9.png', 'images/chon10.png', 'images/chon11.png', 'images/chon12.png', 'images/chon13.png', 'images/chon14.png']
        self.hg_list = ['images/hg1.png', 'images/hg2.png', 'images/hg3.png', 'images/hg4.png', 'images/hg5.png', 'images/hg6.png', 'images/hg7.png', 'images/hg8.png', 'images/hg9.png', 'images/hg10.png']
        self.cl_list = ['images/cl1.png', 'images/cl2.png', 'images/cl3.png', 'images/cl4.png', 'images/cl5.png', 'images/cl6.png', 'images/cl7.png', 'images/cl8.png', 'images/cl9.png', 'images/cl10.png', 'images/cl11.png', 'images/cl12.png']
        self.cr_list = ['images/cr1.png', 'images/cr2.png', 'images/cr3.png', 'images/cr4.png', 'images/cr5.png', 'images/cr6.png', 'images/cr7.png', 'images/cr8.png']
        self.mn_list = ['images/mn1.png', 'images/mn2.png', 'images/mn3.png', 'images/mn4.png', 'images/mn5.png', 'images/mn6.png', 'images/mn7.png', 'images/mn8.png']
        self.po_list = ['images/po1.png', 'images/po2.png', 'images/po3.png', 'images/po4.png', 'images/po5.png', 'images/po6.png', 'images/po7.png', 'images/po8.png']
        self.scn_list = ['images/scn1.png', 'images/scn2.png', 'images/scn3.png', 'images/scn4.png', 'images/scn5.png', 'images/scn6.png', 'images/scn7.png', 'images/scn8.png', 'images/scn9.png']
        self.so_list = ['images/so1.png', 'images/so2.png', 'images/so3.png', 'images/so4.png', 'images/so5.png', 'images/so6.png', 'images/so7.png', 'images/so8.png', 'images/so9.png']
        self.hso_list = ['images/hso1.png', 'images/hso2.png', 'images/hso3.png', 'images/hso4.png', 'images/hso5.png', 'images/hso6.png', 'images/hso7.png', 'images/hso8.png', 'images/hso9.png', 'images/hso10.png', 'images/hso11.png']
        self.choice_dict = {
        'hydronium':self.oh_list,
        'dimercury':self.hg_list,
        'ammonium':self.chon_list + [self.correct_dict['hydronium'], self.correct_dict['cyanide']],
        'acetate':self.oh_list + self.coh_list + [self.correct_dict['hydronium'], self.correct_dict['carbonate'], self.correct_dict['hydrogen carbonate (bicarbonate)'], self.correct_dict['oxalate']],
        'cyanide':self.chon_list + [self.correct_dict['ammonium'], self.correct_dict['nitrate'], self.correct_dict['nitrite'], self.correct_dict['thiocyanate']],
        'carbonate':self.coh_list + [self.correct_dict['acetate'], self.correct_dict['hydrogen carbonate (bicarbonate)']],
        'hydrogen carbonate (bicarbonate)':self.coh_list + [self.correct_dict['acetate'], self.correct_dict['carbonate']],
        'oxalate':self.coh_list + ['images/oh6.png', self.correct_dict['peroxide']],
        'hypochlorite':self.cl_list + [self.correct_dict['chlorite'], self.correct_dict['chlorate'], self.correct_dict['perchlorate']],
        'chlorite':self.cl_list + [self.correct_dict['hypochlorite'], self.correct_dict['chlorate'], self.correct_dict['perchlorate']],
        'chlorate':self.cl_list + [self.correct_dict['hypochlorite'], self.correct_dict['chlorite'], self.correct_dict['perchlorate']],
        'perchlorate':self.cl_list + [self.correct_dict['hypochlorite'], self.correct_dict['chlorite'], self.correct_dict['chlorate']],
        'chromate':self.cr_list + [self.correct_dict['dichromate']],
        'dichromate':self.cr_list + [self.correct_dict['chromate']],
        'permanganate':self.mn_list + self.hg_list,
        'nitrite':self.chon_list + [self.correct_dict['ammonium'], self.correct_dict['nitrate'], self.correct_dict['cyanide']],
        'nitrate':self.chon_list + [self.correct_dict['ammonium'], self.correct_dict['cyanide'], self.correct_dict['nitrite']],
        'peroxide':self.oh_list + self.coh_list + [self.correct_dict['hydronium'], self.correct_dict['carbonate'], self.correct_dict['hydrogen carbonate (bicarbonate)'], self.correct_dict['oxalate']],
        'hydroxide':self.oh_list + [self.correct_dict['hydronium'], self.correct_dict['oxalate']],
        'phosphate':self.po_list,
        'thiocyanate':self.scn_list + [self.correct_dict['ammonium'], self.correct_dict['nitrate'], self.correct_dict['nitrite'], self.correct_dict['cyanide']],
        'sulfite':self.so_list + [self.correct_dict['sulfate'], self.correct_dict['thiosulfate']],
        'sulfate':self.so_list + [self.correct_dict['sulfite'], self.correct_dict['thiosulfate']],
        'hydrogen sulfate':self.hso_list,
        'thiosulfate':self.so_list + [self.correct_dict['sulfite'], self.correct_dict['sulfate'], self.correct_dict['thiocyanate']]
        }


        self.chemical = random.choice(self.correct_list)
        self.question = f'Add some {self.chemical} solution.'
        self.correct_choice = None
        self.choice_list = None
        self.position_list = [100, 180, 260, 540, 620, 700]
        #random.shuffle(self.position_list)
        self.position = None
        self.correct_list = [
        'images/q1.png', 'images/q2.png', 'images/q3.png', 'images/q4.png', 'images/q5.png',
        'images/q6.png', 'images/q7.png', 'images/q8.png', 'images/q9.png', 'images/q10.png',
        'images/q11.png', 'images/q12.png', 'images/q13.png', 'images/q14.png', 'images/q15.png',
        'images/q16.png', 'images/q17.png', 'images/q18.png', 'images/q19.png', 'images/q20.png',
        'images/q21.png', 'images/q22.png', 'images/q23.png', 'images/q24.png', 'images/q25.png'
        ]

    def add_sprite(self):
        self.choice_list = random.sample(self.choice_dict[self.chemical], k = 5)
        self.sprite_choice_list = arcade.SpriteList()
        positions = [[80,100], [180,180], [280, 260], [520, 540], [620, 620], [720, 700]]
        random.shuffle(positions)
        x = positions.pop()
        self.correct_choice = arcade.Sprite(self.correct_dict[self.chemical], scale = 0.1, center_x = x[0], center_y = 220)
        self.correct_choice.orig_x = x[1]
        self.sprite_choice_list.append(self.correct_choice)
        for image in self.choice_list:
            x = positions.pop()
            choice = arcade.Sprite(image, scale = 0.1, center_x = x[0], center_y = 220)
            choice.orig_x = x[1]
            self.sprite_choice_list.append(choice)





class Game(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.snape = None
        self.background = None
        self.bottle_list = None
        self.text_list = None
        self.table = None
        self.cauldron = None
        self.move_sound = None
        self.bottle = None
        self.correct = None
        self.text = None

        self.question_list = None
        self.correct_list = None

    def setup(self):
        # Create your sprites and sprite lists here
        self.snape = arcade.Sprite("images/snape.png", scale = 0.5, center_x = 400, center_y = 300)
        self.background = arcade.load_texture("images/classroom.jpg")
        self.table = arcade.Sprite("images/table.png", scale = 0.8, center_x = 400, center_y = 100)
        self.cauldron = arcade.Sprite("images/cauldron.png", scale = 0.18, center_x = 400, center_y = 300)
        self.bottle = None
        self.correct = False

        self.bottle_list = arcade.SpriteList()
        self.bottle1 = arcade.Sprite("images/bottle1.png", scale = 0.21, center_x = 100, center_y = 297)
        self.bottle1.orig_x = self.bottle1.center_x
        self.bottle_list.append(self.bottle1)
        self.bottle2 = arcade.Sprite("images/bottle2.png", scale = 0.27, center_x = 180, center_y = 300)
        self.bottle2.orig_x = self.bottle2.center_x
        self.bottle_list.append(self.bottle2)
        self.bottle3 = arcade.Sprite("images/bottle3.png", scale = 0.6, center_x = 260, center_y = 300)
        self.bottle3.orig_x = self.bottle3.center_x
        self.bottle_list.append(self.bottle3)
        self.bottle4 = arcade.Sprite("images/bottle4.png", scale = 0.67, center_x = 540, center_y = 300)
        self.bottle4.orig_x = self.bottle4.center_x
        self.bottle_list.append(self.bottle4)
        self.bottle5 = arcade.Sprite("images/bottle5.png", scale = 0.2, center_x = 620, center_y = 293)
        self.bottle5.orig_x = self.bottle5.center_x
        self.bottle_list.append(self.bottle5)
        self.bottle6 = arcade.Sprite("images/bottle6.png", scale = 0.31, center_x = 700, center_y = 297)
        self.bottle6.orig_x = self.bottle6.center_x
        self.bottle_list.append(self.bottle6)
        # self.bottle7 = arcade.Sprite("images/bottle7.png", scale = 0.4, center_x = 700, center_y = 285)
        # self.bottle_list.append(self.bottle7)
        # self.bottle8 = arcade.Sprite("images/bottle8.png", scale = 0.67, center_x = 800, center_y = 300)
        # self.bottle_list.append(self.bottle8)
        # self.text = TextBox('NH4+'.translate(SUB), 100, 400)

        self.q1 = Question()
        self.q1.add_sprite()



        self.move_sound = arcade.load_sound("audio/clink.mp3")
        #self.ion_list = arcade.SpriteList()
        # monkey ex
        # for x in range(100,500,100):
        #   banana = arcade.Sprite("file", scale = 0.1,center_x = x, center_y = 400
        #   self.banana_list.append(banana)

        # arcade.draw_text(text, x, y, color, size)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.snape.draw()
        self.table.draw()
        self.cauldron.draw()
        self.bottle_list.draw()
        self.q1.sprite_choice_list.draw()
        arcade.draw_text(self.q1.question, 100, 500, arcade.color.WHITE, 16)
        #self.text.draw()




    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        if self.bottle:
            self.bottle.center_x = x
            self.bottle.center_y = y


    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        for bottle in self.bottle_list:
            if bottle.center_x - 20 < x < bottle.center_x + 20 and bottle.center_y - 50 < y < bottle.center_y + 50:
                self.bottle = bottle

                if self.bottle.orig_x == self.q1.correct_choice.orig_x:
                    self.correct = True
                else:
                    self.correct = False



    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        if self.cauldron.center_x - 70 < x < self.cauldron.center_x + 70 and self.cauldron.center_y - 20 < y < self.cauldron.center_y + 150:
            self.bottle.center_x = 370
            self.bottle.center_y = 400
            self.bottle.angle = 240

            self.bottle_list.remove(self.bottle)
            self.bottle = None

            if self.correct:
                arcade.draw_text("That is correct... How surprising.", 500, 500, arcade.color.WHITE, 16)
                print('Correct')
                self.setup()
            else:
                arcade.draw_text("Incorrect, you half-wit dunderhead.", 500, 500, arcade.color.WHITE, 16)
                print('Incorrect')

        else:
            self.bottle = None




def main():
    """ Main method """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
