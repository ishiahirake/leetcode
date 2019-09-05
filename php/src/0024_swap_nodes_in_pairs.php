<?php

/**
 * 24. Swap Nodes in Pairs.
 *
 * https://leetcode.com/problems/swap-nodes-in-pairs/
 */
class Solution
{
    /**
     * @param ListNode $head
     *
     * @return ListNode
     */
    public function swapPairs($head)
    {
        if (!$head || !$head->next) {
            return $head;
        }

        $next = $head->next;

        $head->next = $this->swapPairs($next->next);
        $next->next = $head;

        return $next;
    }
}
