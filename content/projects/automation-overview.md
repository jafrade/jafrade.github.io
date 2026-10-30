---
# Field prefixes say where each field appears:
#   (no prefix) = both the home page card and the case study page
#   card_       = home page project card only
#   page_       = case study page only
#   filter_     = not displayed; used for filtering

title: "Building HubSpot's first home page for automation"
slug: automation-overview
order: 2
featured: true
focus: ["Adoption", "0→1", "Onboarding", "Activation"]

card_thumbnail: images/automation-overview/card.jpg
card_context: "HubSpot · B2B CRM · 2025"
card_summary: "Led design and co-led the vision for HubSpot's Automation Overview. Monthly visits grew from about 52,000 to 150,000 in a year, passing 2 million total views since launch."

page_subtitle: "The first thing customers see when they open automation, with suggestions for what to automate next and a quick view of how their automation is running."
page_problem: "Automation was spread across 14 places with nothing tying them together, so customers didn't know where to start or whether what they'd built was working."
page_hero_media: images/automation-overview/hero.jpg
page_hero_fallback: images/automation-overview/hero.jpg
page_metrics:
  - value: "2M+"
    label: "Overview page views from the May 2025 launch to October 2026"
  - value: "26%"
    label: "of people who described an automation in the AI prompt turned on the workflow it drafted"
  - value: "31.7%"
    label: "of visitors came back to the Overview within 7 days"
page_role_summary: "Lead product designer · Co-led vision with PM"
page_timeline: "Aug 2024 – Jan 2026 (private beta March 2025, Pro and Enterprise launch May 2025, Starter launch January 2026)"
page_shipped_to: "HubSpot Pro and Enterprise, then Starter"
page_chapters:
  - { id: context,  label: "Context",            headline: "Customers had more automation tools than they knew how to use" }
  - { id: problem,  label: "Problem",            headline: "Customers didn't know which tool to use or where to start" }
  - { id: strategy, label: "Strategy",           headline: "We set out to build one home for automation where everything leads to an action" }
  - { id: research, label: "Concept validation", headline: "Customers wanted to fix what they had before building something new" }
  - { id: decision, label: "Design direction",   headline: "Customers preferred a workspace, but the A/B test and the UX framework pointed to an overview" }
  - { id: solution, label: "Final design",       headline: "Each part of the page answers something we heard from customers" }
  - { id: impact,   label: "Impact",             headline: "More customers found the Overview, and it helped them get automation running" }

filter_skills: ["Strategy", "Research", "Interaction design", "Visual design", "Prototyping"]
---

<!--
  CAROUSELS: images between the 'carousel' and '/carousel' comment markers render as one carousel, in order. Each image's alt text is that slide's caption.

  OPEN ITEMS before publishing
  - [ ] "2x" new portal metric: kept at Jason's request, in the body only, worded as the Enablement PDF states it. The dashboard's closest comparison shows ~1.5x, and the comparison group is unclear. Be ready to explain it, or drop it.
  - [ ] Zero state: which of the two A/B tested versions shipped? zero-state.jpg is a frame from the redesign M2 Figma page; confirm it matches what shipped.
  - [ ] Starter figure (1 in 3 visitors interact) comes from the Enablement PDF, not the dashboard.
  - [ ] Images show "Welcome, Jason" and your name in "Pick up where you left off" (your own name, fine), plus HubSpot Academy instructors in video thumbnails (public content). Portal names in top bars are blurred.
  - [ ] Voice pass: rewrite anything that doesn't sound like you.
-->

## My role {#role}

I led design for the Automation Overview and co-led defining the vision with my PM. I worked with front-end and back-end engineers to build and ship it.

I owned the experience end to end, from early concepts and prototypes to final designs, across the Pro and Enterprise page, its redesign, the first-run experience for new accounts, and the Starter version. I also planned and ran the research that shaped each version, and tracked how the page performed after launch so we could decide what to change next.

I started on the project in August 2024. The Overview went to a private beta in March 2025 and launched to all Pro and Enterprise customers in May 2025. My work ended with the Starter version, which reached every Starter account in January 2026.

## 01 · Context {#context}
### Customers had more automation tools than they knew how to use

HubSpot's automation had grown from workflows into a whole set of tools, from sequences and chatbots to simple workflows inside forms and rules tucked into pipeline settings. HubSpot measured success by how many different jobs a customer automates, like updating a deal stage or emailing a new lead.

Only 31% of customers using automation had automated ten or more jobs. More than half had automated six or fewer, and it took about five months to reach ten. These were Pro and Enterprise customers, with access to the most automation tools, and only a fraction of them were getting the most value. We set out to understand why and what we could do about it.

## 02 · Problem {#problem}
### Customers didn't know which tool to use or where to start

