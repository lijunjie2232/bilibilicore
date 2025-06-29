from bilibilicore.config.config import Config
from pathlib import Path

# from time import sleep
import os
from pydantic import BaseModel

import threading


_QN_240P = 6
_QN_360P = 16
_QN_480P = 32
_QN_720P = 64
_QN_720P_60 = 74
_QN_1080P = 80
_QN_REPAIR = 100
_QN_1080P_PLUS = 112
_QN_1080P_60 = 116
_QN_4K = 120
_QN_HDR = 125
_QN_DB = 126
_QN_8K = 127

_FNVAL_MP4 = 1
_FNVAL_DASH = 16

_VCODEC_AVC = 7
_VCODEC_HEVC = 12
_VCODEC_AV1 = 13

_ACODEC_64K = 30216
_ACODEC_132K = 30232
_ACODEC_192K = 30280
_ACODEC_DB = 30250
_ACODEC_HR = 30251

_CHUNK_SIZE = 1024 * 64


class DashStream(BaseModel):
    """
    {
        "id": 16,
        "baseUrl": "https://upos-sz-mirroraliov.bilivideo.com/upgcxcode/25/69/30165696925/30165696925-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&mid=400477783&gen=playurlv3&og=cos&nbs=1&platform=pc&trid=93d73bf740c9439c8ebf069735295d0u&deadline=1751174552&os=aliovbv&uipk=5&oi=1860816950&upsig=2d885aa6ecda69be68abd4b0d9cfad1d&uparams=e,mid,gen,og,nbs,platform,trid,deadline,os,uipk,oi&bvc=vod&nettype=0&bw=47473&buvid=&build=0&dl=0&f=u_0_0&agrr=0&orderid=0,2",
        "base_url": "https://upos-sz-mirroraliov.bilivideo.com/upgcxcode/25/69/30165696925/30165696925-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&mid=400477783&gen=playurlv3&og=cos&nbs=1&platform=pc&trid=93d73bf740c9439c8ebf069735295d0u&deadline=1751174552&os=aliovbv&uipk=5&oi=1860816950&upsig=2d885aa6ecda69be68abd4b0d9cfad1d&uparams=e,mid,gen,og,nbs,platform,trid,deadline,os,uipk,oi&bvc=vod&nettype=0&bw=47473&buvid=&build=0&dl=0&f=u_0_0&agrr=0&orderid=0,2",
        "backupUrl": [
            "https://upos-hz-mirrorakam.akamaized.net/upgcxcode/25/69/30165696925/30165696925-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&oi=1860816950&mid=400477783&gen=playurlv3&deadline=1751174552&nbs=1&trid=93d73bf740c9439c8ebf069735295d0u&os=akam&og=cos&uipk=5&platform=pc&upsig=6a9650cbdc0229d56c465d2e1c0e2ab4&uparams=e,oi,mid,gen,deadline,nbs,trid,os,og,uipk,platform&hdnts=exp=1751174552~hmac=99279350ca0855a0435cd7504178606d1b53ef39f95ddac37c5d866ea66ce117&bvc=vod&nettype=0&bw=47473&buvid=&build=0&dl=0&f=u_0_0&agrr=0&orderid=1,2"
        ],
        "backup_url": [
            "https://upos-hz-mirrorakam.akamaized.net/upgcxcode/25/69/30165696925/30165696925-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&oi=1860816950&mid=400477783&gen=playurlv3&deadline=1751174552&nbs=1&trid=93d73bf740c9439c8ebf069735295d0u&os=akam&og=cos&uipk=5&platform=pc&upsig=6a9650cbdc0229d56c465d2e1c0e2ab4&uparams=e,oi,mid,gen,deadline,nbs,trid,os,og,uipk,platform&hdnts=exp=1751174552~hmac=99279350ca0855a0435cd7504178606d1b53ef39f95ddac37c5d866ea66ce117&bvc=vod&nettype=0&bw=47473&buvid=&build=0&dl=0&f=u_0_0&agrr=0&orderid=1,2"
        ],
        "bandwidth": 47411,
        "mimeType": "video/mp4",
        "mime_type": "video/mp4",
        "codecs": "avc1.640033",
        "width": 640,
        "height": 360,
        "frameRate": "30.000",
        "frame_rate": "30.000",
        "sar": "1:1",
        "startWithSap": 1,
        "start_with_sap": 1,
        "SegmentBase": {
            "Initialization": "0-966",
            "indexRange": "967-2162"
        },
        "segment_base": {
            "initialization": "0-966",
            "index_range": "967-2162"
        },
        "codecid": 7
    }
    """

    id: int
    base_url: str
    backup_url: list[str]
    bandwidth: int
    mime_type: str
    codecs: str
    frame_rate: str
    codecid: int


