---
layout: post
title: Programming knowledge
description: Interesting programming knowledge
published: true
---

# Programming knowledge

## Data types
- In C#, a boolean takes 1 bit of memory, however, if one uses sizeof(bool), it will return 1 byte, and not 1 bit. This is because the smallest addressable unit of memory is a byte. The remaining 7 bits are stuffed. 
- `iterrows()` can be used for a pandas data frame, to get the index and the row. However, it is not the most efficient way to iterate over a data frame. The most efficient way is to use `itertuples()` or `iteritems()`.
- `a = {"name":10, "age":10}` can be updated using `a.update({"name":20})`, no need to use `a["name"] = 20`.
