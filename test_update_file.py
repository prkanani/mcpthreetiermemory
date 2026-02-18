def update_file(filename, content):
    """Update the given file with the provided content."""
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"File '{filename}' updated successfully.")
    except Exception as e:
        print(f"Error updating file '{filename}': {e}")

if __name__ == '__main__':
    filename = 'example.txt'
    content = 'This is the updated content of the file.\n'
    update_file(filename, content)
