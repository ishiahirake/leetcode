#!/usr/bin/env python3

import re
from collections import namedtuple
from glob import glob
from os import path, linesep
from difflib import SequenceMatcher
from functools import reduce

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
            m = re.match(r'([\d]*)(\w+)', word)
            fst, sec = ('', word) if not m else m.groups()
            return fst + sec.capitalize()

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


def find_longest_match(str1: str, str2: str) -> str:
    s = SequenceMatcher(a=str1, b=str2)
    m = s.find_longest_match(0, len(str1), 0, len(str2))
    return '' if m.size == 0 else str1[m.a:m.a+m.size]


def resolve_solution_title(solutions: [Solution]) -> str:
    titles = list(map(lambda s: s.title, set(solutions)))
    if len(titles) == 1:
        return titles[0]
    title = reduce(find_longest_match, titles).strip()
    m = re.match(r'(.*)\s\w$', title)
    return title if not m else m.group(1)


def nsl(s: Solution, title: str) -> str:
    language = solution_languages.get(s.language)
    if s.title == title:
        return language
    tag = s.title.replace(title, '')
    return f'{language}({tag.strip()})'


def make_solution_line(solutions: [Solution]) -> str:
    solutions.sort(key=lambda s: solution_orders.index(s.language))
    title = resolve_solution_title(solutions)
    title_text = f"- **{solutions[0].pid}. {title}**:"

    solutions_text = ' '.join(
        map(lambda s: f"[[{nsl(s, title)}]]({s.relative_path})", solutions))

    return title_text + ' ' + solutions_text


def write_solutions(solutions: dict):
    content = ''
    with open(path.realpath(path.join(root_dir, 'README.tpl.md')), 'r') as tpl:
        content = tpl.read()

    solution_lines = []
    for pid in sorted(solutions.keys()):
        solution_lines.append(make_solution_line(solutions.get(pid)))
    bindings = {'solutions': linesep.join(solution_lines)}
    content = content.format_map(bindings)

    with open(path.realpath(path.join(root_dir, 'README.md')), 'w') as readme:
        readme.write(content)


write_solutions(get_current_solutions())
