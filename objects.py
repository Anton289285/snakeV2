from tkinter import *
from random import *
import constant as const
import rec_mod as rec
import can_vid_mod as cvid

class Some_window:
    root = Tk()
    def __init__(self):
        self.root.title("Змейка")

class Some_canvas:
    canvas_grid = []

    def __init__(self, some_window):
        self.style = "normal"
        self.canvas = Canvas(some_window.root,
                             width = const.quantity_of_column_row *
                             const.size_of_column_row,
                             height = const.quantity_of_column_row *
                             const.size_of_column_row,
                             bg = "green")

        self.canvas.grid(column = 0, row = 0, columnspan = 2)
        for i in range(1, const.quantity_of_column_row):
            self.canvas_grid.append(self.canvas.create_line
                                    (0, i * const.size_of_column_row,
                                    const. size_of_column_row *
                                    const.quantity_of_column_row,
                                    i * const.size_of_column_row,
                                    fill = "darkgreen"))
            self.canvas_grid.append(self.canvas.create_line
                                    (i *const.size_of_column_row, 0,
                                    i * const.size_of_column_row,
                                    const.size_of_column_row *
                                    const.quantity_of_column_row,
                                    fill = "darkgreen"))

    def change_style(self, some_style):
        if (some_style == "extra"):
            self.canvas.config(bg  =  "firebrick1")
            for i in range(len(self.canvas_grid)):
                self.canvas.itemconfig(self.canvas_grid[i],
                                       fill = "firebrick3")
        elif (some_style == "low"):
            self.canvas.config(bg = "blue")
            for i in range(len(self.canvas_grid)):
                self.canvas.itemconfig(self.canvas_grid[i],
                                       fill = "cyan2")
        elif (some_style == "normal"):
            self.canvas.config(bg = "green")
            for i in range(len(self.canvas_grid)):
                self.canvas.itemconfig(self.canvas_grid[i],
                                       fill = "darkgreen")


class Some_info:
    def __init__(self, some_window):
        self.window = some_window
        self.apple_value = 0
        self.info_value = ""
        self.speed_value = "0"
        self.record_value = 0
        self.apple_label = Label(self.window.root, text = "apple: "
                                  + str(self.apple_value),
                                 font = "arial 15", bd = 5)
        self.apple_label.grid(column = 0, row = 1)
        self.info_label = Label(self.window.root, text = self.info_value,
                                font = "arial 30")
        self.info_label.grid(column = 0, row = 2, columnspan = 2)
        self.speed_label = Label(self.window.root, text = "speed: "
                                 + str(self.speed_value),
                                 font = "arial 15")
        self.speed_label.grid(column = 1, row = 1)
        self.record_label = Label(self.window.root, text = "record: "
                                  + str(self.record_value),
                                  font = "arial 15")
        self.record_label.grid(column = 0, row = 3, columnspan = 2)

    def update_value(self, some_value_for_update, value):
        if (some_value_for_update == "apple"):
            if (value == "+"):
                self.apple_value = self.apple_value + 1
                self.apple_label.config(text = "apple: " + str(self.apple_value))
            elif (value == "0"):
                self.apple_value = 0
                self.apple_label.config(text = "apple: " + str(self.apple_value))
        elif (some_value_for_update == "info"):
            self.info_value = value
            self.info_label.config(text = self.info_value)
        elif (some_value_for_update == "speed"):
            self.speed_value = value
            self.speed_label.config(text = "speed: " + str(self.speed_value))
        elif(some_value_for_update == "record"):
            self.record_value = value
            self.record_label.config(text = "record: " + str(self.record_value))


