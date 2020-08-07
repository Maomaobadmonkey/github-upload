def heading(word, num=0):
    if num is None:
        return "# " + word
    if num <= 1:
        return "# " + word
    if num == 2:
        return "## " + word
    if num == 3:
        return "### " + word
    if num == 4:
        return "#### " + word
    if num == 5:
        return "##### " + word
    else:
        return "###### " + word
