# python-display-settings/python-display-settings/README.md

# Python Display Settings

This project allows you to quickly change your display settings using a keybind. It is built in Python and utilizes the OS module along with libraries for handling keypress events.

## Requirements

Before running the project, ensure you have the following dependencies installed:

- [keyboard](https://pypi.org/project/keyboard/): For handling keypress events.
- [pygetwindow](https://pypi.org/project/pygetwindow/): For managing display settings.

You can install the required libraries by running:

```
pip install -r requirements.txt
```

## Usage

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the main script:

```
python src/main.py
```

4. Press the designated keybind to change the display settings.

## Keybind Configuration

You can customize the keybind in the `main.py` file. Look for the section where keypress events are handled and modify it according to your preference.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.