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
            music_channels=["zen"],
            music_intensities=["low", "low", "medium", "medium", "high", "high"],
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
            music_channels=["lofi"],
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
            id='midnightacademia',
            #  music
            track_count=24,
            track_duration=150,
            music_channels=["classical"],
            music_intensities=["low", "low", "medium", "medium", "high", "high"],
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
            music_channels=["atmospheric", "chillrave", "dramatic"],
            music_intensities=["low", "high", "high"],
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
            animation_mode="3D",
            diffusion_strength=0.3,
            diffusion_cadence=2,
            rotation_angle=2,
            zoom_speed=1.02,
            y_movement=-1.02,
            #  video prompting
            positive_end='3D, colorful, swirls, abstract, extremely detailed CG unity 8k wallpaper, <lora:psych-face:0.8>',
            negative_end='(blurry:2.0),(worst quality:2.0)',
            places=['A collection of colorful shapes and pattierns that morph and overlap in a mesmerizing and trippy pyschedelic way','A landscape that combines natural elements with impossible dreamlike features to create a surreal and trippy pyschedelic scene','A trippy pyschedelic artwork that represents the complexity and ever-changing nature of thoughts and emotions using vibrant colors and intricate designs','A pyschedelic representation of the universe that explodes with stars planets and galaxies forming intricate patterns and shapes','A trippy pyschedelic interpretation of a jungle or forest filled with strange and exotic plants animals and creatures that are both beautiful and unsettling','A series of pyschedelic mesmerizing optical illusions that play with the viewer','s perception of depth motion and space using vibrant colors and intricate patterns','A pyschedelic cityscape that defies the laws of physics with towering buildings twisting roads and impossible architecture','A trippy pyschedelic artwork that uses abstract forms and patterns to represent the inner workings of the human body','A trippy pyschedelic interpretation of an underwater scene with bizarre creatures and plants that glow in the dark pulsate with color and move in hypnotic patterns','A trippy pyschedelic artwork that uses intricate patterns and swirling colors to represent the ever-changing nature of time','A swirling vortex of neon colors with intricate patterns that spiral into the center of the canvas','An abstract interpretation of sound waves with vibrant colors and dynamic shapes that represent the energy and movement of music','A cosmic dance of planets and stars with each celestial body moving in sync to create a mesmerizing and trippy scene','A psychedelic forest of glowing mushrooms with intricate patterns and vibrant colors that pulse and morph as the viewer moves through the scene','A trippy underwater world of bioluminescent creatures with vibrant colors and hypnotic patterns that create a surreal and dreamlike atmosphere','A kaleidoscope of fractal patterns with intricate details and vibrant colors that create a mesmerizing and hypnotic effect','A surreal cityscape that combines elements of different cultures eras and styles with towering buildings that glow with neon lights and intricate patterns','A trippy interpretation of the human brain with vibrant colors and intricate patterns that represent the complexity and interconnectedness of neural networks','A cosmic explosion of color with vibrant hues and swirling patterns that create a mesmerizing and trippy scene','A surreal landscape of crystal formations with intricate patterns and vibrant colors that create a mesmerizing and otherworldly effect','A mandala of intricate patterns and vibrant colors with each layer representing a different state of consciousness','A surreal dreamscape with impossible features and trippy patterns that create a mesmerizing and surreal atmosphere','A kaleidoscope of abstract forms and patterns with each shape morphing and shifting into new and mesmerizing patterns','A psychedelic interpretation of a neon cityscape with towering buildings and intricate patterns that create a mesmerizing and trippy atmosphere','A cosmic journey through time and space with swirling patterns and vibrant colors that represent the infinite expanse of the universe','An underwater scene of bioluminescent creatures with intricate patterns and vibrant colors that pulse and glow in the dark','A trippy interpretation of the human heart with intricate patterns and vibrant colors that represent the energy and rhythm of life','A surreal landscape of twisted trees and glowing flowers with vibrant colors and trippy patterns that create a mesmerizing and otherworldly atmosphere','A cosmic dance of planets and stars with each celestial body moving in sync to create a mesmerizing and trippy scene','An abstract interpretation of the human soul with vibrant colors and intricate patterns that represent the depth and complexity of the human spirit','A trippy interpretation of the human eye with intricate patterns and vibrant colors that represent the inner workings of vision','A surreal underwater scene of glowing jellyfish with intricate patterns and vibrant colors that create a mesmerizing and dreamlike atmosphere','A cosmic explosion of vibrant colors and swirling patterns with each shape and color representing a different aspect of the universe','A trippy interpretation of the human nervous system with intricate patterns and vibrant colors that represent the interconnectedness of the body and mind','A psychedelic interpretation of a city at night with towering buildings and intricate patterns that create a mesmerizing and trippy atmosphere','A surreal landscape of glowing crystals and trippy patterns with each shape and color representing a different aspect of the natural world','A cosmic journey through the multiverse with intricate patterns and vibrant colors that represent the infinite possibilities of existence','A trippy interpretation of the human ear with intricate patterns and vibrant colors that represent the complexity and beauty of sound','A surreal dreamscape of floating islands and glowing clouds with vibrant colors and trippy patterns that create a mesmerizing and surreal atmosphere','An abstract interpretation of the human mind with vibrant colors and intricate patterns that represent the ever-changing nature of thoughts and emotions','A trippy interpretation of the human respiratory system with intricate patterns and vibrant colors that represent the flow of air and energy through the body','A surreal landscape of twisted vines and glowing flowers with vibrant colors and trippy patterns that create a mesmerizing and otherworldly atmosphere','A cosmic dance of galaxies and black holes with swirling patterns and vibrant colors that represent the complexity and beauty of the universe','A trippy interpretation of the human digestive system with intricate patterns and vibrant colors that represent the flow of nutrients and energy through the body','A psychedelic interpretation of a futuristic cityscape with towering buildings and intricate patterns that create a mesmerizing and trippy atmosphere','A surreal dreamscape of floating islands and glowing clouds with vibrant colors and trippy patterns that create a mesmerizing and surreal atmosphere','An abstract interpretation of the human soul with vibrant colors and intricate patterns that represent the depth and complexity of the human spirit','A psychedelic face with bright colors and distorted features','A portrait of a person with a melting face and exaggerated eyes','An abstract face with a variety of shapes and patterns','A face with multiple eyes and mouths, inspired by a hallucination','A portrait with a symmetrical face and asymmetrical patterns','A portrait with a distorted, elongated face and swirling colors','A face with exaggerated features and intricate, psychedelic details','A portrait with an abstract, trippy design and a kaleidoscope of colors','An asymmetrical face with a mix of realistic and abstract elements','A portrait with a mandala-like pattern incorporated into the face','A face with a third eye and cosmic, psychedelic imagery','An abstract, multi-dimensional face with vibrant colors and intricate details','A portrait with a surreal, dreamlike quality and psychedelic colors','A face with a distorted, trippy effect and neon colors','A portrait with a mix of realistic and abstract features, and vibrant colors','A face with a colorful, abstract background and exaggerated features','An asymmetrical face with trippy, psychedelic patterns and colors','A portrait with a hypnotic, spiraling effect and intense colors','A face with a surreal, otherworldly quality and intricate details','An abstract face with a mix of geometric shapes and patterns, and bold colors','A portrait with a distorted, trippy effect and a chaotic, abstract background','A face with a cosmic, psychedelic theme and bright colors','An asymmetrical face with abstract, trippy details and bold colors'],            #  misc
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
            music_channels=["lounge"],
            music_intensities=["low"],
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
            positive_end='japanese, extremely detailed CG unity 8k wallpaper, <lora:cafe:0.8>',
            negative_end='monochrome, (blurry:2.0), (worst quality:2.0)',
            places=['Indoor daytime cafe with traditional tatami mats and low tables','Outdoor nighttime cafe with lanterns and cherry blossom trees','Indoor daytime cafe with a sushi bar and open kitchen','Outdoor nighttime cafe with a zen garden and koi pond','Indoor daytime cafe with a tea ceremony room and matcha sweets','Outdoor nighttime cafe with a yukata rental service','Indoor daytime cafe with a display of Japanese ceramics and pottery','Outdoor nighttime cafe with a bonfire and mochi making station','Indoor daytime cafe with a karaoke room and J-pop music','Outdoor nighttime cafe with a stargazing platform and telescope','Indoor daytime cafe with a calligraphy corner and ink painting display','Outdoor nighttime cafe with a traditional dance performance stage','Indoor daytime cafe with a tofu making workshop and soy milk drinks','Outdoor nighttime cafe with a summer festival themed decorations','Indoor daytime cafe with a flower arrangement class and ikebana displays','Outdoor nighttime cafe with a hot spring foot bath and yukata robes','Indoor daytime cafe with a bento box lunch menu and rice ball snacks','Outdoor nighttime cafe with a live taiko drumming show','Indoor daytime cafe with a zen meditation corner and incense burning','Outdoor nighttime cafe with a karakuri puppet theater performance','Indoor daytime cafe with a display of traditional Japanese toys and games','Outdoor nighttime cafe with a moon viewing event and Japanese poetry reading','Indoor daytime cafe with a calligraphy workshop and brush pen supplies','Outdoor nighttime cafe with a projection mapping show on a nearby building','Indoor daytime cafe with a soba noodle making class and dipping sauce','Outdoor nighttime cafe with a cherry blossom viewing party and sake tasting','Indoor daytime cafe with a display of Japanese paper art and origami kits','Outdoor nighttime cafe with a summer fireworks display and kakigori shaved ice','Indoor daytime cafe with a display of Japanese fashion and kimono rental service','Outdoor nighttime cafe with a traditional Japanese tea ceremony and wagashi sweets.','Indoor daytime cafe with a pottery painting studio and kiln','Outdoor nighttime cafe with a lantern parade and street food vendors','Indoor daytime cafe with a library of Japanese literature and manga comics','Outdoor nighttime cafe with a garden party and beer garden','Indoor daytime cafe with a Japanese whiskey tasting and cigar lounge','Outdoor nighttime cafe with a light-up bamboo forest and acoustic music','Indoor daytime cafe with a calligraphy exhibition and art sale','Outdoor nighttime cafe with a traditional dance and music festival','Indoor daytime cafe with a display of Japanese bonsai trees and gardening supplies','Outdoor nighttime cafe with a night market and souvenir shops','Indoor daytime cafe with a display of Japanese dolls and figurines','Outdoor nighttime cafe with a light-up torii gate and sake bar','Indoor daytime cafe with a display of Japanese swords and martial arts equipment','Outdoor nighttime cafe with a sumo wrestling tournament and food trucks','Indoor daytime cafe with a display of Japanese lacquerware and pottery','Outdoor nighttime cafe with a lantern-lit boat ride and river views','Indoor daytime cafe with a calligraphy and painting competition','Outdoor nighttime cafe with a street art festival and live mural painting','Indoor daytime cafe with a display of Japanese traditional masks and theater props','Outdoor nighttime cafe with a mochitsuki rice cake pounding ceremony and street performers.'],
            #  misc
            seed=-1,
            color_coherence="LAB",
            sd_model_name="DreamShaper_5_beta2_BakedVae-inpainting.inpainting.safetensors",
            sd_model_hash="b7ecdada"
        )
    else:
        raise Exception(f'Invalid Channel ID: [{id}] Please check config for spelling.')

