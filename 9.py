
class Node():
    def __init__(self, sequence, parent=None):
        self.seq = sequence
        self.parent = parent
        self.next = self.get_next()
        
    def get_next(self):
        next_seq = []
        seq = self.seq
        for i in range(len(seq)-1):
            next_seq.append(seq[i+1]-seq[i])
        if all(element == 0 for element in next_seq):
            return None
        else:
            return Node(next_seq, self)

def find_next_value(node):
    while node.next:
        node = node.next
    next_val = 0
    while node:
        next_val += node.seq[-1]
        node = node.parent
    return next_val

def find_pre_value(node):
    while node.next:
        node = node.next
    pre_val = 0
    while node:
        pre_val = node.seq[0]-pre_val
        node = node.parent
    return pre_val

def main():
    with open("inputs/9.txt", "r") as file:
        lines = file.readlines()
    ini_seqs = [[int(l) for l in line.strip("\n").split()] for line in lines]
    
    # Part 1
    next_vals = []
    for item in ini_seqs:
        node = Node(item)
        next_vals.append(find_next_value(node))
    print(f"Answer 1: {sum(next_vals)}")
    
    # Part 2
    pre_vals = []
    for item in ini_seqs:
        node = Node(item)
        pre_vals.append(find_pre_value(node))
    print(f"Answer 2: {sum(pre_vals)}")

if __name__ == "__main__":
    main()