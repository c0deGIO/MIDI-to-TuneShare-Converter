import math

with open("Assets/OSD2SD.txt", "r") as f:
    OSD2SD = f.read().rsplit(",")

for i in range(len(OSD2SD)):
    if OSD2SD[i].isnumeric():
        OSD2SD[i] = int(OSD2SD[i])
    else:
        OSD2SD[i] = None

with open("Assets/OSI.txt", "r") as f:
    OSI = f.read().rsplit("\n")

for i in range(len(OSI)):
    if "," in OSI[i]:
        OSI[i] = OSI[i].rsplit(",")[0]
    else:
        OSI[i] = None
OSI[0] = '43'
for i in range(len(OSI)):
    if OSI[i].isnumeric():
        OSI[i] = int(OSI[i])
    else:
        OSI[i] = None

with open("Assets/SBI.txt", "r") as f:
    SBI = f.read().rsplit(",")
SBI[0] = '0'

def _getNote(instr, n):
    li = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note = n[:-1]
    transpose = int(n[-1]) - 2
    ret = transpose * len(li) + li.index(note) + 10
    if instr == "l":
        if OSD2SD[ret-10] is None:
            return [0]
        return [1, str(OSD2SD[ret-10])]
    else:
        ret = str(ret)
        if len(ret) < 3:
            return [1, ret]
        else:
            return [0]

def ConvertMIDItoTuneShare(filename, tempo, quality=1, outputname=""):
    with open(f"Input/{filename}", "r") as f:
        data = f.read().rsplit(":")[2]
    notesData = data.rsplit(";")
    notes = []
    slots = []
    lastVolume = 0
    for i in notesData:
        t = str(i).rsplit(" ")
        if len(t) > 2:
            d ={
                "note": t[1],
                "slot": float(t[0]) * quality,
                "length": math.ceil(float(t[2]) * quality),
                "instrument": t[3],
            }
            if len(t) > 4:
                v = min(max(0, round(float(t[4]) * 36 * quality)), 35)
                d["volume"] = v
                lastVolume = v
            else:
                d["volume"] = lastVolume
            notes.append(d)
    maxSlots = 0
    minSlots = notes[0]["slot"]
    for i in notes:
        if i["slot"] > maxSlots:
            maxSlots = i["slot"]
        if i["slot"] < minSlots:
            minSlots = i["slot"]
    maxSlots = math.ceil(maxSlots - minSlots)
    for i in notes:
        i["slot"] = round(i["slot"]-minSlots)
    for i in range(maxSlots+1):
        slots.append([])
    for i in notes:
        slots[i["slot"]].append({"note": i["note"], "length": min(max(1, i["length"]), 36)-1, "instrument": int(i["instrument"]), "volume": i["volume"]})
    code = f"{round(tempo*quality)}!"
    for i in slots:
        for j in i:
            if j["instrument"] in OSI:
                instrument = SBI[OSI.index(j["instrument"])]
                note = _getNote(instrument, j["note"])
                if note[0]:
                    note = note[1]
                    code += note + instrument + "0123456789abcdefghijklmnopqrstuvwxyz"[j["length"]] + "0123456789abcdefghijklmnopqrstuvwxyz"[j["volume"]]
        code += "!"
    if outputname == "":
        outputname = filename
    with open(f"Output/{outputname}", "w") as f:
        f.write(code)


ConvertMIDItoTuneShare(filename="YOUR FILE.txt", tempo=120, quality=1)
