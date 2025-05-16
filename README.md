# sqlite-to-hashcat-gitea
Extracts and formats Gitea user password hashes from SQLite for cracking

# Gitea Hash Exporter

Extracts and formats Gitea PBKDF2 password hashes from the SQLite database.

## Requirements

- Python 3
- Access to the `gitea.db` SQLite database (typically found in Gitea's data directory)
- The database must be accessible and readable from the system running the script

## Usage

1. Place the `gitea.db` file in the same directory as the script (or modify the path in the code).
2. Run the script:

```bash
python3 create_reel_hash.py
```

The script will output password hashes in the format:

```
sha256:<iterations>:<base64_salt>:<base64_hash>
```

## Note

If the script doesn’t work, the SQLite database filename or path might be incorrect.  
You can change it directly in the code here:

```python
con = sqlite3.connect("gitea.db")  # <-- modify the file path or name if needed
```

