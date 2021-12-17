m1 = "ABCDEFG"; musicinfos1 = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]  # "HELLO"
m2 = "CC#BCC#BCC#BCC#B"; musicinfos2 = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]  # "FOO"
m3 = "ABC"; musicinfos3 = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]  # "WORLD"


def split_music(music):
    new_music = []
    i = 0
    while i < len(music):
        if i+1 < len(music):
            if music[i+1] == '#':
                new_music.append(music[i:i+2])
                i += 1
            else:
                new_music.append(music[i])
        else:
            new_music.append(music[i])
        i += 1
    return new_music

def split_infos(musicinfo):
    start, end, title, music = musicinfo.split(',')
    start = start.split(':')
    start = int(start[0])*60 + int(start[1])
    end = end.split(':')
    end = int(end[0])*60 + int(end[1])
    time = end-start
    music = split_music(music)
    music = (music * (time//len(music)+1))[:time]
    return title, music, time

def solution(m, musicinfos):
    m = split_music(m)
    answer = ('(None)', 0)
    for musicinfo in musicinfos:
        title, music, time = split_infos(musicinfo)
        for i in range(len(music)-len(m)+1):
            if music[i:i+len(m)] == m and answer[1] < time:
                answer = (title, time)
                break
    return answer[0]


print(solution(m1, musicinfos1))
print(solution(m2, musicinfos2))
print(solution(m3, musicinfos3))