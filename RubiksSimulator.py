# PREAMBLE:
import numpy as np


# FUNCTIONS:
def F(topf, middlef, bottomf):
    top_layerf = topf[:27] + middlef[52] + topf[28] + middlef[28] + topf[30] + middlef[4] + topf[32:]
    middle_layerf = middlef[:4] + bottomf[3] + middlef[5] + middlef[54] + middlef[7] + middlef[30] + middlef[9] + \
                    middlef[6] + middlef[11] + topf[27] + middlef[13] + middlef[14:28] + bottomf[5] + middlef[29] + \
                    middlef[56] + middlef[31] + middlef[32] + middlef[33] + middlef[8] + middlef[35] + topf[29] + \
                    middlef[37:52] + bottomf[7] + middlef[53] + middlef[58] + middlef[55] + middlef[34] + middlef[57] \
                    + middlef[10] + middlef[59] + topf[31] + middlef[61:]
    bottom_layerf = bottomf[:3] + middlef[60] + bottomf[4] + middlef[36] + bottomf[6] + middlef[12] + bottomf[8:]
    return top_layerf, middle_layerf, bottom_layerf


def Fdash(topfdash, middlefdash, bottomfdash):
    top_layerfdash = topfdash[:26] + "\t" + middlefdash[12] + topfdash[28] + middlefdash[36] + topfdash[30] + \
                 middlefdash[60] + topfdash[32:]
    middle_layerfdash = middlefdash[:4] + topfdash[27] + middlefdash[5] + middlefdash[10] + middlefdash[7] + \
                    middlefdash[34] + middlefdash[9] + middlefdash[58] + middlefdash[11] + bottomfdash[3] + \
                    middlefdash[13:28] + topfdash[29] + middlefdash[29] + middlefdash[8] + middlefdash[31:33] + \
                    middlefdash[33] + middlefdash[56] + middlefdash[35] + bottomfdash[5] + middlefdash[37:52] + \
                    topfdash[31] + middlefdash[53] + middlefdash[6] + middlefdash[55] + middlefdash[30] + \
                    middlefdash[57] + middlefdash[34] + middlefdash[59] + bottomfdash[7] + middlefdash[61:]
    bottom_layerfdash = bottomfdash[:3] + middlefdash[4] + bottomfdash[4] + middlefdash[28] + bottomfdash[6] + \
                        middlefdash[52] + bottomfdash[8:]
    return top_layerfdash, middle_layerfdash, bottom_layerfdash


def R(topr, middler, bottomr):
    top_layerr = topr[:7] + middler[10] + topr[8:19] + middler[34] + topr[20:31] + middler[58] + topr[32:]
    middle_layerr = middler[:10] + bottomr[7] + middler[11] + middler[60] + middler[13] + middler[36] + middler[15] + \
                    middler[12] + middler[17] + topr[31] + middler[19:24] + middler[24:34] + bottomr[19] + middler[35] \
                    + middler[62] + middler[37:40] + middler[14] + middler[41] + topr[19] + middler[43:58] + \
                    bottomr[31] + middler[59] + middler[64] + middler[61] + middler[40] + middler[63] + middler[16] + \
                    middler[65] + topr[7] + middler[67:]
    bottom_layerr = bottomr[:7] + middler[66] + bottomr[8:19] + middler[42] + bottomr[20:31] + middler[18] + \
                    bottomr[32:]
    return top_layerr, middle_layerr, bottom_layerr


