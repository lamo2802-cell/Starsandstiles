import os
import os, sys
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = "hello@starsandstiles.co.uk"
SITE = "https://starsandstiles.co.uk"

MARK = ('<svg class="mark" viewBox="0 0 48 48" width="34" height="34" aria-hidden="true">'
        '<circle class="moon" cx="31" cy="15" r="9" fill="#d9a441"/>'
        '<circle cx="35" cy="12" r="8" fill="#141c2e" class="bite"/>'
        '<path d="M4 40h40" stroke="#f7f3ea" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M13 40V22M31 40V22" stroke="#f7f3ea" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M10 27h24" stroke="#f7f3ea" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M13 40h18" stroke="#d9a441" stroke-width="3" stroke-linecap="round" opacity="0"/>'
        '</svg>')

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
<meta name="theme-color" content="#141c2e">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}/{path}">
<meta property="og:image" content="{SITE}/assets/cringley-413188738.jpg">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<script src="motion.js" defer></script>
</head>
<body>
"""


def nav(current):
    cur = ' aria-current="page"'
    items = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (h, cur if h == current else "", t) for h, t in NAV)
    return f"""<nav class="site"><div class="wrap">
<a class="logo" href="index.html">{MARK}<b>Stars <span>&amp;</span> Stiles</b></a>
<button class="menu-btn" aria-label="Menu" onclick="document.getElementById('m').classList.toggle('open')">Menu</button>
<ul id="m">{items}<li><a class="cta" href="contact.html">Get in touch</a></li></ul>
</div></nav>
"""


FOOT = f"""<footer class="site"><div class="wrap">
<div class="cols">
<div><h4>Stars &amp; Stiles</h4><p>Direct booking websites for UK holiday let owners, with regulation updates to help you stay on top of the rules.</p></div>
<div><h4>Explore</h4><a href="services.html">What we do</a><a href="compliance.html">Compliance Watch</a><a href="showcase.html">Showcase &amp; demos</a><a href="contact.html">Contact</a></div>
<div><h4>See it live</h4><a href="https://www.cringleycottage.com" target="_blank" rel="noopener">Cringley Cottage</a><a href="demos/seaside/">Example: The Old Lifeboat House</a><a href="demos/highland/">Example: Corrie Bothy</a><a href="demos/barn/">Example: Thorn Barn</a></div>
<div><h4>Legal</h4><a href="disclaimer.html">Important information</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
</div>
<div class="fine">&copy; 2026 Stars And Stiles Ltd (Company No. 14294081). Registered in England &amp; Wales.<br>
Our regulatory updates are general information and guidance only. They are not legal, tax or professional advice, and responsibility for compliance stays with the property owner. <a href="disclaimer.html" style="display:inline;color:var(--gold)">Read more</a>.</div>
</div></footer>
</body></html>
"""


def page(fname, title, desc, body):
    html = head(title, desc, "" if fname == "index.html" else fname) + nav(fname) + body + FOOT
    open(f"{OUT}/{fname}", "w").write(html)


# ---------- HOME ----------
page("index.html", "Stars & Stiles | Direct booking websites for holiday let owners",
     "We build direct booking websites for UK holiday let owners, then manage them for you or hand them over, and keep you informed of changing regulations. Built by holiday let owners.",
     """
<header class="hero"><span class="shoot"></span><span class="shoot s2"></span><div class="wrap">
<p class="eyebrow">Direct booking websites for holiday let owners</p>
<h1>Your cottage. Your website.<br>Your bookings.</h1>
<p class="lead">We build a beautiful direct booking site for your holiday let, so more guests book with you instead of paying a platform. We can look after it for you, or hand it over once it&rsquo;s live. Your choice. And as an optional extra, we keep you informed as the rules for holiday lets change.</p>
<a class="btn" href="contact.html">Talk to us</a><a class="btn ghost" href="showcase.html">See example sites</a>
</div></header>

<section class="block"><div class="wrap">
<div class="section-head"><p class="eyebrow" style="color:var(--gold-dark)">Why direct</p>
<h2>Keep the guest. Keep the margin.</h2>
<p>Listing sites are brilliant for being found, but every booking can cost you a commission, and the guest relationship belongs to the platform. A direct booking site puts you back in charge of pricing, policies and repeat business, alongside the platforms you already use.</p></div>
<div class="grid g3">
<div class="card"><div class="icon">£</div><h3>Less commission</h3><p>Direct bookings avoid platform commission. Card payments still carry a small processing fee, but it is a fraction of typical listing-site fees.</p></div>
<div class="card"><div class="icon">♥</div><h3>Repeat guests</h3><p>Guests who book direct are yours to welcome back, with your own emails, offers and returning-guest experience.</p></div>
<div class="card"><div class="icon">⚙</div><h3>No double bookings</h3><p>Your calendar syncs with Airbnb and Booking.com, so a booking on one place blocks the dates everywhere else.</p></div>
</div></div></section>

