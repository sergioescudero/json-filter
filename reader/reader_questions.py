class Reader:

    def __init__(self, questions):
        self.questions = questions

    def get_unique_questions_with_highest_rating_and_older_ordered_by_id_asc(self):
        final_questions = list()
        for question in self.questions:
            if len(self.is_question_already_checked(question, final_questions)) == 0:
                question_with_highest_rating_and_older = \
                    self.get_question_highest_rating_and_older(question)
                if question_with_highest_rating_and_older:
                    final_questions.append(question_with_highest_rating_and_older)
        return self.__order_questions_by_id_asc(final_questions)

    def is_question_already_checked(self, question, final_questions):
        return list(filter(lambda x: x['content'] == question['content'], final_questions))

    def get_question_highest_rating_and_older(self, question):
        similar_questions = self.get_similar_questions(question)
        if len(similar_questions) == 1:
            return similar_questions[0]

        ordered_questions = self.order_questions_by_rating_and_timestamp(similar_questions)
        return ordered_questions[0]

    def order_questions_by_rating_and_timestamp(self, questions):
        return sorted(questions, key=lambda k: (
            -self.__get_highest_rating(k['answers']), k['createTimestamp']))

    def get_similar_questions(self, question):
        return list(filter(lambda x: x['content'] == question['content'],
                           self.questions))

    def __get_highest_rating(self, answers):
        answer_with_higest_rating = max(answers, key=lambda x: x['rating'])
        return answer_with_higest_rating['rating']

    def __order_questions_by_id_asc(self, questions):
        return sorted(questions, key=lambda k: (k['id']))

