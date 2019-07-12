<?php

/**
 * 101. Symmetric Tree.
 *
 * Using recursive approach.
 *
 * @see https://leetcode.com/problems/symmetric-tree/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/
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
        return $this->isSymmetricSubTree([$root]);
    }

    /**
     * @param TreeNode[]|null[] $nodes
     *
     * @return bool
     */
    protected function isSymmetricSubTree(array $nodes)
    {
        if (!$this->isSymmetricList($nodes)) {
            return false;
        }

        $leafs = [];
        foreach (array_filter($nodes) as $node) {
            array_push($leafs, $node->left, $node->right);
        }

        if (!$leafs) {
            return true;
        }

        return $this->isSymmetricSubTree($leafs);
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
