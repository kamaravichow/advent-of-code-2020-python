def readFile() -> list:
    with open(f"{__file__.rstrip('solution.py')}input.txt", "r") as f:
        return [int(line[:-1].replace("F", "0").replace("B", "1")
            .replace("L", "0").replace("R", "1"), 2) for line in f.readlines()]

def part1(seat_ids: list) -> int:
    return max(seat_ids)

if __name__ == "__main__":
    seat_ids = readFile()
    print(f"Part 1: {part1(seat_ids)}")