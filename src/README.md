# python-display-settings/python-display-settings/README.md

# Python Display Settings

This program toggles the display resolution between `1024x706` and `1920x1080` when you press `F11`. It requests stretched scaling for the lower resolution to avoid black bars.

## Dependencies

### Python packages

- [keyboard](https://pypi.org/project/keyboard/): Registers the `F11` hotkey and waits for keyboard events.
- `pygetwindow`: Included in `requirements.txt` for window management support.
- `pyautogui`: Included in `requirements.txt` for GUI automation support.

Install it from the project directory with:

```powershell
pip install -r requirements.txt
```

### NirCmd

The program also depends on the Windows utility [NirCmd](https://www.nirsoft.net/utils/nircmd.html).

Place the 64-bit executable at the repository root:

```text
nircmd-x64/nircmd.exe
```

The program uses NirCmd to apply the display resolution changes. It must be available before starting the script. The executable is currently missing from this workspace and must be added before running the program.

## Usage

1. Open PowerShell in this project directory.
2. Install the Python dependency:

	```powershell
	pip install -r requirements.txt
	```

3. Start the program:

	```powershell
	python src/main.py
	```

4. Press `F11` to switch between the two resolutions.
5. Stop the program with `Ctrl+C` in the PowerShell window.

## Summary

<!-- Write your project summary here. -->


## Notes

- This program is intended for Windows because it uses NirCmd.
- The keyboard package may require administrator privileges on some systems.