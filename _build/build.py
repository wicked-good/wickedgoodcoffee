import re,io,os
HERE=os.path.dirname(os.path.abspath(__file__))+"/"
R=os.path.dirname(HERE.rstrip("/"))+"/"
SUB="https://wicked-good-coffee.beehiiv.com/subscribe"
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">'
OG="https://wickedgoodcoffee.com/assets/og-image.jpg"
PUBDATE="2026-10-06"
SP=HERE

def head(title,desc,path,extra="",noindex=False,otype="website",ogtitle=None):
    url="https://wickedgoodcoffee.com"+path
    robots='<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{url}">'
    og="" if noindex else f'''<meta property="og:type" content="{otype}"><meta property="og:site_name" content="Wicked Good Coffee"><meta property="og:title" content="{ogtitle or title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="{OG}"><meta name="twitter:card" content="summary_large_image">'''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#2a1811">
{og}
{FONTS}
<link rel="stylesheet" href="/style.css">
{extra}
<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "e5accf0f6e114a0990315dd6923b0c45"}}'></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>'''

def header(cur=""):
    c=lambda k:' aria-current="page"' if cur==k else ''
    return f'''
<header class="site-header on-dark">
  <div class="wrap">
    <a class="brand" href="/"><img src="/assets/cup-96.png" width="34" height="34" alt="">Wicked Good Coffee</a>
    <nav class="site-nav" aria-label="Main">
      <a href="/guides/"{c("guides")}>Guides</a>
      <a href="/roasters/"{c("roasters")}>Roasters</a>
      <a href="/coffee-shops/"{c("shops")}>Coffee shops</a>
      <a href="/contribute/"{c("contribute")}>Contribute</a>
      <a href="/about/"{c("about")}>About</a>
      <a class="btn" href="{SUB}">Get the weekly email</a>
    </nav>
  </div>
</header>
'''
FOOT=f'''
<footer class="site-footer on-dark">
  <div class="wrap">
    <div>
      <p class="motto">Coffee worth talking about.</p>
      <p>Wicked Good Coffee. <a href="/about/">How this site works</a></p>
      <p>Questions or corrections: <a href="mailto:info@wickedgoodcoffee.com">info@wickedgoodcoffee.com</a></p>
    </div>
    <p class="foot-links"><a href="/guides/">Guides</a> <a href="/contribute/">Contribute</a> <a href="/about/">About</a> <a href="{SUB}">Newsletter</a></p>
  </div>
</footer>
</body>
</html>
'''
def signup(h="Get the weekly email.",p="One roaster or café worth knowing, one brewing tip, and what's new in coffee. Free, and you can leave any time."):
    return f'''
<section class="signup on-dark">
  <div class="wrap">
    <h2>{h}</h2>
    <p>{p}</p>
    <div class="btn-row"><a class="btn" href="{SUB}">Subscribe for free</a></div>
  </div>
</section>'''

def w(path,html):
    import os; os.makedirs(os.path.dirname(R+path),exist_ok=True); open(R+path,"w").write(html)

# HOME
ld='<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"Wicked Good Coffee","url":"https://wickedgoodcoffee.com/","description":"Coffee guides: brewing at home, roasters and cafés worth knowing, from New England and beyond."}</script>'
home=head("Wicked Good Coffee: coffee worth talking about","Brewing guides, roasters and cafés worth knowing, from New England and everywhere else. From Glenn.","/",ld)+header()+f'''
<main id="main">
  <section class="hero">
    <div class="wrap">
      <img class="sign" src="/assets/sign-1100.webp" srcset="/assets/sign-600.webp 600w, /assets/sign-1100.webp 1100w" sizes="(max-width: 800px) 92vw, 760px" width="1100" height="813" alt="Wicked Good Coffee: a weathered wooden shop sign with a steaming cup, hanging from an iron bracket">
      <h1>Coffee worth talking about.</h1>
      <p class="lede">Guides to brewing better coffee at home, and to the roasters and cafés worth knowing. The name is pure New England. The coffee is from everywhere.</p>
      <div class="btn-row"><a class="btn" href="{SUB}">Get the weekly email</a><a class="btn quiet" href="/guides/pour-over/">Start with pour-over</a></div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>What you'll find here</h2>
      <ul class="shelf">
        <li><div><h3><a href="/guides/pour-over/">Brew guides</a></h3><p>Making good coffee at home without turning the kitchen into a laboratory. Ratios, grinds, and what to change when a cup tastes off.</p></div><span class="state">Open now</span></li>
        <li><div><h3><a href="/roasters/">Roasters worth knowing</a></h3><p>Who's roasting well, what they're known for, and which bag to try first. We start on home turf in New England, then go wider.</p></div><span class="state">Open now</span></li>
        <li><div><h3><a href="/coffee-shops/">Coffee shops worth the drive</a></h3><p>The places worth getting off the highway for, with the practical details sorted out before you go.</p></div><span class="state">Open now</span></li>
        <li><div><h3><a href="/contribute/">From readers</a></h3><p>Reviews, place tips, brewing tips, and coffee stories from people who care about coffee. Add yours.</p></div><span class="state">Open now</span></li>
      </ul>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>This guide has contributors</h2>
      <p>The best coffee tips come from people who drink a lot of coffee. Review a place you've been, point us to a roaster or café we've missed, or share a brewing tip that works. Contributors get a thank-you by name, or anonymously if you'd rather.</p>
      <div class="btn-row"><a class="btn quiet" href="/contribute/">See how to contribute</a></div>
    </div>
  </section>
</main>
'''+signup()+FOOT
w("index.html",home)

