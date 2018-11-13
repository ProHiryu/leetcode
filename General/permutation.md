# Permutations

## Standard

```python
def permute(nums):
    permutations = [[]]
    
    for head in nums:
        permutations = [rest[:i]+[head]+rest[i:] for rest in permutations for i in range(len(rest)+1)]
        
    return permutations
```

- we insert new element at each slot (index i = 0,1,...,len(rest)) at each iteration


## without duplicates

```python
def permute(nums):
    permutations = [[]]
    
    for head in nums:
        permutations = [rest[:i]+[head]+rest[i:] for rest in permutations for i in range((rest+[head]).index(head)+1)]
        
    return permutations
```

but for non-duplicate version, either the new element does not exist in rest (in this case just insert it everywhere like before) or we only insert up to the first occurrence rest.index(head), because any other slot after the first occurrence can be thought as the duplicate of the first occurrence as the inserted element and the slot being the existing one.