from lab7_s3 import build_tabl, matcher


def read_input(filename="combinations_5chars_100k_single_line.txt"):
    with open(filename, 'r') as f:
        H_stack = f.read().strip()
    return H_stack


if __name__ == "__main__":
    needle = input("needle: ").strip()

    H_stack = read_input()

    indexes = matcher(H_stack, needle)

    print("Found at positions:", indexes)
