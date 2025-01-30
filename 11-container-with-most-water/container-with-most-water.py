class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0  
        right=len(height)-1 
        maximum_area=0  
        highest=max(height)

        while left<right:
            if height[left]<height[right]:
                curr_height=height[left]
            else:
                curr_height=height[right]
            curr_area=curr_height*(right-left)
            if curr_area>maximum_area:
                maximum_area=curr_area
            if highest*(right-left)<maximum_area:
                break
            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return maximum_area