# -*- coding: utf-8 -*-
"""
고양 출장마사지 · 고양시 홈타이 지역 SEO 사이트 정적 생성기
- 메인 1 + 행정구 3 + 대표 행정동 30 + 지하철역 21 + 기타 5 = 60 페이지
- 1·2·3동은 대표 행정동으로 통합
- 각 페이지: 고유 Title/H1/본문, 네이버 Description(80자 이내),
  Canonical, BreadcrumbList/WebPage/Organization JSON-LD, 내부링크
"""
import os
import html
import shutil

# ── 사업자/사이트 기본 정보 (배포 시 SITE_URL만 실제 도메인으로 변경) ──
BIZ_NAME = "간다GO"
BIZ_PHONE = "0508-202-4719"
BIZ_PHONE_TEL = "0508-202-4719"
SITE_URL = "https://goyang-massage.kr"   # ← 실제 도메인으로 교체
SITE_TITLE = "고양 출장마사지｜고양시 홈타이 지역별 예약 안내"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")

# ──────────────────────────────────────────────────────────────────────────
# 행정구
# slug, 한글명, Title, Description(<=80), 리드 문단, 대표 생활권 요약
DISTRICTS = {
    "deogyang": {
        "name": "덕양구",
        "url": "/goyang/deogyang-gu-chuljangmassage/",
        "title": "덕양구 출장마사지｜고양 홈타이 방문 가능 지역 안내",
        "desc": "덕양구 출장마사지·홈타이 예약 전 화정, 행신, 삼송 생활권을 확인하세요.",
        "lead": (
            "덕양구는 고양시에서 서울 접근성이 가장 강한 생활권입니다. 화정·행신 같은 "
            "기존 주거 상권과 삼송·원흥·창릉처럼 새로 형성된 신도시·택지지구가 함께 섞여 "
            "있어, 출장마사지를 찾을 때도 본인이 있는 동네가 어느 생활권에 속하는지 먼저 "
            "확인하는 것이 좋습니다. 3호선·경의중앙선·서해선·GTX-A가 모두 지나가는 "
            "교통 요지여서 방문 동선이 동마다 조금씩 다릅니다."
        ),
        "summary": "화정·행신·삼송·원흥·창릉·능곡 중심",
    },
    "ilsandong": {
        "name": "일산동구",
        "url": "/goyang/ilsandong-gu-chuljangmassage/",
        "title": "일산동구 출장마사지｜백석·마두·정발산 홈타이 예약 안내",
        "desc": "일산동구 출장마사지·홈타이 예약 전 백석, 마두, 장항 정보를 정리했습니다.",
        "lead": (
            "일산동구는 일산 중심 상권과 오피스 수요가 함께 모여 있는 생활권입니다. "
            "백석·마두·정발산은 3호선 생활권으로 업무지구와 주거가 가깝게 붙어 있고, "
            "장항동은 라페스타·웨스턴돔·호수공원과 연결되는 상권 수요가 큽니다. "
            "풍산·식사·중산·고봉처럼 경의중앙선과 외곽 주거권으로 나뉘는 지역도 있어 "
            "예약 전 방문 가능 동선을 동별로 확인하는 것이 좋습니다."
        ),
        "summary": "백석·마두·정발산·장항·풍산·식사 중심",
    },
    "ilsanseo": {
        "name": "일산서구",
        "url": "/goyang/ilsanseo-gu-chuljangmassage/",
        "title": "일산서구 출장마사지｜대화·주엽·탄현 홈타이 이용 가이드",
        "desc": "일산서구 출장마사지·홈타이 예약 전 대화, 주엽, 탄현 생활권을 확인하세요.",
        "lead": (
            "일산서구는 주거지와 킨텍스 생활권이 함께 연결되는 지역입니다. 대화·킨텍스는 "
            "전시·공연·행사 수요와 맞물리고, 주엽·일산동은 후곡·강선마을 같은 주거 상권 "
            "검색이 함께 발생합니다. 탄현·덕이·가좌·송포는 차량 이동 기준 안내가 더 "
            "중요한 외곽 주거권이므로, 예약 전 방문 가능 시간과 추가 이동비 여부를 "
            "미리 확인하는 것이 좋습니다."
        ),
        "summary": "대화·주엽·일산·탄현·송포·덕이 중심",
    },
}

