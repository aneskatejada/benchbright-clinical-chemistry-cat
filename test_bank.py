import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build import read_bank

class ChemistryBankTests(unittest.TestCase):
    def test_source_count(self):
        ready,review,total=read_bank()
        self.assertEqual(total,976)
        self.assertEqual(len(ready),608)
        self.assertEqual(len(review),368)
    def test_ready_items(self):
        items,_,_=read_bank()
        self.assertGreaterEqual(len(items),100)
        self.assertEqual(len({q['id'] for q in items}),len(items))
        self.assertGreaterEqual(len({q['topic'] for q in items}),8)
        for item in items:
            self.assertIn(item['answer'],'ABCD')
            self.assertEqual(len(item['options']),4)
            self.assertEqual(len(set(item['options'])),4)
            self.assertTrue(1<=item['difficulty']<=5)
            self.assertTrue(item['rationale'])
            self.assertNotIn('Chemistry/Apply', ''.join(item['options']))

if __name__=='__main__':unittest.main()
