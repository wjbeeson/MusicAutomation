# see https://dreamingcomputers.com/deforum-stable-diffusion/deforum-stable-diffusion-settings/
class Channel:
    def __init__(self, id, music_channels, music_intensities, ambient_track, track_duration, track_count, fade_in_sec, fade_out_sec
                 , music_mode, negative_end, positive_end, places, video_frames, place_dist, rotation_angle, zoom_speed
                 , y_movement, diffusion_strength, fps, seed, video_height, video_width, color_coherence, diffusion_cadence
                 , animation_mode, sd_model_name, sd_model_hash):
        self.id = id
        self.music_channels = music_channels
        self.music_intensities = music_intensities
        self.ambient_track = ambient_track
        self.track_duration = track_duration
        self.track_count = track_count
        self.fade_in_sec = fade_in_sec
        self.fade_out_sec = fade_out_sec
        self.music_mode = music_mode

        self.negative_end = negative_end
        self.positive_end = positive_end
        self.places = places
        self.video_frames = video_frames
        self.place_dist = place_dist
        self.rotation_angle = rotation_angle
        self.zoom_speed = zoom_speed
        self.y_movement = y_movement
        self.diffusion_strength = diffusion_strength
        self.fps = fps
        self.seed = seed
        self.video_height = video_height
        self.video_width = video_width
        self.color_coherence = color_coherence
        self.diffusion_cadence = diffusion_cadence
        self.animation_mode = animation_mode
        self.sd_model_name = sd_model_name
        self.sd_model_hash = sd_model_hash


