class Heap:
    def __init__(self):
        self.heap_list = []
        self.size = 0

    def heap_push(self, ele):
        self.heap_list.append(ele)
        self.size += 1
        self.heapify()

    def heap_pop(self):
        if self.size <= 0:
            raise IndexError
        
        # retrieve the element to return
        ele = self.heap_list[0]

        # replace the top element (Min or Max) with the last one in heap
        self.heap_list[0] = self.heap_list[self.size - 1]

        # remove the last element from heap
        self.size -= 1
        self.heap_list.pop()

        # percolate down the top element in order to satisfy heap property
        self.percolate_down(0)

        return ele

    def heapify(self):
        pass

    def percolate_down(self, idx):
        max_idx = idx
        l_child_idx = 2 * self.size + 1
        r_child_idx = 2 * self.size + 2

        if l_child_idx < len(self.heap_list) and self.heap_list[max_idx] < self.heap_list[l_child_idx]:
            max_idx = l_child_idx

        if r_child_idx < len(self.heap_list) and self.heap_list[max_idx] < self.heap_list[r_child_idx]:
            max_idx = r_child_idx

        if max_idx != idx:
            temp = self.heap_list[idx]
            self.heap_list[idx] = self.heap_list[max_idx]
            self.heap_list[max_idx] = temp

            self.percolate_down(0)





        