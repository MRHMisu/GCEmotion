# one_line_commit = '4920616d206120636f6d6d6974206d6573736167652e'[2:]
# three_line_commit = "4920616d206120636f6d6d6974206d6573736167652e0d0a546869732069732074686520326e64206c696e652e0d0a5468697320697320337264206c696e652e"[
#                     2:]
#
# # p1 = CommitMessage(three_line_commit)
# p1 = CommitMessage(one_line_commit)
#
# # print(p1.to_string())
# print('Title=' + p1.get_commit_title())
# print('Body=' + p1.get_commit_body())
import sys

from filter.bugfix_commit_filter import contains_bug_fix_like_terms
from filter.refactor_commit_filter import contains_refactoring_like_terms


def test_buggy_commit_message():
    commit_message = "#3232 BUG asfdadf asfdadf #323234"
    contains_bug_fix_like_terms(commit_message)
    sys.exit()


test_buggy_commit_message()


def test_refactoring_commit_message():
    commit_message = "#3232 BUGsds asfdadf asfdadf #323234 Split Split"
    contains_refactoring_like_terms(commit_message)
    sys.exit()


test_refactoring_commit_message()