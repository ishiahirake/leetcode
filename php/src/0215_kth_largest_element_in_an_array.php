<?php

class Solution
{
    /**
     * @param Integer[] $nums
     * @param Integer   $k
     *
     * @return Integer
     */
    public function findKthLargest($nums, $k)
    {
        $heap = new SplMaxHeap();

        foreach ($nums as $num) {
            $heap->insert($num);
        }

        for ($i = 0; $i < $k - 1; $i++) {
            $heap->extract();
        }

        return $heap->extract();
    }
}
