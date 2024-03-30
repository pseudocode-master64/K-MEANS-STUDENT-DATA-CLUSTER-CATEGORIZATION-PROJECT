from dataclasses import dataclass
from csv import DictReader
from math import sqrt



@dataclass
class Student_Info: #attributes
    sub_id: int
    sub1: int
    sub2: int
    sub3: int


class Student(Student_Info): #methods
    "A representation of an the subjects."

    def distance(self, other: Student_Info) -> float:
        """
        Pythagorean distance using width and length
        of petals and sepals.
        """

        return sqrt(
            (self.sub1 - other.sub1) ** 2
            + (self.sub2 - other.sub2) ** 2
            +(self.sub3 - other.sub3) ** 2
        )


transform = {
    "id": int,
    "lang_z": float,
    "stem_z": float,
    "hum_z": float
}

student_data: list[Student]
with open("data/processed_data.csv") as f:
    student_data = [
        Student(*(t(row[column]) for column, t in transform.items()))
        for row in DictReader(f)
    ]
