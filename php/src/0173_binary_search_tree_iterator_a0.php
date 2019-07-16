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
     * @var Generator
     */
    protected $inorder;

    /**
     * BSTIterator constructor.
     *
     * @param TreeNode $root
     */
    public function __construct(?TreeNode $root)
    {
        $this->inorder = $this->getInorder($root);
    }

    /**
     * @param TreeNode $root
     *
     * @return Generator
     */
    function getInorder($root): Generator
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
        /** @var TreeNode $node */
        $node = $this->inorder->current();

        $this->inorder->next();

        return $node->val;
    }

    /**
     * @return bool whether we have a next smallest number
     */
    function hasNext()
    {
        return $this->inorder->valid();
    }
}
