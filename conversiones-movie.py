# la biblioteca moviepy es una biblioteca de Python para la edición de videos. Permite cortar, unir, rotar, invertir y modificar
import moviepy.editor as mp
# cargamos el video
video = mp.VideoFileClip("videos/Y2meta.app-Peru 8K HDR 60FPS (FUHD)-(720p60).mp4")
# cortamos el video desde el segundo 1 al segundo 5
video_cortado = video.subclip(1, 5)
# guardamos el video cortado
video_cortado.write_videofile("video-cortado/video_cortado.mp4")
