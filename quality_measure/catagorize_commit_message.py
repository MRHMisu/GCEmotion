import configparser
import csv
from io import TextIOWrapper
from zipfile import ZipFile
from filter.bugfix_commit_filter import is_bug_fix_commit
from filter.commit_message import CommitMessage
import sys

from filter.refactor_commit_filter import is_refactoring_commit
from quality_measure.syntactic_quality_measure import get_normalized_commit_score

config = configparser.ConfigParser()
config.read('../gcemotion.config.txt')
base_data_zip_file = config.get('DEFAULT', 'base_data_zip_file')
base_data_csv_file = config.get('DEFAULT', 'base_data_csv_file')
output_refactor_commit_file = config.get('DEFAULT', 'output_refactor_commit_file')
output_bugfix_commit_file = config.get('DEFAULT', 'output_bugfix_commit_file')
output_others_commit_file = config.get('DEFAULT', 'output_others_commit_file')


def load_data():
    bug_lines = []
    refactor_lines = []
    others_lines = []
    csv.field_size_limit(sys.maxsize)
    with ZipFile(base_data_zip_file) as zf:
        with zf.open(base_data_csv_file, 'r') as infile:
            reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
            count = 0
            for row in reader:
                # process the CSV here
                count += 1
                print("count: "+str(count))
                try:
                    if row:
                        commit_message = CommitMessage(row[0])
                        normalized_score = get_normalized_commit_score(row[0])
                        if is_bug_fix_commit(commit_message.to_string()):
                            bug_lines.append(str(normalized_score) + "," + "Bug" + "," + row[0])
                        elif is_refactoring_commit(commit_message.to_string()):
                            refactor_lines.append(str(normalized_score) + "," + "Refactor" + "," + row[0])
                        else:
                            others_lines.append(str(normalized_score) + "," + "Others" + "," + row[0])
                except Exception:
                    print("UnicodeError>>" + row[0])

    write_to_file(bug_lines, output_bugfix_commit_file)
    write_to_file(refactor_lines, output_refactor_commit_file)
    write_to_file(others_lines, output_others_commit_file)


def write_to_file(lines, path):
    joined_string = "\n".join(lines)
    with open(path, 'w') as f:
        f.writelines(joined_string)


load_data()
