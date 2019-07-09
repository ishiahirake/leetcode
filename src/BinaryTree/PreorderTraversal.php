<?php


namespace Ishiahirake\Leetcode\BinaryTree;


use TreeNode;

/**
 * Binary Tree Preorder Traversal.
 *
 * @see     https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
 *
 * @package Ishiahirake\Leetcode\BinaryTree
 */
class PreorderTraversal
{
    /**
     * @param TreeNode $root
     *
     * @return int[]
     */
    function preorderTraversal($root)
    {
        $result = [];

        $result[] = $root->val;

        if ($left = $root->left) {
            $result = array_merge($result, $this->preorderTraversal($left));
        }

        if ($right = $root->right) {
            $result = array_merge($result, $this->preorderTraversal($right));
        }

        return $result;
    }
}