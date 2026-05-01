from dataclasses import dataclass, field


class WorkoutError(Exception):
    pass 

@dataclass
class Exercise():
    code: str
    name: str
    duration: int
    calories: int
    _label = str, field(default="PENDING",init=False )
    
    def __post_init__(self):
        if self.duration <= 0:
            raise WorkoutError(f"Invalid duration for {self.code}")
    
    @property
    def intensity(self):
        return round(self.calories / self.duration, 1)
    def __str__(self):
        return  f"[{self.code}] {self.name} {self.duration}min {self.calories}cal ({self._label})"
    def __lt__(self, other):
        return self.calories < other.calories
    
class CalorieChecker():
    def __init__(self, exercises, max_cal):
        self.exercises = exercises
        self.max_cal = max_cal
        self.pointer = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.pointer >= len(self.exercises):
            raise StopIteration
        exercise = self.exercises[self.pointer]
        self.pointer += 1

        if exercise.calories <= self.max_cal:
            exercise._label = "APPROVED"
        else:
            exercise._label = "EXCESSIVE"
        
        return exercise
    
def workout_report(checker):
    approved = 0
    excessive = 0

    for exercise in checker:
        if exercise._label == "APPROVED":
            approved += 1
        else:
            excessive += 1
        yield str(exercise)
    yield f"Summary: {approved}approved, {excessive} excessive"

class GymSession():
    def __init__(self, name):
        self.name = name
        self._exercises = []
    def __enter__(self):
        print(f"=== Start: {self.name} ===")
        return self
    def add(self, exercise):
        self._exercises.append(exercise)
    def evaluate(self, max_cal):
        evaluater = CalorieChecker(self._exercises, max_cal)
        return workout_report(evaluater)
    def __exit__(self, exc_type, exc, tb):
        if exc_type is WorkoutError:
            print(f"!!! Error: {exc}")
            print(f"=== End: {self.name} ({len(self._exercises)} exercises) ===")
            return True
        
        print(f"=== End: {self.name} ({len(self._exercises)} exercises) ===")
        return False
    
with GymSession("Cardio Plan") as gym:
    gym.add(Exercise("E01", "Running", 30, 250))
    gym.add(Exercise("E02", "Cycling", 45, 400))
    gym.add(Exercise("E03", "Swimming", 60, 650))

    for line in gym.evaluate(500):
        print(line)

    print(gym._exercises[0] < gym._exercises[1])

print()

with GymSession("Strength Plan") as gym:
    gym.add(Exercise("E04", "Deadlift", -10, 300))