<section class="block alt"><div class="wrap">
<div class="section-head"><p class="eyebrow" style="color:var(--gold-dark)">The core service</p>
<h2>A complete booking website, built around your property</h2>
<p>Not a template you have to figure out. We design it around your property and set it all up. After launch, we can manage it for you, or hand it over to run yourself.</p></div>
<div class="grid g2">
<div class="card"><h3>What guests get</h3><ul class="ticks">
<li>A fast, mobile-friendly site that shows off your property</li>
<li>Live availability and instant price quotes</li>
<li>Secure card payment, with a deposit and balance option</li>
<li>Automatic booking confirmations and balance reminders</li>
<li>A guest information page for arrival details and house guide</li></ul></div>
<div class="card"><h3>What you get</h3><ul class="ticks">
<li>A simple owner login to manage prices and bookings</li>
<li>Calendar sync in and out with Airbnb and Booking.com</li>
<li>Booking notifications straight to your inbox</li>
<li>Cleaner logins and changeover checklists, if you want them</li>
<li>Hosting, updates and support by us, or a full hand-over, as you prefer</li></ul></div>
</div></div></section>

<section class="block dark"><div class="wrap">
<div class="section-head"><p class="eyebrow">Optional extra</p>
<h2>Compliance Watch: rules change, we keep you posted</h2>
<p>Running a holiday let now means keeping up with consumer law, safety duties, registration schemes and tax changes. Compliance Watch is an add-on where we track changes that affect holiday lets, send you plain-English updates, and where a change touches your website, we make the update for you.</p></div>
<div class="grid g3">
<div class="card"><h3>Updates in plain English</h3><p>What changed, who it affects and what owners commonly need to think about, with links to the official source.</p></div>
<div class="card"><h3>Website changes done for you</h3><p>When a rule affects your site, such as publishing a reviews policy or how prices are displayed, we can implement it for you.</p></div>
<div class="card"><h3>Owner tools</h3><p>Things like guest-safety changeover checklists, kept as a dated record you can show if you are ever asked.</p></div>
</div>
<p style="margin-top:2rem"><a class="btn" href="compliance.html">How Compliance Watch works</a></p>
</div></section>

<section class="block"><div class="wrap">
<div class="section-head"><h2>How it works</h2></div>
<div class="steps">
<div class="step"><h3>Chat</h3><p>Tell us about your property, your current listings and how you want to run bookings.</p></div>
<div class="step"><h3>Design</h3><p>We build a site around your photos and personality. See our examples for the range of styles.</p></div>
<div class="step"><h3>Connect</h3><p>We link your calendars, payments and emails, and test the whole booking journey.</p></div>
<div class="step"><h3>Launch &amp; hand over</h3><p>Your site goes live on your own domain. Then you choose: we keep managing it, or we hand it over to you.</p></div>
</div></div></section>

<section class="block alt"><div class="wrap">
<div class="grid g2" style="align-items:center">
<div style="border-radius:6px;overflow:hidden"><img src="assets/cringley-413188738.jpg" alt="Cringley Cottage in Askrigg, Yorkshire Dales" loading="lazy"></div>
<div><p class="eyebrow" style="color:var(--gold-dark)">Built by owners</p>
<h2>We run this ourselves</h2>
<p style="margin-bottom:1rem">Stars &amp; Stiles is the company behind <strong>Cringley Cottage</strong>, our own dog-friendly holiday let in Askrigg in the Yorkshire Dales. Its website takes direct bookings, syncs with Airbnb and Booking.com and runs day to day for us, so everything we offer has been used by real guests.</p>
<p style="margin-bottom:1.6rem">When the rules changed on consumer reviews, we made the update to our own site first. Compliance Watch is that same routine, offered to other owners.</p>
<a class="btn dark" href="https://www.cringleycottage.com" target="_blank" rel="noopener">Visit Cringley Cottage</a></div>
</div></div></section>

<section class="block"><div class="wrap narrow" style="text-align:center">
<h2>Let&rsquo;s talk about your property</h2>
<p style="color:var(--muted);margin-bottom:1.6rem">Tell us a little about your holiday let and we will come back with how we could help and what it would cost.</p>
<a class="btn" href="contact.html">Get in touch</a></div></section>
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
<li>Availability calendar with Airbnb and Booking.com sync</li>
<li>Instant quotes with seasonal and minimum-stay pricing</li>
<li>Secure payments with deposits and balance collection</li>
<li>Automated guest emails: confirmation, reminders, receipts</li>
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
<tr><td>Booking, payments &amp; guest emails</td><td>Included</td><td>Included</td></tr>
<tr><td>Airbnb / Booking.com calendar sync</td><td>Included</td><td>Included</td></tr>
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
<a class="show" href="https://www.cringleycottage.com" target="_blank" rel="noopener" style="max-width:820px">
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
<a class="show" href="demos/barn/"><div class="thumb" style="background:linear-gradient(180deg,#f0ebe0 0,#f0ebe0 60%,#c9a66b 60%,#c9a66b 100%)"><img src="https://images.unsplash.com/photo-1766854766161-86ca70a0f245?auto=format&fit=crop&q=75&w=900" alt="Barn interior with exposed beams" loading="lazy" onerror="this.remove()"><span class="live ex">Example</span></div>
<div class="body"><h3>Thorn Barn</h3><p>Clean, contemporary and editorial. A converted barn in the Cotswolds for groups and celebrations.</p><span class="more">View example &rarr;</span></div></a>
</div></div></section>

