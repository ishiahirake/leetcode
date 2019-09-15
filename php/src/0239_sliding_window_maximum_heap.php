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
        $heap = new SplMaxHeap();
        list($result, $counter) = [[], []];

        foreach ($nums as $idx => $num) {
            $heap->insert($num);
            $counter[$num] = ($counter[$num] ?? 0) + 1;
            while (!$counter[$heap->top()]) {
                $heap->extract();
            }
            if ($idx >= $k - 1) {
                $result[] = $heap->top();
                $counter[$nums[$idx - $k + 1]]--;
            }
        }

        return $result;
    }
}
