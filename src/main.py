import ctypes
import subprocess
from pathlib import Path

import keyboard

# Track the current resolution state.
current_resolution = "1920x1080"


def find_nircmd() -> Path:
    """Find NirCmd in the repository or the legacy parent-folder location."""
    script_path = Path(__file__).resolve()
    repository_path = script_path.parents[2]
    candidates = (
        repository_path / "nircmd-x64" / "nircmd.exe",
        repository_path.parent / "nircmd-x64" / "nircmd.exe",
    )

    for candidate in candidates:
        if candidate.is_file():
            return candidate

    searched_paths = "\n".join(str(path) for path in candidates)
    raise FileNotFoundError(
        "NirCmd was not found. Place nircmd.exe in one of these locations:\n"
        f"{searched_paths}"
    )


def run_nircmd(*args):
    nircmd_path = find_nircmd()

    result = subprocess.run(
        [str(nircmd_path), *args],
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

    try:
        if current_resolution == "1920x1080":
            run_nircmd("setdisplay", "1440", "1080", "32")
            current_resolution = "1440x1080"
            print("Resolution changed to 1440x1080")
        else:
            run_nircmd("setdisplay", "1920", "1080", "32")
            current_resolution = "1920x1080"
            print("Resolution changed to 1920x1080")
    except (FileNotFoundError, OSError, RuntimeError) as error:
        print(f"Could not change the display resolution: {error}")


def main():
    find_nircmd()
    keyboard.add_hotkey("`", change_display_resolution)
    print("Press ` to toggle resolution between 1440x1080 and 1920x1080.")
    keyboard.wait()


if __name__ == "__main__":
    main()