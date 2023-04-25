import config
from tkinter.filedialog import askdirectory
import ffmpeg
import os
import pandas as pd


class ProduceVideo:
    def __init__(self, log_df: pd.DataFrame, bnum, inputs_dir="temp_music", output_path='done/'):
        def get_list_from_directory(directory=""):
            file_list = []
            if directory == "":
                directory = askdirectory()
            for file in os.listdir(directory):
                abs_path = f"{directory}\\{file}"
                split = file.split(".")
                if split[len(split) - 1] != "ini":
                    file_list.append(abs_path)
            return file_list

        def probe_video():
            probe = ffmpeg.probe(self.video_file)
            stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)

            duration = float(stream['duration'])

            fps_raw = stream['avg_frame_rate']
            fps_split = fps_raw.split("/")
            fps = float(int(fps_split[0]) / int(fps_split[1]))

            video_width = int(stream['width'])

            video_height = int(stream['height'])

            frames = int(stream['nb_frames'])

            return (duration, fps, video_width, video_height, frames)

        def probe_audio():
            probe = ffmpeg.probe(self.audio_file)
            stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
            duration = float(stream['duration'])
            return (duration)

        def boomarangify_video(video_file):
            instances = (
                ffmpeg
                .input(video_file)
                .filter_multi_output(filter_name="split", outputs=2)
            )
            ordered_edits = []
            for i in range(2):
                if i % 2 == 0:
                    ordered_edits.append(instances[i])
                else:
                    ordered_edits.append(instances[i].filter(filter_name="reverse"))

            output = (
                ffmpeg
                .concat(*ordered_edits, a=0, v=1)
                .filter(filter_name="loop",loop=-1, size=config.FRAME_COUNT * 2)
                .filter(filter_name="trim", start=0,duration=config.TRACK_DURATION * config.TRACK_COUNT)
                #.output(f"{output_path}test.mp4")
                #.run(overwrite_output=True)
            )
            pass
            return output

        def concat_audio(file_list):
            #  turn files into ffmpeg inputs
            audio_inputs = []
            for file in file_list:
                audio_inputs.append(
                    ffmpeg
                    .input(file)
                    .filter(filter_name="atrim", start=0, duration=config.TRACK_DURATION)
                    .filter(filter_name="afade", type="in", start_time=0, duration=config.FADE_IN_SEC, curve="losi")
                    .filter(filter_name="afade", type="out", start_time=config.TRACK_DURATION - config.FADE_OUT_SEC,
                            duration=config.FADE_OUT_SEC, curve="par")
                    .filter(filter_name="atrim", start=0, duration=config.TRACK_DURATION)
                )
            result = (
                ffmpeg
                .concat(*audio_inputs, v=0, a=1)
                #.output('done/output.mp3')
                #.run(overwrite_output=True)
            )
            return result
            pass
        def get_next_file_index(output_path=output_path):
            num_list = []
            files = os.listdir(output_path)
            if len(files) == 0:
                return 0
            for file in files:
                if len(file.split("_")) == 1:
                    continue
                num = file.split("_")[0]
                is_num = True
                for i in range(len(num)):
                    if num[i] not in "0123456789":
                        is_num = False
                if is_num:
                    num_list.append(int(num))
            if len(num_list) == 0:
                return 0
            return max(num_list) + 1


        pass
        df = log_df.query('bnum == @bnum')
        #  gather video stream
        for index, row in df.iterrows():
            pass
            file = row['idvideo']
            video_file = f"temp_runpod/{file}.mp4"
            video_stream = boomarangify_video(video_file)

            #  gather audio stream
            audio_files = []
            pass
            for id in list(row['idmusic']):
                audio_files.append(f"temp_music/{id}.mp3")
            audio_stream = concat_audio(audio_files)

            #  get title info
            unique_num = get_next_file_index(output_path)
            id = str(row['id'])
            prompt = "_".join(str(row['pmusic']).split(" "))
            pass
            #  produce video
            (
                ffmpeg
                .concat(video_stream, audio_stream, v=1, a=1)
                .output(f"{output_path}{unique_num}_{id}_{prompt}.mp4")
                .run(overwrite_output=True)
            )


