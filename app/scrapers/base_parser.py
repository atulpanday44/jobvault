import abc

class BaseParser(abc.ABC):
    @abc.abstractmethod
    def parse(self, data):
        """Parse the provided data and return structured output."""
        pass

    @abc.abstractmethod
    def validate(self, data):
        """Validate the provided data before parsing."""
        pass