<section class="block"><div class="wrap narrow" style="text-align:center">
<h2>Want a site like these?</h2>
<p style="color:var(--muted);margin-bottom:1.6rem">Every design is built around your property, photos and guests.</p>
<a class="btn" href="contact.html">Get in touch</a></div></section>
""")

# ---------- CONTACT ----------
page("contact.html", "Contact | Stars & Stiles",
     "Tell us about your holiday let and how we can help with direct bookings and compliance updates.",
     f"""
<header class="hero" style="padding:4.5rem 0 3.5rem"><div class="wrap">
<p class="eyebrow">Get in touch</p><h1>Tell us about your holiday let</h1>
<p class="lead">A few details and we will come back with how we could help and what it would cost.</p></div></header>
<section class="block"><div class="wrap"><div class="grid g2">
<form class="contact" id="f" onsubmit="return send(event)">
<div><label for="n">Your name</label><input id="n" required></div>
<div><label for="e">Email</label><input id="e" type="email" required></div>
<div><label for="p">Property name and location</label><input id="p"></div>
<div><label for="i">I&rsquo;m interested in</label><select id="i"><option>A direct booking website</option><option>A direct booking website + Compliance Watch</option><option>Compliance Watch for my existing site</option><option>Not sure yet</option></select></div>
<div><label for="m">Anything else?</label><textarea id="m" placeholder="Number of properties, current listings, existing website..."></textarea></div>
<button class="btn" type="submit">Send enquiry</button>
<p style="font-size:.85rem;color:var(--muted)">This opens your email app with the details filled in, ready to send.</p>
</form>
<div><div class="card"><h3>Or email us directly</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p style="margin-top:1rem">Stars And Stiles Ltd<br>Company No. 14294081</p></div></div>
</div></div></section>
<script>
function send(ev){{ev.preventDefault();
var g=function(i){{return document.getElementById(i).value}};
var body="Name: "+g('n')+"\\nEmail: "+g('e')+"\\nProperty: "+g('p')+"\\nInterested in: "+g('i')+"\\n\\n"+g('m');
location.href="mailto:{EMAIL}?subject="+encodeURIComponent("Enquiry from starsandstiles.co.uk")+"&body="+encodeURIComponent(body);return false}}
</script>
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
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="10" fill="#141c2e"/><circle cx="31" cy="15" r="9" fill="#d9a441"/><circle cx="35" cy="12" r="8" fill="#141c2e"/><path d="M6 39h36" stroke="#f7f3ea" stroke-width="3" stroke-linecap="round"/><path d="M14 39V23M30 39V23M11 28h22" stroke="#f7f3ea" stroke-width="4" stroke-linecap="round"/></svg>')
open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nDisallow: /demos/\nSitemap: {SITE}/sitemap.xml\n")
pages = ["", "services.html", "compliance.html", "showcase.html", "contact.html", "disclaimer.html"]
open(f"{OUT}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                                      "".join(f"<url><loc>{SITE}/{p}</loc></url>\n" for p in pages) + "</urlset>\n")
print("ok")

# ---------- DESIGN B: "Daylight" (same content, different look), served from /v2/ ----------
BANNER = ('<div class="ab-banner">Design option B &middot; Daylight &nbsp;|&nbsp; <a href="../{p}">Compare with design A (Night sky)</a></div>')
os.makedirs(f"{OUT}/v2", exist_ok=True)
for fname in ["index.html", "services.html", "compliance.html", "showcase.html", "contact.html", "disclaimer.html"]:
    h = open(f"{OUT}/{fname}").read()
    h = h.replace('href="style.css">', 'href="../style.css">\n<link rel="stylesheet" href="../style-v2.css">')
    h = h.replace('src="motion.js"', 'src="../motion.js"').replace('href="assets/favicon.svg"', 'href="../assets/favicon.svg"')
    h = h.replace('src="assets/', 'src="../assets/').replace('url(assets/', 'url(../assets/').replace('href="demos/', 'href="../demos/')
    h = h.replace('<meta name="theme-color" content="#141c2e">', '<meta name="theme-color" content="#f6f1e7">\n<meta name="robots" content="noindex">')
    h = h.replace(f'<link rel="canonical" href="{SITE}/', f'<link rel="canonical" href="{SITE}/v2/')
    h = h.replace('<body>\n', '<body class="v2">\n' + BANNER.format(p=fname if fname != "index.html" else "") + '\n', 1)
    open(f"{OUT}/v2/{fname}", "w").write(h)
print("v2 ok")
