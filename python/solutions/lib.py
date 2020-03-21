import json

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTreeCodec:

    def deserialize(self, data):
        values = json.loads(data) if isinstance(data, str) else data
        if not values:
            return None

        root = TreeNode(values[0])

        self._fillTree([root], values[1:])

        return root

    def _fillTree(self, nodes: list, values: list):
        if not values:
            return []

        leafs = []
        count = min(len(nodes) * 2, len(values))

        for i in range(count):
            node = None if values[i] is None else TreeNode(values[i])
            parent = nodes[i // 2]
            if i % 2 == 0:
                parent.left = node
            else:
                parent.right = node
            if node is not None:
                leafs.append(node)

        self._fillTree(leafs, values[count:])

if __name__ == '__main__':
    root = BinaryTreeCodec().deserialize("[5,3,6,2,4,null,7]")
