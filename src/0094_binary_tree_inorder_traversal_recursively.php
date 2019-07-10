<?php

/**
 * Traverse binary tree inorder iteratively.
 *
 * @see https://leetcode.com/problems/binary-tree-inorder-traversal/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
 *
 * @see https://algorithm-visualizer.org/brute-force/binary-tree-traversal
 */
class Solution
{
    /**
     * @var array
     */
    protected $traversalResult = [];

    /**
     * @param TreeNode $root
     *
     * @return int[]
     */
    function inorderTraversal($root)
    {
        if ($left = $root->left) {
            $this->inorderTraversal($left);
        }

        $this->traversalResult[] = $root->val;

        if ($right = $root->right) {
            $this->inorderTraversal($right);
        }

        return $this->traversalResult;
    }
}