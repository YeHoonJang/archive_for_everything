# import parsing_4_0 as ps
import os

def worker(pat_text, save_xml):
    with open(pat_text, "r") as f:
        single_patent = ''
        counts = 0
        while True:
            line = f.readline()
            if line.count("""<?xml """) == 1:
                counts += 1
                if counts > 1 :
                    print("parsing...")  #추후에 삭제할 것임
                    # ps.parsing(single_patent)
                    print("DB...\n")  #추후에 삭제할 것임

                    if save_xml == True:
                        # print("\nStart to save the file as xml...")
                        make_xml_file(pat_text, single_patent, counts)

                single_patent = ''
                single_patent += line

            else:
                single_patent += line


            if not line: break




def make_xml_file(pat_text, single_patent, counts):
    pat_num = pat_text.split('.')[0] + "_" + str(counts-1) + ".xml"
    pat_file = os.path.join(pat_text, pat_num)

    with open(pat_file, "w") as f:
        f.write(single_patent)
        f.close()