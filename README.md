# web-fuzzer

Controlled HTTP form fuzzing utility for security testing in authorized environments.

## What changed in v0.2.0

- moved from single script to package structure
- added CLI arguments for request count, payload length, timeout, and output mode
- added deterministic unit tests
- added GitHub Actions CI

## Usage

```bash
python -m pip install -e .
web-fuzzer --url https://example.org/form --requests 10 --param username --json
```

## Safety note

Use only on systems you own or where you have explicit permission.
