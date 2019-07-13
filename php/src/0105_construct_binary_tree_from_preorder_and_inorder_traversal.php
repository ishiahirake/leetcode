<?php

/**
 * 105. Construct Binary Tree from Preorder and Inorder Traversal.
 *
 * @see https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/943/
 */
class Solution
{
    /**
     * @param int[] $preorder
     * @param int[] $inorder
     *
     * @return TreeNode
     */
    function buildTree($preorder, $inorder)
    {
        if (empty($preorder)) {
            return null;
        }

        // Preorder's first node is the root node of tree.
        $root = new TreeNode($rootVal = $preorder[0]);

        $index = array_search($rootVal, $inorder);

        $root->left = $this->buildTree(
            array_slice($preorder, 1, $index),
            array_slice($inorder, 0, $index)
        );

        $root->right = $this->buildTree(
            array_slice($preorder, $index + 1),
            array_slice($inorder, $index + 1)
        );

        return $root;
    }
}