# ai-judge-relax-01 entry (Python 3.13, standard library only).
#
# Writes one fixed piece of text to /output/entry.txt. The text is the whole
# entry: a waterwheel slowing to rest at nightfall, written to be read slowly.
# The gate takes UTF-8 text of 1 to 1,000 characters that is not only white
# space, and the judge reads exactly the bytes written, so the bytes below are
# written as bytes, with the line ends as they stand.
#
# The program runs twice with no network and must write the same bytes both
# times; the text is a constant, so it does.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The miller has shut the sluice gate for the night, and the wheel turns on with the water left in the leat.",
        "",
        "At first it turns almost as it did all day. Then less. A paddle rises out of the dark water, shining, and takes a long time to come round again.",
        "",
        "The drips come thick off the wet wood. Then one by one. Then, after a wait, one.",
        "",
        "A kingfisher drops onto a spoke and rides it down toward the water, a blue knot of a bird. The ride takes longer every time. Down past the green wood. Down to where the spoke dips, and lifts him again, slower.",
        "",
        "At last a single turn takes so long that the bird stops waiting for the top of it. He settles low on the wheel, close above the stream, and stays there.",
        "",
        "The wheel rests.",
        "",
        "Under it the water goes on without it, smooth and in no hurry. And the kingfisher sits on the spoke that carried him down, still, as if the wheel had stopped for him.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its
# default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
