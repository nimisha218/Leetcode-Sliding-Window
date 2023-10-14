class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        d_t = {}
        s_t = {}

        left, right, need, have, flag = 0, 0, 0, 0, 0

        # Create a dictionary for t
        for character in t:
            d_t[character] = d_t.get(character, 0) + 1

        # print("t_dictionary: ", d_t)

        for key in d_t:
            s_t[key] = 0
            need += 1
    
        # print("Initial s dictionary: ", s_t)

        result = s

        while right < len(s):

            # print("Left: ", left)
            # print("Right: ", right)

            if left <= right and s[right] in s_t:

                s_t[s[right]] += 1

                if s_t[s[right]] == d_t[s[right]]:

                    have += 1

                    while have == need:

                        if len(s[left:right+1]) <= len(result):
                            flag = 1
                            result = s[left:right+1]
                            # print("Result updated: ", result)

                        if s[left] in s_t:
                            if s_t[s[left]] > 0:
                                s_t[s[left]] -= 1
                                if s_t[s[left]] < d_t[s[left]]:
                                    have -= 1
                                    
                        left += 1

                        while left < len(s) and s[left] not in s_t:
                            left = left + 1
                            # print("Updating left pointer: ", left)
                    
                    right += 1

                    # print("s_t: ", s_t)
                    # print("Need: ", need)
                    # print("Have: ", have)
                    # print("------------------")

                    continue
            right += 1

        if flag == 0:
            return ""

        return result

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         # Referred neetcode video

#         if t == "":
#             return ""

#         countT = {}
#         window = {}

#         for c in t:
#             countT[c] = 1 + countT.get(c, 0)

#         have = 0
#         need = len(countT)
#         result = [-1, -1]
#         result_length = float("infinity")
#         l = 0

#         for r in range(len(s)):
#             c = s[r]
#             window[c] = 1 + window.get(c, 0)

#             if c in countT and window[c] == countT[c]:
#                 have += 1
            
#             while have == need:

#                 # Update our result
#                 if (r - l + 1) <= result_length:
#                     result_length = (r - l + 1)
#                     result = [l, r]

#                 # Remove left most character from the window
#                 window[s[l]] -= 1

#                 if s[l] in countT and window[s[l]] < countT[s[l]]:
#                     have -= 1

#                 l += 1     
        
#         left = result[0]
#         right = result[1]

#         return s[left:right+1]



























        # # Approach 2:
        # # Using a sliding window technique and a dictionary:

        # # Let's maintain a dictionary for counts of t
        # t_count = {}

        # for el in t:
        #     if el not in t_count:
        #         t_count[el] = 1
        #     else:
        #         t_count[el] += 1
        
        # # print("t_count dictionary: ", t_count)

        # # Let's start our sliding window traversal
        # left = 0
        # right = 0
        # mismatch = 0

        # s_count = {}
        # result = []
        # flag = 0

        # while left < len(s) and right < len(s):

        #     # print("Substring in consideration: ", s[left:right+1])

        #     if s[right] in t_count:

        #         # print("s[right]: ", s[right])
        #         if flag == 0:
        #             if s[right] not in s_count:
        #                 s_count[s[right]] = 1
        #             else:
        #                 s_count[s[right]] += 1
                    
        #         diff = set(t_count.keys()).difference(s_count.keys())
        #         # print("S_count keys: ", s_count.keys())
        #         # print("T_count keys: ", t_count.keys())
        #         # print("Diff: ", diff)

        #         if len(diff) == 0:

        #             diff2 = set(t_count.values()).difference(s_count.values())
        #             # print("Test difference: ", diff2)

        #             if len(diff2) <= 0:

        #                 # print("Found a substring: ", s[left:right+1])
        #                 result.append(s[left:right+1])
        #                 if s[left] in s_count:
        #                     if s[left] in t_count:
        #                         # print("s_count before deletion: ", s_count)
        #                         if s_count[s[left]] == 1:
        #                             del s_count[s[left]]
        #                         else:
        #                             s_count[s[left]] -= 1
                            
                            
        #                         # print("Updated s_count: ", s_count)
        #                 left = left + 1
        #                 flag = 1
        #                 continue


        #         right = right + 1

        #     else:
        #         right = right + 1
            
        #     # print("Updated s_count dictionary: ", s_count)

        #     # print("----------------------")
        #     flag = 0

        # # print("Result: ", result)

        # if len(result) == 0:
        #     return ""
        
        # min_length = len(result[0])
        # res = result[0]

        # for el in result:
        #     if len(el) <= min_length:
        #         min_length = len(el)
        #         res = el
        # # print("Answer: ", res)
        # return res
                






























        # # Approach 1: 255/257
        # # Use a sliding window approach

        # t_list = [el for el in t]

        # result = []

        # left = 0
        # right = 0
        # store = [el for el in t_list]

        # while right < len(s) and left < len(s):

        #     # print("String in consideration: ", s[left:right+1])

        #     if s[right] in store:

        #         # Remove s[right] from store
        #         # print("Removing: ", s[right], " from ", store)
        #         store.remove(s[right])
        #         # print("Updated store is: ", store)

        #         if len(store) == 0:
        #             result.append(s[left:right+1])
        #             # print("Adding ", s[left:right+1], " to our result list.")
        #             left = left + 1
        #             right = left
        #             store = [el for el in t_list]
        #             # print("New left pointer: ", left)
        #             # print("New right pointer: ", right)
        #             # print("New store: ", store)
        #             continue
                
        #         right = right + 1
                
        #         # print("New left pointer: ", left)
        #         # print("New right pointer: ", right)
        #         # print("New store: ", store)


        #     else:
        #         right = right + 1
            
        #     # print("---------------------------------")

        # # print("---------------------")
        # # print("Result list: ", result)

        # output = 0

        # if len(result) == 0:
        #     return ""
        # else:
        #     min_string = len(result[0])

        # for string in result:
        #     # print("String: ", type(len(string)))
        #     # print("Min_string: ", type(min_string))
        #     if len(string) <= min_string:
        #         min_string = len(string)
        #         output = string
        
        # # print("-----------------")
        # # print("Minimum string found: ", output)

        # return output

   

        
            
            

            