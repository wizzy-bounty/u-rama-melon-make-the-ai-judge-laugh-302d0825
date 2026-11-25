import os


ENTRY = "Our office plant died during the wellness webinar on resilience."


def write_entry(output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as output_file:
        output_file.write(ENTRY)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    write_entry(output_dir)


if __name__ == "__main__":
    main()
