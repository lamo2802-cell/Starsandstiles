import os
import os, sys
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = "hello@starsandstiles.co.uk"
SITE = "https://starsandstiles.co.uk"

SPARK = ('<svg class="sp %s" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0C12.5 7 17 11.5 24 12C17 12.5 12.5 17 12 24C11.5 17 7 12.5 0 12C7 11.5 11.5 7 12 0Z" fill="currentColor"/></svg>')
def spark(cls=""): return SPARK % cls

def _gate():
    """Hand-drawn style five-bar gate between dry stone walls, with grass tufts."""
    import random
    rnd = random.Random(7)
    o = ['<svg class="gate" viewBox="0 0 260 84" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.15" stroke-linecap="round" stroke-linejoin="round">']
    def wall(rows):
        for (yt, yb, xs, xe) in rows:
            x = xs
            while x < xe - 5:
                w = min(rnd.choice([11, 13, 15, 17, 19]), xe - x)
                h = yb - yt
                o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2.4" fill="#f5f2eb"/>' % (x, yt + rnd.uniform(-.7, .7), w - 1, h))
                x += w
    wall([(58, 68, 6, 84), (48, 58, 14, 84), (38, 48, 36, 84), (28, 38, 62, 84)])
    wall([(58, 68, 176, 254), (48, 58, 176, 246), (38, 48, 176, 224), (28, 38, 176, 198)])
    # posts with caps
    for x in (86, 168):
        o.append('<rect x="%d" y="16" width="6" height="52" fill="#f5f2eb"/><path d="M%d 16l3 -4l3 4"/>' % (x, x))
    # rails (double-line planks), five bars
    for y in (22, 31, 40, 49, 58):
        o.append('<rect x="92" y="%d" width="76" height="4" fill="#f5f2eb"/>' % y)
    # diagonal brace and centre slat
    o.append('<path d="M92 62L168 24M92 57L168 19" />')
    o.append('<path d="M130 20v42"/>')
    # latch
    o.append('<path d="M160 36h5"/>')
    # grass tufts
    def tuft(x, y, n=4, hgt=9):
        for k in range(n):
            dx = (k - (n - 1) / 2) * 2.6
            o.append('<path d="M%.1f %.1fq%.1f -%.1f %.1f -%.1f" opacity=".85"/>' % (x + dx, y, dx * .5, hgt * .55, dx * 1.3, hgt - abs(dx) * .6))
    for x in (78, 96, 112, 148, 164, 180, 8, 246):
        tuft(x, 70, rnd.choice([3, 4, 5]), rnd.choice([7, 9, 11]))
    o.append('<path d="M2 70h256" opacity=".55"/>')
    o.append('</svg>')
    return "".join(o)

GATE = _gate()

def BRAND():
    return ('<a class="brand" href="index.html">' + GATE + spark("b1") + spark("b2") +
            '<span class="bn">STARS &amp; STILES</span><span class="bt">FOR HOLIDAY LET OWNERS</span></a>')

def ico(name):
    P = {
     "calendar":'<rect x="5" y="7" width="22" height="20" rx="2"/><path d="M5 13h22M11 4v5M21 4v5"/>',
     "chat":'<path d="M6 8h20a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H15l-6 5v-5H6a2 2 0 0 1-2-2V10a2 2 0 0 1 2-2z"/>',
     "house":'<path d="M4 15L16 4l12 11M7 13v15h18V13M13 28v-8h6v8"/>',
     "shield":'<path d="M16 4l10 4v8c0 6-4 10-10 12C10 26 6 22 6 16V8z"/><path d="M11.5 16l3.5 3.5 6-7"/>',
     "coin":'<circle cx="16" cy="16" r="11"/><path d="M20 11.5c-1-1.3-2.4-1.8-4-1.8-2.4 0-4 1.4-4 3.3 0 4 8 2.4 8 6.7 0 2-1.8 3.3-4.2 3.3-1.8 0-3.3-.7-4.3-2M10.5 16h9"/>',
     "heart":'<path d="M16 27C6 20 4 14.5 4 11.5A6 6 0 0 1 16 9a6 6 0 0 1 12 2.5C28 14.5 26 20 16 27z"/>',
     "sliders":'<path d="M5 9h22M5 16h22M5 23h22"/><circle cx="12" cy="9" r="2.4" fill="#faf8f3"/><circle cx="21" cy="16" r="2.4" fill="#faf8f3"/><circle cx="10" cy="23" r="2.4" fill="#faf8f3"/>',
     "mug":'<path d="M6 10h15v10a6 6 0 0 1-6 6h-3a6 6 0 0 1-6-6zM21 12h3a3 3 0 0 1 0 6h-3"/><path d="M11 4c-1 1.5 1 2.5 0 4M16 4c-1 1.5 1 2.5 0 4"/>',
     "sun":'<circle cx="16" cy="16" r="5"/><path d="M16 4v4M16 24v4M4 16h4M24 16h4M7.5 7.5l2.8 2.8M21.7 21.7l2.8 2.8M7.5 24.5l2.8-2.8M21.7 10.3l2.8-2.8"/>',
    }
    return '<svg class="ic" viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">'+P[name]+'</svg>'

