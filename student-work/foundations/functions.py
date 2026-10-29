# Functions and returned values
# Write `intake_output(request, enabled, has_piece)` using your previous conditional. It should return a value rather than print inside the function. Call it for forward collection, a detected piece, reverse release, and disabled operation.
# Write your attempt below. See the course page for expected results.
def intake_output(request, enabled, has_piece):
    if not enabled:
        output = 0.0
    elif has_piece and request > 0.0:
        output = 0.0
    else:
        output = request
    return output

result = intake_output(-0.4, False, True)
print(result)

