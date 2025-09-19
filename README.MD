# redSAK

*redSAK (red Swiss Army Knife)* is an offensive cybersecurity multitool designed for enumeration and automated exploitation.

> ⚠️ **Disclaimer**  
> This tool is for **educational and ethical use only**. Do not attempt to use it against any system, service, or data you do not own or have explicit permission to test. The author is not responsible for any misuse.

---

## Features

- Lightweight, modular framework for offensive security tasks
- Easy-to-extend structure for adding new modules
- JSON-based reporting for all modules

---

## Currently Supported Modules

| Module | Description |
|--------|-------------|
| LFI    | Local File Inclusion detection and reporting for Windows and Linux targets |

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/redSAK.git
cd redSAK
```

2. Run redSAK

```bash
python3 main.py
```

3. Follow prompts

4. Results stored in JSON file