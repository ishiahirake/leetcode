<?php

/**
 * Class TestCase
 */
class TestCase extends \PHPUnit\Framework\TestCase
{
    /**
     */
    public static function setUpBeforeClass(): void
    {
        self::loadSourceIfExists();
    }

    /**
     */
    protected static function loadSourceIfExists()
    {
        $found = preg_match('/^p(.*?)_test$/', static::class, $matches);
        if ($found && is_file($source = "../src/${matches[1]}.php")) {
            /** @noinspection PhpIncludeInspection */
            require_once $source;
        }
    }
}