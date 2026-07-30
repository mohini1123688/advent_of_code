import pandas as pd

df = pd.read_csv("input.txt", sep=r"\s+", header = None)
list1, list2 = df[0].tolist(), df[1].tolist()
sorted1 = sorted(list1)
sorted2 = sorted(list2)

def calculate_distance(sorted1, sorted2):
    distance = 0
    for i in range(len(sorted1)):
        distance = distance + abs(sorted1[i] - sorted2[i])

    # print(distance)

def calculate_similarity_score(sorted1, sorted2):
    unique_list1 = {}
    similarity_score = 0
    for index_i, number in enumerate(sorted1):
        for index_j, other_number in enumerate(sorted2):
            #print(f"sorted1 number: {number}")
            #print(f"sorted2 number: {other_number}")
            if number == other_number:
                if number not in unique_list1:
                    unique_list1[number] = 1
                else:
                    unique_list1[number] = unique_list1[number] + 1
    for number in unique_list1:
        similarity_score = similarity_score + number*unique_list1[number]

    print(similarity_score)

def main ():
    calculate_distance(sorted1, sorted2)
    calculate_similarity_score(sorted1, sorted2)

if __name__ == "__main__":
    main()

# PART 2


