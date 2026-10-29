# Checking behavior with assertions
# Add clamping to your intake function. Write assertions for forward/no piece, forward/held piece, reverse/held piece, disabled, and requests outside both bounds.
# Write your attempt below. See the course page for expected results.
def clamp_request(request):
    if request > 1.0:
        return 1.0
    if request < -1.0:
        return -1.0
    return request
def intake_output(request, enabled, has_piece):
    request = clamp_request(request)
    if not enabled:
        output = 0.0
    elif has_piece and request > 0.0:
        output = 0.0
    else:
        output = request
    return output

assert intake_output(0.5, True, False) == 0.5
assert intake_output(0.5, True, True) == 0.0
assert intake_output(-0.5, True, True) == -0.5
assert intake_output(1.5, True, False) == 1.0
assert intake_output(-1.5, True, False) == -1.0
print("All request checks passed.")
