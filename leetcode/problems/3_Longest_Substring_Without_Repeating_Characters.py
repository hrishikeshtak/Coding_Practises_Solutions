"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        visited = set()
        start_index = 0
        end_index = 0
        max_length = 0

        # breakpoint()
        while end_index < len(str):
            if str[end_index] not in visited:
                visited.add(str[end_index])
                end_index += 1
                # print(visited, start_index, end_index)
            else:
                # print(visited, start_index, end_index)
                max_length = max(max_length, len(visited))
                # find where the char is matched
                while start_index < end_index:
                    if str[start_index] == str[end_index]:
                        start_index += 1
                        break
                    else:
                        visited.remove(str[start_index])
                        start_index += 1
                end_index += 1

        return max(max_length, len(visited))


if __name__ == '__main__':
    # str = "abcadf"
    # str = "dvdf"
    # str = "abcabcbb"
    # str = "bbbbb"
    # str = ""
    # str = "pwwkew"
    # str = "hkcpmprxxxqw"
    # str = "amqpcsrumjjufpu"
    # str = "bpfbhmipx"
    # str = "wsslpluuwekuaxt"
    # str = "ruowzgiooobpple"
    # str = "aabaab!bb"
    # str = " "
    print(Solution().lengthOfLongestSubstring(str))
