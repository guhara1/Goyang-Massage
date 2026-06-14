# 지역별 안내 — 고양시 허브 1 + 자치구 허브 3 + 대표 동 30.
# 숫자 행정동(화정1동, 행신2동 등) 개별 페이지는 만들지 않는다.
from .site import PHONE, PHONE_DISPLAY
from .pricing import PRICING
from ._data_deogyang import DONGS as _DEO_A
from ._data_deogyang_b import DONGS as _DEO_B
from ._data_ilsan import ILSANDONG as ILSANDONG_DONGS, ILSANSEO as ILSANSEO_DONGS

DEO_DONGS = _DEO_A + _DEO_B

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>방문 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

# ── 고양시 전체 허브 ──────────────────────────────────────────────
_HUB_BODY = """
<p class="lead">고양시 방문 관리는 덕양구·일산동구·일산서구 세 개 자치구와 그 아래 대표 동을 기준으로 안내합니다. 거주하시는 행정동이 숫자로 나뉘어 있어도 대표 동 페이지에서 모든 정보를 확인하실 수 있습니다.</p>

<section>
<h2>고양시 지역 안내 구성</h2>
<p>고양시는 공식 기준으로 덕양구, 일산동구, 일산서구 세 개 자치구로 이루어져 있고, 행정동은 모두 합쳐 마흔 곳이 넘습니다. 다만 화정1동과 화정2동, 행신1동부터 행신4동, 백석1동과 백석2동처럼 숫자로 세분된 행정동은 이 사이트에서 화정동·행신동·백석동 같은 대표 동으로 통합해 안내합니다. 행정동 단위로 페이지를 쪼개면 같은 생활권을 두고 비슷한 설명이 반복될 수밖에 없고, 이용자 입장에서도 어느 페이지를 봐야 할지 혼란스럽기 때문입니다. 방문 가능 여부는 행정동 경계가 아니라 실제 위치와 예약 시간으로 판단하므로, 대표 동 기준 안내가 실제 이용 흐름과도 일치합니다. 행정동 이름으로 검색해 들어오셨더라도 필요한 내용은 모두 대표 동 페이지 안에 담아 두었습니다.</p>
</section>

<section>
<h2>세 개 자치구의 생활권 차이</h2>
<ul class="card-grid">
<li><a href="/goyang/deogyang-gu/">덕양구</a></li>
<li><a href="/goyang/ilsandong-gu/">일산동구</a></li>
<li><a href="/goyang/ilsanseo-gu/">일산서구</a></li>
</ul>
<p>덕양구는 화정·행신·삼송·원흥처럼 서울 접근성이 강한 생활권으로, 기존 주거 상권과 새로 들어선 택지지구가 함께 섞여 있습니다. 일산동구는 백석·마두·정발산·장항을 중심으로 상권과 오피스 수요가 모여 있고, 라페스타와 호수공원 일대의 유동 인구가 많습니다. 일산서구는 대화·주엽·일산·탄현을 중심으로 한 주거지에 킨텍스 전시 생활권이 더해지는 지역입니다. 같은 고양시라도 자치구마다 주거 형태와 생활 리듬이 다르기 때문에, 방문 시간대나 공간 준비에 대한 안내도 지역별로 조금씩 달라집니다. 각 자치구 페이지에서 소속 대표 동과 생활권 특징을 자세히 설명합니다.</p>
</section>

<section>
<h2>대표 동 통합 안내 기준</h2>
<p>덕양구는 주교동·원신동·흥도동·성사동·효자동·삼송동·창릉동·고양동·관산동·능곡동·화정동·행주동·행신동·화전동·대덕동 열다섯 곳, 일산동구는 식사동·중산동·정발산동·풍산동·백석동·마두동·장항동·고봉동 여덟 곳, 일산서구는 일산동·탄현동·주엽동·대화동·송포동·덕이동·가좌동 일곱 곳을 대표 동으로 둡니다. 성사1·2동은 성사동, 삼송1·2동은 삼송동, 화정1·2동은 화정동, 행신1~4동은 행신동, 중산1·2동은 중산동, 백석1·2동은 백석동, 마두1·2동은 마두동, 장항1·2동은 장항동, 일산1~3동은 일산동, 탄현1·2동은 탄현동, 주엽1·2동은 주엽동으로 통합합니다. 숫자 동 단위의 개별 페이지는 만들지 않는 것이 원칙입니다. 예약 시 도로명 주소만 알려주시면 어느 행정동이든 동일한 기준으로 안내해 드립니다.</p>
</section>

<section>
<h2>지역과 역세권을 함께 확인하세요</h2>
<p>고양시는 3호선·경의중앙선·서해선·GTX-A가 지나는 지역이라 동 기준보다 역 기준이 익숙한 분들도 많습니다. 화정역, 백석역, 대화역, 대곡역처럼 역 인근 위치에서 예약하실 때는 <a href="/goyang/stations/">지하철역별 안내</a>를 함께 확인해 보세요. 역 페이지에서는 해당 역세권의 생활권과 인접 동을 연결해 설명합니다. 다만 역과 동, 테마를 조합한 별도 페이지는 운영하지 않으므로, 원하시는 관리 유형은 <a href="/themes/">테마별 안내</a>에서 따로 확인하시면 됩니다. 동 페이지와 역 페이지 중 어느 쪽을 보셔도 예약 기준은 같으니, 본인에게 익숙한 기준으로 보시면 됩니다.</p>
</section>

<section>
<h2>예약 전 참고사항</h2>
<p>어느 동이든 예약 절차는 동일합니다. 위치 확인, 시간 확인, 코스·인원 확인, 방문 가능 여부 안내, 예약 확정 순서로 진행되며, 저녁 시간대와 주말은 문의가 몰릴 수 있어 미리 연락 주시는 편이 좋습니다. 아파트 단지는 동·호수와 공동현관 출입 방법을, 오피스텔과 숙소는 건물 출입 안내를 함께 알려주시면 방문이 한층 매끄럽습니다. 고양시 경계와 맞닿은 파주, 김포, 서울 은평·마포 방면 주소도 위치에 따라 방문이 가능할 수 있으니 포기하지 마시고 전화로 확인해 주세요. 자세한 준비사항은 <a href="/guide/">이용가이드</a>에서 확인하실 수 있습니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>우리 동네 행정동 이름이 안 보여요.</h3>
<p>숫자가 붙은 행정동은 모두 대표 동 페이지에 통합되어 있습니다. 예를 들어 행신3동은 행신동 페이지, 백석2동은 백석동 페이지를 보시면 됩니다.</p>
</div>
<div class="faq-item">
<h3>구 경계가 애매한 위치는 어떻게 하나요?</h3>
<p>경계 지역은 어느 페이지를 보셔도 무방합니다. 실제 방문은 주소 기준으로 진행되므로 예약 전화에서 정확한 주소만 알려주시면 됩니다.</p>
</div>
</section>
""" + PRICING + _CTA

