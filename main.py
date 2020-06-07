from objects import *
game = Some_game()
game.window.root.bind('<Escape>', quit)
game.window.root.bind('<Left>', game.set_move_left)
game.window.root.bind('<Right>', game.set_move_right)
game.window.root.bind('<Up>', game.set_move_up)
game.window.root.bind('<Down>', game.set_move_down)
game.window.root.bind('<r>', game.game_restart)
game.window.root.bind('<space>', game.pause)

game.window.root.bind('<F1>', lambda event, some_speed = 1:  game.update_speed(event, some_speed))
game.window.root.bind('<F2>', lambda event, some_speed = 2:  game.update_speed(event, some_speed))
game.window.root.bind('<F3>', lambda event, some_speed = 3:  game.update_speed(event, some_speed))
game.window.root.bind('<F4>', lambda event, some_speed = 4:  game.update_speed(event, some_speed))
game.window.root.bind('<F5>', lambda event, some_speed = 5:  game.update_speed(event, some_speed))
game.window.root.bind('<F6>', lambda event, some_speed = 6:  game.update_speed(event, some_speed))
game.window.root.bind('<F7>', lambda event, some_speed = 7:  game.update_speed(event, some_speed))
game.window.root.bind('<F8>', lambda event, some_speed = 8:  game.update_speed(event, some_speed))
game.window.root.bind('<F9>', lambda event, some_speed = 9:  game.update_speed(event, some_speed))

#game.window.root.bind('<w>', game.update_speed)
#game.move_snake()
#game.snake_append_apple()
game.window.root.mainloop()


