import pytest

# https://docs.pytest.org/en/latest/how-to/capture-stdout-stderr.html
# https://docs.pytest.org/en/stable/how-to/parametrize.html

from main import print_workout_days


def test_print_workout_days_upperbody(capsys):
    print_workout_days("upper body")
    captured = capsys.readouterr()
    assert captured.out == "Mon, Thu\n"


def test_print_workout_days_lowerbody(capsys):
    print_workout_days("lower body")
    captured = capsys.readouterr()
    assert captured.out == "Tue, Fri\n"


def test_print_workout_days_wrong_question(capsys):
    print_workout_days("x body")
    captured = capsys.readouterr()
    assert captured.out == "No matching workout\n"


def test_print_workout_days_cardio(capsys):
    print_workout_days("cardio")
    captured = capsys.readouterr()
    assert captured.out == "Wed\n"


# SOLUTION PROVIDED
# import pytest
#
# from workouts import print_workout_days
#
#
# @pytest.mark.parametrize("arg, expected", [
#     ('upper', 'Mon, Thu'),
#     ('lower', 'Tue, Fri'),
#     ('30', 'Wed'),
#     ('30 min', 'Wed'),
#     ('30 min cardio', 'Wed'),
#     ('30 MIN CARDIO', 'Wed'),
#     ('upper body #1', 'Mon'),
#     ('upper body #2', 'Thu'),
#     ('lower body #1', 'Tue'),
#     ('lower body #2', 'Fri'),
#     ('Upper', 'Mon, Thu'),
#     ('UPPEr', 'Mon, Thu'),
#     ('Upper Body #', 'Mon, Thu'),
#     ('lower upper body', 'No matching workout'),
#     ('sun', 'No matching workout'),
#     ('30 min cardio -', 'No matching workout'),
#     ('nonsense', 'No matching workout'),
# ])
# def test_print_workout_days(arg, expected, capfd):
#     print_workout_days(arg)
#     actual = capfd.readouterr()[0].strip()
#     assert actual == expected