def get_channel(id):

    if id == 'zenscend':
        return Channel(
            id='zenscend',
            #  music
            track_count=24,
            track_duration=150,
            music_channels=["calm"],
            music_intensities=["high"],
            ambient_track="overlay/rain.wav",
            fade_in_sec=5,
            fade_out_sec=10,
            music_mode="TRACK",

            #  video control
            fps=30,
            video_height=720,
            video_width=1280,
            video_frames=2250,
            place_dist=100,
            animation_mode="2D",
            diffusion_strength=1,
            diffusion_cadence=2,
            rotation_angle=0,
            zoom_speed=1.02,
            y_movement=-1.02,

            #  video prompting
            positive_end='(otherwordly terrain:2),(muted colors:1.4), (extremely intricate:1.3), (hyperdetailed:1.15), (intricate details:1.12), (masterpiece:1.2), (planets in sky:1.2), (sharp:1.2), 8k, award winning, beautiful, best quality, blur effect, clear water, bright, cinematic, cinematic lighting, cinematic rendering, detailed, detailed background, detailed light, devian art, digital art, digital painting, dramatic, hdr, high detail, high resolution, highly detailed, illustration, intricate, isolated, long exposure, lots of fine detail, matte drawing, mystical, natural lighting, octane render, oil on matte canvas, photography, raytracing, rich color, sci-fi movie style, sharp details, sharp focus, smooth, soaring, soft light, sunset lighting, the highest detail, the highest quality, the most beautiful artwork in the world, trending artstation, ultra-hd, unreal engine 5, volumetrics dtx, wide shot, wonder',
            negative_end="(fog:2), (anime:1.4),(overgrown:1.4), (blurry:1.2), (low quality:2), (mono chrome:1.2), (normal quality:2), (ugly:1.2), (worst quality:2), [out of frame], 3d, 3dface, 3drender, acnes, anime, artist name, asian, bad anatomy, bad art, bad hands, bad proportions, blurry, body out of frame, canvas frame, cartoon, cgi, cloned, cloned face, closeup, collapsed eyeshadow, conjoined fingers, copyright, cropped, cross-eye, cut, deformed, deformed fingers, deformed hands, dehydrated, disfigured, distorted, doll, drawing, duplicate, error, extra arms, extra digit, extra fingers, extra legs, extra limbs, fat, fewer digits, fused fingers, girl, gray scale, grey scale, gross proportions, imperfect, imperfect eyes, jpeg artifacts, large breasts, loli, long body, long neck, low resolution, malformed, malformed limbs, missing arms, missing fingers, missing legs, missing limbs, morbid, multiple view, muscular, muscular female, mutated, mutated hands, mutation, mutilated, oversaturated, photoshop, plump, poorly drawn face, poorly drawn feet, poorly drawn hands, red eyes, reference sheet, render, semi-realistic, signature, sketch, sketches, skewed eyes, skin blemishes, skin spots, text, tiling, title, too many fingers, trademark, ugly, ugly eyes, unnatural body, unnatural face, username, vagina, vaginas in breasts, videogame, watermark, weirdcolors, young",
            places=['Golden Temple Peak', 'Verdant Green Temple', 'Serene Mountain Sanctuary', 'Vibrant Jade Mountain', 'Mossy Forest Temple', 'Rustic Pine Ridge', 'Ancient Bamboo Grove', 'Pink Lotus Peak', 'Dewy Fern Valley', 'Scenic Hilltop Temple', 'Cedarwood Ridge', 'Mystical Mountain', 'Majestic Oak Grove', 'Tranquil Serenity Peak', 'Blossoming Cherry Blossom', 'Cloudy Temple', 'Zen Mountain', 'Towering Redwood Grove', 'Colorful Wildflower Hill', 'Radiant Golden Peak', 'Sacred Temple Grove', 'Alpine Zen Retreat', 'Blooming Plum Blossom', 'Oasis Temple', 'Lush Mountain Garden', 'Serene Lavender Ridge', 'Panoramic Temple View', 'Blossoming Spring Peak', 'Emerald Green Temple', 'Graceful Willow Glen', 'Secluded Forest Retreat', 'Tranquil Mountain Peak', 'Crystal Mountain Stream', 'Serene Lotus Grove', 'Cedarwood Summit', 'Colorful Sunset Ridge', 'Enchanted Forest Temple', 'Serene Pine Forest', 'Zen Forest Retreat', 'Serene Temple', 'Rainbow', 'Scenic Bamboo Hill', 'Haven Mountain', 'Forest Zen Retreat', 'Garden Temple Oasis', 'Maplewood Ridge', 'Peaceful Mountain Peak', 'Scenic Mountain Path', 'Blossoming Cherry Blossom Hill', 'Tranquil Forest Temple'],

            #  misc
            seed=-1,
            color_coherence="LAB",
            sd_model_name="DreamShaper_5_beta2_BakedVae-inpainting.inpainting.safetensors",
            sd_model_hash="b7ecdada"
        )

    elif id == "sliceoflofi":
        return Channel(
            id='sliceoflofi',
            #  music
            track_count=24,
            track_duration=150,
            music_channels=["calm"],
            music_intensities=["low","low","low","medium"],
            ambient_track="overlay/rain.wav",
            fade_in_sec=5,
            fade_out_sec=10,
            music_mode="TRACK",
            #  video control
            fps=30,
            video_height=720,
            video_width=1280,
            video_frames=2250,
            place_dist=100,
            animation_mode="2D",
            diffusion_strength=1,
            diffusion_cadence=2,
            rotation_angle=0,
            zoom_speed=1.02,
            y_movement=-1.02,
            #  video prompting
            positive_end='medieval japan, extremely detailed CG unity 8k wallpaper, (bright color:0.2), <lora:howls:0.5>',
            negative_end="(birds:2),(fog:2), (blurry:2), (low quality:2), (mono chrome:1.2), (normal quality:2), (ugly:1.2), (worst quality:2), [out of frame], 3d, 3dface, 3drender, acnes, anime, artist name, asian, bad anatomy, bad art, bad hands, bad proportions, blurry, body out of frame, canvas frame, cartoon, cgi, cloned, cloned face, closeup, collapsed eyeshadow, conjoined fingers, copyright, cropped, cross-eye, cut, deformed, deformed fingers, deformed hands, dehydrated, disfigured, distorted, doll, drawing, duplicate, error, extra arms, extra digit, extra fingers, extra legs, extra limbs, fat, fewer digits, fused fingers, girl, gray scale, grey scale, gross proportions, imperfect, imperfect eyes, jpeg artifacts, large breasts, loli, long body, long neck, low resolution, malformed, malformed limbs, missing arms, missing fingers, missing legs, missing limbs, morbid, multiple view, muscular, muscular female, mutated, mutated hands, mutation, mutilated, oversaturated, photoshop, plump, poorly drawn face, poorly drawn feet, poorly drawn hands, red eyes, reference sheet, render, semi-realistic, signature, sketch, sketches, skewed eyes, skin blemishes, skin spots, text, tiling, title, too many fingers, trademark, ugly, ugly eyes, unnatural body, unnatural face, username, vagina, vaginas in breasts, videogame, watermark, weirdcolors, young",
            places=['A charming village nestled in the mountains, with lanterns lining the streets, a lively festival in the town square, and the night sky ablaze with stars.','A serene riverbank with rows of cherry blossom trees, colorful lanterns hanging overhead, and a floating lantern festival at night.','A rustic countryside with a tranquil lake, a lively summer festival with fireworks, and a magical meteor shower that can be seen from the hilltops at night.','A traditional Japanese garden with a picturesque pond, a tea ceremony held by lantern light, and a summer festival featuring an outdoor theatre performance under the stars.','A cozy town with a winding river, a night market selling handmade crafts and delicious street food, and a stunning display of aurora borealis in the winter sky.','A charming seaside town with a sandy beach, a lively summer festival featuring taiko drum performances and a bonfire on the shore, and a starry night sky perfect for stargazing.','A quaint farming village with a rice paddy field, a harvest festival featuring traditional dance and music, and a breathtaking view of the Milky Way galaxy in the night sky.','A tranquil forest with a hidden waterfall, a lantern-lit hiking trail leading to a scenic lookout point, and a meteor shower that can be viewed from the forest clearing at night.','A picturesque mountain town with a hot spring resort, a lantern-lit ski slope at night, and a stunning display of the Northern Lights in the winter sky.','A traditional temple town with a historic shrine, a lantern-lit ceremony held at night, and a star-filled sky that is said to bring good fortune to those who make a wish upon it.','A charming coastal village with a lighthouse, a lantern-lit fishing festival at night, and a breathtaking view of the full moon rising over the sea.','A rustic mountain town with a secret hot spring, a lantern-lit hike through the forest to a hidden waterfall, and a meteor shower that can be seen from the mountaintop.','A historic castle town with a cherry blossom festival, a lantern-lit night parade, and a stunning view of the fireworks display over the castle moat.','A quaint lakeside village with a water lantern festival, a traditional dance performance under the stars, and a view of the constellations reflecting in the still waters of the lake.','A traditional temple town with a lantern-lit night market, a tea ceremony by the riverbank, and a view of the starry sky from the temple courtyard.','A charming countryside with a field of sunflowers, a summer festival featuring taiko drum performances and fireworks, and a view of the Milky Way galaxy over the horizon.','A serene bamboo forest with a lantern-lit path, a traditional dance performance by moonlight, and a view of the shooting stars in the clear night sky.','A cozy town with a winter festival featuring ice sculptures and a hot springs soak, a lantern-lit snowshoe hike, and a view of the aurora borealis over the snowy landscape.','A picturesque mountain village with a lantern-lit night hike to a shrine, a traditional music performance, and a view of the meteor shower over the peaks.','A hidden valley with a waterfall, a lantern-lit camping trip, and a view of the stars reflected in the crystal-clear waters of the pool.','A quaint seaside village with a fishing festival, a lantern-lit bonfire on the beach, and a view of the bioluminescence in the ocean waves.','A tranquil riverbank with a cherry blossom viewing picnic, a traditional Japanese dance performance by the water, and a view of the stars in the clear night sky.','A historic castle town with a moon viewing festival, a tea ceremony under the full moon, and a view of the fireworks display over the castle walls.','A rustic mountain village with a hot springs soak, a lantern-lit hike through the forest to a hidden shrine, and a view of the shooting stars in the night sky.','A charming countryside with a field of fireflies, a summer festival featuring traditional music and dance, and a view of the Milky Way galaxy over the horizon.','A serene bamboo forest with a tea ceremony, a lantern-lit meditation walk, and a view of the stars in the clear night sky.','A cozy town with a winter festival featuring snow sculptures and a hot springs soak, a lantern-lit snowshoe hike, and a view of the aurora borealis over the snowy landscape.','A picturesque mountain village with a lantern-lit night hike to a secret hot spring, a traditional music performance, and a view of the meteor shower over the peaks.','A tranquil lake with a cherry blossom viewing boat ride, a traditional dance performance by the water, and a view of the stars in the clear night sky.','A historic castle town with a lantern-lit night market, a tea ceremony under the castle walls, and a view of the fireworks display over the moat.','A charming seaside village with a summer festival featuring taiko drum performances and a bonfire on the beach, and a view of the Milky Way','A mystical forest with a lantern-lit path, a traditional dance performance by the moonlight, and a view of the shooting stars in the clear night sky.','A cozy town with a winter festival featuring ice skating, a hot springs soak, and a view of the aurora borealis over the snowy landscape.','A hidden shrine in the mountains with a lantern-lit path, a traditional music performance, and a view of the stars in the clear night sky.','A charming countryside with a field of lavender, a summer festival featuring traditional Japanese games and dance, and a view of the Milky Way galaxy over the horizon.','A serene bamboo forest with a tea ceremony, a lantern-lit meditation walk, and a view of the stars in the clear night sky.','A picturesque seaside town with a fishing festival, a bonfire on the beach, and a view of the bioluminescence in the ocean waves.','A historic temple town with a lantern-lit night market, a tea ceremony in the temple gardens, and a view of the fireworks display over the nearby lake.','A rustic mountain village with a hot springs soak, a lantern-lit hike to a waterfall, and a view of the shooting stars in the night sky.','A charming riverside town with a traditional dance performance, a cherry blossom viewing picnic, and a view of the stars reflected in the tranquil river.','A tranquil lake with a water lantern festival, a traditional music performance by the water, and a view of the stars in the clear night sky.','A hidden bamboo grove with a tea ceremony, a lantern-lit meditation walk, and a view of the shooting stars in the clear night sky.','A historic castle town with a lantern-lit night parade, a tea ceremony under the castle walls, and a view of the fireworks display over the moat.','A charming seaside village with a summer festival featuring traditional Japanese games and dance, and a view of the Milky Way galaxy over the horizon.','A cozy town with a winter festival featuring snow sculptures and a hot springs soak, a lantern-lit snowshoe hike, and a view of the aurora borealis over the snowy landscape.','A picturesque mountain village with a night hike to a secret hot spring, a traditional music performance, and a view of the meteor shower over the peaks.','A mystical forest with a lantern-lit path, a traditional dance performance by the moonlight, and a view of the shooting stars in the clear night sky.','A charming countryside with a field of sunflowers, a summer festival featuring taiko drum performances and fireworks, and a view of the Milky Way galaxy over the horizon.','A tranquil riverbank with a cherry blossom viewing picnic, a traditional Japanese dance performance by the water, and a view of the stars reflected in the calm waters.','A serene bamboo grove with a tea ceremony, a lantern-lit meditation walk, and a view of the stars in the clear night sky.','A picturesque seaside town with a fishing festival, a bonfire on the beach, and a view of the bioluminescence in the ocean waves.','A historic temple town with a lantern-lit night market, a tea ceremony in the temple gardens, and a view of the fireworks display over the nearby lake.','A rustic mountain village with a hot springs soak, a lantern-lit hike to a waterfall, and a view of the shooting stars in the night sky.','A charming riverside town with a traditional dance performance, a cherry blossom viewing picnic, and a view of the stars reflected in the tranquil river.','A tranquil lake with a water lantern festival, a traditional music performance by the water, and a view of the stars in the clear night sky.','A hidden bamboo grove with a tea ceremony, a lantern-lit meditation walk, and a view of the shooting stars in the clear night sky.','A historic castle town with a lantern-lit night parade, a tea ceremony under the castle walls, and a view of the fireworks display over the moat.','A charming seaside village with a summer festival featuring traditional Japanese games and dance, and a view of the Milky Way galaxy over the horizon.','A cozy town with a winter festival featuring snow sculptures and a hot springs soak, a lantern-lit snowshoe hike, and a view of the aurora borealis over the snowy landscape.','A tranquil riverbank with a cherry blossom viewing picnic, a traditional Japanese dance performance by the water, and a view of the stars reflected in the calm waters.','A hidden temple in the mountains with a traditional music performance, a lantern-lit meditation walk, and a view of the stars in the clear night sky.','A charming countryside with a field of wildflowers, a summer festival featuring food stalls and traditional Japanese dance, and a view of the Milky Way galaxy over the horizon.','A picturesque mountain village with a night hike to a secret hot spring, a traditional music performance, and a view of the meteor shower over the peaks.','A mystical forest with a lantern-lit path, a traditional dance performance by the moonlight, and a view of the shooting stars in the clear night sky.','A cozy seaside town with a summer festival featuring fireworks, a beach bonfire, and a view of the bioluminescence in the ocean waves.','A historic castle town with a cherry blossom viewing picnic, a tea ceremony in the castle gardens, and a view of the stars reflected in the moat waters.','A rustic mountain village with a hot springs soak, a lantern-lit hike to a nearby waterfall, and a view of the shooting stars in the clear night sky.','A charming riverside town with a traditional dance performance, a cherry blossom viewing picnic, and a view of the stars reflected in the tranquil river.','A tranquil lake with a water lantern festival, a traditional music performance by the water, and a view of the stars in the clear night sky.','A hidden shrine in the mountains with a traditional music performance, a lantern-lit meditation walk, and a view of the stars in the clear night sky.','A charming countryside with a field of sunflowers, a summer festival featuring taiko drum performances and fireworks, and a view of the Milky Way galaxy over the','A picturesque mountain town with a night hike to a secluded hot spring, a traditional music performance, and a view of the meteor shower over the peaks.','A mystical forest with a lantern-lit path, a traditional dance performance by the moonlight, and a view of the shooting stars in the clear night sky.','A cozy seaside village with a summer festival featuring fireworks, a beach bonfire, and a view of the bioluminescence in the ocean waves.','A historic castle town with a cherry blossom viewing picnic, a tea ceremony in the castle gardens, and a view of the stars reflected in the moat waters.','A rustic mountain village with a hot springs soak, a lantern-lit hike to a nearby waterfall, and a view of the shooting stars in the clear night sky.','A charming riverside town with a traditional dance performance, a cherry blossom viewing picnic, and a view of the stars reflected in the tranquil river.','A tranquil lake with a water lantern festival, a traditional music performance by the water, and a view of the stars in the clear night sky.','A hidden shrine in the mountains with a traditional music performance, a lantern-lit meditation walk, and a view of the stars in the clear night sky.','A peaceful bamboo forest with a tea ceremony, a lantern-lit meditation walk, and a view of the stars in the clear night sky.','A serene seaside town with a fishing festival, a bonfire on the beach, and a view of the bioluminescence in the ocean waves.','A historic temple town with a lantern-lit night market, a tea ceremony in the temple gardens, and a view of the fireworks display over the nearby lake.','A rustic mountain village with a hot springs soak, a lantern-lit hike to a waterfall, and a view of the shooting stars in the night sky.','A charming riverside town with a traditional dance performance, a cherry blossom viewing picnic, and a view of the stars reflected in the tranquil river.','A tranquil lake with a water lantern festival, a traditional music performance by the water, and a view of the stars in the clear night sky.','A hidden bamboo grove with a tea ceremony, a lantern-lit meditation walk, and a view of the shooting stars in the clear night sky.','A historic castle town with a lantern-lit night parade, a tea ceremony under the castle walls, and a view of the fireworks display over the moat.','A charming seaside village with a summer festival featuring traditional Japanese games and dance, and a view of the Milky Way galaxy over the horizon.','A cozy town with a winter festival featuring snow sculptures and a hot springs soak, a lantern-lit snowshoe hike, and a view of the aurora borealis over the snowy landscape.','A serene riverbank with a cherry blossom viewing picnic, a traditional Japanese dance performance by the water, and a view of the stars reflected in the calm waters.','A hidden temple in the mountains with a traditional music performance, a lantern-lit meditation walk, and a view of the stars in the clear night sky.','A charming countryside with a field of wildflowers, a summer festival featuring food stalls and traditional Japanese dance, and a view of the Milky Way galaxy over the horizon.','A picturesque mountain village with a night hike to a secret hot spring, a traditional music performance, and a view of the meteor shower over the peaks.','A mystical forest with a lantern-lit path, a traditional dance performance by the moonlight, and a view of the shooting stars in the clear night sky.','A seaside town with a summer festival featuring fireworks, a beach bonfire, and a view of the bioluminescence in the ocean waves.','A historic castle town with a cherry blossom viewing picnic, a tea ceremony in the castle gardens, and a view of the stars reflected in the moat waters.','A rustic mountain village with a hot springs soak, a lantern-lit hike to a nearby waterfall, and a view of the shooting stars in the clear night sky.','A charming riverside town with a traditional dance performance, a cherry blossom viewing picnic, and a view of the stars reflected in the tranquil river.','A tranquil lake with a water lantern festival, a traditional music performance by the water, and a view of the stars in the clear night sky.','A hidden shrine in the mountains with a traditional music performance, a lantern-lit meditation walk, and a view of the stars in the clear night sky.'],
            #  misc
            seed=-1,
            color_coherence="LAB",
            sd_model_name="DreamShaper_5_beta2_BakedVae-inpainting.inpainting.safetensors",
            sd_model_hash="b7ecdada"
        )

    elif id == "midnightacademia":
        return Channel(
            id='sliceoflofi',
            #  music
            track_count=24,
            track_duration=150,
            music_channels=["calm"],
            music_intensities=["low", "low", "low", "medium"],
            ambient_track="overlay/rain.wav",
            fade_in_sec=5,
            fade_out_sec=10,
            music_mode="TRACK",
            #  video control
            fps=30,
            video_height=720,
            video_width=1280,
            video_frames=2250,
            place_dist=100,
            animation_mode="2D",
            diffusion_strength=1,
            diffusion_cadence=2,
            rotation_angle=0,
            zoom_speed=1.02,
            y_movement=-1.02,
            #  video prompting
            positive_end='',
            negative_end='',
            places=[],
            #  misc
            seed=-1,
            color_coherence="LAB",
            sd_model_name="DreamShaper_5_beta2_BakedVae-inpainting.inpainting.safetensors",
            sd_model_hash="b7ecdada"
        )

    elif id == "melodream":
        return Channel(
            id='melodream',
            #  music
            track_count=24,
            track_duration=150,
            music_channels=["psychill"],
            music_intensities=["low", "low", "low", "medium"],
            ambient_track="",
            fade_in_sec=5,
            fade_out_sec=10,
            music_mode="TRACK",
            #  video control
            fps=30,
            video_height=720,
            video_width=1280,
            video_frames=2250,
            place_dist=100,
            animation_mode="2D",
            diffusion_strength=1,
            diffusion_cadence=2,
            rotation_angle=0,
            zoom_speed=1.02,
            y_movement=-1.02,
            #  video prompting
            positive_end='',
            negative_end='',
            places=[],
            #  misc
            seed=-1,
            color_coherence="LAB",
            sd_model_name="DreamShaper_5_beta2_BakedVae-inpainting.inpainting.safetensors",
            sd_model_hash="b7ecdada"
        )

    elif id == "tokyojazzcafe":
        return Channel(
            id='tokyojazzcafe',
            #  music
            track_count=24,
            track_duration=150,
            music_channels=["acidjazz"],
            music_intensities=["low", "low", "low", "medium"],
            ambient_track="",
            fade_in_sec=5,
            fade_out_sec=10,
            music_mode="TRACK",
            #  video control
            fps=30,
            video_height=720,
            video_width=1280,
            video_frames=2250,
            place_dist=100,
            animation_mode="2D",
            diffusion_strength=1,
            diffusion_cadence=2,
            rotation_angle=0,
            zoom_speed=1.02,
            y_movement=-1.02,
            #  video prompting
            positive_end='',
            negative_end='',
            places=[],
            #  misc
            seed=-1,
            color_coherence="LAB",
            sd_model_name="DreamShaper_5_beta2_BakedVae-inpainting.inpainting.safetensors",
            sd_model_hash="b7ecdada"
        )
    else:
        raise Exception(f'Invalid Channel ID: [{id}]')