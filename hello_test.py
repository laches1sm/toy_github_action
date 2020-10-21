import unittest

class TestHelloWorld(unittest.TestCase):
    def test_parrot(self):
        self.assertEqual("parrot".upper, "PARROT")
        

if __name__ == '__main__':
    unittest.main()        
