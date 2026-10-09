import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from unit_economics import result
class EconomicsTests(unittest.TestCase):
 def test_loss_increases_with_volume(self):
  self.assertEqual(result(90,100,1000,20000)['operating_result'],-30000)
  self.assertEqual(result(90,100,2000,20000)['operating_result'],-40000)
  self.assertIsNone(result(90,100,1000,20000)['break_even_volume'])
 def test_break_even(self):self.assertEqual(result(120,100,1000,20000)['break_even_volume'],1000)
 def test_nan(self):
  with self.assertRaises(ValueError):result(float('nan'),100,10,100)
 def test_negative(self):
  with self.assertRaises(ValueError):result(10,1,-1,0)