# ──────────────────────────────────────────────────────────────────────────
# 대표 행정동
# key: (한글명, slug, 구, Description, lead, area(주변/랜드마크), route(이동 동선), [관련 역 slug])
DONGS = [
    # 덕양구 (15)
    ("주교동", "ju-gyo", "deogyang",
     "주교동 출장마사지·홈타이 예약 전 원당역 주변 이용 기준을 확인하세요.",
     "주교동은 덕양구청과 원당 구도심이 자리한 행정 중심지로, 관공서·주거·상권이 한곳에 모여 있습니다. 낮에는 업무 수요, 저녁에는 인근 주거지 수요가 함께 발생하는 생활권입니다.",
     "덕양구청, 원당 재래시장, 성사동 경계 주거 단지와 가깝습니다.",
     "3호선 원당역 도보권으로 접근성이 좋아 차량·도보 방문이 모두 수월합니다.",
     ["wondang-station"]),
    ("원신동", "wonsin", "deogyang",
     "원신동 출장마사지·홈타이 예약 전 원당·신원 생활권을 확인하세요.",
     "원신동은 원당과 신원 일대를 묶은 생활권으로, 한적한 주거지와 농촌형 지역이 함께 있습니다. 차량 이동 기준 안내가 중요한 동네입니다.",
     "원당역 동쪽, 서오릉로 방면 주거지와 인접합니다.",
     "지하철보다 차량 이동이 편리한 지역으로, 방문 가능 시간과 동선을 미리 확인하면 좋습니다.",
     ["wondang-station"]),
    ("흥도동", "heungdo", "deogyang",
     "흥도동 출장마사지·홈타이 예약 전 도래울 생활권을 확인하세요.",
     "흥도동은 도래울마을을 중심으로 한 주거 생활권입니다. 신축 아파트 단지와 학교가 밀집해 가족 단위 수요가 많은 동네입니다.",
     "도래울마을, 화정·원당 사이 주거 단지와 연결됩니다.",
     "화정역·원당역 양쪽에서 차량으로 접근하기 쉬운 위치입니다.",
     ["hwajeong-station", "wondang-station"]),
    ("성사동", "seongsa", "deogyang",
     "성사동 출장마사지·홈타이 예약 전 원당역 주변 이용 기준을 확인하세요.",
     "성사동은 원당역을 끼고 있는 덕양구의 대표 주거·상권 지역입니다. 성사1동·성사2동을 아우르는 생활권으로 유동 인구가 많습니다.",
     "원당역, 화정지구와 가깝고 학원·상가가 밀집해 있습니다.",
     "3호선 원당역 중심 도보권이라 저녁 시간대 방문 수요가 꾸준합니다.",
     ["wondang-station"]),
    ("효자동", "hyoja", "deogyang",
     "효자동 출장마사지·홈타이 예약 전 북한산 인근 방문 기준을 확인하세요.",
     "효자동은 북한산 자락에 위치한 한적한 주거·자연 생활권입니다. 펜션·전원주택 수요가 있어 숙소 방문 문의가 종종 발생합니다.",
     "북한산성 입구, 지축·삼송 경계 자연 녹지와 인접합니다.",
     "차량 이동 기준 지역으로, 방문 가능 시간과 추가 이동비 여부를 미리 확인하는 것이 좋습니다.",
     ["jichuk-station", "samsong-station"]),
    ("삼송동", "samsong", "deogyang",
     "삼송동 출장마사지·홈타이 예약 전 삼송역 생활권을 확인하세요.",
     "삼송동은 삼송지구 개발로 인구가 크게 늘어난 신주거 생활권입니다. 삼송1동·삼송2동을 아우르며 대형 상업시설과 신축 단지가 밀집해 있습니다.",
     "삼송역, 스타필드 고양, 원흥지구와 연결됩니다.",
     "3호선 삼송역 도보권으로 접근성이 뛰어나 저녁·심야 수요가 많은 편입니다.",
     ["samsong-station", "wonheung-station"]),
    ("창릉동", "changleung", "deogyang",
     "창릉동 출장마사지·홈타이 예약 전 창릉신도시 생활권을 확인하세요.",
     "창릉동은 창릉신도시 개발이 진행 중인 지역으로, 새 주거 단지가 점차 늘고 있습니다. 향후 생활권 변화가 큰 동네입니다.",
     "원흥지구, 화전·덕은 경계 택지와 인접합니다.",
     "차량 이동이 편리하며 원흥역·화전역 양쪽에서 접근할 수 있습니다.",
     ["wonheung-station", "hanguk-aerospace-univ-station"]),
    ("고양동", "goyang-dong", "deogyang",
     "고양동 출장마사지·홈타이 예약 전 고양동 주거권 기준을 확인하세요.",
     "고양동은 덕양구 북부의 전통 주거 생활권입니다. 고양향교와 오래된 주택가, 신축 단지가 함께 있어 차분한 동네 분위기를 가집니다.",
     "고양향교, 관산동·벽제 방면 주거지와 연결됩니다.",
     "지하철보다 차량 이동이 편한 외곽 지역으로 동선 확인이 필요합니다.",
     ["wondang-station"]),
    ("관산동", "gwansan", "deogyang",
     "관산동 출장마사지·홈타이 예약 전 관산동 생활권을 확인하세요.",
     "관산동은 덕양구 북동부의 주거·농촌 혼합 생활권입니다. 벽제·고양동과 이어지는 한적한 지역으로 차량 방문이 기본입니다.",
     "벽제, 고양동, 서울 은평 경계 방면과 인접합니다.",
     "외곽 차량 이동 기준 지역이라 예약 전 방문 가능 시간과 이동비를 확인하면 좋습니다.",
     ["wondang-station"]),
    ("능곡동", "neunggok", "deogyang",
     "능곡동 출장마사지·홈타이 예약 전 능곡역 주변 기준을 확인하세요.",
     "능곡동은 능곡역을 중심으로 한 전통 주거 생활권입니다. 재개발이 진행되며 신축 단지와 구도심이 공존하는 동네입니다.",
     "능곡역, 행주·화정 사이 주거지와 연결됩니다.",
     "경의중앙선·서해선 능곡역 도보권으로 접근성이 점차 좋아지고 있습니다.",
     ["neunggok-station", "haengsin-station"]),
    ("화정동", "hwajeong", "deogyang",
     "화정동 출장마사지·홈타이 예약 전 화정역 주변 이용 기준을 확인하세요.",
     "화정동은 덕양구 최대 상권 중 하나인 화정역을 끼고 있는 생활권입니다. 화정1동·화정2동을 아우르며 유동 인구와 주거 밀도가 모두 높습니다.",
     "화정역, 롯데·이마트 상권, 능곡·행신 경계와 연결됩니다.",
     "3호선·서해선 화정역 도보권으로 저녁·심야 시간대 방문 수요가 가장 많은 동네입니다.",
     ["hwajeong-station"]),
    ("행주동", "haengju", "deogyang",
     "행주동 출장마사지·홈타이 예약 전 행주산성 인근 기준을 확인하세요.",
     "행주동은 행주산성과 한강 변을 끼고 있는 자연·주거 생활권입니다. 음식점·전원형 주거가 많아 차량 방문이 일반적입니다.",
     "행주산성, 한강공원, 강매·능곡 경계와 인접합니다.",
     "차량 이동 기준 지역으로 방문 가능 동선과 시간대를 미리 확인하는 것이 좋습니다.",
     ["gangmae-station", "neunggok-station"]),
    ("행신동", "haengsin", "deogyang",
     "행신동 출장마사지·홈타이 예약 전 행신역 주변 범위를 확인하세요.",
     "행신동은 행신역을 중심으로 한 덕양구 대표 주거 생활권입니다. 행신1동부터 행신4동까지 아우르며 아파트 단지와 상권이 밀집해 있습니다.",
     "행신역, 소만·샘터마을, 화정·강매 경계와 연결됩니다.",
     "경의중앙선·KTX 행신역 생활권으로 서울 접근성이 좋아 수요가 꾸준합니다.",
     ["haengsin-station", "gangmae-station"]),
    ("화전동", "hwajeon", "deogyang",
     "화전동 출장마사지·홈타이 예약 전 한국항공대역 생활권을 확인하세요.",
     "화전동은 한국항공대학교와 화전역을 중심으로 한 생활권입니다. 대학가 수요와 인근 주거지가 함께 있어 시간대별 방문 패턴이 다릅니다.",
     "한국항공대, 화전역, 덕은·수색 경계와 연결됩니다.",
     "경의중앙선 한국항공대역(화전역) 생활권으로 서울 수색·상암 접근이 편리합니다.",
     ["hanguk-aerospace-univ-station"]),
    ("대덕동", "daedeok", "deogyang",
     "대덕동 출장마사지·홈타이 예약 전 덕은·대덕 생활권을 확인하세요.",
     "대덕동은 덕은지구 개발로 새 주거·업무 단지가 들어선 생활권입니다. 한강과 서울 마곡·상암 접근성이 좋아 직장 수요가 늘고 있습니다.",
     "덕은지구, 한강, 서울 상암·마곡 경계와 연결됩니다.",
     "차량 이동이 편리하며 화전·수색 방면에서 빠르게 접근할 수 있습니다.",
     ["hanguk-aerospace-univ-station"]),
    # 일산동구 (8)
    ("식사동", "siksa", "ilsandong",
     "식사동 출장마사지·홈타이 예약 전 위시티 생활권을 확인하세요.",
     "식사동은 위시티를 중심으로 한 대규모 아파트 생활권입니다. 일산 동쪽 외곽에 위치해 가족 단위 주거 수요가 많은 동네입니다.",
     "위시티, 일산자이, 고봉·풍산 경계와 연결됩니다.",
     "차량 이동 기준 지역으로 풍산역에서 접근하거나 차량 방문이 일반적입니다.",
     ["pungsan-station"]),
    ("중산동", "jungsan", "ilsandong",
     "중산동 출장마사지·홈타이 예약 전 중산 주거권 기준을 확인하세요.",
     "중산동은 하늘마을·중산마을을 중심으로 한 주거 생활권입니다. 중산1동·중산2동을 아우르며 학교와 단지가 밀집해 있습니다.",
     "하늘마을, 중산마을, 정발산·고봉 경계와 연결됩니다.",
     "정발산역·풍산역에서 차량으로 접근하기 쉬운 주거 밀집 지역입니다.",
     ["jeongbalsan-station", "pungsan-station"]),
    ("정발산동", "jeongbalsan", "ilsandong",
     "정발산동 출장마사지·홈타이 예약 전 정발산역 주변을 확인하세요.",
     "정발산동은 정발산역과 일산문화광장, 호수공원을 끼고 있는 일산동구 중심 생활권입니다. 상권과 주거가 가깝게 붙어 있습니다.",
     "정발산역, 일산문화공원, 라페스타·웨스턴돔과 연결됩니다.",
     "3호선 정발산역 도보권으로 접근성이 뛰어나 저녁 시간 수요가 많습니다.",
     ["jeongbalsan-station"]),
    ("풍산동", "pungsan", "ilsandong",
     "풍산동 출장마사지·홈타이 예약 전 풍산역 생활권을 확인하세요.",
     "풍산동은 풍산역을 중심으로 한 경의중앙선 생활권입니다. 밤가시마을 등 주거 단지와 학원가가 함께 있습니다.",
     "풍산역, 밤가시마을, 정발산·식사 경계와 연결됩니다.",
     "경의중앙선 풍산역 생활권으로 일산 동부 주거 수요가 꾸준합니다.",
     ["pungsan-station", "baengma-station"]),
    ("백석동", "baekseok", "ilsandong",
     "백석동 출장마사지·홈타이 예약 전 백석역 주변 기준을 확인하세요.",
     "백석동은 백석역을 중심으로 한 일산 최대 업무·상업 생활권입니다. 백석1동·백석2동을 아우르며 오피스와 주거가 함께 밀집해 있습니다.",
     "백석역, 요진와이시티, 일산테크노밸리 방면과 연결됩니다.",
     "3호선 백석역 도보권이며 업무지구 특성상 평일·저녁 수요가 모두 많습니다.",
     ["baekseok-station"]),
    ("마두동", "madu", "ilsandong",
     "마두동 출장마사지·홈타이 예약 전 마두역 중심 기준을 확인하세요.",
     "마두동은 마두역을 중심으로 한 일산동구 주거 중심 생활권입니다. 마두1동·마두2동, 강촌마을·백마마을을 아우릅니다.",
     "마두역, 강촌마을, 백마역·호수공원과 연결됩니다.",
     "3호선 마두역과 경의중앙선 백마역 사이에 있어 양쪽 접근이 모두 편리합니다.",
     ["madu-station", "baengma-station"]),
    ("장항동", "janghang", "ilsandong",
     "장항동 출장마사지·홈타이 예약 전 라페스타·호수공원 주변을 확인하세요.",
     "장항동은 라페스타·웨스턴돔·호수공원·업무지구가 모여 있는 일산 핵심 상권입니다. 장항1동·장항2동을 아우르며 유동 인구가 가장 많습니다.",
     "라페스타, 웨스턴돔, 일산호수공원, 정발산역과 연결됩니다.",
     "정발산역·마두역 도보권으로 상권 특성상 저녁·심야 방문 수요가 큽니다.",
     ["jeongbalsan-station", "madu-station"]),
    ("고봉동", "gobong", "ilsandong",
     "고봉동 출장마사지·홈타이 예약 전 고봉동 외곽 생활권을 확인하세요.",
     "고봉동은 일산동구 북동부의 농촌·외곽 주거 생활권입니다. 한적한 전원 지역으로 차량 방문이 기본입니다.",
     "고봉산, 성석·식사 경계 주거지와 연결됩니다.",
     "외곽 차량 이동 기준 지역이라 예약 전 방문 가능 시간과 이동비를 확인하면 좋습니다.",
     ["pungsan-station"]),
    # 일산서구 (7)
    ("일산동", "ilsan", "ilsanseo",
     "일산동 출장마사지·홈타이 예약 전 일산역 생활권을 확인하세요.",
     "일산동은 일산역과 후곡마을을 중심으로 한 일산서구 주거 생활권입니다. 일산1~3동을 아우르며 구일산 상권과 학원가가 발달해 있습니다.",
     "일산역, 후곡마을, 일산시장·주엽 경계와 연결됩니다.",
     "경의중앙선 일산역과 3호선 주엽역 사이로 도보·차량 접근이 모두 편리합니다.",
     ["ilsan-station", "juyeop-station"]),
    ("탄현동", "tanhyeon", "ilsanseo",
     "탄현동 출장마사지·홈타이 예약 전 탄현역 주변 기준을 확인하세요.",
     "탄현동은 탄현역과 탄현마을을 중심으로 한 주거 생활권입니다. 탄현1동·탄현2동을 아우르며 대단지 아파트가 밀집해 있습니다.",
     "탄현역, 탄현마을, 일산·송포 경계와 연결됩니다.",
     "경의중앙선 탄현역 생활권이며 일부 외곽은 차량 이동 기준 안내가 필요합니다.",
     ["tanhyeon-station"]),
    ("주엽동", "juyeop", "ilsanseo",
     "주엽동 출장마사지·홈타이 예약 전 주엽역 중심 기준을 확인하세요.",
     "주엽동은 주엽역과 강선·문촌마을을 중심으로 한 일산서구 중심 생활권입니다. 주엽1동·주엽2동을 아우르며 상권과 주거가 가깝습니다.",
     "주엽역, 강선마을, 문촌마을, 일산호수공원과 연결됩니다.",
     "3호선 주엽역 도보권으로 접근성이 좋아 저녁 시간대 수요가 많습니다.",
     ["juyeop-station"]),
    ("대화동", "daehwa", "ilsanseo",
     "대화동 출장마사지·홈타이 예약 전 대화역·킨텍스 생활권을 확인하세요.",
     "대화동은 대화역과 킨텍스를 끼고 있는 일산서구 서쪽 생활권입니다. 전시·행사 수요와 대단지 주거가 함께 있어 방문 패턴이 다양합니다.",
     "대화역, 킨텍스, 일산호수공원, 한류월드와 연결됩니다.",
     "3호선 대화역·킨텍스역 생활권으로 행사 기간에는 숙소 방문 문의가 늘어납니다.",
     ["daehwa-station", "kintex-station"]),
    ("송포동", "songpo", "ilsanseo",
     "송포동 출장마사지·홈타이 예약 전 송포동 차량 방문 기준을 확인하세요.",
     "송포동은 일산서구 서북부의 주거·농촌 혼합 생활권입니다. 대화·법곳 방면 외곽 지역으로 차량 방문이 기본입니다.",
     "법곳, 대화 경계, 킨텍스 서쪽 주거지와 연결됩니다.",
     "차량 이동 기준 지역이라 예약 전 방문 가능 시간과 이동비를 확인하면 좋습니다.",
     ["daehwa-station", "kintex-station"]),
    ("덕이동", "deogi", "ilsanseo",
     "덕이동 출장마사지·홈타이 예약 전 덕이동 주거권 기준을 확인하세요.",
     "덕이동은 하이파크시티 등 대단지가 들어선 일산서구 북부 주거 생활권입니다. 신축 아파트와 외곽 주거가 함께 있습니다.",
     "하이파크시티, 탄현·가좌 경계와 연결됩니다.",
     "탄현역에서 차량으로 접근하거나 차량 방문이 일반적인 지역입니다.",
     ["tanhyeon-station"]),
    ("가좌동", "gajwa", "ilsanseo",
     "가좌동 출장마사지·홈타이 예약 전 가좌동 외곽 생활권을 확인하세요.",
     "가좌동은 일산서구 서북부의 가좌마을을 중심으로 한 외곽 주거 생활권입니다. 한강·송산 방면과 이어지는 한적한 동네입니다.",
     "가좌마을, 송산, 대화·송포 경계와 연결됩니다.",
     "차량 이동 기준 지역으로 방문 가능 동선과 시간대를 미리 확인하는 것이 좋습니다.",
     ["daehwa-station", "kintex-station"]),
]

