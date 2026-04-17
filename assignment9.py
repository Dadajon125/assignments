from dataclasses import dataclass, field

@dataclass
class Member:
    name:str
    member_id:str
    sessions_attented:int = 0
    calories_burned:list[int] = field(default_factory=list)

    def log_session(self, calories: int):
        self.sessions_attented += 1
        self.calories_burned.append(calories)

    def avg_calories(self) -> float:
        if not self.calories_burned:
            return 0.0
        total = 0
        for calories in self.calories_burned:
            total += calories
        average = total / len(self.calories_burned)
        return average
    
@dataclass
class FitnessClass:
    class_name: str
    instructor: str
    capacity: int
    members: list[Member] = field(default_factory=list)# [Javohir, Dadajon]
    enrolled: int = field(init=False)
    
    def __post_init__(self):
        self.enrolled =  len(self.members)

    def enroll(self, member: Member) -> bool:
        if self.enrolled + 1 > self.capacity:
            return False
        self.members.append(member)
        self.enrolled += 1
        return True 
    def best_performer(self) -> str:
        if self.members == []:
            return "No data"
        sorted_members = sorted(
            self.members,
            key=lambda x: x.avg_calories(),
            reverse=True
        )
        return sorted_members[0].name

    def class_stats(self) -> str:
        print(f"{self.class_name} ({self.instructor}):")
        for member in self.members:
            print(f"  {member.name} - {member.sessions_attented} sessions, avg {member.avg_calories():.1f} cal")
        print(f"Enrolled: {self.enrolled}/{self.capacity}")

m1 = Member("Alice", "M001")
m2 = Member("Bob", "M002")
m3 = Member("Charlie", "M003")

m1.log_session(350)
m1.log_session(420)
m1.log_session(380)
m2.log_session(500)
m2.log_session(450)
m3.log_session(300)

fc = FitnessClass("HIIT", "Coach Dana", 3)
print(fc.enroll(m1))
print(fc.enroll(m2))
print(fc.enroll(m3))
print(fc.enroll(Member("Dave", "M004")))
print(fc.enrolled)
print(fc.best_performer())
print(fc.class_stats())
