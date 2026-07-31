import sys, os
sys.path.insert(0, "/home/claude/uploaded_site/dyer-kw.com/_build")
from areas import GOVERNORATES
from shared import head_open, header, footer, h1_block, page_title_section, breadcrumb_schema, local_business_schema, BASE

OUT = "/home/claude/uploaded_site/dyer-kw.com"
FOOTER_AREAS = [("الفروانية","farwaniya"),("حولي","hawalli"),("السالمية","salmiya"),("الجهراء","jahra"),("الأحمدي","ahmadi")]

flat = []
for gov, areas in GOVERNORATES:
    for name, slug, desc in areas:
        flat.append({"gov": gov, "name": name, "slug": slug, "desc": desc})
by_gov = {}
for item in flat:
    by_gov.setdefault(item["gov"], []).append(item)

def floating_buttons():
    return """    <!-- Floating Button -->
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

SERVICE_IMG = {
    "interior": "post-landscape-3.webp", "exterior": "post-landscape-7.webp",
    "wallpaper": "post-landscape-5.webp", "gypsum": "post-landscape-2.webp",
}

def area_body(name, gov, slug, desc, nearby):
    nearby_chips = "\n".join(
        f'            <a href="{BASE}/area-{n["slug"]}.html" class="btn btn-outline-secondary btn-sm m-1">صباغ {n["name"]}</a>'
        for n in nearby
    )
    return f"""    <main class="main">
{h1_block(f"صباغ {name} - دهانات وتشطيبات باحترافية", f"معاينة مجانية وضمان 3 سنوات على التنفيذ في {name}")}
{page_title_section(f"صباغ {name}", desc, [("الرئيسية", f"{BASE}/"), ("مناطق التغطية", f"{BASE}/areas.html"), (name, None)])}

    <section class="business-category section">
      <div class="container" data-aos="fade-up">
        <div class="row align-items-center">
          <div class="col-md-6">
            <img loading="lazy" src="{BASE}/assets/img/post-landscape-3.webp" alt="صباغة داخلية في {name}" class="img-fluid rounded">
          </div>
          <div class="col-md-6">
            <div class="post-meta"><span class="date">{gov}</span> <span class="mx-1">•</span> <span>{name}</span></div>
            <h2 class="mb-2">صباغ محترف في {name}</h2>
            <p>{name} من مناطق محافظة {gov}، و{desc}. يصل فريق صباغ أبو وليد إلى {name} لتنفيذ أعمال الصباغة الداخلية والخارجية وتركيب ورق الجدران والجبس بورد، بنفس الجودة وضمان 3 سنوات المعتمد في جميع مناطق الكويت.</p>
            <p>نوفر معاينة ميدانية مجانية في {name} وعرض سعر واضح قبل البدء، مع دهانات جوتن الأصلية بدون رائحة.</p>
            <a href="{BASE}/contact.html" class="btn btn-primary mt-2">اطلب معاينة مجانية في {name}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section py-5" style="background:#f9f9f9">
      <div class="container">
        <h2 class="text-center mb-4">خدماتنا في {name}</h2>
        <div class="row g-4">
          <div class="col-md-3 col-6 text-center">
            <a href="{BASE}/services.html#interior" class="text-decoration-none">
              <img loading="lazy" src="{BASE}/assets/img/post-landscape-3.webp" alt="صباغة داخلية {name}" class="img-fluid rounded mb-2" style="aspect-ratio:4/3;object-fit:cover">
              <h3 class="h6">صباغة داخلية</h3>
            </a>
          </div>
          <div class="col-md-3 col-6 text-center">
            <a href="{BASE}/services.html#exterior" class="text-decoration-none">
              <img loading="lazy" src="{BASE}/assets/img/post-landscape-7.webp" alt="صباغة خارجية {name}" class="img-fluid rounded mb-2" style="aspect-ratio:4/3;object-fit:cover">
              <h3 class="h6">صباغة خارجية</h3>
            </a>
          </div>
          <div class="col-md-3 col-6 text-center">
            <a href="{BASE}/services.html#wallpaper" class="text-decoration-none">
              <img loading="lazy" src="{BASE}/assets/img/post-landscape-5.webp" alt="ورق جدران {name}" class="img-fluid rounded mb-2" style="aspect-ratio:4/3;object-fit:cover">
              <h3 class="h6">ورق جدران</h3>
            </a>
          </div>
          <div class="col-md-3 col-6 text-center">
            <a href="{BASE}/services.html#gypsum" class="text-decoration-none">
              <img loading="lazy" src="{BASE}/assets/img/post-landscape-2.webp" alt="جبس بورد {name}" class="img-fluid rounded mb-2" style="aspect-ratio:4/3;object-fit:cover">
              <h3 class="h6">جبس بورد</h3>
            </a>
          </div>
        </div>
      </div>
    </section>

    <section class="section py-5">
      <div class="container">
        <div class="p-4 rounded" style="background:#f5f5f5">
          <h2 class="h4 mb-3">لماذا يختارنا سكان {name}؟</h2>
          <div class="row">
            <div class="col-md-6"><p>✓ معاينة مجانية وسريعة في {name}</p></div>
            <div class="col-md-6"><p>✓ ضمان 3 سنوات على التنفيذ</p></div>
            <div class="col-md-6"><p>✓ دهانات جوتن الأصلية بدون رائحة</p></div>
            <div class="col-md-6"><p>✓ الالتزام التام بالموعد المتفق عليه</p></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section pb-5">
      <div class="container">
        <h2 class="h5 mb-3">نخدم أيضاً مناطق قريبة من {name}</h2>
        <div>
{nearby_chips}
          <a href="{BASE}/areas.html" class="btn btn-dark btn-sm m-1">+ كل المناطق</a>
        </div>
      </div>
    </section>

    <section class="py-5 text-center" style="background:#f5f5f5">
      <div class="container">
        <h2 class="mb-3">احجز معاينة مجانية في {name}</h2>
        <a href="tel:+96599660310" class="btn btn-primary me-2">اتصل: 99660310</a>
        <a href="https://wa.me/96599660310" class="btn btn-outline-success">واتساب</a>
      </div>
    </section>

    </main>
