from collections import deque

def push(queue, value): # thêm vào cuối
    queue.append(value)

def push_head(queue: list, value):
    queue.insert(0, value)
def is_empty(queue):
    return len(queue) == 0

def pop(queue): # xóa đầu
    if is_empty(queue):
        return None
    return queue.pop(0)

def pop_tail(queue): # xóa cuoois
    if is_empty(queue):
        return None
    return queue.pop()

def front(queue):
    if is_empty(queue):
        return None
    return queue[0]

def back(queue):
    if is_empty(queue):
        return None
    return queue[len(queue)-1]

def size(queue):
    return len(queue)

def print_queue(queue):
    for i in queue:
        print(i, end = " ")
    print()

def sapxep(queue):
    result = []
    for i in queue:
        if is_empty(result) or i >= back(result):
            push(result,i)
        else:
            other = []
            while is_empty(result) is False and i < back(result):
                push(other, pop_tail(result))
            push(result,i)
            while is_empty(other) is False:
                push(result,pop_tail(other))
    return result

n = [int(x) for x in input().split()]
queue = sapxep(n)
print(queue)