class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        # recursive function
        def backtrack(word, arr, index):
            if not palindrome(word):
                return False
            
            arr.append(word)

            if index == len(s):
                ans.append(arr.copy())
                return True

            for i in range(index, len(s)):
                val = backtrack(s[index:i+1], arr, i + 1)
                if val:
                    arr.pop()
            return True
                

        # palindrome helper
        def palindrome(w):
            left = 0
            right = len(w) - 1
            ans = True

            while left < right and ans:
                if w[left] != w[right]:
                    ans = False
                left += 1
                right -= 1
            
            return ans
        
        for i in range(0, len(s)):
                val = backtrack(s[0:i+1], [], i + 1)
        return ans


