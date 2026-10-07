from dataclasses import dataclass
import pickle


@dataclass
class Speciality:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    adress: str


@dataclass
class Group:
    speciality: Speciality
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_list, f)
    return max((len(group.students) for group in group_list), default=0)


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(student_list, f)
    return len(student_list)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        groups_data = pickle.load(f)
    return sorted({i.speciality.name for i in groups_data})


def read_students_information() -> list[Student]:
    with open("student.pickle", "rb") as f:
        students_data = pickle.load(f)
    return list(students_data)
