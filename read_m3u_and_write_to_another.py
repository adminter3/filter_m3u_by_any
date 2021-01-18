# python read .m3u and create another one with desired channels
import sys
import getopt
import os
import time

valid_filer = ["group-title=\"|AR|",
               "group-title=\"ARAB|", "group-title=\"EU| SWEDEN\""]


current_working_dir = os.getcwd()

NEW_FILE_NAME = "tv_channels_filtered.m3u"
NEW_FILE_PATH = os.path.join(current_working_dir, NEW_FILE_NAME)
print("The new filtered file will be place in the current script directory\n {}".format(NEW_FILE_PATH))


def write_to_file(file_path, content):
    with open(file_path, "a") as newF:
        newF.write(content)


def waitingAnimation():
    # n = n % 3+1
    dots = "."  # n*'.'+(3-n)*' '
    sys.stdout.write('\r Waiting ' + dots)
    sys.stdout.flush()
    # time.sleep(0.5)
    # return n


def read_original_file_and_filter_the_result(original_file_path):
    # ORIGINAL_FILE_PATH = "C:\\Users\\Ali\\Downloads\\tv_channels_R7MDRVCAGL_plus.m3u"
    ORIGINAL_FILE_ABS_PATH = os.path.abspath(original_file_path)
    with open(ORIGINAL_FILE_ABS_PATH, 'r', errors='ignore') as f:
        # .m3u starts with the syntax '#EXTM3U'
        write_to_file(NEW_FILE_PATH, "#EXTM3U\n")
        for line in f:
            if any(valid in line for valid in valid_filer):
                write_to_file(NEW_FILE_PATH, line)
                write_to_file(NEW_FILE_PATH, next(f))

        print("Process finished")


def main(argv):
    original_file_path = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["orgfile="])
    except getopt.GetoptError:
        print('usage: read_m3u_and_write_to_another.py -i <original_file_path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: read_m3u_and_write_to_another.py -i <original_file_path>')
            sys.exit()
        elif opt in ("-i", "--orgfile"):
            original_file_path = arg
            read_original_file_and_filter_the_result(original_file_path)


if __name__ == "__main__":
    main(sys.argv[1:])