def botanical():
    import math
    out=['<svg class="botan" viewBox="0 0 200 320" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round">']
    stems=[(70,318,[(66,250),(74,190),(72,120)],72,90,26),(120,318,[(124,260),(112,200),(118,150)],118,138,22),(160,318,[(158,270),(166,220),(160,190)],160,178,17)]
    for x0,y0,pts,hx,hy,r in stems:
        d="M%d %d "%(x0,y0)+" ".join("L%d %d"%p for p in pts)+" L%d %d"%(hx,hy+r*0.4)
        out.append('<path d="%s"/>'%d)
        # umbel
        n=11
        for k in range(n):
            a=math.pi*(1.1+0.8*k/(n-1))*-1+math.pi  # fan upward
            a=-math.pi/2+(k-(n-1)/2)*0.32
            ex=hx+math.cos(a)*r*1.25; ey=hy-r*0.4+math.sin(a)*r*1.25+r*0.35
            out.append('<path d="M%d %d L%.1f %.1f"/><circle cx="%.1f" cy="%.1f" r="1.8" fill="currentColor"/>'%(hx,hy+r*0.3,ex,ey,ex,ey))
        # leaves
        for (lx,ly,dx) in [(x0,y0-50,-26),(x0+4,y0-110,24),(x0-2,y0-165,-20)]:
            out.append('<path d="M%d %d q%d -22 %d -34 M%d %d q%d -6 %d -14 M%d %d q%d -8 %d -20"/>'%(lx,ly,dx,dx*1.6,lx+dx*0.5,ly-12,dx*0.5,dx*0.8,lx+dx*0.9,ly-22,dx*0.5,dx*0.8))
    out.append('</svg>')
    return "".join(out)

NAV = [("index.html", "Home"), ("services.html", "What we do"), ("compliance.html", "Compliance Watch"),
       ("showcase.html", "Showcase")]


def head(title, desc, path):
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{path}">
<meta name="theme-color" content="#f5f2eb">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}/{path}">
<meta property="og:image" content="{SITE}/assets/cringley-413188738.jpg">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<script src="motion.js" defer></script>
</head>
<body>
"""


def nav(current):
    cur = ' aria-current="page"'
    items = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (h, cur if h == current else "", t) for h, t in NAV)
    return f"""<header class="topbar"><div class="wrap">
{BRAND()}
<button class="menu-btn" aria-label="Menu" onclick="document.getElementById('m').classList.toggle('open')">Menu</button>
<nav class="site"><ul id="m">{items}<li><a class="cta" href="contact.html">Get in touch</a></li></ul></nav>
</div></header>
"""


FOOT = f"""<footer class="site"><div class="wrap">
<div class="cols">
<div><h4>Stars &amp; Stiles</h4><p>Direct booking websites for UK holiday let owners, with regulation updates to help you stay on top of the rules.</p></div>
<div><h4>Explore</h4><a href="services.html">What we do</a><a href="compliance.html">Compliance Watch</a><a href="showcase.html">Showcase &amp; demos</a><a href="contact.html">Contact</a></div>
<div><h4>See it live</h4><a href="https://www.cringleycottage.com" target="_blank" rel="noopener">Cringley Cottage</a><a href="demos/seaside/">Example: The Old Lifeboat House</a><a href="demos/highland/">Example: Corrie Bothy</a><a href="demos/barn/">Example: Thorn Barn</a></div>
<div><h4>Contact</h4><a href="disclaimer.html">Important information</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:+447854075084">07854 075084</a></div>
</div>
<div class="fine">&copy; 2026 Stars And Stiles Ltd (Company No. 14294081). Registered in England &amp; Wales.<br>
Our regulatory updates are general information and guidance only. They are not legal, tax or professional advice, and responsibility for compliance stays with the property owner. <a href="disclaimer.html" style="display:inline">Read more</a>.</div>
</div></footer>
</body></html>
"""


def page(fname, title, desc, body):
    html = head(title, desc, "" if fname == "index.html" else fname) + nav(fname) + body + FOOT
    open(f"{OUT}/{fname}", "w").write(html)


# ---------- HOME ----------
GATEPHOTO = "https://images.unsplash.com/photo-1737027883185-24b41fca2431?auto=format&fit=crop&q=75&w=1600"
WINDOWPHOTO = "https://images.unsplash.com/photo-1770893670070-42a3c6f85133?auto=format&fit=crop&q=75&w=1200"

def photo(url, fallback, alt, cls=""):
    return f'<img class="{cls}" src="{url}" alt="{alt}" loading="lazy" onerror="this.onerror=null;this.src=\'{fallback}\'">'

page("index.html", "Stars & Stiles | Direct booking websites for holiday let owners",
     "We build direct booking websites for UK holiday let owners, then manage them for you or hand them over, and keep you informed of changing regulations. Built by holiday let owners.",
     f"""
