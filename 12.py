import numpy as np

class Record():
    def __init__(self, line):
        self.condition = line[0]
        self.criteria = [int(item) for item in line[1].split(",")]
        #print(self.criteria)

def get_combinations(cond):
    idx = cond.find("?")

    if idx == -1:
        combination = []
        count = 0
        for idx, i in enumerate(cond):
            if i == "#":
                count += 1
            if i == ".":
                if count != 0:
                    combination.append(count)
                count = 0
            if idx == len(cond)-1 and count != 0:
                combination.append(count)
                
        return [combination]
    
    option1 = cond[:idx] + "#" + cond[idx +1:]
    option2 = cond[:idx] + "." + cond[idx +1:]

    combinations1 = get_combinations(option1)
    combinations2 = get_combinations(option2)

    return combinations1 + combinations2    

def find_arr(rec):
    combs = get_combinations(rec.condition)
    arr = 0
    for comb in combs:
        if comb == rec.criteria:
            arr += 1
    return arr

def main():
    with open("inputs/12.txt", "r") as file:
        lines = file.readlines()
    
    records = [Record(line.strip("\n").split()) for line in lines]
    arrs = []
    for record in records:
        arrs.append(find_arr(record))
    print(arrs)
    print(sum(arrs))

    #universe = np.array([[e for e in line.strip("\n")] for line in lines])

if __name__ == "__main__":
    main()