# Lucky Draw System

DISCLAIMER: This is a very simple program done within a short amount of time. Purpose is to be used in a lucky draw event. The program is not fully tested and should be used at your own risk.

## Steps to Setup
1. Clone the repository.
2. Configure using `config.ini`, can configure lucky draw number range, and the randomizing effect time.
3. Run `python src/main.py`.

## Steps to Build and Deploy
1. Run `pip install pyinstaller`.
2. Download latest release pywin32 [here], choose your installed python version (3.X 32/64bit).
3. Follow [Steps to Setup] above.
4. Change directory to `src`.
6. Run code `pyinstaller --noconsole --onefile main.py`.
7. The exe file is created in `dist` folder.
8. Copy the `config.ini` file into the `dist` folder.
9. Always make sure the config file is beside the exe file.

[here]: https://github.com/mhammond/pywin32/releases