<section class="home-hero"><div class="wrap">
<div class="hh-text">
<h1>Your holiday let.<br>Your own website.<br>Your bookings.</h1>
<span class="rule"></span>
<p>We build direct booking websites for holiday let owners, so more guests book with you instead of paying a platform.</p>
<p>We can look after your site for you, or hand it over once it&rsquo;s live. Your choice.</p>
<a class="btn" href="#how">See how it works &nbsp;&rarr;</a>
</div>
<div class="hh-photo">{photo(GATEPHOTO, "assets/cringley-413188738.jpg", "A stone barn on a green hillside in the Yorkshire Dales")}
{spark("s1")}{spark("s2")}{spark("s3")}</div>
</div></section>

<section class="strip"><div class="wrap"><div class="cells">
<div><span class="i">{ico("house")}</span><h3>A site of your own</h3><p>Direct bookings on your own domain, beautifully designed.</p></div>
<div><span class="i">{ico("calendar")}</span><h3>Calendars in sync</h3><p>Airbnb, Booking.com and other listing sites, no double bookings.</p></div>
<div><span class="i">{ico("chat")}</span><h3>Guest communications</h3><p>Confirmations, reminders, check-in and check-out, sent for you.</p></div>
<div><span class="i">{ico("shield")}</span><h3>Compliance Watch</h3><p>Plain-English updates when the rules change. An optional extra.</p></div>
</div></div></section>

<section class="story"><div class="s-photo">{photo(WINDOWPHOTO, "assets/cringley-living.jpg", "Sunlight through a cottage window")}</div>
<div class="s-panel"><div class="s-in">
<p class="label">Built by owners</p>
<h2>We run a holiday let too.</h2>
<span class="rule"></span>
<p>Stars &amp; Stiles is the company behind <strong>Cringley Cottage</strong>, our own dog-friendly holiday let in Askrigg in the Yorkshire Dales. Its website takes direct bookings, syncs with Airbnb and Booking.com, and runs day to day for us.</p>
<p>When the rules changed on consumer reviews, we made the update to our own site first. Compliance Watch is that same routine, offered to other owners.</p>
<a class="btn" href="https://www.cringleycottage.com" target="_blank" rel="noopener">Visit Cringley Cottage &nbsp;&rarr;</a>
</div>{botanical()}{spark("s4")}{spark("s5")}</div></section>

<section class="band"><div class="wrap"><div class="band-in">
<div class="b-text"><p class="label center">A simpler way to run your holiday let</p>
<h2 class="center">More time for what you love.</h2>
<div class="cells four">
<div><span class="i">{ico("coin")}</span><h3>No commission</h3><p>Direct bookings carry no booking commission. You keep what your guests pay, less only the card processing fee charged by the payment provider.</p></div>
<div><span class="i">{ico("heart")}</span><h3>Happier guests</h3><p>A seamless journey, from booking to check-out.</p></div>
<div><span class="i">{ico("sliders")}</span><h3>Greater control</h3><p>Your prices, policies and guest relationships, all in one place.</p></div>
<div><span class="i">{ico("mug")}</span><h3>More freedom</h3><p>We manage it, or hand it over. Either way, more time for you.</p></div>
</div></div>
<div class="b-photo"><img src="assets/cringley-garden.jpg" alt="Garden table at Cringley Cottage" loading="lazy"></div>
</div></div></section>

