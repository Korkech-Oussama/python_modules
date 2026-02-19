def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("Initiating secure vault access...")

    with open('../classified_data.txt', 'r') as f_extract:
        print("Vault connection established with failsafe protocols\n")
        print("SECURE EXTRACTION:")
        res: str = f_extract.read()
        print(res)

    with open('new_file.txt', 'w') as f_preserve:
        print("\nSECURE PRESERVATION:")
        line: str = "[CLASSIFIED] New security protocols archived\n"
        print(line, end="")
        f_preserve.write(line)

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
