<?php

/**
 * 107. Binary Tree Level Order Traversal II.
 *
 * @see https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
 */
class Solution
{
    /**
     * @param TreeNode $root
     *
     * @return int[][]
     */
    function levelOrderBottom($root)
    {
        $result = [];
        if (!$root) {
            return $result;
        }

        // For bottom-up level order traversal,
        // we can do up-bottom level order traversal
        // and then simply reserve the result.
        $nodes = [$root];
        for ($level = 0; !empty($nodes); $level++) {
            $leafs = [];
            /** @var TreeNode $node */
            foreach ($nodes as $node) {
                $result[$level][] = $node->val;
                if ($left = $node->left) {
                    $leafs[] = $left;
                }
                if ($right = $node->right) {
                    $leafs[] = $right;
                }
            }
            $nodes = $leafs;
        }

        return array_reverse($result);
    }
}