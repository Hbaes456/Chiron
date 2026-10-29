# Methods and changing state
# Add your clamp function to the intake behavior and store output history in a list on each instance. Append once per update. Create two intakes and prove their histories are separate.
# Write your attempt below. See the course page for expected results.
class Intake:
    def __init__(self):
        self.has_piece = False
        self.output = 0.0
        self.output_history = []
    def clamp_request(self, request):
            if request > 1.0:
                return 1.0
            if request < -1.0:
                return -1.0
            return request
    def update(self, request, enabled, detected):
        request = self.clamp_request(request)
        self.has_piece = detected
        if not enabled or (detected and request > 0):
            self.output = 0.0
        else:
            self.output = request
        self.output_history.append(self.output)
    
    def stop(self):
        self.output = 0.0
        self.output_history.append(self.output)

left_intake = Intake()
left = left_intake
right_intake = Intake()
left_intake.update(0.5, True, False)
left_intake.update(0.9, True, False)
left_intake.update(0.5, True, True)
left_intake.update(-0.5, True, True)
right_intake.update(0.5, True, True)
left.stop()
print("Left intake history:", left_intake.output_history)
print("Right intake history:", right_intake.output_history)