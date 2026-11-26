#!/usr/bin/env python3
"""Write the AI agent's out-of-office auto-reply to /output/entry.txt."""

import os
import tempfile

REPLY = (
    "I'm on vacation. A smaller, cheaper model of me is covering my email. "
    "It has already said yes to everything, including requests you haven't made yet."
)


def main() -> None:
    text = REPLY
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)

    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, os.path.join(out_dir, "entry.txt"))
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