def Rdash(toprdash, middlerdash, bottomrdash):
    top_layerrdash = toprdash[:7] + middlerdash[66] + toprdash[8:19] + middlerdash[42] + toprdash[20:31] + \
                     middlerdash[18] + toprdash[32:]
    middle_layerrdash = middlerdash[:10] + toprdash[7] + middlerdash[11] + middlerdash[16] + middlerdash[13] + \
                        middlerdash[40] + middlerdash[15] + middlerdash[64] + middlerdash[17] + bottomrdash[31] + \
                        middlerdash[19:34] + toprdash[19] + middlerdash[35] + middlerdash[14] + middlerdash[37] + \
                        middlerdash[38] + middlerdash[39] + middlerdash[62] + middlerdash[41] + bottomrdash[19] + \
                        middlerdash[43:58] + toprdash[31] + middlerdash[59] + middlerdash[12] + middlerdash[61] + \
                        middlerdash[36] + middlerdash[63] + middlerdash[60] + middlerdash[65] + bottomrdash[7] + \
                        middlerdash[67:]
    bottom_layerrdash = bottomrdash[:7] + middlerdash[10] + bottomrdash[8:19] + middlerdash[34] + bottomrdash[20:31] + \
                        middlerdash[58] + bottomrdash[32:]
    return top_layerrdash, middle_layerrdash, bottom_layerrdash


def U(topu, middleu, bottomu):
    top_layeru = topu[:3] + topu[27] + topu[4] + topu[15] + topu[6] + topu[3] + topu[8:15] + topu[29] + topu[16] + \
                 topu[17] + topu[18] + topu[5] + topu[20:27] + topu[31] + topu[28] + topu[19] + topu[30] + topu[7] + \
                 topu[32:]
    middle_layeru = middleu[6:23] + middleu[1] + middleu[0:5] + middleu[23] + middleu[24:]
    bottom_layeru = bottomu
    return top_layeru, middle_layeru, bottom_layeru


def Udash(topudash, middleusdash, bottomudash):
    top_layerudash = topudash[:3] + topudash[7] + topudash[4] + topudash[19] + topudash[6] + topudash[31] + \
                     topudash[8:15] + topudash[5] + topudash[16] + topudash[17] + topudash[18] + topudash[29] + \
                     topudash[20:27] + topudash[3] + topudash[28] + topudash[15] + topudash[30] + topudash[27] + \
                     topudash[32:]

    middle_layerudash = middleusdash[18:23] + middleusdash[1] + middleusdash[0:17] + middleusdash[23] + \
                        middleusdash[24:]
    bottom_layerudash = bottomudash

    return top_layerudash, middle_layerudash, bottom_layerudash


def D(topd, middled, bottomd):
    top_layerd = topd
    middle_layerd = middled[:48] + middled[66:71] + middled[1] + middled[48:65] + middled[71]
    bottom_layerd = bottomd[:3] + bottomd[27] + bottomd[4] + bottomd[15] + bottomd[6] + bottomd[3] + bottomd[8:15] + \
                    bottomd[29] + bottomd[16] + bottomd[17] + bottomd[18] + bottomd[5] + bottomd[20:27] + bottomd[31] \
                    + bottomd[28] + bottomd[19] + bottomd[30] + bottomd[7] + bottomd[32:]
    return top_layerd, middle_layerd, bottom_layerd


def Ddash(topddash, middleddash, bottomddash):
    top_layerddash = topddash
    middle_layerddash = middleddash[:48] + middleddash[54:71] + middleddash[1] + middleddash[48:53] + middleddash[71]
    bottom_layerddash = bottomddash[:3] + bottomddash[7] + bottomddash[4] + bottomddash[19] + bottomddash[6] + \
                        bottomddash[31] + bottomddash[8:15] + bottomddash[5] + bottomddash[16] + bottomddash[17] + \
                        bottomddash[18] + bottomddash[29] + bottomddash[20:27] + bottomddash[3] + bottomddash[28] + \
                        bottomddash[15] + bottomddash[30] + bottomddash[27] + bottomddash[32:]
    return top_layerddash, middle_layerddash, bottom_layerddash


