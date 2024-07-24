import io
import contextlib
from unittest import mock
from pro_filer.actions.main_actions import show_details


def test_show_details_file_not_exists():
    context = {"base_path": "/home/trybe/????"}
    expected_output = "File '????' does not exist\n"

    with mock.patch("os.path.exists", return_value=False):
        captured_output = io.StringIO()
        with contextlib.redirect_stdout(captured_output):
            show_details(context)

    result = captured_output.getvalue()
    assert result == expected_output


def test_show_details_file_exists_with_extension():
    context = {"base_path": "/home/trybe/Downloads/Trybe_logo.png"}
    expected_output = (
        "File name: Trybe_logo.png\n"
        "File size in bytes: 22438\n"
        "File type: file\n"
        "File extension: .png\n"
        "Last modified date: 2023-06-13\n"
    )

    with mock.patch("os.path.exists", return_value=True), \
         mock.patch("os.path.getsize", return_value=22438), \
         mock.patch("os.path.isdir", return_value=False), \
         mock.patch("os.path.getmtime", return_value=1686662400), \
         mock.patch("os.path.splitext", return_value=("Trybe_logo", ".png")):

        captured_output = io.StringIO()
        with contextlib.redirect_stdout(captured_output):
            show_details(context)

    result = captured_output.getvalue()
    assert result == expected_output


def test_show_details_file_exists_no_extension():
    context = {"base_path": "/home/trybe/Downloads/file_no_ext"}
    expected_output = (
        "File name: file_no_ext\n"
        "File size in bytes: 12345\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date: 2023-06-13\n"
    )

    with mock.patch("os.path.exists", return_value=True), \
         mock.patch("os.path.getsize", return_value=12345), \
         mock.patch("os.path.isdir", return_value=False), \
         mock.patch("os.path.getmtime", return_value=1686662400), \
         mock.patch("os.path.splitext", return_value=("file_no_ext", "")):

        captured_output = io.StringIO()
        with contextlib.redirect_stdout(captured_output):
            show_details(context)

    result = captured_output.getvalue()
    assert result == expected_output


def test_show_details_directory_exists():
    context = {"base_path": "/home/trybe/Downloads/some_directory"}
    expected_output = (
        "File name: some_directory\n"
        "File size in bytes: 4096\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        "Last modified date: 2023-06-13\n"
    )

    with mock.patch("os.path.exists", return_value=True), \
         mock.patch("os.path.getsize", return_value=4096), \
         mock.patch("os.path.isdir", return_value=True), \
         mock.patch("os.path.getmtime", return_value=1686662400), \
         mock.patch("os.path.splitext", return_value=("some_directory", "")):

        captured_output = io.StringIO()
        with contextlib.redirect_stdout(captured_output):
            show_details(context)

    result = captured_output.getvalue()
    assert result == expected_output
