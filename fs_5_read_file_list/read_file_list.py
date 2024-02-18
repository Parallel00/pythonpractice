def read_file_list(filename):
    with open(filename) as q:
        for ln in q:
            ln = ln.strip()
            print(f"- {ln}")