<section class="block" id="what"><div class="wrap">
<div class="section-head center"><p class="label">The core service</p>
<h2>A complete booking website, built around your property</h2>
<span class="rule"></span>
<p>Not a template you have to figure out. We design it around your property and set it all up. After launch, we can manage it for you, or hand it over to run yourself.</p></div>
<div class="grid g2">
<div class="card"><h3>What guests get</h3><ul class="ticks">
<li>A fast, mobile-friendly site that shows off your property</li>
<li>Live availability and instant price quotes</li>
<li>Secure card payment, with a deposit and balance option</li>
<li>Automated guest communications: booking confirmations, payment reminders, check-in and check-out emails</li>
<li>A guest information page for arrival details and house guide</li></ul></div>
<div class="card"><h3>What you get</h3><ul class="ticks">
<li>A simple owner login to manage prices and bookings</li>
<li>Calendar sync in and out with Airbnb, Booking.com and other listing sites</li>
<li>Booking notifications straight to your inbox</li>
<li>Cleaner logins and changeover checklists, if you want them</li>
<li>Hosting, updates and support by us, or a full hand-over, as you prefer</li></ul></div>
</div>
<p class="center" style="margin-top:2.2rem"><a class="btn ghost-dark" href="services.html">Everything we do &nbsp;&rarr;</a></p>
</div></section>

<section class="block dark"><div class="wrap">
<div class="section-head center"><p class="label">Optional extra</p>
<h2>Compliance Watch: rules change, we keep you posted</h2>
<span class="rule"></span>
<p>Running a holiday let now means keeping up with consumer law, safety duties, registration schemes and tax changes. Compliance Watch is an add-on where we track changes that affect holiday lets, send you plain-English updates, and where a change touches your website, we make the update for you.</p></div>
<div class="grid g3">
<div class="card"><h3>Updates in plain English</h3><p>What changed, who it affects and what owners commonly need to think about, with links to the official source.</p></div>
<div class="card"><h3>Website changes done for you</h3><p>When a rule affects your site, such as publishing a reviews policy or how prices are displayed, we can implement it for you.</p></div>
<div class="card"><h3>Owner tools</h3><p>Things like guest-safety changeover checklists, kept as a dated record you can show if you are ever asked.</p></div>
</div>
<p class="center" style="margin-top:2.2rem"><a class="btn light" href="compliance.html">How Compliance Watch works &nbsp;&rarr;</a></p>
</div></section>

<section class="block" id="how"><div class="wrap">
<div class="section-head center"><p class="label">How it works</p><h2>Four simple steps</h2><span class="rule"></span></div>
<div class="steps">
<div class="step"><h3>Chat</h3><p>Tell us about your property, your current listings and how you want to run bookings.</p></div>
<div class="step"><h3>Design</h3><p>We build a site around your photos and personality. See our examples for the range of styles.</p></div>
<div class="step"><h3>Connect</h3><p>We link your calendars, payments and emails, and test the whole booking journey.</p></div>
<div class="step"><h3>Launch &amp; hand over</h3><p>Your site goes live on your own domain. Then you choose: we keep managing it, or we hand it over to you.</p></div>
</div></div></section>

<section class="block alt"><div class="wrap">
<div class="section-head center"><p class="label">Our work</p><h2>Every property is different</h2><span class="rule"></span>
<p>Each site is unique to its property, with its own look, feel and personality.</p></div>
<div class="showcase">
<a class="show" href="demos/seaside/"><div class="thumb" style="background:linear-gradient(180deg,#bfe4f2 0,#eaf6fa 55%,#f4dfb4 55%,#e8cf98 75%,#3f9cc0 75%,#2b7fa3 100%)"><img src="https://images.unsplash.com/photo-1510069551606-f9ec0a62fe28?auto=format&fit=crop&q=75&w=900" alt="White house beside the sea" loading="lazy" onerror="this.remove()"></div><div class="body"><h3>The Old Lifeboat House</h3><p>Coastal, bright and airy.</p><span class="more">View example &rarr;</span></div></a>
<a class="show" href="demos/highland/"><div class="thumb" style="background:linear-gradient(180deg,#0e1420 0,#26324a 55%,#3a3020 55%,#1a1712 100%)"><img src="https://images.unsplash.com/photo-1773057679427-3aa69c2369e2?auto=format&fit=crop&q=75&w=900" alt="Small white house in a misty Scottish glen" loading="lazy" onerror="this.remove()"></div><div class="body"><h3>Corrie Bothy</h3><p>Dark, moody and atmospheric.</p><span class="more">View example &rarr;</span></div></a>
<a class="show" href="demos/barn/"><div class="thumb" style="background:linear-gradient(180deg,#12372a 0,#12372a 60%,#f2b632 60%,#f2b632 100%)"><img src="https://images.unsplash.com/photo-1766854766161-86ca70a0f245?auto=format&fit=crop&q=75&w=900" alt="Barn interior with exposed beams" loading="lazy" onerror="this.remove()"></div><div class="body"><h3>Thorn Barn</h3><p>Clean, contemporary and editorial.</p><span class="more">View example &rarr;</span></div></a>
</div>
<p class="center" style="margin-top:2.2rem"><a class="btn ghost-dark" href="showcase.html">See all examples &nbsp;&rarr;</a></p>
</div></section>