# ──────────────────────────────────────────────────────────────────────────
# 지하철역 (환승역은 1개로 통합)
# key: (한글명, slug, Title, Description, lead, 노선, 주변 행정동/상권, 이동 동선)
STATIONS = [
    ("대화역", "daehwa-station",
     "대화역 출장마사지｜킨텍스 인근 고양 홈타이 안내",
     "대화역 출장마사지·홈타이 예약 전 킨텍스 인근 방문 범위를 확인하세요.",
     "대화역은 3호선 서쪽 종착역으로 킨텍스·한류월드 생활권과 맞닿아 있습니다. 전시·공연 기간에는 인근 숙소 방문 수요가 늘어나는 곳입니다.",
     "수도권 3호선", "대화동, 송포동, 킨텍스, 한류월드",
     "대화역 도보권과 킨텍스 일대 호텔·숙소까지 차량 이동이 모두 편리합니다."),
    ("주엽역", "juyeop-station",
     "주엽역 출장마사지｜일산서구 중심 홈타이 예약 안내",
     "주엽역 출장마사지·홈타이 예약 전 일산서구 중심 상권을 확인하세요.",
     "주엽역은 일산서구 중심 상권을 끼고 있는 3호선 역입니다. 강선·문촌마을 주거지와 상가가 함께 모여 있어 저녁 시간 수요가 많습니다.",
     "수도권 3호선", "주엽동, 강선마을, 문촌마을, 일산호수공원",
     "주엽역 도보권 주거 단지와 인근 상권까지 빠르게 이동할 수 있습니다."),
    ("정발산역", "jeongbalsan-station",
     "정발산역 출장마사지｜라페스타·호수공원 주변 안내",
     "정발산역 출장마사지·홈타이 예약 전 라페스타 주변을 확인하세요.",
     "정발산역은 라페스타·웨스턴돔·호수공원과 가까운 일산 핵심 상권 역입니다. 유동 인구가 많아 저녁·심야 방문 문의가 꾸준합니다.",
     "수도권 3호선", "정발산동, 장항동, 라페스타, 일산호수공원",
     "정발산역 도보권 상권과 장항동 업무지구까지 접근이 편리합니다."),
    ("마두역", "madu-station",
     "마두역 출장마사지｜일산동구 중심 방문 관리 안내",
     "마두역 출장마사지·홈타이 예약 전 일산동구 중심 동선을 확인하세요.",
     "마두역은 일산동구 주거 중심에 위치한 3호선 역입니다. 강촌마을·백마마을 등 대단지가 인접해 가족 단위 수요가 많습니다.",
     "수도권 3호선", "마두동, 강촌마을, 백마역 방면",
     "마두역 도보권 주거 단지와 경의중앙선 백마역 사이를 함께 안내합니다."),
    ("백석역", "baekseok-station",
     "백석역 출장마사지｜백석동 업무지구 홈타이 안내",
     "백석역 출장마사지·홈타이 예약 전 백석 업무지구 기준을 확인하세요.",
     "백석역은 일산 최대 업무지구를 끼고 있는 3호선 역입니다. 오피스와 주거가 함께 밀집해 평일·저녁 수요가 모두 많은 곳입니다.",
     "수도권 3호선", "백석동, 요진와이시티, 일산테크노밸리",
     "백석역 도보권 업무지구와 인근 주거 단지까지 접근이 편리합니다."),
    ("대곡역", "daegok-station",
     "대곡역 출장마사지｜고양 환승 거점 홈타이 안내",
     "대곡역 출장마사지·홈타이 이용 전 환승역 주변 기준을 확인하세요.",
     "대곡역은 3호선·경의중앙선·서해선·GTX-A가 만나는 고양시 최대 환승 거점입니다. 여러 노선이 모이는 만큼 인근 이동 동선이 다양합니다.",
     "3호선·경의중앙선·서해선·GTX-A", "대곡, 화정·능곡 경계",
     "환승 거점 특성상 화정·능곡 방면 주거지로의 차량 이동을 함께 안내합니다."),
    ("화정역", "hwajeong-station",
     "화정역 출장마사지｜덕양구 중심 상권 방문 안내",
     "화정역 출장마사지·홈타이 예약 전 덕양구 중심 상권을 확인하세요.",
     "화정역은 덕양구 최대 상권 중 하나로 유동 인구가 많은 3호선·서해선 역입니다. 화정1·2동 주거지와 상가가 함께 밀집해 있습니다.",
     "수도권 3호선·서해선", "화정동, 능곡·행신 경계",
     "화정역 도보권 상권과 인근 주거 단지까지 빠르게 이동할 수 있습니다."),
    ("원당역", "wondang-station",
     "원당역 출장마사지｜성사동·주교동 인근 홈타이 안내",
     "원당역 출장마사지·홈타이 예약 전 성사·주교 인근을 확인하세요.",
     "원당역은 덕양구 행정·주거 중심을 끼고 있는 3호선 역입니다. 성사동·주교동 구도심 상권과 주거지가 함께 있습니다.",
     "수도권 3호선", "성사동, 주교동, 원신동",
     "원당역 도보권 구도심과 인근 주거지까지 접근이 편리합니다."),
    ("원흥역", "wonheung-station",
     "원흥역 출장마사지｜원흥지구 생활권 방문 안내",
     "원흥역 출장마사지·홈타이 예약 전 원흥지구 생활권을 확인하세요.",
     "원흥역은 원흥지구 택지 개발로 인구가 늘어난 3호선 역입니다. 신축 단지와 상업시설이 함께 형성된 생활권입니다.",
     "수도권 3호선", "원흥지구, 삼송·창릉 경계",
     "원흥역 도보권 신주거 단지와 삼송 방면까지 접근이 편리합니다."),
    ("삼송역", "samsong-station",
     "삼송역 출장마사지｜삼송지구 홈타이 예약 안내",
     "삼송역 출장마사지·홈타이 예약 전 삼송지구 생활권을 확인하세요.",
     "삼송역은 삼송지구와 대형 상업시설을 끼고 있는 3호선 역입니다. 신축 대단지가 밀집해 저녁·심야 수요가 많은 곳입니다.",
     "수도권 3호선", "삼송동, 스타필드 고양, 원흥지구",
     "삼송역 도보권 상업시설과 인근 신주거 단지까지 접근이 편리합니다."),
    ("지축역", "jichuk-station",
     "지축역 출장마사지｜지축지구 방문 가능 지역 안내",
     "지축역 출장마사지·홈타이 예약 전 지축지구 방문 기준을 확인하세요.",
     "지축역은 지축지구 개발로 새 단지가 들어선 3호선 역입니다. 서울 은평 경계와 가까워 양쪽 생활권이 함께 연결됩니다.",
     "수도권 3호선", "지축지구, 효자동, 서울 은평 경계",
     "지축역 도보권 신주거 단지와 북한산 방면까지 접근이 편리합니다."),
    ("한국항공대역", "hanguk-aerospace-univ-station",
     "한국항공대역 출장마사지｜화전동·항공대 생활권 안내",
     "한국항공대역 출장마사지·홈타이 예약 전 화전동 생활권을 확인하세요.",
     "한국항공대역(화전역)은 한국항공대학교와 화전동 생활권을 끼고 있는 경의중앙선 역입니다. 대학가와 주거지 수요가 함께 발생합니다.",
     "경의중앙선", "화전동, 한국항공대, 덕은·수색 경계",
     "한국항공대역 도보권 대학가와 서울 수색·상암 방면 접근이 편리합니다."),
    ("강매역", "gangmae-station",
     "강매역 출장마사지｜강매동·행신 인근 방문 안내",
     "강매역 출장마사지·홈타이 예약 전 강매·행신 인근을 확인하세요.",
     "강매역은 강매동과 행신 생활권 사이에 위치한 경의중앙선 역입니다. 한강 변 주거지와 행신 단지가 함께 연결됩니다.",
     "경의중앙선", "강매동, 행신동, 행주 경계",
     "강매역 도보권 주거지와 행신·행주 방면까지 접근이 편리합니다."),
    ("행신역", "haengsin-station",
     "행신역 출장마사지｜행신동 중심 홈타이 안내",
     "행신역 출장마사지·홈타이 예약 전 행신동 중심 동선을 확인하세요.",
     "행신역은 행신동 주거 중심을 끼고 있는 경의중앙선·KTX 역입니다. 소만·샘터마을 등 대단지가 밀집해 수요가 꾸준합니다.",
     "경의중앙선·KTX", "행신동, 소만마을, 화정 경계",
     "행신역 도보권 대단지와 화정·강매 방면까지 접근이 편리합니다."),
    ("능곡역", "neunggok-station",
     "능곡역 출장마사지｜능곡동 생활권 방문 안내",
     "능곡역 출장마사지·홈타이 예약 전 능곡동 생활권을 확인하세요.",
     "능곡역은 능곡동 구도심과 재개발 단지를 끼고 있는 경의중앙선·서해선 환승역입니다. 구도심과 신축이 공존하는 생활권입니다.",
     "경의중앙선·서해선", "능곡동, 행주·화정 경계",
     "능곡역 도보권 주거지와 화정·행주 방면까지 접근이 편리합니다."),
    ("곡산역", "goksan-station",
     "곡산역 출장마사지｜백석·능곡 사이 생활권 안내",
     "곡산역 출장마사지·홈타이 예약 전 백석·능곡 사이를 확인하세요.",
     "곡산역은 백석동과 능곡 사이에 위치한 경의중앙선 역입니다. 한적한 주거지와 인접 단지가 함께 연결되는 생활권입니다.",
     "경의중앙선", "백석동 일부, 능곡 경계",
     "곡산역 도보권 주거지와 백석·능곡 방면까지 차량 접근이 편리합니다."),
    ("백마역", "baengma-station",
     "백마역 출장마사지｜마두·풍산 인근 홈타이 안내",
     "백마역 출장마사지·홈타이 예약 전 마두·풍산 인근을 확인하세요.",
     "백마역은 마두동과 풍산동 사이를 잇는 경의중앙선 역입니다. 백마마을·강촌마을 등 일산 동부 주거 단지가 밀집해 있습니다.",
     "경의중앙선", "마두동, 풍산동, 백마마을",
     "백마역 도보권 주거 단지와 3호선 마두역 방면까지 접근이 편리합니다."),
    ("풍산역", "pungsan-station",
     "풍산역 출장마사지｜풍산동 생활권 예약 안내",
     "풍산역 출장마사지·홈타이 예약 전 풍산동 생활권을 확인하세요.",
     "풍산역은 풍산동 주거 중심을 끼고 있는 경의중앙선 역입니다. 밤가시마을 등 단지와 학원가가 함께 형성되어 있습니다.",
     "경의중앙선", "풍산동, 밤가시마을, 식사 경계",
     "풍산역 도보권 주거지와 식사동 방면까지 접근이 편리합니다."),
    ("일산역", "ilsan-station",
     "일산역 출장마사지｜일산동 중심 홈타이 안내",
     "일산역 출장마사지·홈타이 예약 전 일산동 중심 동선을 확인하세요.",
     "일산역은 구일산 상권과 후곡마을을 끼고 있는 경의중앙선 역입니다. 전통 상권과 주거지가 함께 모여 있는 생활권입니다.",
     "경의중앙선", "일산동, 후곡마을, 일산시장",
     "일산역 도보권 상권과 주엽 방면 주거지까지 접근이 편리합니다."),
    ("탄현역", "tanhyeon-station",
     "탄현역 출장마사지｜탄현동 주거권 방문 안내",
     "탄현역 출장마사지·홈타이 예약 전 탄현동 주거권을 확인하세요.",
     "탄현역은 탄현동 대단지 주거 생활권을 끼고 있는 경의중앙선 역입니다. 탄현마을과 인근 단지가 함께 연결됩니다.",
     "경의중앙선", "탄현동, 탄현마을, 덕이 경계",
     "탄현역 도보권 주거 단지와 덕이·일산 방면까지 접근이 편리합니다."),
    ("킨텍스역", "kintex-station",
     "킨텍스역 출장마사지｜대화동·킨텍스 행사권 안내",
     "킨텍스역 출장마사지·홈타이 예약 전 킨텍스 행사권을 확인하세요.",
     "킨텍스역은 킨텍스 전시장과 한류월드를 끼고 있는 GTX-A·전시 생활권입니다. 행사·전시 기간에는 인근 숙소 방문 수요가 크게 늘어납니다.",
     "GTX-A", "대화동, 킨텍스, 한류월드",
     "킨텍스역 일대 전시장·호텔·숙소까지 차량 이동이 모두 편리합니다."),
]

