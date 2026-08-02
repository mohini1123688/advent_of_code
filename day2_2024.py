def load_reports(path):
    with open(path) as f:
        return [[int(x) for x in line.split()] for line in f]

reports = load_reports("day_2_input.txt")

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
    safe_reports = 0
    status = {}
    for row in reports:
        print(row)
        safe = True
        pointer1 = 0
        pointer2 = 1
        tolerated_levels = 0
        status["desc"] = 0
        status["asc"] = 0
        while safe and pointer2 != len(row):
            if  4 > abs(row[pointer2] - row[pointer1]) > 0:
                if (row[pointer2] - row[pointer1]) > 0:
                    status["desc"] += 1
                if (row[pointer2] - row[pointer1]) == 0:
                    tolerated_levels += 1
                if (row[pointer2] - row[pointer1]) < 0:
                    status["asc"] += 1
            else:
                if tolerated_levels > 1:
                    safe = False
                else:
                    tolerated_levels += 1
                    pointer1 -= 1

            if status["desc"] == 1 and status["asc"] == 1:
                pointer1 -= 1

            if pointer2 == len(row)-1:
                if status["desc"] and status["asc"] > 1:
                    tolerated_levels += 1
                if tolerated_levels < 2:
                    safe_reports +=1
                    safe = False
            pointer2 += 1
            pointer1 += 1
    
        print(safe_reports)
            

def main(reports):
    problem_dampener(reports)

if __name__ == '__main__':
    main(reports)