param = {
    'student_id': 10012,
    'lssn_id': 1000005,
}

result_param = {}
result_format = {}

for k, v in param.items():
    print(k, v)
    if isinstance(v, dict) or isinstance(v, list):
        result_format[k] = v
    else:
        result_param[k] = v

print(result_param, result_format

query = query.format(**result_format))

print(query)