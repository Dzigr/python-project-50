import pytest
from gendiff import generate_diff



RESULT_STYLISH_FLAT = 'tests/fixtures/correct_flat_result_stylish'
RESULT_STYLISH_TREE = 'tests/fixtures/correct_recursive_result_stylish'
RESULT_PLAIN_FLAT = 'tests/fixtures/correct_flat_result_plain'
RESULT_PLAIN_TREE = 'tests/fixtures/correct_recursive_result_plain'
RESULT_JSON_FLAT = 'tests/fixtures/correct_flat_result_json'
RESULT_JSON_TREE = 'tests/fixtures/correct_recursive_result_json'
JSON_FLAT_FILE1 = 'tests/fixtures/file1.json'
JSON_FLAT_FILE2 = 'tests/fixtures/file2.json'
YAML_FLAT_FILE1 = 'tests/fixtures/file1.yaml'
YAML_FLAT_FILE2 = 'tests/fixtures/file2.yaml'
YML_FLAT_FILE1 = 'tests/fixtures/file1.yml'
YML_FLAT_FILE2 = 'tests/fixtures/file2.yml'
JSON_TREE_FILE1 = 'tests/fixtures/file1_tree.json'
JSON_TREE_FILE2 = 'tests/fixtures/file2_tree.json'
YAML_TREE_FILE1 = 'tests/fixtures/file1_tree.yaml'
YAML_TREE_FILE2 = 'tests/fixtures/file2_tree.yaml'
YML_TREE_FILE1 = 'tests/fixtures/file1_tree.yml'
YML_TREE_FILE2 = 'tests/fixtures/file2_tree.yml'

FORMATTERS = (
    'stylish',
    'plain',
    'json',
)


@pytest.mark.parametrize(
    ('argument1', 'argument2', 'formatter', 'expected'),
    (
            (JSON_FLAT_FILE1, JSON_FLAT_FILE2, FORMATTERS[0], RESULT_STYLISH_FLAT),
            (YAML_FLAT_FILE1, YAML_FLAT_FILE2, FORMATTERS[0], RESULT_STYLISH_FLAT),
            (YML_FLAT_FILE1, YML_FLAT_FILE2, FORMATTERS[0], RESULT_STYLISH_FLAT),
            (JSON_TREE_FILE1, JSON_TREE_FILE2, FORMATTERS[0], RESULT_STYLISH_TREE),
            (YAML_TREE_FILE1, YAML_TREE_FILE2, FORMATTERS[0], RESULT_STYLISH_TREE),
            (YML_TREE_FILE1, YML_TREE_FILE2, FORMATTERS[0], RESULT_STYLISH_TREE),
            (JSON_FLAT_FILE1, JSON_FLAT_FILE2, FORMATTERS[1], RESULT_PLAIN_FLAT),
            (YAML_FLAT_FILE1, YAML_FLAT_FILE2, FORMATTERS[1], RESULT_PLAIN_FLAT),
            (YML_FLAT_FILE1, YML_FLAT_FILE2, FORMATTERS[1], RESULT_PLAIN_FLAT),
            (JSON_TREE_FILE1, JSON_TREE_FILE2, FORMATTERS[1], RESULT_PLAIN_TREE),
            (YAML_TREE_FILE1, YAML_TREE_FILE2, FORMATTERS[1], RESULT_PLAIN_TREE),
            (YML_TREE_FILE1, YML_TREE_FILE2, FORMATTERS[1], RESULT_PLAIN_TREE),
            (JSON_FLAT_FILE1, JSON_FLAT_FILE2, FORMATTERS[2], RESULT_JSON_FLAT),
            (YAML_FLAT_FILE1, YAML_FLAT_FILE2, FORMATTERS[2], RESULT_JSON_FLAT),
            (YML_FLAT_FILE1, YML_FLAT_FILE2, FORMATTERS[2], RESULT_JSON_FLAT),
            (JSON_TREE_FILE1, JSON_TREE_FILE2, FORMATTERS[2], RESULT_JSON_TREE),
            (YAML_TREE_FILE1, YAML_TREE_FILE2, FORMATTERS[2], RESULT_JSON_TREE),
            (YML_TREE_FILE1, YML_TREE_FILE2, FORMATTERS[2], RESULT_JSON_TREE),
    ),
)
def test_generate_diff(argument1, argument2, formatter, expected):
    with open(expected) as result_file:
        expected_result = result_file.read()
        assert generate_diff(argument1, argument2, formatter) == expected_result
