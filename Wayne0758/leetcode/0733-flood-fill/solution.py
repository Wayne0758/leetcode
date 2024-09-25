class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        queue = [[sr,sc]]
        original_color = image[sr][sc]
        image[sr][sc] = color
        d = [0,1,0,-1,0]
        if original_color==color:
            return image
        while queue:
            i,j = queue.pop(0)
            for k in range(4):
                if 0<=i+d[k]<m and 0<=j+d[k+1]<n and image[i+d[k]][j+d[k+1]]==original_color:
                    queue.append([i+d[k],j+d[k+1]])
                    image[i+d[k]][j+d[k+1]] = color
        return image
