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
        if (!$root) {
            return $root;
        }

        $this->levelConnect([$root]);

        return $root;
    }

    /**
     * @param Node[] $nodes
     */
    protected function levelConnect(array $nodes)
    {
        $nodeCount = count($nodes);
        for ($i = 0; $i < $nodeCount - 1; $i++) {
            $nodes[$i]->next = $nodes[$i + 1];
        }

        // Since the tree is a perfect binary tree,
        // so when a node's left (or right) node is null,
        // it indicate there is no more nodes,
        // we can just stop the recursion here.
        if ($nodes[0]->left === null) {
            return;
        }

        $leafs = [];
        foreach ($nodes as $node) {
            array_push($leafs, $node->left, $node->right);
        }

        $this->levelConnect($leafs);
    }
}
