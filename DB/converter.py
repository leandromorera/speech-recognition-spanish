
file1 = open('transcript.txt', 'r')#), encoding='utf-8')
Lines = file1.readlines()
 
count = 0
txline=[]
txline.append('[')
# Strips the newline character
for line in Lines[0:len(Lines)-3]:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    if len(line.strip().split('|')[0])>1 and len(line.strip().split('|')[1])>1:
        txline.append('{"path": '+'"'+line.strip().split('|')[0]+'","text": '+'"'+line.strip().split('|')[1]+'"},')

txline.append('{"path": '+'"'+Lines[len(Lines)-2].strip().split('|')[0]+'","text": '+'"'+Lines[len(Lines)-2].strip().split('|')[1]+'"},')
f = open("nuevo.json", "w")#,encoding='utf-8')
f.write("".join(txline))
f.close()

'''[
  {
    "path": "path/to/audio/file1.wav",
    "text": "hello world"
  },
  {
    "path": "path/to/audio/file2.wav",
    "text": "goodbye world"
  }
]'''

