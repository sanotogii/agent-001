from functions.write_file import write_file


def main():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for writing 'lorem.txt':")
    print(result)
    print()

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for writing 'pkg/morelorem.txt':")
    print(result)
    print()

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for writing '/tmp/temp.txt':")
    print(result)
    print()


if __name__ == "__main__":
    main()