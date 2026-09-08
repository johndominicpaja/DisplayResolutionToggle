import subprocess
from pathlib import Path

import keyboard

# Track the current resolution state
current_resolution = "1920x1080"
NIRCMD_PATH = Path(__file__).resolve().parents[3] / "nircmd-x64" / "nircmd.exe"


def run_nircmd(*args):
    if not NIRCMD_PATH.exists():
        raise FileNotFoundError(f"NirCmd was not found at: {NIRCMD_PATH}")

    result = subprocess.run(
        [str(NIRCMD_PATH), *args],
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or "Unknown error"
        raise RuntimeError(f"NirCmd failed: {message}")

    return result


def change_display_resolution():
    global current_resolution

    if current_resolution == "1920x1080":
        run_nircmd("setdisplay", "1024", "768", "32")
        current_resolution = "1024x768"
        print("Resolution changed to 1024x768")
    else:
        run_nircmd("setdisplay", "1920", "1080", "32")
        current_resolution = "1920x1080"
        print("Resolution changed to 1920x1080")


def main():
    keyboard.add_hotkey("f11", change_display_resolution)
    print("Press F11 to toggle resolution between 1024x768 and 1920x1080.")
    keyboard.wait()


if __name__ == "__main__":
    main()