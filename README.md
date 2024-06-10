# File Integrity Checker

This Python script is designed for security purposes, enabling users to detect file tampering or corruption by comparing hash values. 

## Usage
1. **Installation:** Ensure you have Python installed on your system.
2. **Setup:** Place the script in the directory containing the files you wish to monitor.
3. **Execution:** Run the script using the command line, specifying the directory containing the compromised files.
    ```bash
    python file_integrity_checker.py compromised_directory
    ```
4. **Output:** The script will compare the hash values of compromised and original files. If discrepancies are found, indicating potential tampering, the script will alert the user.

## Dependencies
- `os`: For handling file paths.
- `sys`: For accepting command-line arguments.
- `hashlib`: For generating hash values.

## Functionality
- The script recursively walks through the specified directory to identify compromised files.
- It generates MD5 hash values for both the compromised and original files.
- If the hash values differ, the script alerts the user, indicating potential file modification.
- It also detects newly created files within the directory.

## Note
- For optimal functionality, ensure the script is executed with appropriate permissions to access the files within the specified directory.
- In case of any issues or concerns, feel free to open an issue or reach out to the project maintainers.


[Project Description.pdf](https://github.com/tahirabbas11/File-Hash-Matching-Python-/files/10087392/Project.Description.pdf)
