import re


def pre_process_line(line):
    return line.lower().strip()


def is_bug_fix_commit(commit_message):
    return contains_buggy_keywords(commit_message) or contains_bug_fix_like_terms(commit_message)


def contains_bug_or_issue_number(line):
    bug_number_pattern = "#(\\d+)"
    bug_or_issue_numbers = re.findall(bug_number_pattern, line)
    # print(bug_or_issue_numbers)
    if bug_or_issue_numbers:
        return True
    return False


def contains_buggy_keywords(line):
    keywords = {"bug", "bugs", "fix", "fixed", "fixing", "fixes", "patching", "patch",
                "patches", "patched", "close", "closed", "closing", "resolve", "resolves", "resolving", "resolved"}
    tokens = set(line.split())
    for kw in keywords:
        if kw in tokens:
            return True
    return False


def contains_bug_fix_like_terms(line):
    processed_line = pre_process_line(line)
    if contains_bug_or_issue_number(processed_line):
        if contains_buggy_keywords(processed_line):
            return True
    return False
