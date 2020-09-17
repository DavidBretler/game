import math
import turtle
import platform
import winsound
# add sound
import random

#  Set up the screen
bulletstate = "ready"
enemy_bullet_state = "ready"

import playsound #as playsound

def clickLeft2(x,y):
    run()
def rungame():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Space Invaders virus attack !!!")
    wn.bgpic("Gbg2.gif")
    wn.setup(900,900,300,-10)
    # Register the shapes
    wn.register_shape("invader.gif")
    wn.register_shape("player2.gif")
    wn.register_shape("corona4.gif")
    wn.register_shape("corona5.gif")
    wn.register_shape("vaxinBullet5.gif")
    wn.register_shape("drop.gif")
    wn.tracer(0)
    #  Draw border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300, -300)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()

    # Set the score to 0
    score = 0

    # Draw the score
    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.setposition(-290, 280)
    scorestring = str(score)
    score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    score_pen.hideturtle()

    lives = 3 # num of lives
    # drew the lives
    lives_pen = turtle.Turtle()
    lives_pen.speed(0)
    lives_pen.color("white")
    lives_pen.penup()
    lives_pen.setposition(280, 280)
    lives_pen.write(str(lives), False, align="left", font=("Arial", 14, "normal"))
    lives_pen.hideturtle()

    #  Create the player turtle
    player = turtle.Turtle()
    player.color("blue")
    player.shape("player2.gif")
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)
    player.speed = 0
    state="neutral"
    # Create the enemy
    # Choose a number of enemies
    number_of_enemies = 27
    # Create an empty list of enemies
    enemies = []
    enemysSpeed=[]

    # Add enemies speed to the list
    #for i in range(number_of_enemies):
    #    enemysSpeed.append(20)

    # Add enemies to the list
    for i in range(number_of_enemies):
        enemies.append(turtle.Turtle())
    enemy_start_x=-250
    enemy_start_y= 250
    enemy_number=0

    for enemy in enemies:
            enemy.color("red")
            enemy.shape("corona4.gif")
            enemy.penup()
            enemy.speed(0)
            x = enemy_start_x +(60 * enemy_number)
            y = enemy_start_y
            enemy.setposition(x,y)
            enemy_number = enemy_number + 1
            #  make enemy in line
            if enemy_number == 9:
                enemy_start_y -=60
                enemy_number= 0

    enemy_speed=0.3

    # Create the enemy's bullet
    enemy_bullet=turtle.Turtle()
    enemy_bullet.penup()
    enemy_bullet.setposition(-500,-500)
    enemy_bullet.color("green")
    enemy_bullet.shape("drop.gif")
    enemy_bullet.speed(0)
    enemy_bullet.hideturtle()
    enemy_bullet_speed=0.1

    # Create the player's bullet
    bullet = turtle.Turtle()
    bullet.penup()
    bullet.setposition(-500,-500)
    bullet.color("yellow")
    bullet.shape("vaxinBullet5.gif")
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()
    bulletspeed = 7

    # Define bullet state
    # ready - ready to fire
    # fire - bullet is firing


    #  Move the player left and right

    def ML():
        player.speed=-2

    def MR():
        player.speed=2

    def MP():
        x=player.xcor()+player.speed
        if x > 280:
            x = 280
        if x < -280:
            x = - 280
        player.setx(x)

    def h4():
        wn.bye()

    def fire_bullet():
    # Declare bulletstate as a global if it needs changed
        global bulletstate
        if bulletstate == "ready":
           # play_sound("laser.wav")
            bulletstate = "fire"
            # Move t he bullet to the just above the player
            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x, y)
            bullet.showturtle()

    def fire_enemy_bullet(enemy):
    # Declare bulletstate as a global if it needs changed
        global enemy_bullet_state
        if enemy_bullet_state == "ready":
            play_sound("sneeze.wav")
            enemy_bullet_state = "fire"
            # Move t he bullet to the just down the enemy
            x = enemy.xcor()
            y = enemy.ycor() - 10
            enemy_bullet.setposition(x, y)
            enemy_bullet.showturtle()

    def isCollision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance < 20:
            return True
        else:
            return False
    def random_place(enemy):
        global enemy_start_x
        global enemy_start_y
        enemy_start_x = -250
        enemy_start_y = 250
        i = random.randint(0, 2)
        j = random.randint(0, 8)
        y=enemy_start_y-(60*i)
        x=enemy_start_x+(50*j)
        enemy.setposition(x,y)

    def play_sound(sound_file,time=0):
        winsound.PlaySound(sound_file,winsound.SND_ASYNC)
        if time > 0:
            wn.ontimer(lambda:play_sound(sound_file,time),t=int(time*1000))

    wn.onkeypress(ML, "Left")
    wn.onkeypress(MR, "Right")
    wn.onkeypress(fire_bullet, "space")
    wn.onkeypress(h4, "q")
    wn.listen()
    # background music
    playsound.playsound('bgm.wav', False)

    num_points_to_win=1000

    #  Main game loop ###########################################################################################
    while True:
        wn.update()
        global bulletstate
        global enemy_bullet_state
        MP()
        if score == num_points_to_win:
            print ("you won !! ")
            print( "your score is "+str(score))
            state = "win"
            break

        for enemy in enemies:
                    # if enemy_bullet_state=="ready":
                    fire_enemy_bullet(enemy)
                    #  Move the enemy
                    x = enemy.xcor()
                    x += enemy_speed
                    enemy.setx(x)
                    #  Move the enemy back and down
                    if enemy.xcor() > 280:
                        #  Move all enemies down
                        for e in enemies:
                            y = e.ycor()
                            y -= 30
                            e.sety(y)
                        #  Change enemy direction
                        enemy_speed =enemy_speed* -1

                    if enemy.xcor() < -280:
                        #  Move all enemies down
                        for e in enemies:
                            y = e.ycor()
                            y -= 30
                            e.sety(y)
                        #  Change enemy direction
                        enemy_speed =enemy_speed* -1
                    if(enemy.ycor()<-300):
                        x = random.randint(-200, 200)
                        y = random.randint(100, 250)
                        enemy.setposition(x, y)

                    if isCollision(bullet, enemy):
                        #  Reset the bullet
                        playsound.playsound('scream6.wav', False)
                        bullet.hideturtle()
                        bulletstate = "ready"
                        bullet.setposition(0, -400)
                        #  "kill" the enemy enemy.setposition(0,10000)
                        #  Reset the enemy in new random position
                        random_place(enemy)
                        #  Update the score
                        score += 10
                        scorestring = str(score)
                        score_pen.clear()
                        score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
                       # enemy_bullet.hideturtle()
                        #enemy_bullet_state = "ready"
                    # if enemy hit lost all lifes
                    if isCollision(player, enemy) or lives<=0 :
                        player.hideturtle()
                        enemy.hideturtle()
                        print("Game Over")
                        print("your score is " + str(score))
                        state="lost"
                        break
                   # if drop hit lost one life
                    if isCollision(player, enemy_bullet):
                        playsound.playsound("explosion.wav",False)
                       # play_sound("explosion.wav")

                        enemy_bullet.hideturtle()
                        enemy_bullet_state = "ready"
                        lives -= 1
                        lives_pen.clear()
                        lives_pen.write(str(lives), False, align="left", font=("Arial", 14, "normal"))
                    #  Move the enemy bullet
                    if enemy_bullet_state == "fire":
                        y = enemy_bullet.ycor()
                        y -= enemy_bullet_speed
                        enemy_bullet.sety(y)

                        #  Check to see if the enemy bullet has gone to the bottom
                    if enemy_bullet.ycor() < -300:
                        enemy_bullet.hideturtle()
                        enemy_bullet_state = "ready"

        # play losing sound
        if state == "lost":
             play_sound("lose.wav")
             key = input("press enter to continue")
             exit()

            #  Move the bullet
        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

            #  Check to see if the  bullet has gone to the top
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"



    # play wining sound
    if state =="win" :
           playsound.playsound("win.wav", False)
           key= input("press enter to continue")
           exit()

# create start screen
wn1 = turtle.Screen()

def clickLeft(x,y):
    rungame()
def clickRight(x,y):
    rungame()
def run():
    wn1.listen()
    #wn1.register_shape("start.gif")
    wn1.title("Space Invaders virus attack ")
    wn1.bgpic("start.gif")
    wn1.onscreenclick(clickLeft,1)
    wn1.onscreenclick(clickRight,3)

    wn1.mainloop()
if __name__ =="__main__":
    run()