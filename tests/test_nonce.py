import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.nonce import Nonces
class NonceTests(unittest.TestCase):
    def test_replay(self):
        n=Nonces();self.assertTrue(n.consume('a','1'));self.assertFalse(n.consume('a','1'));self.assertTrue(n.consume('b','1'))
    def test_empty(self):
        with self.assertRaises(ValueError):Nonces().consume('','1')
