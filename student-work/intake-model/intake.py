class Intake:
    def __init__(self):
        self.has_piece = False
        self.output = 0.0


    def update(self, request, enabled, detected):
        self.has_piece = detected
        if not enabled:
            self.output = 0.0
            return
        if request > 1:
            request = 1
        elif request < -1:
            request = -1
            
        if detected and request > 0:
            self.output = 0.0
        elif detected and request < 0:
            self.output = request
        elif not detected:
            self.output = request

    def stop(self):
        self.output = 0.0
