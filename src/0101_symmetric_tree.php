<?php

/**
 * 101. Symmetric Tree.
 *
 * Using iterative approach.
 *
 * @see https://leetcode.com/problems/symmetric-tree/
 */
class Solution
{
    /**
     * @param TreeNode $root
     *
     * @return bool
     */
    function isSymmetric($root)
    {
        if (!$root) {
            return true;
        }

        /** @var TreeNode[] $nodes */
        $nodes = [$root];
        while ($nodes) {
            if (!$this->isSymmetricList($nodes)) {
                return false;
            }

            $leafs = [];
            foreach (array_filter($nodes) as $node) {
                $leafs[] = $node->left;
                $leafs[] = $node->right;
            }

            $nodes = $leafs;
        }

        return true;
    }

    /**
     * @param TreeNode[]|null[] $nodes
     *
     * @return bool
     */
    protected function isSymmetricList(array $nodes)
    {
        $values = array_map(function ($node) {
            /** @var TreeNode|null $node */
            return $node ? $node->val : null;
        }, $nodes);

        for ($i = 0, $j = count($values) - 1; $i <= $j; $i++, $j--) {
            if ($values[$i] !== $values[$j]) {
                return false;
            }
        }

        return true;
    }
}