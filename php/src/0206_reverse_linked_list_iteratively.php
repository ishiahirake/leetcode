<?php

/**
 * 206. Reverse Linked List.
 *
 * https://leetcode.com/problems/reverse-linked-list/
 */
class Solution
{
    /**
     * @param ListNode $head
     *
     * @return ListNode
     */
    public function reverseList($head)
    {
        $newHead = null;
        $node    = $head;

        while ($node) {
            $next       = $node->next;
            $node->next = $newHead;
            $newHead    = $node;
            $node       = $next;
        }

        return $newHead;
    }
}
