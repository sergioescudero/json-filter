from typing import List, Dict


class Reader:

    def _order_by_id(self, items: List, reverse: bool = False) -> List:
        return sorted(items, key=lambda k: (k['id']), reverse=reverse)


class QuestionReader(Reader):

    def __init__(self, questions: List):
        self.questions = questions

    def get_unique_questions_with_highest_rating_and_older_ordered_by_id(self, asc=True):
        final_questions = list()
        for question in self.questions:
            if self.is_question_already_checked(question, final_questions):
                question_with_highest_rating_and_older = \
                    self.get_question_highest_rating_and_older(question)
                if question_with_highest_rating_and_older:
                    final_questions.append(question_with_highest_rating_and_older)

        return self.__order_questions_by_id_asc(final_questions)

    def is_question_already_checked(self, question: Dict, final_questions: List) -> bool:
        return len(list(
            filter(lambda x: x['content'] == question['content'], final_questions))) == 0

    def get_question_highest_rating_and_older(self, question: Dict) -> Dict:
        similar_questions = self.get_similar_questions(question)
        if len(similar_questions) == 1:
            return similar_questions[0]

        ordered_questions = self.order_questions_by_rating_and_timestamp(similar_questions)
        return ordered_questions[0]

    def order_questions_by_rating_and_timestamp(self, questions: List) -> List:
        return sorted(questions, key=lambda k: (
            -self.__get_highest_rating(k['answers']), k['createTimestamp']))

    def get_similar_questions(self, question: Dict) -> List:
        return list(filter(lambda x: x['content'] == question['content'],
                           self.questions))

    @staticmethod
    def __get_highest_rating(answers: List) -> int:
        answer_with_higest_rating = max(answers, key=lambda x: x['rating'])
        return answer_with_higest_rating['rating']

    def __order_questions_by_id_asc(self, questions: List) -> List:
        return sorted(questions, key=lambda k: (k['id']))
