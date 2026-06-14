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
