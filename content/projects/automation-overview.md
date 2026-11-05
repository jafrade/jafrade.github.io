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
focus: ["Growth", "Onboarding", "Systems thinking", "Craft"]

card_thumbnail: images/automation-overview/card.jpg
card_context: "HubSpot · Workflow automation · 2025"
card_summary: "Led design and co-led the vision for HubSpot's Automation Overview. Monthly visits nearly tripled in a year, to about 150,000, and the page passed 2 million views."

page_overview: "Automation had grown into so many tools that many customers didn't know where to start. The more customers automated, the more of their business HubSpot kept. We built one home for automation, where AI-assisted workflows and personalized recommendations help customers get started and see what needs attention."
page_hero_media: images/automation-overview/hero.jpg
page_hero_fallback: images/automation-overview/hero.jpg
page_metrics:
  - value: "60%"
    label: "of Starter customers had turned on a workflow, up from 40%"
  - value: "2M+"
    label: "Overview page views from the May 2025 launch to October 2026"
  - value: "26%"
    label: "of people who described an automation in the AI prompt turned on the workflow it drafted"
page_role_summary: "Lead product designer · Co-led vision with PM"
page_timeline: "Aug 2024 – Jan 2026 (private beta March 2025, Pro and Enterprise launch May 2025, Starter launch January 2026)"
page_shipped_to: "HubSpot Pro and Enterprise, then Starter"
page_chapters:
  - { id: context,  label: "Context",            headline: "Customers who automated more jobs stayed with HubSpot, but few got there quickly" }
  - { id: problem,  label: "Problem",            headline: "Customers didn't know which tool to use or where to start" }
  - { id: strategy, label: "Strategy",           headline: "We set out to build one home for automation where everything leads to an action" }
  - { id: research, label: "Concept validation", headline: "Customers wanted to fix what they had before building something new" }
  - { id: decision, label: "Design direction",   headline: "Customers preferred a workspace, but the A/B test and the UX framework pointed to an overview" }
  - { id: solution, label: "Final design",       headline: "Each part of the page answers something we heard from customers" }
  - { id: impact,   label: "Impact",             headline: "More customers found the Overview, and it helped them get automation running" }

filter_skills: ["Strategy", "Research", "Interaction design", "Visual design", "Prototyping"]
---
<!--
  NOTES FOR THE SITE BUILD
  - Top of page layout: context line, title, page_overview (in the spot the old subtitle used), focus tags, hero, then a full-width Results row with the three page_metrics side by side (number above label), then My role, Timeline and Shipped to below. page_subtitle and page_problem are retired; remove the subtitle and the "The problem" block.
  - Carousels: images between the 'carousel' and '/carousel' comment markers are one carousel, in order; each alt text is that slide's caption
  - Single images outside a carousel use their alt text as the caption
  - Metric sources: Starter create and turn-on rates (60% to 75%, 40% to 60%, January to August) come from the Enablement project report and a Hex dashboard
-->

## My role {#role}

I led design for the Automation Overview and co-led defining the vision with my PM. I worked with front-end and back-end engineers to build and ship it.

I owned the experience end to end, from early concepts and prototypes to final designs, across the Pro and Enterprise page, its redesign, the first-run experience for new accounts, and the Starter version. I also planned and ran the research that shaped each version, and tracked how the page performed after launch so we could decide what to change next.

I started on the project in August 2024. The Overview went to a private beta in March 2025 and launched to all Pro and Enterprise customers in May 2025. My work ended with the Starter version, which reached every Starter account in January 2026.

## 01 · Context {#context}
### Customers who automated more jobs stayed with HubSpot, but few got there quickly

HubSpot's automation had grown from workflows into a whole set of tools, from sequences and chatbots to rules tucked into pipeline settings. HubSpot measured how many different jobs each customer automated, like updating a deal stage or emailing a new lead. Customers who automated ten or more jobs were more likely to stay, and HubSpot kept more of their revenue. But only about 1 in 3 customers using automation had reached ten jobs, and it took about five months to get there.

That gave us our question: how might we help more customers reach ten automated jobs, and get there sooner?

## 02 · Problem {#problem}
### Customers didn't know which tool to use or where to start

Each new tool was meant to save customers time, but together they made automation harder to use. Customers had so many options that they didn't know which tool fit which job, like choosing between a sequence and a workflow. Many ended up automating very little, or nothing at all.

![Fourteen places to create automation, spread across separate apps, marketing tools and settings](images/automation-overview/problem-map.jpg)

Customers said they "spend a lot of time going from tool to tool, or don't know you even offer solutions to my problems." Others couldn't tell whether their automation was working, and some avoided it altogether.

> "People were put off actually doing anything, because it was just too scary to go in there and sort it out yourself."
>
> Customer, automation research

That held customers back. They weren't saving the time HubSpot could save them, so they got less return on what they paid.

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

Beta customers were getting value from the first concept, but they found it hard to navigate, and advanced customers saw little in it for them. Interviews could only tell us so much, so we launched the first concept to all Pro and Enterprise customers in May 2025, and built the workspace version to A/B test against it.

![The launched first concept and the workspace version we A/B tested](images/automation-overview/ab-test.jpg)

