class JobNotFound(Exception):
    """Exception raised when a job is not found."""
    def __init__(self, message="Job not found."):
        super().__init__(message)

class Unauthorized(Exception):
    """Exception raised for unauthorized access."""
    def __init__(self, message="Unauthorized access."):
        super().__init__(message)

class ValidationError(Exception):
    """Exception raised for validation errors."""
    def __init__(self, message="Validation error."):
        super().__init__(message)
