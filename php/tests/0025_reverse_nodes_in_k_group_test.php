<?php

class p0025_reverse_nodes_in_k_group_test extends TestCase
{
    /**
     * @var Solution
     */
    protected $solution;

    /**
     *
     */
    public function testKEqualsToListLength()
    {
        $head = $this->makeLinkedList([1, 2, 3, 4, 5]);

        $this->assertEquals(
            [5, 4, 3, 2, 1],
            $this->linkedListToArray(
                $this->solution->reverseKGroup($head, 5)
            )
        );
    }

    protected function makeLinkedList(array $values): ?ListNode
    {
        if (!$values) {
            return null;
        }

        $head = new ListNode(0);

        array_reduce($values, function (ListNode $tail, $value) {
            $tail->next = new ListNode($value);
            return $tail->next;
        }, $head);

        return $head->next;
    }

    protected function linkedListToArray(ListNode $head): array
    {
        if (!$head) {
            return [];
        }

        $values = [];
        while ($head) {
            $values[] = $head->val;
            $head     = $head->next;
        }

        return $values;
    }

    /**
     */
    protected function setUp(): void
    {
        $this->solution = new Solution();
    }
}