At the same time, HubSpot's UX group was defining a framework for what each kind of page should be. A global home is a jumping-off point, and a workspace is where people spend most of their day doing work. An overview sits in between, as a signpost for one area of the product. Our workspace version stretched past that definition.

![Where the Automation Overview fits between a global home and a workspace](images/automation-overview/fit-diagram.jpg)
<!-- IMAGE: redrawn from the PRD appendix and the "Overview v Workspace" deck -->

The framework hadn't been tested with customers, so we wanted our own data before following it. We ran the A/B test for two weeks that summer, and the results were nearly identical across activation, interaction and retention, so the team kept the overview model.

The test still taught us something. In the launched page, the AI prompt came first and got the most use. In the workspace version, issues came first and usage shifted to issues. Whatever we put at the top got used.

After launch, we turned our attention to new accounts. Nearly half of new customers weren't getting any value from automation in their first month, and for an account with no automations, the Overview was mostly empty charts. I ran another round of research to find which zero state would get people started fastest: unmoderated click tests of three versions, with about seven people each. In every version, the AI prompt was the most common place to start. After the click tests, we combined the best of each version into one design and released it to customers.

<!-- carousel -->
![Version 1, hero with widgets: encouraged exploring, with a first click in about 12 seconds](images/automation-overview/zero-state-v1.jpg)
![Version 2, hero with widgets below: 7 in 10 chose the AI prompt to set up their first automation](images/automation-overview/zero-state-v2.jpg)
![Version 3, onboarding guide: the fastest first click, in under 7 seconds](images/automation-overview/zero-state-v3.jpg)
<!-- /carousel -->

## 06 · Final design {#solution}
### Each part of the page answers something we heard from customers

<!-- carousel -->
![The redesign, organized around four jobs: orient, discover, monitor and learn](images/automation-overview/final-1-four-jobs.jpg)
![The top of the page: the AI prompt, issues to review and recent workflows, then recommended automations and a condensed performance row](images/automation-overview/final-2-orient-discover-monitor.jpg)
![Suggested prompts open under the AI prompt, so people can start from an example instead of a blank box](images/automation-overview/final-3-suggestions.jpg)
![Further down: apps to automate and short HubSpot Academy videos](images/automation-overview/final-4-apps-learn.jpg)
<!-- /carousel -->

With the overview model settled, we focused on two things: getting people to the page, and making it clear what each part was for.

The Overview originally lived on its own page, which meant fewer people visited it. So we moved it into a tab alongside Workflows to make it easier to find and understand. We then organized the page around four jobs: orient, discover, monitor and learn.

Customers can describe what they want to automate and get a drafted workflow to review, or start from a suggestion based on their account's activity. They can see which automations need attention, pick up where they left off, and turn on recommended automations that explain why they fit the account. Reporting stays short and links to the automations behind each number, so the page stays focused on what to do next. People who want to go further can find apps to connect and short Academy videos.

Accounts with no automations get a guided start instead, built around the AI prompt, since it was the most common place to start in every version we tested.

![The zero state for new accounts: an intro video, the AI prompt and popular automations](images/automation-overview/final-5-zero-state.jpg)

In November 2025, as part of a company-wide push to improve product quality, we brought the Overview to Starter. Automation came up in about a third of Starter churn calls, often about features Starter already had. So I built the Starter version around the automation those customers already have, instead of the Workflows tool they don't, and kept reporting to a simple count, since they can't drill into reports. It launched to every Starter account in January 2026 without testing first, and we learned from live usage.

![The Starter Overview: automations available on Starter, Academy lessons, and a count of active automations](images/automation-overview/final-6-starter.jpg)

## 07 · Impact {#impact}
### More customers found the Overview, and it helped them get automation running

Our goal was to help more customers reach ten automated jobs, because those customers stay with HubSpot. New accounts that used the Overview turned on automations twice as often in their first month as older accounts, and the AI prompt gave customers a reliable way to get a workflow running.

- Monthly visits to the Overview nearly tripled in a year, to about 150,000, and the page passed 2 million views.
- About 1 in 4 people who described an automation in the AI prompt turned on the workflow it drafted.
- Nearly 1 in 3 visitors came back within a week.

On Starter, about 1 in 3 visitors interact with the page, more than on Pro. The Starter Overview was the first of several launches aimed at getting more Starter customers to create and turn on workflows. From January to August, the share of Starter customers who created a workflow rose from 60% to 75%, beating our goal, and the share who turned one on rose from 40% to 60%.

Several launches landed close together, so we couldn't isolate the Overview's effect on the number of jobs customers automated, or on retention. We believe it helped customers automate more jobs than before, or get there faster.

## Reflection {#reflection}
### What I'd do differently

A page like the Overview gets every kind of visitor, and the risk was always that it would try to serve all of them and end up as a catch-all with no clear starting point. New accounts were looking for something to turn on, while established accounts cared more about how their existing automations were running.

We did a lot of concept testing early on, but I'd have kept gathering feedback after launch to see how people used the page over time.

Recommendations were the hardest part. Our goal was to get customers automating more jobs, but the system behind them couldn't vary or personalize recommendations enough to get there. This was before we could use LLMs in our infrastructure to generate personalized recommendations.
