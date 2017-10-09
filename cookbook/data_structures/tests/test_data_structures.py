from .. import sequence_to_variables
from .. import arbitrary_length_sequence



def test_sequence_date():
    assert sequence_to_variables.year == 2012
    assert sequence_to_variables.day == 21
    assert sequence_to_variables.mon == 12


def test_arbitrary_length():
    grades = [1, 2, 3, 4, 5, 6, 7]
    middle = arbitrary_length_sequence.drop_first_last(grades)
    assert middle == 4.0

    assert arbitrary_length_sequence.phone_numbers == ["773-552-1212", "847-555-1212"]
    

