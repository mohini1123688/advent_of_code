# Parse the file properly

def load_reports(path):
    with open(path) as f:
        return f.read()

reports = load_reports("advent_of_code/input_files/example3_input.txt")
print(reports)