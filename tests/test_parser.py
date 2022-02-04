import unittest

from parser.parser import FileParser


class TestParser(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_read_json_from_file(self):
        a_parser = FileParser()
        data = a_parser.read_json_from_file("resources/input.json")
        self.assertEqual(len(data) > 1, True)


if __name__ == '__main__':
    unittest.main()
