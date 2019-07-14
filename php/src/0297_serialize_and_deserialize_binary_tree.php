<?php

/**
 * 297. Serialize and Deserialize Binary Tree.
 *
 * Encode / Decode binary tree using Leetcode's format.
 *
 * @see https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/995/
 *
 * @see https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation-
 */
class Solution
{
    /**
     * @param TreeNode $root
     *
     * @return array|TreeNode
     */
    function Codec($root)
    {
        if (is_string($root)) {
            return $this->deserialize($root);
        }

        return $this->serialize($root);
    }

    /**
     * @param string $data
     *
     * @return TreeNode|null
     */
    public function deserialize(string $data): ?TreeNode
    {
        $values = json_decode($data);
        if (empty($values)) {
            return null;
        }

        $root = new TreeNode($values[0]);
        $this->fillTree([$root], array_slice($values, 1));

        return $root;
    }

    /**
     * @param TreeNode[] $nodes
     * @param array      $values
     *
     * @return array
     */
    protected function fillTree(array $nodes, array $values): array
    {
        if (!$values) {
            return [];
        }

        $leafs     = [];
        $leafCount = count($nodes) * 2;
        $count     = min($leafCount, count($values));

        for ($i = 0; $i < $count; $i++) {
            $key  = $i % 2 == 0 ? 'left' : 'right';
            $node = $values[$i] ? new TreeNode($values[$i]) : null;

            $nodes[$i / 2]->{$key} = $node;
            $node && $leafs[] = $node;
        }

        return $this->fillTree($leafs, array_slice($values, $leafCount));
    }

    /**
     * Encode a tree.
     *
     * NOTE:
     * Although there are `String` return type in the template code,
     * to pass the test we should return array actually.
     *
     * @param TreeNode|null $node
     *
     * @return array
     */
    public function serialize(?TreeNode $node)
    {
        if (!$node) {
            return [];
        }

        $result = [$node->val];
        $nodes  = [$node];
        while (!empty($nodes)) {
            $leafs = [];
            foreach ($nodes as $node) {
                array_push($result, $node->left->val ?? null, $node->right->val ?? null);

                if ($node->left !== null) {
                    $leafs[] = $node->left;
                }
                if ($node->right !== null) {
                    $leafs[] = $node->right;
                }
            }
            $nodes = $leafs;
        }

        // Remove trim null values
        $maxNotNullIndex = count($result) - 1;
        while ($result[$maxNotNullIndex] === null) {
            $maxNotNullIndex--;
        }

        return array_slice($result, 0, $maxNotNullIndex + 1);
    }
}
