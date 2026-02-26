---
title: "Encode and Decode"
question_id: ""
question_link: "https://neetcode.io/problems/string-encode-and-decode/question"
difficulty: "Medium"
---
This is one of those questions where if you don't know decoding or encoding you can't solve it... Like probably unless your super smart but that's not me.

1. Input a list of strings
2. Create an encoder that encodes the string and a decoder that decodes the string into a list

The main thing when encoding to think about is [length of string][delimeter][string value] this is the process of encoding. With each value we want to combine them together with that specific order

When decoding we can thus use the length of the string and two pointers to determine each word, then spit the word into a list of the words and boom its completed.

The delimiter has to be something unique and the other thing to think about is basically edge cases such as what if the string in the list has a space ["Hello World", "Sup"], this would mean if we used space as a delimeter it could cause issues. 

I just really hate this question. But at least its useful irl like HTTP, Zip files etc.. all use similar context.
```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string = encoded_string + str(len(word)) + "#" + word
        return encoded_string
    

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j 
        return result
```

> Time Complexity : `O(m)`
> 
> Space Complexity : `O(m + n)`