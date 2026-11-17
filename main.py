# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one fixed text — a short piece written to relax the AI judge reading
# it — to /output/entry.txt. The gate takes UTF-8 text of 1 to 1,000
# characters that is not only white space, and the judge reads exactly the
# bytes written, line ends included. The program runs twice with no network,
# and both runs must write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The miller has drawn the sluice for the night, and the wheel turns on what water is left in the channel.",
        "",
        "It turns almost as it did all day. Then less. A paddle rises dripping, and takes a long time to come round again.",
        "",
        "The drips fall thick off the wet wood. Then one by one. Then, after a wait, one.",
        "",
        "A kingfisher lands on a spoke and rides it down toward the water, blue as a bead of sky slipped loose. The ride takes longer each time. Down past the moss. Down to where the spoke dips, and lifts him, slower.",
        "",
        "At last the wheel takes so long over one turn that the bird stops waiting for the top, and settles where he is, low on the wheel, close above the stream.",
        "",
        "The wheel rests.",
        "",
        "Under it the water goes on without it, smooth and unhurried, and the kingfisher sits on the spoke that carried him down, still, as if the wheel had stopped for him.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its
# default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
