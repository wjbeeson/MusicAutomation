from tkinter.filedialog import askdirectory

import ffmpeg
import os


class ProduceVideo:
    def __init__(self, inputs_dir="inputs", output_path='done/final.mp4'):
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

        def boomarangify_video():
            instances = (
                ffmpeg
                .input(self.video_file)
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
                .filter(filter_name="loop",loop=-1, size=self.frames * 2)
                .filter(filter_name="trim", start=0,duration=self.duration)
                #.output(output_path)
                #.run(overwrite_output=True)
            )
            return output


        self.video_file = ""
        self.audio_file = ""
        files = get_list_from_directory(inputs_dir)
        for file in files:
            if file.split(".")[1] == "mp4":
                self.video_file = file
            if file.split(".")[1] == "mp3":
                self.audio_file = file

        (vdur, fps, video_width, video_height, frames) = probe_video()
        adur = probe_audio()
        self.frames = frames
        self.duration = adur


        video_stream = boomarangify_video()
        (
            ffmpeg
            .concat(video_stream, ffmpeg.input(self.audio_file), v=1, a=1)
            .output(output_path)
            .run(overwrite_output=True)
        )

pv = ProduceVideo()