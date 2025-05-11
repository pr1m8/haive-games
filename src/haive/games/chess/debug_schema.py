"""Debug script for chess game validation models.

This script prints the validation models and field requirements
for better debugging of validation errors.
"""

import inspect
from typing import get_args, get_origin

from haive.games.chess.models import ChessPlayerDecision, SegmentedAnalysis
from haive.games.chess.state import ChessState


def debug_field(field_name, model_class):
    """Debug a specific field in a model class."""
    print(f"\n{'='*50}")
    print(f"Field: {field_name}")

    if hasattr(model_class, "__annotations__"):
        annotations = model_class.__annotations__
        if field_name in annotations:
            field_type = annotations[field_name]
            print(f"Type annotation: {field_type}")

            # Check if it's a complex type
            origin = get_origin(field_type)
            args = get_args(field_type)
            if origin:
                print(f"Origin: {origin}")
                print(f"Type args: {args}")

    # Check field definition
    if hasattr(model_class, "model_fields") and field_name in model_class.model_fields:
        field_info = model_class.model_fields[field_name]
        print(f"Field info: {field_info}")

        # Check validators
        if hasattr(field_info, "field_validators"):
            print(f"Validators: {field_info.field_validators}")

        # Check default values
        if hasattr(field_info, "default"):
            print(f"Default: {field_info.default}")


def main():
    """Run debug analysis on the chess models."""
    print("Debugging Chess State Models")
    print("===========================\n")

    print("ChessState Fields:")
    for field_name in ChessState.model_fields:
        debug_field(field_name, ChessState)

    print("\nChessPlayerDecision Fields:")
    for field_name in ChessPlayerDecision.model_fields:
        debug_field(field_name, ChessPlayerDecision)

    print("\nSegmentedAnalysis Fields:")
    for field_name in SegmentedAnalysis.model_fields:
        debug_field(field_name, SegmentedAnalysis)

    # Check computed fields as well
    print("\nComputed Fields in ChessState:")
    for name, method in inspect.getmembers(ChessState):
        if name.startswith("__"):
            continue
        if hasattr(method, "__is_computed_field"):
            print(f"Computed field: {name}")
            print(f"  Return type: {method.__annotations__.get('return')}")

    # Print the complete models for reference
    print("\nComplete Models:")
    print(f"ChessState: {ChessState.model_json_schema()}")
    print(f"ChessPlayerDecision: {ChessPlayerDecision.model_json_schema()}")
    print(f"SegmentedAnalysis: {SegmentedAnalysis.model_json_schema()}")


if __name__ == "__main__":
    main()
