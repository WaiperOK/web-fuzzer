import unittest

from web_fuzzer.core import fuzz, generate_random_string


class DummyResponse:
    def __init__(self, status_code: int) -> None:
        self.status_code = status_code


class TestCore(unittest.TestCase):
    def test_random_string_length(self) -> None:
        value = generate_random_string(32)
        self.assertEqual(len(value), 32)

    def test_fuzz_uses_requester(self) -> None:
        calls = []

        def fake_requester(url, data, timeout):  # noqa: ANN001
            calls.append((url, data, timeout))
            return DummyResponse(200)

        out = fuzz(
            "https://example.org",
            num_requests=3,
            param_name="q",
            payload_length=8,
            requester=fake_requester,
        )
        self.assertEqual(len(out), 3)
        self.assertEqual(len(calls), 3)
        self.assertTrue(all(item.status_code == 200 for item in out))


if __name__ == "__main__":
    unittest.main()
