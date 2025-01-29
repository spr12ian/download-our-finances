from cls_helper_log import LogHelper
from cls_method_sorter import MethodSorter

l = LogHelper(__file__)
l.set_level_debug()
l.debug(__file__)

if __name__ == "__main__":

    directory = "/home/probity/projects/download-our-finances/"
    classes = [
        ["cls_hmrc", "HMRC"],
        ["cls_hmrc_calculation", "HMRC_Calculation"],
    ]

    for basename, class_name in classes:
        file_path = directory + basename + ".py"

        l.info(f'file_path: {file_path}')
        l.info(f'class_name: {class_name}')

        method_sorter = MethodSorter(file_path, class_name)
        method_sorter.sort_methods_in_class()
