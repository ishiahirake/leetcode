from typing import List


def normalize_email(email: str) -> str:
    local, host = email.split('@')
    letters = []
    for char in local:
        if char == '+':
            break
        if char == '.':
            continue
        letters.append(char)
    return ''.join(letters) + '@' + host


class Solution:
    """
    929. Unique Email Addresses.

    :see https://leetcode.com/problems/unique-email-addresses/
    """

    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            unique_emails.add(normalize_email(email))
        return len(unique_emails)
