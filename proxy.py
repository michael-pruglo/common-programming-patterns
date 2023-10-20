#!/usr/bin/env python3

from abc import ABC, abstractmethod


class ThirdPartyYTLib:
    @abstractmethod
    def list_videos(self): pass
    @abstractmethod
    def get_video_info(self, id): pass
    @abstractmethod
    def download_video(self, id): pass

class ThirdPartyYTClass(ThirdPartyYTLib):
    def list_videos(self):
        print("sending API request to get list from YT")
        return ["m2j_Y", "7oJe", "3MMo_"]
    def get_video_info(self, id):
        print(f"request metadata about {id}")
        return "bitrate, codec"
    def download_video(self, id):
        print(f"downloading {id}")

class CachedYTClass(ThirdPartyYTLib):
    def __init__(self, service):
        self.service = service
        self.list_cache = []
        self.info_cache = ""
        self.downloaded_list = set()
    def list_videos(self):
        if not self.list_cache:
            self.list_cache = self.service.list_videos()
        return self.list_cache
    def get_video_info(self, id):
        if not self.info_cache:
            self.info_cache = self.service.get_video_info(id)
        return self.info_cache
    def download_video(self, id):
        if id not in self.downloaded_list:
            self.service.download_video(id)
            self.downloaded_list.add(id)


if __name__ == "__main__":
    proxy = CachedYTClass(ThirdPartyYTClass())
    for _ in range(10):
        proxy.list_videos()
        proxy.get_video_info(17)
        proxy.download_video(17)
