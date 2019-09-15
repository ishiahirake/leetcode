<?php

class KthLargest
{
    /**
     * @var int
     */
    protected $k;

    /**
     * @var SplMinHeap
     */
    protected $heap;

    /**
     * @param int   $k
     * @param int[] $nums
     */
    public function __construct($k, $nums)
    {
        $this->k    = $k;
        $this->heap = new SplMinHeap();

        foreach ($nums as $num) {
            $this->add($num);
        }
    }

    /**
     * @param Integer $val
     *
     * @return Integer
     */
    public function add($val)
    {
        if ($this->heap->count() >= $this->k) {
            if ($this->heap->top() < $val) {
                $this->heap->extract();
                $this->heap->insert($val);
            }
        }
        else {
            $this->heap->insert($val);
        }
        return $this->heap->top();
    }
}