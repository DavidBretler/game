#define the_master():
master=turtle.Turtle()
master.shape("corona5.gif")
master.penup()
master.speed(0)
master.setposition(0,1000)
master_lives=3
master.speed=0
def master_move():
  wn.update()
  master_speed=0.5
  while master_lives>0:

      x = master.xcor()
      x += master_speed
      master.setx(x)

      #  Move the enemy back and down
      if master.xcor() > 280:
              #Move all enemies down
              y = master.ycor()
              y -= 30
              master.sety(y)
              #Change enemy direction
              master_speed = master_speed * -1

      if master.xcor() < -280:
          #  Move all enemies down
              y = master.ycor()
              y -= 30
              master.sety(y)
              # Change enemy direction
              master_speed = master_speed * -1

      if score == num_points_finsh_stage1:  # check if finish stage 1
          enemy.setposition(0, 10000)



          # if score==num_points_finsh_stage1:
          if all([enemy.ycor() > 5000 for enemy in enemies]):
              master.setposition(enemy_start_x, enemy_start_y)
              master_move()

              if score < num_points_finsh_stage1:  # check if not finish stage 1
                  fire_enemy_bullet(enemy)



              num_points_finsh_stage1 = 10

              places[i][j] = True  # taken

              places = [[True] * 9 for i in range(3)]  # true if the place is taken