# ──────────────────────────────────────────────────────────────────────────
# 공통 유틸
def slug_paths():
    """slug -> url 매핑 생성"""
    m = {}
    for d in DONGS:
        name, slug, dist = d[0], d[1], d[2]
        m[slug] = f"/goyang/{dist_short(dist)}/{slug}-chuljangmassage/"
    for s in STATIONS:
        m[s[1]] = f"/goyang/{s[1]}-chuljangmassage/"
    return m

def dist_short(dist):
    return {"deogyang": "deogyang", "ilsandong": "ilsandong", "ilsanseo": "ilsanseo"}[dist]

URLMAP = {}

def build_urlmap():
    for slug, info in DISTRICTS.items():
        URLMAP[slug] = info["url"]
    for d in DONGS:
        URLMAP[d[1]] = f"/goyang/{dist_short(d[2])}/{d[1]}-chuljangmassage/"
    for s in STATIONS:
        URLMAP[s[1]] = f"/goyang/{s[1]}-chuljangmassage/"

def e(s):
    return html.escape(s, quote=True)

NAV_HTML = None

def build_nav():
    """상단 메뉴 (행정구 > 행정동, 지하철역, 기타) 생성"""
    dongs_by_dist = {"deogyang": [], "ilsandong": [], "ilsanseo": []}
    for d in DONGS:
        dongs_by_dist[d[2]].append(d)

    def dong_links(dist):
        items = []
        for d in dongs_by_dist[dist]:
            url = f"/goyang/{dist_short(dist)}/{d[1]}-chuljangmassage/"
            items.append(f'<li><a href="{url}">{e(d[0])}</a></li>')
        return "\n".join(items)

    station_links = "\n".join(
        f'<li><a href="/goyang/{s[1]}-chuljangmassage/">{e(s[0])} 출장마사지</a></li>'
        for s in STATIONS
    )

    return f"""
<nav class="site-nav" aria-label="주요 메뉴">
  <ul class="nav-root">
    <li><a href="/">고양 출장마사지</a></li>
    <li class="has-sub">
      <a href="/goyang/deogyang-gu-chuljangmassage/">행정구별 안내</a>
      <ul class="sub">
        <li><a href="/goyang/deogyang-gu-chuljangmassage/">덕양구 출장마사지</a></li>
        <li><a href="/goyang/ilsandong-gu-chuljangmassage/">일산동구 출장마사지</a></li>
        <li><a href="/goyang/ilsanseo-gu-chuljangmassage/">일산서구 출장마사지</a></li>
      </ul>
    </li>
    <li class="has-sub">
      <a href="/goyang/deogyang-gu-chuljangmassage/">덕양구 동별</a>
      <ul class="sub">{dong_links('deogyang')}</ul>
    </li>
    <li class="has-sub">
      <a href="/goyang/ilsandong-gu-chuljangmassage/">일산동구 동별</a>
      <ul class="sub">{dong_links('ilsandong')}</ul>
    </li>
    <li class="has-sub">
      <a href="/goyang/ilsanseo-gu-chuljangmassage/">일산서구 동별</a>
      <ul class="sub">{dong_links('ilsanseo')}</ul>
    </li>
    <li class="has-sub">
      <a href="/goyang/daehwa-station-chuljangmassage/">지하철역별 안내</a>
      <ul class="sub">{station_links}</ul>
    </li>
    <li class="has-sub">
      <a href="/reservation/">이용 안내</a>
      <ul class="sub">
        <li><a href="/reservation/">예약 안내</a></li>
        <li><a href="/notice/">이용 전 확인사항</a></li>
        <li><a href="/guide/">홈타이 이용 가이드</a></li>
        <li><a href="/contact/">고객센터</a></li>
        <li><a href="/privacy/">개인정보 처리방침</a></li>
      </ul>
    </li>
  </ul>
</nav>
"""

