class JobMatcher:
    def __init__(self, jobs, user_criteria):
        self.jobs = jobs  # List of jobs
        self.user_criteria = user_criteria  # Criteria for matching

    def match_jobs(self):
        matched_jobs = []
        for job in self.jobs:
            if self._matches_criteria(job):
                matched_jobs.append(job)
        return matched_jobs

    def _matches_criteria(self, job):
        # Check job against user criteria
        for key, value in self.user_criteria.items():
            if job.get(key) != value:
                return False
        return True

# Example usage:
if __name__ == '__main__':
    jobs = [
        {'title': 'Software Engineer', 'location': 'Remote', 'salary': 80000},
        {'title': 'Data Scientist', 'location': 'On-site', 'salary': 90000},
    ]
    user_criteria = {'location': 'Remote', 'salary': 80000}
    matcher = JobMatcher(jobs, user_criteria)
    matched = matcher.match_jobs()
    print(matched)  # Output: [{'title': 'Software Engineer', 'location': 'Remote', 'salary': 80000}]