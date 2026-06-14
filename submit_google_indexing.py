#!/usr/bin/env python3
"""구글 Indexing API 통보 (구글은 IndexNow 미참여이므로 별도 처리).

구글은 sitemap ping(2023년 폐지)을 더 이상 받지 않으므로, 빠른 색인 요청은
Search Console 등록 + sitemap 제출이 기본이고, Indexing API로 개별 URL 갱신을
통보할 수 있다(공식 지원 범위는 JobPosting·BroadcastEvent이지만 URL_UPDATED 통보는 동작).

사전 준비:
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 발급 → 이 파일 옆에 google-sa.json 로 저장
  3) Search Console 속성에 그 서비스 계정 이메일을 "소유자"로 추가
  4) pip install google-auth requests

사용법:
  python3 submit_google_indexing.py            # sitemap.xml 전체 통보(쿼터 200/일 주의)
  python3 submit_google_indexing.py <URL ...>  # 특정 URL만
"""
import re
import sys

SA_FILE = "google-sa.json"
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def urls_from_sitemap():
    with open("sitemap.xml", encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def main():
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        print("의존성이 필요합니다:  pip install google-auth requests")
        return

    import os
    if not os.path.exists(SA_FILE):
        print(f"서비스 계정 키 파일이 없습니다: {SA_FILE}")
        print("README의 '구글 Indexing API' 절차를 따라 발급해 두세요.")
        return

    urls = sys.argv[1:] or urls_from_sitemap()
    creds = service_account.Credentials.from_service_account_file(SA_FILE, scopes=SCOPES)
    session = AuthorizedSession(creds)

    ok = 0
    for url in urls:
        body = {"url": url, "type": "URL_UPDATED"}
        r = session.post(ENDPOINT, json=body)
        status = "OK" if r.status_code == 200 else f"ERR {r.status_code}"
        print(f"  {status}  {url}")
        ok += r.status_code == 200
    print(f"\n구글 Indexing API 통보 완료: {ok}/{len(urls)} (일일 쿼터 기본 200건)")


if __name__ == "__main__":
    main()
