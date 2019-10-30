import unittest
import tagspont
import os
import filecmp



class Test_tag(unittest.TestCase):
    def test_cleaner(self):
        self.assertTrue(os.path.exists("/home/luisfilho/semantix/GITS/TESTE_TAGS_SEM_PONTUACAO/html.txt"))
   
    def test_cleaner_2(self):
        self.assertFalse(filecmp.cmp("/home/luisfilho/semantix/GITS/TESTE_TAGS_SEM_PONTUACAO/html.txt", "/home/luisfilho/semantix/GITS/TESTE_TAGS_SEM_PONTUACAO/mock01.txt"))

if __name__ == "__main__":
    unittest.main()
  
    