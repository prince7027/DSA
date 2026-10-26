class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            # Shift from 1-indexed to 0-indexed
            columnNumber -= 1
            
            # Find the remainder to determine the current character
            remainder = columnNumber % 26
            
            # Convert remainder to character and append to list
            result.append(chr(ord('A') + remainder))
            
            # Move to the next digit position
            columnNumber //= 26
            
        # The list was built right-to-left, so reverse it to get the final title
        return "".join(reversed(result))
