import os
def find_updated_result(device_b_content):
    ext = ['.txt']
    device_a_content = {}
    files_all = [f for f in os.listdir(os.getcwd()) if f.endswith(tuple(ext))]
    print(files_all)
    for file_name in files_all:
        with open (file_name, 'r+') as f:
            file_a_content = f.readlines()
            f.close()
        with open (file_name, 'w+') as f:
            f.close()
        # print(device_b_content)
        device_a_content[file_name] = file_a_content
    updated_a = []
    updated_b = []
    original = []
    final_to_print = {}
    for k, v in device_a_content.items():
        if k not in final_to_print:
            final_to_print[k] = 's'
        if type(final_to_print[k]) is not list:
            temp = []
            final_to_print[k] = temp
        for line in v:
            if line.startswith("A --> ") or line.startswith("B --> "):
                final_to_print[k].append(line)
            else:
                line = 'A --> ' + line
                final_to_print[k].append(line)

    for k, v in device_b_content.items():
        if k not in final_to_print:
            final_to_print[k] = 's'
        if type(final_to_print[k]) is not list:
            temp = []
            final_to_print[k] = temp
        for line in v:
            if line.startswith("A --> ") or line.startswith("B --> "):
                final_to_print[k].append(line)
            else:
                line = 'B --> ' + line
                final_to_print[k].append(line)
    for k, v in final_to_print.items():
        with open (k, 'w+') as f:
            for s in v:
                f.write(s)
    print(final_to_print)
    return final_to_print
