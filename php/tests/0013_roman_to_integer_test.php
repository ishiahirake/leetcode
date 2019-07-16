<?php


class p0013_roman_to_integer_test extends TestCase
{
    /**
     * @var Solution
     */
    protected $solution;

    /**
     * Normal test case.
     */
    public function testNormal()
    {
        $this->assertEquals(3, $this->solution->romanToInt('III'));
        $this->assertEquals(58, $this->solution->romanToInt('LVIII'));
    }

    /**
     * Irregular test case.
     */
    public function testIrregular()
    {
        $this->assertEquals(4, $this->solution->romanToInt('IV'));
        $this->assertEquals(9, $this->solution->romanToInt('IX'));
        $this->assertEquals(1994, $this->solution->romanToInt('MCMXCIV'));
    }

    /**
     *
     */
    protected function setUp(): void
    {
        $this->solution = new Solution();
    }
}