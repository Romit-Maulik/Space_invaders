import turtle
import os
import random


# Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw a border in the window
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-250,-250)#Pixels from center (0,0)
border_pen.pensize(3)
border_pen.pendown()

#Draw a square
for side in range(4):
    border_pen.fd(500)#Move
    border_pen.lt(90)#Left turn

border_pen.hideturtle()


#Create the enemies
num_enemies = 5
enemies = []
enemyxspeed = 2
enemyyspeed = 20
# Add enemies to list
for i in range(num_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.shape("circle")
    enemy.speed(0)
    enemy.color("Red")
    enemy.penup()
    enemy.setposition(random.randint(-200,200),random.randint(150,200))
    enemy.showturtle()


#Create the player turtle
player = turtle.Turtle()
player.hideturtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-200)
player.setheading(90)
player.showturtle()

# Working on moving the player turtle
playerspeed = 15 #Adjust for sensitivity

# Moving left
def move_left():
    x = player.xcor()
    x = x-playerspeed

    #Bound left location
    if x < -240:
        x = -240

    player.setx(x)

# Moving left
def move_right():
    x = player.xcor()
    x = x+playerspeed

    # Bound left location
    if x > 240:
        x = 240

    player.setx(x)

# Create the players bullet
bullet = turtle.Turtle()
bullet.hideturtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bulletspeed=20
collision_distance = 15

# Bullet has two states - ready (to fire) and moving
bullet_state = "ready"

#Bullet firing function
def fire_bullet():
    global bullet_state # So that the state changes

    if bullet_state == "ready":
        #Bullet position initialized above player
        x = player.xcor()
        y = player.ycor()
        y = y + 20
        bullet.setposition(x,y)
        bullet.showturtle()

def check_collision(bullet,enemy):

    global collision_distance


    xb = bullet.xcor()
    yb = bullet.ycor()

    xe = enemy.xcor()
    ye = enemy.ycor()

    dist = (xb-xe)**2 + (yb-ye)**2

    if dist<collision_distance**2:
        return True
    else:
        return False

#Keyword binding
wn.listen()
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')
wn.onkey(fire_bullet,"space")

while True:
    # Move enemies
    for enemy in enemies:
        if enemy.isvisible():
            x = enemy.xcor()
            x = x + enemyxspeed
            y = enemy.ycor()

            if x > 240:
                x = 240
                enemyxspeed = enemyxspeed*(-1)
                y = y - enemyyspeed
                enemy.sety(y)

            elif x<-240:
                x = -240
                enemyxspeed = enemyxspeed*(-1)
                y = y - enemyyspeed
                enemy.sety(y)

            enemy.setx(x)

    #Fired bullet
    y = bullet.ycor()
    y = y + bulletspeed
    bullet.sety(y)

    global bullet_state
    if y > 250:
        bullet_state = "ready"
        # bullet.hideturtle()
    else:
        bullet_state = "firing"

    for enemy in enemies:
        if enemy.isvisible():
            # Check for collision
            if (check_collision(bullet,enemy)):
                #Reset bullet
                bullet_state = "ready"
                bullet.hideturtle()
                bullet.setposition(0,-400)
                #Reset enemy
                # enemy.setposition(0,200)
                enemy.hideturtle()

            if (check_collision(player,enemy)):
                player.hideturtle()
                enemy.hideturtle()

                print("Game over!")
                break

    val = 0

    for enemy in enemies:
        if enemy.isvisible():
            val = val + 1

    if val == 0:
        print("Game over! You won!")
        break



delay = input('Press enter to finish!')