def L(topl, middlel, bottomel):
    top_layerl = topl[:3] + middlel[70] + topl[4:15] + middlel[46] + topl[16:27] + middlel[22] + topl[28:]
    middle_layerl = middlel[48] + middlel[1] + middlel[24] + middlel[3] + middlel[0] + middlel[5] + topl[3] + \
                    middlel[7:22] + bottomel[27] + middlel[23] + middlel[50] + middlel[25] + middlel[26] + \
                    middlel[27] + middlel[2] + middlel[29] + topl[15] + middlel[31:46] + bottomel[15] + \
                    middlel[47] + middlel[52] + middlel[49] + middlel[28] + middlel[51] + middlel[4] + middlel[53] + \
                    topl[27] + middlel[55:70] + bottomel[3] + middlel[71]
    bottom_layerl = bottomel[:3] + middlel[6] + bottomel[4:15] + middlel[30] + bottomel[16:27] + middlel[54] + \
                    bottomel[28:]
    return top_layerl, middle_layerl, bottom_layerl


def Ldash(topldash, middleldash, bottomldash):
    top_layerldash = topldash[:3] + middleldash[6] + topldash[4:15] + middleldash[30] + topldash[16:27] + \
                     middleldash[54] + topldash[28:]
    middle_layerldash = middleldash[4] + middleldash[1] + middleldash[28] + middleldash[3] + middleldash[52] + \
                        middleldash[5] + bottomldash[3] + middleldash[7:22] + topldash[27] + middleldash[23] + \
                        middleldash[2] + middleldash[25] + middleldash[26] + middleldash[27] + middleldash[50] + \
                        middleldash[29] + bottomldash[15] + middleldash[31:46] + topldash[15] + middleldash[47] + \
                        middleldash[0] + middleldash[49] + middleldash[24] + middleldash[51] + middleldash[48] + \
                        middleldash[53] + bottomldash[27] + middleldash[55:70] + topldash[3] + middleldash[71]

    bottom_layerldash = bottomldash[:3] + middleldash[70] + bottomldash[4:15] + middleldash[46] + bottomldash[16:27] + \
                        middleldash[22] + bottomldash[28:]

    return top_layerldash, middle_layerldash, bottom_layerldash


def B(topb, middleb, bottomb):
    top_layerb = topb[:3] + middleb[16] + topb[4] + middleb[40] + topb[6] + middleb[64] + topb[8:]
    middle_layerb = topb[7] + middleb[1:16] + bottomb[31] + middleb[17] + middleb[66] + middleb[19] + \
                    middleb[42] + middleb[21] + middleb[18] + middleb[23] + topb[5] + middleb[25:40] + bottomb[29] + \
                    middleb[41] + middleb[68] + middleb[43] + middleb[44] + middleb[45] + middleb[20] + middleb[47] + \
                    topb[3] + middleb[49:64] + bottomb[27] + middleb[65] + middleb[70] + middleb[67] + middleb[46] + \
                    middleb[69] + middleb[22] + middleb[71]
    bottom_layerb = bottomb[:27] + middleb[0] + bottomb[28] + middleb[24] + bottomb[30] + middleb[48] + bottomb[32:]
    return top_layerb, middle_layerb, bottom_layerb


def Bdash(topbdash, middlebdash, bottombdash):
    top_layerbdash = topbdash[:3] + middlebdash[48] + topbdash[4] + middlebdash[24] + topbdash[6] + middlebdash[0] + \
                     topbdash[8:]
    middle_layerbdash = bottombdash[27] + middlebdash[1:16] + topbdash[3] + middlebdash[17] + middlebdash[22] + \
                        middlebdash[19] + middlebdash[46] + middlebdash[21] + middlebdash[70] + middlebdash[23] + \
                        bottombdash[29] + middlebdash[25:40] + topbdash[5] + middlebdash[41] + middlebdash[20] + \
                        middlebdash[43] + middlebdash[44] + middlebdash[45] + middlebdash[68] + middlebdash[47] + \
                        bottombdash[31] + middlebdash[49:64] + topbdash[7] + middlebdash[65] + middlebdash[18] + \
                        middlebdash[67] + middlebdash[42] + middlebdash[69] + middlebdash[66] + middlebdash[71]
    bottom_layerbdash = bottombdash[:27] + middlebdash[64] + bottombdash[28] + middlebdash[40] + bottombdash[30] + \
                        middlebdash[16] + bottombdash[32:]
    return top_layerbdash, middle_layerbdash, bottom_layerbdash


