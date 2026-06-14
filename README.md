# 고양 출장마사지 · 고양시 홈타이 지역 SEO 사이트

간다GO(전화예약 **0508-202-4719**) 고양 출장마사지·홈타이 지역 SEO 정적 사이트입니다.
구글 SEO·네이버 검색 설명문·스키마·내부링크 기준을 반영해 자동 생성합니다.

## 페이지 구성 (총 60페이지)

| 구분 | 개수 |
|------|------|
| 메인 | 1 |
| 행정구 (덕양구·일산동구·일산서구) | 3 |
| 대표 행정동 (1·2·3동은 대표 동으로 통합) | 30 |
| 지하철역 (환승역은 1개로 통합) | 21 |
| 기타 (예약·확인사항·가이드·고객센터·개인정보) | 5 |

## 구조 / SEO

- **URL**: 메인 `/`, 행정구 `/goyang/<구>-gu-chuljangmassage/`, 행정동 `/goyang/<구>/<동>-chuljangmassage/`, 역 `/goyang/<역>-station-chuljangmassage/`
- **각 페이지**: 고유 Title·H1·본문 / 네이버 Description(80자 이내) / canonical / OG 태그
- **JSON-LD**: `BreadcrumbList` + `WebPage` + `Organization`
- **중복 방지**: 지역별 생활권·동선·주변 정보를 다르게 작성, 번호 동·환승역 통합
- `sitemap.xml`, `robots.txt` 자동 생성

## 빌드

```bash
python3 generate.py     # → public/ 에 정적 사이트 생성
```

배포 전 `generate.py` 상단의 `SITE_URL` 값을 실제 도메인으로 변경하세요
(canonical·OG·스키마·sitemap에 반영됩니다).

## 배포

`public/` 디렉터리를 그대로 정적 호스팅(Netlify, Cloudflare Pages, GitHub Pages 등)에
도메인 루트로 올리면 됩니다. 내부 링크는 루트 절대경로(`/goyang/...`)를 사용합니다.

## 콘텐츠 정책

합법적인 방문형 관리 안내 사이트 기준으로 작성되었으며, 불법·선정적 표현, 허위 후기,
과장 광고, 가짜 주소 기반 LocalBusiness 스키마는 사용하지 않습니다.
