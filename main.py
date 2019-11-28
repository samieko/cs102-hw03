import sys
import csv


def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

    from statistics import mean
    # TODO: Fill in the actual logic here!
    with open(input_file_path, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            l1 = []
            for numbers in row:
                l1.append(float(numbers))
            average = mean(l1)
            print(average)


if __name__ == "__main__":
    main()
