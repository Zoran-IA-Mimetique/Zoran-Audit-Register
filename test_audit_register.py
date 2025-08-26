import unittest, json, os
from audit_register import log_action, LOG_FILE

class TestAuditRegister(unittest.TestCase):
    def test_log_action(self):
        entry, root = log_action("test_action", "allowed")
        self.assertIn("hash", entry)
        self.assertTrue(len(root) == 64)

    def test_merkle_chain_integrity(self):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIn("merkle_root", data)

if __name__ == "__main__":
    unittest.main()
