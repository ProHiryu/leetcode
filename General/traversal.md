# Tree Travesal

## Recrusion

### Inorder

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
        
    def inorderTraversal(self, root):
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)
```

### Preorder

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
        
    def preorderTraversal(self, root):
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
```

### Postorder

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
        
    def postorderTraversal(self, root):
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.res.append(root.val)
```

## Iteration

### Inorder

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def inorderTraversal(self, root):
        res = []
        stack = []
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right

        return res
```

### Preorder

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        res = []
        stack = []
        
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
                
        return res
```

### Postorder

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        res = []
        stack = []
        
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root.left)
                root = root.right
            else:
                root = stack.pop()
        
        return res[::-1]
```


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        res = []
        stack = [root]
        stack_final = []
        
        while stack:
            root = stack.pop()
            stack_final.append(root)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        
        while stack_final:
            res.append(stack_final.pop().val)
        
        return res
```