class Some_segment:
    def __init__(self, some_canvas, some_style, some_column, some_row):
        self.column = some_column
        self.row = some_row
        self.canvas = some_canvas
        if (some_style == "segment_style_head"):
            self.style = "segment_style_head"
            self.body = some_canvas.create_rectangle(self.column * const.size_of_column_row,
                                                     self.row * const.size_of_column_row,
                                                     (self.column + 1) * const.size_of_column_row,
                                                     (self.row + 1) * const.size_of_column_row,
                                                     fill = const.segment_style_head_color)

        elif (some_style == "segment_style1"):
            self.style = "segment_style1"
            self.body = some_canvas.create_rectangle(self.column * const.size_of_column_row,
                                                     self.row * const.size_of_column_row,
                                                     (self.column + 1) * const.size_of_column_row,
                                                     (self.row + 1) * const.size_of_column_row,
                                                     fill = const.segment_style1_color)
        elif (some_style == "segment_style2"):
            self.style = "segment_style2"
            self.body = some_canvas.create_rectangle(self.column * const.size_of_column_row,
                                                     self.row * const.size_of_column_row,
                                                     (self.column + 1) * const.size_of_column_row,
                                                     (self.row + 1) * const.size_of_column_row,
                                                     fill = const.segment_style2_color)
        elif (some_style == "segment_style3"):
            self.style = "segment_style3"
            self.body = some_canvas.create_rectangle(self.column * const.size_of_column_row,
                                                     self.row * const.size_of_column_row,
                                                     (self.column + 1) * const.size_of_column_row,
                                                     (self.row + 1) * const.size_of_column_row,
                                                     fill = const.segment_style3_color)
        elif (some_style == "segment_style_tail"):
            self.style = "segment_style_tail"
            self.body = some_canvas.create_rectangle(self.column * const.size_of_column_row,
                                                     self.row * const.size_of_column_row,
                                                     (self.column + 1) * const.size_of_column_row,
                                                     (self.row + 1) * const.size_of_column_row,
                                                     fill = const.segment_style_tail_color)

    def move_to(self, column, row):
        self.column = column
        self.row = row
        self.canvas.coords(self.body, (column * const.size_of_column_row),
                           (row * const.size_of_column_row),
                           (column * const.size_of_column_row + const.size_of_column_row),
                           (row * const.size_of_column_row + const.size_of_column_row))

    def change_style(self, some_new_style):
        self.style = some_new_style
        if (some_new_style == "segment_style_head"):
            self.canvas.itemconfig(self.body, fill = const.segment_style_head_color)
        elif (some_new_style == "segment_style1"):
            self.canvas.itemconfig(self.body, fill = const.segment_style1_color)
        elif (some_new_style == "segment_style2"):
            self.canvas.itemconfig(self.body, fill = const.segment_style2_color)
        elif (some_new_style == "segment_style3"):
            self.canvas.itemconfig(self.body, fill = const.segment_style3_color)
        elif (some_new_style == "segment_style_tail"):
            self.canvas.itemconfig(self.body, fill = const.segment_style_tail_color)

    def change_style_to_dead(self):
        if (self.style == "segment_style_head"):
            self.canvas.itemconfig(self.body, fill = const.segment_style_head_color_dead)
        elif (self.style == "segment_style1"):
            self.canvas.itemconfig(self.body, fill = const.segment_style1_color_dead)
        elif (self.style == "segment_style2"):
            self.canvas.itemconfig(self.body, fill = const.segment_style2_color_dead)
        elif (self.style == "segment_style3"):
            self.canvas.itemconfig(self.body, fill = const.segment_style3_color_dead)
        elif (self.style == "segment_style_tail"):
            self.canvas.itemconfig(self.body, fill = const.segment_style_tail_color_dead)

    def change_style_to_heaven(self):
        if (self.style == "segment_style_head"):
            self.canvas.itemconfig(self.body, fill = const.segment_style_head_color_heaven)
        elif (self.style == "segment_style1"):
            self.canvas.itemconfig(self.body, fill = const.segment_style1_color_heaven)
        elif (self.style == "segment_style2"):
            self.canvas.itemconfig(self.body, fill = const.segment_style2_color_heaven)
        elif (self.style == "segment_style3"):
            self.canvas.itemconfig(self.body, fill = const.segment_style3_color_heaven)
        elif (self.style == "segment_style_tail"):
            self.canvas.itemconfig(self.body, fill = const.segment_style_tail_color_heaven)

    def rotate_style(self):
        if self.style == "segment_style_head":
            pass
        elif self.style == "segment_style1":
            self.change_style("segment_style3")
        elif self.style == "segment_style2":
            self.change_style("segment_style1")
        elif self.style == "segment_style3":
            self.change_style("segment_style2")
        elif self.style == "segment_style_tail":
            pass

    def delete(self):
        self.canvas.delete(self.body)


