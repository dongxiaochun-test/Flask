from typing import List

class Solution(object):
  def longestCommonPrefix(self, strs: List[str]) -> str:
    res = ""
    for tmp in zip(*strs):
        tmp_set = set(tmp)
        if len(tmp_set) == 1:
            res += tmp[0]
        else:
            break
    return res

b = ["flower","flow","flight"]
#a = Solution.longestCommonPrefix(b)     #错误表达
a = Solution().longestCommonPrefix(b)

print(a)



# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。