# from moviepy import VideoFileClip, AudioFileClip
import subprocess

import av

VIDEO_CODEC_MAP = {
    ".mp4": "libx264",  # H.264 codec (default for MP4)
    ".avi": "mpeg4",  # MPEG-4 codec (common for AVI)
    ".ogv": "libvorbis",  # Ogg Vorbis (open format)
    ".webm": "libvpx",  # VP8/VP9 codec (web-friendly)
    ".mkv": "libx264",  # H.264 in MKV container
    ".mov": "libx264",  # H.264 in QuickTime
    ".flv": "libx264",  # H.264 in Flash
    ".3gp": "libx264",  # H.264 for mobile
    # Additional codecs
    "rawvideo": "rawvideo",  # Uncompressed (huge files)
    "png": "png",  # Lossless compression
    "libx265": "libx265",  # HEVC/H.265 (4K support)
    "av1": "libaom-av1",  # Open AV1 codec
}

AUDIO_CODEC_MAP = {
    ".mp3": "libmp3lame",  # MP3 format
    ".ogg": "libvorbis",  # Ogg Vorbis
    ".webm": "libvorbis",  # Default for WebM
    ".m4a": "libfdk_aac",  # AAC format
    ".wav": "pcm_s16le",  # 16-bit PCM
    ".flac": "flac",  # Lossless FLAC
    ".aac": "aac",  # Advanced Audio Codec
    ".ac3": "ac3",  # Dolby Digital
    # Special cases
    "raw32": "pcm_s32le",  # 32-bit PCM
    "opus": "libopus",  # Low-latency audio
}


def merge_audio_video(video_path, audio_path, output_path):
    # 打开视频和音频文件
    video_container = av.open(video_path)
    audio_container = av.open(audio_path)

    # 创建输出容器
    output_container = av.open(output_path, mode="w")

    # 复制视频流
    video_stream = video_container.streams.video[0]
    output_video_stream = output_container.add_stream(template=video_stream)

    # 复制音频流
    audio_stream = audio_container.streams.audio[0]
    output_audio_stream = output_container.add_stream(template=audio_stream)

    # 从视频文件中读取数据包并写入输出容器
    for packet in video_container.demux(video_stream):
        output_container.mux(output_video_stream.encode(packet))

    # 从音频文件中读取数据包并写入输出容器
    for packet in audio_container.demux(audio_stream):
        output_container.mux(output_audio_stream.encode(packet))

    # 关闭文件容器
    video_container.close()
    audio_container.close()
    output_container.close()


def combine(
    v,
    a,
    out_file,
    ffmpeg_path="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe",
    fmt=None,
    overwrite=False,
):

    # video = VideoFileClip(v)
    # if a:
    #     audio = AudioFileClip(a)
    #     setattr(
    #         video,
    #         "audio",
    #         audio,
    #     )
    # if fmt:
    #     video.write_videofile(
    #         out_file,
    #         codec=VIDEO_CODEC_MAP.get(f".{fmt}"),
    #     )
    # else:
    #     video.write_videofile(
    #         out_file,
    #     )
    cmd = [
        f"{ffmpeg_path}",
        "-i",
        f"{v.absolute().as_posix()}",
        "-i",
        f"{a.absolute().as_posix()}",
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-strict",
        "experimental",
    ]
    if overwrite:
        cmd.append("-y")
    if fmt:
        cmd.extend(
            [
                "-f",
                f"{fmt}",
            ]
        )

    cmd.append(f"{out_file.absolute().as_posix()}")
    subprocess.run(cmd)
