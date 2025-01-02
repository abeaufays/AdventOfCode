import y24.d17.part2 as part2


def test_octal_digits_list_to_int():
    assert part2.octal_digits_list_to_int([7, 5, 3], 5) == 0o75300
    assert part2.octal_digits_list_to_int([2, 3, 7], 6) == 0o237000


def test_run_part1():
    assert part2.answer_part1("y24/d17/data") == "1,3,5,1,7,2,5,1,6"
