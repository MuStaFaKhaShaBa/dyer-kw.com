BASE = "https://dyer-kw.com"

FLOATING_BUTTONS = f"""    <!-- Floating Button -->
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

def header(active):
    """active: one of 'home','about','services','blog','areas','contact'"""
    def a(key, extra=""):
        return ' class="active"' if key == active else extra

    return f"""    <header id="header" class="header d-flex align-items-center sticky-top">
      <div
        class="container position-relative d-flex align-items-center justify-content-between">

        <!-- Logo with Arabic title and phone number -->
        <a href="{BASE}"
          class="logo d-flex align-items-center me-auto me-xl-0">
          <p class="sitename h2">
            صباغ أبو وليد
            <span class="d-none d-md-inline"> | 99660310</span>
          </p>
        </a>

        <!-- Arabic-optimized navigation -->
        <nav id="navmenu" class="navmenu">
          <ul>
            <li><a href="{BASE}"{a('home')}>الرئيسية</a></li>
            <li><a href="{BASE}/about.html"{a('about')}>من نحن</a></li>
            <li class="dropdown">
              <a href="{BASE}/services.html"{a('services')}><span>خدماتنا</span> <i
                  class="bi bi-chevron-down toggle-dropdown"></i></a>
              <ul>
                <li><a href="{BASE}/services.html#interior">صباغة
                    داخلية</a></li>
                <li><a href="{BASE}/services.html#exterior">صباغة
                    خارجية</a></li>
                <li><a
                    href="{BASE}/services.html#wallpaper">تركيب
                    ورق
                    جدران</a></li>
                <li><a href="{BASE}/services.html#gypsum">تركيب
                    جبس بورد</a></li>
                <li><a
                    href="{BASE}/services.html#parquet">تركيب
                    باركيه</a></li>
              </ul>
            </li>
            <li><a href="{BASE}/areas.html"{a('areas')}>مناطق التغطية</a></li>
            <li><a href="{BASE}/category.html"{a('blog')}>المدونة</a></li>
            <li><a href="{BASE}/contact.html"{a('contact')}>اتصل بنا</a></li>
          </ul>
          <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
        </nav>

        <!-- Kuwait-specific social links -->
        <div class="header-social-links">
          <a href="https://api.whatsapp.com/send?phone=96599660310"
            class="whatsapp" target="_blank" rel="noopener">
            <i class="bi bi-whatsapp"></i>
          </a>
          <a href="tel:+96599660310" class="phone">
            <i class="bi bi-telephone-fill"></i>
          </a>

        </div>

      </div>
    </header>
"""

def area_footer_links(area_items):
    """area_items: list of (name, slug) tuples, up to 5, for the footer 'مناطق الخدمة' column"""
    lines = []
    for name, slug in area_items:
        lines.append(f'              <li><a href="{BASE}/area-{slug}.html">{name}</a></li>')
    return "\n".join(lines)

def footer(area_items):
    area_links = area_footer_links(area_items)
    return f"""    <footer id="footer" class="footer dark-background">

      <div class="container footer-top">
        <div class="row gy-4">
          <div class="col-lg-4 col-md-6 footer-about">
            <a href="{BASE}"
              class="logo d-flex align-items-center">
              <span class="sitename">صباغ أبو وليد</span>
            </a>
            <div class="footer-contact pt-3">
              <p>الديجيج، محافظة الفروانية</p>
              <p>الكويت</p>
              <p class="mt-3"><strong>هاتف:</strong> <span>+965 9966
                  0310</span></p>
              <p><strong>واتساب:</strong> <span>+965 9966 0310</span></p>
            </div>
            <div class="social-links d-flex mt-4">
              <a href="https://api.whatsapp.com/send?phone=96599660310"
                target="_blank" rel="noopener"><i class="bi bi-whatsapp"></i></a>
              <a href="tel:+96599660310"><i
                  class="bi bi-telephone-fill"></i></a>
            </div>
          </div>

          <div class="col-lg-2 col-md-3 footer-links">
            <h4>روابط سريعة</h4>
            <ul>
              <li><a href="{BASE}">الرئيسية</a></li>
              <li><a href="{BASE}/about.html">من نحن</a></li>
              <li><a href="{BASE}/services.html">خدماتنا</a></li>
              <li><a href="{BASE}/areas.html">مناطق التغطية</a></li>
              <li><a href="{BASE}/category.html">المدونة</a></li>
              <li><a href="{BASE}/contact.html">اتصل بنا</a></li>
            </ul>
          </div>

          <div class="col-lg-2 col-md-3 footer-links">
            <h4>خدماتنا</h4>
            <ul>
              <li><a href="{BASE}/services.html#interior">صباغة
                  داخلية</a></li>
              <li><a href="{BASE}/services.html#exterior">صباغة
                  خارجية</a></li>
              <li><a href="{BASE}/services.html#wallpaper">ورق
                  جدران</a></li>
              <li><a href="{BASE}/services.html#gypsum">جبس
                  بورد</a></li>
              <li><a href="{BASE}/services.html#parquet">تركيب
                  باركيه</a></li>
            </ul>
          </div>

          <div class="col-lg-2 col-md-3 footer-links">
            <h4>مناطق الخدمة</h4>
            <ul>
{area_links}
              <li><a href="{BASE}/areas.html"><strong>عرض كل المناطق (45)</strong></a></li>
            </ul>
          </div>

          <div class="col-lg-2 col-md-3 footer-links">
            <h4>مواد نستخدمها</h4>
            <ul>
              <li><a href="{BASE}/services.html">دهانات جوتن</a></li>
              <li><a href="{BASE}/services.html">دهانات
                  ناشونال</a></li>
              <li><a href="{BASE}/services.html">دهانات سايبس</a></li>
              <li><a href="{BASE}/services.html#wallpaper">ورق
                  جدران أوروبي</a></li>
              <li><a href="{BASE}/services.html">مواد صديقة
                  للبيئة</a></li>
            </ul>
          </div>

        </div>
      </div>

      <div class="container copyright text-center mt-4">
        <p>© <span>حقوق النشر</span> <strong class="px-1 sitename">صباغ أبو
            وليد</strong> <span>محفوظة</span></p>
        <div class="credits">
          صباغ وتشطيبات في الكويت منذ 2010
        </div>
      </div>

    </footer>

    <!-- Scroll Top -->
    <a href="#" id="scroll-top"
      class="scroll-top d-flex align-items-center justify-content-center"><i
        class="bi bi-arrow-up-short"></i></a>

    <!-- Preloader -->
    <div id="preloader"></div>

    <!-- Vendor JS Files -->
    <script
      src="{BASE}/assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
    <script src="{BASE}/assets/vendor/aos/aos.js"></script>
    <script
      src="{BASE}/assets/vendor/swiper/swiper-bundle.min.js"></script>

    <!-- Main JS File -->
    <script src="{BASE}/assets/js/main.js"></script>
  </body>

