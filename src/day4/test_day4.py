import os
from unittest import TestCase
from day4.day4 import parse_passport, read_input, parse_rows

_MOCK_INPUT_FILEPATH = os.path.join(os.path.dirname(__file__), "mock_input.txt")


class TestDay4(TestCase):
    def test_should_parse_passports(self):
        # Arrange
        test_input = read_input(_MOCK_INPUT_FILEPATH)

        # Act
        result = parse_rows(test_input)

        # Assert
        self.assertEqual(len(result), 3)

    def test_should_parse_passport(self):
        # Arrange
        test_input = read_input(_MOCK_INPUT_FILEPATH)
        raw_passports = parse_rows(test_input)

        # Act
        result = parse_passport(raw_passports[0])

        # Assert
        self.assertEqual(result._iyr, "2013")
        self.assertEqual(result._hcl, "#ceb3a1")
        self.assertEqual(result._hgt, "151cm")
        self.assertEqual(result._eyr, "2030")
        self.assertEqual(result._byr, "1943")
        self.assertEqual(result._ecl, "grn")

    def test_should_parse_other_passport(self):
        # Arrange
        test_input = read_input(_MOCK_INPUT_FILEPATH)
        raw_passports = parse_rows(test_input)

        # Act
        result = parse_passport(raw_passports[2])

        # Assert
        self.assertEqual(result._hcl, "#733820")
        self.assertEqual(result._iyr, "2014")
        self.assertEqual(result._hgt, "166cm")
        self.assertEqual(result._eyr, "2025")
        self.assertEqual(result._byr, "1952")
        self.assertEqual(result._ecl, "blu")
        self.assertEqual(result._pid, "79215921")

    def test_should_validate_passport(self):
        # Arrange
        test_input = read_input(_MOCK_INPUT_FILEPATH)
        raw_passports = parse_rows(test_input)

        # Act
        invalid_pp = parse_passport(raw_passports[0])
        valid_pp = parse_passport(raw_passports[1])
        valid_pp2 = parse_passport(raw_passports[2])

        # Assert
        self.assertFalse(invalid_pp.has_valid_props())
        self.assertTrue(valid_pp.has_valid_props())
        self.assertTrue(valid_pp2.has_valid_props())
