import unittest

from parser.parser import FileParser
from reader.reader_questions import Reader
from tests.test_values_helper import TestValues


class ReaderQuestionsTest(unittest.TestCase):

    def setUp(self):
        self.questions = TestValues.questions
        self.questions_ordered = TestValues.questions_ordered

        self.unique_question = {
            "id": 98673,
            "createTimestamp": 1555067471,
            "content": "No more!",
            "answers": [
              {
                "id": 15,
                "rating": 4,
                "content": "Answer content 15"
              },
              {
                "id": 16,
                "rating": 4,
                "content": "Answer content 16"
              }
            ]
          }

        self.non_unique_question = {
            "id": 34672,
            "createTimestamp": 1557655871,
            "content": "Don't hurt me.",
            "answers": [
              {
                "id": 7,
                "rating": 4,
                "content": "Answer content 7"
              },
              {
                "id": 8,
                "rating": 4,
                "content": "Answer content 8"
              }
            ]
        }

        self.a_non_existing_question = {
          "id": 98673,
          "createTimestamp": 1555067471,
          "content": "I dont like it",
          "answers": [
            {
              "id": 15,
              "rating": 4,
              "content": "Answer content 15"
            },
            {
              "id": 16,
              "rating": 4,
              "content": "Answer content 16"
            }
          ]
        }

        self.highest_rating_and_oldest_question = {
            'id': 34673,
            'createTimestamp': 1557655871,
            'content': "Don't hurt me.",
            'answers': [{'id': 7, 'rating': 4, 'content': 'Answer content 7'},
                        {'id': 8, 'rating': 14, 'content': 'Answer content 8'}]
        }

    def test_existing_question_exists_in_questions_list(self):
        reader = Reader(self.questions)
        x = reader.is_question_already_checked(self.unique_question, self.questions)
        self.assertTrue(len(x) > 0, "It does not exists")

    def test_non_existing_question_not_exists_in_questions_list(self):
        reader = Reader(self.questions)
        x = reader.is_question_already_checked(self.a_non_existing_question, self.questions)
        self.assertTrue(len(x) == 0, "It exists")

    def test_get_similar_questions_with_unique_question(self):
        reader = Reader(self.questions)
        x = reader.get_similar_questions(self.unique_question)
        self.assertEqual(len(x) == 1, True, "It is not unique")

    def test_get_similar_questions_with_question_existing_more_than_once(self):
        reader = Reader(self.questions)
        x = reader.get_similar_questions(self.non_unique_question)
        self.assertEqual(len(x) == 3, True, "It does not exists")

    def test_get_similar_questions_not_similar(self):
        reader = Reader(self.questions)
        x = reader.get_similar_questions(self.a_non_existing_question)
        self.assertEqual(len(x) == 0, True, "It exists")

    def test_order_questions_by_rating_and_timestamp(self):
        reader = Reader(self.questions)
        x = reader.order_questions_by_rating_and_timestamp(self.questions)
        self.assertEqual(self.questions_ordered == x, True)

    def test_get_highest_rating_and_older(self):
        reader = Reader(self.questions)
        x = reader.get_question_highest_rating_and_older(self.non_unique_question)
        self.assertEqual(self.highest_rating_and_oldest_question == x, True)

    def test_get_unique_questions_with_highest_rating_and_older(self):
        a_parser = FileParser()
        input = a_parser.read_json_from_file("resources/input.json")
        expected_result = a_parser.read_json_from_file("resources/output.json")
        reader = Reader(input)
        result = reader.get_unique_questions_with_highest_rating_and_older_ordered_by_id_asc()
        self.assertEqual(result == expected_result, True)


if __name__ == '__main__':
    unittest.main()
