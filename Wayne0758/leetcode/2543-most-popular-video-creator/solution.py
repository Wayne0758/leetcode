class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        totalviews = defaultdict(int)
        videoviews = defaultdict(list)
        n = len(creators)
        mxview = 0
        for i in range(n):
            totalviews[creators[i]]+=views[i]
            if totalviews[creators[i]]>mxview:
                mxview = totalviews[creators[i]]
            videoviews[creators[i]].append((ids[i],views[i]))
        res = []
        for creator in totalviews.keys():
            if totalviews[creator]==mxview:
                video = videoviews[creator]
                video = sorted(video)
                video = sorted(video, key = lambda x:x[1],reverse = True)
                res.append([creator,video[0][0]])
        return res
