@namespace
class SpriteKind:
    Stick_figer = SpriteKind.create()

def on_a_released():
    music.stop_all_sounds()
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def on_player2_connected():
    global mySprite2
    controller.player2.move_sprite(mySprite)
    mySprite2 = sprites.create(assets.image("""
            TheChosenOne
        """),
        SpriteKind.Stick_figer)
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

mySprite2: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(assets.image("""
    mouseClicer
"""), SpriteKind.player)
scene.set_background_image(assets.image("""
    win 11
"""))
mySprite.set_stay_in_screen(True)
controller.move_sprite(mySprite)

def on_forever():
    music.play_melody("B A F G A G A C5 ", 120)
forever(on_forever)
