# water - 3.5 litter - drank - every 45min
#
# eye - washed - every 30 min
#
# physical activity - exdone - every 46 min


from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input("CODE:")
        if a == stopper:
            mixer.music.stop()
            break
if __name__ == '__main__':
    # musiconloop("water_tune.mp3","stop")
    init_water = time()
    init_eye = time()
    init_exercise = time()
    water_sec = 30*60
    exercise_sec =45*60
    eye_sec =50*60

    while True:
        if time() - init_water > water_sec:
            print("\nWater drinking Time. Enter 'drank' to stop this alarm")
            musiconloop('water_tune.mp3', 'drank')
            init_water = time()

        if time() - init_eye > eye_sec:
            print("\nTime To Wash Your Eyes. Enter 'washed' to stop this alarm")
            musiconloop('open_your_eyes.mp3','washed')
            init_eye = time()

        if time() - init_exercise > exercise_sec:
            print("\ntime to exercise. Enter 'exdone' to stop this")
            musiconloop('time_to_exercise.mp3', 'exdone')
            init_exercise = time()
