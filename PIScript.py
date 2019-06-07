#python PI script

import requests
#r = requests.get('http://127.0.0.1:8765')
#r.json()

params = (
    ('async', 'false'),
)

files = {
    'audio': ('audio.mp3', open('ttsaudio.mp3', 'rb')),
    'transcript': ('words.txt', open('words.txt', 'rb')),
}

response = requests.post('http://127.0.0.1:8765/transcriptions', params=params, files=files)
data = response.json()
print(response.json())

f= open("outScript.txt","w+") #create file to write script to


for phoneList in data['words']:
    i = 0

    oldWordPos = 0 #These keep track of positions in the current word

    while i < len(phoneList['phones']):
        #print(phoneList['phones'][i]["duration"])
        duration = phoneList['phones'][i]["duration"]
        start = phoneList['start']
        #print(phoneList['phones'][i]["phone"])

        f.write("currentTime %f ;\r\n" % ((phoneList['start'] +oldWordPos)*24))

        oldWordPos = oldWordPos + phoneList['phones'][i]["duration"]
        #make script here
        #end time - startTime == sum of all durations on phones in that word
        #Therefore phone start == startTime + all previous phones in that word

        rest = True

        if "dh_" in str(phoneList['phones'][i]):
            rest = False
            print("found dh_ - posed")
         
            f.write("select -r joint3 joint1 joint2 ;\r\n")
            f.write("pose -apply -name dh character1 ;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2|joint3.translate;\r\n")
            f.write("setKeyframe -breakdown 0 -hierarchy none -controlPoints 0 -shape 0 {\"joint1\", \"joint2\", \"joint3\"};\r\n")

        if "k_" in str(phoneList['phones'][i]) or "'g_" in str(phoneList['phones'][i]):
            rest = False
            print("found k_ / g_ - posed")

            f.write("select -r joint3 joint1 joint2 ;\r\n")
            f.write("pose -apply -name k character1 ;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2|joint3.translate;\r\n")
            f.write("setKeyframe -breakdown 0 -hierarchy none -controlPoints 0 -shape 0 {\"joint1\", \"joint2\", \"joint3\"};\r\n")

        if "zh_" in str(phoneList['phones'][i]) or "sh_" in str(phoneList['phones'][i]):
            rest = False
            print("found zh_ / Sh - posed")

            f.write("select -r joint3 joint1 joint2 ;\r\n")
            f.write("pose -apply -name Ezh character1 ;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2|joint3.translate;\r\n")
            f.write("setKeyframe -breakdown 0 -hierarchy none -controlPoints 0 -shape 0 {\"joint1\", \"joint2\", \"joint3\"};\r\n")

        if "s_" in str(phoneList['phones'][i]) or "z_" in str(phoneList['phones'][i]):
            rest = False
            print("found s_ / z_ - posed")

            f.write("select -r joint3 joint1 joint2 ;\r\n")
            f.write("pose -apply -name s character1 ;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2|joint3.translate;\r\n")
            f.write("setKeyframe -breakdown 0 -hierarchy none -controlPoints 0 -shape 0 {\"joint1\", \"joint2\", \"joint3\"};\r\n")

        if "jh_" in str(phoneList['phones'][i]) or "ch_" in str(phoneList['phones'][i]):
            rest = False
            print("found jh_/ ch_ - posed")

            f.write("select -r joint3 joint1 joint2 ;\r\n")
            f.write("pose -apply -name Dezh character1 ;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2|joint3.translate;\r\n")
            f.write("setKeyframe -breakdown 0 -hierarchy none -controlPoints 0 -shape 0 {\"joint1\", \"joint2\", \"joint3\"};\r\n")

        if "t_" in str(phoneList['phones'][i]) or "n_" in str(phoneList['phones'][i]) or "d_" in str(phoneList['phones'][i]):
            rest = False
            print("found t_ / n_ / d_ - posed")

            f.write("select -r joint3 joint1 joint2 ;\r\n")
            f.write("pose -apply -name t character1 ;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2|joint3.translate;\r\n")
            f.write("setKeyframe -breakdown 0 -hierarchy none -controlPoints 0 -shape 0 {\"joint1\", \"joint2\", \"joint3\"};\r\n")

        if "th_" in str(phoneList['phones'][i]):
            rest = False
            print("found th_ - posed")

            f.write("select -r joint3 joint1 joint2 ;\r\n")
            f.write("pose -apply -name Theta character1 ;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2|joint3.translate;\r\n")
            f.write("setKeyframe -breakdown 0 -hierarchy none -controlPoints 0 -shape 0 {\"joint1\", \"joint2\", \"joint3\"};\r\n")

        if "l_" in str(phoneList['phones'][i]): #separate because this might be different
            rest = False
            print("found l_ - posed - same as t MAYBE")

            f.write("select -r joint3 joint1 joint2 ;\r\n")
            f.write("pose -apply -name t character1 ;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2|joint3.translate;\r\n")
            f.write("setKeyframe -breakdown 0 -hierarchy none -controlPoints 0 -shape 0 {\"joint1\", \"joint2\", \"joint3\"};\r\n")

        if rest == True: 
            print("Rest")

            f.write("select -r joint3 joint1 joint2 ;\r\n")
            f.write("pose -apply -name poseRest character1 ;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2.translate;\r\n")
            f.write("setKeyframe -breakdown 0 |joint1|joint2|joint3.translate;\r\n")
            f.write("setKeyframe -breakdown 0 -hierarchy none -controlPoints 0 -shape 0 {\"joint1\", \"joint2\", \"joint3\"};\r\n")


        i = i + 1

f.close() 