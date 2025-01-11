class Solution:

    def rat(self, maze , r , c , n ,path , result):

        if r == n-1 and c == n-1 :
            result.append(path)

            return
        if 0<= r <= n-1 and 0 <= c <= n-1:
            if maze[r][c] == 0:
                maze[r][c] = 1

                self.rat(maze , r+1 , c , n , path+"D",result)

                self.rat(maze , r , c+1,n,path+"R", result)

                self.rat(maze , r-1 , c ,n, path+"U",result)

                self.rat(maze , r,c-1 , n, path+"L",result)

                maze[r][c] = 0

                return

        else :

            return


n = 4
maze = [[0]*n for _ in range(n)]
# here '0' means "rat can go " and '1' means there is a Obstacle .
maze[2][2] = 1
obj = Solution()
result = []
obj.rat(maze , 0 , 0 ,len(maze),"",result)

print(result)