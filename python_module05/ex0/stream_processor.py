from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    # Injected Optional and Dict into the base method signature
    def format_output(self, result: str,
                      metadata: Optional[Dict[str, Any]] = None) -> str:
        return result


class NumericProcessor(DataProcessor):

    def process(self, data: List[Union[int, float]]) -> str:
        try:
            print(f"Processing data: {data}")
            s = 0
            i = 0
            for item in data:
                i += 1
                s += int(item)
            avg = s / len(data)
        except Exception as e:
            return f"Error: {e}"
        else:
            return f"Output: Processed {i} numeric values, sum={s}, avg={avg}"

    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            return False
        for item in data:
            if type(item) is not int:
                return False
        print("Validation: Numeric data verified")
        return True

    # Added type hints to match the parent's new signature
    def format_output(self, result: str,
                      metadata: Optional[Dict[str, Any]] = None) -> str:
        return super().format_output(result, metadata)


class TextProcessor(DataProcessor):

    def process(self, data: str) -> str:
        try:
            print(f"Processing data: {data}")
            char_c = 0
            word_c = 1
            for item in data:
                if item == ' ':
                    word_c += 1
                char_c += 1
        except Exception as e:
            return f"Error: {e}"
        else:
            return f"Output:Processed text:{char_c} characters, {word_c} words"

    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            return False
        print("Validation: Text data verified")
        return True

    def format_output(self, result: str,
                      metadata: Optional[Dict[str, Any]] = None) -> str:
        return super().format_output(result, metadata)


class LogProcessor(DataProcessor):

    def process(self, data: str) -> str:
        try:
            print(f'Processing data: "{data}"')
            parts = data.split(": ", 1)
            level = parts[0]
            message = parts[1] if len(parts) > 1 else ""
            prefix = "[ALERT]" if level == "ERROR" else f"[{level}]"
            return f"{prefix} {level} level detected: {message}"
        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        if type(data) is not str or ":" not in data:
            return False
        print("Validation: Log entry verified")
        return True

    def format_output(self, result: str,
                      metadata: Optional[Dict[str, Any]] = None) -> str:
        return result


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numeric_list: List[int] = [1, 2, 3, 4, 5]
    numeric = NumericProcessor()
    numeric.validate(numeric_list)
    res = numeric.process(numeric_list)
    print(numeric.format_output(res))

    print("\nInitializing Text Processor...")
    line: str = "Hello Nexus World"
    text = TextProcessor()
    text.validate(line)
    res = text.process(line)
    print(text.format_output(res))

    print("\nInitializing Log Processor...")
    log_line: str = "ERROR: Connection timeout"
    log_proc = LogProcessor()
    log_proc.validate(log_line)
    res = log_proc.process(log_line)
    print(log_proc.format_output(res))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    # Using List and Union one more time in the main execution block
    streams: List[tuple[DataProcessor, Any]] = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello World!"),
        (LogProcessor(), "INFO: System ready")
    ]

    i = 1
    for processor, data in streams:
        res = processor.process(data)
        print(f"Result {i}: {res}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")