<section class="block cta-block"><div class="wrap narrow center">
{spark("s6")}<h2>Let&rsquo;s talk about your property</h2>
<p>Tell us a little about your holiday let and we will come back with how we could help and what it would cost.</p>
<a class="btn" href="contact.html">Get in touch &nbsp;&rarr;</a></div></section>
""")

# ---------- SERVICES ----------
page("services.html", "What we do | Stars & Stiles",
     "Direct booking websites for holiday lets, managed by us or handed over to you, plus an optional Compliance Watch regulation update service.",
     """
<header class="hero" style="padding:4.5rem 0 3.5rem"><div class="wrap">
<p class="eyebrow">What we do</p><h1>Two services, one goal</h1>
<p class="lead">Get you more direct bookings, and help you keep up with the rules of running a holiday let.</p></div></header>

<section class="block"><div class="wrap">
<div class="grid g2">
<div class="card"><span class="tag">Core service</span><h2 style="font-size:1.8rem">Direct Booking Site</h2>
<p>We design and build your holiday let website, then either manage it for you or hand it over.</p>
<ul class="ticks">
<li>Bespoke design around your property and brand</li>
<li>Availability calendar that syncs with Airbnb, Booking.com and other listing sites</li>
<li>Instant quotes with seasonal and minimum-stay pricing</li>
<li>Secure payments with deposits and balance collection</li>
<li>Automated guest communications: booking confirmation, payment reminders and receipts, check-in details before arrival, check-out reminders on departure day</li>
<li>Owner admin area for prices and bookings</li>
<li>Guest info page, house guide and terms</li>
<li>Your own domain, set up in your name</li>
<li>Hosting, security updates and support, if you choose us to manage it</li></ul></div>
<div class="card"><span class="tag green">Optional add-on</span><h2 style="font-size:1.8rem">Compliance Watch</h2>
<p>Regulation updates and website changes to go with them.</p>
<ul class="ticks">
<li>Plain-English updates when rules affecting holiday lets change</li>
<li>Links to the official source for every update</li>
<li>Website changes made for you where a rule touches the site</li>
<li>Reviews policy, price display and guest information pages kept current</li>
<li>Optional safety changeover checklists with dated records</li>
<li>A simple owner checklist of the areas worth reviewing</li></ul>
<p style="margin-top:1.2rem"><a href="compliance.html"><strong>More about Compliance Watch &rarr;</strong></a></p></div>
</div></div></section>

<section class="block alt"><div class="wrap">
<div class="section-head"><h2>Two ways to run your site</h2>
<p>Every site is built the same way. What happens after launch is up to you, and you can switch later.</p></div>
<div class="grid g2">
<div class="card"><span class="tag">Option 1</span><h3>We manage it</h3><p>We keep the site hosted, secure and up to date, update prices and content when you ask, and look after the technical side, so you can get on with welcoming guests.</p>
<ul class="ticks"><li>Hosting, security and updates included</li><li>Changes made for you</li><li>Support when something needs fixing</li></ul></div>
<div class="card"><span class="tag green">Option 2</span><h3>We build it, you run it</h3><p>We design and build the site, set everything up in your own accounts, show you how it all works, and hand it over. It is yours to manage.</p>
<ul class="ticks"><li>Domain, hosting and accounts in your name</li><li>A walkthrough of how to run it day to day</li><li>Optional support or Compliance Watch, whenever you want it</li></ul></div>
</div></div></section>

<section class="block"><div class="wrap">
<div class="section-head"><h2>At a glance</h2></div>
<div class="tablewrap"><table class="cmp">
<tr><th></th><th>Direct Booking Site</th><th>+ Compliance Watch</th></tr>
<tr><td>Website design &amp; build</td><td>Included</td><td>Included</td></tr>
<tr><td>Ongoing management</td><td>Your choice: we manage it, or we hand it over</td><td>Works with either option</td></tr>
<tr><td>Booking, payments &amp; automated guest communications (check-in and check-out emails and more)</td><td>Included</td><td>Included</td></tr>
<tr><td>Calendar sync with Airbnb, Booking.com &amp; other listing sites</td><td>Included</td><td>Included</td></tr>
<tr><td>Regulation updates by email</td><td>&ndash;</td><td>Included</td></tr>
<tr><td>Rule-driven website updates</td><td>Quoted as needed</td><td>Included where the change affects your site (if we manage it, or by arrangement if you run it)</td></tr>
<tr><td>Owner compliance checklist</td><td>&ndash;</td><td>Included</td></tr>
</table></div>
<p style="margin-top:1.2rem;color:var(--muted);font-size:.93rem">Pricing depends on your property and how you want to run it, so we quote for each owner. Get in touch and we will give you a clear figure with no surprises.</p>
</div></section>

