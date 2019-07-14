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
    const INT_MIN = -(2 ** 31);
    const INT_MAX = 2 ** 31 - 1;

    const INT_MAX_STR = '2147483647';
    const INT_MIN_STR = '2147483648';

    /**
     * @param string $str
     *
     * @return int
     */
    function myAtoi($str)
    {
        list($digits, $isNegative) = $this->extract($str);

        return $this->toi(join('', $digits), $isNegative);
    }

    /**
     * @param string $str
     *
     * @return array
     */
    protected function extract(string $str): array
    {
        $str = trim($str, ' ');

        $isNegative = false;
        $digits     = [];

        // Firstly, discard +/- sign and set corresponding flag
        if (($str[0] ?? null) === '+') {
            $str = substr($str, 1);
        }
        else if (($str[0] ?? null) === '-') {
            $str        = substr($str, 1);
            $isNegative = true;
        }

        if (empty($str)) {
            return [$digits, $isNegative];
        }

        // Remove leading 0
        foreach (str_split(ltrim($str, '0')) as $char) {
            if ($char < '0' || $char > '9') {
                break;
            }

            $digits[] = $char;
        }

        return [$digits, $isNegative];
    }

    /**
     * @param string $digits
     * @param bool   $isNegative
     *
     * @return int
     */
    protected function toi(string $digits, bool $isNegative): int
    {
        if (empty($digits)) {
            return 0;
        }

        $intMaxLen = strlen(self::INT_MIN_STR);
        $digit     = str_pad($digits, $intMaxLen, '0', STR_PAD_LEFT);
        if (strlen($digit) > $intMaxLen) {
            return $isNegative ? self::INT_MIN : self::INT_MAX;
        }

        $toCompare = $isNegative ? self::INT_MIN_STR : self::INT_MAX_STR;
        if (strcmp($digit, $toCompare) > 0) {
            return $isNegative ? self::INT_MIN : self::INT_MAX;
        }

        $value = (int) $digit;

        return $isNegative ? -1 * $value : $value;
    }
}
