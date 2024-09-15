# Unit Testing

import unittest
from unittest.mock import patch, mock_open
from CS_230_Project_1_By_Aditi_and_Keith import generate_short_id, shorten_url, get_full_url, save_data, load_data



class TestURLShortener(unittest.TestCase):

    def test_generate_short_id(self):
        """Test that the short ID has the correct format."""
        short_id = generate_short_id()
        self.assertEqual(len(short_id), 6)
        self.assertTrue(short_id[:3].isdigit())
        self.assertTrue(short_id[3:].isalpha())
        self.assertTrue(short_id[3:].islower())

    @patch('CS_230_Project_1_By_Aditi_and_Keith.validators.url', return_value=True)
    def test_shorten_url_valid(self, mock_validator):
        """Test shortening a valid URL."""
        url = "https://example.com"
        result = shorten_url(url)
        self.assertTrue(result.startswith("https://myApp.com/"))

    @patch('CS_230_Project_1_By_Aditi_and_Keith.validators.url', return_value=False)
    def test_shorten_url_invalid(self, mock_validator):
        """Test handling of invalid URL."""
        url = "invalidurl"
        result = shorten_url(url)
        self.assertEqual(result, "Invalid URL")

    @patch('CS_230_Project_1_By_Aditi_and_Keith.url_map', {'abc123': 'https://example.com'})
    def test_get_full_url_exist(self, mock_url_map):
        """Test retrieving an existing short URL."""
        result = get_full_url('abc123')
        self.assertEqual(result, 'https://example.com')

    @patch('CS_230_Project_1_By_Aditi_and_Keith.url_map', {})
    def test_get_full_url_not_exist(self, mock_url_map):
        """Test retrieving a non-existing short URL."""
        result = get_full_url('nonexistent')
        self.assertEqual(result, "Shortened URL does not exist.")

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_save_data(self, mock_json_dump, mock_file):
        """Test saving data to a file."""
        save_data()
        mock_file.assert_called_once_with('urls.json', 'w')
        mock_json_dump.assert_called()

    @patch('builtins.open', new_callable=mock_open, read_data='{"abc123": "https://example.com"}')
    @patch('json.load', return_value={'abc123': 'https://example.com'})
    def test_load_data(self, mock_json_load, mock_file):
        """Test loading data from a file."""
        result = load_data()
        self.assertEqual(result, {'abc123': 'https://example.com'})

if __name__ == '__main__':
    unittest.main()
