<?php

/**
 * 98. Validate Binary Search Tree.
 *
 * @see https://leetcode.com/problems/validate-binary-search-tree/
 * @see https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/997/
 *
 * TestCase:
 *
 * // [1, 1]
 * // [10,5,15,null,null,6,20]
 */
class Solution
{
    /**
     * @var TreeNode
     */
    protected $lastNode = null;

    /**
     * Check given binary tree is a binary search tree or not.
     *
     * As the definition of binary search tree, it's **inorder traversal**
     * will be in **ascending order**, so to validate a binary search tree,
     * we just to validate it's **inorder traversal** will be in **ascending order**.
     *
     * @param TreeNode $root
     *
     * @return bool
     */
    function isValidBST($root)
    {
        if ($root === null) {
            return true;
        }

        if (!$this->isValidBST($root->left)) {
            return false;
        }

        if ($this->lastNode !== null && $this->lastNode->val >= $root->val) {
            return false;
        }

        $this->lastNode = $root;

        return $this->isValidBST($root->right);
    }
}
