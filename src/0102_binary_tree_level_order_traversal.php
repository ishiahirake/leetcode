<?php

/**
 * Binary Tree Level Order Traversal.
 *
 * @see https://leetcode.com/problems/binary-tree-level-order-traversal/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/
 */
class Solution
{
    /**
     * @param TreeNode $root
     *
     * @return int[][]
     */
    function levelOrder($root)
    {
        $result = [];
        if (!$root) {
            return $result;
        }

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

        return $result;
    }
}