# test_cli_args.py

import pytest
import subprocess
import sys

import cli_args

# Test the read_args function
def test_read_args_name_only(mocker):
    mocker.patch("sys.argv", ["cli_args.py", "Alice"])
    args = cli_args.read_args()
    assert args.name == "Alice"
    assert args.age is None

def test_read_args_name_and_age(mocker):
    mocker.patch("sys.argv", ["cli_args.py", "Bob", "--age", "30"])
    args = cli_args.read_args()
    assert args.name == "Bob"
    assert args.age == 30

def test_read_args_missing_name(mocker):
    mocker.patch("sys.argv", ["cli_args.py"])
    with pytest.raises(SystemExit) as exc_info:
        cli_args.read_args()
    assert exc_info.value.code == 2

def test_read_args_invalid_age(mocker):
    mocker.patch("sys.argv", ["cli_args.py", "Alice", "--age", "invalid"])
    with pytest.raises(SystemExit) as exc_info:
        cli_args.read_args()
    assert exc_info.value.code == 2

def test_read_args_empty_name(mocker):
    mocker.patch("sys.argv", ["cli_args.py", ""])
    args = cli_args.read_args()
    assert args.name == ""
    assert args.age is None

# Test the main function
def test_main_no_args(capsys, mocker):
    mocker.patch("sys.argv", ["cli_args.py"])
    
    exit_code = cli_args.main()
    
    captured = capsys.readouterr()
    assert captured.out == "Script name: cli_args.py\nArguments: []\n"
    assert captured.err == ""
    assert exit_code == 0

def test_main_with_name(capsys, mocker):
    mocker.patch("sys.argv", ["cli_args.py", "Alice"])
    
    exit_code = cli_args.main()
    
    captured = capsys.readouterr()
    expected_output = (
        "Script name: cli_args.py\n"
        "Arguments: ['Alice']\n"
        "Name: Alice\n"
    )
    assert captured.out == expected_output
    assert captured.err == ""
    assert exit_code == 0

def test_main_with_name_and_age(capsys, mocker):
    mocker.patch("sys.argv", ["cli_args.py", "Bob", "--age", "30"])
    
    exit_code = cli_args.main()
    
    captured = capsys.readouterr()
    expected_output = (
        "Script name: cli_args.py\n"
        "Arguments: ['Bob', '--age', '30']\n"
        "Name: Bob\n"
        "Age: 30\n"
    )
    assert captured.out == expected_output
    assert captured.err == ""
    assert exit_code == 0

def test_main_invalid_args(capsys, mocker):
    mocker.patch("sys.argv", ["cli_args.py", "--age", "30"])
    
    exit_code = cli_args.main()
    
    captured = capsys.readouterr()
    assert "Script name: cli_args.py" in captured.out
    assert "Arguments: ['--age', '30']" in captured.out
    assert "error: the following arguments are required: name" in captured.err
    assert exit_code == 2

def test_main_empty_name(capsys, mocker):
    mocker.patch("sys.argv", ["cli_args.py", ""])
    
    exit_code = cli_args.main()
    
    captured = capsys.readouterr()
    assert "Script name: cli_args.py" in captured.out
    assert "Arguments: ['']" in captured.out
    assert "Error: Name cannot be empty" in captured.err
    assert exit_code == 1

def test_main_negative_age(capsys, mocker):
    mocker.patch("sys.argv", ["cli_args.py", "Bob", "--age", "-30"])
    
    exit_code = cli_args.main()
    
    captured = capsys.readouterr()
    assert "Script name: cli_args.py" in captured.out
    assert "Arguments: ['Bob', '--age', '-30']" in captured.out
    assert "Error: Age cannot be negative" in captured.err
    assert exit_code == 1

def test_main_name_with_spaces(capsys, mocker):
    mocker.patch("sys.argv", ["cli_args.py", "Alice Smith"])
    exit_code = cli_args.main()
    captured = capsys.readouterr()
    expected_output = (
        "Script name: cli_args.py\n"
        "Arguments: ['Alice Smith']\n"
        "Name: Alice Smith\n"
    )
    assert captured.out == expected_output
    assert captured.err == ""
    assert exit_code == 0

def test_script_execution(capsys):
    result = subprocess.run(
        ["python3", "cli_args.py", "Alice"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Script name: cli_args.py" in result.stdout
    assert "Arguments: ['Alice']" in result.stdout
    assert "Name: Alice" in result.stdout
    assert result.stderr == ""
