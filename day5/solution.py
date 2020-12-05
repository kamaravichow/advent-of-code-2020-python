def readFile() -> list:
    with open(f"{__file__.rstrip('solution.py')}input.txt", "r") as f:
        return [int(line[:-1].replace("F", "0").replace("B", "1")
            .replace("L", "0").replace("R", "1"), 2) for line in f.readlines()]

def part1(seat_ids: list) -> int:
    return max(seat_ids)

def part2(seat_ids: list) -> int:
    for i in range(min(seat_ids), max(seat_ids)):
        if i not in seat_ids and (i - 1) in seat_ids and (i + 1) in seat_ids:
            return i

if __name__ == "__main__":
    seat_ids = readFile()
    print(f"Part 1: {part1(seat_ids)}")
    print(f"Part 2: {part2(seat_ids)}")

f={int(bytes(c>>2&1^49 for c in t),2)>>1 for t in open("input.txt","rb")}
print(*{*range(min(f),max(f))}-f)