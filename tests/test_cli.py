import subprocess
import sys
import unittest


def run_cli(*args: str) -> str:
    result = subprocess.run(
        [sys.executable, "-m", "badge_cli", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


class TestBadgeCli(unittest.TestCase):
    def test_greet(self) -> None:
        self.assertEqual(run_cli("greet", "Riaza"), "Hello, Riaza!")

    def test_wordcount(self) -> None:
        self.assertEqual(run_cli("wordcount", "--text", "Hello world"), "2")

    def test_slugify(self) -> None:
        self.assertEqual(
            run_cli("slugify", "--text", "Hello, GitHub!"),
            "hello-github",
        )

    def test_hash(self) -> None:
        output = run_cli("hash", "--text", "demo")
        self.assertEqual(len(output), 64)
