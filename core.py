from tools import get_download_url, download_commandline_tools, add_to_path, install_platform_tools

from pathlib import Path
import os

def check_tools() -> str | None:
    ANDROID_HOME = os.environ.get("ANDROID_HOME")
    return ANDROID_HOME

def return_path(path: Path) -> Path:
    return path / "Android" / "Sdk"

class App:
    def __init__(self, path):
        self.android_home = return_path(Path(path))

    def setup(self):
        tools = check_tools()
        if tools:
            response = input(f"Path '{tools}' already exists. Overwrite? [y/N]: ").lower().strip()
            if response not in ("y", "yes"):
                print("Aborted.")
                return

        download_url, file_name, checksum = get_download_url()
        download_commandline_tools(download_url, file_name, checksum, self.android_home)
        install_platform_tools(self.android_home)
        add_to_path(self.android_home)

        print(f"Success! Android SDK installed to path: {self.android_home}")