<section class="block"><div class="wrap narrow">
<h2>What we don&rsquo;t do</h2>
<p style="color:var(--muted);margin-bottom:1rem">To keep expectations clear: we are not solicitors, accountants or fire safety assessors. We do not give legal or tax advice, carry out risk assessments or inspections, or take on your legal responsibilities as owner. Compliance Watch helps you stay informed and keeps your website up to date. For advice on your own circumstances, you should always speak to a qualified professional.</p>
<a class="btn dark" href="disclaimer.html">Read the full notice</a></div></section>
""")

# ---------- COMPLIANCE ----------
page("compliance.html", "Compliance Watch | Stars & Stiles",
     "Regulation updates for UK holiday let owners, plus website changes made for you when the rules affect your site.",
     """
<header class="hero" style="padding:4.5rem 0 3.5rem"><div class="wrap">
<p class="eyebrow">Optional add-on</p><h1>Compliance Watch</h1>
<p class="lead">The rules for holiday lets keep moving. We watch for changes, tell you what they mean in plain English, and update your website where it is affected.</p></div></header>

<section class="block"><div class="wrap">
<div class="section-head"><h2>How it works</h2></div>
<div class="steps">
<div class="step"><h3>We watch</h3><p>We follow official sources and trade bodies for changes that affect UK holiday lets.</p></div>
<div class="step"><h3>We tell you</h3><p>You get a short update: what changed, who it affects, and where to read the official detail.</p></div>
<div class="step"><h3>We update your site</h3><p>Where a change touches your website, we make the changes for you, such as a new policy page or how prices are shown.</p></div>
<div class="step"><h3>You decide</h3><p>The action is always yours. For your own circumstances, a qualified adviser is the right person to ask.</p></div>
</div></div></section>

<section class="block alt"><div class="wrap">
<div class="section-head"><h2>Areas we keep an eye on</h2>
<p>These are the kinds of topics we follow. Which ones apply to you depends on your property and where it is, and some differ between England, Wales, Scotland and Northern Ireland.</p></div>
<div class="tablewrap"><table class="cmp">
<tr><th>Area</th><th>What we track</th><th>Where it can show up on your site</th></tr>
<tr><td>Consumer law &amp; reviews</td><td>Rules on fake or incentivised reviews and how reviews are presented</td><td>Reviews policy page, review display</td></tr>
<tr><td>Pricing display</td><td>Rules on showing the full price up front, including mandatory fees</td><td>Quote and checkout pages</td></tr>
<tr><td>Fire &amp; guest safety</td><td>Duties around fire risk, alarms and safety records for guests</td><td>Changeover checklists, guest info page</td></tr>
<tr><td>Gas, electrical &amp; other safety</td><td>Certificate and inspection expectations</td><td>Owner reminders and records</td></tr>
<tr><td>Registration &amp; licensing</td><td>National and local schemes for short-term lets</td><td>Registration details on your site where required</td></tr>
<tr><td>Tax</td><td>Changes to how holiday let income is treated</td><td>Owner updates only, no site change</td></tr>
<tr><td>Data &amp; privacy</td><td>Guest data, cookies and privacy notice expectations</td><td>Privacy notice, cookie banner</td></tr>
<tr><td>Terms &amp; cancellations</td><td>Fair terms, refund and cancellation wording</td><td>Booking terms page</td></tr>
</table></div></div></section>

<section class="block"><div class="wrap narrow">
<div class="section-head"><h2>A real example</h2></div>
<div class="timeline">
<div class="tl"><time>1 &middot; The rules change</time><h3>Fake reviews are banned</h3><p>New consumer law and regulator guidance made it clear that businesses should be open about how they collect and show reviews.</p></div>
<div class="tl"><time>2 &middot; We tell owners</time><h3>A short, plain update</h3><p>What changed, what it means for a holiday let taking direct bookings, and a link to the official guidance.</p></div>
<div class="tl"><time>3 &middot; We update the site</time><h3>A reviews policy page</h3><p>On our own Cringley Cottage site, we published a reviews policy and linked it beside the guest reviews. With Compliance Watch, we do the same on yours.</p></div>
</div>
<p style="margin-top:2rem"><a class="btn dark" href="https://www.cringleycottage.com/reviews-policy.html" target="_blank" rel="noopener">See it on Cringley Cottage</a></p>
</div></section>

