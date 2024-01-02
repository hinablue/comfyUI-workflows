# Prompt Schedule Helper
# Created by Hina Chen (hinablue)
# Version: 1.0
# https://blog.hinablue.me

import re
from collections import defaultdict

class promptScheduleHelper:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": {
                "frame_1": ("INT", {
                    "default": 0,
                    "min": 0
                }),
                "text_1": ("STRING", {
                    "multiline": True,
                    "default": "",
                }),
                "frame_2": ("INT", {
                    "default": 12,
                    "min": 0
                }),
                "text_2": ("STRING", {
                    "multiline": True,
                    "default": "",
                }),
                "frame_3": ("INT", {
                    "default": 24,
                    "min": 0
                }),
                "text_3": ("STRING", {
                    "multiline": True,
                    "default": "",
                }),
                "frame_4": ("INT", {
                    "default": 36,
                    "min": 0
                }),
                "text_4": ("STRING", {
                    "multiline": True,
                    "default": "",
                }),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "combinePromptScheduleToText"
    CATEGORY = "advanced"

    def combinePromptScheduleToText(self, text_in_opt="", frame_1=0, text_1="", frame_2=0, text_2="", frame_3=0, text_3="", frame_4=0, text_4=""):
        frames = []

        if text_in_opt != "":
            for data in text_in_opt.split(',\n'):
                m = re.search(r"\"([0-9]+)\": \"(.*)\",?", data) # 0: frame, 1: text
                if m:
                    frames.append((int(m.group(1)), m.group(2)))

        if text_1 != "" and frame_1 >= 0:
            text_1 = text_1.replace('\n', ', ').replace('"', '\\"').replace(',,', ',')
            frames.append((frame_1, text_1))
        if text_2 != "" and frame_2 >= 0:
            text_2 = text_2.replace('\n', ', ').replace('"', '\\"').replace(',,', ',')
            frames.append((frame_2, text_2))
        if text_3 != "" and frame_3 >= 0:
            text_3 = text_3.replace('\n', ', ').replace('"', '\\"').replace(',,', ',')
            frames.append((frame_3, text_3))
        if text_4 != "" and frame_4 >= 0:
            text_4 = text_4.replace('\n', ', ').replace('"', '\\"').replace(',,', ',')
            frames.append((frame_4, text_4))

        frame_dict = defaultdict(tuple)

        for frame, text in frames:
            frame_dict[frame] += (text,)

        # print(frame_dict)

        prompt = []
        for frame in sorted(frame_dict.keys()):
            prompt.append('"' + str(frame) + '": "' + ', '.join(frame_dict[frame]) + '"')

        return (',\n'.join(prompt), )

NODE_CLASS_MAPPINGS = {
    "PromptScheduleHelper": promptScheduleHelper
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptScheduleHelper": "Prompt Schedule Helper"
}
