from collections import deque

class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

class Codec:
    def serialize(self, root):
        if root is None:
            return ""

        result = []
        self._serializeHelper(root, result)
        return ''.join(result)

    def _serializeHelper(self, root, result):
        q = deque()
        endNode = Node()
        childNode = Node()
        q.append(root)
        q.append(endNode)

        while q:
            node = q.popleft()
            if node == endNode:
                result.append('None')
                if q:
                    q.append(endNode)
            elif node == childNode:
                result.append('$')
            else:
                result.append(chr(node.val + ord('0')))
                q.extend(node.children)
                if q[0] != endNode:
                    q.append(childNode)

    def deserialize(self, data):
        if not data:
            return None

        rootNode = Node(int(data[0]), [])
        self._deserializeHelper(data, rootNode)
        return rootNode

    def _deserializeHelper(self, data, rootNode):
        currentLevel = deque()
        prevLevel = deque()
        currentLevel.append(rootNode)
        parentNode = rootNode
        data = data.split()
        for i in range(1, len(data)):
            d = data[i]
            if d == 'None':
                prevLevel = currentLevel
                currentLevel = deque()
                if prevLevel:    
                    parentNode = prevLevel.popleft()
            elif d == '$':
                parentNode = prevLevel.popleft()
            else:
                childNode = Node(int(d), [])
                currentLevel.append(childNode)
                parentNode.children.append(childNode)
    
    @staticmethod
    def preorder(root:Node):
        if root:
            if root.children:
                for i in root.children:
                    Codec.preorder(i)
        print(root.val)

# Example usage:
codec = Codec()
root = codec.deserialize("1 None 2 3 None 4 5 None None 6 None 7 None None")
serialized_data = codec.serialize(root)
codec.preorder(serialized_data)
print(serialized_data)

