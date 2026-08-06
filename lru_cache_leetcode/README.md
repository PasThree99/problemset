# Problem source
https://leetcode.com/problems/lru-cache?q=lru+

# Notes
The c implememtation does not pass the leet code problem. This implementation was done using raw linked lists, no hash tables were implemented which makes the runtime slower, specifically at look up time: linked lists have a O(n) complexity whereas hash tables have pseudo O(1) lookup. However, the Python implementation uses maps which makes lookups faster and thus passes the problem.