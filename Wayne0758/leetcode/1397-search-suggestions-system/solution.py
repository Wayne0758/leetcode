class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        hashmap = defaultdict(list)
        for product in products:
            for i in range(1,1+len(product)):
                if len(hashmap[product[:i]])<3:
                    hashmap[product[:i]].append(product)
        res = []
        for i in range(1,1+len(searchWord)):
            res.append(hashmap[searchWord[:i]])
        return res
