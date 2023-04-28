#  Music Settings
TRACK_DURATION = 150  # individual track length
TRACK_COUNT = 24  # total number of tracks
FADE_IN_SEC = 5  # amount of time for each track to fade in
FADE_OUT_SEC = 12  # amount of time for each track to fade out
MUSIC_MODE = "track"  # mubert specific setting, see api

#  Video Settings
VIDEO_HEIGHT = 720
ASPECT_RATIO = {9:16}
SEED = -1  # set to -1 for random. Only used for testing
VIDEO_WIDTH = round(VIDEO_HEIGHT * ASPECT_RATIO[list(ASPECT_RATIO.keys())[0]] / list(ASPECT_RATIO.keys())[0] / 10) * 10

DIFFUSION_CADENCE = 2  # number of frames to wait before diffusion
COLOR_COHERENCE = "LAB"  # determines the variations in color palate. Set to "LAB" for consistent colors throughout
ANIMATION_MODE = "2D"  # can set to 3D or 2D

# for description of all parameters,
# see https://dreamingcomputers.com/deforum-stable-diffusion/deforum-stable-diffusion-settings/

def channels_dict(channel_id):
  channel_dicts = \
  {
    "zenscend" : {
        #  music
        "streams": ["calm"],
        "intensities": ["high"],
        "ambient_track": "overlay/rain.wav",
        #  video
        "negative": "(fog:1.4), (anime:1.4), (blurry:1.2), (low quality:2), (mono chrome:1.1), (normal quality:2), (ugly:1.2), (worst quality:2), [out of frame], 3d, 3dface, 3drender, acnes, anime, artist name, asian, bad anatomy, bad art, bad hands, bad proportions, blurry, body out of frame, canvas frame, cartoon, cgi, cloned, cloned face, closeup, collapsed eyeshadow, conjoined fingers, copyright, cropped, cross-eye, cut, deformed, deformed fingers, deformed hands, dehydrated, disfigured, distorted, doll, drawing, duplicate, error, extra arms, extra digit, extra fingers, extra legs, extra limbs, fat, fewer digits, fused fingers, girl, gray scale, grey scale, gross proportions, imperfect, imperfect eyes, jpeg artifacts, large breasts, loli, long body, long neck, low resolution, malformed, malformed limbs, missing arms, missing fingers, missing legs, missing limbs, morbid, multiple view, muscular, muscular female, mutated, mutated hands, mutation, mutilated, oversaturated, photoshop, plump, poorly drawn face, poorly drawn feet, poorly drawn hands, red eyes, reference sheet, render, semi-realistic, signature, sketch, sketches, skewed eyes, skin blemishes, skin spots, text, tiling, title, too many fingers, trademark, ugly, ugly eyes, unnatural body, unnatural face, username, vagina, vaginas in breasts, videogame, watermark, weirdcolors, young",
        "positive": '(extremely intricate:1.3), (floating:1.2), (hyperdetailed:1.15), (intricate details:1.12), (masterpiece:1.2), (pandora avatar planet style:1.2), (sharp:1.2), 8k, award winning, beautiful, best quality, blur effect, bright, cinematic, cinematic lighting, cinematic rendering, detailed, detailed background, detailedlight, devian art, digital art, digital painting, dramatic, hdr, high detail, high resolution, highly detailed, illustration, intricate, intricate detail, isolated, long exposure, lots of fine detail, matte drawing, mystical, natural lighting, octane render, oil on matte canvas, photography, raytracing, rich color, sci-fi movie style, sharp details, sharp focus, smooth, soaring, soft light, sunset lighting, the highest detail, the highest quality, the most beautiful artwork in the world, trending artstation, ultra-hd, unreal engine 5, volumetrics dtx, wide shot, wonder',
        "colors": {
          0: ["bright sunny day","dark-green","light-green","tan","light-red"],
          1: ["bright sunny day","black", "dark-blue", "light-green", "light purple"],
          2: ["rainy ambient","orange", "green", "teal", "dark blue"],
          3: ["rainy ambient", "yellow", "green", "brown", "green"]
        },
        "transitions": [['dematerialize', 'nebula', 'rearrange'], ['indoors', 'rotate', 'outdoors'], ['fall', 'underwater', 'emerge'], ['disappear', 'subterranean network'], ['fly', 'fog', 'emerge'], ['fall', 'cave'], ['flip upside down', 'fall', 'in the sky'], ['fade', 'underground system'], ['ascend', 'vast desert', 'glide'], ['descend', 'open plains', 'zoom'], ['fly', 'in the clouds', 'mountains'], ['fly', 'space', 'fly'], ['fall', 'clouds', 'descend'], ['outdoors', 'rotate', 'indoors'], ['rise', 'through the atmosphere'], ['indoors', 'twist', 'outdoors'], ['soar', 'above the treetops', 'valleys'], ['soar', 'galaxy'], ['rise', 'ocean surface', 'dive'], ['levitate', 'dense forest', 'hover'], ['sink', 'marshland', 'float'], ['materialize', 'ancient ruins', 'explore'], ['immerse', 'tropical rainforest', 'ascend'], ['glide', 'over a lake', 'ripple'], ['phase', 'between dimensions', 'resurface'], ['sail', 'across the ocean', 'island'], ['shift', 'through time', 'prehistoric'], ['drift', 'along a river', 'cascade'], ['swim', 'coral reef', 'surface'], ['dance', 'among the stars', 'cosmic'], ['tunnel', 'through a glacier', 'emerge'], ['slide', 'on ice', 'polar landscape'], ['teleport', 'urban skyline', 'descend'], ['rise', 'volcanic landscape', 'descend'], ['traverse', 'mystical landscape', 'shimmer'], ['float', 'ethereal realm', 'transcend'], ['orbit', 'celestial bodies', 'universe'], ['navigate', 'winding canyon', 'soar'], ['plunge', 'into a whirlpool', 'resurface'], ['hover', 'above a meadow'], ['explore', 'ancient city'], ['traverse', 'dense jungle'], ['admire', 'a serene waterfall'], ['shapeshift', 'mystical forest'], ['navigate', 'through a labyrinth'], ['climb', 'a towering mountain'], ['experience', 'a dream world'], ['cross', 'a rickety bridge'], ['race', 'down a sand dune'], ['witness', 'an aurora borealis'], ['venture', 'into a haunted house'], ['sway', 'among treetops'], ['discover', 'a hidden oasis'], ['unravel', 'in a field of flowers'], ['escape', 'a maze of mirrors'], ['follow', 'a moonlit path'], ['encounter', 'a mythical creature'], ['merge', 'with the shadows'], ['bask', 'in a sunlit glade'], ['journey', 'through a realm of clouds'], ['revel', 'in a field of fireflies'], ['glide', 'over rolling hills'], ['penetrate', 'a mysterious fog'], ['drift', 'through a snowscape'], ['uncover', 'a secret garden'], ['amble', 'along a cobblestone street'], ['gaze', 'at a distant horizon'], ['inhabit', 'an enchanted castle'], ['savor', 'a tranquil beach sunset'], ['flow', 'with a gentle stream'], ['perceive', 'a world of illusions'], ['spiral', 'through a vortex', 'emerge'], ['morph', 'among ever-changing clouds', 'shapes'], ['pulsate', 'at the heart of a thunderstorm', 'lightning'], ['bounce', 'atop a field of trampolines', 'soar'], ['splash', 'through a rain-soaked city', 'puddles'], ['scatter', 'amidst a flurry of snowflakes', 'glisten'], ['vibrate', 'within a soundwave landscape', 'resonance'], ['merge', 'among a kaleidoscope of butterflies', 'flutter']],
        "places": ['Golden Temple Peak', 'Verdant Green Temple', 'Serene Mountain Sanctuary', 'Vibrant Jade Mountain', 'Mossy Forest Temple', 'Rustic Pine Ridge', 'Lush Bamboo Grove', 'Pink Lotus Peak', 'Dewy Fern Valley', 'Scenic Hilltop Temple', 'Cedarwood Ridge', 'Mystical Mountain', 'Majestic Oak Grove', 'Tranquil Serenity Peak', 'Blossoming Cherry Blossom', 'Cloudy Temple', 'Zen Mountain', 'Towering Redwood Grove', 'Colorful Wildflower Hill', 'Radiant Golden Peak', 'Sacred Temple Grove', 'Alpine Zen Retreat', 'Blooming Plum Blossom', 'Oasis Temple', 'Lush Mountain Garden', 'Serene Lavender Ridge', 'Panoramic Temple View', 'Blossoming Spring Peak', 'Emerald Green Temple', 'Graceful Willow Glen', 'Secluded Forest Retreat', 'Tranquil Mountain Peak', 'Crystal Mountain Stream', 'Serene Lotus Grove', 'Cedarwood Summit', 'Colorful Sunset Ridge', 'Enchanted Forest Temple', 'Serene Pine Forest', 'Zen Forest Retreat', 'Serene Temple', 'Rainbow', 'Scenic Bamboo Hill', 'Haven Mountain', 'Forest Zen Retreat', 'Garden Temple Oasis', 'Maplewood Ridge', 'Peaceful Mountain Peak', 'Scenic Mountain Path', 'Blossoming Cherry Blossom Hill', 'Tranquil Forest Temple'],
        #  general
        "frames": 2070,  # total number of frames in each video.
        "prompt_dist": 80,  # distance between place prompts
        "rotation_angle": 0,
        "zoom_speed": 1.02,
        "strength": 1,  # amount of presence of previous frame to influence next frame
        "fps": 30,
        "sd_model_name": "DreamShaper_5_beta2_BakedVae-inpainting.inpainting.safetensors",
        "sd_model_hash": "b7ecdada"
    }
  }
  return channel_dicts[channel_id]