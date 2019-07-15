<?php

/**
 * 173. Binary Search Tree Iterator.
 *
 * @see https://leetcode.com/problems/binary-search-tree-iterator/
 * @see https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/1008/
 */
class BSTIterator
{
    /**
     * @var TreeNode[]
     */
    protected $nodes = [];

    /**
     * @param TreeNode $root
     */
    public function __construct($root)
    {
        $this->pushLeftNodes($root);
    }

    /**
     * @param TreeNode|null $node
     */
    protected function pushLeftNodes(?TreeNode $node)
    {
        while ($node !== null) {
            $this->nodes[] = $node;
            $node          = $node->left;
        }
    }

    /**
     * @return int the next smallest number
     */
    public function next()
    {
        $node = array_pop($this->nodes);

        $this->pushLeftNodes($node->right);

        return $node->val;
    }

    /**
     * @return bool whether we have a next smallest number
     */
    public function hasNext()
    {
        return !empty($this->nodes);
    }
}
