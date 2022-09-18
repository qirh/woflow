from collections import defaultdict
import requests
import json

def make_api_call(node_ids):
    url = 'https://nodes-on-nodes-challenge.herokuapp.com/nodes/' + ','.join(node_ids)
    response = json.loads(requests.get(url).content)
    return response

def parse_nodes(node_ids):
    data = make_api_call(node_ids)

    for node in data:
        child_node_ids = node['child_node_ids']
        if child_node_ids:
            for child in child_node_ids:
                node_counts[child] += 1
            parse_nodes(child_node_ids)

def get_most_frequent_node():
    most_frequent_node = None
    most_frequent_node_count = 0
    for node, count in node_counts.items():
        if count > most_frequent_node_count:
            most_frequent_node = node
            most_frequent_node_count = count
    return most_frequent_node

node_counts = defaultdict(int)
node_counts['089ef556-dfff-4ff2-9733-654645be56fe'] = 1
parse_nodes(['089ef556-dfff-4ff2-9733-654645be56fe'])
print(f'1. Unique ids: {len(node_counts)}')
most_frequent_node = get_most_frequent_node()
print(f'2. Most frequent node: {most_frequent_node}, with count: {node_counts[most_frequent_node]}')
