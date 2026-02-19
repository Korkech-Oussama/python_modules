def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open('lost_archive.txt'):
            pass
    except (FileNotFoundError, Exception):
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")

    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open('classified_vault.txt', 'r+'):
            pass
    except (PermissionError, Exception):
        print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained")

    try:
        print("\nROUTINE ACCESS: Attempting " +
              "access to 'standard_archive.txt'...")
        with open('../standard_archive.txt', 'r') as f:
            res = f.read()
            print(f"SUCCESS: Archive recovered - ``{res}''")
    except Exception as e:
        print(e)
    print("STATUS: Normal operations resumed\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
