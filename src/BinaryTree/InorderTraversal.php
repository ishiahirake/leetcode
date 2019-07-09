<?php


namespace Ishiahirake\Leetcode\BinaryTree;


use TreeNode;

/**
 * Binary Tree Inorder Traversal.
 *
 * @see     https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
 *
 * @package Ishiahirake\Leetcode\BinaryTree
 */
class InorderTraversal
{
    /**
     * @param TreeNode $root
     *
     * @return int[]
     */
    function inorderTraversal($root)
    {
        $result = [];

        if ($left = $root->left) {
            $result = array_merge($result, $this->inorderTraversal($left));
        }

        $result[] = $root->val;

        if ($right = $root->right) {
            $result = array_merge($result, $this->inorderTraversal($right));
        }

        return $result;
    }
}