import unittest
from your_module import deduplicate_jobs  # Adjust the import based on your project structure

class TestJobDeduplication(unittest.TestCase):

    def test_unique_hashes(self):
        jobs = [
            {"id": 1, "hash": "abc123"},
            {"id": 2, "hash": "def456"}
        ]
        result = deduplicate_jobs(jobs)
        self.assertEqual(len(result), 2)

    def test_duplicate_hashes(self):
        jobs = [
            {"id": 1, "hash": "abc123"},
            {"id": 2, "hash": "abc123"}
        ]
        result = deduplicate_jobs(jobs)
        self.assertEqual(len(result), 1)

    def test_mixed_hashes(self):
        jobs = [
            {"id": 1, "hash": "abc123"},
            {"id": 2, "hash": "def456"},
            {"id": 3, "hash": "abc123"}
        ]
        result = deduplicate_jobs(jobs)
        self.assertEqual(len(result), 2)

if __name__ == "__main__":
    unittest.main()