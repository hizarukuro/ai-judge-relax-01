# ai-judge-relax-01 draft v2 candidate (Python 3.13, standard library only).
#
# Writes one fixed text to /output/entry.txt: a child asleep on a grandmother's
# lap while her knitting needles slow, space out, and stop. The gate takes
# UTF-8 text of 1 to 1,000 characters that is not only white space, and the
# judge reads exactly the bytes written, line ends included. The program runs
# twice with no network, and both runs must write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "You are asleep before the lamp is warm, curled on the sofa, your head in your grandmother's lap, your shoes still on.",
        "",
        "Above you her needles are going, soft as rain through a roof. Click, and the wool slides. Click, and it slides again.",
        "",
        "She is knitting a scarf nobody asked for. It has grown past her knees, off the sofa, and lies in grey folds on the rug, longer than any neck it will meet.",
        "",
        "After a while the clicks leave more room between them. A stitch. A stitch. Her hands are slowing to keep time with your breathing.",
        "",
        "Once, her thumb leaves the needle and crosses your hair, the way you settle a blanket over someone who never asked. Then the wool again. Click. A while. Click.",
        "",
        "In its basket the ball of yarn turns, smaller each time, and rests.",
        "",
        "Then a click does not come. The needle rests, its stitch half made, and her hand comes down and settles on your hair, and stays.",
        "",
        "The lamp stays on. The scarf can keep till morning. Nothing else is going to happen tonight.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its
# default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
