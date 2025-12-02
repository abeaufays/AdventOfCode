import y25.d02.part2 as solution


def test_answer():
    assert solution.answer("y25/d02/test") == 4174379265  # TO FILL


def test_split_in_even_parts():
    assert solution.split_in_even_parts("123456789", 3) == ["123", "456", "789"]
    assert solution.split_in_even_parts("1234567890", 5) == ["12345", "67890"]
    assert solution.split_in_even_parts("1234567890", 2) == [
        "12",
        "34",
        "56",
        "78",
        "90",
    ]
