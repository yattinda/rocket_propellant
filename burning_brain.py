import math
status_1 = float(input("片面:0\n両面:1\n"))
status_2 = float(input("端のみ：0\n内面と端（課題内容）:1\n外面と端:2\n全て:3\n"))
indir = float(input("内径m\n"))
outdir = float(input("外径m\n"))
long = float(input("長さm\n"))
time = float(input("時間s\n"))
row = float(input("比重・密度\n"))
r = float(input("燃焼速度m/s\n"))

if status_2 == 1:
    indir = indir + 2 * r * time
elif status_2 == 2:
    outdir = outdir - 2 * r * time
elif status_2 == 3:
    indir = indir + 2 * r * time
    outdir = outdir - 2 * r * time

if status_1 == 0:
    long = long - r * time
elif status_2 == 1:
    long = long - 2 * r * time

if long < 0 or outdir < indir:
    print("#################\n")
    print("AAAAAAAAAAAAAAAAA\n")
    print("#################\n")

Ain  = indir * long * math.pi
Aout = outdir * long * math.pi
Aend = ((outdir * outdir - indir * indir)/ 4) * math.pi * 2

if status_2 == 0:
    A = Aend
elif status_2 == 1:
    A = Ain + Aend
elif status_2 == 2:
    A = Aout + Aend
elif status_2 == 3:
    A = Ain + Aout + Aend

print("内径{}m\n外径{}m\n長さ{}m\n推進剤質量流量{}kg/s\n".format(indir, outdir, long, A * r * row * 1000))
