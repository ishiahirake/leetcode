<?php


namespace BinaryTree;


use TreeNode;

/**
 * Binary Tree Postorder Traversal.
 *
 * @see     https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
 *
 * @package BinaryTree
 */
class PostorderTraversal
{
    /**
     * @param TreeNode $root
     *
     * @return int[]
     */
    function postorderTraversal($root)
    {
        $result = [];

        if ($left = $root->left) {
            $result = array_merge($result, $this->postorderTraversal($left));
        }

        if ($right = $root->right) {
            $result = array_merge($result, $this->postorderTraversal($right));
        }

        $result[] = $root->val;

        return $result;
    }
}