class TrieNode:
    def __init__(self):
        self.cut=False
        self.children=collections.defaultdict(TrieNode)

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()
        for path in sorted(paths):
            curnode = root
            for c in path:
                if c not in curnode.children:
                    curnode.children[c] = TrieNode()
                curnode = curnode.children[c]
        subtreeToNodes = collections.defaultdict(list)
        def serial(root):
            subtree = '(' + ''.join(s + serial(root.children[s]) for s in root.children) + ')'
            if subtree != '()':
                subtreeToNodes[subtree].append(root)
            return subtree
        serial(root)
        curpath = []
        res = []
        for nodes in subtreeToNodes.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.cut = True
        def dfs(root, curpath):
            if root.cut:
                return
            if curpath:
                res.append(curpath)
            for child in root.children:
                dfs(root.children[child], curpath + [child])
        dfs(root, curpath)
        return res
