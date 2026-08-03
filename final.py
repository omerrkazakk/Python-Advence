# #SECTİON 6:FİNAL
#

print("-"*60)
print("Section 7: Final")
print("-"*60)

from typing import final

class BaseGame:
    def start(self):
        return "start the game"
    @final
    def calculate_points(self,points:int)->int:
        bonus=100
        return points+bonus
    def end(self):
        return "end the game"
class MyGame(BaseGame):
    def start(self):
        return "start the my game"
    def calculate_points(self,points:int)->int:
        return points*2
@final
class GameCheat():
    def cheat(self):
        return "found game cheat"
game = MyGame()
print(game.start())
print(game.calculate_points(5))

game_exploit = GameCheat()
print(game_exploit.cheat())