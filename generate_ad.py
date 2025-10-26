from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip, concatenate_videoclips
import numpy as np

class VideoGenerator:
    def __init__(self):
        self.clips = []

    def create_text_clip(self, text, duration, fontsize=70):
        """Creates a text clip."""
        return TextClip(text, fontsize=fontsize, color='white').set_duration(duration)

    def add_rain_effect(self, clip):
        """Applies a rain effect to a given clip."""
        rain = np.random.rand(clip.h, clip.w, 3) * 255  # Simple random rain effect
        rain_clip = VideoFileClip(rain, ismask=True).set_duration(clip.duration)
        return CompositeVideoClip([clip.set_opacity(0.5), rain_clip])

    def add_scene(self, clip):
        """Adds a scene to the video."""
        self.clips.append(clip)

    def generate_full_video(self):
        """Generates the full video from the added clips."""
        final_clip = concatenate_videoclips(self.clips)
        final_clip.write_videofile("final_video.mp4", fps=24)

# Example usage
if __name__ == "__main__":
    video_gen = VideoGenerator()
    text_clip = video_gen.create_text_clip("Welcome to Video Generation", duration=5)
    video_gen.add_scene(text_clip)
    
    # Assuming you have a background clip to add rain effect
    # background_clip = VideoFileClip("background.mp4")
    # rain_effect_clip = video_gen.add_rain_effect(background_clip)
    # video_gen.add_scene(rain_effect_clip)
    
    video_gen.generate_full_video()