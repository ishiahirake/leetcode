<?php

class Solution
{
    /**
     * @param int[] $nums
     *
     * @return int[]
     */
    public function sortArray($nums)
    {
        $nums = $nums ?? [];
        shuffle($nums);
        return $this->quickSort($nums);
    }

    /**
     * @param array|null $nums
     *
     * @return array
     */
    public function quickSort(array $nums)
    {
        if (count($nums) < 2) {
            return $nums;
        }

        $pivot = $nums[0];

        $less = array_values(array_filter(array_slice($nums, 1), function ($num) use ($pivot) {
            return $num <= $pivot;
        }));

        $greater = array_values(
            array_filter(array_slice($nums, 1), function ($num) use ($pivot) {
                return $num > $pivot;
            })
        );

        return array_merge($this->quickSort($less), [$pivot], $this->quickSort($greater));
    }
}