HUB = {
    "path": "goyang/",
    "title": "고양시 출장마사지·홈타이 | 지역별 방문 관리 안내",
    "desc": "고양시 방문 관리 지역 안내입니다. 덕양구, 일산동구, 일산서구 세 개 자치구와 대표 동 기준으로 생활권 특징과 방문 조건을 확인하세요.",
    "h1": "고양시 지역별 안내",
    "body": _HUB_BODY,
    "breadcrumb": [("지역별 안내", None)],
}


# ── 자치구 허브 ──────────────────────────────────────────────────
def _gu_hub(slug, gu_name, title, desc, body):
    return {
        "path": f"goyang/{slug}/",
        "title": title,
        "desc": desc,
        "h1": f"{gu_name} 지역별 안내",
        "body": body + PRICING + _CTA,
        "breadcrumb": [("지역별 안내", "/goyang/"), (gu_name, None)],
    }


DEOGYANG_HUB = _gu_hub(
    "deogyang-gu", "덕양구",
    "덕양구 출장마사지·홈타이 | 고양 방문 관리 지역 안내",
    "덕양구 방문 마사지·홈타이 안내입니다. 화정동, 행신동, 삼송동 등 열다섯 개 대표 동 생활권과 화정역·삼송역·대곡역 역세권 기준으로 확인하세요.",
    """
<p class="lead">덕양구는 고양시에서 서울 접근성이 가장 강한 생활권으로, 열다섯 개 대표 동을 기준으로 방문 관리를 안내합니다.</p>

<section>
<h2>덕양구 생활권 개요</h2>
<p>덕양구는 화정·행신처럼 오래 자리 잡은 주거 상권과 삼송·원흥·창릉처럼 새로 형성된 택지지구·신도시가 함께 섞여 있는 지역입니다. 한강과 맞닿은 행주·대덕 방면, 북한산 자락의 효자동, 벽제 방면의 고양동·관산동까지 더해져 같은 자치구 안에서도 분위기 차이가 큽니다. 3호선·경의중앙선·서해선·GTX-A가 모두 지나가는 교통 요지여서 동마다 가까운 역과 방문 동선이 조금씩 다릅니다. 서울 은평·마포·상암으로 출퇴근하는 세대가 많아 평일 저녁과 심야 방문 문의가 꾸준한 것도 덕양구의 특징입니다. 신축 대단지와 구도심, 전원 주택가가 한 자치구 안에 공존하기 때문에, 예약 시 건물 유형과 출입 방법을 함께 알려주시면 방문 준비가 한결 수월합니다.</p>
</section>

<section>
<h2>덕양구 대표 동</h2>
<ul class="card-grid">
<li><a href="/goyang/deogyang-gu/jugyo-dong/">주교동</a></li>
<li><a href="/goyang/deogyang-gu/wonsin-dong/">원신동</a></li>
<li><a href="/goyang/deogyang-gu/heungdo-dong/">흥도동</a></li>
<li><a href="/goyang/deogyang-gu/seongsa-dong/">성사동</a></li>
<li><a href="/goyang/deogyang-gu/hyoja-dong/">효자동</a></li>
<li><a href="/goyang/deogyang-gu/samsong-dong/">삼송동</a></li>
<li><a href="/goyang/deogyang-gu/changneung-dong/">창릉동</a></li>
<li><a href="/goyang/deogyang-gu/goyang-dong/">고양동</a></li>
<li><a href="/goyang/deogyang-gu/gwansan-dong/">관산동</a></li>
<li><a href="/goyang/deogyang-gu/neunggok-dong/">능곡동</a></li>
<li><a href="/goyang/deogyang-gu/hwajeong-dong/">화정동</a></li>
<li><a href="/goyang/deogyang-gu/haengju-dong/">행주동</a></li>
<li><a href="/goyang/deogyang-gu/haengsin-dong/">행신동</a></li>
<li><a href="/goyang/deogyang-gu/hwajeon-dong/">화전동</a></li>
<li><a href="/goyang/deogyang-gu/daedeok-dong/">대덕동</a></li>
</ul>
<p>화정동과 행신동은 덕양구에서 인구가 가장 밀집한 상권·주거 중심이고, 삼송동과 창릉동은 신도시 개발로 세대가 빠르게 늘고 있는 지역입니다. 성사동·주교동은 원당 구도심 생활권, 화전동·대덕동은 서울 상암과 가까운 대학가·신축 업무권입니다. 각 동 페이지에서 생활권 특징과 방문 조건을 동마다 다르게 설명합니다.</p>
</section>

<section>
<h2>덕양구 인근 역세권</h2>
<p>덕양구 생활권과 연결되는 주요 역으로는 3호선·서해선 <a href="/goyang/stations/hwajeong-station/">화정역</a>, 3호선 <a href="/goyang/stations/wondang-station/">원당역</a>·<a href="/goyang/stations/samsong-station/">삼송역</a>·<a href="/goyang/stations/wonheung-station/">원흥역</a>·<a href="/goyang/stations/jichuk-station/">지축역</a>, 경의중앙선 <a href="/goyang/stations/haengsin-station/">행신역</a>·<a href="/goyang/stations/gangmae-station/">강매역</a>·<a href="/goyang/stations/neunggok-station/">능곡역</a>·<a href="/goyang/stations/hanguk-aerospace-univ-station/">한국항공대역</a>, 그리고 네 개 노선이 만나는 환승 거점 <a href="/goyang/stations/daegok-station/">대곡역</a>이 있습니다. 역 기준 안내가 편하시면 각 역 페이지를 함께 참고해 주세요.</p>
</section>

<section>
<h2>덕양구 예약 안내</h2>
<p>덕양구는 신축 대단지가 많아 공동현관 출입 방법과 방문 차량 등록 여부 확인이 중요합니다. 효자동·고양동·관산동처럼 외곽 주택가는 차량 이동 기준으로 도착 시간을 안내하므로, 큰길 기준 진입 방향을 함께 알려주시면 좋습니다. 예약 절차는 위치 확인, 시간 확인, 코스·인원 확인, 방문 가능 여부 안내, 예약 확정 순서로 진행되며 자세한 내용은 <a href="/reservation/">예약안내</a>와 <a href="/guide/">이용가이드</a>에서 확인하실 수 있습니다.</p>
</section>
""")