"""

generated = []
for item in flat:
    gov, name, slug, desc = item["gov"], item["name"], item["slug"], item["desc"]
    title = f"صباغ {name} | صباغ أبو وليد الكويت"
    if len(title) > 58:
        title = f"صباغ {name} | أبو وليد"

    schema_extra = breadcrumb_schema([
        ("الرئيسية", f"{BASE}/"),
        ("مناطق التغطية", f"{BASE}/areas.html"),
        (name, f"{BASE}/area-{slug}.html"),
    ]) + local_business_schema(f"صباغ أبو وليد - {name}", area_name=name)

    head = head_open(
        title=title,
        description=f"صباغ أبو وليد يقدم خدمات الصباغة الداخلية والخارجية وورق الجدران والجبس بورد في {name} (محافظة {gov}) بضمان 3 سنوات. اتصل الآن 99660310.",
        keywords=f"صباغ {name}, صباغ منازل {name}, صباغة داخلية {name}, صباغة خارجية {name}, ورق جدران {name}",
        canonical=f"{BASE}/area-{slug}.html",
        og_title=f"صباغ {name} - صباغ أبو وليد",
        og_desc=f"معاينة مجانية وضمان 3 سنوات في {name}.",
        og_image=f"{BASE}/assets/img/post-slide-1.webp",
        extra_schema=schema_extra
    )

    siblings = [x for x in by_gov[gov] if x["slug"] != slug]
    nearby = (siblings * 2)[:3] if siblings else []

    body = area_body(name, gov, slug, desc, nearby)
    full = head + '  <body class="area-page">\n\n' + floating_buttons() + header("areas") + "\n" + body + "\n" + footer(FOOTER_AREAS)

    with open(os.path.join(OUT, f"area-{slug}.html"), "w", encoding="utf-8") as f:
        f.write(full)
    generated.append((gov, name, slug, len(title)))

print(f"Generated {len(generated)} area pages, max title len:", max(t for *_, t in generated))