# GUIDES INDEX
gi=head("Guides | Wicked Good Coffee","Brewing guides now, with roaster and café guides on the way, starting in New England.","/guides/")+header("guides")+f'''
<main id="main">
  <section class="article">
    <div class="wrap">
      <header>
        <h1>Guides</h1>
        <p class="deck">Brewing help now. Roaster and café guides are on the way, starting with New England.</p>
      </header>
      <a class="guide-row" href="/guides/pour-over/">
        <p class="meta">Brewing basics, 6 minute read</p>
        <h3>How to make pour-over coffee at home</h3>
        <p>One ratio, one grind, one pour. Everything you need for a clean, sweet cup, plus what to change when it tastes off.</p>
      </a>
      <a class="guide-row" href="/guides/french-press/" style="margin-top:2rem">
        <p class="meta">Brewing basics, 5 minute read</p>
        <h3>How to make french press coffee at home</h3>
        <p>Coarse grind, hot water, four minutes. The whole method, plus how to fix a cup that's muddy, bitter, or weak.</p>
      </a>
      <a class="guide-row" href="/guides/percolator/" style="margin-top:2rem">
        <p class="meta">Brewing basics, 5 minute read</p>
        <h3>How to make stovetop percolator coffee</h3>
        <p>Coarse grind, medium heat, then low. How to get a hot, hearty pot without boiling it into bitterness.</p>
      </a>
      <a class="guide-row" href="/guides/moka-pot/" style="margin-top:2rem">
        <p class="meta">Brewing basics, 5 minute read</p>
        <h3>How to make coffee in a moka pot</h3>
        <p>The Italian stovetop pot. Fill it right, keep the heat at medium, and pull it off at the first gurgle.</p>
      </a>
      <p class="note" style="margin-top:2.5rem">Looking for places instead of methods? See the <a href="/roasters/">roasters</a> and <a href="/coffee-shops/">coffee shops</a>.</p>
    </div>
  </section>
</main>
'''+signup()+FOOT
w("guides/index.html",gi)

# POUR-OVER: reuse the article body from the previous version
old=open(R+"guides/pour-over/index.html").read()
art=re.search(r'<article class="article">.*?</article>',old,re.S).group(0)
art=art.replace("Brewing basics · 6 minute read · October 2026","Brewing basics, 6 minute read, October 2026")
art=art.replace("Write down what you did.","Write down what you did.")
ld2='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"How to make pour-over coffee at home","datePublished":"2026-10-06","dateModified":"2026-10-06","author":{"@type":"Organization","name":"Wicked Good Coffee"},"image":"'+OG+'","publisher":{"@type":"Organization","name":"Wicked Good Coffee","url":"https://wickedgoodcoffee.com/"},"mainEntityOfPage":"https://wickedgoodcoffee.com/guides/pour-over/"}</script>'
po=head("How to make pour-over coffee at home | Wicked Good Coffee","A simple pour-over method: the 1:16 ratio, the right grind and water temperature, step-by-step pouring, and how to fix coffee that tastes sour or bitter.","/guides/pour-over/",ld2,otype="article",ogtitle="How to make pour-over coffee at home")+header("guides")+'\n<main id="main">\n'+art+'\n</main>\n'+signup("Get a roaster worth knowing in your inbox every week.","One roaster or café, one brewing tip, and what's new in coffee. Free.")+FOOT
w("guides/pour-over/index.html",po)

# ABOUT
ab=head("About | Wicked Good Coffee","Wicked Good Coffee is a coffee guide from Glenn: brewing help, roasters and cafes worth knowing, and how the recommendations are made.","/about/")+header("about")+f'''
<main id="main">
  <section class="article">
    <div class="wrap">
      <header>
        <h1>About Wicked Good Coffee</h1>
        <p class="deck">A coffee guide from Glenn, a wicked pissah guy.</p>
      </header>
      <p>"Wicked good" is New England for really, really good. The name comes from home turf, and the first roaster and café guides start there. But coffee is global, so this site won't stay in one corner of the map.</p>
      <p>There's no coffee snobbery required. Just good coffee, and the places and people behind it.</p>

      <h2>What you'll find here</h2>
      <p>Brew guides for making better coffee at home. Profiles of roasters and cafés worth knowing. Reader reviews from people who've been. And a weekly email that pulls it together.</p>

      <h2>Where the content comes from</h2>
      <p>What you read here is a mix of research, personal visits, and reader contributions. Each page says which. Most profiles are researched from published sources, roaster and café websites, and public reviews. Where Glenn has been, or a reader has weighed in, the page says that too.</p>
      <p>When something can't be confirmed, such as hours, a menu, or whether a place is still open, the page says so. Check before you drive an hour. Glenn reviews everything and decides what gets published.</p>
      <p>Nobody here accepts free product in exchange for a good word. If that ever changes, it will be stated plainly on the page it affects.</p>

      <h2>Written with readers</h2>
      <p>This guide gets better when readers add to it. Review a place, recommend one we've missed, or share a brewing tip. <a href="/contribute/">Here's how to contribute</a>. Contributors are thanked by name, or anonymously if they prefer.</p>

      <h2>The email</h2>
      <p>One email a week: a roaster or café worth knowing, a brewing tip, and what's new. It's free. <a href="{SUB}">Subscribe here</a>.</p>

      <h2>Corrections and contact</h2>
      <p>If something here is wrong, or you know a roaster or café that belongs on the site, email <a href='mailto:info@wickedgoodcoffee.com'>info@wickedgoodcoffee.com</a>. Corrections get fixed.</p>
    </div>
  </section>
</main>
'''+signup()+FOOT
w("about/index.html",ab)

# 404
nf=head("Page not found | Wicked Good Coffee","Page not found.","/404.html",noindex=True)+header()+'''
<main id="main">
  <section class="article">
    <div class="wrap">
      <h1>That page isn't here.</h1>
      <p class="deck">The link may be old or mistyped. Try the guides, or head back home.</p>
      <div class="btn-row"><a class="btn" href="/guides/">See the guides</a><a class="btn quiet" href="/">Go home</a></div>
    </div>
  </section>
</main>
'''+FOOT
w("404.html",nf)


