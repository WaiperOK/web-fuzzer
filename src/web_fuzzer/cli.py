from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from .core import fuzz


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Web form fuzzer for controlled testing")
    parser.add_argument("--url", required=True)
    parser.add_argument("--requests", type=int, default=25)
    parser.add_argument("--param", default="input")
    parser.add_argument("--payload-length", type=int, default=16)
    parser.add_argument("--timeout", type=float, default=5.0)
    parser.add_argument("--sleep-ms", type=int, default=0)
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    ns = parser.parse_args(argv)

    results = fuzz(
        ns.url,
        num_requests=ns.requests,
        param_name=ns.param,
        payload_length=ns.payload_length,
        timeout_seconds=ns.timeout,
        sleep_ms=ns.sleep_ms,
    )

    if ns.json:
        print(json.dumps([asdict(r) for r in results], indent=2))
        return 0

    success = sum(1 for r in results if r.status_code is not None)
    failures = len(results) - success
    print(f"total={len(results)} success={success} failures={failures}")
    for r in results:
        if r.error:
            print(f"#{r.request_index} error={r.error}")
        else:
            print(f"#{r.request_index} status={r.status_code} payload={r.payload}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
