"""
Utility functions following naming conventions.
"""

from constants import OperationConstants, PATTERN_ID

def hiea_initialize():
    """Initialize {PATTERN_ID} operation."""
    return OperationConstants.INIT_STEP

def hiea_get_operation():
    """Get operation for {PATTERN_ID} pattern."""
    return OperationConstants.OPERATION_NAME

def hiea_get_target():
    """Get target for {PATTERN_ID} pattern."""
    return OperationConstants.TARGET_NAME

def initialize_processor():
    """Initialize main processor using {PATTERN_ID} pattern."""
    init_result = hiea_initialize()
    return init_result