# FRENCH PRESS
FP_ART = """<article class="article">
  <div class="wrap">
    <header>
      <p class="meta">Brewing basics, 5 minute read, October 2026</p>
      <h1>How to make french press coffee at home</h1>
      <p class="deck">Coarse grind, hot water, four minutes. Here's the whole method, and what to change when a cup comes out muddy, bitter, or weak.</p>
    </header>

    <p>A french press is the simplest way to brew a full-bodied cup. The grounds steep in hot water, then you push a metal mesh filter down to hold them at the bottom. Because the mesh lets the coffee's natural oils through, the cup tastes heavier and rounder than one made with a paper filter. It's hard to do badly, and a few small habits make it much better.</p>

    <h2>What you need</h2>
    <ul>
      <li>A french press. A standard 34 fluid ounce (1 liter) press fits this recipe with room to spare.</li>
      <li>A kettle. Any kettle works.</li>
      <li>A kitchen scale that reads in grams (most can switch from ounces)</li>
      <li>Whole beans and, ideally, a burr grinder with a coarse setting</li>
      <li>A timer. Your phone is fine.</li>
      <li>A spoon for stirring</li>
    </ul>
    <p>Weighing is still worth it here. Scoops vary a lot with grind size and bean density, and weight is what makes a good cup repeatable. Coffee is weighed in grams because an ounce is about 28 of them, so ounces are too coarse to hold a ratio. Ounce equivalents are in parentheses.</p>

    <div class="recipe">
      <h2>The starting recipe</h2>
      <dl>
        <dt>Coffee</dt><dd>30 g (1.1 oz), about 4&frac12; level tablespoons of whole beans</dd>
        <dt>Water</dt><dd>450 g, about 15 fluid ounces (the ratio is 1 part coffee to 15 parts water)</dd>
        <dt>Water temperature</dt><dd>195&ndash;205&deg;F. Boil the kettle, then wait about 30 seconds.</dd>
        <dt>Grind</dt><dd>Coarse, like coarse sea salt or breadcrumbs</dd>
        <dt>Steep time</dt><dd>4 minutes</dd>
        <dt>Makes</dt><dd>About 13 ounces of coffee, since the grounds soak up some water. That's one big mug and a bit, or two small cups.</dd>
      </dl>
    </div>

    <h2>Step by step</h2>
    <ol>
      <li><strong>Warm the press.</strong> Rinse the empty carafe with hot water and pour it out. A cold glass pulls the heat out of your brew.</li>
      <li><strong>Add the coffee.</strong> Put the ground coffee in the carafe, set it on the scale, and zero the scale.</li>
      <li><strong>Pour and start the timer.</strong> Pour in all 450 g (15 oz) of water, making sure every bit of coffee is wet. Set the lid on top with the plunger still up, which holds in the heat.</li>
      <li><strong>Steep for 4 minutes.</strong> Leave it alone. A crust of grounds will float on top.</li>
      <li><strong>Stir and press.</strong> At 4:00, give the crust a gentle stir, then press the plunger down slowly over about 20 to 30 seconds. Use steady pressure and don't force it.</li>
      <li><strong>Pour it all out right away.</strong> Coffee left sitting on the grounds keeps extracting and turns bitter. If you're not drinking it all, pour the rest into a mug, carafe, or thermos.</li>
    </ol>

    <h2>If it doesn't taste right</h2>
    <p>Change only one thing at a time, so you know what made the difference.</p>
    <ul>
      <li><strong>Muddy or gritty:</strong> the grind is too fine, or your grinder makes a lot of dust. Grind coarser, let the cup sit for a minute before drinking, and leave the last sip behind.</li>
      <li><strong>Bitter, harsh, or dry:</strong> the coffee is over-extracted. Grind coarser, shorten the steep to 3&frac12; minutes, or pour it out sooner after pressing.</li>
      <li><strong>Sour, thin, or salty:</strong> the coffee is under-extracted. Grind a little finer, use slightly hotter water, or steep for 4&frac12; minutes.</li>
      <li><strong>Weak but not sour:</strong> use more coffee. Try 35 g (1.2 oz) with the same 450 g of water.</li>
      <li><strong>Hard to press down:</strong> the grind is too fine or there's too much coffee. Grind coarser, and don't push harder to make up for it.</li>
    </ul>

    <h2>Tips that make a bigger difference than gear</h2>
    <ul>
      <li><strong>Grind right before you brew.</strong> Ground coffee goes stale within minutes, not days. A burr grinder makes even pieces, while a blade grinder makes a mix of boulders and dust, and the dust ends up in your cup.</li>
      <li><strong>Buy fresh beans.</strong> Beans taste best in the first few weeks after roasting. Look for a roast date on the bag, not just a best-by date.</li>
      <li><strong>Don't rinse grounds down the sink.</strong> They clog drains. Scrape them into the trash or compost, then rinse the carafe.</li>
    </ul>

    <p class="note">This guide describes a widely used starting method, not a single correct way. Some brewers steep longer and skim the foam off the top before pressing, and others use a slightly different ratio. Beans, grinders, and water all vary, so treat the numbers as a starting point and adjust to your taste.</p>
  </div>
</article>"""
fld='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"How to make french press coffee at home","datePublished":"2026-10-06","dateModified":"2026-10-06","author":{"@type":"Organization","name":"Wicked Good Coffee"},"image":"'+OG+'","publisher":{"@type":"Organization","name":"Wicked Good Coffee","url":"https://wickedgoodcoffee.com/"},"mainEntityOfPage":"https://wickedgoodcoffee.com/guides/french-press/"}</script>'
fp=head("How to make french press coffee at home | Wicked Good Coffee","A simple french press method: the 1:15 ratio, a coarse grind, 4 minute steep, how to press, and how to fix coffee that tastes muddy, bitter or weak.","/guides/french-press/",fld,otype="article",ogtitle="How to make french press coffee at home")+header("guides")+'\n<main id="main">\n'+FP_ART+'\n</main>\n'+signup("Get a roaster worth knowing in your inbox every week.","One roaster or café, one brewing tip, and what's new in coffee. Free.")+FOOT
w("guides/french-press/index.html",fp)


