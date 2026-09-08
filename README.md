# Python Display Settings

This Windows program lets you press `F11` to switch the display resolution
between `1920x1080` and `1024x706`.

## Requirements

- Windows
- Python 3
- The packages listed in [`src/requirements.txt`](src/requirements.txt)
- The 64-bit [NirCmd](https://www.nirsoft.net/utils/nircmd.html) utility

The required Python packages are:

- `keyboard` - listens for the `F11` hotkey
- `pygetwindow`
- `pyautogui`

## Install NirCmd

Download the 64-bit NirCmd package, extract `nircmd.exe`, and place it in a
folder named `nircmd-x64` in the repository folder.

For example, if this repository is located at:

```text
C:\Users\YourName\Documents\Test
```

place NirCmd here:

```text
C:\Users\YourName\Documents\Test\nircmd-x64\nircmd.exe
```

The program also checks the parent folder for compatibility with older
installations. Make sure the file is named exactly `nircmd.exe`.

## Install the Python packages

Open PowerShell and change to the repository directory:

```powershell
cd C:\Users\YourName\Documents\Test
```

Install the dependencies:

```powershell
python -m pip install -r src\requirements.txt
```

If `python` is not recognized, install Python from
[python.org](https://www.python.org/downloads/) and enable **Add Python to
PATH** during installation.

## Run the program

From the repository directory, run:

```powershell
python src\src\main.py
```

The program will display:

```text
Press F11 to toggle resolution between 1024x706 and 1920x1080.
```

Press `F11` to change the resolution. Press `Ctrl+C` in PowerShell to stop the
program.

## Troubleshooting

### `NirCmd was not found`

Verify that NirCmd exists at:

```text
nircmd-x64\nircmd.exe
```

relative to the repository directory.

### Permission or hotkey errors

The `keyboard` package may require an elevated PowerShell window. If the hotkey
does not work, close the program, open PowerShell as Administrator, and run it
again.

### Resolution change fails

Confirm that the requested resolutions are supported by the display. The
program changes the color depth to 32-bit and requests stretched scaling for
the `1024x706` mode. If black bars remain, open your graphics driver control
panel and set the display scaling mode to **Full-screen** or **Stretch**.

## Start the program automatically with Windows

Use the Windows Startup folder to launch the program when you sign in.

1. Make sure the program runs manually before configuring startup.
2. Press `Win+R`, enter `shell:startup`, and press **Enter**.
3. In the Startup folder, right-click an empty area and select **New >
   Shortcut**.
4. For the shortcut location, enter the full path to your Python executable
   followed by the script path. For example:

   ```text
   "C:\Users\YourName\AppData\Local\Programs\Python\Python314\python.exe" "C:\Users\YourName\Documents\Test\src\src\main.py"
   ```

5. Select **Next**, name the shortcut `Python Display Settings`, and select
   **Finish**.
6. Right-click the new shortcut, select **Properties**, and set **Start in**
   to the repository directory:

   ```text
   C:\Users\YourName\Documents\Test
   ```

7. Select **Apply** and **OK**.
8. Sign out and sign in again, or restart Windows, to test the shortcut.

Replace `YourName` and the Python path with the paths on your computer. To
disable startup later, press `Win+R`, enter `shell:startup`, and delete or
move the `Python Display Settings` shortcut.
