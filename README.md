# USB Keycapture PCAP Interpreter
Python parser for interpreting keyboard captures, under USB device class definition HID 1.11.

NAME:

        A python parser for interpreting keyboard captures,
        under USB device class definition HID 1.11.

        *** REQUIRES PYTHON 3.5+ ***

SYNOPSIS:

        $ upc_decode <input_file.pcap> [flags]...
                - Accepts stdin or stdin redirect
                - Flags must be in correct position

DESCRIPTION:

        -a, --alpha-numeric
                only print alphanumeric chars

        -d, --debug
                output the lookup information for each character

        -h, --help
                display all application information

        -o [FILE], --output [FILE]
                output results to specified file

        -O [FILE], --output-concurrent [FILE]
                output results to specified file and print results to stdout

        -s, --supress-errors
                supress errors, reserved values, and unknown returns

AUTHOR:

        Written by Nathaniel Singer (singer.cloud).

REPORTING BUGS:

        This application is still in early development, please
        report any identified bugs to the git repository at
        https://github.com/nmsinger/USB-PCAP-Parser or directly
        to the author via email: nathaniel@singer.cloud


COPYRIGHT:

        Copyright 2020 Nathaniel Singer

        Licensed under the Apache License, Version 2.0 (the "License"); you
        may not use this application except in compliance with the License.
        You may obtain a copy of the License at

                http://www.apache.org/licenses/LICENSE-2.0

        Unless required by applicable law or agreed to in writing, software
        distributed under the License is distributed on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        See the License for the specific language governing permissions and
        limitations under the License.


SEE ALSO:

        Specification HID1_11.pdf:
                https://usb.org/sites/default/files/documents/hid1_11.pdf
        Mappings table [page 53]:
                https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
        Additional USB protocol documentation: 
                https://www.beyondlogic.org/usbnutshell/usb4.shtml#Interrupt
