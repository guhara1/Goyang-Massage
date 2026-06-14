# 간다GO · 고양 출장마사지 · 홈타이 지역 SEO 사이트

경기도 고양시 방문 관리(출장마사지·홈타이) 지역 SEO 사이트입니다.
"다크 럭스 스파" 디자인 + 데이터 기반 정적 빌드 구조로, 구글/네이버 SEO·스팸 정책을 준수해 제작되었습니다.

- 상호: **간다GO**
- 예약전화: **0508-202-4719**
- 배포 도메인: https://goyang-massage.pages.dev

## 페이지 구성 (총 88페이지 · 색인 86)

| 구분 | 개수 |
|------|------|
| 메인 | 1 |
| 고양시 지역 허브 | 1 |
| 자치구 허브 (덕양구·일산동구·일산서구) | 3 |
| 대표 행정동 (1·2·3동 통합) | 30 (덕양 15 · 일산동 8 · 일산서 7) |
| 지하철역 (환승역 단일 페이지) | 21 + 허브 1 |
| 테마 | 14 + 허브 1 |
| 매거진 | 6 + 허브 1 |
| 정보 (massage·courses·reservation·guide·reviews·support) | 6 |
| 운영자 소개 / 약관 2종 | 3 |

## SEO·콘텐츠 원칙

- **대표 동 단위만** 운영 — 숫자 행정동(화정1·2동 등)은 대표 동으로 통합, 도어웨이 페이지 금지
- **역 1개당 페이지 1개** — 대곡역 등 환승역도 URL 하나, 출구별·역+테마 조합 페이지 없음
- 색인 페이지 본문 **2,000자 이상** (요금 블록 제외 측정) — 미달 시 빌드가 자동 noindex
- 페이지마다 **고유 타이틀·디스크립션·본문** (중복 0, 깨진 내부링크 0, JSON-LD 오류 0 — 감사 통과)
- JSON-LD: 메인 `HealthAndBeautyBusiness` + `FAQPage`, 매거진 `Article`
- `sitemap.xml` / `robots.txt` 자동 생성 (색인 페이지만 포함)
- 합법적 방문형 관리 안내 톤 — 불법·선정적·허위 표현 미사용

## 기술 구조

```
build.py            레이아웃·TOC·글자수 검사·sitemap 생성 빌드 스크립트
content/
  site.py           BASE_URL·상호·전화·메뉴(NAV)
  main.py           메인 (히어로 + JSON-LD)
  areas.py          고양시 허브 + 자치구 허브 3 + 대표 동 30 (조립)
  stations.py       역 허브 + 21개 역 (조립)
  themes.py         테마 허브 + 14개
  info.py           정보 페이지 + 약관
  magazine.py       매거진 허브 + 아티클
  about.py          운영자 소개 (E-E-A-T)
  pricing.py        공용 요금 블록
  _data_*.py        동·역 본문 데이터 (지역별 분리)
assets/             style.css, nav.js, favicon, og-image
PLAYBOOK.md         사이트 제작·복제 플레이북
```

## 빌드

```bash
python3 build.py     # → 저장소 루트에 정적 HTML 생성 + 글자수 리포트
```

배포 도메인 변경 시 `content/site.py`의 `BASE_URL`만 수정 후 재빌드하세요.

## 배포 (Cloudflare Pages)

정적 파일이 저장소 루트에 생성됩니다. Cloudflare Pages에서 이 저장소를 연결한 뒤:

- **Production branch**: `main`
- **Framework preset**: None
- **Build command**: `python3 build.py`
- **Build output directory**: `/`

빌드 없이 올릴 경우 `python3 build.py` 결과(루트의 `index.html`, `goyang/`, `assets/` 등)를 그대로 업로드하면 됩니다.

## 색인(인덱싱) 설정 — 네이버·구글·빙 빠른 색인

빌드 시 자동 생성되는 파일:

- `sitemap.xml` — 색인 페이지 86개, `lastmod`·`changefreq`·`priority` 포함
- `rss.xml` — 전체 콘텐츠 피드(네이버·피드 색인 가속), 모든 페이지 `<head>`에 자동발견 링크 삽입
- `robots.txt` — 두 사이트맵(`sitemap.xml`, `rss.xml`) 안내, 전 크롤러 허용
- `<INDEXNOW_KEY>.txt` — IndexNow 소유 확인 키 파일 (루트)
- 메인페이지 `<head>`에 네이버 사이트 소유확인 메타태그

### 1. 네이버 서치어드바이저
1. https://searchadvisor.naver.com → 사이트 등록 (`https://goyang-massage.pages.dev/`)
2. 소유확인: **HTML 태그** 방식 — 메인페이지에 이미 메타태그가 삽입되어 있어 바로 확인됨
3. 요청 → **사이트맵 제출**: `sitemap.xml`, 그리고 **RSS 제출**: `rss.xml`

### 2. 구글 서치 콘솔
1. https://search.google.com/search-console → 속성 추가(URL 접두어)
2. 소유확인 후 **Sitemaps**에 `sitemap.xml` 제출
   - 구글은 2023년부터 sitemap ping(자동 핑)을 폐지 → Search Console 제출이 표준
3. 개별 URL 즉시 색인은 아래 Indexing API 사용

### 3. IndexNow — 빙·네이버·Yandex 즉시 통보 (글 올릴 때마다)
키 파일(`<KEY>.txt`)이 도메인 루트에 **배포된 뒤** 실행하세요.
```bash
python3 submit_indexnow.py                       # sitemap 전체 통보
python3 submit_indexnow.py /goyang/.../baekseok-dong/   # 특정 글만
```
> IndexNow는 빙·네이버·Yandex·Seznam이 키를 공유하므로 한 번 전송으로 모두 통보됩니다.

### 4. 구글 Indexing API (선택, 구글은 IndexNow 미참여)
1. Google Cloud에서 **Indexing API** 사용 설정 → 서비스 계정 JSON 키 발급 → `google-sa.json` 으로 저장(깃 제외됨)
2. Search Console 속성에 그 서비스 계정 이메일을 **소유자**로 추가
3. `pip install google-auth requests` 후:
```bash
python3 submit_google_indexing.py     # sitemap 전체(일일 쿼터 200)
```

### 새 글/수정 후 권장 루틴
```bash
python3 build.py            # 재빌드(사이트맵·RSS 갱신)
git add -A && git commit -m "..." && git push   # 배포
python3 submit_indexnow.py  # 빙·네이버 즉시 통보
python3 submit_google_indexing.py   # (선택) 구글 통보
```
