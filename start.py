import os
import platform

if platform.system() == "Darwin":
    os.system("python3 wake_word_util.py --model_path resources/ko.pv --keyword_paths resources/vanilla_mac.ppn --sensitivities 0.8")
else:
    os.system("python3 wake_word_util.py --model_path resources/ko.pv --keyword_paths resources/vanilla.ppn --sensitivities 0.8")