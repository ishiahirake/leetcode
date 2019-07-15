<?php


namespace Ishiahirake\Leetcode\Tools;


use TreeNode;

/**
 * Class BinaryTree
 *
 * @package Ishiahirake\Leetcode\Tools
 */
class BinaryTree
{
    /**
     * @var BinaryTreeCodec
     */
    protected static $codec;

    /**
     * @var TreeNode
     */
    protected $root;

    /**
     * BinaryTree constructor.
     *
     * @param TreeNode $root
     */
    public function __construct(TreeNode $root)
    {
        $this->root = $root;
    }

    /**
     * @param string $data
     *
     * @return BinaryTree|null
     */
    public static function deserialize(string $data): ?BinaryTree
    {
        $root = self::codec()->deserialize($data);

        return $root ? new BinaryTree($root) : null;
    }

    /**
     * @return BinaryTreeCodec
     */
    protected static function codec(): BinaryTreeCodec
    {
        if (!isset(self::$codec)) {
            self::$codec = new BinaryTreeCodec();
        }

        return self::$codec;
    }

    /**
     * @return array
     */
    public function serialize()
    {
        return self::codec()->serialize($this->getRoot());
    }

    /**
     * @return TreeNode
     */
    public function getRoot(): TreeNode
    {
        return $this->root;
    }
}