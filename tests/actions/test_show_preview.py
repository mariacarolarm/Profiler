import io
import contextlib
from pro_filer.actions.main_actions import show_preview


def test_show_preview_with_files_and_dirs():
    context = {
        "all_files": ["src/__init__.py", "src/app.py",
                      "src/utils/__init__.py"],
        "all_dirs": ["src", "src/utils"]
    }

    expected_output = (
        "Found 3 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )

    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        show_preview(context)

    result = captured_output.getvalue()
    assert result == expected_output


def test_show_preview_with_empty_files_and_dirs():
    context = {
        "all_files": [],
        "all_dirs": []
    }

    expected_output = (
        "Found 0 files and 0 directories\n"
    )

    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        show_preview(context)

    result = captured_output.getvalue()
    assert result == expected_output


def test_show_preview_with_more_than_five_files_and_dirs():
    context = {
        "all_files": [f"file_{i}.txt" for i in range(10)],
        "all_dirs": [f"dir_{i}" for i in range(10)]
    }

    expected_output = (
        "Found 10 files and 10 directories\n"
        "First 5 files: ['file_0.txt', 'file_1.txt', "
        "'file_2.txt', 'file_3.txt', 'file_4.txt']\n"
        "First 5 directories: ['dir_0', 'dir_1', 'dir_2', 'dir_3', 'dir_4']\n"
    )

    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        show_preview(context)

    result = captured_output.getvalue()
    assert result == expected_output


def test_show_preview_with_less_than_five_files_and_dirs():
    context = {
        "all_files": ["file_1.txt", "file_2.txt", "file_3.txt"],
        "all_dirs": ["dir_1", "dir_2"]
    }

    expected_output = (
        "Found 3 files and 2 directories\n"
        "First 5 files: ['file_1.txt', 'file_2.txt', 'file_3.txt']\n"
        "First 5 directories: ['dir_1', 'dir_2']\n"
    )

    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        show_preview(context)

    result = captured_output.getvalue()
    assert result == expected_output


def test_show_preview_only_files():
    context = {
        "all_files": ["file_1.txt", "file_2.txt", "file_3.txt"],
        "all_dirs": []
    }

    expected_output = (
        "Found 3 files and 0 directories\n"
        "First 5 files: ['file_1.txt', 'file_2.txt', 'file_3.txt']\n"
        "First 5 directories: []\n"
    )

    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        show_preview(context)

    result = captured_output.getvalue()
    assert result == expected_output


def test_show_preview_only_dirs():
    context = {
        "all_files": [],
        "all_dirs": ["dir_1", "dir_2", "dir_3"]
    }

    expected_output = (
        "Found 0 files and 3 directories\n"
        "First 5 files: []\n"
        "First 5 directories: ['dir_1', 'dir_2', 'dir_3']\n"
    )

    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        show_preview(context)

    result = captured_output.getvalue()
    assert result == expected_output
