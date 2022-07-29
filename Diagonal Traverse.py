#Approach - 1
#TC : O(n)
#SC : O(1)

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        result = [0] * (rows* cols)
        index=0
        r=0
        c=0
        dir_=1
        
        while(index<len(result)):
            result[index] = mat[r][c]
            #up
            if dir_ ==1:
                if c == cols -1:
                    r+=1
                    dir_=-1
                elif r==0:
                    c+=1
                    dir_=-1
                else:
                    r-=1
                    c+=1
            #down
            elif dir_ == -1:
                if r == rows-1:
                    c+=1
                    dir_=1
                elif c==0:
                    r+=1
                    dir_=1
                else:
                    r+=1
                    c-=1
            index+=1
        return result

#Approach - 2
#TC : O(n^2)
#SC : O(n)

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = list()
        sum_dict = defaultdict(list)


        # Segregate elements as per the sum if indexes (i,j)
        for i in range(m):
            for j in range(n):
                sum_dict[i+j].append(mat[i][j])
           

        # Take care of the right order of the elements as per traversal rules
        for i,v in sum_dict.items():
            if i%2 == 0:
                res.extend(v[::-1])
            else:
                res.extend(v)
        return res
                