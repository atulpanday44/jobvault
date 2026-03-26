import hashlib

class JobDeduplicator:
    def __init__(self):
        self.job_hashes = set()

    def deduplicate(self, job_data):
        # Create a unique hash for the job data using SHA256
        job_hash = hashlib.sha256(job_data.encode('utf-8')).hexdigest()
        
        if job_hash in self.job_hashes:
            # Job is a duplicate
            return False
        else:
            # Store the hash and accept the job
            self.job_hashes.add(job_hash)
            return True

# Example usage:
# deduplicator = JobDeduplicator()
# print(deduplicator.deduplicate('job1'))  # True
# print(deduplicator.deduplicate('job1'))  # False
