import pytest
from pro_filer.actions.main_actions import find_duplicate_files


def test_find_duplicate_files_no_duplicates(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("content1")

    file2 = tmp_path / "file2.txt"
    file2.write_text("content2")

    context = {"all_files": [str(file1), str(file2)]}

    result = find_duplicate_files(context)

    assert result == []


def test_find_duplicate_files_with_duplicates(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("same content")

    file2 = tmp_path / "file2.txt"
    file2.write_text("same content")

    file3 = tmp_path / "file3.txt"
    file3.write_text("unique content")

    context = {"all_files": [str(file1), str(file2), str(file3)]}

    result = find_duplicate_files(context)

    assert result == [(str(file1), str(file2))]


def test_find_duplicate_files_all_duplicates(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("identical content")

    file2 = tmp_path / "file2.txt"
    file2.write_text("identical content")

    file3 = tmp_path / "file3.txt"
    file3.write_text("identical content")

    context = {"all_files": [str(file1), str(file2), str(file3)]}

    result = find_duplicate_files(context)

    assert set(result) == {(str(file1), str(file2)), (str(file1), str(file3)),
                           (str(file2), str(file3))}


def test_find_duplicate_files_no_files():
    context = {"all_files": []}

    result = find_duplicate_files(context)

    assert result == []


def test_find_duplicate_files_file_not_found(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("some content")

    non_existing_file = tmp_path / "file2.txt"

    context = {"all_files": [str(file1), str(non_existing_file)]}

    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)
