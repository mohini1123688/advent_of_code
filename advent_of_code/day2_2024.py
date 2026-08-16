def load_reports(path):
    with open(path) as f:
        return [[int(x) for x in line.split()] for line in f]

reports = load_reports("example2_input.txt")

def find_safe_reports(reports):
    safe = 0
    for row in reports:
        pointer1 = 0
        pointer2 = 1
        if row[pointer2] < row[pointer1]:
            print(row)
            row = row[::-1]
        while 4 > (row[pointer2] - row[pointer1]) > 0:
            pointer1 += 1
            pointer2 += 1
            if pointer2 == len(row):
                safe +=1
                break
        print(safe)

def problem_dampener(reports):
    safe = 0
    for row in reports:
            

def main(reports):
    problem_dampener(reports)

if __name__ == '__main__':
    main(reports)