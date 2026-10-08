"""Build the static web edition from the checked, editable content file."""
from pathlib import Path
from html import escape as e
import json

ROOT = Path(__file__).resolve().parent
d = json.loads((ROOT / 'content.json').read_text())
s = d['summary']
r = d['practitioner_account']
topics = d['testimony']
def p(t): return '<p>' + e(t) + '</p>'
def ps(items): return ''.join(p(t) for t in items)
def section(title, items): return '<section class="prose-block"><h3>'+e(title)+'</h3>'+ps(items)+'</section>'

case = section(s[2],s[3:5])+section(s[6],s[7:9])+section(s[9],s[10:12])+section(s[12],s[13:15])+section(s[15],s[16:18])
skills=''.join('<li><strong>'+e(t.split(':',1)[0])+'</strong><span>'+e(t.split(':',1)[1].strip())+'</span></li>' for t in s[20:25])
case += '<section class="prose-block"><h3>'+e(s[18])+'</h3>'+p(s[19])+'<ul class="skills">'+skills+'</ul></section>'+section(s[25],s[26:])
role=p(r[1])+'<ul class="duties">'+''.join('<li>'+e(t)+'</li>' for t in r[2:10])+'</ul><h3>Everyday work and the case for guards</h3>'+ps(r[10:-1])+'<p class="byline">Active Train Guard</p>'
shortnames=['Emergencies','Sexual assaults','Anti-social behaviour','Accessibility','Security']
filters='<button type="button" data-filter="all" aria-pressed="true">All themes</button>'+''.join('<button type="button" data-filter="'+t['key']+'" aria-pressed="false">'+name+'</button>' for t,name in zip(topics,shortnames))
voices=''
for i,t in enumerate(topics):
    quotes=''.join('<blockquote><p>'+e(q)+'</p><footer>Train guard testimony</footer></blockquote>' for q in t['quotes'])
    voices+='<section class="topic" id="'+t['key']+'" data-topic="'+t['key']+'" aria-labelledby="heading-'+t['key']+'"><div class="topic-heading"><div><span class="eyebrow">'+str(i+1).zfill(2)+' / In guards’ own words</span><h3 id="heading-'+t['key']+'">'+e(t['title'])+'</h3><a class="source-link" href="assets/more-than-checking-tickets.pdf#page='+str(i+7)+'">Read in the report <span aria-hidden="true">↗</span></a></div><div class="stat"><strong>'+e(t['figure'])+'</strong>'+p(t['stat'])+'</div></div><div class="quotes">'+quotes+'</div></section>'

html='''<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>More than checking tickets | A guard’s perspective</title>
<meta name="description" content="Safety. Judgement. Passenger care. Explore a serving train guard’s account and 41 first-hand testimonies about the work behind a railway journey.">
<meta name="theme-color" content="#09243d"><meta property="og:title" content="More than checking tickets"><meta property="og:description" content="A guard’s perspective on safety, judgement and passenger care."><meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><script src="app.js" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap header-inner"><a class="wordmark" href="#top"><span class="wordmark-rule" aria-hidden="true"></span>A guard’s perspective</a><button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" hidden>Menu <span aria-hidden="true">+</span></button><nav id="site-nav" aria-label="Main navigation"><a href="#case-study">The case study</a><a href="#guard-role">The testimony</a><a href="#experiences">Experiences</a><a class="nav-download" href="assets/more-than-checking-tickets.pdf" download>Download PDF <span aria-hidden="true">↓</span></a></nav></div></header>
<main id="main"><section class="hero wrap" id="top"><div class="hero-top"><div><p class="eyebrow">The people behind the journey</p><h1>More than<br>checking tickets<span class="orange">.</span></h1></div><div class="hero-intro"><p class="hero-tagline">Safety. <br>Judgement. <br>Passenger care.</p><p>A serving guard’s perspective on the work that keeps passengers safe, supported and moving.</p><a class="text-link" href="#case-study">Read the case study <span aria-hidden="true">↘</span></a></div></div>
<figure class="campaign"><div class="photo-window"><img src="assets/cover.png" width="898" height="1122" alt="Railway campaigners holding RMT banners and a banner reading ‘No Driver-Only Operation on East West Rail’." fetchpriority="high"></div><figcaption>From the cover of <cite>More than checking tickets</cite>.</figcaption></figure>
<div class="principles"><a href="#case-study"><span>Everyday safety</span><p>Safe dispatch and<br>hazard awareness</p></a><a href="#emergency"><span>Emergency response</span><p>Calm judgement<br>and coordination</p></a><a href="#access"><span>Accessible travel</span><p>Assistance and<br>reassurance</p></a><a href="#guard-role"><span>Passenger care</span><p>Support through<br>disruption</p></a></div></section>
<section class="reading-section wrap" id="case-study"><aside class="section-label"><span class="chapter-number">01</span><p class="eyebrow">The case study</p><h2>A wider role. <br>A human presence.</h2><p>Understanding the responsibilities and skills behind the uniform.</p><a class="text-link" href="#guard-role">Hear from a guard <span aria-hidden="true">↓</span></a></aside><article class="prose"><p class="lead">'''+e(s[1])+'''</p>'''+case+'''</article></section>
<section class="testimony-section" id="guard-role"><div class="wrap reading-section"><aside class="section-label"><span class="chapter-number">02</span><p class="eyebrow">The testimony</p><h2>The role of <br>a train guard.</h2><p>A practitioner account, credited to Active Train Guard.</p><div class="pull-quote"><span aria-hidden="true">“</span><p>Let the drivers drive and the Guards look after passengers.</p><span class="byline">Active Train Guard</span></div></aside><article class="prose">'''+role+'''</article></div></section>
<section class="experience-section wrap" id="experiences"><div class="experience-intro"><div><span class="chapter-number">03</span><p class="eyebrow">Experiences from the railway</p><h2>In guards’ <br>own words.</h2></div><div><p class="lead">Emergency response. Everyday assistance. Being there when someone needs help.</p><p>Explore the statistics and first-hand accounts in the report, across five themes.</p></div></div><div class="filter-bar" hidden><span class="filter-label" id="filter-label">Explore a theme</span><div class="filters" role="group" aria-labelledby="filter-label">'''+filters+'''</div><p class="filter-status" aria-live="polite" aria-atomic="true">All 5 themes · 41 accounts</p></div>'''+voices+'''</section>
<section class="download-section" id="report"><div class="wrap download-inner"><img src="assets/cover.png" alt="Front cover of the finished report" width="898" height="1122" loading="lazy"><div><p class="eyebrow">The complete collection</p><h2>Take the story<br>with you.</h2><p>Read, keep or share the complete 11-page report, including the case study, practitioner account and all five collections of testimony.</p><a class="button" href="assets/more-than-checking-tickets.pdf" download>Download the report <span aria-hidden="true">↓</span></a><p class="file-detail">PDF · 11 pages</p></div></div></section>
</main><footer class="site-footer wrap"><div><a class="wordmark" href="#top">A guard’s perspective</a><p>Safety. Judgement. Passenger care.</p></div><div><p>Based on an account by a serving, safety-critical trained train guard.<br>Statistics and quotations reproduced from the finished report.</p><a href="#top">Back to top ↑</a></div></footer></body></html>'''
(ROOT/'public/index.html').write_text(html)
print('Built public/index.html with',sum(len(t['quotes']) for t in topics),'quotations.')
