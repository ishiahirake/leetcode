<?php

// Given a binary tree, count the number of uni-value subtrees.
//
// A Uni-value subtree means all nodes of the subtree have the same value.
//
// Example :
//
// Input:  root = [5,1,5,5,5,null,5]
//
//                5
//               / \
//              1   5
//             / \   \
//            5   5   5
//
// Output: 4
//

/**
 * 250. Count Uni-value Subtrees.
 *
 * @see https://leetcode.com/problems/count-univalue-subtrees/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/538/
 */
class Solution
{
    /**
     * @var int
     */
    protected $uniValueCount = 0;

    /**
     * @param TreeNode $root
     *
     * @return int
     */
    function countUnivalSubtrees($root)
    {
        if (!$root) {
            return 0;
        }

        $this->isUnivalSubtreeCount($root);

        return $this->uniValueCount;
    }

    /**
     * @param TreeNode $root
     *
     * @return bool
     */
    protected function isUnivalSubtreeCount($root)
    {
        if (!$root) {
            return true;
        }

        if ($root->left === null && $root->right === null) {
            $this->uniValueCount++;
            return true;
        }

        $isLeftUnival  = $this->isUnivalSubtreeCount($root->left);
        $isRightUnival = $this->isUnivalSubtreeCount($root->right);

        if (!$isLeftUnival || !$isRightUnival) {
            return false;
        }

        $leftVal  = $root->left ? $root->left->val : $root->val;
        $rightVal = $root->right ? $root->right->val : $root->val;

        if ($root->val === $leftVal && $root->val === $rightVal) {
            $this->uniValueCount++;
            return true;
        }

        return false;
    }
}