import ion as i
import kandinsky as k
import time as t
import mu

class gv:  #global variables
  gx   = 49           # global x
  gy   = 3            # global y
  box  = 70           # box size
  us   = 12           # symbol unit size
  x_sp = 3            # x column spacing
  y_sp = 3            # y line spacing
  cw   = 2            # cursor width
  bgc  = (0, 0, 0)    # background color
  bxc  = (75, 75, 75) # box color
  cc   = (0, 0, 255)  # cursor color
  cp1  = (255, 0, 0)  # color player 1
  cp2  = (0, 255, 0)  # color player 1


class draw:
  cross = "1000101010001000101010001"
  round = "0111010001101011000101110"

  def board(bg=gv.bgc, bx=gv.bxc):
    """
Draw the main board game with empty boxes.
    """
    mu.fill(bg)
    for x in range(3):
      for y in range(3):
        temp_x = gv.gx + x*(gv.box+gv.x_sp)
        temp_y = gv.gy + y*(gv.box+gv.y_sp)
        k.fill_rect(temp_x, temp_y, gv.box, gv.box, bx)

  def symbol(x, y, symbol, color):
    """
Draw symbol in box (x,y) in color.
Look at cross and round in class draw for syntax example.
    """
    for i in range(25):
      if symbol[i]=="1":
        temp_x = gv.gx + x*(gv.box+gv.x_sp) + i//5*gv.us + 5  # Add spacing betwen box border and symbol
        temp_y = gv.gy + y*(gv.box+gv.y_sp) + i%5 *gv.us + 5
        k.fill_rect(temp_x, temp_y, gv.us, gv.us, color)

  def cursor(x, y, color=gv.cc):
    temp_x = gv.gx + x*(gv.box+gv.x_sp)
    temp_y = gv.gy + y*(gv.box+gv.y_sp)
    k.fill_rect(temp_x, temp_y, gv.cw, gv.box, color)
    k.fill_rect(temp_x, temp_y, gv.box, gv.cw, color)
    temp_x += 70-gv.cw
    k.fill_rect(temp_x, temp_y, gv.cw, gv.box, color)
    temp_x -= 70-gv.cw
    temp_y += 70-gv.cw
    k.fill_rect(temp_x, temp_y, gv.box, gv.cw, color)

def init():
  global cux, cuy
  cux = 0  # cursor x
  cuy = 0  # cursor y
  draw.board()
  draw.cursor(cux, cuy)

# Test zone
def test():
  draw.board()
  draw.symbol(0,0,draw.round,(255,0,0))
  draw.symbol(1,0,draw.round2,(255,0,0))
  draw.symbol(0,1,draw.cross,(0,255,0))
  draw.cursor(0,2)
  draw.cursor(1,2)
  draw.cursor(2,2)
  draw.symbol(0,2,draw.round,(255,0,0))
  draw.symbol(1,2,draw.cross,(0,255,0))

# main
init()
while not i.keydown(i.KEY_BACKSPACE):
  k.draw_string(f"[{cux},{cuy}]",0,0)
  if 'left' in i.get_keys() or 'right' in i.get_keys() or 'down' in i.get_keys() or 'up' in i.get_keys():
    draw.cursor(cux, cuy, gv.bxc) # erase cursor
    cux = (cux + i.keydown(i.KEY_RIGHT)-i.keydown(i.KEY_LEFT)) % 3
    cuy = (cuy + i.keydown(i.KEY_DOWN) -i.keydown(i.KEY_UP))   % 3
    draw.cursor(cux, cuy, gv.cc)  # update cursor
    t.sleep(0.1)                  # add cooldown
  if i.keydown(i.KEY_MULTIPLICATION):
    draw.symbol(cux, cuy, draw.round, gv.cp1)
  if i.keydown(i.KEY_DIVISION):
    draw.symbol(cux, cuy, draw.cross, gv.cp2)
