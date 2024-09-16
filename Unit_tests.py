# Unit Testing, Aditi 9/14/2024

import unittest
from unittest.mock import patch
import CS_230_Project_1_By_Aditi_and_Keith as url_shortener

class TestURLShortener(unittest.TestCase):
    def setUp(self):
        # Set up a fresh url_map for each test
        url_shortener.url_map = {}
    
    def test_shorten_url_valid(self):
        url = "https://example.com"
        short_url = url_shortener.shorten_url(url)
        self.assertTrue(short_url.startswith("https://myApp.com/"))
        self.assertEqual(len(short_url), len("https://myApp.com/") + 6)  # 6 is the length of the short_id

    def test_shorten_url_invalid(self):
        url = "example"
        result = url_shortener.shorten_url(url)
        self.assertEqual(result, "Invalid URL")

    def test_get_full_url_existing(self):
        url_shortener.url_map['abc123'] = "https://example.com"
        result = url_shortener.get_full_url('abc123')
        self.assertEqual(result, "https://example.com")
        
    def test_get_full_url_non_existing(self):
        result = url_shortener.get_full_url('nonexisting')
        self.assertEqual(result, "Shortened URL does not exist.")
    
    def test_save_and_load_data(self):
        url_shortener.url_map = {'abc123': "https://example.com"}
        url_shortener.save_data()
        url_shortener.url_map = {}
        url_shortener.url_map = url_shortener.load_data()
        self.assertEqual(url_shortener.url_map, {'abc123': "https://example.com"})
    
    @patch('tkinter.messagebox.showinfo')
    def test_gui_shorten_url(self, mock_showinfo):
        with patch('tkinter.simpledialog.askstring', return_value="https://example.com"):
            url_shortener.gui_shorten_url()
        mock_showinfo.assert_called_once()
        self.assertTrue(mock_showinfo.call_args[0][1].startswith("Shortened URL: https://myApp.com/"))
        
    @patch('tkinter.messagebox.showerror')
    def test_gui_get_full_url_non_existing(self, mock_showerror):
        with patch('tkinter.simpledialog.askstring', return_value="nonexisting"):
            url_shortener.gui_get_full_url()
        mock_showerror.assert_called_once_with("Error", "Shortened URL does not exist.")

if __name__ == '__main__':
    unittest.main()
