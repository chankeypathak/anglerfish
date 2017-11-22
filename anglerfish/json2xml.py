#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Convert JSON to XML."""


from collections import deque


def json2xml(json_obj: dict, line_padding: str="", at_end: str="") -> str:
    """Convert JSON to XML."""
    result_deque, json_obj_type = deque(), type(json_obj)
    _resultapend = result_deque.append  # Optimization.
    if json_obj_type is list:
        for sub_elem in json_obj:
            _resultapend(json2xml(sub_elem, line_padding))
        return "\n".join(result_deque)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            _resultapend(f"{ line_padding }<{ tag_name }>")
            _resultapend(json2xml(sub_obj, "    " + line_padding))
            _resultapend(f"{ line_padding }</{ tag_name }>{ at_end }")
        return "\n".join(result_deque)

    return f"{ line_padding }{ json_obj }"