class DurlStream(BaseModel):
    """
    {
        "order": 1,
        "length": 483301,
        "size": 12109469,
        "ahead": "",
        "vhead": "",
        "url": "https://upos-hz-mirrorakam.akamaized.net/upgcxcode/25/69/30165696925/30165696925-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&nbs=1&uipk=5&oi=1860816950&gen=playurlv3&deadline=1751176394&platform=pc&trid=98de3b1b13624862ba296f1d145b5a5u&mid=400477783&os=akam&og=hw&upsig=f9d7350e586c3cac64f3fc7bcd0114ae&uparams=e,nbs,uipk,oi,gen,deadline,platform,trid,mid,os,og&hdnts=exp=1751176394~hmac=85c46d0372dd0a04b6c6405dae0f20f24082c5330886ff5e65532ea911734dd3&bvc=vod&nettype=0&bw=200570&dl=0&f=u_0_0&agrr=0&buvid=&build=0&orderid=0,2",
        "backup_url": [
            "https://upos-sz-mirroraliov.bilivideo.com/upgcxcode/25/69/30165696925/30165696925-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&deadline=1751176394&nbs=1&trid=98de3b1b13624862ba296f1d145b5a5u&og=hw&oi=1860816950&mid=400477783&uipk=5&platform=pc&gen=playurlv3&os=aliovbv&upsig=065e11f90cf47d09debfaf5f9e5ed95e&uparams=e,deadline,nbs,trid,og,oi,mid,uipk,platform,gen,os&bvc=vod&nettype=0&bw=200570&agrr=0&buvid=&build=0&dl=0&f=u_0_0&orderid=1,2"
        ]
    }
    """

    order: int
    length: int
    size: int
    ahead: str
    vhead: str
    url: str
    backup_url: str


class Stream(ApiClass):
    def __init__(
        self,
        v,
        a=None,
        name=None,
        dir=None,
        cache_dir=Config().cache_dir,
        out_fmt="mp4",
    ):
        self.v = v
        self.a = a
        self.cache_dir = cache_dir
        self.dir = Path(dir or cache_dir)
        self.name = name
        assert name, "name is required"
        self.fmt = out_fmt
        self.dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def clean_tmp(self, *files):
        for file in files:
            if file.exists():
                file.unlink()

    def get_stream(self):
        if isinstance(self.v, DashStream):
            ori_fmt = "m4s"
            if len(self.v.base_url.split("?")[0].split(".")) > 2:
                ori_fmt = self.v.base_url.split("?")[0].split(".")[-1]
            out_video_name = f"{self.name}_v.{ori_fmt}"
            out_audio_name = f"{self.name}_a.{ori_fmt}"
            tmp_video_path = self.cache_dir / f".{out_video_name}"
            tmp_audio_path = self.cache_dir / f".{out_audio_name}"
            out_path = self.dir / f"{self.name}.{self.fmt}"

            try:
                with self.__SESSION__.get(
                    self.v.base_url,
                    stream=True,
                ) as r:
                    with open(
                        tmp_video_path,
                        "wb",
                    ) as f:
                        for chunk in r.iter_content(_CHUNK_SIZE):
                            f.write(chunk)
            except Exception:
                with self.__SESSION__.get(
                    self.v.backup_url,
                    stream=True,
                ) as r:
                    with open(
                        tmp_video_path,
                        "wb",
                    ) as f:
                        for chunk in r.iter_content(_CHUNK_SIZE):
                            f.write(chunk)
            try:
                with self.__SESSION__.get(
                    self.a.base_url,
                    stream=True,
                ) as r:
                    with open(
                        tmp_audio_path,
                        "wb",
                    ) as f:
                        for chunk in r.iter_content(_CHUNK_SIZE):
                            f.write(chunk)
            except Exception:
                with self.__SESSION__.get(
                    self.a.backup_url,
                    stream=True,
                ) as r:
                    with open(
                        tmp_audio_path,
                        "wb",
                    ) as f:
                        for chunk in r.iter_content(_CHUNK_SIZE):
                            f.write(chunk)
            from bilibilicore.utils import combine

            combine(
                v=tmp_video_path,
                a=tmp_audio_path,
                out_file=out_path,
                fmt=None if self.fmt != ori_fmt else None,
            )
            self.clean_tmp(
                tmp_video_path,
                tmp_audio_path,
            )
        else:
            raise NotImplementedError()