</html>
"""

def head_open(title, description, keywords, canonical, og_title, og_desc, og_image, extra_schema=""):
    return f"""<!DOCTYPE html>
<html lang="ar-KW" dir="rtl">

  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- Title -->
    <title>{title}</title>

    <!-- Favicon -->
    <link rel="icon" href="{BASE}/assets/img/flagofkuwait_6485.ico"
      type="image/x-icon" />

    <!-- Meta Description -->
    <meta name="description"
      content="{description}" />

    <!-- Robots -->
    <meta name='robots'
      content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />
    <link rel="canonical" href="{canonical}" />

    <!-- Keywords -->
    <meta name="keywords"
      content="{keywords}" />

    <!-- Geo Tags -->
    <meta name="geo.region" content="KW" />
    <meta name="geo.placename" content="Al Farwaniyah, Kuwait" />
    <meta name="geo.position" content="29.2775;47.9586" />
    <meta name="ICBM" content="29.2775,47.9586" />
    <meta name="geo.country" content="KW" />

    <!-- Open Graph -->
    <meta property="og:title"
      content="{og_title}" />
    <meta property="og:description"
      content="{og_desc}" />
    <meta property="og:image"
      content="{og_image}" />
    <meta property="og:url" content="{canonical}" />
    <meta property="og:type" content="website" />
    <meta property="og:locale" content="ar_KW" />

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title"
      content="{og_title}" />
    <meta name="twitter:description"
      content="{og_desc}" />
    <meta name="twitter:image"
      content="{og_image}" />

    <!-- Fonts -->
    <link href="https://fonts.googleapis.com" rel="preconnect">
    <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,500;1,600;1,700;1,800&display=swap"
      rel="stylesheet">

    <!-- CSS -->
    <link
      href="{BASE}/assets/vendor/bootstrap/css/bootstrap.min.css"
      rel="stylesheet">
    <link
      href="{BASE}/assets/vendor/bootstrap-icons/bootstrap-icons.css"
      rel="stylesheet">
    <link href="{BASE}/assets/vendor/aos/aos.css" rel="stylesheet">
    <link href="{BASE}/assets/vendor/swiper/swiper-bundle.min.css"
      rel="stylesheet">
    <link rel="stylesheet" href="{BASE}/assets/css/main.css">
{extra_schema}
  </head>
"""

def breadcrumb_schema(items):
    """items: list of (name, url) tuples"""
    entries = ",\n    ".join(
        f'{{"@type": "ListItem", "position": {i+1}, "name": "{name}", "item": "{url}"}}'
        for i, (name, url) in enumerate(items)
    )
    return f"""    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {entries}
  ]
}}
</script>
"""

def local_business_schema(name, area_name=None):
    area_line = f',\n  "areaServed": {{"@type": "Place", "name": "{area_name}, Kuwait"}}' if area_name else ""
    return f"""    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "{name}",
  "telephone": "+96599660310",
  "priceRange": "$$",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "الفروانية",
    "addressRegion": "الكويت",
    "addressCountry": "KW"
  }}{area_line}
}}
</script>
"""

def h1_block(title, subtitle):
    return f"""      <h1 class="head-title mx-auto h2 w-75 text-center mt-4">
        {title}
        <span class="d-block fs-5 fw-normal mt-2">{subtitle}</span>
      </h1>
"""

def page_title_section(label, tagline, breadcrumb_items):
    """breadcrumb_items: list of (name, url_or_none) - last item has url_or_none=None (current page)"""
    crumbs = []
    for name, url in breadcrumb_items:
        if url:
            crumbs.append(f'          <li class="breadcrumb-item"><a href="{url}" class="text-decoration-none">{name}</a></li>')
        else:
            crumbs.append(f'          <li class="breadcrumb-item active" aria-current="page">{name}</li>')
    crumbs_html = "\n".join(crumbs)
    return f"""      <!-- Page Title Section -->
      <section class="page-title position-relative bg-light py-4">
        <div
          class="container d-lg-flex justify-content-between align-items-center">
          <div class="title-content">
            <h2 class="mb-2 mb-lg-0 text-primary">{label}</h2>
            <p class="lead text-muted d-none d-lg-block mt-2">{tagline}</p>
          </div>
          <nav aria-label="breadcrumb" class="breadcrumbs">
            <ol class="breadcrumb mb-0">
{crumbs_html}
            </ol>
          </nav>
        </div>
      </section>
"""
