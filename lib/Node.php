<?php

/**
 * Class Node
 */
class Node
{
    /**
     * @var int
     */
    public $val;

    /**
     * @var Node|null
     */
    public $left;

    /**
     * @var Node|null
     */
    public $right;

    /**
     * @var Node|null
     */
    public $next;

    /* @param Integer $val
     * @param Node|null $left
     * @param Node|null $right
     * @param Node|null $next
     */
    function __construct($val, $left, $right, $next)
    {
        $this->val   = $val;
        $this->left  = $left;
        $this->right = $right;
        $this->next  = $next;
    }
}