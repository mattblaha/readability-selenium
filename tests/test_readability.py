import unittest
from readability import Reader

class MockDriver():
    url = ""
    def get(self,url):
        self.url = url
        return True

    def execute_script(self,script):
        if self.url == "http://www.example.com/no-author/":
            return ['Article text\n\n', None]
        else:
            return ['Article text\n\n', 'Matt Blaha']

    def quit(self):
        return True

class TestReadability(unittest.TestCase):

    def test_get_readable(self):
        driver = MockDriver()
        reader = Reader(driver,readability_js="tests/Readability.js")
        dict = reader.get_readable_dict("http://www.example.com")
        self.assertEqual(dict["byline"], 'Matt Blaha')
        self.assertEqual(dict["content"], 'Article text\n\n')

    def test_get_readable_no_author(self):
        driver = MockDriver()
        reader = Reader(driver,readability_js="tests/Readability.js")
        dict = reader.get_readable_dict("http://www.example.com/no-author/")
        self.assertEqual(dict["byline"], 'Unknown')
        self.assertEqual(dict["content"], 'Article text\n\n')

    def test_get_url(self):
        driver = MockDriver()
        reader = Reader(driver,readability_js="tests/Readability.js")
        content = reader.get_url("http://www.example.com")
        self.assertEqual(content, 'Article text\n\n')

    def test_readable(self):
        driver = MockDriver()
        reader = Reader(driver,readability_js="tests/Readability.js")
        content = reader.get_readable("http://www.example.com")
        self.assertEqual(content, 'Article text\n\n')

if __name__ == '__main__':
    unittest.main()
