import re


def parse_headings(line):
    heading = re.search("^#+", line)
    if heading:
        heading_lvl = heading.group().count("#")
        line = f"<h{heading_lvl}>{line[heading_lvl+1:]}</h{heading_lvl}>"
    return line


def parse_strong(line):
    strong_occurrences = line.count("**")
    for _ in range(strong_occurrences):
        line = line.replace("**", "<strong>", 1)
        line = line.replace("**", "</strong>", 1)
    return line


def parse_em_ul(line, in_list_append):
    asterisk_count = line.count("*")
    if (asterisk_count % 2 == 1 or in_list_append) and line.startswith("*"):
        line = line.replace("* ", "<li>", 1) + "</li>"
        asterisk_count -= 1
        if not in_list_append:
            line = "<ul>" + line
            in_list_append = True
    elif in_list_append:
        line = "</ul>" + parse_para(line)
        in_list_append = False
    if asterisk_count % 2 == 0:
        for _ in range(asterisk_count):
            line = line.replace("*", "<em>", 1)
            line = line.replace("*", "</em>", 1)
    return line, in_list_append


def parse_para(line):
    if all(tag not in line for tag in ["<h", "<li>", "<p>"]):
        line = f"<p>{line}</p>"
    return line


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list_append = False
    for line in lines:

        # Replacement for easy formatting
        line = line.replace("_", "*")

        line = parse_headings(line)
        line = parse_strong(line)
        line, in_list_append = parse_em_ul(line, in_list_append)
        line = parse_para(line)

        res += line

    if in_list_append:
        res += "</ul>"

    return res
