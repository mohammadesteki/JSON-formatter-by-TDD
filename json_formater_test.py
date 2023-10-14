import json
import unittest

import json_formater


class MyTestCase(unittest.TestCase):
    def test_empty_string(self):
        formatted_string = json_formater.validate_and_format_json_string("")
        self.assertEqual(formatted_string, "")

    def test_empty_brace(self):
        formatted_string = json_formater.validate_and_format_json_string("{}")
        self.assertEqual(formatted_string, "{\n}")

    def test_string_without_opening_brace(self):
        formatted_string = json_formater.validate_and_format_json_string("a}")
        self.assertEqual(formatted_string, "Invalid json string")

    def test_one_key_one_value(self):
        formatted_string = json_formater.validate_and_format_json_string("{  \"a\" : \"b\" }")
        self.assertEqual(formatted_string, "{\n\t\"a\":\"b\"\n}")

    def test_one_level_key_values(self):
        formatted_string = json_formater.validate_and_format_json_string("{\"a\":\"b\",\"c\":\"d\",\"e\":\"f\"}")
        self.assertEqual(formatted_string, "{\n\t\"a\":\"b\",\n\t\"c\":\"d\",\n\t\"e\":\"f\"\n}")

    def test_one_key_one_int_value(self):
        formatted_string = json_formater.validate_and_format_json_string("{  \"a\" : 36}")
        self.assertEqual(formatted_string, "{\n\t\"a\":36\n}")

    def test_key_with_list_value(self):
        formatted_string = json_formater.validate_and_format_json_string("{\"a\":[36 ,\"b\",44]}")
        self.assertEqual(formatted_string, "{\n\t\"a\":[\n\t\t36,\n\t\t\"b\",\n\t\t44\n\t]\n}")

    def test_key_with_dict_value(self):
        formatted_string = json_formater.validate_and_format_json_string("{\"a\":{\"b\":\"c\",\"d\":34}}")
        self.assertEqual(formatted_string, "{\n\t\"a\":{\n\t\t\"b\":\"c\",\n\t\t\"d\":34\n\t}\n}")

    def test_all_together(self):
        formatted_string = json_formater.validate_and_format_json_string("{\"a\":{\"b\":{\"z\":{\"w\":123}},\"d\":34}}")
        ans = "{\n\t\"a\":{\n\t\t\"b\":{\n\t\t\t\"z\":{\n\t\t\t\t\"w\":123\n\t\t\t}\n\t\t},\n\t\t\"d\":34\n\t}\n}"
        self.assertEqual(formatted_string, ans)

