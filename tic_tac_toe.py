import random as r
import ion as i
import kandinsky as k
import time as t

class gv:  #global variables
  bxx  = 70            # box lenght, 70 is the best, 102 makes the game stretched
  bxy  = 70            # box height, 70 is the best
  gx   = 52            # global x, should be (320 - (2*x_sp + 3*bxx)) / 2
  gy   = 3             # global y
  usx  = 12            # symbol unit x size, default=12, 19 when stretched game
  usy  = 12            # symbol unit y size
  x_sp = 3             # x column spacing
  y_sp = 3             # y line spacing
  cw   = 2             # cursor width
  bgc  = (0, 0, 0)     # background color
  bxc  = (75, 75, 75)  # box color
  cc   = (0, 0, 255)   # cursor color
  cp1  = (255, 0, 0)   # color player 1
  cp2  = (0, 255, 0)   # color player 1
  lcol = [0, 127, 255] # list of numbers used to generate a random color in welcome screen

class draw:
  cross = "1000101010001000101010001"
  round = "0111010001101011000101110"

  def board(bg=gv.bgc, bx=gv.bxc):
    """
Draw the main board game with empty boxes.
    """
    k.fill_rect(0,0,320,222,bg) # fill screen
    for x in range(3):
      for y in range(3):
        temp_x = gv.gx + x*(gv.bxx+gv.x_sp)
        temp_y = gv.gy + y*(gv.bxy+gv.y_sp)
        k.fill_rect(temp_x, temp_y, gv.bxx, gv.bxy, bx)

  def symbol(x, y, symbol, color):
    """
Draw symbol in box (x,y) in color.
Look at cross and round in class draw for syntax example.
    """
    for i in range(25):
      if symbol[i]=="1":
        temp_x = int(gv.gx + x*(gv.bxx+gv.x_sp) + i//5*gv.usx + 5) # add spacing betwen box border and symbol
        temp_y = int(gv.gy + y*(gv.bxy+gv.y_sp) + i%5 *gv.usy + 5) # int is used for welcome screen
        k.fill_rect(temp_x, temp_y, gv.usx, gv.usy, color)

  def cursor(x, y, color):
    temp_x = gv.gx + x*(gv.bxx+gv.x_sp)
    temp_y = gv.gy + y*(gv.bxy+gv.y_sp)
    k.fill_rect(temp_x, temp_y, gv.cw, gv.bxy, color)
    k.fill_rect(temp_x, temp_y, gv.bxx, gv.cw, color)
    temp_x += gv.bxx-gv.cw
    k.fill_rect(temp_x, temp_y, gv.cw, gv.bxy, color)
    temp_x -= gv.bxx-gv.cw
    temp_y += gv.bxy-gv.cw
    k.fill_rect(temp_x, temp_y, gv.bxx, gv.cw, color)

class welcome:
  """
Welcome screen showing how to use the script
  """
  def thank_you():
    k.fill_rect(0, 0, 320, 222, (0,0,0))
    k.draw_string("Thank you for playing my game!", 10, 153, (255,0,127), (0,0,0))
    k.draw_string("Power to continue\nOK to skip tuto", 201, 196, (255,255,255), (0,0,0), 1)
    draw.symbol(0, 0.7, draw.round, gv.cp1)
    k.draw_string("VS", 150, 85, (255,255,0), (0,0,0))
    draw.symbol(2, 0.7, draw.cross, gv.cp2)
    while not (i.keydown(i.KEY_ONOFF) or i.keydown(i.KEY_OK)):
      color = (r.choice(gv.lcol), r.choice(gv.lcol), r.choice(gv.lcol))
      k.draw_string("Tic Tac Toe", 94, 0, color, (0,0,0))
    while i.keydown(i.KEY_ONOFF):pass
    return i.get_keys()

  def tutorial():
    k.fill_rect(0, 0, 320, 222, (0,0,0))
    k.draw_string("  Use arrow keys to move\n\nYou can pass through walls", 30, 100, (255,0,127), (0,0,0))
    k.draw_string("Power to continue", 201, 209, (255,255,255), (0,0,0), 1)
    while not i.keydown(i.KEY_ONOFF):
      color = (r.choice(gv.lcol), r.choice(gv.lcol), r.choice(gv.lcol))
      k.draw_string("Tic Tac Toe", 94, 0, color, (0,0,0))
    while i.keydown(i.KEY_ONOFF):pass
    k.fill_rect(0, 0, 320, 222, (0,0,0))
    k.draw_string("Use home key to place pawns\n\n Pawns are auto calculated", 25, 100, (255,0,127), (0,0,0))
    k.draw_string("Power to continue", 201, 209, (255,255,255), (0,0,0), 1)
    while not i.keydown(i.KEY_ONOFF):
      color = (r.choice(gv.lcol), r.choice(gv.lcol), r.choice(gv.lcol))
      k.draw_string("Tic Tac Toe", 94, 0, color, (0,0,0))
    while i.keydown(i.KEY_ONOFF):pass
    k.fill_rect(0, 0, 320, 222, (0,0,0))
    k.draw_string("ENJOY ;-)", 115, 100, (255,0,127), (0,0,0))
    k.draw_string("Power to start", 222, 209, (255,255,255), (0,0,0), 1)
    while not i.keydown(i.KEY_ONOFF):
      color = (r.choice(gv.lcol), r.choice(gv.lcol), r.choice(gv.lcol))
      k.draw_string("Tic Tac Toe", 94, 0, color, (0,0,0))

def init():
  global cux, cuy, player
  if "OK" not in welcome.thank_you():
    welcome.tutorial()
  player = 0  # player turn
  cux    = 0  # cursor x
  cuy    = 0  # cursor y
  draw.board()
  draw.cursor(cux, cuy, gv.cc)

# main
init()
while not i.keydown(i.KEY_BACKSPACE):
#  k.draw_string(f"[{cux},{cuy}]",0,0)
  if 'left' in i.get_keys() or 'right' in i.get_keys() or 'down' in i.get_keys() or 'up' in i.get_keys():
    draw.cursor(cux, cuy, gv.bxc) # erase cursor
    cux = (cux + i.keydown(i.KEY_RIGHT)-i.keydown(i.KEY_LEFT)) % 3
    cuy = (cuy + i.keydown(i.KEY_DOWN) -i.keydown(i.KEY_UP))   % 3
    draw.cursor(cux, cuy, gv.cc)  # update cursor
    t.sleep(0.1)                  # add cooldown
  if i.keydown(i.KEY_HOME):
    if player:  # player = 1
      draw.symbol(cux, cuy, draw.round, gv.cp1)
    else:
      draw.symbol(cux, cuy, draw.cross, gv.cp2)
    player = (player+1)%2
    t.sleep(0.2) # add cooldown
