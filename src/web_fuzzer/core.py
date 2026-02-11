from __future__ import annotations

import random
import string
import time
from dataclasses import dataclass
from typing import Callable

import requests


@dataclass(frozen=True)
class FuzzResult:
    request_index: int
    payload: str
    status_code: int | None
    error: str | None = None


def generate_random_string(length: int = 16) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(alphabet) for _ in range(length))


def fuzz(
    url: str,
    *,
    num_requests: int = 100,
    param_name: str = "input",
    payload_length: int = 16,
    timeout_seconds: float = 5.0,
    sleep_ms: int = 0,
    requester: Callable[..., requests.Response] = requests.post,
) -> list[FuzzResult]:
    out: list[FuzzResult] = []
    for i in range(1, num_requests + 1):
        payload = generate_random_string(payload_length)
        try:
            resp = requester(url, data={param_name: payload}, timeout=timeout_seconds)
            out.append(FuzzResult(request_index=i, payload=payload, status_code=resp.status_code))
        except Exception as exc:  # noqa: BLE001
            out.append(FuzzResult(request_index=i, payload=payload, status_code=None, error=str(exc)))
        if sleep_ms > 0:
            time.sleep(sleep_ms / 1000.0)
    return out
