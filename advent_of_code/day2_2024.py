def load_reports(path):
    with open(path) as f:
        return [[int(x) for x in line.split()] for line in f]

reports = load_reports("advent_of_code/input_files/day_2_input.txt")

def find_safe_reports(row):
    pointer1 = 0
    pointer2 = 1
    if row[pointer2] < row[pointer1]:
        row = row[::-1]
    while 4 > (row[pointer2] - row[pointer1]) > 0:
        pointer1 += 1
        pointer2 += 1
        if pointer2 == len(row):
            return True

def problem_dampener(reports):
    safe = 0
    for row in reports:
        for i in range(len(row)):
            new_level = row[:i] + row[i+1:]
            if find_safe_reports(new_level):
                safe +=1
                break

    return(safe)

def main(reports):
    print(problem_dampener(reports))
    

if __name__ == '__main__':
    main(reports)