# ai-judge-relax-01 entry (Python 3.13, standard library only).
#
# Writes one fixed piece of text to /output/entry.txt: a mill wheel turning
# on the last of the channel's water after the sluice is shut for the night,
# slowing by degrees until it stops with a kingfisher settled on a spoke.
# The text is the whole entry; nothing else is computed.
#
# The gate takes UTF-8 text of 1 to 1,000 characters that is not only white
# space, and the judge reads exactly the bytes written, line ends included,
# so the text below is written as bytes. The program runs twice with no
# network and must write the same bytes both times; the text is a constant,
# so it does.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "At dusk the miller shuts the gate at the head of the channel, and the wheel turns on only the water the channel holds.",
        "",
        "It goes round as it did at noon. Then slower. A board climbs out of the stream, water sheeting off it, and is a long while coming back around.",
        "",
        "Drops fall close together off the wet rim. Then one at a time. Then one gathers, hangs, and falls, and the wait for the next one is longer still.",
        "",
        "Out of the half-light a kingfisher drops onto a spoke and rides it down. The wheel lowers him toward the water an inch at a time, each descent slower than the one before.",
        "",
        "In the end one turning is so slow that the bird no longer waits for the top. He settles low on the wheel, just above the stream, and stays.",
        "",
        "And then the wheel is still.",
        "",
        "Underneath, the water slides on alone, smooth and in no hurry. The kingfisher sits motionless on the spoke that carried him down, as though the wheel had spent the evening slowing down just for him.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its
# default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
