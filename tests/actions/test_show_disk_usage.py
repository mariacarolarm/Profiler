from pro_filer.actions.main_actions import show_disk_usage


def test_show_disk_usage_with_two_files(tmp_path, capsys):
    file_a = tmp_path / "file_a.txt"
    file_a.write_text("hello world")

    file_b = tmp_path / "file_b.txt"
    file_b.write_text("test")

    context = {"all_files": [str(file_a), str(file_b)]}

    show_disk_usage(context)

    captured = capsys.readouterr().out

    output_lines = captured.splitlines()

    total_size_line = output_lines[-1]
    file_a_line = next(line for line in output_lines if "file_a.txt" in line)
    file_b_line = next(line for line in output_lines if "file_b.txt" in line)

    assert "Total size: 15" in total_size_line
    assert "file_a.txt" in file_a_line and "11 (73%)" in file_a_line
    assert "file_b.txt" in file_b_line and "4 (26%)" in file_b_line


def test_show_disk_usage_no_files_empty_context(capsys):
    context = {"all_files": []}

    show_disk_usage(context)

    captured = capsys.readouterr().out

    assert "Total size: 0" in captured


def test_show_disk_usage_with_unsorted_files(tmp_path, capsys):
    file_a = tmp_path / "file_a.txt"
    file_a.write_text("A" * 20)

    file_b = tmp_path / "file_b.txt"
    file_b.write_text("B" * 10)

    file_c = tmp_path / "file_c.txt"
    file_c.write_text("C" * 5)

    context = {"all_files": [str(file_c), str(file_b), str(file_a)]}

    show_disk_usage(context)

    captured = capsys.readouterr().out

    output_lines = captured.splitlines()

    assert "file_a.txt" in output_lines[0] and "20 (57%)" in output_lines[0]
    assert "file_b.txt" in output_lines[1] and "10 (28%)" in output_lines[1]
    assert "file_c.txt" in output_lines[2] and "5 (14%)" in output_lines[2]
    assert "Total size: 35" in output_lines[-1]
