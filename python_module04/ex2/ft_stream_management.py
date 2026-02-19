import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    # sys.stdout.write("Input Stream active. Enter archivist ID: \n")
    # id = sys.stdin.readline()[:-1]

    # sys.stdout.write("Input Stream active. Enter status report: \n")
    # status = sys.stdin.readline()[:-1]
    try:
        sys.stdout.write(f"\n[STANDARD] Archive status from {id}: {status}\n")
        sys.stderr.write("[ALERT] System diagnostic: " +
                         "Communication channels verified\n")
        sys.stdout.write("[STANDARD] Data transmission complete\n")
    except Exception as e:
        print(e)
    else:
        print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
