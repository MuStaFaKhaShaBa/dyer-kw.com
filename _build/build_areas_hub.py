import sys
sys.path.insert(0, "/home/claude/uploaded_site/dyer-kw.com/_build")
from areas import GOVERNORATES
from shared import head_open, header, footer, h1_block, page_title_section, breadcrumb_schema, BASE

FOOTER_AREAS = [("الفروانية","farwaniya"),("حولي","hawalli"),("السالمية","salmiya"),("الجهراء","jahra"),("الأحمدي","ahmadi")]

schema_extra = breadcrumb_schema([("الرئيسية", f"{BASE}/"), ("مناطق التغطية", f"{BASE}/areas.html")])

head = head_open(
    title="مناطق تغطية صباغ الكويت | 45 منطقة - صباغ أبو وليد",
    description="صباغ أبو وليد يغطي 45 منطقة في جميع محافظات الكويت الست. اختر منطقتك لمعرفة تفاصيل خدمة الصباغة فيها.",
    keywords="صباغ الكويت جميع المناطق, صباغ حولي, صباغ السالمية, صباغ الفروانية, صباغ الجهراء, صباغ مبارك الكبير, صباغ الاحمدي",
    canonical=f"{BASE}/areas.html",
    og_title="مناطق تغطية صباغ الكويت - صباغ أبو وليد",
    og_desc="خدمة صباغة في 45 منطقة عبر جميع محافظات الكويت.",
    og_image=f"{BASE}/assets/img/post-slide-1.webp",
    extra_schema=schema_extra
)

sections = []
for gov, areas in GOVERNORATES:
    chips = "\n".join(
        f'            <a href="{BASE}/area-{slug}.html" class="btn btn-outline-primary btn-sm m-1">صباغ {name}</a>'
        for name, slug, desc in areas
    )
    sections.append(f"""        <div class="mb-5">
          <h2 class="h4 mb-3">محافظة {gov}</h2>
          <div>
{chips}
          </div>
        </div>""")

body = f"""    <main class="main">
{h1_block("مناطق تغطية صباغ الكويت", "صباغ أبو وليد في 45 منطقة عبر جميع محافظات الكويت")}
{page_title_section("مناطق التغطية", "اختر منطقتك لمعرفة تفاصيل الخدمة فيها", [("الرئيسية", f"{BASE}/"), ("مناطق التغطية", None)])}

    <section class="section py-5">
      <div class="container">
{chr(10).join(sections)}
        <div class="p-4 rounded text-center" style="background:#f5f5f5">
          <p class="mb-0">لا ترى منطقتك في القائمة؟ لا مشكلة — نصل إلى جميع مناطق الكويت تقريباً. تواصل معنا وسنؤكد التغطية والموعد المناسب خلال دقائق.</p>
        </div>
      </div>
    </section>

    <section class="py-5 text-center" style="background:#f5f5f5">
      <div class="container">
        <h2 class="mb-3">احجز معاينة في منطقتك اليوم</h2>
        <a href="tel:+96599660310" class="btn btn-primary me-2">اتصل: 99660310</a>
        <a href="https://wa.me/96599660310" class="btn btn-outline-success">واتساب</a>
      </div>
    </section>

    </main>
"""

floating = """    <!-- Floating Button -->
    <a href="https://wa.me/96599660310"
      class="floating-button"
      title="Chat with me on WhatsApp" target="_blank" rel="noopener">
      <i class="bi bi-whatsapp"></i>
    </a>
    <!-- Floating Button -->
    <a href="tel:+96599660310" class="floating-button second"
      title="Call Us Now"
      target="_blank" rel="noopener">
      <i class="bi bi-telephone-fill"></i>
    </a>

"""

full = head + '  <body class="areas-page">\n\n' + floating + header("areas") + "\n" + body + "\n" + footer(FOOTER_AREAS)

with open("/home/claude/uploaded_site/dyer-kw.com/areas.html", "w", encoding="utf-8") as f:
    f.write(full)
print("areas.html hub written")
