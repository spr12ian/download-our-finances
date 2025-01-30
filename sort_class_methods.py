from cls_helper_log import LogHelper
from cls_method_sorter import MethodSorter

l = LogHelper(__file__)
l.set_level_debug()
l.debug(__file__)

if __name__ == "__main__":

    directory = "/home/probity/projects/download-our-finances/"
    classes = [
        ["cls_helper_config", "ConfigHelper"],
        ["cls_helper_date_time", "DateTimeHelper"],
        ["cls_helper_google", "GoogleHelper"],
        ["cls_helper_log", "LogHelper"],
        ["cls_helper_sqlalchemy", "SQLAlchemyHelper"],
        ["cls_hmrc", "HMRC"],
        ["cls_hmrc_calculation", "HMRC_Calculation"],
        ["cls_method_sorter", "ClassFinder"],
        ["cls_method_sorter", "ClassTransformer"],
        ["cls_method_sorter", "MethodCollector"],
        ["cls_method_sorter", "MethodSorter"],
        ["cls_table_hmrc_constants_by_year", "HMRC_ConstantsByYear"],
        ["cls_table_hmrc_overrides_by_year", "HMRC_OverridesByYear"],
    ]

    for basename, class_name in classes:
        file_path = directory + basename + ".py"

        l.info(f'file_path: {file_path}')
        l.info(f'class_name: {class_name}')

        method_sorter = MethodSorter(file_path, class_name)
        method_sorter.sort_methods_in_class()
