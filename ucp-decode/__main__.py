import sys, os
import print_usage #local
from usb_capture import Capture #local
from os import path

def main():
    alpha_num_only=False
    debug=False
    supress_stdout=False
    supress_errors=False
    output_file=False
    output_filename=""

    #if no args supplied, print basic usage information
    if len(sys.argv[1:]) == 0:
        print_usage.abbreviated()
        exit()

    #if help is asked for, ignore everything else, provide output, exit
    if ("-h" in sys.argv[1:]) or ("--help" in sys.argv[1:]):
        print_usage.all()
        exit()

    #check if file exists
    if not (path.isfile(sys.argv[1])):
        print("File: {}, does not exist".format(sys.argv[1]))
        print_usage.abbreviated()
        exit()

    #check for output, no stdout
    if ("-o" in sys.argv[1:]) or ("--output" in sys.argv[1:]):
        output_file=True
        supress_stdout=True

    #check for output, with concurrent stdout
    if ("-O" in sys.argv[1:]) or ("--output-concurrent" in sys.argv[1:]):
        output_file=True

    #get and prepare to pass filename
    if output_file == True:
        #locate arg position
        arg_pos=0
        try: arg_pos=sys.argv[1:].index("--output-concurrent")
        except:
            try: arg_pos=sys.argv[1:].index("--output")
            except:
                try: arg_pos=sys.argv[1:].index("-o")
                except:
                    try: arg_pos=sys.argv[1:].index("-O")
                    except:
                        print("Error: Syntax\n")
                        print_usage.abbreviated()
                        exit()
        #get filename
        output_filename = os.path.abspath(sys.argv[arg_pos+2])
        sys.argv.remove(sys.argv[arg_pos+2]) #to prevent tripping invalid arg check later


    #check for alphanumeric flag
    if ("-a" in sys.argv[1:]) or ("--alpha-numeric" in sys.argv[1:]):
        alpha_num_only=True

    #check for debug flag
    if ("-d" in sys.argv[1:]) or ("--debug" in sys.argv[1:]):
        debug=True

    #check for supress flag
    if ("-s" in sys.argv[1:]) or ("--supress-errors" in sys.argv[1:]):
        supress_errors=True

    #check for invalid args, starting at 2, since first is file name
    validArgs = ["-a",  "--alpha-numeric",  "-d",   "--debug", "-h", "--help",
        "-o", "--output", "-O", "--output-concurrent", "-s", "--supress_errors"]
    for i in range(2,len(sys.argv[1:])+1):
        if not (sys.argv[i] in validArgs):
            print("Error: Syntax, {} is not a valid argument\n"\
             .format(sys.argv[i]))
            print_usage.abbreviated()
            exit()

    #give user param info if debugging is turned on
    if debug == True:
        print('Executing within the following parameters:\n\
        alpha_num_only: {}\n\
        debug: {}\n\
        supress_stdout: {}\n\
        supress_errors: {}\n\
        output_file: {}\n\
        output_filename: {}\n\
        '.format(alpha_num_only, debug, supress_stdout, \
            supress_errors, output_file, output_filename))

    #RUN THE QUERY!
    query_object = Capture(sys.argv[1])
    query_object.decode(alpha_num_only, debug, supress_stdout, supress_errors,\
                        output_file, output_filename)

if __name__ == '__main__':
    main()
