def all():
    name()
    usage()
    description()
    author()
    bugs()
    copyright()
    seealso()

def abbreviated():
    name()
    usage()
    description()

def name():
    print('\033[1m\033[33mNAME:\033[0m\n\n\
    \tA python parser for interpreting keyboard captures,\n\
    \tunder USB device class definition HID 1.11.\n\n\
    \t*** REQUIRES PYTHON 3.5+ ***\n')

def usage():
    print('\033[1m\033[33mSYNOPSIS:\033[0m\n\n\
    \t$ upc_decode <input_file.pcap> [flags]...\n\
    \t\t- Accepts stdin or stdin redirect\n\
    \t\t- Flags must be in correct position\n')

def description():
    print('\033[1m\033[33mDESCRIPTION:\033[0m\n\n\
    \t\033[1m-a, --alpha-numeric\033[0m\n\
    \t\tonly print alphanumeric chars\n\n\
    \t\033[1m-d, --debug\033[0m\n\
    \t\toutput the lookup information for each character\n\n\
    \t\033[1m-h, --help\033[0m\n\
    \t\tdisplay all application information\n\n\
    \t\033[1m-o [FILE], --output [FILE]\033[0m\n\
    \t\toutput results to specified file\n\n\
    \t\033[1m-O [FILE], --output-concurrent [FILE]\033[0m\n\
    \t\toutput results to specified file and print results to stdout\n\n\
    \t\033[1m-s, --supress-errors\033[0m\n\
    \t\tsupress errors, reserved values, and unknown returns\n')

def author():
    print('\033[1m\033[33mAUTHOR:\033[0m\n\n\
    \tWritten by Nathaniel Singer (singer.cloud).\n')

def bugs():
    print('\033[1m\033[33mREPORTING BUGS:\033[0m\n\n\
    \tThis application is still in early development, please\n\
    \treport any identified bugs to the git repository at\n\
    \thttps://github.com/nmsinger/USB-PCAP-Parser or directly\n\
    \tto the author via email: nathaniel@singer.cloud\n\n')

def copyright():
    print('\033[1m\033[33mCOPYRIGHT:\033[0m\n\n\
    \tCopyright 2020 Nathaniel Singer\n\n\
    \tLicensed under the Apache License, Version 2.0 (the "License"); you\n\
    \tmay not use this application except in compliance with the License.\n\
    \tYou may obtain a copy of the License at\n\n\
    \t\thttp://www.apache.org/licenses/LICENSE-2.0\n\n\
    \tUnless required by applicable law or agreed to in writing, software\n\
    \tdistributed under the License is distributed on an "AS IS" BASIS,\n\
    \tWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n\
    \tSee the License for the specific language governing permissions and\n\
    \tlimitations under the License.\n\n')

def seealso():
    print('\033[1m\033[33mSEE ALSO:\033[0m\n\n\
    \tSpecification HID1_11.pdf:\n\
    \t\thttps://usb.org/sites/default/files/documents/hid1_11.pdf\n\
    \tMappings table [page 53]:\n\
    \t\thttps://www.usb.org/sites/default/files/documents/hut1_12v2.pdf\n\
    \tAdditional USB protocol documentation: \n\
    \t\thttps://www.beyondlogic.org/usbnutshell/usb4.shtml#Interrupt\n\n')
