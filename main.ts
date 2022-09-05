namespace SpriteKind {
    export const Stick_figer = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Released, function () {
    music.stopAllSounds()
})
controller.B.onEvent(ControllerButtonEvent.Released, function () {
    music.baDing.play()
    game.reset()
})
let mySprite = sprites.create(assets.image`mouseClicer`, SpriteKind.Player)
scene.setBackgroundImage(assets.image`win 11`)
mySprite.setStayInScreen(true)
controller.moveSprite(mySprite)
forever(function () {
    music.playMelody("B A F G A G A C5 ", 120)
})
