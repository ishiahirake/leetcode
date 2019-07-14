<?php

/**
 * 8. String to Integer (atoi).
 *
 * @see https://leetcode.com/problems/string-to-integer-atoi/
 *
 * TestCase:
 *
 * // "  0000000000012345678"
 * // "+-2"
 * // "3.14159"
 * // "+1"
 * // "010"
 * // "2147483648"
 */
class Solution
{
    const INT_MIN = -2147483648;
    const INT_MAX = 2147483647;

    /**
     * @param string $str
     *
     * @return int
     */
    function myAtoi($str)
    {
        return $this->toi($this->extract($str));
    }

    /**
     * @param string $digit
     *
     * @return int
     */
    protected function toi(string $digit): int
    {
        $floatDigit = (float) $digit;

        if ($floatDigit < self::INT_MIN) {
            return self::INT_MIN;
        }

        if ($floatDigit > self::INT_MAX) {
            return self::INT_MAX;
        }

        return (int) $digit;
    }

    /**
     * @param string $str
     *
     * @return string
     */
    protected function extract(string $str): string
    {
        $str = trim($str, ' ');

        $digits = [];

        // Firstly, extract +/- sign if it exists
        if (in_array($sign = ($str[0] ?? null), ['-', '+'])) {
            $digits[] = $sign;
            $str      = substr($str, 1);
        }

        if (empty($str)) {
            return '0';
        }

        // Remove leading 0
        foreach (str_split(ltrim($str, '0')) as $char) {
            if ($char < '0' || $char > '9') {
                break;
            }

            $digits[] = $char;
        }

        return join('', $digits);
    }
}
