import unittest
from unittest.mock import patch, mock_open
import os
import sys

# Adjust path to import from parent directory's 'think_project' module
# This allows running the test file directly for development/debugging.
# For automated test discovery (e.g., python -m unittest discover),
# the test runner usually handles path adjustments.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from think_project.think import _handle_file_create, _handle_file_delete

class TestFileOperations(unittest.TestCase):
    # --- Tests for _handle_file_create ---
    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open)
    def test_create_file_success_oluştur(self, mock_file_open, mock_print):
        """Test successful file creation with 'oluştur' keyword."""
        command = "dosya oluştur testfile.txt"
        _handle_file_create(command)
        mock_file_open.assert_called_once_with("testfile.txt", "w")
        mock_print.assert_called_with(f"testfile.txt dosyasını oluşturuyorum.")

    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open)
    def test_create_file_success_yarat(self, mock_file_open, mock_print):
        """Test successful file creation with 'yarat' keyword."""
        command = "dosya yarat anotherfile.txt"
        _handle_file_create(command)
        mock_file_open.assert_called_once_with("anotherfile.txt", "w")
        mock_print.assert_called_with(f"anotherfile.txt dosyasını oluşturuyorum.")

    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open) # Should not be called
    def test_create_file_no_filename_oluştur(self, mock_file_open, mock_print):
        """Test file creation with 'oluştur' but no filename."""
        command = "dosya oluştur"
        _handle_file_create(command)
        mock_file_open.assert_not_called()
        mock_print.assert_called_with("Dosya adı belirtilmedi.")
        
    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open) # Should not be called
    def test_create_file_no_filename_yarat(self, mock_file_open, mock_print):
        """Test file creation with 'yarat' but no filename."""
        command = "dosya yarat"
        _handle_file_create(command)
        mock_file_open.assert_not_called()
        mock_print.assert_called_with("Dosya adı belirtilmedi.")

    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open)
    def test_create_file_with_exception(self, mock_file_open, mock_print):
        """Test file creation when open() raises an exception."""
        mock_file_open.side_effect = OSError("Test OS Error")
        command = "dosya oluştur errorfile.txt"
        _handle_file_create(command)
        mock_file_open.assert_called_once_with("errorfile.txt", "w")
        mock_print.assert_called_with("Dosya oluşturulurken hata: Test OS Error")


    # --- Tests for _handle_file_delete ---
    @patch('builtins.print')
    @patch('os.remove')
    @patch('os.path.exists', return_value=True)
    def test_delete_file_success(self, mock_exists, mock_os_remove, mock_print):
        """Test successful file deletion."""
        command = "dosya sil testfile.txt"
        _handle_file_delete(command)
        mock_exists.assert_called_once_with("testfile.txt")
        mock_os_remove.assert_called_once_with("testfile.txt")
        mock_print.assert_called_with(f"testfile.txt dosyası silindi.")

    @patch('builtins.print')
    @patch('os.remove') # Should not be called
    @patch('os.path.exists', return_value=False)
    def test_delete_file_not_exists(self, mock_exists, mock_os_remove, mock_print):
        """Test file deletion when file does not exist."""
        command = "dosya sil non_existent_file.txt"
        _handle_file_delete(command)
        mock_exists.assert_called_once_with("non_existent_file.txt")
        mock_os_remove.assert_not_called()
        mock_print.assert_called_with(f"non_existent_file.txt dosyası bulunamadı.")

    @patch('builtins.print')
    @patch('os.remove') # Should not be called
    @patch('os.path.exists') # Should not be called if no filename
    def test_delete_file_no_filename(self, mock_exists, mock_os_remove, mock_print):
        """Test file deletion with no filename provided."""
        command = "dosya sil"
        _handle_file_delete(command)
        mock_exists.assert_not_called()
        mock_os_remove.assert_not_called()
        mock_print.assert_called_with("Dosya adı belirtilmedi.")

    @patch('builtins.print')
    @patch('os.remove', side_effect=OSError("Test OS Error on delete"))
    @patch('os.path.exists', return_value=True)
    def test_delete_file_with_exception(self, mock_exists, mock_os_remove, mock_print):
        """Test file deletion when os.remove() raises an exception."""
        command = "dosya sil errorfile.txt"
        _handle_file_delete(command)
        mock_exists.assert_called_once_with("errorfile.txt")
        mock_os_remove.assert_called_once_with("errorfile.txt")
        mock_print.assert_called_with("Dosya silinirken hata: Test OS Error on delete")


if __name__ == '__main__':
    unittest.main()
