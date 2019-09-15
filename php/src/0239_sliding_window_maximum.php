<?php

class Solution
{
    /**
     * @param int[] $nums
     * @param int   $k
     *
     * @return int[]
     */
    public function maxSlidingWindow($nums, $k)
    {
        $result = [];
        $limit  = count($nums) - $k;
        for ($i = 0; $i <= $limit; $i++) {
            $result[] = max(array_slice($nums, $i, $k));
        }

        return $result;
    }
}