ILSANDONG_HUB = _gu_hub(
    "ilsandong-gu", "일산동구",
    "일산동구 출장마사지·홈타이 | 백석·마두·정발산 방문 관리 안내",
    "일산동구 방문 마사지·홈타이 안내입니다. 백석동, 마두동, 정발산동, 장항동 등 여덟 개 대표 동과 백석역·마두역·정발산역 역세권 기준으로 확인하세요.",
    """
<p class="lead">일산동구는 일산의 상권과 오피스 수요가 모인 생활권으로, 여덟 개 대표 동을 기준으로 방문 관리를 안내합니다.</p>

<section>
<h2>일산동구 생활권 개요</h2>
<p>일산동구는 백석동의 업무지구, 장항동의 라페스타·웨스턴돔 상권, 정발산동의 일산문화광장과 호수공원이 가까이 모여 있어 고양시 안에서도 유동 인구가 가장 많은 축에 듭니다. 백석·마두·정발산은 3호선 생활권으로 오피스와 주거가 가깝게 붙어 있고, 풍산·식사·중산·고봉은 경의중앙선과 외곽 주거권으로 분위기가 한결 차분합니다. 업무지구가 가까운 만큼 평일 저녁과 심야 방문 문의가 많고, 호수공원과 상권 일대는 주말 수요가 더해집니다. 같은 일산동구라도 업무지구·상권·대단지 주거·외곽 농촌권이 뚜렷하게 나뉘므로, 예약 시 가까운 역이나 단지명을 알려주시면 방문 동선을 정확히 잡을 수 있습니다.</p>
</section>

<section>
<h2>일산동구 대표 동</h2>
<ul class="card-grid">
<li><a href="/goyang/ilsandong-gu/siksa-dong/">식사동</a></li>
<li><a href="/goyang/ilsandong-gu/jungsan-dong/">중산동</a></li>
<li><a href="/goyang/ilsandong-gu/jeongbalsan-dong/">정발산동</a></li>
<li><a href="/goyang/ilsandong-gu/pungsan-dong/">풍산동</a></li>
<li><a href="/goyang/ilsandong-gu/baekseok-dong/">백석동</a></li>
<li><a href="/goyang/ilsandong-gu/madu-dong/">마두동</a></li>
<li><a href="/goyang/ilsandong-gu/janghang-dong/">장항동</a></li>
<li><a href="/goyang/ilsandong-gu/gobong-dong/">고봉동</a></li>
</ul>
<p>백석동은 요진와이시티와 일산테크노밸리를 낀 업무 중심, 장항동은 라페스타·호수공원을 낀 상권 중심입니다. 마두동과 정발산동은 3호선 주거·상권이 어우러진 지역이고, 풍산동·식사동·중산동·고봉동은 경의중앙선과 외곽 대단지 주거권입니다. 각 동 페이지에서 생활권과 방문 조건을 자세히 다룹니다.</p>
</section>

<section>
<h2>일산동구 인근 역세권</h2>
<p>일산동구의 주요 역으로는 3호선 <a href="/goyang/stations/baekseok-station/">백석역</a>·<a href="/goyang/stations/madu-station/">마두역</a>·<a href="/goyang/stations/jeongbalsan-station/">정발산역</a>, 경의중앙선 <a href="/goyang/stations/baengma-station/">백마역</a>·<a href="/goyang/stations/pungsan-station/">풍산역</a>이 있습니다. 백석·마두·정발산은 3호선 생활권, 풍산·백마는 경의중앙선 생활권으로 나뉩니다. 역 기준으로 위치를 설명하시면 더 편하게 안내받으실 수 있습니다.</p>
</section>

<section>
<h2>일산동구 예약 안내</h2>
<p>일산동구는 업무지구 오피스텔과 대단지 아파트 방문이 많아 건물 출입 방법과 호실 확인이 중요합니다. 라페스타·호수공원 일대는 주말 저녁 교통이 혼잡해 도착 시간에 여유를 두시는 편이 좋고, 식사동·고봉동 외곽은 차량 이동 기준으로 안내합니다. 예약 절차와 준비사항은 <a href="/reservation/">예약안내</a>와 <a href="/guide/">이용가이드</a>에서 확인하실 수 있습니다.</p>
</section>
""")

