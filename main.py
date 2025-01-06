class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        
        # Step 1: Calculate the left to right pass (prefix)
        left_operations = [0] * n
        left_ball_count = 0
        left_distance = 0
        for i in range(1, n):
            if boxes[i-1] == '1':
                left_ball_count += 1
            left_operations[i] = left_operations[i-1] + left_ball_count
        
        # Step 2: Calculate the right to left pass (suffix)
        right_operations = [0] * n
        right_ball_count = 0
        right_distance = 0
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1':
                right_ball_count += 1
            right_operations[i] = right_operations[i+1] + right_ball_count
        
        # Step 3: Combine both left and right operations
        result = [0] * n
        for i in range(n):
            result[i] = left_operations[i] + right_operations[i]
        
        return result