def guide(slug,title,desc,deck,body,ogdesc=None):
    ld='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"'+title+'","datePublished":"'+PUBDATE+'","dateModified":"'+PUBDATE+'","author":{"@type":"Organization","name":"Wicked Good Coffee"},"image":"'+OG+'","publisher":{"@type":"Organization","name":"Wicked Good Coffee","url":"https://wickedgoodcoffee.com/"},"mainEntityOfPage":"https://wickedgoodcoffee.com/guides/'+slug+'/"}</script>'
    art=f'''<article class="article">
  <div class="wrap">
    <header>
      <p class="meta">Brewing basics, 5 minute read, October 2026</p>
      <h1>{title}</h1>
      <p class="deck">{deck}</p>
    </header>
{body}
  </div>
</article>'''
    html=head(title+" | Wicked Good Coffee",desc,"/guides/"+slug+"/",ld,otype="article",ogtitle=title)+header("guides")+'\n<main id="main">\n'+art+'\n</main>\n'+signup("Get a roaster worth knowing in your inbox every week.","One roaster or café, one brewing tip, and what's new in coffee. Free.")+FOOT
    w("guides/"+slug+"/index.html",html)

PERC = """
    <p>A percolator is the classic camp-and-kitchen coffee pot. Water in the bottom heats up and is pushed up a thin tube, then rains down over the grounds in a basket at the top, again and again, until you take it off the heat. It makes a hot, strong, hearty pot, and it's easy to overdo. The whole trick is keeping it at a gentle bubble instead of a boil.</p>

    <h2>What you need</h2>
    <ul>
      <li>A stovetop percolator, with its stem and basket</li>
      <li>Whole beans and a grinder with a coarse setting. Fine grounds slip through the basket holes and make the pot muddy and bitter.</li>
      <li>A tablespoon, or a scale that reads in grams (most can switch from ounces)</li>
      <li>A timer. Your phone is fine.</li>
    </ul>

    <div class="recipe">
      <h2>The starting recipe</h2>
      <dl>
        <dt>Coffee</dt><dd>1 to 2 heaping tablespoons per 8 fluid ounces of water. Start at 1&frac12; (about 10 g, 0.35 oz).</dd>
        <dt>Water</dt><dd>8 fluid ounces is about 240 g. Fill only to below the bottom of the basket and the spout.</dd>
        <dt>Grind</dt><dd>Coarse, like sea salt or coarse breadcrumbs</dd>
        <dt>Heat</dt><dd>Start at medium. Turn it to low as soon as the pot starts perking.</dd>
        <dt>Perk time</dt><dd>4 to 8 minutes once it starts perking. Start checking at 4.</dd>
        <dt>Example</dt><dd>For 32 fluid ounces (about 950 g) of water, use 6 heaping tablespoons of coffee, roughly 40 g (1.4 oz).</dd>
      </dl>
    </div>

    <h2>Step by step</h2>
    <ol>
      <li><strong>Add the water.</strong> Fill the pot with cold water, keeping the level below the bottom of the basket and the spout. If the water touches the grounds before it heats, the coffee tastes flat.</li>
      <li><strong>Fill the basket.</strong> Put the stem in the pot, add the coarse coffee to the basket, and put the basket lid on. Wipe any stray grounds off the stem so they don't clog it.</li>
      <li><strong>Heat to medium.</strong> Put the lid on the pot and set it on a burner over medium heat.</li>
      <li><strong>Turn it down when it perks.</strong> The glass knob on the lid shows the coffee bubbling up. As soon as it starts, drop the heat to low. You want a lazy, steady perk, not a rolling boil.</li>
      <li><strong>Start the timer.</strong> Perk for 4 to 8 minutes. About 4 makes a lighter pot, 5 or 6 is a good middle, and 7 or 8 is strong. Check the color through the glass knob.</li>
      <li><strong>Take it off the heat and pull the stem.</strong> Lift out the whole stem and basket, not just the basket. Left in place, steam condenses and drips back through spent grounds, and the pot goes sour and bitter within minutes. Let the coffee settle for about 30 seconds, then pour.</li>
    </ol>

    <h2>If it doesn't taste right</h2>
    <p>Change only one thing at a time, so you know what made the difference.</p>
    <ul>
      <li><strong>Bitter, harsh, or burnt:</strong> the heat was too high or it perked too long. Turn the heat down sooner, shorten the time, and pull the stem right away.</li>
      <li><strong>Muddy or gritty:</strong> the grind is too fine. Grind coarser, and let the pot rest for 30 seconds before you pour.</li>
      <li><strong>Weak or thin:</strong> use more coffee, up to 2 heaping tablespoons per 8 fluid ounces, or perk a minute or two longer.</li>
      <li><strong>It spits or boils over:</strong> the heat is too high, or the water level is too high. Turn it down and check the fill line.</li>
      <li><strong>It won't perk:</strong> the heat is too low, or the tube is clogged with grounds. Raise the heat a notch and check that the stem is clean.</li>
    </ul>

    <h2>Tips that make a bigger difference than gear</h2>
    <ul>
      <li><strong>Grind right before you brew.</strong> Ground coffee goes stale within minutes, not days.</li>
      <li><strong>Buy fresh beans.</strong> Beans taste best in the first few weeks after roasting. Look for a roast date on the bag.</li>
      <li><strong>Keep the pot clean.</strong> Old coffee oils turn rancid and flavor every pot after. Wash the stem, basket, and pot after each use and scrub the tube if you can.</li>
      <li><strong>Try a paper disk.</strong> If your grounds keep getting through, a paper filter disk cut to fit the basket catches the fines.</li>
    </ul>

    <p class="note">This guide describes a widely used starting method, not a single correct way. Pots, burners, and beans all vary, so treat the numbers as a starting point and adjust to your taste. Based on published percolator guides, including <a href="https://coletticoffee.com/blogs/camping-coffee-tips/how-to-make-percolator-coffee">Colletti Coffee</a> and <a href="https://www.talkaboutcoffee.com/how-to-make-coffee-in-a-percolator.html">Talk About Coffee</a>.</p>
"""
guide("percolator","How to make stovetop percolator coffee","A simple stovetop percolator method: coarse grind, medium heat then low, a 4 to 8 minute perk, and how to fix coffee that tastes bitter, weak or muddy.","Coarse grind, medium heat, then low. Here's how to get a hot, hearty pot without boiling it into bitterness.",PERC)