def move_options(argument, top_net, middle_net, bottom_net):
    switch_between = {
        0: F(top_net, middle_net, bottom_net),  # 90 clockwise
        1: R(top_net, middle_net, bottom_net),
        2: U(top_net, middle_net, bottom_net),
        3: B(top_net, middle_net, bottom_net),
        4: L(top_net, middle_net, bottom_net),
        5: D(top_net, middle_net, bottom_net),
        6: Fdash(top_net, middle_net, bottom_net),  # 90 anticlockwise
        7: Rdash(top_net, middle_net, bottom_net),
        8: Udash(top_net, middle_net, bottom_net),
        9: Bdash(top_net, middle_net, bottom_net),
        10: Ldash(top_net, middle_net, bottom_net),
        11: Ddash(top_net, middle_net, bottom_net)}
    return switch_between.get(argument, "Invalid direction.")


def choice_moves(moves_chosen):
    store_moves = np.zeros(int(moves_chosen), dtype=int)
    for i in range(0, len(store_moves)):
        move = input("Please select a move: ")
        if int(move) > 11:
            updated_choice = input("\033[1m" + "INVALID! Please choose again: ")
            store_moves[i] = int(updated_choice)
        else:
            store_moves[i] = int(move)
    print(
        "\n\t----------------------------------------------------------------------------------------------------------"
        "----------")
    print("\t\tSelection stored successfully!")
    print(
        "\t------------------------------------------------------------------------------------------------------------"
        "--------\n")
    return store_moves


# MAIN:
current_state = 'Solved'

# START POSITION:
top_layer_start = "\t\t\tW\tW\tW\t\t\t\n\t\t\tW\tW\tW\t\t\t\n\t\t\tW\tW\tW\t\t\t\n"
middle_layer_start = "O\tO\tO\tG\tG\tG\tR\tR\tR\tB\tB\tB\n" \
                     "O\tO\tO\tG\tG\tG\tR\tR\tR\tB\tB\tB\n" \
                     "O\tO\tO\tG\tG\tG\tR\tR\tR\tB\tB\tB\n"
bottom_layer_start = "\t\t\tY\tY\tY\t\t\t\n\t\t\tY\tY\tY\t\t\t\n\t\t\tY\tY\tY\t\t\t\n"

print(
    "\n\t--------------------------------------------------------------------------------------------------------------"
    "------")
print("\t\tDirections to chose from: \tF(0), R(1), U(2), B(3), L(4), D(5), "
      "F'(6), R'(7), U'(8), B'(9), L'(10), D'(11)\t\t")
print(f"\t\tCurrent state of cube: \t\t{current_state}\t\t")
print(
    "\t----------------------------------------------------------------------------------------------------------------"
    "----\n")
# Show the net of the current state of cube (solved):
print(top_layer_start + "\n" + middle_layer_start + "\n" + bottom_layer_start)
number_of_moves = input("How many moves would you like to perform? ")
choices = choice_moves(number_of_moves)

step1_top, step1_middle, step1_bottom = move_options(choices[0], top_layer_start, middle_layer_start,
                                                     bottom_layer_start)

current_state = 'Unsolved'
print(
    "\t----------------------------------------------------------------------------------------------------------------"
    "----")
print(f"\t\tUpdated state of the cube: \t\t{current_state}\t\t")
print(
    "\t----------------------------------------------------------------------------------------------------------------"
    "----\n")

output1 = step1_top
output2 = step1_middle
output3 = step1_bottom

for choice in choices[1:]:
    top_out, middle_out, bottom_out = move_options(choice, output1, output2, output3)
    output1 = top_out
    output2 = middle_out
    output3 = bottom_out

print(output1 + "\n" + output2 + "\n" + output3)
