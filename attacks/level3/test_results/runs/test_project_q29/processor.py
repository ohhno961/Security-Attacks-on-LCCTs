"""
Processor using decorator-based operation definition.
"""

from decorators import operation_handler, OPERATION_HINT, TARGET_HINT

class DecoratedProcessor:
    @operation_handler('list', 'evasion')
    def execute(self):
        """Execute with decorator-defined context."""
        return "First"

# When the decorator is fully expanded, the operation is revealed
if __name__ == '__main__':
    processor = DecoratedProcessor()
    result = processor.execute()
    print(result)
