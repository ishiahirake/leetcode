<?php

/**
 * 104. Maximum Depth of Binary Tree.
 *
 * Using bottom-up approach.
 *
 * @see https://leetcode.com/problems/maximum-depth-of-binary-tree/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
 */
class Solution
{

    /**
     * @param TreeNode $root
     *
     * @return int
     */
    function maxDepth($root)
    {
        if ($root === null) {
            return 0;
        }

        $leftDepth  = $this->maxDepth($root->left);
        $rightDepth = $this->maxDepth($root->right);

        return max($leftDepth, $rightDepth) + 1;
    }
}