import sys
sys.path.insert(0, "/home/claude/uploaded_site/dyer-kw.com/_build")
from shared import head_open, header, footer, h1_block, page_title_section, breadcrumb_schema, BASE

AREA_FOOTER_ITEMS = [("الفروانية","farwaniya"),("حولي","hawalli"),("السالمية","salmiya"),("الجهراء","jahra"),("الأحمدي","ahmadi")]

schema_extra = breadcrumb_schema([
    ("الرئيسية", f"{BASE}/"),
    ("خدماتنا", f"{BASE}/services.html"),
]) + f"""    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "صباغة وتشطيبات",
  "provider": {{"@type": "ProfessionalService", "name": "صباغ أبو وليد", "telephone": "+96599660310"}},
  "areaServed": {{"@type": "Country", "name": "Kuwait"}},
  "hasOfferCatalog": {{
    "@type": "OfferCatalog",
    "name": "خدمات صباغ أبو وليد",
    "itemListElement": [
      {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "صباغة داخلية"}}}},
      {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "صباغة خارجية"}}}},
      {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "تركيب ورق جدران"}}}},
      {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "تركيب جبس بورد"}}}},
      {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "تركيب باركيه"}}}}
    ]
  }}
}}
</script>
"""

head = head_open(
    title="خدماتنا | صباغة داخلية وخارجية وورق جدران - صباغ أبو وليد",
    description="صباغ أبو وليد يقدم صباغة داخلية وخارجية، تركيب ورق جدران، جبس بورد، وباركيه في الكويت بضمان 3 سنوات ودهانات جوتن بدون رائحة.",
    keywords="صباغة داخلية الكويت, صباغة خارجية الكويت, تركيب ورق جدران الكويت, تركيب جبس بورد الكويت, تركيب باركيه الكويت, اسعار صباغة الكويت",
    canonical=f"{BASE}/services.html",
    og_title="خدماتنا - صباغ أبو وليد",
    og_desc="صباغة داخلية وخارجية، ورق جدران، جبس بورد، وباركيه بضمان 3 سنوات.",
    og_image=f"{BASE}/assets/img/post-slide-1.webp",
    extra_schema=schema_extra
)

def service_block(anchor, tag_a, tag_b, title, desc, bullets, img, alt, author_role, reverse=False):
    order = "order-md-2" if reverse else ""
    bullets_html = "\n".join(f'      <li>{b}</li>' for b in bullets)
    return f"""
    <section id="{anchor}" class="business-category section">
      <div class="container" data-aos="fade-up">
        <div class="row align-items-center">
          <div class="col-md-6 {order}">
            <img loading="lazy" src="{BASE}/assets/img/{img}" alt="{alt}" class="img-fluid rounded">
          </div>
          <div class="col-md-6">
            <div class="post-meta"><span class="date">{tag_a}</span> <span class="mx-1">•</span> <span>{tag_b}</span></div>
            <h2 class="mb-2">{title}</h2>
            <p>{desc}</p>
            <ul class="mb-3">
{bullets_html}
            </ul>
            <span class="author d-block">{author_role}</span>
            <a href="{BASE}/contact.html" class="btn btn-primary mt-3">اطلب معاينة مجانية</a>
          </div>
        </div>
      </div>
    </section>
"""

body = f"""    <main class="main">
{h1_block("خدماتنا - صباغة وتشطيبات كاملة في الكويت", "دهانات جوتن بدون رائحة مع ضمان 3 سنوات على التنفيذ")}
{page_title_section("خدماتنا", "كل ما يحتاجه منزلك من صباغة وتشطيبات", [("الرئيسية", f"{BASE}/"), ("خدماتنا", None)])}

{service_block("interior","صباغة داخلية","بدون رائحة","صباغة داخلية للمنازل والشقق",
  "نقدم صباغة داخلية احترافية لجميع غرف المنزل باستخدام دهانات جوتن الأصلية بدون رائحة قوية، مع تجهيز كامل للجدران وتغطية الأثاث.",
  ["دهان غرف النوم والصالات والمطابخ","معالجة الشقوق الصغيرة قبل الدهان","دهانات آمنة للأطفال وكبار السن"],
  "post-landscape-3.webp","صباغة داخلية لمنزل في الكويت","فريق صباغة محترف")}

{service_block("exterior","صباغة خارجية","مقاوم للطقس","صباغة خارجية وواجهات الفلل",
  "دهانات خارجية مقاومة لأشعة الشمس والأمطار وحرارة الكويت، مع إمكانية عزل مائي للأسطح لحماية المبنى من التسريبات.",
  ["دهانات عاكسة للحرارة","تجهيز ورمل الواجهات القديمة","عزل حراري ومائي للأسطح"],
  "post-landscape-7.webp","صباغة خارجية لواجهة فيلا","فني صباغة خارجية", reverse=True)}

{service_block("wallpaper","ورق جدران","أحدث التصاميم","تركيب ورق جدران",
  "تركيب ورق حائط بجميع الخامات والتصاميم مع تسوية الجدران قبل التركيب لضمان نتيجة نظيفة بدون فقاعات هواء.",
  ["ورق جدران غرف الأطفال والصالات","خامات قابلة للغسيل ومقاومة للرطوبة","تركيب دقيق للنقشات المتكررة"],
  "post-landscape-5.webp","تركيب ورق جدران في الكويت","فني تركيب ورق جدران")}

{service_block("gypsum","جبس بورد","أسقف حديثة","تركيب جبس بورد وأسقف مستعارة",
  "تصميم وتنفيذ أسقف وديكورات جبسية بمستويات وإضاءة مخفية، مع دهان نهائي متقن يبرز التفاصيل.",
  ["أسقف مستعارة وبراويز جبسية","إضاءة مخفية ومنافذ تكييف مدمجة","تشطيب ودهان نهائي احترافي"],
  "post-landscape-2.webp","تركيب جبس بورد في الكويت","فني تشطيبات جبس", reverse=True)}

{service_block("parquet","باركيه","أرضيات خشبية","تركيب أرضيات باركيه",
  "تركيب أرضيات باركيه عالية الجودة بمختلف الخامات والألوان، مع تجهيز الأرضية بشكل صحيح لضمان ثبات ومتانة النتيجة.",
  ["باركيه HDF وSPC مقاوم للرطوبة","تركيب سريع ونظيف بدون فوضى","ضمان على التركيب"],
  "post-landscape-6.webp","تركيب أرضية باركيه في الكويت","فني تركيب أرضيات")}

    <!-- CTA -->
    <section class="py-5 text-center" style="background:#f5f5f5">
      <div class="container">
        <h2 class="mb-3">جاهزون لتنفيذ مشروعك اليوم</h2>
        <p class="lead text-muted mb-4">تواصل معنا الآن واحصل على معاينة وعرض سعر مجاني.</p>
        <a href="tel:+96599660310" class="btn btn-primary me-2">اتصل: 99660310</a>
        <a href="https://wa.me/96599660310" class="btn btn-outline-success">واتساب</a>
      </div>
    </section>

    </main>
"""

full = head + "  <body class=\"services-page\">\n\n" + \
"""    <!-- Floating Button -->
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

""" + header("services") + "\n" + body + "\n" + footer(AREA_FOOTER_ITEMS)

with open("/home/claude/uploaded_site/dyer-kw.com/services.html", "w", encoding="utf-8") as f:
    f.write(full)
print("services.html written")
