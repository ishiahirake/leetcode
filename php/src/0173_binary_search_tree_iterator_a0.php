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
     * @var TreeNode
     */
    protected $root = null;

    /**
     * @var Generator
     */
    protected $inorderNext;

    /**
     * @var TreeNode[]
     */
    protected $nodes = [];

    /**
     * BSTIterator constructor.
     *
     * @param TreeNode $root
     */
    public function __construct(?TreeNode $root)
    {
        $this->root = $root;

        $this->inorderNext = $this->getInorderNext($root);
    }

    /**
     * @param TreeNode $root
     *
     * @return Generator
     */
    function getInorderNext($root): Generator
    {
        if (!$root) {
            return;
        }

        $nodes = [
            [$root, false],
        ];
        while ($nodes) {
            /** @var TreeNode $node */
            list($node, $traversed) = array_pop($nodes);
            if ($traversed) {
                yield $node;
                continue;
            }

            if ($right = $node->right) {
                $nodes[] = [$right, false];
            }

            $nodes[] = [$node, true];

            if ($left = $node->left) {
                $nodes[] = [$left, false];
            }
        }
    }

    /**
     * @return int the next smallest number
     */
    function next()
    {
        if (!$this->hasNext()) {
            return null;
        }

        return array_shift($this->nodes)->val;
    }

    /**
     * @return bool whether we have a next smallest number
     */
    function hasNext()
    {
        if (!empty($this->nodes)) {
            return true;
        }

        if (!$this->inorderNext->valid()) {
            return false;
        }

        $this->nodes[] = $this->inorderNext->current();
        $this->inorderNext->next();

        return true;
    }
}
