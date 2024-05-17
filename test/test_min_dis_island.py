import unittest
from src.min_dis_island import find_min_len_cable_in_the_island


class VehicleInternetTest(unittest.TestCase):
    def test_empty_graph(self):
        find_min_len_cable_in_the_island("src/resources/islands_empty.csv", "src/resources/islands_empty.out")
        with open("src/resources/islands_empty.out", 'r') as file:
            first_line = file.readline()
        self.assertEqual(first_line, "Graph is empty")

    def test_normal_graph(self):
        find_min_len_cable_in_the_island("src/resources/islands.csv", "src/resources/islands.out")
        with open("src/resources/islands.out", 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()
        self.assertEqual(int(numbers[0]), 30)