def breadcrumb_jsonld(items):
    """items: [(name, url_or_None), ...]"""
    elements = []
    for i, (name, url) in enumerate(items, start=1):
        el = {"@type": "ListItem", "position": i, "name": name}
        if url:
            el["item"] = SITE_URL + url
        elements.append(el)
    import json
    data = {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": elements}
    return json.dumps(data, ensure_ascii=False)

def webpage_jsonld(name, url, desc):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": name,
        "url": SITE_URL + url,
        "description": desc,
        "inLanguage": "ko-KR",
        "isPartOf": {"@type": "WebSite", "name": SITE_TITLE, "url": SITE_URL + "/"},
        "publisher": {
            "@type": "Organization",
            "name": BIZ_NAME,
            "telephone": BIZ_PHONE,
        },
    }
    return json.dumps(data, ensure_ascii=False)

def organization_jsonld():
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": BIZ_NAME,
        "url": SITE_URL + "/",
        "telephone": BIZ_PHONE,
        "areaServed": "경기도 고양시",
        "description": "고양 출장마사지·홈타이 지역별 예약 안내",
    }
    return json.dumps(data, ensure_ascii=False)

def breadcrumb_html(items):
    parts = []
    for name, url in items:
        if url:
            parts.append(f'<a href="{url}">{e(name)}</a>')
        else:
            parts.append(f"<span>{e(name)}</span>")
    return '<nav class="breadcrumb" aria-label="현재 위치">' + \
           ' <span class="sep">›</span> '.join(parts) + "</nav>"

CTA_HTML = f"""
<aside class="cta" aria-label="전화 예약">
  <div class="cta-inner">
    <div class="cta-text">
      <strong>{e(BIZ_NAME)}</strong>
      <span>전화 한 통이면 가까운 방문 가능 지역을 바로 안내해 드립니다.</span>
    </div>
    <a class="cta-btn" href="tel:{BIZ_PHONE_TEL}">전화예약 {e(BIZ_PHONE)}</a>
  </div>
</aside>
"""

def trust_block():
    return f"""
<section class="trust">
  <h2>예약 전 확인사항</h2>
  <ul>
    <li><strong>방문 가능 지역</strong> · 고양시 덕양구·일산동구·일산서구 전 지역, 인근 생활권</li>
    <li><strong>예약 가능 시간</strong> · 예약제 운영, 방문 가능 시간은 전화로 안내</li>
    <li><strong>추가 이동비</strong> · 외곽·차량 이동 지역은 거리 기준 별도 안내</li>
    <li><strong>결제 방식</strong> · 예약 시 안내된 정상 결제 방식만 이용</li>
    <li><strong>취소 기준</strong> · 방문 일정 변경·취소는 가능한 한 미리 연락</li>
    <li><strong>개인정보</strong> · 예약에 필요한 최소 정보만 수집·이용</li>
  </ul>
  <p class="note">{e(BIZ_NAME)}는 합법적인 방문형 관리 안내 서비스입니다. 불법·선정적 서비스는 제공하지 않습니다.</p>
</section>
"""

def page(title, desc, canonical_url, breadcrumb_items, body, extra_jsonld=None):
    bc_json = breadcrumb_jsonld(breadcrumb_items)
    wp_json = webpage_jsonld(title, canonical_url, desc)
    org_json = organization_jsonld()
    extra = ""
    if extra_jsonld:
        extra = f'<script type="application/ld+json">{extra_jsonld}</script>\n'
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE_URL}{canonical_url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE_URL}{canonical_url}">
<meta property="og:locale" content="ko_KR">
<meta name="robots" content="index, follow">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{bc_json}</script>
<script type="application/ld+json">{wp_json}</script>
<script type="application/ld+json">{org_json}</script>
{extra}</head>
<body>
<header class="site-header">
  <div class="bar">
    <a class="logo" href="/">고양 출장마사지 <span>· {e(BIZ_NAME)}</span></a>
    <a class="header-tel" href="tel:{BIZ_PHONE_TEL}">전화예약 {e(BIZ_PHONE)}</a>
  </div>
  {build_nav()}
</header>
<main class="container">
{breadcrumb_html(breadcrumb_items)}
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <p class="biz"><strong>{e(BIZ_NAME)}</strong> · 전화예약 <a href="tel:{BIZ_PHONE_TEL}">{e(BIZ_PHONE)}</a></p>
    <p class="foot-area">고양 출장마사지 · 고양시 홈타이 | 덕양구 · 일산동구 · 일산서구 전 지역 방문 안내</p>
    <p class="foot-links">
      <a href="/reservation/">예약 안내</a> ·
      <a href="/notice/">이용 전 확인사항</a> ·
      <a href="/guide/">홈타이 이용 가이드</a> ·
      <a href="/contact/">고객센터</a> ·
      <a href="/privacy/">개인정보 처리방침</a>
    </p>
    <p class="disclaimer">본 사이트는 합법적인 방문형 관리 안내 사이트이며, 불법·선정적 서비스를 제공하지 않습니다.</p>
  </div>
