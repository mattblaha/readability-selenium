import unittest
from readability import Reader

class MockDriver():
    def get(self,url):
        return True

    def execute_script(self,script):
        return ['<body>Article text</body>', 'Matt Blaha']

    def quit(self):
        return True

class TestReadability(unittest.TestCase):

    def test_get_readable(self):
        driver = MockDriver()
        reader = Reader(driver,readability_js="tests/Readability.js")
        dict = reader.get_readable_dict("http://www.example.com")
        self.assertEqual(dict["byline"], 'Matt Blaha')
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