<section class="block dark"><div class="wrap narrow">
<h2>Clear about what this is</h2>
<p style="margin-bottom:1rem">Compliance Watch is an information and website-maintenance service. It is general guidance, not legal, tax or professional advice, and we do not guarantee that following it will meet every legal requirement that applies to you. Rules change and vary by location, so please check official sources or take professional advice for your own situation.</p>
<a class="btn" href="disclaimer.html">Full notice</a> <a class="btn ghost" href="contact.html">Ask us a question</a></div></section>
""")

# ---------- SHOWCASE ----------
page("showcase.html", "Showcase | Stars & Stiles",
     "See a live holiday let site we run, plus more example sites showing different designs.",
     """
<header class="hero" style="padding:4.5rem 0 3.5rem"><div class="wrap">
<p class="eyebrow">Showcase</p><h1>Every property is different</h1>
<p class="lead">One live site we run ourselves, and more examples showing how the look and feel can change while the booking engine underneath stays reliable.</p></div></header>

<section class="block"><div class="wrap">
<div class="section-head"><h2>Live site</h2></div>
<a class="show wide" href="https://www.cringleycottage.com" target="_blank" rel="noopener">
<div class="thumb" style="background-image:url(assets/cringley-IMG_1423.jpg)"><span class="live">Live</span></div>
<div class="body"><h3>Cringley Cottage, Yorkshire Dales</h3>
<p>Our own dog-friendly cottage in Askrigg. Direct bookings with deposits, Airbnb and Booking.com sync, guest emails, cleaner checklists and a reviews policy. This is the site everything else is based on.</p>
<span class="more">Visit cringleycottage.com &rarr;</span></div></a>
</div></section>

<section class="block alt"><div class="wrap">
<div class="section-head"><h2>Other examples</h2>
<p>Each site we build is unique to its property, with its own look, feel and personality. These examples show the range, from bright and coastal to dark and dramatic to clean and contemporary.</p></div>
<div class="showcase">
<a class="show" href="demos/seaside/"><div class="thumb" style="background:linear-gradient(180deg,#bfe4f2 0,#eaf6fa 55%,#f4dfb4 55%,#e8cf98 75%,#3f9cc0 75%,#2b7fa3 100%)"><img src="https://images.unsplash.com/photo-1510069551606-f9ec0a62fe28?auto=format&fit=crop&q=75&w=900" alt="White house beside the sea" loading="lazy" onerror="this.remove()"><span class="live ex">Example</span></div>
<div class="body"><h3>The Old Lifeboat House</h3><p>Coastal, bright and airy. A seaside cottage on the Cornish coast for families and dogs.</p><span class="more">View example &rarr;</span></div></a>
<a class="show" href="demos/highland/"><div class="thumb" style="background:linear-gradient(180deg,#0e1420 0,#26324a 55%,#3a3020 55%,#1a1712 100%)"><img src="https://images.unsplash.com/photo-1773057679427-3aa69c2369e2?auto=format&fit=crop&q=75&w=900" alt="Small white house in a misty Scottish glen" loading="lazy" onerror="this.remove()"><span class="live ex">Example</span></div>
<div class="body"><h3>Corrie Bothy</h3><p>Dark, moody and atmospheric. A Highland hideaway for couples, with a hot tub and dark skies.</p><span class="more">View example &rarr;</span></div></a>
<a class="show" href="demos/barn/"><div class="thumb" style="background:linear-gradient(180deg,#12372a 0,#12372a 60%,#f2b632 60%,#f2b632 100%)"><img src="https://images.unsplash.com/photo-1766854766161-86ca70a0f245?auto=format&fit=crop&q=75&w=900" alt="Barn interior with exposed beams" loading="lazy" onerror="this.remove()"><span class="live ex">Example</span></div>
<div class="body"><h3>Thorn Barn</h3><p>Clean, contemporary and editorial. A converted barn in the Cotswolds for groups and celebrations.</p><span class="more">View example &rarr;</span></div></a>
</div></div></section>

<section class="block"><div class="wrap narrow" style="text-align:center">
<h2>Want a site like these?</h2>
<p style="color:var(--muted);margin-bottom:1.6rem">Every design is built around your property, photos and guests.</p>
<a class="btn" href="contact.html">Get in touch</a></div></section>
""")

# ---------- CONTACT ----------
page("contact.html", "Contact | Stars & Stiles",
     "Get in touch by email or phone to talk about a direct booking website for your holiday let.",
     f"""
