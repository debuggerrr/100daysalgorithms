
Problem Statement Link:
https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False
        
        node_stack=[root]
        sum_final = [sum-root.val]
        while node_stack:
            current_node= node_stack.pop(0)
            current_sum=sum_final.pop(0)
            if (current_node.left==None and current_node.right==None and current_sum==0):
                return True
            if(current_node.left!=None):
                node_stack.append(current_node.left)
                sum_final.append(current_sum-current_node.left.val)
            if(current_node.right!=None):
                node_stack.append(current_node.right)
                sum_final.append(current_sum-current_node.right.val)
        return False
"""
Here the approach would be as we travel the tree leafs we would decrement the sum. Initially we have added the root element and the intial sum(Queues)after subtracting the root with the intial sum passed. While there are elements under the queue we will pop up the elements from the queue we will add the left and right elements of the tree to the queue as well as will keep on decrement the sum while traversing and will add to the queue and in next iteration if the sum which is popped up is 0 then will return true or else false. Also added validation to check whether we have reached the end of the left and right subtree along with checking the sum to be 0
"""