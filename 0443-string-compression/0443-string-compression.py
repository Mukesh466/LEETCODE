class Solution:
  def compress(self, chars: List[str]) -> int:
    ans = 0
    i = 0
    while i < len(chars):
      l = chars[i]
      count = 0
      while i < len(chars) and chars[i] == l:
        count += 1
        i += 1
      chars[ans] = l
      ans += 1
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1

    return ans