<?php

use Ishiahirake\Leetcode\Tools\BinaryTree;

/**
 * Class p0173_binary_search_tree_iterator_test
 */
class p0173_binary_search_tree_iterator_a0_test extends TestCase
{
    /**
     */
    public function testBasic()
    {
        $iterator = $this->makeBSTIterator("[7,3,15,null,null,9,20]");

        $this->assertEquals(3, $iterator->next());
        $this->assertEquals(7, $iterator->next());
        $this->assertTrue($iterator->hasNext());
        $this->assertEquals(9, $iterator->next());
        $this->assertTrue($iterator->hasNext());
        $this->assertEquals(15, $iterator->next());
        $this->assertTrue($iterator->hasNext());
        $this->assertEquals(20, $iterator->next());
        $this->assertFalse($iterator->hasNext());
    }

    /**
     * @param string $data
     *
     * @return BSTIterator|null
     */
    protected function makeBSTIterator(string $data): ?BSTIterator
    {
        $binaryTree = BinaryTree::deserialize($data);
        if (!$binaryTree) {
            return null;
        }

        return new BSTIterator($binaryTree->getRoot());
    }
}