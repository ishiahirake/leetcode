<?php

/**
 * Traverse binary tree recursively.
 *
 * @see https://leetcode.com/problems/binary-tree-postorder-traversal/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
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
    function postorderTraversal($root)
    {
        if ($left = $root->left) {
            $this->postorderTraversal($left);
        }

        if ($right = $root->right) {
            $this->postorderTraversal($right);
        }

        $this->traversalResult[] = $root->val;

        return $this->traversalResult;
    }
}