class Some_snake:

    body = []

    def __init__(self, some_canvas):
        self.canvas = some_canvas
        self.body.append(Some_segment(self.canvas, "segment_style_head",
                                      int(const.quantity_of_column_row/2),
                                      int(const.quantity_of_column_row/2)))
        self.body.append(Some_segment(self.canvas, "segment_style1",
                                      int(const.quantity_of_column_row/2),
                                      int(const.quantity_of_column_row/2 + 1)))
        self.body.append(Some_segment(self.canvas, "segment_style2",
                                      int(const.quantity_of_column_row/2),
                                      int(const.quantity_of_column_row/2 + 2)))
        self.body.append(Some_segment(self.canvas, "segment_style3",
                                      int(const.quantity_of_column_row/2),
                                      int(const.quantity_of_column_row/2 + 3)))
        self.body.append(Some_segment(self.canvas, "segment_style_tail",
                                      int(const.quantity_of_column_row/2),
                                      int(const.quantity_of_column_row/2 + 4)))


    def generate(self):
        self.body.append(Some_segment(self.canvas, "segment_style_head",
                                      int(const.quantity_of_column_row/2),
                                      int(const.quantity_of_column_row/2)))
        self.body.append(Some_segment(self.canvas, "segment_style1",
                                      int(const.quantity_of_column_row/2),
                                      int(const.quantity_of_column_row/2 + 1)))
        self.body.append(Some_segment(self.canvas, "segment_style2",
                                      int(const.quantity_of_column_row/2),
                                      int(const.quantity_of_column_row/2 + 2)))
        self.body.append(Some_segment(self.canvas, "segment_style3",
                                      int(const.quantity_of_column_row/2),
                                      int(const.quantity_of_column_row/2 + 3)))
        self.body.append(Some_segment(self.canvas, "segment_style_tail",
                                      int(const.quantity_of_column_row/2),
                                      int(const.quantity_of_column_row/2 + 4)))

    def rotate_style(self):
        for i in range(len(self.body)):
            self.body[i].rotate_style()

    def change_style_to_death(self):
        for i in range(len(self.body)):
            self.body[i].change_style_to_dead()

    def change_style_to_heaven(self):
        for i in range(len(self.body)):
            self.body[i].change_style_to_heaven()

    def move(self, some_movement):
        self.column_last = self.body[(len(self.body) - 1)].column
        self.row_last = self.body[(len(self.body) - 1)].row
        if some_movement == "left":
            for i in range((len(self.body) - 1), 0, -1):
                self.body[i].move_to(self.body[i-1].column,
                                     self.body[i-1].row)
            self.body[0].move_to(self.body[0].column - 1,
                                 self.body[0].row)
        if some_movement == "right":
            for i in range((len(self.body) - 1), 0, -1):
                self.body[i].move_to(self.body[i-1].column,
                                     self.body[i-1].row)
            self.body[0].move_to(self.body[0].column + 1,
                                 self.body[0].row)
        if some_movement == "up":
            for i in range((len(self.body) - 1), 0, -1):
                self.body[i].move_to(self.body[i-1].column,
                                     self.body[i-1].row)
            self.body[0].move_to(self.body[0].column,
                                 self.body[0].row - 1)
        if some_movement == "down":
            for i in range((len(self.body) - 1), 0, -1):
                self.body[i].move_to(self.body[i-1].column,
                                     self.body[i-1].row)
            self.body[0].move_to(self.body[0].column,
                                 self.body[0].row + 1)

    def append(self):
        if (self.body[(len(self.body) - 2)].style == "segment_style1"):
            self.body[len(self.body) - 1].change_style("segment_style2")
        elif (self.body[(len(self.body) - 2)].style == "segment_style2"):
            self.body[len(self.body) - 1].change_style("segment_style3")
        elif (self.body[(len(self.body) - 2)].style == "segment_style3"):
            self.body[len(self.body) - 1].change_style("segment_style1")
        self.body.append(Some_segment(self.canvas, "segment_style_tail",
                                      self.column_last, self.row_last))
    def delete(self):
        for i in range(len(self.body)):
            self.body[i].delete()
        self.body.clear()



class Some_apple:
    def __init__(self, some_canvas, some_column, some_row):
        self.canvas = some_canvas
        self.column = some_column
        self.row = some_row
        self.body = self.canvas.create_rectangle(self.column * const.size_of_column_row,
                                                 self.row *const.size_of_column_row,
                                                 (self.column + 1)*const.size_of_column_row,
                                                 (self.row + 1)*const.size_of_column_row,
                                                 fill = "red")

    def delete(self):
        self.column = - 5
        self.row = - 5
        self.canvas.delete(self.body)

    def generate(self, some_column, some_row):
        self.column = some_column
        self.row = some_row
        self.body = self.canvas.create_rectangle(self.column * const.size_of_column_row,
                                                 self.row * const.size_of_column_row,
                                                 (self.column + 1)*const.size_of_column_row,
                                                 (self.row + 1)*const.size_of_column_row,
                                                 fill = "red")


