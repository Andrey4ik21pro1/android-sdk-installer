from utils import get_home_path
from core import App

import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        prog="android-sdk-installer",
        description="CLI tool for Android SDK installation and environment setup"
    )

    parser.add_argument(
        "--path",
        default=str(get_home_path()),
        help="Specify the SDK installation path"
    )

    args = parser.parse_args()
    path = Path(args.path).resolve()

    app = App(path)
    app.setup()

if __name__ == "__main__":
    main()