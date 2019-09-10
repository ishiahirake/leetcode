<?php

/**
 * 23. Merge k Sorted Lists.
 *
 * @see https://leetcode.com/problems/merge-k-sorted-lists/
 */
class Solution
{
    /**
     * @param ListNode[] $lists
     *
     * @return ListNode
     */
    public function mergeKLists($lists)
    {
        if (empty($lists)) {
            return null;
        }

        if (count($lists) === 1) {
            return $lists[0];
        }

        $head = array_pop($lists);

        return array_reduce($lists, [$this, 'mergeList'], $head);
    }

    /**
     * @param ListNode|null $l1
     * @param ListNode|null $l2
     *
     * @return ListNode|null
     */
    protected function mergeList(ListNode $l1 = null, ListNode $l2 = null)
    {
        if ($l1 === null) {
            return $l2;
        }

        if ($l2 === null) {
            return $l1;
        }

        if ($l1->val <= $l2->val) {
            $head = $tail = $l1;
            $l1   = $l1->next;
        }
        else {
            $head = $tail = $l2;
            $l2   = $l2->next;
        }

        while ($l1 && $l2) {
            if ($l1->val < $l2->val) {
                $tail->next = $l1;
                $l1         = $l1->next;
            }
            else {
                $tail->next = $l2;
                $l2         = $l2->next;
            }
            $tail = $tail->next;
        }

        if ($l1) {
            $tail->next = $l1;
        }

        if ($l2) {
            $tail->next = $l2;
        }

        return $head;
    }
}