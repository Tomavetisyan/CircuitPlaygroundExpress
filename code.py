from adafruit_circuitplayground.express import cpx
import time
import random
#play_file()
#play_tone()
#pixels[i] = ((r,g,b))
#pixels.fill((r,g,b))
#switch
#button_a
#button_b
#touch_A1
#temperature
#light

color_list = [(255, 0, 0),(255, 50, 0),(255, 165, 0),(255, 180, 0),(255, 200, 0),(0, 128, 0),(0, 128, 255),(0, 0, 255),(75, 0, 130),(238, 130, 238)]
game_dic = {1: [5,6], 2: [7,8,9], 3: [0,1,2], 4: [3,4]}
color_dic = {5: (255,0,0), 6: (255,0,0), 7: (0,255,0), 8:(0,255,0), 9:(0,255,0), 0:(255,165,0), 1:(255,165,0), 2:(255,165,0), 3:(0,0,255), 4:(0,0,255) }
sound_dic = {1: 200, 2: 300, 3: 400, 4: 500}


def playPattern(pattern):
    for a in pattern:
      for num in game_dic[a]:
          cpx.pixels[num] = color_dic[num]
      cpx.play_tone(sound_dic[a], 0.3)
      cpx.pixels.fill((0,0,0))

def playerLose():
    cpx.pixels.fill((255,0,0))
    cpx.play_tone(200, 0.1)
    cpx.play_tone(200, 0.5)

def check(game, player):
    if game[len(player)-1] == player[-1]:
      return True
    else:
      return False

while True:
  if cpx.switch:
    if cpx.button_a:
        score = 0
        playing = True
        game = []
        for i in range(10):
            cpx.pixels[i] = color_list[i]
            cpx.play_tone(i*75, 0.05)
        cpx.pixels.fill((0,0,0))
        while playing:
            time.sleep(0.5)
            game.append(random.randint(1,4))
            playPattern(game)
            print(game)
            player = []
            while len(player) < len(game):
              if cpx.touch_A1:
                player.append(1)
                playPattern([1])
                if not check(game, player):
                  playerLose();
                  playing = False
                  break
              elif cpx.touch_A2 or cpx.touch_A3:
                player.append(2)
                playPattern([2])
                if not check(game, player):
                  playerLose();
                  playing = False
                  break
              elif cpx.touch_A4 or cpx.touch_A5:
                player.append(3)
                playPattern([3])
                if not check(game, player):
                  playerLose();
                  playing = False
                  break
              elif cpx.touch_A6 or cpx.touch_A7:
                player.append(4)
                playPattern([4])
                if not check(game, player):
                  playerLose();
                  playing = False
                  break
              elif not cpx.switch:
                playing = False
                cpx.pixels.fill((0,255,0))
                cpx.play_tone(600, 0.1)
                cpx.pixels.fill((255,0,0))
                cpx.play_tone(300, 0.1)

            cpx.pixels.fill((0,0,0))
            score += 1
        print("Your score is " + str(score-1))

  cpx.pixels.fill((0,0,0))
