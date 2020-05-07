import os

keymap = {1:  '(err_roll_over)',  2:  '(post_fail)',  3:  '(err_undef)',  4:  'a',
        5:  'b',             6:  'c',             7:  'd',             8:  'e',
        9:  'f',             10: 'g',             11: 'h',             12: 'i',
        13: 'j',             14: 'k',             15: 'l',             16: 'm',
        17: 'n',             18: 'o',             19: 'p',             20: 'q',
        21: 'r',             22: 's',             23: 't',             24: 'u',
        25: 'v',             26: 'w',             27: 'x',             28: 'y',
        29: 'z',             30: '1',             31: '2',             32: '3',
        33: '4',             34: '5',             35: '6',             36: '7',
        37: '8',             38: '9',             39: '0',             40: '(return)',
        41: '(esc)',         42: '(del)',         43: '(tab)',         44: ' ',
        45: '(-/_)',         46: '(=/+)',         47: '([/{)',         48: '(]/})',
        49: '(\\or|)',       50: '(`/~)',         51: '(;/:)',         52: '(\'/\")',
        53: '(~/`)',         54: '(,/<)',         55: '(./>)',         56: '(/or?)',
        57: '(caps)',        58: '(F1)',          59: '(F2)',          60: '(F3)',
        61: '(F4)',          62: '(F5)',          63: '(F6)',          64: '(F7)',
        65: '(F8)',          66: '(F9)',          67: '(F10)',         68: '(F11)',
        69: '(F12)',         70: '(prt-sc)',      71: '(scr-lk)',      72: '(pause)',
        73: '(ins)',         74: '(home)',        75: '(pg-up)',       76: '(del)',
        77: '(end)',         78: '(pg-dwn)',      79: '(arrow_r)',     80: '(arrow_l)',
        81: '(arrow_d)',     82: '(arrow_up)',    83: '(nm_lck)',      84: '(kp_/)',
        85: '(kp_*)',        86: '(kp_-)',        87: '(kp_+)',        88: '(kp_ent)',
        89: '(kp_1/end)',    90: '(kp_2/dwn)',    91: '(kp_3/pgdwn)',  92: '(kp_4/left)',
        93: '(kp_5)',        94: '(kp_6/right)',  95: '(kp_7/home)',   96: '(kp_8/up)',
        97: '(kp_9/pgup)',   98: '(kp_0/ins)',    99: '(kp_./del)',    100:'(\\/|)',
        101:'(application)', 102:'(power)',       103:'(kp_=)',        104:'(F13)',
        105:'(F14)',         106:'(F15)',         107:'(F16)',         108:'(F17)',
        109:'(F18)',         110:'(F19)',         111:'(F20)',         112:'(F21)',
        113:'(F22)',         114:'(F23)',         115:'(F24)',         116:'(exec)',
        117:'(help)',        118:'(menu)',        119:'(select)',      120:'(stop)',
        121:'(again)',       122:'(undo)',        123:'(cut)',         124:'(copy)',
        125:'(paste)',       126:'(find)',        127:'(mute)',        128:'(vol_up)',
        129:'(vol_dwn)',     130:'(cap_lk)',      131:'(num_lk)',      132:'(scrl_lk)',
        133:'(kp_,)',        134:'(kp_=)',        135:'(internat_1)',  136:'(internat_2)',
        137:'(internat_3)',  138:'(internat_4)',  139:'(internat_5)',  140:'(internat_6)',
        141:'(internat_7)',  142:'(internat_8)',  143:'(internat_9)',  144:'(lang_1)',
        145:'(lang_2)',      146:'(lang_3)',      147:'(lang_4)',      148:'(lang_5)',
        149:'(lang_6)',      150:'(lang_7)',      151:'(lang_8)',      152:'(lang_9)',
        153:'(alt_erase)',   154:'(sysreq/attn)', 155:'(cancel)',      156:'(clear)',
        157:'(prior)',       158:'(return)',      159:'(separator)',   160:'(out)',
        161:'(oper)',        162:'(clr/again)',   163:'(crsel/props)', 164:'(exsel)',
        165:'(reserved)',    166:'(reserved)',    167:'(reserved)',    168:'(reserved)',
        169:'(reserved)',    170:'(reserved)',    171:'(reserved)',    172:'(reserved)',
        173:'(reserved)',    174:'(reserved)',    175:'(reserved)',    176:'(kp_00)',
        177:'(kp_000)',      178:'(thou_sep)',    179:'(dec_sep)',     180:'(cur_unit)',
        181:'(cursub_unit)', 182:'(kp_\'(\')',    183:'(kp_\')\')',    184:'(kp_\'{\')',
        185:'(kp_\'}\')',    186:'(kp_tab)',      187:'(kp_bkspc)',    188:'(kp_A)',
        189:'(kp_B)',        190:'(kp_C)',        191:'(kp_D)',        192:'(kp_E)',
        193:'(kp_F)',        194:'(kp_XOR)',      195:'(kp_^)',        196:'(kp_%)',
        197:'(kp_<)',        198:'(kp_>)',        199:'(kp_&)',        200:'(kp_&&)',
        201:'(kp_|)',        202:'(kp_||)',       203:'(kp_:)',        204:'(kp_#)',
        205:'(kp_space)',    206:'(kp_@)',        207:'(kp_!)',        208:'(kp_memstore)',
        209:'(kp_memrecal)', 210:'(kp_memclr)',   211:'(kp_memadd)',   212:'(kp_memsub)',
        213:'(kp_memmult)',  214:'(kp_memdiv)',   215:'(kp_+/-)',      216:'(kp_clr)',
        217:'(kp_clrent)',   218:'(kp_bin)',      219:'(kp_octal)',    220:'(kp_decimal)',
        221:'(kp_hex)',      222:'(reserved)',    223:'(reserved)',    224:'(ctrl_left)',
        225:'(shift_left)',  226:'(alt_left)',    227:'(gui_left)',    228:'(ctrl_right)',
        229:'(shift_right)', 230:'(alt_right)',   231:'(gui_right)',   range(232,65535):'(reserved)'
}
errors = [1,2,3,*range(165,176,1),*range(232,65536,1)]

