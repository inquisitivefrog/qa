# test_script.py
import pytest
import script

def test_main(capsys):
    # Call the main function
    exit_code = script.main()
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Assert the expected output and exit code
    assert captured.out == "This is my script\n"
    assert captured.err == ""
    assert exit_code == 0
