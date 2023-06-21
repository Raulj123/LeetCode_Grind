
def maxArea(height: list[int]) -> int:
    l,r = 0, len(height)-1
    max_area, area = 0,0

    while(l <r):
        if(height[l] > height[r]):
            area = (r-l) * height[r]
            r-=1
        else:
            area = (r-l) * height[l]
            l+=1
        if area > max_area:
            max_area = area
    return max_area 

height = [1,8,6,2,5,4,8,3,7]
max_area = maxArea(height)
print("The max area of water is:", max_area)