# MegaShield

MegaShield is a Python-based utility designed to automatically detect and clear unused files and applications on Windows devices, helping you to free up valuable disk space and improve system performance.

## Features

- **Unused File Detection**: Scans specified directories for files that have not been accessed in a set period and removes them.
- **Unused Application Detection**: Identifies applications that have not been used recently and uninstalls them.

## Requirements

- Python 3.x
- Windows Operating System
- Administrative privileges (required for uninstalling applications)

## Installation

1. Clone the repository or download the `megashield.py` file to your local machine.

   ```bash
   git clone https://github.com/yourusername/megashield.git
   ```

2. Ensure you have Python installed on your Windows device.

3. Run the script using a Python interpreter.

   ```bash
   python megashield.py
   ```

## Usage

- Modify the `directory_to_scan` variable in the script to point to the directory you want to scan for unused files.
- Run the script to automatically detect and remove unused files and applications.

## Notes

- The application utilizes a placeholder detection mechanism for unused applications (`SampleApp`). This should be replaced with a more sophisticated method to accurately detect unused applications.
- Ensure you have the necessary permissions to remove files and uninstall applications.

## Disclaimer

Use this utility at your own risk. Ensure that you have backups of your important data before running the script, as it will permanently delete files and uninstall applications.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.