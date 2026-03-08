# Phantom Trace

A desktop security scanner that detects traces hackers leave behind on Windows and Linux systems. It combines rule-based checks with lightweight AI models to catch both obvious and subtle intrusion indicators.

## What it does

- Scans running processes, network connections, startup entries, SSH configs, and the filesystem
- Flags suspicious activity by severity — High, Medium, and Low
- Uses a lightweight anomaly model to score overall threat level
- Gives you a live feed of findings as the scan runs

## Requirements

- Python 3.10+
- CustomTkinter
- psutil

Install dependencies:
```bash
pip install -r requirements.txt
```

## Running it
```bash
python main.py
```

## Project status

Early development. Rule coverage and the AI model are still being built out. Contributions and suggestions are welcome.
