sample_input1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
sample_input2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
sample_input3 = "nppdvjthqldpwncqszvftbrmjlhg"
sample_input4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
sample_input5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


def detect_marker(dat: str, limit=4):
    for i in range(limit, len(dat)):
        packet = dat[i - limit : i]
        if len(set(packet)) == limit:
            return i


assert detect_marker(sample_input1) == 7
assert detect_marker(sample_input2) == 5
assert detect_marker(sample_input3) == 6
assert detect_marker(sample_input4) == 10
assert detect_marker(sample_input5) == 11
