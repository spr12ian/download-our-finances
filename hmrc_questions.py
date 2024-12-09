from useful_functions import to_valid_method_name
from sqlite_helper import SQLiteTable


class HMRC_Questions(SQLiteTable):
    def __init__(self, question=None):
        super().__init__("hmrc_questions")
        self.question = question

    def get_method_names(self):
        method_names = {}
        for row in self.fetch_all():
            question = row[0]
            print(question)
            method_name = "get_" + to_valid_method_name(question)
            print(method_name)
            method_names[question] = method_name

        return method_names


# class Trial:
#     def call_method(self, method_name):
#         method = getattr(self, method_name)

#     def get_your_date_of_birth():
#         print("Started get_your_date_of_birth")


# print(HMRC_Questions().get_method_names())

# method_names = HMRC_Questions().get_method_names()
# print(method_names)
# for question in method_names:
#     method_name = method_names[question]
#     print(method_name)
#     trial = Trial()
#     trial.call_method(method_name)