MOKA = """
    <p>A moka pot is the small aluminum or steel pot with an octagon shape that sits on every Italian stove. Water heats in the bottom, steam pressure pushes it up through a basket of coffee, and finished coffee collects in the top. It makes a strong, concentrated cup. It isn't true espresso, because the pressure is much lower than an espresso machine's, but it's a great way to get close at home for the price of a pot.</p>

    <h2>What you need</h2>
    <ul>
      <li>A moka pot. The size is measured in "cups," and a moka cup is a small espresso-sized pour of roughly 2 fluid ounces. Fill the pot all the way each time, so buy the size you'll actually use.</li>
      <li>Whole beans and, ideally, a burr grinder</li>
      <li>A kettle is optional. Some people start with hot water, and the steps below say when.</li>
      <li>A stove. Gas, electric, and most induction burners work, though induction needs a steel pot.</li>
    </ul>

    <div class="recipe">
      <h2>The starting recipe</h2>
      <dl>
        <dt>Coffee</dt><dd>Fill the basket level to the top. Don't tamp or press it down.</dd>
        <dt>Water</dt><dd>Fill the bottom chamber to just below the safety valve on the side, and no higher</dd>
        <dt>Grind</dt><dd>Fine, about like table salt. That's finer than drip and coarser than espresso.</dd>
        <dt>Heat</dt><dd>Medium</dd>
        <dt>Time</dt><dd>Around 5 minutes on the stove. You'll hear when it's done.</dd>
        <dt>Makes</dt><dd>A small, strong pour. Sip it as is, or add hot water or milk.</dd>
      </dl>
    </div>

    <h2>Step by step</h2>
    <ol>
      <li><strong>Fill the bottom chamber.</strong> Pour water in up to the safety valve, but not over it. Cold water is the usual choice. Hot water gets the coffee done faster and keeps the grounds from sitting on a heating pot as long, but use a towel to hold the pot.</li>
      <li><strong>Fill the basket.</strong> Spoon in the ground coffee and level it off with your finger. Wipe any grounds off the rim so the pot seals.</li>
      <li><strong>Screw it together.</strong> Put the basket in, then screw the top on snugly. Use a towel if the bottom is hot. The seal matters, because a loose pot leaks steam and struggles to build pressure.</li>
      <li><strong>Heat on medium.</strong> Set the pot on a burner that fits under it, with the handle turned away from the flame. High heat feels faster but scorches the coffee before it finishes. Leave the lid open if you want to watch.</li>
      <li><strong>Listen for the gurgle.</strong> Coffee will rise into the top, first as a dark, steady stream and then paler and spluttering, with a hissing, gurgling sound. Take the pot off the heat as soon as you hear it.</li>
      <li><strong>Stop it and serve.</strong> Set the base on a cool, damp towel or run it briefly under cold water, so the last of the water doesn't keep pushing through and turn the coffee bitter. Give the coffee a quick stir and pour.</li>
    </ol>

    <h2>If it doesn't taste right</h2>
    <p>Change only one thing at a time, so you know what made the difference.</p>
    <ul>
      <li><strong>Bitter, burnt, or metallic:</strong> the heat was too high, or the pot stayed on the burner after the gurgle. Lower the heat and pull it off sooner.</li>
      <li><strong>Sour or thin:</strong> the grind may be too coarse. Grind a little finer.</li>
      <li><strong>It won't build pressure or leaks:</strong> a loose top, a worn or misaligned rubber gasket, or coffee packed too tightly. Check the seal first, keep the coffee level instead of compressed, and replace the gasket if it's cracked.</li>
      <li><strong>Sputters or spits right away:</strong> the heat is too high. Turn it down.</li>
    </ul>

    <h2>Tips that make a bigger difference than gear</h2>
    <ul>
      <li><strong>Never run it empty.</strong> Always fill the bottom chamber to the valve line, and don't heat the pot without water.</li>
      <li><strong>Grind right before you brew.</strong> Ground coffee goes stale within minutes, not days.</li>
      <li><strong>Hand-wash it.</strong> Aluminum pots darken in the dishwasher. Rinse with warm water, skip the soap if you can, and dry it fully.</li>
      <li><strong>Buy fresh beans.</strong> Look for a roast date on the bag, not just a best-by date.</li>
    </ul>

    <p class="note">This guide describes a widely used starting method, not a single correct way. Pot sizes, burners, and beans all vary, so treat the steps as a starting point and adjust to your taste. Based on published moka pot guides, including <a href="https://dipacci.com.au/blogs/news/how-to-use-a-moka-pot-a-step-by-step-guide">Dipacci</a>.</p>
"""
guide("moka-pot","How to make coffee in a moka pot","A simple moka pot method: fine grind, level basket, water to the valve, medium heat, and when to pull it off. Plus fixes for bitter or weak coffee.","The Italian stovetop pot. Fill it right, keep the heat at medium, and pull it off at the first gurgle.",MOKA)


def place(section,slug,title,desc,deck,body,kicker,cur):
    path=f"/{section}/{slug}/"
    ld='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"'+title+'","datePublished":"'+PUBDATE+'","dateModified":"'+PUBDATE+'","author":{"@type":"Organization","name":"Wicked Good Coffee"},"image":"'+OG+'","publisher":{"@type":"Organization","name":"Wicked Good Coffee","url":"https://wickedgoodcoffee.com/"},"mainEntityOfPage":"https://wickedgoodcoffee.com'+path+'"}</script>'
    art=f'''<article class="article">
  <div class="wrap">
    <header>
      <p class="meta">{kicker}</p>
      <h1>{title}</h1>
      <p class="deck">{deck}</p>
    </header>
{body}
    <p>Been here? <a href="/reviews/">Send us a reader review</a>.</p>
  </div>
</article>'''
    html=head(title+" | Wicked Good Coffee",desc,path,ld,otype="article",ogtitle=title)+header(cur)+'\n<main id="main">\n'+art+'\n</main>\n'+signup("Get a roaster worth knowing in your inbox every week.","One roaster or café, one brewing tip, and what's new in coffee. Free.")+FOOT
    w(f"{section}/{slug}/index.html",html)

