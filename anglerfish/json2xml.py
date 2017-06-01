#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Convert JSON to XML."""


def json2xml(json_obj, line_padding="", at_end=""):
    """Convert JSON to XML."""
    result_list, json_obj_type = [], type(json_obj)
    _resultapend = result_list.append  # Optimization.
    if json_obj_type is list:
        for sub_elem in json_obj:
            _resultapend(json2xml(sub_elem, line_padding))
        return "\n".join(result_list)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            _resultapend("{0}<{1}>".format(line_padding, tag_name))
            _resultapend(json2xml(sub_obj, "    " + line_padding))
            _resultapend("{0}</{1}>{2}".format(line_padding, tag_name, at_end))
        return "\n".join(result_list)

    return "{0}{1}".format(line_padding, json_obj)
