#  Music Settings
TRACK_DURATION = 150  # individual track length
TRACK_COUNT = 24  # total number of tracks
FADE_IN_SEC = 5  # amount of time for each track to fade in
FADE_OUT_SEC = 12  # amount of time for each track to fade out
MUSIC_MODE = "track"  # mubert specific setting, see api

#  Video Settings
VIDEO_HEIGHT = 512
ASPECT_RATIO = {9:9}
SEED = -1  # set to -1 for random. Only used for testing
VIDEO_WIDTH = round(VIDEO_HEIGHT * ASPECT_RATIO[list(ASPECT_RATIO.keys())[0]] / list(ASPECT_RATIO.keys())[0] / 10) * 10
FRAME_COUNT = 200  # total number of frames in each video. 1000 = ~60 seconds
DIST_BETWEEN = 50  # distance between place prompts
DIFFUSION_CADENCE = 2  # number of frames to wait before diffusion
STRENGTH = 0.8  # amount of presence of previous frame to influence next frame
COLOR_COHERENCE = "LAB"  # determines the variations in color palate. Set to "LAB" for consistent colors throughout
ZOOM_SPEED = 1.03
ROTATION_ANGLE = 0  # angle by which to rotate each frame
ANIMATION_MODE = "2D"  # can set to 3D or 2D


# for description of all parameters,
# see https://dreamingcomputers.com/deforum-stable-diffusion/deforum-stable-diffusion-settings/
