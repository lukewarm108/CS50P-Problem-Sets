import sys
import csv


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Only CSV files are supported")
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    students = []
    try:
        with open(arg1) as infile:
            reader = csv.DictReader(infile)
            for x in reader:
                last, first = x["name"].split(", ")
                students.append({
                    "first": first,
                    "last": last,
                    "house": x["house"]
                })
    except FileNotFoundError:
        sys.exit("File not found")
    with open(arg2, "w", newline="") as outfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)


if __name__ == "__main__":
    main()