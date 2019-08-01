<?php

declare(strict_types=1);

/**
 * 701. Insert into a Binary Search Tree.
 *
 * @see https://leetcode.com/problems/insert-into-a-binary-search-tree/
 * @see https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1003/
 */
class Solution
{
    /**
     * @param TreeNode $root
     * @param int      $val
     *
     * @return TreeNode
     */
    function insertIntoBST($root, $val)
    {
        if (!$root) {
            return new TreeNode($val);
        }

        $node = $root;
        for (; ;) {
            $pos = $node->val < $val ? 'right' : 'left';
            if ($node->{$pos} === null) {
                $node->{$pos} = new TreeNode($val);
                break;
            }

            $node = $node->{$pos};
        }

        return $root;
    }
}