Each new tool was meant to save customers time, but together they made automation harder to use. Customers had so many options that they didn't know which tool fit which job, like choosing between a sequence and a workflow. Many ended up automating very little, or nothing at all.

![Fourteen places to create automation, spread across separate apps, marketing tools and settings](images/automation-overview/problem-map.jpg)

Customers said they "spend a lot of time going from tool to tool, or don't know you even offer solutions to my problems." Others couldn't tell whether their automation was working, and some avoided it altogether.

> "People were put off actually doing anything, because it was just too scary to go in there and sort it out yourself."
>
> Customer, automation research

That held customers back. They weren't saving the time HubSpot could save them, so they got less return on what they paid. And our data showed that the more jobs a company automated, the more of its revenue HubSpot kept over time.

## 03 · Strategy {#strategy}
### We set out to build one home for automation where everything leads to an action

My PM and I wrote the brief in August 2024 and ran a brainstorm with our engineers. Our goal was one home for automation, where customers could find tools and use cases they didn't know about and get started with little effort.

<!-- carousel -->
![Our brainstorm: problems, ideas, then a prioritization matrix](images/automation-overview/brainstorm-1-board.jpg)
![Ideas grouped by theme, from learning and easy starts to AI recommendations and templates](images/automation-overview/brainstorm-3-ideas.jpg)
![The insights ideas, where we agreed everything on the page should be actionable](images/automation-overview/brainstorm-4-insights.jpg)
![We plotted every idea by effort and priority to pick what went into the first version](images/automation-overview/brainstorm-5-matrix.jpg)
<!-- /carousel -->
<!-- IMAGE: FigJam brainstorm; coworker names and avatars blurred on close-ups, a coworker's sticky removed from the problems slide -->

We set one firm rule. HubSpot had tried a similar home page before, and it failed because it became another reporting dashboard. So every part of the Overview had to lead to an action. A recommendation opens a ready-made automation, and the AI prompt drafts a workflow for the customer to review. To decide what to recommend, we mapped which jobs customers automate at each stage. Recommendations could then suggest the next jobs for each stage, without overwhelming people who were just starting.

