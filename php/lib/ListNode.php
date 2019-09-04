<?php


class ListNode
{
    public $val  = 0;

    /** @var ListNode|null */
    public $next = null;

    function __construct($val)
    {
        $this->val = $val;
    }
}