def index_page(section,cur,title,desc,deck,rows,note):
    items="".join(f'''
      <a class="guide-row" href="/{section}/{slug}/" style="margin-top:2rem">
        <p class="meta">{meta}</p>
        <h3>{t}</h3>
        <p>{blurb}</p>
      </a>''' for slug,meta,t,blurb in rows)
    html=head(title+" | Wicked Good Coffee",desc,f"/{section}/")+header(cur)+f'''
<main id="main">
  <section class="article">
    <div class="wrap">
      <header>
        <h1>{title}</h1>
        <p class="deck">{deck}</p>
      </header>{items}
      <p class="note" style="margin-top:2.5rem">{note}</p>
    </div>
  </section>
</main>
'''+signup()+FOOT
    w(f"{section}/index.html",html)

SA = """
    <p>Most coffee is roasted over gas. Speckled Ax roasts with wood, and that's the reason to know the name. It's one of a handful of wood-fired coffee roasters in the United States, and it's based in Portland, Maine.</p>

    <div class="recipe">
      <h2>The short version</h2>
      <dl>
        <dt>Where</dt><dd>Portland, Maine</dd>
        <dt>Started</dt><dd>2007, in Waterville, Maine, as Matt's Wood Roasted Organic Coffee</dd>
        <dt>Renamed</dt><dd>Speckled Ax, in 2012</dd>
        <dt>Roaster</dt><dd>A refurbished 1970s Italian Petroncini, fired with kiln-dried Maine wood</dd>
        <dt>Buy it</dt><dd>Online (blends, single-origin coffees, and monthly subscriptions) or at its Portland cafe</dd>
      </dl>
    </div>

    <h2>How the coffee is roasted</h2>
    <p>The wood is kiln-dried Maine red oak, maple, and ash. The owner's favorite is ash, because it burns the fastest. Wood fire needs more hands-on control than gas does. The hard part is managing the heat between first crack and the end of the roast, according to a 2022 visit by Brian's Coffee Spot, which called the coffee excellent.</p>

    <h2>Where to find it</h2>
    <p>That 2022 write-up lists three Portland spots: the original on Congress Street (opened 2012), a flagship on Thames Street (opened 2020), and a roastery with a coffee bar on Walton Street (opened 2021). The company's own website currently lists a single address, 567 Congress St, Portland, ME 04101, phone 207-660-3333. It doesn't post hours there, so check before you go.</p>

    <h2>Where to start</h2>
    <p>Speckled Ax sorts its coffee on its website into blends, single-origin coffees, and gear. A blend is the easy way into any new roaster, and a monthly subscription is there if you like it. The site also displays Good Food Awards recognition.</p>

    <p class="note">This profile is researched from published sources, not from a visit. Locations and hours change, so check before you go. Sources: <a href="https://www.speckledax.com">Speckled Ax</a> and <a href="https://www.brian-coffee-spot.com/2022/02/24/meet-the-roaster-speckled-ax/">Brian's Coffee Spot</a>.</p>
"""
place("roasters","speckled-ax","Speckled Ax, the wood-fired roaster in Portland, Maine","Speckled Ax roasts coffee with wood in Portland, Maine. How it's roasted, where to find it, and where to start.","A Portland, Maine roaster that fires its roaster with wood instead of gas.",SA,"Roaster profile, Maine, October 2026","roasters")
EXTRA_R=[];EXTRA_S=[];EXTRA_G=[]
exec(open(SP+"content2.py").read())
index_page("roasters","roasters","Roasters","Roasters worth knowing, starting with New England. Each profile says what it's based on.","Who's roasting well and what they're known for. We start in New England and go wider.",[("speckled-ax","Maine, wood-fired","Speckled Ax","One of a handful of wood-fired coffee roasters in the United States, in Portland, Maine.")]+[(sl,m,t,b) for sl,m,t,b in EXTRA_R],"More roasters are coming. Know one that belongs here? Email <a href='mailto:info@wickedgoodcoffee.com'>info@wickedgoodcoffee.com</a>, or see <a href='/contribute/'>how to contribute</a>.")

TANDEM = """
    <p>Tandem is a Portland, Maine roaster with two cafes. One is the roastery itself on Anderson Street. The other, on Congress Street, pairs the coffee with a bakery.</p>

    <div class="recipe">
      <h2>The short version</h2>
      <dl>
        <dt>Started</dt><dd>2012, by Will and Kathleen Pratt</dd>
        <dt>Cafe + Roastery</dt><dd>122 Anderson St, East Bayside. Monday to Saturday, 7am to 1pm.</dd>
        <dt>Coffee + Bakery</dt><dd>742 Congress St, West End (opened 2014). Every day, 8am to 1pm, with an online ordering window from 7:45 to 10:15am.</dd>
        <dt>Phone</dt><dd>(207) 760-4440</dd>
        <dt>Hours</dt><dd>As posted on Tandem's website in October 2026</dd>
      </dl>
    </div>

    <h2>The cafe and roastery on Anderson Street</h2>
    <p>The building is a 1930s L-shaped brick structure that holds both a cafe and a separate roastery. The cafe closed during COVID, was remodeled, and reopened in May 2022. A 2023 visit by Brian's Coffee Spot describes two rooms, window bars along the walls, counter seating, tables, benches, and outdoor seating. Parking is free on site or on the street.</p>
    <p>That write-up lists a single-origin espresso every day, a decaf, batch brew, and pour-overs, usually from a choice of two or three single-origins. The menu changes, so check what's on when you go.</p>

    <h2>The coffee and bakery on Congress Street</h2>
    <p>Baking is led by Briana Holt, who trained at M. Wells and Pies and Thighs in New York and is named on Tandem's site as a James Beard nominee. Online ordering for same-day pickup is open for a short window each morning.</p>

    <h2>Buying beans</h2>
    <p>Tandem sells a rotating list of single-origin coffees and seasonal blends online. Its site lists free shipping on most orders over $50.</p>

    <p class="note">This profile is researched from published sources, not from a visit. Hours and menus change, so check before you go. Sources: <a href="https://www.tandemcoffee.com/pages/our-story">Tandem's story</a>, <a href="https://www.tandemcoffee.com">Tandem's website</a>, and <a href="https://www.brian-coffee-spot.com/2023/07/27/tandem-cafe-roastery-update">Brian's Coffee Spot</a>.</p>
"""
place("coffee-shops","tandem","Tandem Coffee in Portland, Maine","Tandem Coffee Roasters has two Portland, Maine cafes, one at the roastery and one with a bakery. Addresses, hours, and what to know.","Two Portland, Maine cafes from the same roasters: one at the roastery, one with a bakery.",TANDEM,"Coffee shop, Portland, Maine, October 2026","shops")

