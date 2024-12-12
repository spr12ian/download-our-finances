from cls_table_categories import Categories


class HMRC_Category(Categories):
    def __init__(self, category, person_code):
        category = self.get_hmrc_category(category, person_code)
        super().__init__(category)

    def get_hmrc_category(self, category, person_code):
        first_four_chars = category[:4]
        if first_four_chars == "HMRC":
            return category
        else:
            return f"HMRC {person_code} {category}"

    def get_hmrc_page(self):
        return self.get_value_by_category("HMRC page")

    def get_hmrc_question_id(self):
        return self.get_value_by_category("HMRC question id")
