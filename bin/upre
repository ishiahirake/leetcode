#!/usr/bin/env python3

import re
from collections import namedtuple
from glob import glob
from os import path, linesep

root_dir = path.dirname(path.dirname(path.realpath(__file__)))

solution_orders = ['py', 'php', 'js']
solution_languages = {
    'py': 'Python',
    'php': 'PHP',
    'js': 'JS'
}

word_transforms = {
    'upper': ['ii', 'bst'],
    'none': ['a', 'an', 'to', 'in', 'II', 'of', 'k', 'from', 'and', 'BST'],
}

languages = {
    "python": {
        "target": "./python/solutions/*.py",
        "exclusive": ".*test.py"
    },
    "php": {
        "target": "./php/src/*.php",
    },
    "js": {
        "target": "./js/src/*.js",
    },
}

Solution = namedtuple(
    'Solution',
    ['pid', 'title', 'language', 'relative_path']
)


def normalize_title(title: str) -> str:
    words = title.split('_')

    def transform_word(word: str) -> str:
        if word in word_transforms.get("none"):
            return word
        elif word in word_transforms.get("upper"):
            return word.upper()
        else:
            return word.capitalize()

    return ' '.join(map(transform_word, words))


def make_solution(filepath: str):
    filename = path.basename(filepath)
    match = re.match(r'.*?(\d{1,4})[_]?([^\.]*)\.(.*)', filename)
    if not match:
        return None
    pid, title, suffix = match.groups()

    return Solution(pid=pid, title=normalize_title(title),
                    language=suffix, relative_path=filepath.replace(root_dir, "."))


def get_current_solutions() -> dict:
    solutions = {}

    for _, config in languages.items():
        language_path = path.realpath(
            path.join(root_dir, config.get("target")))
        exclusive = config.get("exclusive")
        for filepath in glob(language_path):
            filename = path.basename(filepath)
            if exclusive and re.match(exclusive, filename):
                continue
            solution = make_solution(filepath)
            if not solution:
                continue
            if solution.pid not in solutions:
                solutions[solution.pid] = []
            solutions.get(solution.pid).append(solution)

    return solutions


def nsl(language: str) -> str:
    return solution_languages.get(language)


def make_solution_line(solutions: [Solution]) -> str:
    solutions.sort(key=lambda s: solution_orders.index(s.language))
    solution = solutions[0]
    title_text = f"- **{solution.pid}. {solution.title}**:"

    solutions_text = ' '.join(
        map(lambda s: f"[[{nsl(s.language)}]]({s.relative_path})", solutions))

    return title_text + ' ' + solutions_text


def write_solutions(solutions: dict):
    lines = """# Leetcode

Solutions for [leetcode](https://leetcode.com/).

## Solutions

""".splitlines()

    for pid in sorted(solutions.keys()):
        lines.append(make_solution_line(solutions.get(pid)))

    infos = """
## Info

- [What are the environments for the programming languages?](https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages)
""".splitlines()
    for info in infos:
        lines.append(info)

    readme = open(path.realpath(path.join(root_dir, 'README.md')), 'w')
    readme.writelines(map(lambda l: l + linesep, lines))
    readme.close()


write_solutions(get_current_solutions())
