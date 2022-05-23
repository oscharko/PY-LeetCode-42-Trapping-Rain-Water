heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

class Solution(object):
    def trap(self, height):
        v = [0,len(height)-1, 0, 0]
        while (v[0] < v[1]):
          v[2] = max(v[2], min(height[v[0]], height[v[1]]))
          v[3] += v[2] - min(height[v[0]], height[v[1]])

          if height[v[0]] <= height[v[1]]:
            v[0] += 1
          else:
            v[1] -= 1
        return v[3]

print(Solution().trap(heights))