BC = """
    <p>Black Cap is a Vermont cafe and bakery with shops in Stowe, Waterbury, Morrisville, and Burlington. The Stowe shop sits right on Main Street, and the bakery side is a big part of the pitch: the cafe's own site calls it a "Vermont coffee shop with pastries, food and craft beer."</p>

    <div class="recipe">
      <h2>The short version</h2>
      <dl>
        <dt>Stowe</dt><dd>144 Main St, Stowe, VT 05672. (802) 253-2123. Open daily, with hours not listed on its site.</dd>
        <dt>Other shops</dt><dd>Morrisville (53 Lower Main St), Waterbury Train Station (1 Rotarian Pl), and Burlington (42 Church St). Waterbury is listed as open daily, 7am to mid-afternoon.</dd>
        <dt>Owner</dt><dd>Laura Vilalta, who bought the original Stowe shop in December 2012</dd>
        <dt>On the menu</dt><dd>Coffee, tea, a maple latte it calls famous, pastries, breakfast sandwiches, lunch, and Vermont craft beer</dd>
      </dl>
    </div>

    <h2>The food</h2>
    <p>According to Edible Vermont (August 2025), most of the pastries are made at the Waterbury shop in the town's historic train station. The Stowe shop has a large pastry case along with hot and cold sandwiches. Black Cap's site lists made-to-order breakfast sandwiches and a lunch menu with gluten-free, vegetarian, and vegan options. Edible Vermont said the croissants are "as good as any you might have in France."</p>

    <h2>The Stowe shop</h2>
    <p>The Stowe shop was renovated in 2020 and again in 2025. Its site mentions air conditioning and an upgraded porch.</p>

    <h2>The story</h2>
    <p>Vilalta moved to Vermont from Barcelona in 2010 and bought the Stowe shop two years later. She added Morrisville in 2017 and Burlington's Church Street in July 2020. Edible Vermont reported that she grew the business partly to be able to offer her employees health insurance.</p>

    <p class="note">The details here come from published sources, and Glenn has been to the Stowe shop. Neither Black Cap's site nor the articles say who roasts its coffee, so this profile doesn't either. Hours and locations change, so check before you go. Sources: <a href="https://blackcapvermont.com/">Black Cap</a>, <a href="https://ediblevermont.ediblecommunities.com/drink/black-cap-coffee-bakery-of-vermont-burlington-morrisville-stowe-waterbury/">Edible Vermont</a>, and <a href="https://churchstmarketplace.com/blog/inside-black-cap-coffee-and-bakery-of-vermont">Church Street Marketplace</a>.</p>
"""
place("coffee-shops","black-cap","Black Cap Coffee & Bakery in Stowe, Vermont","Black Cap Coffee & Bakery of Vermont has shops in Stowe, Waterbury, Morrisville and Burlington. Addresses, food, and the story.","A Vermont cafe and bakery on Main Street in Stowe, with three more shops around the state.",BC,"Coffee shop, Stowe, Vermont, October 2026","shops")
index_page("coffee-shops","shops","Coffee shops","Coffee shops worth the drive, starting in New England. Each profile says what it's based on.","Places worth getting off the highway for, with the practical details sorted out before you go.",[("black-cap","Stowe, Vermont","Black Cap Coffee & Bakery","A cafe and bakery on Main Street in Stowe, with three more shops across Vermont."),("tandem","Portland, Maine","Tandem Coffee","Two Portland cafes from the same roasters: one at the roastery, one with a bakery.")]+[(sl,m,t,bl) for sl,m,t,bl in EXTRA_S],"More shops are coming. Know a place that belongs here? Email <a href='mailto:info@wickedgoodcoffee.com'>info@wickedgoodcoffee.com</a>.")


