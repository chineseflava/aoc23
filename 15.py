
class Lens():
    def __init__(self, seq):
        self.label = seq[:-2]
        self.fl = seq[-2:]
        self.hash = HASH_algo(self.label)

def HASH_algo(item):
    val = 0
    for l in item:
        #translate to ASCII
        val += ord(l)
        val = val*17
        val = val%256
    return val

def HASHMAP_algo(item, boxes):
    if item[-1] == "-":
        for box in boxes:
            for i, lens in enumerate(box):
                if lens.label == item[:-1]:
                    box.remove(lens)
                    break
    elif item[-2] == "=":
        new_lens = Lens(item)
        replaced = False
        for i, lens in enumerate(boxes[new_lens.hash]):
            if lens.label == new_lens.label:
                boxes[new_lens.hash][i] = new_lens
                replace = True
        if not replace:
            boxes[new_lens.hash]
            

        # if boxes[lens.hash].contains
        # boxes[lens.hash].append(lens)
    



def main():
    with open("inputs/15_test.txt", "r") as file:
        lines = file.readlines()
    sequence = lines[0].split(",")
    values = []
    for item in sequence:
        val = HASH_algo(item)
        values.append(val)
    print(values)
    print(sum(values))

    # Part 2
    boxes = []*9
    for item in sequence:
        HASHMAP_algo(item, boxes)
        
if __name__ == "__main__":
    main()
