from moviepy.editor import VideoFileClip

clip = VideoFileClip("./FASTER_Community_Çalıştay_Türkiye_Senior_Developer_vs_Junior_ONE.mp4")
clip.write_gif("junior.gif", fps=20)