MAIL="info@wickedgoodcoffee.com"
SUBJ="Reader review: "
BODYT="Place (name and town):\n\nWhen you went:\n\nWhat you ordered or bought:\n\nWhat you liked, or didn't:\n\nWould you go back?\n\nName to show (first name and town, or anonymous):\n\nI visited this place myself, I wasn't paid or given anything for this review, and you can publish it."
import urllib.parse
href="mailto:"+MAIL+"?subject="+urllib.parse.quote(SUBJ)+"&body="+urllib.parse.quote(BODYT)
REV = """
    <p>Been to a roaster or café we cover, or got a favorite we haven't found yet? Tell us about it. Honest reviews from real visits are welcome, good and bad.</p>
    <div class="btn-row"><a class="btn" href='""" + href + """'>Email your review</a></div>
    <p>If the button doesn't open your email, send it to <strong>info@wickedgoodcoffee.com</strong>. It's free to send, and free to be published.</p>

    <h2>How it works</h2>
    <ol>
      <li><strong>Write a short review.</strong> What you ordered or bought, what you liked or didn't, and whether you'd go back. A few sentences is plenty.</li>
      <li><strong>Email it to us.</strong> Use the button above, or copy the template below.</li>
      <li><strong>We read every one.</strong> If it's honest and follows the rules below, we publish it on this page and may share it in the newsletter. We'll email you if we have a question.</li>
    </ol>

    <h2>The template</h2>
    <pre class="template">Place (name and town):

When you went:

What you ordered or bought:

What you liked, or didn't:

Would you go back?

Name to show (first name and town, or anonymous):

I visited this place myself, I wasn't paid or given anything for this review, and you can publish it.</pre>

    <h2>The rules</h2>
    <ul>
      <li><strong>It's free.</strong> There's no cost to send a review and no payment for publishing one. We don't pay for reviews, and we don't trade free coffee for them.</li>
      <li><strong>Real visits only.</strong> Write about coffee you actually bought or drank. If you own, work for, or compete with the place, say so, or don't review it.</li>
      <li><strong>Good or bad.</strong> We publish critical reviews alongside the glowing ones, as long as they're honest and fair.</li>
      <li><strong>What we won't publish.</strong> Personal attacks, hate, accusations we can't stand behind, spam, and anything that reads like an ad.</li>
      <li><strong>Light edits only.</strong> We may fix typos or trim for length. We won't change what you said.</li>
      <li><strong>Your details.</strong> We show the name and town you give us, or "anonymous." We never publish your email address.</li>
      <li><strong>Your permission.</strong> By sending a review, you let us publish it on this site and in the newsletter.</li>
    </ul>

    <h2>Reviews from readers</h2>
    <p class="note">No reader reviews yet. Yours could be the first.</p>
    <p>Reader reviews are one person's opinion, published as sent. We don't verify visits, so they're labeled as reader reviews and kept separate from our own researched profiles.</p>
"""
html=head("Reader reviews | Wicked Good Coffee","Send a short, honest review of a coffee roaster or cafe. It's free to send and free to be published. Here's how it works and the rules.","/reviews/")+header("contribute")+'\n<main id="main">\n<article class="article">\n  <div class="wrap">\n    <header>\n      <h1>Reader reviews</h1>\n      <p class="deck">Your turn. Tell us about a roaster or cafe worth knowing.</p>\n    </header>\n'+REV+'  </div>\n</article>\n</main>\n'+signup()+FOOT
w("reviews/index.html",html)


import urllib.parse as _u
def _mailto(subj,body):
    return "mailto:info@wickedgoodcoffee.com?subject="+_u.quote(subj)+"&body="+_u.quote(body)
TIP_PLACE=_mailto("Place tip: ","Name of the roaster or cafe:\n\nTown and state (or country):\n\nWebsite, if you know it:\n\nWhy it's worth a stop:\n\nName to credit (first name and town, or anonymous):\n\nYou can use this tip, and I'm not connected to this business (or I've said how I am).")
TIP_BREW=_mailto("Brewing tip: ","What method or tool is this for?\n\nYour tip, ratio, or fix:\n\nWhat problem does it solve?\n\nName to credit (first name and town, or anonymous):\n\nYou can use this tip.")
TIP_STORY=_mailto("Coffee story: ","Your story (a few short paragraphs is plenty):\n\nPlace or person it's about, if any:\n\nName to show (first name and town, or anonymous):\n\nThis is a true story, and you can publish it.")
CONTRIB = """
    <p>The best coffee advice comes from people who drink a lot of coffee. This guide gets better with every reader who adds to it. Pick a way to pitch in.</p>

    <h2>Review a place</h2>
    <p>Been to a roaster or café we cover, or one we haven't found yet? Send a short, honest review. Good or critical, as long as it's fair and from a real visit.</p>
    <div class="btn-row"><a class="btn" href="/reviews/">Write a review</a></div>

    <h2>Recommend a place</h2>
    <p>Know a roaster or café we should cover? Tell us its name, its town, and why it's worth a stop. We'll research it, and if it fits, write it up and thank you for the tip.</p>
    <div class="btn-row"><a class="btn" href='""" + TIP_PLACE + """'>Recommend a place</a></div>

    <h2>Share a brewing tip</h2>
    <p>Got a ratio, a method, or a fix for a bad cup? Send it. We check tips against other sources before they go into a guide, and we credit you when one does.</p>
    <div class="btn-row"><a class="btn" href='""" + TIP_BREW + """'>Share a tip</a></div>

    <h2>Tell a coffee story</h2>
    <p>A diner you almost drove past, a roaster that changed how you drink coffee, a morning you remember. Short and true.</p>
    <div class="btn-row"><a class="btn" href='""" + TIP_STORY + """'>Tell a story</a></div>

    <p>If a button doesn't open your email, send it to <strong>info@wickedgoodcoffee.com</strong> and tell us which kind of contribution it is.</p>

    <h2>Ground rules</h2>
    <ul>
      <li><strong>It's free.</strong> There's no cost to contribute and no payment for publishing. We don't pay for reviews or tips, and we don't trade free coffee for them.</li>
      <li><strong>Keep it real.</strong> Write about things you actually know or did. If you own, work for, or compete with a place, say so.</li>
      <li><strong>Credit is yours to choose.</strong> We thank you by the first name and town you give us, or anonymously. We never publish your email address.</li>
      <li><strong>We check before we publish.</strong> Place tips and brewing tips get verified against other sources. We may edit for length and clarity, and we won't change what you meant.</li>
      <li><strong>We can't publish everything.</strong> Personal attacks, accusations we can't support, spam, and ads are out.</li>
      <li><strong>Your permission.</strong> By sending something, you let us publish it on this site and in the newsletter.</li>
    </ul>

    <h2>Contributors</h2>
    <p class="note">No contributors listed yet. Yours could be the first name here.</p>
"""
html=head("Contribute | Wicked Good Coffee","Review a place, recommend a roaster or cafe, share a brewing tip, or tell a coffee story. It's free, and contributors are thanked by name.","/contribute/")+header("contribute")+'\n<main id="main">\n<article class="article">\n  <div class="wrap">\n    <header>\n      <h1>Contribute</h1>\n      <p class="deck">This guide has contributors. Here are four ways to be one.</p>\n    </header>\n'+CONTRIB+'  </div>\n</article>\n</main>\n'+signup()+FOOT
w("contribute/index.html",html)