</footer>
</body>
</html>
"""

def write(path_url, content):
    """path_url like /goyang/.../  -> public/goyang/.../index.html"""
    rel = path_url.strip("/")
    if rel == "":
        out_path = os.path.join(OUT, "index.html")
    else:
        out_path = os.path.join(OUT, rel, "index.html")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

# ──────────────────────────────────────────────────────────────────────────
# 페이지 빌더
ALL_URLS = []  # for sitemap

def link_list(slugs, suffix=" 출장마사지"):
    items = []
    for slug in slugs:
        url = URLMAP.get(slug)
        name = None
        for s in STATIONS:
            if s[1] == slug:
                name = s[0] + suffix
        for d in DONGS:
            if d[1] == slug:
                name = d[0]
        if url and name:
            items.append(f'<li><a href="{url}">{e(name)}</a></li>')
    return "\n".join(items)

def build_home():
    url = "/"
    title = SITE_TITLE
    desc = "고양 출장마사지·홈타이 예약 전 덕양구, 일산동구, 일산서구 정보를 정리했습니다."
    bc = [("고양 출장마사지", None)]

    dist_cards = ""
    for slug in ("deogyang", "ilsandong", "ilsanseo"):
        d = DISTRICTS[slug]
        dist_cards += f"""
    <a class="card" href="{d['url']}">
      <h3>{e(d['name'])} 출장마사지</h3>
      <p>{e(d['summary'])}</p>
    </a>"""

    featured_stations = ["daehwa-station", "hwajeong-station", "samsong-station",
                         "daegok-station", "kintex-station"]
    station_cards = ""
    for slug in featured_stations:
        for s in STATIONS:
            if s[1] == slug:
                station_cards += f"""
    <a class="chip" href="/goyang/{s[1]}-chuljangmassage/">{e(s[0])} 출장마사지</a>"""

    # 전체 역 목록
    all_station_links = "\n".join(
        f'<li><a href="/goyang/{s[1]}-chuljangmassage/">{e(s[0])} 출장마사지</a></li>'
        for s in STATIONS)

    body = f"""
<h1>고양 출장마사지 · 고양시 홈타이 지역별 예약 안내</h1>
<p class="intro">고양 출장마사지를 찾는 분들은 대부분 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다.
{e(BIZ_NAME)}는 덕양구·일산동구·일산서구로 나뉜 고양시 생활권을 행정구 → 대표 행정동 → 지하철역 구조로
정리해, 본인이 있는 지역의 출장마사지·홈타이 예약 정보를 빠르게 찾을 수 있도록 안내합니다.</p>

{CTA_HTML}

<h2>고양시에서 출장마사지를 찾는 이유</h2>
<p>고양시는 경기도 안에서도 생활권이 넓은 편입니다. 화정·행신·삼송·원흥처럼 서울 접근성이 강한 덕양구,
백석·마두·정발산·장항처럼 상권과 오피스가 모인 일산동구, 대화·주엽·탄현·덕이처럼 주거지와 킨텍스
생활권이 연결되는 일산서구로 성격이 서로 다릅니다. 그래서 출장마사지를 예약할 때는 본인이 있는 동네가
어느 생활권에 속하는지 먼저 확인하는 것이 좋습니다.</p>

<h2>덕양구 · 일산동구 · 일산서구 생활권 차이</h2>
<div class="cards">{dist_cards}
</div>

<h2>행정동별 방문 가능 지역 안내</h2>
<p>고양시는 공식적으로 3개 구, 44개 행정동 체계입니다. 다만 1·2·3동처럼 번호가 붙은 행정동은
대표 행정동 한 곳으로 묶어 안내합니다. 예를 들어 화정1·2동은 화정동, 행신1~4동은 행신동으로
통합해, 같은 본문을 반복하지 않고 각 동네의 실제 생활권을 다르게 설명합니다.</p>
<div class="dong-cols">
  <div class="dong-col">
    <h3><a href="/goyang/deogyang-gu-chuljangmassage/">덕양구</a></h3>
    <ul class="dong-list">{link_list([d[1] for d in DONGS if d[2]=='deogyang'])}</ul>
  </div>
  <div class="dong-col">
    <h3><a href="/goyang/ilsandong-gu-chuljangmassage/">일산동구</a></h3>
    <ul class="dong-list">{link_list([d[1] for d in DONGS if d[2]=='ilsandong'])}</ul>
  </div>
  <div class="dong-col">
    <h3><a href="/goyang/ilsanseo-gu-chuljangmassage/">일산서구</a></h3>
    <ul class="dong-list">{link_list([d[1] for d in DONGS if d[2]=='ilsanseo'])}</ul>
  </div>
</div>

<h2>지하철역별 출장마사지 지역 SEO 구조</h2>
<p>고양시는 3호선·경의중앙선·서해선·GTX-A 생활권이 함께 섞여 있습니다. 특히 대곡역은 네 개 노선이
만나는 환승 거점입니다. 역세권 페이지는 역명+출장마사지 키워드로 만들되, 환승역도 하나의 페이지로만
안내해 중복을 줄였습니다.</p>
<div class="chips">{station_cards}
</div>
<ul class="dong-list cols3">{all_station_links}</ul>

<h2>고양 홈타이 예약 전 확인사항</h2>
<p>고양 홈타이는 자택·숙소·사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리
서비스입니다. 예약 가능 시간, 방문 가능 지역, 추가 이동비, 취소 기준, 결제 방식, 개인정보 처리 기준을
미리 확인하면 더 편리하게 이용할 수 있습니다.</p>
{trust_block()}

<h2>고양 출장마사지 사이트 이용 가이드</h2>
<p>메인페이지는 고양시 전체 안내를 맡고, 행정구 페이지는 덕양구·일산동구·일산서구의 큰 생활권을
설명합니다. 대표 행정동 페이지는 세부 지역 검색을, 역세권 페이지는 대화역·화정역·삼송역·대곡역·킨텍스역
처럼 실제 검색 의도가 분명한 키워드를 담당합니다. 더 자세한 내용은
<a href="/guide/">홈타이 이용 가이드</a>와 <a href="/reservation/">예약 안내</a>에서 확인하세요.</p>
{CTA_HTML}
"""
    write(url, page(title, desc, url, bc, body))
    ALL_URLS.append((url, "1.0"))

def build_district(slug):
    d = DISTRICTS[slug]
    url = d["url"]
    title = d["title"]
    desc = d["desc"]
    bc = [("고양 출장마사지", "/"), (f"{d['name']} 출장마사지", None)]

    dongs = [x for x in DONGS if x[2] == slug]
    dong_links = "\n".join(
        f'<li><a href="/goyang/{slug}/{x[1]}-chuljangmassage/">{e(x[0])} 출장마사지</a></li>'
        for x in dongs)

    # 관련 역: 해당 구 동들의 station 모음
    rel_stations = []
    for x in dongs:
        for st in x[6]:
            if st not in rel_stations:
                rel_stations.append(st)
    station_links = link_list(rel_stations)

    body = f"""
<h1>{e(d['name'])} 출장마사지 · 고양 홈타이 방문 가능 지역 안내</h1>
<p class="intro">{e(d['lead'])}</p>
{CTA_HTML}

<h2>{e(d['name'])} 대표 행정동별 안내</h2>
<p>{e(d['name'])}에서 출장마사지·홈타이를 찾을 때는 아래 대표 행정동 중 본인 위치와 가까운 곳을
선택하면 방문 가능 지역과 이동 동선을 더 정확히 안내받을 수 있습니다.</p>
<ul class="dong-list cols2">{dong_links}</ul>

<h2>{e(d['name'])} 인근 지하철역 안내</h2>
<p>{e(d['name'])} 생활권과 연결되는 지하철역입니다. 역세권 검색을 선호한다면 아래 역 페이지에서
주변 행정동과 이동 동선을 확인하세요.</p>
<ul class="dong-list cols2">{station_links}</ul>

{trust_block()}
{CTA_HTML}
"""
    write(url, page(title, desc, url, bc, body))
    ALL_URLS.append((url, "0.8"))

def build_dong(d):
    name, slug, dist = d[0], d[1], d[2]
    desc, lead, area, route, stations = d[3], d[4], d[5], d[6], d[7]
    dname = DISTRICTS[dist]["name"]
    url = f"/goyang/{dist}/{slug}-chuljangmassage/"
    # title from spec mapping
    title = DONG_TITLES[slug]
    bc = [("고양 출장마사지", "/"),
          (f"{dname} 출장마사지", DISTRICTS[dist]["url"]),
          (f"{name} 출장마사지", None)]

    station_links = link_list(stations)
    body = f"""
<h1>{e(name)} 출장마사지 · {e(dname)} 홈타이 안내</h1>
<p class="intro">{e(lead)}</p>
{CTA_HTML}

<h2>{e(name)} 주변 생활권</h2>
<p>{e(area)}</p>

<h2>{e(name)} 방문 동선 안내</h2>
<p>{e(route)} 정확한 방문 가능 시간과 추가 이동비 여부는 예약 시 전화로 안내해 드립니다.</p>

<h2>{e(name)} 인근 지하철역</h2>
<ul class="dong-list cols2">{station_links}</ul>
<p class="back-link"><a href="{DISTRICTS[dist]['url']}">› {e(dname)} 출장마사지 전체 보기</a></p>