class Some_game:

    def __init__(self):
        self.window = Some_window()
        self.canvas = Some_canvas(self.window)
        self.info = Some_info(self.window)
        self.info.update_value("apple", "0")
        self.snake = Some_snake(self.canvas.canvas)
        self.direction = "up"
        self.apple = Some_apple(self.canvas.canvas, 2, 2)
        self.apple.delete()
        self.locate_apple_with_rand_coord()
        self.game_status = "pause"
        self.info.update_value("info", self.game_status)
        self.game_speed = 2
        self.info.update_value("speed", self.game_speed)
        self.record = rec.Some_record('./record/record.txt')
        self.info.update_value("record", self.record.apple)
        self.record_for_heaven = rec.Some_record('./record/record_heaven.txt')
        self.trigger = False
        self.canvas_vidjet = cvid.Canvas_widjet(const.quantity_of_column_row,
                                                const.size_of_column_row,
                                                self.canvas.canvas,
                                                self.window.root,
                                                self.record.recordsman)

    def set_move_left(self, event):
        if (((self.snake.body[0].column - 1) != self.snake.body[1].column) or
            (self.snake.body[0].row != self.snake.body[1].row)):
                self.direction = "left"

    def set_move_right(self, event):
        if (((self.snake.body[0].column + 1) != self.snake.body[1].column) or
            (self.snake.body[0].row != self.snake.body[1].row)):
                self.direction = "right"

    def set_move_up(self, event):
        if ((self.snake.body[0].column != self.snake.body[1].column) or
            ((self.snake.body[0].row - 1) != self.snake.body[1].row)):
                self.direction = "up"

    def set_move_down(self, event):
        if ((self.snake.body[0].column != self.snake.body[1].column) or
            ((self.snake.body[0].row + 1) != self.snake.body[1].row)):
                self.direction = "down"

    def move_snake(self):
        if self.direction == "left":
            self.snake.move("left")
        elif self.direction == "right":
            self.snake.move("right")
        elif self.direction == "up":
            self.snake.move("up")
        elif self.direction == "down":
            self.snake.move("down")

        if not(self.check_self_crossing() or self.check_way_out()):
            self.snake_append_apple()
            if len(self.snake.body) == ((const.quantity_of_column_row *
                                         const.quantity_of_column_row) - 1):
                self.game_status = "heaven"
                self.snake.change_style_to_heaven()
                self.canvas_vidjet.draw(self.info.apple_value, "The chosen one")
                self.id_for_unbind_enter = self.window.root.bind("<Return>",
                                                                 self.heaven)
            else:
                self.anchor_move_snake = self.window.root.after(self.translate_speed_to_time_delay(), self.move_snake)
                self.snake.rotate_style()
        else:
            self.snake.change_style_to_death()
            self.game_status = "game over"
            self.info.update_value("info", self.game_status)
            if self.trigger == True:
                self.game_status = "enter record"
                self.canvas_vidjet.draw(self.info.apple_value, self.record.recordsman)
                self.id_for_unbind_enter = self.window.root.bind("<Return>",
                                                                 self.redraw_canvas_widjet)


    def heaven(self, event):
        string = self.canvas_vidjet.entry.get()
        self.record_for_heaven.update(string, self.info.apple_value)
        self.canvas_vidjet.erase()
        self.window.root.unbind("<Return>")
        self.game_status = "game over"


    def redraw_canvas_widjet(self, event):
        string = self.canvas_vidjet.entry.get()
        self.record.update(string, self.info.apple_value)
        self.canvas_vidjet.erase()
        self.window.root.unbind("<Return>")
        self.game_status = "game over"


    def check_self_crossing(self):
        self_crossing = False
        for i in range(1, (len(self.snake.body)), 1):
            if ((self.snake.body[0].column == self.snake.body[i].column)
                and (self.snake.body[0].row == self.snake.body[i].row)):
                self_crossing = True
        return self_crossing

    def check_way_out(self):
        way_out = False
        if ((self.snake.body[0].column < 0)
            or (self.snake.body[0].column > const.quantity_of_column_row - 1)
            or (self.snake.body[0].row < 0)
            or (self.snake.body[0].row > const.quantity_of_column_row - 1)):
                way_out = True
        return way_out

    def snake_append_apple(self):
        if ((self.snake.body[0].column == self.apple.column)
            and (self.snake.body[0].row == self.apple.row)):
                self.snake.append()
                self.apple.delete()
                self.locate_apple_with_rand_coord()
                self.info.update_value("apple", "+")
                if ((self.record.apple < self.info.apple_value) and
                    (self.trigger == False)):
                    self.canvas.change_style("low")
                    self.trigger = True

    def game_restart(self, event):
        if self.game_status == "game over":
            self.window.root.after_cancel(self.anchor_move_snake)
            self.apple.delete()
            self.info.update_value("apple", "0")
            self.snake.delete()
            self.snake.generate()
            self.locate_apple_with_rand_coord()
            self.anchor_move_snake = self.window.root.after(self.translate_speed_to_time_delay(),
                                                            self.move_snake)
            self.direction = "up"
            self.game_status = "play"
            self.info.update_value("info", self.game_status)
            self.info.update_value("record", self.record.apple)
            self.canvas.change_style("normal")
            self.trigger = False

    def pause(self, event):
        if self.game_status == "play":
            self.window.root.after_cancel(self.anchor_move_snake)
            self.game_status = "pause"
            self.info.update_value("info", self.game_status)
        elif self.game_status == "pause":
            self.anchor_move_snake = self.move_snake()
            self.game_status = "play"
            self.info.update_value("info", self.game_status)
        elif self.game_status == "game over":
            pass

    def locate_apple_with_rand_coord(self):
        generate_list_column = []
        generate_list_row = []
        result_coord = []
        for column in range(0, const.quantity_of_column_row):
            for row in range(0, const.quantity_of_column_row):
                check = False
                for i in range(0, len(self.snake.body)):
                    if ((self.snake.body[i].column == column) and
                        (self.snake.body[i].row == row)):
                        check = True
                if (check == False):
                    generate_list_column.append(column)
                    generate_list_row.append(row)
        dice = randint(0, (len(generate_list_column) - 1))
        self.apple.generate(generate_list_column[dice], generate_list_row[dice])

    def translate_speed_to_time_delay(self):
        time_delay = 500
        for i in range(self.game_speed):
            time_delay = int(time_delay - time_delay/5)
        return time_delay

    def update_speed(self, event, some_key):
        if some_key == 1:
            self.game_speed = 1
            if self.game_status == "play":
                self.window.root.after_cancel(self.anchor_move_snake)
                self.anchor_move_snake = self.window.root.after(self.translate_speed_to_time_delay(),
                                                                self.move_snake)
        elif some_key == 2:
            self.game_speed = 2
            if self.game_status == "play":
                self.window.root.after_cancel(self.anchor_move_snake)
                self.anchor_move_snake = self.window.root.after(self.translate_speed_to_time_delay(),
                                                                self.move_snake)
        elif some_key == 3:
            self.game_speed = 3
            if self.game_status == "play":
                self.window.root.after_cancel(self.anchor_move_snake)
                self.anchor_move_snake = self.window.root.after(self.translate_speed_to_time_delay(),
                                                                self.move_snake)
        elif some_key == 4:
            self.game_speed = 4
            if self.game_status == "play":
                self.window.root.after_cancel(self.anchor_move_snake)
                self.anchor_move_snake = self.window.root.after(self.translate_speed_to_time_delay(),
                                                                self.move_snake)
        elif some_key == 5:
            self.game_speed = 5
            if self.game_status == "play":
                self.window.root.after_cancel(self.anchor_move_snake)
                self.anchor_move_snake = self.window.root.after(self.translate_speed_to_time_delay(),
                                                                self.move_snake)
        elif some_key == 6:
            self.game_speed = 6
            if self.game_status == "play":
                self.window.root.after_cancel(self.anchor_move_snake)
                self.anchor_move_snake = self.window.root.after(self.translate_speed_to_time_delay(),
                                                                self.move_snake)
        elif some_key == 7:
            self.game_speed = 7
            if self.game_status == "play":
                self.window.root.after_cancel(self.anchor_move_snake)
                self.anchor_move_snake = self.window.root.after(self.translate_speed_to_time_delay(),
                                                                self.move_snake)
        elif some_key == 8:
            self.game_speed = 8
            if self.game_status == "play":
                self.window.root.after_cancel(self.anchor_move_snake)
                self.anchor_move_snake = self.window.root.after(self.translate_speed_to_time_delay(),
                                                                self.move_snake)
        elif some_key == 9:
            self.game_speed = 9
            if self.game_status == "play":
                self.window.root.after_cancel(self.anchor_move_snake)
                self.anchor_move_snake = self.window.root.after(self.translate_speed_to_time_delay(),
                                                                self.move_snake)
        self.info.update_value("speed", self.game_speed)