ILSANSEO_HUB = _gu_hub(
    "ilsanseo-gu", "일산서구",
    "일산서구 출장마사지·홈타이 | 대화·주엽·탄현 방문 관리 안내",
    "일산서구 방문 마사지·홈타이 안내입니다. 대화동, 주엽동, 일산동, 탄현동 등 일곱 개 대표 동과 대화역·주엽역·킨텍스역 역세권 기준으로 확인하세요.",
    """
<p class="lead">일산서구는 주거지와 킨텍스 생활권이 함께 이어지는 지역으로, 일곱 개 대표 동을 기준으로 방문 관리를 안내합니다.</p>

<section>
<h2>일산서구 생활권 개요</h2>
<p>일산서구는 대화동의 킨텍스·한류월드 전시 생활권부터 주엽·일산동의 주거 상권, 탄현·덕이·가좌·송포의 외곽 주거권까지 폭넓게 걸쳐 있습니다. 대화와 킨텍스 일대는 전시·공연·행사 수요와 맞물려 인근 호텔·숙소 방문 문의가 행사 기간에 크게 늘고, 주엽과 일산동은 강선·문촌·후곡마을 같은 대단지와 구일산 상권 검색이 함께 발생합니다. 탄현·덕이·가좌·송포는 차량 이동 기준 안내가 더 중요한 외곽 주거권입니다. 같은 일산서구라도 전시 생활권과 대단지 주거권, 외곽 주거권의 성격이 뚜렷이 다르므로, 예약 전 방문 가능 시간과 도착 동선을 미리 확인하시면 좋습니다.</p>
</section>

<section>
<h2>일산서구 대표 동</h2>
<ul class="card-grid">
<li><a href="/goyang/ilsanseo-gu/ilsan-dong/">일산동</a></li>
<li><a href="/goyang/ilsanseo-gu/tanhyeon-dong/">탄현동</a></li>
<li><a href="/goyang/ilsanseo-gu/juyeop-dong/">주엽동</a></li>
<li><a href="/goyang/ilsanseo-gu/daehwa-dong/">대화동</a></li>
<li><a href="/goyang/ilsanseo-gu/songpo-dong/">송포동</a></li>
<li><a href="/goyang/ilsanseo-gu/deogi-dong/">덕이동</a></li>
<li><a href="/goyang/ilsanseo-gu/gajwa-dong/">가좌동</a></li>
</ul>
<p>대화동은 킨텍스·한류월드 전시 생활권, 주엽동은 3호선 중심 상권·주거권입니다. 일산동은 경의중앙선 구일산 상권, 탄현동·덕이동은 대단지 주거권이며, 송포동·가좌동은 한강 방면 외곽 주거권입니다. 각 동 페이지에서 생활권과 방문 조건을 동마다 다르게 설명합니다.</p>
</section>

<section>
<h2>일산서구 인근 역세권</h2>
<p>일산서구의 주요 역으로는 3호선 <a href="/goyang/stations/daehwa-station/">대화역</a>·<a href="/goyang/stations/juyeop-station/">주엽역</a>, 경의중앙선 <a href="/goyang/stations/ilsan-station/">일산역</a>·<a href="/goyang/stations/tanhyeon-station/">탄현역</a>, GTX-A <a href="/goyang/stations/kintex-station/">킨텍스역</a>이 있습니다. 대화·킨텍스는 전시 생활권, 주엽·일산은 주거·상권 생활권으로 나뉩니다. 역 기준 위치 설명이 편하시면 각 역 페이지를 참고해 주세요.</p>
</section>

<section>
<h2>일산서구 예약 안내</h2>
<p>일산서구는 킨텍스 행사 기간에 숙소 방문 문의가 몰리므로, 행사 일정이 있는 날은 미리 예약을 잡아 두시는 편이 안전합니다. 송포동·가좌동·덕이동처럼 외곽 주거권은 차량 이동 기준으로 도착 시간을 안내하고, 대단지는 공동현관 출입 방법 확인이 필요합니다. 예약 절차와 준비사항은 <a href="/reservation/">예약안내</a>와 <a href="/guide/">이용가이드</a>에서 확인하실 수 있습니다.</p>
</section>
""")


