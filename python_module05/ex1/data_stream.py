from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        return data_batch

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            res: str = ", ".join([str(item) for item in data_batch])
            print(f"Processing sensor batch: [{res}]")

            temps = [float(item.split(":")[1]) for item in data_batch
                     if isinstance(item, str) and item.startswith("temp")]
            avg_temp = sum(temps) / len(temps) if temps else 0.0
            ln = len(data_batch)
            return (f"Sensor analysis: {ln} "
                    f"readings processed, avg temp: {avg_temp}°C"
                    )
        except Exception as e:
            return f"Error processing sensor batch: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria == "critical":
                return [item for item in data_batch if isinstance(item, str)
                        and item.startswith("temp") and
                        float(item.split(":")[1]) > 30.0]
            return super().filter_data(data_batch, criteria)
        except Exception:
            return []


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print("\nInitializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            res: str = ", ".join([str(item) for item in data_batch])
            print(f"Processing transaction batch: [{res}]")

            flows = [float(item.split(":")[1]) if item.startswith("buy")
                     else -float(item.split(":")[1])
                     for item in data_batch if isinstance(item, str)
                     and (item.startswith("buy") or item.startswith("sell"))]
            net = int(sum(flows))
            sign = "+" if net > 0 else ""
            ln = len(data_batch)
            return (f"Transaction analysis: {ln} operations,"
                    f" net flow: {sign}{net} units")
        except Exception as e:
            return f"Error processing transaction batch: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria == "large":
                return [item for item in data_batch if isinstance(item, str)
                        and float(item.split(":")[1]) > 1000.0]
            return super().filter_data(data_batch, criteria)
        except Exception:
            return []


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print("\nInitializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            res: str = ", ".join([str(item) for item in data_batch])
            print(f"Processing event batch: [{res}]")

            errors = len([item for item in data_batch
                          if isinstance(item, str) and item == "error"])
            ln = len(data_batch)
            return f"Event analysis: {ln} events, {errors} error detected"
        except Exception as e:
            return f"Error processing event batch: {e}"


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def run_pipeline(self, batches: Dict[str, List[Any]]) -> None:
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")

        sensor_alerts = 0
        large_tx = 0

        for stream in self.streams:
            batch = batches.get(stream.stream_id, [])

            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {len(batch)} readings processed")
                sensor_alerts = len(stream.filter_data(batch, "critical"))
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {len(batch)} operations processed")
                large_tx = len(stream.filter_data(batch, "large"))
            elif isinstance(stream, EventStream):
                print(f"- Event data: {len(batch)} events processed")
        print("\nStream filtering active: High-priority data only")
        print(f"Filtered results: {sensor_alerts} " +
              f"critical sensor alerts, {large_tx} large transaction\n")
        print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(sensor.process_batch(sensor_batch))

    tx = TransactionStream("TRANS_001")
    tx_batch = ["buy:100", "sell:150", "buy:75"]
    print(tx.process_batch(tx_batch))

    event = EventStream("EVENT_001")
    event_batch = ["login", "error", "logout"]
    print(event.process_batch(event_batch))

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(tx)
    processor.add_stream(event)

    polymorphic_batches = {
        "SENSOR_001": ["temp:40.0", "temp:35.0"],
        "TRANS_001": ["buy:1500", "sell:10", "buy:5", "sell:5"],
        "EVENT_001": ["login", "warning", "logout"]
    }

    processor.run_pipeline(polymorphic_batches)
