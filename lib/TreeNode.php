<?php

/**
 * Class TreeNode
 */
class TreeNode
{
    /**
     * @var mixed|null
     */
    public $val = null;

    /**
     * @var TreeNode|null
     */
    public $left = null;

    /**
     * @var TreeNode|null
     */
    public $right = null;

    /**
     * TreeNode constructor.
     *
     * @param mixed $value
     */
    function __construct($value)
    {
        $this->val = $value;
    }
}