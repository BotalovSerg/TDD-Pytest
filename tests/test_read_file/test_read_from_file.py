from backend.utils.read_file import read_file_get_list


def create_test_data(file_path, data: list[str]):
    with open(file_path, "a") as file:
        file.writelines(data)


def test_read_from_file_one(test_file_path):
    test_data = ["one\n", "two\n", "three\n"]
    create_test_data(test_file_path, test_data)
    assert test_data == read_file_get_list(test_file_path)


def test_read_from_file_two(test_file_path):
    test_data = ["one\n", "two\n", "three\n", "four\n"]
    create_test_data(test_file_path, test_data)
    assert test_data == read_file_get_list(test_file_path)
