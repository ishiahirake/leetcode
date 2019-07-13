<?php

/**
 * 116. Populating Next Right Pointers in Each Node.
 *
 * @see https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/994/
 */
class Solution
{
    /**
     * @param Node $root
     *
     * @return Node
     */
    function connect($root)
    {
        if (!$root || $root->left === null) {
            return $root;
        }

        $root->left->next  = $root->right;
        $root->right->next = $root->next ? $root->next->left : null;

        $this->connect($root->left);
        $this->connect($root->right);

        return $root;
    }
}
