def abbreviateName(name):
    parts = name.split()
    if len(parts) == 1:
        return name  # If there's only one part, return it as is
    abbreviated = [part[0].upper() + '.' for part in parts[:-1]]
    abbreviated.append(parts[-1].capitalize())
    return ' '.join(abbreviated)

# Example usage:
print(abbreviateName("John Doe"))  # Output: J. Doe
print(abbreviateName("Jane Mary Smith"))  # Output: J. M. Smith
