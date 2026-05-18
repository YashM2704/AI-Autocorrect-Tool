import language_tool_python


tool = language_tool_python.LanguageTool(
    'en-US'
)


def calculate_grammar_score(text):

    matches = tool.check(text)

    error_count = len(matches)

    # Fewer errors = higher score
    score = max(0, 1 - (error_count * 0.1))

    return round(score, 2)