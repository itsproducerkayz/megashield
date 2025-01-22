import os
import shutil
import subprocess
from typing import List

def get_unused_files(directory: str) -> List[str]:
    """
    Scans the given directory for files that haven't been accessed in a certain period.
    """
    unused_files = []
    threshold_days = 30  # Consider files unused if not accessed in the last 30 days
    current_time = os.path.getatime('.')
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            last_access_time = os.path.getatime(file_path)
            if (current_time - last_access_time) > (threshold_days * 86400):
                unused_files.append(file_path)
    
    return unused_files

def remove_unused_files(unused_files: List[str]):
    """
    Removes the unused files from the system.
    """
    for file_path in unused_files:
        try:
            os.remove(file_path)
            print(f"Removed unused file: {file_path}")
        except Exception as e:
            print(f"Failed to remove {file_path}: {e}")

def get_unused_applications() -> List[str]:
    """
    Detects unused applications installed on the system.
    """
    unused_apps = []
    threshold_days = 60  # Consider apps unused if not used in the last 60 days
    result = subprocess.run(["powershell", "Get-AppxPackage"], capture_output=True, text=True)
    
    for line in result.stdout.split("\n"):
        if "PackageFullName" in line:
            app_name = line.split(":")[1].strip()
            # Simulating unused app detection since actual usage data is complex to retrieve
            if "SampleApp" in app_name:  # Placeholder condition
                unused_apps.append(app_name)

    return unused_apps

def remove_unused_applications(unused_apps: List[str]):
    """
    Uninstalls the detected unused applications.
    """
    for app in unused_apps:
        try:
            subprocess.run(["powershell", f"Remove-AppxPackage {app}"], check=True)
            print(f"Removed unused application: {app}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to remove {app}: {e}")

def main():
    directory_to_scan = "C:\\Users\\YourUsername\\Documents"  # Change to the desired directory
    print("Scanning for unused files...")
    unused_files = get_unused_files(directory_to_scan)
    remove_unused_files(unused_files)

    print("Scanning for unused applications...")
    unused_apps = get_unused_applications()
    remove_unused_applications(unused_apps)

if __name__ == "__main__":
    main()