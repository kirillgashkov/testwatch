import datetime

from testwatch import export


#
# Low-level Input
#


def readline():
    s = input('>>> ').strip()
    return s or readline()


def ask(prompt):
    if prompt:
        print(prompt)
    s = readline().strip()
    return s


def confirm(prompt):
    s = ask(prompt).lower()
    if s in {'y', 'yes'}:
        return True
    if s in {'n', 'no'}:
        return False
    return confirm(prompt)


#
# Low-level Output
#


def raw(s):
    print(s)


def info(s):
    print(s)


def error(s):
    print(s)


#
# High-level Output
#


def print_report(report):
    print(f'[Human readable report]')
    print(f'')
    print(f'Start time (UTC): {format_date(report.start_time)}')
    print(f'End time (UTC): {format_date(report.end_time)}')
    print(f'---')

    for task in report.tasks:
        print(f'{task.name}: {format_time(task.duration())}')

    print(f'---')
    print(f'Total time spent: {format_time(report.total_time_spent())}')
    print(f'Time spent on starting: {format_time(report.time_spent_on_starting())}')
    print(f'Time spent on ending: {format_time(report.time_spent_on_ending())}')
    print(f'Time spent on tasks: {format_time(report.time_spent_on_tasks())}')
    print(f'Time spent on breaks: {format_time(report.time_spent_on_breaks())}')

    print(f'')
    print(f'[TSV report]')
    print(f'')
    print(export.report_to_tsv(report))


#
# Formatters
#


def format_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    h_str = f'{h}h ' if h else ''
    m_str = f'{m}m ' if m else ''
    s_str = f'{s}s'

    return h_str + m_str + s_str


def format_date(unix):
    fmt = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.utcfromtimestamp(unix).strftime(fmt)
