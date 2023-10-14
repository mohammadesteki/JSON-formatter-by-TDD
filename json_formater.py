import json


def validate_and_format_json_string(input_json_string):
    input_json_string = remove_all_blank(input_json_string)
    if is_empty(input_json_string):
        return ""
    try:
        json.loads(input_json_string)
        return format_json_string(input_json_string, 0)
    except:
        return "Invalid json string"


def format_json_string(input_json_string, level):
    dictionary = json.loads(input_json_string)

    pretty_json_string = ""
    for key in dictionary:
        if len(pretty_json_string) > 0:
            pretty_json_string = pretty_json_string + ","
        pretty_json_string = pretty_json_string+add_indent(level+1)+add_key(key)+add_value(dictionary[key], level+1)

    return "{" + pretty_json_string + add_indent(level) + "}"


def is_valid(input_json_string):
    if input_json_string[0] != '{':
        return False
    else:
        return True


def is_empty(input_json_string):
    if len(input_json_string) == 0:
        return True
    else:
        return False


def remove_all_blank(input_json_string):
    return remove_all_tabs(remove_all_lines(remove_all_spaces(input_json_string)))


def remove_all_spaces(input_json_string):
    return input_json_string.replace(" ", "")


def remove_all_lines(input_json_string):
    return input_json_string.replace("\n", "")


def remove_all_tabs(input_json_string):
    return input_json_string.replace("\t", "")


def add_str_value(value):
    if type(value) == str:
        return "\"" + value + "\""
    else:
        return ""


def add_number_value(value):
    if type(value) == int or type(value) == float:
        return str(value)
    else:
        return ""


def add_list_value(value, level):
    pretty_json_list = ""
    if type(value) == list:
        for item in value:
            if len(pretty_json_list) > 0:
                pretty_json_list = pretty_json_list + ","
            pretty_json_list = pretty_json_list + add_indent(level) + add_value(item, level + 1)
        return "[" + pretty_json_list + add_indent(level-1) + "]"
    else:
        return ""


def add_dict_value(value, level):
    if type(value) == dict:
        return format_json_string(json.dumps(value), level)
    else:
        return ""


def add_value(value, level):
    return add_str_value(value)+add_number_value(value)+add_list_value(value, level+1)+add_dict_value(value, level)


def add_indent(level):
    return "\n" + "\t" * level


def add_key(key):
    return "\"" + key + "\":"
