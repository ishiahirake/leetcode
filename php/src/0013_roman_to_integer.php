<?php

/**
 * 13. Roman to Integer.
 *
 * @see https://leetcode.com/problems/roman-to-integer/
 */
class Solution
{
    /**
     * @var array
     */
    protected $romanIntegers = [
        'I' => 1,
        'V' => 5,
        'X' => 10,
        'L' => 50,
        'C' => 100,
        'D' => 500,
        'M' => 1000,
    ];

    /**
     * @param string $s
     *
     * @return int
     */
    public function romanToInt($s)
    {
        $integer = 0;

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($i + 1 === $len) {
                $integer += $this->romanInt($s[$i]);
                continue;
            }

            $curr = $this->romanInt($s[$i]);
            $next = $this->romanInt($s[$i + 1]);

            if ($curr >= $next) {
                $integer += $curr;
            }
            else {
                $integer += ($next - $curr);
                $i++;
            }
        }

        return $integer;
    }

    /**
     * @param string $numeral
     *
     * @return int
     */
    protected function romanInt(string $numeral): int
    {
        return $this->romanIntegers[$numeral];
    }
}
