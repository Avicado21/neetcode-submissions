class Solution:
    def isPalindrome(self, s: str) -> bool:
        #okay so start from each end and work backwards and forwards until both sides meet
        #if they meet and nothing doesn't equal the other then we return the default true

        #remove all non letter symbols
        s = s.replace(" ", "" )
        s = s.replace("?", "")
        s = s.replace(",", "")
        s = s.replace("'", "")
        s = s.replace(".", "")
        s = s.replace(":", "")
        s = s.lower()
         
        #check base cases
        if(len(s) == 0 or len(s) == 1):
            return True

        #run odd or even check
        odd = False
        midpoint = len(s)/2


        if(len(s)%2 != 0):
            odd = True
            midpoint = int(len(s)/2) +1

        pali = True

        left = 0
        right = len(s)-1

        #do the iteration loop
        working = True
        while(working):

            #false condition
            if(s[right] != s[left]):
                pali = False
                working = False
                break
            
            #odd end
            if(odd):
                if(left + 1 == midpoint):
                    working = False
                    break
            #even end
            else:
                if(left == midpoint):
                    working = False
                    break

            
            left += 1 
            right -= 1

        return pali
        