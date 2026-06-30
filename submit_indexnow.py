#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — Bing·네이버·Yandex·Seznam에 URL 변경을 한 번에 알린다.

사용법:
  python3 submit_indexnow.py                # sitemap.xml 의 전체 URL 통보
  python3 submit_indexnow.py /goyang/ilsandong-gu/baekseok-dong/   # 특정 경로만
  python3 submit_indexnow.py https://goyang-massage.netlify.app/...  # 전체 URL도 가능

동작: 루트의 <KEY>.txt 가 배포되어 있어야 검색엔진이 소유권을 확인한다(빌드가 자동 생성).
외부 라이브러리 없이 표준 라이브러리(urllib)만 사용한다.
새 글을 올리거나 내용을 고친 뒤 이 스크립트를 실행하면 즉시 통보된다.
"""
import json
import re
import sys
import urllib.request
import urllib.error

sys.path.insert(0, ".")
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = BASE.split("://", 1)[-1]
ENDPOINT = "https://api.indexnow.org/indexnow"  # 한 곳에 보내면 참여 엔진끼리 공유


def urls_from_sitemap():
    with open("sitemap.xml", encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def normalize(arg):
    if arg.startswith("http"):
        return arg
    return BASE + "/" + arg.lstrip("/")


def main():
    args = sys.argv[1:]
    urls = [normalize(a) for a in args] if args else urls_from_sitemap()
    if not urls:
        print("통보할 URL이 없습니다."); return

    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    print(f"IndexNow 통보: {len(urls)}개 URL → {ENDPOINT}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"응답 {resp.status} {resp.reason}")
            print("성공: 참여 검색엔진(빙·네이버·Yandex 등)에 색인 요청이 접수되었습니다.")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        print(f"HTTP {e.code}: {body}")
        print("키 파일이 배포(접근 가능)되어 있는지, host가 도메인과 일치하는지 확인하세요.")
    except Exception as e:  # noqa: BLE001
        print(f"오류: {e}")


if __name__ == "__main__":
    main()
