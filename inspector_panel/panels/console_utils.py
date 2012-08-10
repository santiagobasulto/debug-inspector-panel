MINIMUM_WIDTH = 22
TITLE = "Debug Info"
RIGHT_PADDING = 2


def console_debug(record):
    val = generate_line("Value", record.value)
    clas = generate_line("Class", record.class_name)
    module_name = generate_line("Module Name: ", record.module_name)
    width = longest_line_width([val, clas, module_name]) + RIGHT_PADDING
    print_title(width)
    print_complete(val, width)
    print_complete(clas, width)
    print_complete(module_name, width)
    print_ending(width)


def print_title(width):
    free_space = width - (len(TITLE) + 2)
    to_left = free_space / 2
    if free_space % 2 == 0:
        to_right = to_left
    else:
        to_right = to_left - 1
    print "%s %s %s" % ("#" * to_left, TITLE, "#" * to_right)


def print_complete(line, width):
    completed_line = line
    if len(line) < width:
        to_complete = width - len(line) - 1
        completed_line = "%s%s%s" % (line, " " * to_complete, "#")
    print completed_line


def print_ending(width):
    print "#" * width


def generate_line(title, value):
    return "# %s: %s" % (title, value)


def longest_line_width(lines):
    max_width = MINIMUM_WIDTH
    for l in lines:
        if len(l) > max_width:
            max_width = len(l)
    return max_width
