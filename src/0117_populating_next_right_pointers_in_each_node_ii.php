<?php

/**
 * 117. Populating Next Right Pointers in Each Node II.
 *
 * @see https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/1016/
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
        if ($root === null) {
            return $root;
        }

        if ($left = $root->left) {
            if ($root->right) {
                $left->next = $root->right;
            }
            else {
                $left->next = $this->getRootNextSubNode($root);
            }
        }

        if ($right = $root->right) {
            $right->next = $this->getRootNextSubNode($root);
        }

        // Should connect right node first
        // otherwise the right part's linkage will be insufficient.
        $this->connect($root->right);
        $this->connect($root->left);

        return $root;
    }

    /**
     * @param Node $root
     *
     * @return Node|null
     */
    protected function getRootNextSubNode($root)
    {
        $next = $root->next;

        while ($next && ($next->left === null && $next->right === null)) {
            $next = $next->next;
        }

        if ($next === null) {
            return $next;
        }

        return $next->left ?: $next->right;
    }
}