{trust_block()}
{CTA_HTML}
"""
    write(url, page(title, desc, url, bc, body))
    ALL_URLS.append((url, "0.7"))

def build_station(s):
    name, slug, title, desc, lead, line, around, route = s
    url = f"/goyang/{slug}-chuljangmassage/"
    bc = [("고양 출장마사지", "/"),
          (f"{name} 출장마사지", None)]

    # 관련 동: around에 언급된 동 매칭
    rel_dongs = []
    for d in DONGS:
        if d[0][:-1] in around or d[0] in around:  # 동 이름(끝글자 동 제거)
            rel_dongs.append(d[1])
    rel_links = link_list(rel_dongs) if rel_dongs else ""
    rel_block = ""
    if rel_links:
        rel_block = f"""
<h2>{e(name)} 인근 행정동</h2>
<ul class="dong-list cols2">{rel_links}</ul>
"""

    body = f"""
<h1>{e(name)} 출장마사지 · 고양 홈타이 안내</h1>
<p class="intro">{e(lead)}</p>
{CTA_HTML}

<h2>{e(name)} 노선 · 주변 정보</h2>
<p><strong>운행 노선</strong> · {e(line)}<br>
<strong>주변 행정동 · 상권</strong> · {e(around)}</p>

<h2>{e(name)} 방문 동선 안내</h2>
<p>{e(route)} 역 주변 숙소·자택·사무실 방문이 가능하며, 정확한 방문 가능 시간과 추가 이동비
여부는 예약 시 전화로 안내해 드립니다.</p>
{rel_block}
{trust_block()}
{CTA_HTML}
"""
    write(url, page(title, desc, url, bc, body))
    ALL_URLS.append((url, "0.7"))

# 대표 행정동 Title 매핑 (명세서 기준)
DONG_TITLES = {
    "ju-gyo": "주교동 출장마사지｜고양 덕양구 홈타이 안내",
    "wonsin": "원신동 출장마사지｜원당·신원 생활권 홈타이 안내",
    "heungdo": "흥도동 출장마사지｜도래울·흥도 생활권 방문 관리 안내",
    "seongsa": "성사동 출장마사지｜원당역 인근 홈타이 예약 안내",
    "hyoja": "효자동 출장마사지｜북한산 인근 방문 가능 지역 안내",
    "samsong": "삼송동 출장마사지｜삼송역 생활권 홈타이 안내",
    "changleung": "창릉동 출장마사지｜창릉신도시 생활권 홈타이 안내",
    "goyang-dong": "고양동 출장마사지｜고양동 주거권 방문 안내",
    "gwansan": "관산동 출장마사지｜관산동 생활권 홈타이 안내",
    "neunggok": "능곡동 출장마사지｜능곡역 주변 방문 관리 안내",
    "hwajeong": "화정동 출장마사지｜화정역 중심 홈타이 안내",
    "haengju": "행주동 출장마사지｜행주산성 인근 홈타이 안내",
    "haengsin": "행신동 출장마사지｜행신역 생활권 방문 안내",
    "hwajeon": "화전동 출장마사지｜한국항공대역 생활권 안내",
    "daedeok": "대덕동 출장마사지｜덕은·대덕 생활권 방문 안내",
    "siksa": "식사동 출장마사지｜위시티 생활권 홈타이 안내",
    "jungsan": "중산동 출장마사지｜중산동 주거권 방문 안내",
    "jeongbalsan": "정발산동 출장마사지｜정발산역 주변 예약 안내",
    "pungsan": "풍산동 출장마사지｜풍산역 생활권 홈타이 안내",
    "baekseok": "백석동 출장마사지｜백석역 업무지구 방문 안내",
    "madu": "마두동 출장마사지｜마두역 중심 홈타이 안내",
    "janghang": "장항동 출장마사지｜라페스타·호수공원 주변 안내",
    "gobong": "고봉동 출장마사지｜고봉동 외곽 생활권 방문 안내",
    "ilsan": "일산동 출장마사지｜일산역 생활권 홈타이 안내",
    "tanhyeon": "탄현동 출장마사지｜탄현역 주변 예약 안내",
    "juyeop": "주엽동 출장마사지｜주엽역 중심 홈타이 안내",
    "daehwa": "대화동 출장마사지｜대화역·킨텍스 생활권 안내",
    "songpo": "송포동 출장마사지｜송포동 차량 방문 가능 지역 안내",
    "deogi": "덕이동 출장마사지｜덕이동 주거권 홈타이 안내",
    "gajwa": "가좌동 출장마사지｜가좌동 외곽 생활권 방문 안내",
}

# ──────────────────────────────────────────────────────────────────────────
# 기타 페이지
def build_misc():
    pages = []

    # 예약 안내
    pages.append((
        "/reservation/",
        "예약 안내｜고양 출장마사지·홈타이 예약 방법",
        "고양 출장마사지·홈타이 예약 방법과 방문 가능 지역, 시간을 안내합니다.",
        [("고양 출장마사지", "/"), ("예약 안내", None)],
        f"""
<h1>예약 안내</h1>
<p class="intro">{e(BIZ_NAME)} 고양 출장마사지·홈타이는 전화 예약제로 운영됩니다.
현재 위치와 가까운 방문 가능 지역을 먼저 확인한 뒤 일정을 안내해 드립니다.</p>
{CTA_HTML}
<h2>예약 방법</h2>
<ol class="steps">
  <li>전화로 현재 위치(동·역·숙소 등)와 희망 시간을 알려주세요.</li>
  <li>방문 가능 지역·시간과 추가 이동비 여부를 안내받습니다.</li>
  <li>안내된 내용으로 예약을 확정합니다.</li>
</ol>
<h2>방문 가능 지역</h2>
<p>덕양구·일산동구·일산서구 전 지역과 인근 생활권을 안내합니다. 외곽·차량 이동 지역은
거리 기준으로 추가 이동비가 발생할 수 있습니다.</p>
{trust_block()}
{CTA_HTML}
""", "0.6"))

    # 이용 전 확인사항
    pages.append((
        "/notice/",
        "이용 전 확인사항｜고양 출장마사지 안내",
        "고양 출장마사지 이용 전 방문 지역, 시간, 추가 비용 기준을 확인하세요.",
        [("고양 출장마사지", "/"), ("이용 전 확인사항", None)],
        f"""
<h1>이용 전 확인사항</h1>
<p class="intro">{e(BIZ_NAME)}는 합법적인 방문형 관리 안내 서비스입니다. 이용 전 아래 기준을
확인하시면 더 편리하게 예약하실 수 있습니다.</p>
{trust_block()}
<h2>안내 드리는 내용</h2>
<ul class="dong-list">
  <li>방문 가능 지역과 동선</li>
  <li>예약 가능 시간대</li>
  <li>추가 이동비 발생 기준</li>
  <li>결제 방식 및 취소 기준</li>
  <li>개인정보 수집·이용 범위</li>
</ul>
<p>불법 서비스, 선정적 표현, 허위 후기는 제공·게시하지 않습니다.</p>
{CTA_HTML}
""", "0.5"))

    # 홈타이 이용 가이드
    pages.append((
        "/guide/",
        "홈타이 이용 가이드｜고양 홈타이 방문 관리 안내",
        "고양 홈타이 이용 가이드 - 방문형 관리 서비스의 준비와 이용 방법 안내.",
        [("고양 출장마사지", "/"), ("홈타이 이용 가이드", None)],
        f"""
<h1>홈타이 이용 가이드</h1>
<p class="intro">고양 홈타이는 자택·숙소·사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤
이용하는 방문형 관리 서비스입니다. 처음 이용하신다면 아래 내용을 참고하세요.</p>
{CTA_HTML}
<h2>이용 순서</h2>
<ol class="steps">
  <li>전화로 위치와 희망 시간을 알려주세요.</li>
  <li>방문 가능 지역·시간을 안내받고 예약을 확정합니다.</li>
  <li>편안한 환경에서 방문 관리를 받습니다.</li>
</ol>
<h2>준비하면 좋은 점</h2>
<ul class="dong-list">
  <li>방문 주소와 출입 방법(공동현관 등)을 미리 알려주시면 빠릅니다.</li>
  <li>편안한 복장과 휴식 공간을 준비해 주세요.</li>
</ul>
{trust_block()}
{CTA_HTML}
""", "0.5"))

    # 고객센터
    pages.append((
        "/contact/",
        "고객센터｜고양 출장마사지 전화 예약 문의",
        "고양 출장마사지·홈타이 예약과 문의는 간다GO 고객센터로 연락하세요.",
        [("고양 출장마사지", "/"), ("고객센터", None)],
        f"""
<h1>고객센터</h1>
<p class="intro">예약과 문의는 전화로 안내해 드립니다. 현재 위치와 희망 시간을 알려주시면
가까운 방문 가능 지역을 바로 확인해 드립니다.</p>
{CTA_HTML}
<h2>연락처</h2>
<p class="contact-big"><strong>{e(BIZ_NAME)}</strong><br>
전화예약 <a href="tel:{BIZ_PHONE_TEL}">{e(BIZ_PHONE)}</a></p>
<h2>지역별 안내 바로가기</h2>
<ul class="dong-list cols3">
  <li><a href="/goyang/deogyang-gu-chuljangmassage/">덕양구 출장마사지</a></li>
  <li><a href="/goyang/ilsandong-gu-chuljangmassage/">일산동구 출장마사지</a></li>
  <li><a href="/goyang/ilsanseo-gu-chuljangmassage/">일산서구 출장마사지</a></li>
