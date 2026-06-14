# 지하철역별 안내 — 허브 1개 + 역 21개.
# 환승역도 URL은 하나만 사용한다. 출구별·역+테마 조합 페이지는 만들지 않는다.
from .site import PHONE, PHONE_DISPLAY
from .pricing import PRICING
from ._data_stations import STATIONS

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>역 인근 위치와 희망 시간을 알려주시면 방문 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

_HUB_BODY = """
<p class="lead">고양시를 지나는 3호선·경의중앙선·서해선·GTX-A 주요 역세권을 기준으로 방문 관리를 안내합니다. 환승역은 노선이 여러 개라도 페이지는 하나만 운영합니다.</p>

<section>
<h2>역세권 안내 구성 기준</h2>
<p>고양시는 수도권 서북부 교통의 요지로 여러 노선이 지나갑니다. 이 사이트의 역 안내는 역마다 페이지 하나를 두는 단일 페이지 원칙을 따릅니다. 대곡역처럼 3호선·경의중앙선·서해선·GTX-A 네 개 노선이 만나는 환승 거점도, 화정역이나 능곡역처럼 두 노선이 겹치는 역도 페이지는 하나입니다. 출구 번호별 페이지나 역 이름에 관리 테마를 붙인 조합 페이지는 만들지 않습니다. 그런 페이지는 내용이 겹칠 수밖에 없고 검색 이용자에게도 도움이 되지 않기 때문입니다. 각 역 페이지에서는 역세권 분위기, 인근 대표 동, 방문 형태, 예약 시 참고사항을 역마다 고유하게 설명합니다.</p>
</section>

<section>
<h2>3호선 고양 구간</h2>
<p>3호선은 고양시를 동서로 길게 가로지르는 핵심 노선입니다. 동쪽 끝 <a href="/goyang/stations/jichuk-station/">지축역</a>부터 <a href="/goyang/stations/samsong-station/">삼송역</a>, <a href="/goyang/stations/wonheung-station/">원흥역</a>, <a href="/goyang/stations/wondang-station/">원당역</a>, <a href="/goyang/stations/hwajeong-station/">화정역</a>, <a href="/goyang/stations/daegok-station/">대곡역</a>을 지나 일산으로 들어가 <a href="/goyang/stations/baekseok-station/">백석역</a>, <a href="/goyang/stations/madu-station/">마두역</a>, <a href="/goyang/stations/jeongbalsan-station/">정발산역</a>, <a href="/goyang/stations/juyeop-station/">주엽역</a>, 종착 <a href="/goyang/stations/daehwa-station/">대화역</a>까지 이어집니다. 덕양구 상권과 일산 중심 상권을 모두 연결하는 노선입니다.</p>
</section>

<section>
<h2>경의중앙선 고양 구간</h2>
<p>경의중앙선은 한강 변을 따라 고양시 남부를 지납니다. 서울 방면의 <a href="/goyang/stations/hanguk-aerospace-univ-station/">한국항공대역</a>(화전)부터 <a href="/goyang/stations/gangmae-station/">강매역</a>, <a href="/goyang/stations/haengsin-station/">행신역</a>, <a href="/goyang/stations/neunggok-station/">능곡역</a>, <a href="/goyang/stations/daegok-station/">대곡역</a>, <a href="/goyang/stations/goksan-station/">곡산역</a>, <a href="/goyang/stations/baengma-station/">백마역</a>, <a href="/goyang/stations/pungsan-station/">풍산역</a>, <a href="/goyang/stations/ilsan-station/">일산역</a>, <a href="/goyang/stations/tanhyeon-station/">탄현역</a>으로 이어집니다. 대단지 주거권과 서울 출퇴근 수요가 함께 걸려 있는 노선입니다.</p>
</section>

<section>
<h2>서해선·GTX-A 고양 구간</h2>
<p>서해선(대곡소사선)은 <a href="/goyang/stations/daegok-station/">대곡역</a>과 <a href="/goyang/stations/neunggok-station/">능곡역</a>을 지나 김포공항 방면으로 이어져 서울 서남부 접근성을 높여 줍니다. GTX-A는 <a href="/goyang/stations/kintex-station/">킨텍스역</a>과 대곡역을 지나며, 킨텍스역은 전시·행사 생활권과 맞물려 행사 기간에 인근 숙소 방문 문의가 늘어나는 곳입니다. 환승 거점인 대곡역은 네 개 노선이 만나는 만큼 인근 이동 동선이 다양합니다.</p>
</section>

<section>
<h2>역 기준으로 예약하실 때</h2>
<p>역 이름은 위치를 설명하는 좋은 기준이지만, 실제 방문에는 정확한 주소가 필요합니다. 예약 전화에서 가까운 역과 함께 건물명 또는 도로명 주소를 알려주시면 도착 시간을 정확히 안내해 드릴 수 있습니다. 거주 지역 기준 안내가 편하시면 <a href="/goyang/">지역별 안내</a>를, 관리 유형이 먼저 궁금하시면 <a href="/themes/">테마별 안내</a>를 확인해 주세요. 어느 역에서 출발하든 예약 절차와 이용 기준은 동일합니다.</p>
</section>

<section>
<h2>역세권별 분위기 한눈에 보기</h2>
<p>스물한 개 역은 성격이 뚜렷하게 갈립니다. 화정역·백석역·정발산역은 상권·업무형 역세권이라 평일 저녁과 심야 문의가 많고, 마두역·풍산역·탄현역·삼송역은 대단지 주거 역세권이라 가족 단위 자택 예약이 중심입니다. 대화역과 킨텍스역은 전시·행사 생활권으로 행사 기간 숙소 방문 수요가 더해지고, 한국항공대역은 대학가 영향을 받습니다. 원당역·주교동 일대는 구도심 생활권, 대곡역은 네 개 노선이 만나는 환승 거점이라 방문 동선이 가장 다양합니다. 본인 생활 패턴과 비슷한 역 페이지를 골라 보시면 필요한 정보가 더 빨리 보일 것입니다. 어느 역이든 예약 절차와 비용 기준은 동일하므로, 역 선택은 위치 설명의 편의를 위한 것일 뿐입니다. 두 역 사이 애매한 위치라면 둘 중 아무 페이지나 보셔도 되고, 최종 안내는 언제나 주소 기준으로 이루어집니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>역에서 만나서 같이 이동하는 방식인가요?</h3>
<p>아니요, 관리사가 장비를 챙겨 알려주신 주소로 직접 방문합니다. 역은 위치를 설명하는 기준일 뿐 만남 장소가 아닙니다.</p>
</div>
<div class="faq-item">
<h3>환승역인데 무슨 호선 쪽인지 말해야 하나요?</h3>
<p>노선 구분은 필요 없습니다. 대곡역 같은 환승역도 페이지는 하나로 통합되어 있고, 방문은 주소 기준으로 진행됩니다.</p>
</div>
<div class="faq-item">
<h3>역에서 먼 위치인데 역 페이지를 봐도 되나요?</h3>
<p>괜찮습니다. 가까운 역으로 위치를 가늠하시고, 예약 시 도로명 주소만 알려주시면 동일하게 안내해 드립니다.</p>
</div>
<div class="faq-item">
<h3>GTX-A 킨텍스역이나 서해선 대곡역 쪽도 안내되나요?</h3>
<p>노선과 상관없이 모든 역세권을 같은 기준으로 안내합니다. 킨텍스역은 전시·행사 생활권, 대곡역은 네 개 노선 환승 거점으로 각 역 페이지에서 따로 설명합니다.</p>
</div>
<div class="faq-item">
<h3>3호선과 경의중앙선 중 어느 역으로 찾아야 하나요?</h3>
<p>편하신 노선 기준으로 보시면 됩니다. 같은 위치라도 가까운 역이 노선마다 다를 수 있으니, 예약 시에는 주소를 함께 알려주시면 가장 정확합니다.</p>
</div>
</section>
""" + PRICING + _CTA

HUB = {
    "path": "goyang/stations/",
    "title": "고양 지하철역 출장마사지·홈타이 | 3호선·경의중앙선 역세권 안내",
    "desc": "고양시 지하철역 인근 방문 관리 안내입니다. 화정역, 백석역, 대화역, 대곡역, 킨텍스역 등 3호선·경의중앙선·서해선·GTX-A 21개 역세권 기준으로 확인하세요.",
    "h1": "고양 지하철역별 안내",
    "body": _HUB_BODY,
    "breadcrumb": [("지하철역별 안내", None)],
}


def _station(slug, name, desc, body):
    return {
        "path": f"goyang/stations/{slug}/",
        "title": f"{name} 출장마사지·홈타이 | 역세권 방문 관리 안내",
        "desc": desc,
        "h1": f"{name} 인근 방문 관리 안내",
        "body": body + PRICING + _CTA,
        "breadcrumb": [("지하철역별 안내", "/goyang/stations/"), (name, None)],
    }


PAGES = [HUB] + [_station(s, n, d, b) for (s, n, d, b) in STATIONS]
