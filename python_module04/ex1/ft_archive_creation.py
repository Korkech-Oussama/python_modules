def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    print("Initializing new storage unit: new_discovery.txt")
    file_w = None
    try:
        file_w = open("new_discovery.txt", 'w')
    except Exception as e:
        print(e)
    else:
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        lines = [
            "[ENTRY 001] New quantum algorithm discovered\n",
            "[ENTRY 002] Efficiency increased by 347%\n",
            "[ENTRY 003] Archived by Data Archivist trainee\n"
        ]
        for line in lines:
            print(line, end="")
            file_w.write(line)
    finally:
        if file_w is not None:
            file_w.close()
        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    ft_archive_creation()
