<?php

/**
 * 112. Path Sum.
 *
 * @see https://leetcode.com/problems/path-sum/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
 */
class Solution
{
    /**
     * @param TreeNode $root
     * @param Integer  $sum
     *
     * @return bool
     */
    function hasPathSum($root, $sum)
    {
        if ($root === null) {
            return false;
        }

        // The condition is the node is **a leaf** and it's val equals to the sum.
        if ($root->val === $sum && $root->left === null && $root->right === null) {
            return true;
        }

        if ($this->hasPathSum($root->left, $sum - $root->val)) {
            return true;
        }

        return $this->hasPathSum($root->right, $sum - $root->val);
    }
}
