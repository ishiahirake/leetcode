<?php

/**
 * 106. Construct Binary Tree from Inorder and Postorder Traversal.
 *
 * @see https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/942/
 */
class Solution
{
    /**
     * @param int[] $inorder
     * @param int[] $postorder
     *
     * @return TreeNode
     */
    function buildTree($inorder, $postorder)
    {
        if (empty($inorder)) {
            return null;
        }

        $root = new TreeNode($rootVal = end($postorder));

        $index = array_search($rootVal, $inorder);

        $root->left = $this->buildTree(
            array_slice($inorder, 0, $index),
            array_slice($postorder, 0, $index)
        );

        $root->right = $this->buildTree(
            array_slice($inorder, $index + 1),
            array_slice($postorder, $index, -1)
        );

        return $root;
    }
}