def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")
    ancient = None
    try:
        ancient = open('../ancient_fragment.txt', 'r')
    except (FileNotFoundError, Exception) as e:
        print(e)
    else:
        print("RECOVERED DATA:")
        test: str = ancient.read()
        print(test)
    finally:
        if ancient is not None:
            ancient.close()
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    ft_ancient_text()
