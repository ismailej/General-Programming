class Solution(object):
    def calculate(self, height, start, count, ref):
        print('Reached calculate with start, end', start, count)
        store = 0
        #ref = height[start]
        #print(ref)
        i = start + 1
        end = count - 1
        while i <= end:
            store += ref - height[i]
            i += 1
        #print(store)
        #print('Returned value - ', store)
        return store 
    def calculate_max_array(self, height):
        i = len(height) - 1
        elem_max = -1
        max_array = [-1]*len(height)
        while i >= 0:
            if elem_max < height[i]:
                max_array[i] = elem_max
                elem_max = height[i]
            else:
                max_array[i] = elem_max
            i -= 1
        #print(max_array)
        return max_array
                
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if height == []:
            return 0
        start = 0
        
        count = 1
        length = len(height)
        total = 0
        max_array = self.calculate_max_array(height)
        ref = min(height[start], max_array[start])
        while(count < length):
            if ref <= height[count]:
                total += self.calculate(height, start, count, ref)
                start = count
                ref = min(height[start], max_array[start])
            count += 1

        
        return total
