<?php

/**
 * Traverse binary tree postorder iteratively.
 *
 * @see https://leetcode.com/problems/binary-tree-postorder-traversal/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
 *
 * @see https://algorithm-visualizer.org/brute-force/binary-tree-traversal
 */
class Solution
{
    /**
     * @param TreeNode $root
     *
     * @return int[]
     */
    function postorderTraversal($root)
    {
        $result = [];
        if (!$root) {
            return $result;
        }

        // Unlike preorder traversal, for postorder traversal,
        // we should use a flag to keep whether the node is traversed or not
        // since we put it in and pop it later.
        $nodes = [
            [$root, false],
        ];
        while ($nodes) {
            /** @var TreeNode $node */
            list($node, $traversed) = array_pop($nodes);
            if ($traversed) {
                $result[] = $node->val;
                continue;
            }

            $nodes[] = [$node, true];
            if ($right = $node->right) {
                $nodes[] = [$right, false];
            }

            if ($left = $node->left) {
                $nodes[] = [$left, false];
            }
        }

        return $result;
    }
}