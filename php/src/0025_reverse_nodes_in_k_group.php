<?php

class Solution
{
    /**
     * @param ListNode $head
     * @param Integer  $k
     *
     * @return ListNode
     */
    public function reverseKGroup($head, $k)
    {
        if (!$head || !$head->next || !$this->hasAtLeastLength($head, $k)) {
            return $head;
        }

        $newHead    = $tail = $head;
        $node       = $head->next;
        for ($i = 1; $i < $k; $i++) {
            if (!$node) {
                break;
            }

            $next       = $node;
            $node       = $node->next;
            $next->next = $newHead;
            $newHead    = $next;

            if ($i === $k - 1) {
                $tail->next = $this->reverseKGroup($node, $k);
            }
        }

        return $newHead;
    }

    /**
     * @param ListNode $head
     * @param int      $k
     *
     * @return bool
     */
    protected function hasAtLeastLength($head, $k)
    {
        for ($i = 1; $head; $i++) {
            if ($i === $k) {
                return true;
            }
            $head = $head->next;
        }

        return false;
    }
}
