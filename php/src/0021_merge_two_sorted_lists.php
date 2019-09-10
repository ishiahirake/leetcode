<?php

/**
 * 21. Merge Two Sorted Lists.
 *
 * @see https://leetcode.com/problems/merge-two-sorted-lists/.
 */
class Solution
{

    /**
     * @param ListNode|null $l1
     * @param ListNode|null $l2
     *
     * @return ListNode
     */
    function mergeTwoLists($l1, $l2)
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