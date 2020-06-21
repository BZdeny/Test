line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLecl' \
       'MwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWux' \
       'IhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQWrMMsYpLtdqRltXPqcSMXJ' \
       'IvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZy' \
       'wYkmjCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCuUJmG' \
       'YJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnu' \
       'yEZIheApQGOXWeXoLWiDQNJFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHf' \
       'yHNGmkNqSwXUrxgc'


# 2.1


def regular_lower_case(element):
    import re
    three_letters = re.findall(r'(?<=[A-Z])[a-z](?=[A-Z])', element)
    result = ''.join(three_letters)
    return result


print('Символы в нижнем регистре с помощью re: ')
print(regular_lower_case(line))


def lower_case(element):
    x = 0
    new_array = []
    for i in element:
        if element[x].isupper() and element[x+2].isupper() and element[x+1].islower():
            new_array.append(element[x+1])
            ''.join(new_array)
        x += 1
        if x == len(element) or (x == len(element)-1):
            break
    result = ''.join(new_array)
    return result


print('Символы в нижнем регистре без re: ')
print(lower_case(line))


# 2.2


def regular_upper_case(element):
    import re
    three_letters = re.findall(r'(?<=[a-z]{2})[A-Z](?=[A-Z]{2})', element)
    result = ''.join(three_letters)
    return result


print('Символы в верхнем регистре с помощью re: ')
print(regular_upper_case(line))


def upper_case(element):
    x = 0
    new_array = []
    for i in element:
        if element[x].islower() and element[x+1].islower() and element[x+2].isupper() \
                and element[x+3].isupper() and element[x+4].isupper():
            new_array.append(element[x+2])
            ''.join(new_array)
        x += 1
        if x == len(element) or (x == len(element)-2):
            break
    result = ''.join(new_array)
    return result


print('Символы в верхнем регистре без re: ')
print(upper_case(line))


# 2.3


def write_to_file(element):
    x = 1
    for i in element:
        while x <= 5:
            file_number = 'files/file_' + str(x) + '.txt'
            file = open(file_number, 'w')
            file.write(element[x - 1])
            x += 1


write_to_file(line)