![The jobs customers automate at each stage, and what we'd recommend next](images/automation-overview/jobs-by-stage.jpg)

## 04 · Concept validation {#research}
### Customers wanted to fix what they had before building something new

Our first concept was one long page with everything from our brainstorm: an AI prompt, recommended automations, marketing assets and apps to automate, ways to improve existing automations, issues to review, and reporting. I walked four customers through it to hear their first impressions.

I also asked what they'd expect from a page called Overview compared to one called Workspace. HubSpot already had a few pages that felt similar, but no shared framework defined what each kind of page should be, so the name mattered. Customers expected an overview to coach them and a workspace to be where they'd build.

The page itself had problems. People had to scroll too far, and anything below the first few sections risked being ignored. What they valued most was seeing issues and ways to improve the automations they already had, so the next version needed to bring those up the page.

> "Everything under here is going to be ignored."
>
> Customer, concept test 1

<!-- carousel -->
![The top of the first concept: the AI prompt and recommended automations](images/automation-overview/concept-1.jpg)
![Further down: ways to improve existing automations and issues to review](images/automation-overview/concept-2.jpg)
![A count of every automation by source](images/automation-overview/concept-3.jpg)
![Reporting at the very bottom of a long scroll](images/automation-overview/concept-4.jpg)
<!-- /carousel -->

## 05 · Design direction {#decision}
### Customers preferred a workspace, but the A/B test and the UX framework pointed to an overview

So I designed a second concept in a compact, workspace style, with issues, a performance scorecard and recommendations at the top. I tested it against the first concept with 10 customers at every experience level, and they preferred the compact version. They called it "intuitive" and "a place to come back to." The first concept felt "cluttered" and "heavy."

> "This is much more useful to me than what I currently see."
>
> Customer, concept test 2

Beta customers were getting value from the first concept, but they found it hard to navigate, and advanced customers saw little in it for them. Interviews could only tell us so much, so we launched the first concept to all Pro and Enterprise customers on May 12, 2025, and built the workspace version to A/B test against it.

![The launched first concept and the workspace version we A/B tested](images/automation-overview/ab-test.jpg)

At the same time, HubSpot's UX group was defining a framework for what each kind of page should be. A global home is a jumping-off point, and a workspace is where people spend most of their day doing work. An overview sits in between, as a signpost for one area of the product. Our workspace version stretched past that definition.

![Where the Automation Overview fits between a global home and a workspace](images/automation-overview/fit-diagram.jpg)
<!-- IMAGE: redrawn from the PRD appendix and the "Overview v Workspace" deck -->

The framework hadn't been tested with customers, so we wanted our own data before following it. From June 30 to July 14, 2025, we ran the A/B test. The results were nearly identical across activation, interaction and retention, so the team kept the overview model.

The test still taught us something. In the launched page, the AI prompt came first and got the most use. In the workspace version, issues came first and usage shifted to issues. Whatever we put at the top got used.

After launch, we turned our attention to new accounts. Nearly half of new customers weren't getting any value from automation in their first month, and for an account with no automations, the Overview was mostly empty charts. I ran another round of research to find which zero state would get people started fastest: unmoderated click tests of three versions, with about seven people each. In every version, the AI prompt was the most common place to start. After the click tests, we combined the best of each version into one design and released it to customers.

<!-- carousel -->
![Version 1, hero with widgets: encouraged exploring, with a first click in 11.6 seconds](images/automation-overview/zero-state-v1.jpg)
![Version 2, hero with widgets below: 71% chose the AI prompt to set up their first automation](images/automation-overview/zero-state-v2.jpg)
![Version 3, onboarding guide: the fastest first click, at 6.6 seconds](images/automation-overview/zero-state-v3.jpg)
<!-- /carousel -->

## 06 · Final design {#solution}
### Each part of the page answers something we heard from customers

With the overview model settled, we focused on two things: getting people to the page, and making it clear what each part was for.

Most people went straight to the Workflows list and never saw the Overview, which lived on its own page. So in September 2025 we combined them into one Automation app with the Overview as the first tab. A month later, the redesign organized the page around four jobs:

- Orient: customers didn't know where to start or what needed attention, so the top of the page holds the AI prompt, with suggested prompts based on the account's activity, plus issues to review and "Pick up where you left off."
- Discover: recommendations felt random, so each card says why it's there, like "700 form submissions on this form aren't automated."
- Monitor: the reporting read like a dashboard to look at and leave, so it's condensed into one row, and each count links to the automations behind it.
- Learn: short HubSpot Academy videos sit at the bottom for people who want to go further.

New accounts with no automations get a guided start instead: a short intro video, the AI prompt next to two of the most popular automations, and charts with sample data so they can see what to expect.

The last step was bringing the page to Starter. In November 2025, as part of a company-wide push to improve product quality, we brought the Overview to Starter. Automation came up in about a third of Starter churn calls, often about features Starter already had.

I reframed the page around the automation Starter customers already have, like simple workflows in forms and emails and pipeline automation, instead of the Workflows tool they don't. Charts became a simple count of the customer's automations by type, because Starter customers can't drill into reporting. We launched it in January 2026 without testing first, and learned from live usage.

<!-- carousel -->
![The redesign, organized around four jobs: orient, discover, monitor and learn](images/automation-overview/final-1-four-jobs.jpg)
![The top of the page: the AI prompt, issues to review and recent workflows, then recommended automations and a condensed performance row](images/automation-overview/final-2-orient-discover-monitor.jpg)
![Suggested prompts open under the AI prompt, so people can start from an example instead of a blank box](images/automation-overview/final-3-suggestions.jpg)
![Further down: apps to automate and short HubSpot Academy videos](images/automation-overview/final-4-apps-learn.jpg)
![The zero state for new accounts: an intro video, the AI prompt and popular automations](images/automation-overview/final-5-zero-state.jpg)
![The Starter Overview: automations available on Starter, Academy lessons, and a count of active automations](images/automation-overview/final-6-starter.jpg)
<!-- /carousel -->

## 07 · Impact {#impact}
### More customers found the Overview, and it helped them get automation running

Customers had been automating very little because they didn't know where to start. After launch, monthly visits to the Overview grew from about 52,000 to 150,000 a year later.

- The page passed 2 million views by October 2026.
- 31.7% of visitors came back within 7 days.
- 26% of the 22,021 people who described an automation in the AI prompt turned on the workflow it drafted.

On Starter, about 1 in 3 visitors interact with the page, more than on Pro.

Our main goal was to help customers automate more jobs. Several launches landed close together, so we couldn't isolate the Overview's effect on that number, but we did see clear signs in the steps leading up to it. New accounts that used the Overview turned on automations twice as often in their first month as older accounts, and the AI prompt gave customers a reliable way to get a workflow running. We believe this helped customers automate more jobs than before, or get there faster.

## Reflection {#reflection}
### What I'd do differently

A page like the Overview gets every kind of visitor, and the risk was always that it would try to serve all of them and end up as a catch-all with no clear starting point. New accounts were looking for something to turn on, while established accounts cared more about how their existing automations were running.

We did a lot of concept testing early on, but I'd have kept gathering feedback after launch to see how people used the page over time.

Recommendations were the hardest part. Our goal was to get customers automating more jobs, but the system behind them couldn't vary or personalize recommendations enough to get there. This was before we could use LLMs in our infrastructure to generate personalized recommendations.
