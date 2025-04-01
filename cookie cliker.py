import turtle

width = 1280
height = 720
game = turtle.Screen()
game.setup(width=width, height=height, startx=100, starty=100)
game.screensize(width, height)
game.tracer(0)

backgrounds = ["background1.gif", "background2.gif"]
b_cookies = ["cookies1.gif", "cookies2.gif", "cookies3.gif", "cookies4.gif", "cookies5.gif"]

# background
background = turtle.Turtle()
b_cookie = turtle.Turtle()
for i in backgrounds:
    game.addshape(i)
for i in b_cookies:
    game.addshape(i)
background.shape("background1.gif")

# setup counter
number = 0
font_name = "Arial"  # Font name
font_size = 24       # Font size
font_type = "normal"  # Font type: "normal", "bold", or "italic"
counter = turtle.Turtle()
counter.hideturtle()
counter.up()
counter.goto(0 - 0.5 * len(str(number)) * font_size * 0.6, 200)
counter.write(number, font = (font_name, font_size, font_type))

# setup cookie generation
g_counter = turtle.Turtle()
g_counter.hideturtle()
g_counter.up()
generation = 0
g_counter.goto(0 - 0.5 * len("Currently baking " + str(generation) + " cookies per second") * font_size * 0.6, 150)
g_counter.write("Currently baking " + str(generation) + " cookies per second", font = (font_name, font_size, font_type))

# buy menu setup
menu = turtle.Turtle()
m_length = width/2
m_height = height/3
m_font_size = 12
menu.hideturtle()
menu.up()
menu.goto(0 - m_length / 2, -250 - m_height / 2)
menu.down()
b1_opts_x = 20 - m_length / 2
b1_opts_y = -200
b2_opts_x = 20 - m_length / 2
b2_opts_y = -300

def drawMenu():
    menu.clear()
    menu.fillcolor("green")
    menu.begin_fill()
    buy_options = ["Clicker: 20", "Grandma: 100", "Student: 1000", "Baker",
                "Robots", "Factory", "Power Plant", "MOAG"]
    menu.up()
    menu.goto(0 - m_length / 2, -250 - m_height / 2)
    menu.down()
    for i in range(2):
        menu.forward(m_length)
        menu.left(90)
        menu.forward(m_height)
        menu.left(90)
    menu.end_fill()
    menu.up()
    menu.goto(b1_opts_x, b1_opts_y)
    menu.pencolor("black")
    for i in range(4):
        menu.write(buy_options[i], font=(font_name, m_font_size, "italic"))
        menu.forward(m_length/4)
    menu.goto(b2_opts_x, b2_opts_y) 
    for i in range(4, 8):
        menu.write(buy_options[i], font=(font_name, m_font_size, "italic"))
        menu.forward(m_length/4)

drawMenu()
# PURCHASED TEXT

purchase = turtle.Turtle()
purchase.hideturtle()
purchase.up()
p_width = len("Not Enough.") * .6 * font_size
purchase.goto(0 - p_width / 2, 0 - m_height + 120)   
purchase.down()
purchase.pencolor("gray")



# cookie picture
cookie = turtle.Turtle()
game.addshape("cookiesmall.gif")
cookie.shape("cookiesmall.gif")

def tryBuy(needed, gen_boost):
    global number, generation
    text = "Not Enough."
    purchase.clear()
    if number >= needed:
        number -= needed
        generation += gen_boost
        
        text = "Purchased. -" + str(needed)
        p_width = len(text) * .6 * font_size
        purchase.up()
        purchase.goto(0 - p_width / 2, 0 - m_height + 120)
        purchase.down()
        purchase.write(text, font = (font_name, font_size, font_type))
        game.ontimer(clearDrawing, 2000)
        
    else:
        p_width = len(text) * .6 * font_size
        purchase.up()
        purchase.goto(0 - p_width / 2, 0 - m_height + 120)
        purchase.down()
        purchase.write(text, font = (font_name, font_size, font_type))

    game.ontimer(clearDrawing, 2000)


def clearDrawing():
    purchase.clear()

def redraw():
    # draw background
    if number >= 100000:
        background.shape("background2.gif")
        b_cookie.shape("cookies5.gif")
        drawMenu()
    elif number >= 50000:
        background.shape("background2.gif")
        b_cookie.shape("cookies4.gif")
        drawMenu()
    elif number >= 10000:
        background.shape("background2.gif")
        b_cookie.shape("cookies3.gif")
        drawMenu()
    elif number >= 1000:
        background.shape("background2.gif")
        b_cookie.shape("cookies2.gif")
        drawMenu()
    elif number >= 100:
        background.shape("background1.gif")
        b_cookie.shape("cookies1.gif")
        drawMenu()
    
    
    

    # drawing counters
    counter_x = 0 - 0.5 * len(str(int(number))) * font_size * 0.6
    g_counter_x = 0 - 0.5 * len("Currently baking " + str(round(generation, 1)) + " cookies per second") * font_size * 0.6

    counter.clear()
    g_counter.clear()

    counter.up()
    g_counter.up()

    counter.goto(counter_x, 200)
    g_counter.goto(g_counter_x, 150)
    
    counter.down()
    g_counter.down()

    counter.write(int(number), font = (font_name, font_size, font_type))
    g_counter.write("Currently baking " + str(round(generation, 1)) + " cookies per second", font = (font_name, font_size, font_type))




def click(x, y): 
    global number, generation
    global b1_opts_x, b1_opts_y, b2_opts_x, b2_opts_y, m_length
    if x < 50 and x > -50 and y < 50 and y > -50:
        number += 1
    elif x > b1_opts_x and x < b1_opts_x + (len("Clicker: 20") * .6 * 12) and y > b1_opts_y and y < b1_opts_y + 20:
        tryBuy(20, .2)
    elif x > b1_opts_x + m_length / 4 and x < b1_opts_x + m_length/4 + (len("Grandma: 100") * .6 * 12) and y > b1_opts_y and y < b1_opts_y + 20:
        tryBuy(100, 1)
    elif x > b1_opts_x + 2 * m_length / 4 and x < b1_opts_x + 2 * m_length / 4 + (len("Student: 1000") * .6 * 12) and y > b1_opts_y and y < b1_opts_y + 20:
        tryBuy(1000, 10)

    redraw()
    game.update()

def main():
    global generation
    global number
    
    # set the cookies per second
    number += generation # add to the number
    
    redraw()
    game.update()
    game.ontimer(main, 1000)
    

    

main()
