# Classes and objects
# Create a `Launcher` class with `target_speed` and `measured_speed`, both initially zero. Make two instances, change one target, and demonstrate that the other is unaffected.
# Write your attempt below. See the course page for expected results.
class Launcher:
    def __init__(self):
        self.target_speed = 0
        self.measured_speed = 0
    
turret = Launcher()
fixed_shooter = Launcher()
turret.target_speed = 35
print("Turret target speed:", turret.target_speed)
print("Fixed shooter target speed:", fixed_shooter.target_speed)