class Capture():
    def __init__(self, capture_file):
        self.f_cap = capture_file

    def decode(self, alpha_num_only, debug, supress_stdout, supress_errors,\
                        output_file, output_filename):
        data=os.popen('tshark -r {} -T fields -e usb.capdata -2 \'usb.src =='\
             ' "1.1.1" && usb.transfer_type==0x01\''.format(self.f_cap)).read()

        debug_feed=''
        parsing_feed=''

        for l in data.splitlines():
            b_array = bytearray.fromhex(l.strip()) #get line as hex
            for b in b_array: #for each byte in each line
                if b != 0: #loop until non-null
                    val = int(b) #get USB integer value for lookup

                    if supress_errors == True:
                        if val in errors:
                            debug_feed+="Matched int({}), as char({}), supress_errors=True\n".format(str(val), keymap[val])
                            continue #cancel this iteration

                    if alpha_num_only == True:
                        if 4 <= val <= 40:
                            parsing_feed+=keymap[val]
                            debug_feed+="Matched int({}), as char({}), alpha_only=True\n".format(str(val), keymap[val])
                        else:
                            debug_feed+="Error: Could not find int({}), alpha_only=True\n".format(str(val), keymap[val])
                    elif val in keymap:
                        debug_feed+="Matched int({}), as char({})\n".format(str(val), keymap[val])
                        parsing_feed+=keymap[val]
                    else:
                        debug_feed+="Error: Could not find int({})\n".format(str(val), keymap[val])

        if debug == True:
            print(debug_feed)

        if not (supress_stdout == True):
            print(parsing_feed)

        if output_file == True:
            try:
                with open(output_filename, "w") as f:
                    f.write(parsing_feed + "\n")
                print("\nWrote parsing feed to: {}".format(output_filename))
            except:
                print("\nEncountered error writing output to: {}".format(output_filename))
