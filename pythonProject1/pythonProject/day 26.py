import audio
print("MyPOD Music Player")
print("Press 1 to play")
print("press 2 to Exit")
print("Press anything else to see the menu again")
def play():
    source = audio.play_file('audio.wav')
    while True:
        input()

play = 0
while True:
    play = int(input())
    if play == 1:
        play()
        print("Play some proper tunes!")
    if play == 2:
        exit()
    else:
        