# ── 대표 동 페이지 조립 ───────────────────────────────────────────
def _dong(district_slug, district_name, slug, name, desc, body):
    return {
        "path": f"goyang/{district_slug}/{slug}/",
        "title": f"{name} 출장마사지·홈타이 | 고양 방문 관리 예약 안내",
        "desc": desc,
        "h1": f"{name} 방문 관리 안내",
        "body": body + PRICING + _CTA,
        "breadcrumb": [("지역별 안내", "/goyang/"),
                       (district_name, f"/goyang/{district_slug}/"),
                       (name, None)],
    }


_DEO_PAGES = [_dong("deogyang-gu", "덕양구", s, n, d, b) for (s, n, d, b) in DEO_DONGS]
_ILSANDONG_PAGES = [_dong("ilsandong-gu", "일산동구", s, n, d, b) for (s, n, d, b) in ILSANDONG_DONGS]
_ILSANSEO_PAGES = [_dong("ilsanseo-gu", "일산서구", s, n, d, b) for (s, n, d, b) in ILSANSEO_DONGS]

PAGES = ([HUB, DEOGYANG_HUB, ILSANDONG_HUB, ILSANSEO_HUB]
         + _DEO_PAGES + _ILSANDONG_PAGES + _ILSANSEO_PAGES)
