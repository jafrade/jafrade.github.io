---
# Field prefixes say where each field appears (same convention as the case studies):
#   (no prefix) = shared with other pages (nav, meta)
#   page_       = About page only
#   filter_     = not displayed

title: "About"
slug: about
meta_description: "Jason Frade is a senior product designer who makes complicated software simple for the people who use it."

page_photo: images/about/headshot.jpg
page_photo_alt: "Jason Frade"

page_experience:
  - { company: "HubSpot", role: "Senior Product Designer", dates: "2022 – 2026", note: "Automation and AI agents" }
  - { company: "HubSpot", role: "Product Designer", dates: "2017 – 2022", note: "Advertising" }
  - { company: "Kyruus", role: "Lead Product Designer, Product Designer", dates: "2015 – 2017", note: "Healthcare provider matching" }
  - { company: "Hewlett Packard", role: "UX/UI Designer", dates: "2014 – 2015", note: "Cloud automation software" }
  - { company: "XPO Logistics", role: "UX Engineer", dates: "2013 – 2014", note: "Internal logistics tools" }

page_testimonial:
  quote: "TBD"
  name: "TBD"
  role: "TBD"

page_contact:
  heading: "Let's work together"
  email: "TBD"
  linkedin: "TBD"
  resume: files/jason-frade-resume.pdf
---

<!--
  OPEN ITEMS
  - Photos: confirm the England caption and that the travel photo is Copenhagen. Swap in original photos if available (current ones are screenshots, about 1,250 px wide)
  - Woodworking photo: the TV screen reflects Jason and part of a TV box shows on the left; fine as is, or retake if there's a cleaner shot
  - Experience dates: fill in HP and XPO dates so they match the resume and LinkedIn
  - XPO title: the resume says UX Engineer; keep it here only if the resume keeps it
  - Testimonial: optional. Use a real quote from a peer or manager review, with their OK. Delete page_testimonial if there isn't one
  - Contact: add email and LinkedIn URL; add the resume PDF under files/

  NOTES FOR THE SITE BUILD
  - Layout order: intro with headshot, values, experience timeline, testimonial (if any), outside of work, contact
  - Values: render each value as a card with the bold label as its heading. Grid of 2 or 3 columns on desktop, 1 column on mobile
  - Experience: a compact list from page_experience, one row per role, not full job descriptions
  - Headshot: images/about/headshot.jpg, shown beside the intro
  - Outside of work: images between the 'photo-grid' and '/photo-grid' comment markers are one grid; each alt text is that photo's caption. Lay them out as a mosaic like Simon Pan's, not a uniform grid:
    Desktop: 5 columns × 3 rows of square cells, small gap, no rounded corners. Spans (column, row, width × height):
      England 1,1 2×2 · woodworking 3,1 1×2 · sourdough 4,1 1×1 · van 5,1 1×2 · cooking 4,2 1×1 · Copenhagen 1,3 2×1 · cats 3,3 1×1 · Epcot 4,3 2×1
    Mobile: 2 columns; England and Copenhagen span both columns, everything else 1×1
    Use object-fit: cover on the uncropped photos in images/about/originals so each fills its cell
  - Photo files, so layouts can be compared:
    images/about/originals: every photo uncropped (same names as below), plus alt-apron, alt-autumn, alt-donuts and alt-park as other headshot or grid options
    images/about: the same photos pre-cropped to 960 × 1,200 (4:5), for a uniform grid or a scrolling strip
    about-photos-preview.jpg shows the 4:5 crops side by side
    Captions: a small label on each photo (bottom left, light text on a soft dark gradient), always visible since hover doesn't work on phones
    See mosaic-preview.jpg for the intended layout
  - No skill or tool lists on this page; the resume carries those
-->

## Intro {#intro}

I'm Jason, a senior product designer with more than a decade of experience. I believe software should help people get their work done, however complicated the problem underneath and however technical they are.

That belief has taken me through a lot of industries. At HubSpot, I designed automation and AI agents that take repetitive work off small business teams, and before that spent five years on advertising tools for marketers. At Kyruus, I improved how patients get matched with the right doctor, on consumer websites and through call centers. At HP I worked on cloud automation software, and at XPO I designed internal tools for a logistics company.

Every new industry meant learning how someone else's work actually happens, and the fastest way I've found to do that is to talk to the people doing it.

## What I believe in {#values}

### Make the complicated feel simple

I believe the best answer is usually the simplest one that works well, so I keep asking what we can take away until only what people need is left. A marketer shouldn't have to think like an engineer to set up a workflow, and a shop owner shouldn't need a manual to use the software that runs their business.

### Care about the craft

I care about how a product looks and feels as much as how it works. I spend real time on visual and interaction details, and on the parts that are easy to skip, like what a screen looks like before there's any data and what happens when something goes wrong. Those moments can decide whether someone trusts the product.

### Let customers lead the way

I lean on customers to help guide where a design goes, so I talk to them throughout a project, from early interviews, card sorts and tree tests to concept and usability tests. After launch, I watch the data to see whether we got it right.

### Build to learn

I use AI tools like Claude and Lovable to turn early ideas into working prototypes. They give me something real to work through with customers, and help me answer technical questions with engineers sooner. The tools help me move faster, and my own design judgment still decides what we ship.

### Design for the teams who build on it

Some of my favorite work has been designing patterns other teams can build on, and working with those teams to keep the experience consistent wherever it shows up.

### Help each other get better

I make a point of giving thoughtful, specific feedback to every designer I work with in team critiques, and I welcome the same in return.

## Outside of work {#outside}

When I'm not designing, I'm usually making something, whether that's sourdough, a vegan dinner or a piece of furniture. I also converted a van into a camper. I used to live in England, I travel whenever I can, and I share my home with two cats and far too many Blu-rays.

<!-- photo-grid -->
![Sourdough, cut open to check the crumb](images/about/sourdough.jpg)
![Plating a vegan dinner](images/about/cooking.jpg)
![An entertainment center I built](images/about/woodworking.jpg)
![The van I converted into a camper](images/about/van.jpg)
![My two cats](images/about/cats.jpg)
![When I lived in England](images/about/england.jpg)
![A quiet morning in Copenhagen](images/about/travel.jpg)
![Spaceship Earth at Epcot](images/about/epcot.jpg)
<!-- /photo-grid -->
