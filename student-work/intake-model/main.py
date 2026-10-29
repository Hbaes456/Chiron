from intake import Intake

# Add a Robot class, a sequence of inputs, and assertions as described in the lesson.
class Robot:
    def __init__(self):
        self.intake = Intake()
testBot = Robot()
testBot.update(1.0, True, False)
assert testBot.intake.output == 1.0
testBot.update(66.0, True, False)
assert testBot.intake.output == 1.0
testBot.update(-66.0, True, False)
assert testBot.intake.output == -1.0