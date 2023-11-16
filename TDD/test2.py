import unittest

class TestAdd(unittest.TestCase):
    def test_one(self):
        print('1 테스트')
        self.assertEqual(1, 1)
    
    def test_two(self):
        print('2 테스트')
        self.assertEqual(2, 2)
    
    def test_three(self):
        print('3 테스트')
        self.assertEqual(3, 3)
        
    def donghu(self):
        '''
        테스트 이름을 마음대로 정할 수 있는지 체크
        'test_'로 시작하지 않으면 테스트로 인식하지 않음
        '''
        self.assertEqual(4, 5)

if __name__ == '__main__':
    unittest.main()