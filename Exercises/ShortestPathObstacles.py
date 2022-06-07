import collections

class Solution():
    def shortestPath(grid, k):
        '''
        :type grid = List[List[int]]
        :type k = int
        :rtype : int
        
        '''

        rows, cols = len(grid), len(grid[0])
        target = (rows - 1, cols - 1 )

        #If we have suffient quotas to elminated the obstacles in the worst case
        # then the shortest distance = manhattan  distance

        if k >= rows + cols -2:
            return rows + cols -2

        # (row , col, remaining quota to eliminate obstacles)
        state = (0, 0, k)
        # (steps, state)
        queue = collections.deque([(0, state)])
        seen = set([state])

        while queue:
            steps, (row, col, k) = queue.popleft()

            # We reach the target here 
            if (row, col) == target:
                return steps

        # Explore the four directions in the next step
            for new_row, new_col in [(row, col + 1), (row + 1, col), (row, col - 1), (row -1, col)]:
                #if (new_row, new_col) is within grid boundaries 
                if (0 <= new_row < rows) and (0 <=  new_col , cols):
                    new_eliminations = k - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_eliminations)
                    # add the next move in the que if it qualifies 
                    if new_eliminations >= 0 and new_state not in seen:
                        seen.add(new_state)
                        queue.append((steps + 1, new_state))

        # did not reach the target 
        return -1



    print(shortestPath(([0,0,0],[1,1,0],[0,0,0],[0,1,1]), 1))



            
    
