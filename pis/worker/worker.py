import parsing_4_0 as ps

pat_text ="toy_2.xml"


with open(pat_text, "r") as f:
    a = ''
    counts = 0
    while True:
        line = f.readline()
        if line.count("""<?xml """) == 1:
            counts += 1
            if counts == 1:
                pass
            else:
                print("parsing...")
                ps.parsing(a)
                print("DB...\n")

            a = ''
            a += line
        else:
            a += line

        if not line: break