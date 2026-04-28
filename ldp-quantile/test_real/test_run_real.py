#!/usr/bin/env python3

import subprocess as sbc
import sys
import argparse
import math
import os

############################################################

q_values = ["0.01", "0.25",  "0.5", "0.75", "0.90", "0.95", "0.99"]
q_default = "0.99"

ds_names = ["planetlaball", "seattleall"]
ds_default = "planetlaball"

e_values = ["0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5"]
e_default = ["1.0", "2.0", "3.0", "4.0", "5.0"]

s_base = 16033099
s_step = 127
reps = 100
############################################################


parser = argparse.ArgumentParser()

parser.add_argument("cmd", help="executable name")

options = parser.parse_args()

exec_name = "./" + options.cmd


def print_to_stderr(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()
    return

def test_on_q(outdir):
    for q in q_values:
        outputdir = outdir + "/test_real_q_" + str(q)
        os.makedirs(outputdir, exist_ok=True)
        print_to_stderr('Test quantile = ' + q + '\n')

        for ds in ds_names:
            for e in e_default:
                rep = 1
                for seed in range(s_base, s_base + (reps * s_step), s_step):
                    outputfile = f"{outputdir}/test_q_{q}_e_{e}_ds_{ds}_{rep}.csv"
                    sbc.run([exec_name, "-q" , q, "-r", f'datasets/{ds}.csv', "-e", e, "-f", outputfile, "-s", str(seed)])

                    rep = rep + 1
                    print_to_stderr("#")

                print_to_stderr("\n")

    return

def test_on_ds(outdir):
    for ds in ds_names:
        outputdir = outdir + "/test_real_ds_" + str(ds)
        os.makedirs(outputdir, exist_ok=True)

        print_to_stderr('Test dataset = ' + ds + '\n')

        rep = 1
        for seed in range(s_base, s_base + (reps * s_step), s_step):
            for e in e_values:
                outputfile = f"{outputdir}/test_ds_{ds}_e_{e}_{rep}.csv"
                sbc.run([exec_name, "-q" , q_default, "-r", f'datasets/{ds}.csv', "-e", e, "-f", outputfile, "-s", str(seed)])
            
            rep = rep + 1
            print_to_stderr("#")

        print_to_stderr("\n")

    return


outdir = "Test_of_" + options.cmd

test_on_q(outdir)
test_on_ds(outdir)

print_to_stderr("\nTest completed!!\n")
