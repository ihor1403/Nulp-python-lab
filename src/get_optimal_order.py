from collections import defaultdict, deque

def read_input(filename):
    dependencies = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            doc, required_doc = line.strip().split()
            dependencies[required_doc].append(doc)
    return dependencies

def get_optimal_order(dependencies):
    in_degree = {doc: 0 for doc in dependencies}
    for docs in dependencies.values():
        for doc in docs:
            in_degree[doc] += 1

    queue = deque([doc for doc, count in in_degree.items() if count == 0])
    order = []

    while queue:
        current_doc = queue.popleft()
        order.append(current_doc)

        for required_doc in dependencies[current_doc]:
            in_degree[required_doc] -= 1
            if in_degree[required_doc] == 0:
                queue.append(required_doc)

    if len(order) != len(dependencies):
        raise Exception("Graph has a cycle")

    return order

def write_output(filename, order):
    with open(filename, 'w') as f:
        for doc in order:
            f.write(doc + '\n')

if __name__ == '__main__':
    dependencies = read_input('govern.in')
    order = get_optimal_order(dependencies)
    write_output('govern.out', order)
