#https://cdn.databases.today/Ubisoft.com%20forum.sql
read_file = "Datasets/Ubisoft_Forum.sql"
write_file ="Datasets/Ubisoft_Forum_processed.txt"
ignore_first_n_lines = 0

def main():
    process()

def process():
    with open(read_file,"r") as fi:
        with open(write_file,"w") as fo:
            fo.write('"username";"hash";"salt"')
            if ignore_first_n_lines != 0:
                for _ in range(ignore_first_n_lines):
                    next(fi)

            for index,entry in enumerate(fi):
                try:
                    fo.write('"{}";"{}";"{}"'.format(*entry.split(':')))
                except:
                    print(entry.split(':'))

def analyse_raw():
    with open(read_file,"r") as fi:
        with open(write_file,"w") as fo:
            if ignore_first_n_lines != 0:
                for _ in range(ignore_first_n_lines):
                    next(fi)

            for index,entry in enumerate(fi):
                print(entry)
                if index == 50:
                    break

if __name__ == "__main__":
    main()
