import arcade
import os
#from PIL import Image
#import assign04


#image = Image.open(assign04)
#image.save("NewImage", format="PNG")



SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "MICE IN THE KITCHEN"
SCORE = 0

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 140
RIGHT_MARGIN = 150

# Physics
MOVEMENT_SPEED = 7
JUMP_SPEED = 15
GRAVITY = 0.5   


class MyGame(arcade.Window):
    """ Main application class. """
    
    def __init__(self):
        """
        Initializer
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        #self.background = arcade.cleanup_texture_cache("NewImage")
        self.platform_list = None
        self.enemy_list = None
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False
        self.SCORE = 3

    def setup(self):
        """ Set up the game and initialize the variables. """     

        # Sprite lists
        self.platform_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Draw the walls on the bottom
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            counter = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)

            counter.bottom = 0
            counter.left = x
            self.platform_list.append(counter)

        # Draw the platforms
        for x in range(SPRITE_SIZE * 3, SPRITE_SIZE * 8, SPRITE_SIZE):
            shelf1 = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)

            shelf1.bottom = 190
            shelf1.left = x
            shelf1.width = 150
            self.platform_list.append(shelf1)

            shelf2 = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)

            shelf2.bottom = 350
            shelf2.left= 550
            shelf2.width = 250
            self.platform_list.append(shelf2)

            shelf3 = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)

            shelf3.bottom = 400
            shelf3.left= 50
            shelf3.width = 300
            self.platform_list.append(shelf3)

            shelf4 = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)

            shelf4.bottom = 500
            shelf4.left= 400
            shelf4.width = 200
            self.platform_list.append(shelf4)

            shelf5 = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)

            shelf5.bottom = 680
            shelf5.left= 600
            shelf5.width = 360
            self.platform_list.append(shelf5)
        # Draw the mushrooms
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 3):
            shelf1 = arcade.Sprite(":resources:images/tiles/mushroomRed.png", SPRITE_SCALING)

            shelf1.bottom = SPRITE_SIZE
            shelf1.left = x
            self.platform_list.append(shelf1)

        # -- Draw an enemy on the ground
        enemy = arcade.Sprite(":resources:images/enemies/mouse.png", SPRITE_SCALING)

        enemy.bottom = SPRITE_SIZE
        enemy.left = SPRITE_SIZE * 2

        # Set enemy initial speed
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        # -- Draw a enemies on the shelves
        enemy = arcade.Sprite(":resources:images/enemies/mouse.png", SPRITE_SCALING)

        enemy.bottom = SPRITE_SIZE * 4
        enemy.left = SPRITE_SIZE * 4

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = SPRITE_SIZE * 8
        enemy.boundary_left = SPRITE_SIZE * 3
        enemy.change_x = 2
        self.enemy_list.append(enemy)


        enemy = arcade.Sprite(":resources:images/enemies/mouse.png", SPRITE_SCALING)

        enemy.bottom = 565
        enemy.left = 400

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 530
        enemy.boundary_left = 320
        enemy.change_x = 2
        self.enemy_list.append(enemy)



        # -- Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
                                           SPRITE_SCALING)
        self.player_list.append(self.player_sprite)

        # Starting position of the player
        self.player_sprite.center_x = 24
        self.player_sprite.center_y = 270

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.platform_list,
                                                             gravity_constant=GRAVITY)
        
        self.player_sprite.boundary_left= 20
        self.player_sprite.boundary_right=800
        # Set the background color
        arcade.set_background_color(arcade.color.BONE)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()
        #draw kitchen background
        


        #set up score on game
        arcade.draw_rectangle_filled(100,750, 180, 60, arcade.color.FUCHSIA_PINK,0)
        arcade.draw_rectangle_filled(100,750, 175, 55, arcade.color.LIGHT_BLUE,0)   
        arcade.draw_text(f"LIVES: {self.SCORE}", 25 , 740, arcade.color.RED, 25, 50,"left","calibri", True, False, "left", "baseline", False, 0)        

        # Draw all the sprites.
        self.player_list.draw()
        self.platform_list.draw()
        self.enemy_list.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update the player based on the physics engine
        if not self.game_over:
            # Move the enemies
            self.enemy_list.update()

            # Check each enemy
            for enemy in self.enemy_list:
                # If the enemy hit a wall, reverse
                if len(arcade.check_for_collision_with_list(enemy, self.platform_list)) > 0:
                    enemy.change_x *= -1
                # If the enemy hit the left boundary, reverse
                elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                    enemy.change_x *= -1
                # If the enemy hit the right boundary, reverse
                elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                    enemy.change_x *= -1

            # Update the player using the physics engine
            self.physics_engine.update()

            # See if the player hit a worm. If so, game over.
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)) > 0:
                self.game_over = True

                if self.game_over == True:
                    self.SCORE -= 1
                    self.game_over = False
                    self.setup()

                    if self.SCORE == 0:
                        self.game_over = True
                        self.SCORE ==3

                        if self.game_over == True:
                            self.game_over = True

                        


class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.MEDIUM_AQUAMARINE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
    
    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_text("Mice in the Kitchen", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=70, anchor_x="center")
        arcade.draw_text("click the X to start!", self.window.width / 2, self.window.height / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)      
            

def main():

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


    window = MyGame()
    window.setup()    
    arcade.run()


if __name__ == "__main__":
    main()
