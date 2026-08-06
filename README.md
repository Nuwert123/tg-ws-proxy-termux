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

---

## Run

```bash
proxy
```

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
├── LICENSE           # MIT License
├── pyproject.toml    # Project configuration
└── README.md         # Documentation
```

---

## License

[MIT](https://github.com/Nuwert123/tg-ws-proxy-termux/blob/main/LICENSE)

---

## Links

- Original project: [tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy)
- Issues: https://github.com/Nuwert123/tg-ws-proxy-termux/issues
- Termux: [Installation Guide](https://github.com/termux/termux-app)