from gendiff import generate_diff
import pytest


@pytest.mark.parametrize(
    ("argument1", "argument2", "expected"),
    (
            pytest.param(
                "fixtures/file1.json",
                "fixtures/file2.json",
                "fixtures/correct_flat_result.txt",
                id='flat_json'),
            pytest.param(
                "fixtures/file1.yaml",
                "fixtures/file2.yaml",
                "fixtures/correct_flat_result.txt",
                id='flat_yaml'),
            pytest.param(
                "fixtures/file1_tree.json",
                "fixtures/file2_tree.json",
                "fixtures/correct_recursive_result.txt",
                id='tree_json'),
            pytest.param(
                "fixtures/file1_tree.yaml",
                "fixtures/file2_tree.yaml",
                "fixtures/correct_recursive_result.txt",
                id='tree_yaml'),
    ),
)
def test_generate_diff(argument1, argument2, expected):
    with open(expected) as result_file:
        expected_result = result_file.read()
        assert generate_diff(argument1, argument2) == expected_result
