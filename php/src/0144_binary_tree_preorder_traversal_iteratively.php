<?php

/**
 * Traverse binary tree preorder iteratively.
 *
 * @see https://leetcode.com/problems/binary-tree-preorder-traversal/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
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
     * Binary Tree Preorder Traversal Iteratively.
     *
     * @param TreeNode $root
     *
     * @return int[]
     */
    function preorderTraversal($root)
    {
        $result = [];
        $nodes  = [];

        $node = $root;
        while ($node) {
            $result[] = $node->val;

            if ($right = $node->right) {
                $nodes[] = $right;
            }

            if ($left = $node->left) {
                $node = $left;
                continue;
            }

            $node = array_pop($nodes);
        }

        return $result;
    }
}