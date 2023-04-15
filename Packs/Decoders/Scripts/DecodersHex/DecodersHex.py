"""Base Script for Cortex XSOAR (aka Demisto)

This is an empty script with some basic structure according
to the code conventions.

MAKE SURE YOU REVIEW/REPLACE ALL THE COMMENTS MARKED AS "TODO"

Developer Documentation: https://xsoar.pan.dev/docs/welcome
Code Conventions: https://xsoar.pan.dev/docs/integrations/code-conventions
Linting: https://xsoar.pan.dev/docs/integrations/linting

"""

from typing import Any, Dict

import demistomock as demisto
from CommonServerPython import *
from CommonServerUserPython import *

""" STANDALONE FUNCTION """


# TODO: REMOVE the following dummy function:
def decoders_hex(encoded_text: str, to: str = 'utf-8') -> str:
    decode = bytes.fromhex(encoded_text).decode(to)
    return str(decode)




""" COMMAND FUNCTION """


def decoders_hex_command(args: Dict[str, Any]) -> CommandResults:

    encoded_text = args.get("encoded", None)
    decode_to = args.get("to", None)

    if not encoded_text:
        raise ValueError("Encoded text not specified")

    result = decoders_hex(encoded_text=encoded_text, to=decode_to)

    result_dict  = {
        "Decoded": result,
        "Encoded": encoded_text,
        "Encoder": "HEX",
        "Decoded-To": decode_to
    }
    return CommandResults(
        outputs_prefix="Decoders",
        outputs_key_field="",
        outputs=result_dict,
    )



""" MAIN FUNCTION """


def main():
    try:
        return_results(decoders_hex_command(demisto.args()))
    except Exception as ex:
        return_error(f"Failed to execute DecodersHex. Error: {str(ex)}")


""" ENTRY POINT """


if __name__ in ("__main__", "__builtin__", "builtins"):  # pragma: no cover
    main()
