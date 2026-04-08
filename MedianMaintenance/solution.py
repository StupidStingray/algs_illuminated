
class Heap:
    def __init__(self, type):
        self.items = []
        self.type = type
        self.hashTable = dict()
        self.size = 0
        assert self.type in ["low","high"], f"heap type must be either high or low but not {self.type}"

    def compare(self, item1, item2) -> bool:
        if self.type == "low":
            return item1>item2
        else:
            return item1<item2

    def insert_item(self, item):
        self.items.append(item)
        heap_i = len(self.items)
        while self.compare(self.items[heap_i-1],self.items[heap_i//2-1]) & (heap_i>1):
            self.items[heap_i-1],self.items[heap_i//2-1] = self.items[heap_i//2-1],self.items[heap_i-1]
            heap_i = heap_i//2
        self.size = len(self.items)
    def retrieveMin(self):
        self.items[0],self.items[-1] = self.items[-1],self.items[0]
        min_item = self.items.pop()
        heap_i = 1
        while True:
            if heap_i*2+1 <= len(self.items):
                if self.compare(self.items[heap_i*2-1],self.items[heap_i*2]):
                    targetChild = heap_i*2
                else:
                    targetChild = heap_i*2+1
            elif heap_i*2 <= len(self.items):
                targetChild = heap_i*2
            else:
                break
            if not(self.compare(self.items[heap_i-1], self.items[targetChild-1])):
                self.items[heap_i-1],self.items[targetChild-1] = self.items[targetChild-1],self.items[heap_i-1]
                heap_i = targetChild
            else:
                break
        self.size = len(self.items)
        return min_item
    def __repr__(self):
        output_string = ""
        for i in range(min(20, len(self.items))):
            output_string += str(self.items[i])+"   "
            if i in {0, 2, 6, 12}:
                output_string += "\n"
        return output_string
with open('problem11.3test.txt', 'r') as file:
    input_numbers = [int(_.strip()) for _ in file.readlines()]

print(input_numbers)
kth_medians_last_digits = []
heap_min = Heap("high")
heap_max = Heap("low")
current_median = input_numbers[0]
heap_max.insert_item(input_numbers[0])
kth_medians_sum = current_median
kth_medians_last_digits.append(str(kth_medians_sum)[-4:])
print(f"first element and the initial median equals {current_median}")
for i in range(1,len(input_numbers)):
    current_item = input_numbers[i]
    # print(f"inserting item {current_item}")
    if current_item > current_median:
        # print(f"inserting the item to heap high because {current_item} is greater than {current_median}")
        heap_min.insert_item(current_item)
    else:
        # print(f"inserting the item to heap low because {current_item} is lower than {current_median}")
        heap_max.insert_item(current_item)
    if heap_max.size > heap_min.size +1:
        heap_min.insert_item(heap_max.retrieveMin())

    # print(f"heap high (of size {heap_min.size}):")
    # print(heap_min)
    # print(f"heap low (of size {heap_max.size}):")
    # print(heap_max)
    # print("retrieving current median")
    if heap_min.size > heap_max.size:
        current_median = heap_min.retrieveMin()
    else:
        current_median = heap_max.retrieveMin()
    # print(f"current median equals {current_median}")
    heap_max.insert_item(current_median)
    kth_medians_sum += current_median
    kth_medians_last_digits.append(str(kth_medians_sum)[-4:])
    # print("heap high:")
    # print(heap_min)
    # print("heap low:")
    # print(heap_max)
print(f"last four digits of the sum of kth medians equals {kth_medians_last_digits[-1]}")


    
