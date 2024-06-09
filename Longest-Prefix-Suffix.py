class Solution:
	def lps(self, s):
		# code here
            n = len(s)
            if n == 0:
                return 0  # If the string is empty, return 0
            
            # Create the prefix function array
            pi = [0] * n  # Initialize the prefix function array with zeros
            j = 0  # Length of the previous longest prefix suffix
            
            # Loop through the string to fill the prefix function array
            for i in range(1, n):
                # Adjust j while we have a mismatch
                while j > 0 and s[i] != s[j]:
                    j = pi[j - 1]  # Use the prefix function to backtrack
                
                # If there is a match, extend the current prefix suffix length
                if s[i] == s[j]:
                    j += 1
                
                pi[i] = j  # Update the prefix function array
            
            # The length of the longest proper prefix which is also a suffix
            return pi[n - 1]