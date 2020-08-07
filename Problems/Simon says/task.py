def what_to_do(instructions):
    if instructions.startswith('Simon says') or instructions.endswith('Simon says'):
        response = 'I ' + instructions.replace('Simon says', "").strip()
    else:
        response = "I won't do it!"
    return response