# tg-ws-proxy-termux

Telegram Proxy for Termux.

Fork of [tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) adapted for Termux on Android.

---

## Installation

```bash
pkg update && pkg upgrade
pkg install python3 git
git clone https://github.com/Nuwert123/tg-ws-proxy-termux.git
cd tg-ws-proxy-termux/install
python3 controller.py
```
## Usage
To start (if it doesn't work, just re-enter Termux):

```
proxy
```
Copy this line (it's a secret for the proxy).
<img width="1019" height="439" alt="изображение" src="https://github.com/user-attachments/assets/8a494c1e-b195-497d-a31a-92a08738fef3" /> 



Paste this string into the "secret" field and apply the settings shown in the screenshot.
<img width="1080" height="1054" alt="изображение" src="https://github.com/user-attachments/assets/f9ef5802-b666-4297-8e19-12c7f870a5e7" />


---

## Dependencies

- Python >= 3.8
- pyperclip == 1.9.0
- art == 6.5
- psutil == 7.0.0
- cryptography == 46.0.5

---

## Project Structure

```
tg-ws-proxy-termux/
├── install/          # Installation script
├── packaging/        # Additional packages
├── proxy/            # Main proxy code
├── utils/            # Utilities
├── pyproject.toml    # Project configuration
└── README.md         # Documentation
```

---

## License 
MIT


Copyright 2026 Nuwert123

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


---

## Links

- Original project: [tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy)
- Issues: https://github.com/Nuwert123/tg-ws-proxy-termux/issues
- Termux: [Installation Guide](https://github.com/termux/termux-app)
