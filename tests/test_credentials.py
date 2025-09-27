import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.credentials import issue,evaluate
class CredentialTests(unittest.TestCase):
    def test_valid_and_tampered(self):
        c=issue(10,100,'salt',b'key');self.assertTrue(evaluate(c,b'key','demo-issuer',20,50)[0]);c['payload']['dob']=5;self.assertFalse(evaluate(c,b'key','demo-issuer',20,50)[0])
    def test_cutoff_boundary(self):
        c=issue(20,50,'s',b'key');self.assertTrue(evaluate(c,b'key','demo-issuer',20,50)[0]);self.assertFalse(evaluate(c,b'key','demo-issuer',19,50)[0])