</ul>
{CTA_HTML}
""", "0.5"))

    # 개인정보 처리방침
    pages.append((
        "/privacy/",
        "개인정보 처리방침｜고양 출장마사지",
        "간다GO 고양 출장마사지 개인정보 수집·이용 및 처리 기준 안내입니다.",
        [("고양 출장마사지", "/"), ("개인정보 처리방침", None)],
        f"""
<h1>개인정보 처리방침</h1>
<p class="intro">{e(BIZ_NAME)}는 예약 안내에 필요한 최소한의 개인정보만 수집·이용합니다.</p>
<h2>수집 항목 및 목적</h2>
<ul class="dong-list">
  <li>연락처 · 방문 지역 · 희망 시간 — 예약 접수 및 방문 안내 목적</li>
</ul>
<h2>보유 및 이용 기간</h2>
<p>예약 안내 목적 달성 후 지체 없이 파기하며, 관련 법령에 따라 보관이 필요한 경우 해당
기간 동안만 보관합니다.</p>
<h2>제3자 제공</h2>
<p>이용자의 동의 없이 개인정보를 외부에 제공하지 않습니다.</p>
<h2>문의</h2>
<p>개인정보 관련 문의는 <a href="tel:{BIZ_PHONE_TEL}">{e(BIZ_PHONE)}</a>로 연락해 주세요.</p>
{CTA_HTML}
""", "0.3"))

    for url, title, desc, bc, body, prio in pages:
        write(url, page(title, desc, url, bc, body))
        ALL_URLS.append((url, prio))

# ──────────────────────────────────────────────────────────────────────────
def build_sitemap_robots():
    today = "2026-06-14"
    items = ""
    for url, prio in ALL_URLS:
        items += f"""  <url>
    <loc>{SITE_URL}{url}</loc>
    <lastmod>{today}</lastmod>
    <priority>{prio}</priority>
  </url>
"""
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{items}</urlset>
"""
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)

    robots = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

CSS = """
:root{--bg:#fff;--ink:#1f2328;--muted:#5b6470;--line:#e6e8eb;--brand:#1f6f4f;--brand-d:#175a40;--soft:#f4f7f5;--accent:#c8932b}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Apple SD Gothic Neo","Malgun Gothic",sans-serif;color:var(--ink);line-height:1.7;background:var(--bg);-webkit-text-size-adjust:100%}
a{color:var(--brand);text-decoration:none}
a:hover{text-decoration:underline}
.container{max-width:960px;margin:0 auto;padding:0 18px}
/* header */
.site-header{border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(255,255,255,.97);backdrop-filter:saturate(180%) blur(6px);z-index:50}
.bar{max-width:960px;margin:0 auto;padding:12px 18px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.logo{font-weight:800;font-size:18px;color:var(--ink)}
.logo span{color:var(--brand);font-weight:700}
.header-tel{font-weight:700;background:var(--brand);color:#fff;padding:8px 14px;border-radius:999px;white-space:nowrap;font-size:14px}
.header-tel:hover{background:var(--brand-d);text-decoration:none}
/* nav */
.site-nav{border-top:1px solid var(--line);background:var(--soft)}
.nav-root{list-style:none;display:flex;flex-wrap:wrap;gap:2px;margin:0;padding:0 8px;max-width:960px;margin:0 auto}
.nav-root>li{position:relative}
.nav-root>li>a{display:block;padding:11px 12px;font-weight:600;font-size:14px;color:var(--ink)}
.nav-root>li>a:hover{color:var(--brand);text-decoration:none}
.sub{list-style:none;margin:0;padding:8px;position:absolute;left:0;top:100%;background:#fff;border:1px solid var(--line);border-radius:10px;box-shadow:0 12px 30px rgba(0,0,0,.10);min-width:200px;max-height:70vh;overflow:auto;display:none;z-index:60}
.has-sub:hover .sub,.has-sub:focus-within .sub{display:block}
.sub li a{display:block;padding:7px 10px;font-size:14px;border-radius:6px;color:var(--ink)}
.sub li a:hover{background:var(--soft);color:var(--brand);text-decoration:none}
/* breadcrumb */
.breadcrumb{font-size:13px;color:var(--muted);margin:18px 0 6px}
.breadcrumb a{color:var(--muted)}
.breadcrumb .sep{margin:0 2px;color:#c2c7cd}
/* content */
main h1{font-size:26px;line-height:1.35;margin:10px 0 14px}
main h2{font-size:20px;margin:34px 0 12px;padding-bottom:6px;border-bottom:2px solid var(--soft)}
main h3{font-size:17px;margin:18px 0 8px}
.intro{font-size:16px;color:#333}
p{margin:10px 0}
.note{font-size:13px;color:var(--muted)}
/* cta */
.cta{margin:22px 0;border:1px solid var(--line);background:linear-gradient(135deg,#f4f7f5,#eef3f0);border-radius:14px}
.cta-inner{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:16px 18px;flex-wrap:wrap}
.cta-text{display:flex;flex-direction:column}
.cta-text strong{font-size:17px;color:var(--brand-d)}
.cta-text span{font-size:14px;color:var(--muted)}
.cta-btn{background:var(--brand);color:#fff;font-weight:800;padding:13px 20px;border-radius:999px;font-size:16px;white-space:nowrap}
.cta-btn:hover{background:var(--brand-d);text-decoration:none}
/* cards */
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.card{display:block;border:1px solid var(--line);border-radius:12px;padding:16px;background:#fff;transition:.15s}
.card:hover{border-color:var(--brand);box-shadow:0 6px 18px rgba(0,0,0,.06);text-decoration:none;transform:translateY(-2px)}
.card h3{margin:0 0 6px;color:var(--brand-d)}
.card p{margin:0;font-size:14px;color:var(--muted)}
/* dong cols & lists */
.dong-cols{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.dong-col h3{border-bottom:1px solid var(--line);padding-bottom:6px}
.dong-list{list-style:none;padding:0;margin:8px 0;display:grid;gap:4px}
.dong-list.cols2{grid-template-columns:repeat(2,1fr)}
.dong-list.cols3{grid-template-columns:repeat(3,1fr)}
.dong-list li a{display:block;padding:7px 10px;border:1px solid var(--line);border-radius:8px;font-size:14px;background:#fff}
.dong-list li a:hover{background:var(--soft);border-color:var(--brand);text-decoration:none}
/* chips */
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.chip{background:var(--soft);border:1px solid var(--line);padding:8px 14px;border-radius:999px;font-size:14px;font-weight:600;color:var(--brand-d)}
.chip:hover{background:var(--brand);color:#fff;text-decoration:none}
/* trust */
.trust{background:var(--soft);border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin:26px 0}
.trust h2{margin-top:0;border:0}
.trust ul{list-style:none;padding:0;margin:10px 0;display:grid;grid-template-columns:repeat(2,1fr);gap:8px}
.trust li{font-size:14px;background:#fff;border:1px solid var(--line);border-radius:8px;padding:9px 12px}
.trust li strong{color:var(--brand-d)}
/* steps */
.steps{padding-left:20px}
.steps li{margin:8px 0}
.contact-big{font-size:18px;line-height:1.8}
.back-link{margin-top:10px}
/* footer */
.site-footer{border-top:1px solid var(--line);margin-top:40px;padding:26px 0;background:var(--soft);font-size:14px;color:var(--muted)}
.site-footer .biz strong{color:var(--ink)}
.foot-links{margin:8px 0}
.foot-links a{color:var(--muted)}
.disclaimer{font-size:12px;color:#8a929b;margin-top:8px}
@media(max-width:760px){
  .cards,.dong-cols{grid-template-columns:1fr}
  .dong-list.cols2,.dong-list.cols3{grid-template-columns:1fr}
  .trust ul{grid-template-columns:1fr}
  .nav-root{overflow-x:auto;flex-wrap:nowrap}
  .nav-root>li>a{white-space:nowrap}
  .sub{position:static;box-shadow:none;border:0;background:transparent;padding:0 0 0 12px;display:block;max-height:none}
  .has-sub:hover .sub{display:block}
  main h1{font-size:22px}
}
"""

def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    with open(os.path.join(OUT, "assets", "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)

    build_urlmap()
    build_home()
    for slug in DISTRICTS:
        build_district(slug)
    for d in DONGS:
        build_dong(d)
    for s in STATIONS:
        build_station(s)
    build_misc()
    build_sitemap_robots()

    print(f"생성 완료: 총 {len(ALL_URLS)} 페이지")
    for url, _ in ALL_URLS:
        print("  ", url)

if __name__ == "__main__":
    main()
