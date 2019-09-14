<?php

/**
 * 704. Binary Search.
 *
 * @see https://leetcode.com/problems/binary-search/
 */
class Solution
{
    /**
     * @param int[] $nums
     * @param int   $target
     *
     * @return int
     */
    public function search($nums, $target)
    {
        if (!$nums) {
            return -1;
        }

        list($mini, $maxi) = [0, count($nums) - 1];

        while ($mini <= $maxi) {
            $index = intdiv($mini + $maxi, 2);
            if ($nums[$index] < $target) {
                $mini = $index + 1;
            }
            else if ($nums[$index] > $target) {
                $maxi = $index - 1;
            }
            else {
                return $index;
            }
        }

        return -1;
    }
}