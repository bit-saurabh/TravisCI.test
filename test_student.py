from student import calculate_average, get_grade


def test_average():
    marks = [90, 80, 70]
    assert calculate_average(marks) == 80


def test_grade_a_plus():
    assert get_grade(95) == "A+"


def test_grade_a():
    assert get_grade(85) == "A"


def test_grade_b():
    assert get_grade(75) == "B"


def test_grade_f():
    assert get_grade(40) == "F"