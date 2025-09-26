def format_name(full_name):
    parts = full_name.strip().split()
    if len(parts) < 2:
        return full_name  # Not enough parts to swap
    # Swap first and last name
    return f"{parts[1]} {parts[0]}"

if __name__ == "__main__":
    name = input("Enter your full name (first last): ")
    formatted = format_name(name)
    print("Formatted name:", formatted)
