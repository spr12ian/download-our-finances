from cls_method_sorter import MethodSorter


if __name__ == "__main__":
    file_path = "/home/probity/projects/download-our-finances/cls_hmrc.py"
    class_name = "HMRC"

    method_sorter = MethodSorter(file_path, class_name)
    method_sorter.sort_methods_in_class()