<header class="hero" style="padding:4.5rem 0 3.5rem"><div class="wrap">
<p class="eyebrow">Get in touch</p><h1>Tell us about your holiday let</h1>
<p class="lead">Drop us an email or give us a call and we will come back with how we could help and what it would cost.</p></div></header>
<section class="block"><div class="wrap narrow" style="text-align:center">
<div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">
<a class="btn" href="mailto:{EMAIL}?subject=Enquiry%20from%20starsandstiles.co.uk">&#9993;&nbsp; Email us</a>
<a class="btn ghost-dark" href="tel:+447854075084">&#9742;&nbsp; Call 07854 075084</a>
</div>
<p style="margin-top:1.6rem;color:var(--muted)">{EMAIL}</p>
<p style="margin-top:2.4rem;font-size:.9rem;color:var(--muted)">Stars And Stiles Ltd &middot; Company No. 14294081</p>
</div></section>
""")

# ---------- DISCLAIMER ----------
page("disclaimer.html", "Important information | Stars & Stiles",
     "How to read our regulatory updates: general information, not legal or professional advice.",
     """
<header class="hero" style="padding:4rem 0 3rem"><div class="wrap"><p class="eyebrow">Legal</p><h1 style="font-size:clamp(2rem,5vw,3rem)">Important information</h1></div></header>
<section class="block"><div class="wrap narrow">
<h3>Information and guidance only</h3>
<p style="margin-bottom:1.4rem;color:var(--muted)">Compliance Watch updates, checklists, website text and anything else we send or publish about regulations are general information and guidance. They are not legal, tax, financial, insurance or fire-safety advice, and they do not create a solicitor-client or other professional relationship.</p>
<h3>Not a guarantee</h3>
<p style="margin-bottom:1.4rem;color:var(--muted)">We make reasonable efforts to keep information accurate and up to date, but laws and guidance change and differ between England, Wales, Scotland and Northern Ireland and between local authorities. We do not guarantee that information is complete, current or suitable for your circumstances, or that acting on it will make you compliant.</p>
<h3>Responsibility stays with the owner</h3>
<p style="margin-bottom:1.4rem;color:var(--muted)">As the owner or operator of a holiday let, you are responsible for meeting the legal requirements that apply to you. Where we update your website or provide tools such as checklists or policy text, please check that they are right for your property, and take professional advice where you need it. Website changes we make are made on your instructions and are drafted from general templates.</p>
<h3>Check the official source</h3>
<p style="margin-bottom:1.4rem;color:var(--muted)">Our updates link to official sources where possible. Where our summary and an official source differ, the official source is right.</p>
<h3>Our service scope</h3>
<p style="margin-bottom:1.4rem;color:var(--muted)">We are a website and information business. We do not carry out risk assessments, inspections or certification, and we do not act as your legal, tax or safety adviser. Our liability is set out in the terms of the written agreement between us.</p>
<h3>Example sites</h3>
<p style="margin-bottom:1.4rem;color:var(--muted)">The Old Lifeboat House, Corrie Bothy and Thorn Barn are fictional properties created to show design styles. They are not real holiday lets, and no bookings can be made.</p>
<h3>Privacy</h3>
<p style="color:var(--muted)">If you contact us, we use your details only to reply to your enquiry and to provide our services. This site does not use advertising trackers. To ask about your data, email <a href="mailto:hello@starsandstiles.co.uk">hello@starsandstiles.co.uk</a>.</p>
</div></section>
""")

open(f"{OUT}/assets/favicon.svg", "w").write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="8" fill="#1f2f26"/><g fill="none" stroke="#f5f2eb" stroke-width="2" stroke-linecap="round"><path d="M12 38V19M36 38V19M12 21h24M12 28h24M12 34h24M12 34l24-13"/><path d="M4 39h40"/></g><path d="M35 5c.3 3 2 4.7 5 5-3 .3-4.7 2-5 5-.3-3-2-4.7-5-5 3-.3 4.7-2 5-5z" fill="#c9a86a"/></svg>')
open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nDisallow: /demos/\nSitemap: {SITE}/sitemap.xml\n")
pages = ["", "services.html", "compliance.html", "showcase.html", "contact.html", "disclaimer.html"]
open(f"{OUT}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                                      "".join(f"<url><loc>{SITE}/{p}</loc></url>\n" for p in pages) + "</urlset>\n")
print("ok")


import shutil
shutil.rmtree(f"{OUT}/v2", ignore_errors=True)
print("built")
