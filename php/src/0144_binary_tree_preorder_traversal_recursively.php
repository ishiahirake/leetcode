<?php

/**
 * Traverse binary tree preorder recursively.
 *
 * @see https://leetcode.com/problems/binary-tree-preorder-traversal/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
 *
 * @see https://algorithm-visualizer.org/brute-force/binary-tree-traversal
 */
class Solution {
    /**
     * @var array
     */
    protected $traversalResult = [];

    /**
     *
     * @param TreeNode $root
     *
     * @return int[]
     */
    function preorderTraversal($root)
    {
        $this->traversalResult[] = $root->val;

        if ($left = $root->left) {
            $this->preorderTraversal($left);
        }

        if ($right = $root->right) {
            $this->preorderTraversal($right);
        }

        return $this->traversalResult;
    }
}