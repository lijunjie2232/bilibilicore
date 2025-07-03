# from moviepy import VideoFileClip, AudioFileClip
import subprocess

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


def combine(
    v,
    a,
    out_file,
    ffmpeg_path="ffmpeg",
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
        f"{v.absolute().__str__()}",
        "-i",
        f"{a.absolute().__str__()}",
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

    cmd.append(f"{out_file.absolute().__str__()}")
    subprocess.run(cmd)
