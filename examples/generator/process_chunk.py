

# Sample list with 100 elements
NUMBERS = list(range(1, 100))

# Process list elements from 10 in 10 chunks
CHUNK = 10


def generate_fifty_numbers():
    start = 0
    while start < len(NUMBERS):
        end = start + CHUNK
        current_chunk_numbers = NUMBERS[start:end]
        start += CHUNK

        yield current_chunk_numbers


if __name__ == '__main__':
    for chunck_number, chunk in enumerate(generate_fifty_numbers()):
        print("Chunk {} has {} elements".format(chunck_number, len(chunk)))
        print("Elements: {}".format(chunk))
        print("-" * 10)
