"""
Abstract base class for all processors.
"""

from abc import ABC, abstractmethod

class BaseProcessor(ABC):
    """Base processor with standard interface."""
    
    @abstractmethod
    def get_operation_type(self):
        """Returns the operation type this processor handles."""
        pass
    
    @abstractmethod
    def get_target_domain(self):
        """Returns the domain this processor targets."""
        pass
    
    @abstractmethod
    def initialize(self):
        """Initialize the processor with operation-specific setup."""
        pass
    
    def get_first_step(self):
        """Get the first step in the operation sequence."""
        return "First"

class SpecializedProcessor(BaseProcessor):
    """Specialized processor inheriting from base."""
    
    def get_operation_type(self):
        return 'how'
    
    def get_target_domain(self):
        return 'identity'
    
    def initialize(self):
        # When LLM implements this, it will maintain consistency
        # with the operation_type and target_domain defined above
        pass
