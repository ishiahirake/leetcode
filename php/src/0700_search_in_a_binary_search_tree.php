<?php

/**
 * 700. Search in a Binary Search Tree.
 *
 * @see https://leetcode.com/problems/search-in-a-binary-search-tree/
 * @see https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1000/
 */
class Solution
{
    /**
     * @param TreeNode $root
     * @param int      $val
     *
     * @return TreeNode
     */
    function searchBST($root, $val)
    {
        if ($root === null) {
            return null;
        }

        if ($root->val === $val) {
            return $root;
        }

        if ($root->val > $val) {
            return $this->searchBST($root->left, $val);
        }

        return $this->searchBST($root->right, $val);
    }
}