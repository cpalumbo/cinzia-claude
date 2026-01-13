# Python Automation Skill

## When to Use
Use this skill when creating Python scripts for automations, data processing, API calls, or utility tasks.

## Golden Rules

1. **Virtual environment always** — never install globally
2. **Secrets in `.env`** — never hardcode API keys
3. **Logger not print** — easier to debug later
4. **Fail loud** — if something breaks, make it obvious

## Quick Start Template

```python
#!/usr/bin/env python3
"""What this script does in one line."""

import logging
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Config
API_KEY = os.environ["API_KEY"]
OUTPUT_DIR = Path("output")

# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
log = logging.getLogger(__name__)


def main():
    log.info("Starting")
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Your code here
    
    log.info("Done")


if __name__ == "__main__":
    main()
```

## Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install python-dotenv requests
pip3 freeze > requirements.txt
```

Add to `.gitignore`:
```
venv/
.env
__pycache__/
```

## Secrets

Create `.env`:
```
API_KEY=your-key-here
```

Create `.env.example` (commit this):
```
API_KEY=
```

Load in script:
```python
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ["API_KEY"]
```

## Logging

```python
log.info(f"Processing {len(items)} items")
log.warning(f"Skipping bad record: {record}")
log.error(f"Failed: {e}")
```

## Error Handling

Keep it simple — catch what you expect, let the rest crash loudly:

```python
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.RequestException as e:
    log.error(f"Request failed: {e}")
    raise
```

## Files

Use pathlib:
```python
from pathlib import Path

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

file_path = output_dir / "results.csv"
file_path.write_text(content, encoding="utf-8")
```

## HTTP Requests

```python
import requests

response = requests.get(url, timeout=30)
response.raise_for_status()
data = response.json()
```

## CSV Output

```python
import csv

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "url", "price"])
    writer.writeheader()
    writer.writerows(data)
```

## Before You're Done

- [ ] Runs without errors
- [ ] No hardcoded secrets
- [ ] requirements.txt exists
- [ ] .env.example documents needed vars
- [ ] You'll understand it in 3 months
