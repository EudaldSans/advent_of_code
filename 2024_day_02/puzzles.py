from typing import List


def process_report(report: List[int]) -> List[int]:
    errors = list()
    position = 0

    report_descending = False
    report_ascending = False

    for prev_level, curr_level in zip(report, report[1:]):
        if abs(curr_level - prev_level) > 3:
            errors.append(position)

        if curr_level == prev_level:
            errors.append(position)

        if curr_level > prev_level:
            report_ascending = True
            if report_descending:
                report_descending = False
                errors.append(position)

        if curr_level < prev_level:
            report_descending = True
            if report_ascending:
                report_ascending = False
                errors.append(position)

        position += 1

    return errors


def main(data_file: str):
    with open(data_file, 'r') as f:
        data = f.readlines()
        data = [report.strip('\n').split(' ') for report in data]

    wrong_reports = list()

    for report in data:
        report = [int(level) for level in report]
        errors = process_report(report)

        if len(errors) > 0:
            wrong_reports.append([report, errors])

    safe_reports = len(data) - len(wrong_reports)
    print(f'Number of safe reports in part one is {safe_reports}')

    for report, errors in wrong_reports:
        report_dampened = False

        for pos in range(len(report)):
            dampened_report = [level for count, level in enumerate(report) if count != pos]
            if len(process_report(dampened_report)) == 0:
                print(f'Report {report} dampened by removing {report[pos]}')
                safe_reports += 1
                report_dampened = True
                break

        if not report_dampened:
            print(f'Report {report} with {errors} can not be dampened')

    print(f'Number of safe reports in part two is {safe_reports}')


if __name__ == '__main__':
    main('report_data.txt')

