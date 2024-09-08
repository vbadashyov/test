employees = [
    'Андрей 9',
    'Василий 11',
    'Роман 7',
    'X Æ A-12 45',
    'Иван Петров 3',
    'Андрей 6',
    'Роман 11'
]


if __name__ == "__main__":
    result = {}
    for employee in employees:
        name, hours = employee.rsplit(" ", 1)
        hours = int(hours)
        if name in result:
            result[name].append(hours)
        else:
            result[name] = [hours]

    for name in result.keys():
        print(f"{name} : { ', '.join(map(str, result[name]))};  sum: {sum(result[name])}")
