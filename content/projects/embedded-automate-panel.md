---
# Field prefixes say where each field appears:
#   (no prefix) = both the home page card and the case study page
#   card_       = home page project card only
#   page_       = case study page only
#   filter_     = not displayed; used for filtering

title: "Bringing automation to HubSpot Starter"
slug: embedded-automate-panel
order: 1
featured: true
focus: ["0→1", "Activation", "Adoption", "Platform"]

card_thumbnail: images/embedded-automate-panel/card.jpg
card_context: "HubSpot · B2B CRM · 2026"
card_summary: "Led design and co-led strategy for HubSpot's Automate panel. 7 in 10 workflows customers built were new to Starter, and AI-recommended ones went live at 2× the rate."

page_subtitle: "One consistent Automate panel where customers already work, starting from AI recommendations instead of a blank page."
page_problem: "Starter customers, mostly small teams without time to learn new tools, had no central place to automate. Their automation was scattered across five different patterns and hard to find, and customers who couldn't get what they needed were leaving for other tools."
page_hero_media: images/embedded-automate-panel/hero.mp4   # not recorded yet; use page_hero_fallback
page_hero_fallback: images/embedded-automate-panel/hero.jpg
page_metrics:
  - value: "3×"
    label: "automation discovery from putting Automate on the deal records page instead of in settings (A/B test)"
  - value: "45%"
    label: "of AI-recommended workflows went live, twice the rate of starting from a blank page"
  - value: "72%"
    label: "of panel workflows used automation Starter customers never had before"
page_role_summary: "Lead product designer · Co-led vision with PM · Feb – Oct 2026"
page_timeline: "Feb – Oct 2026 (beta July 23, launched to all Starter customers July 28–30, iterated through October)"
page_shipped_to: "HubSpot Starter"
page_chapters:
  - { id: context,  label: "Context",      headline: "Starter customers are small teams with little time to learn new tools" }
  - { id: problem,  label: "Problem",      headline: "Automation for Starter customers was scattered and hard to find" }
  - { id: strategy, label: "Strategy",     headline: "We moved automation onto the pages people already use" }
  - { id: research, label: "Concept validation", headline: "Customers backed the direction and showed us what was missing" }
  - { id: decision, label: "Design direction", headline: "Stakeholders and my team disagreed on the builder, so we tested both" }
  - { id: solution, label: "Final design",     headline: "Each part of the panel addresses something we saw in research" }
  - { id: impact,   label: "Impact",       headline: "Most workflows built in the panel used features Starter didn't have before" }

filter_skills: ["Strategy", "Research", "AI and LLM design", "Interaction design", "Prototyping", "Cross-team leadership"]
---

<!--
  OPEN ITEMS before publishing
  - [ ] Redraw the 'audit' and 'they're all workflows' diagrams; brainstorm text is too small to read on the web
  - [ ] Record the hero clip (or use a still) with customer data blurred
  - [ ] Gather and blur the images listed below (coworker names in dropdowns, real portal names)
  - [ ] Voice pass: rewrite anything that doesn't sound like you
-->

<!-- ============ CASE STUDY PAGE LAYOUT ============
  1. Top of page: title + focus + all page_ fields except page_chapters
  1b. "My role" (unnumbered) comes right after the top section, before 01 Context
  2. Full-story chapters (the body below). Each chapter: "## NN · Label {#id}" then "### Headline".
     Labels/headlines must match page_chapters.
  3. Reflection (unnumbered, last)
  Pull quotes: a blockquote (">") is a pull quote for people scanning the page. It repeats a customer
  quote that already appears in the text; it never replaces it. Last line of the blockquote = attribution.
  Max one per chapter (Design direction uses a pair to show the split).
  Nothing below this line appears on the home page card.
=================================================== -->

## My role {#role}

I led design for the Automate panel from February to October 2026 and co-led the vision with my PM. I worked with six front-end and back-end engineers, and with partner product teams who reviewed the design and placement of the panel on their pages.

I owned the interaction and visual design, from the first concepts in Lovable to the final specs in Figma. I ran the research, including the concept test with 12 customers and the usability test comparing the two builder designs. I also wrote the framework for how AI recommendations explain themselves, and built the rulebook and agent skill that write each automation's sentence.

The panel went to beta on July 23 and launched to all Starter customers by July 30. I kept improving it through October.

## 01 · Context {#context}
### Starter customers are small teams with little time to learn new tools

HubSpot Starter is the entry-level paid plan, used by more than 150,000 customers, mostly founders and early hires at companies with 1 to 25 people. They’re wearing a lot of hats, and their attention is on finding customers and growing the business. Learning a tool like HubSpot, and automation in particular, feels like a big investment of time they don’t have. What they need is simple: leads that don’t fall through the cracks, deals that get followed up on, and tasks that get created without doing it manually.

## 02 · Problem {#problem}
### Automation for Starter customers was scattered and hard to find

Starter customers didn't have access to a central Workflows app. Instead, their automation experience was scattered across five different patterns. Each one had its own UI, its own entry point, and its own permissions. Some lived in settings, some lived inside individual apps, and some weren't visible anywhere. One customer described finding the automations tied to their records as "a little bit of an Easter egg hunt."

> "A little bit of an Easter egg hunt."
>
> Customer, describing how they found existing automations

Automating a simple task meant leaving your work to find the right screen, figuring out how that screen worked, and then coming back later to check what was running. Even our own teams had trouble keeping track of where automations lived. Adoption stayed low, and Starter customers who couldn't get what they needed were leaving to find other tools.

![Our audit of every automation surface in HubSpot, from pipeline settings to rulesets to sequences](images/embedded-automate-panel/audit.jpg)
<!-- IMAGE: brainstorm "Current world of disparate automation solutions" (unnamed-1), redrawn or used as texture with this caption -->

## 03 · Strategy {#strategy}
### We moved automation onto the pages people already use

My PM and I started with a brainstorm to define the goal for the project and how we might reach it. Our goal was to give Starter customers automation that was easy to find and easy to start, so they could stop doing repetitive work manually and wouldn't need to leave HubSpot for other tools.

The idea that shaped how we'd get there was that they're all workflows. Every embedded automation, wherever it showed up, could be backed by a real workflow. That meant someone could start with something simple on a deal page and later open the same automation in the full Workflows app without rebuilding it.

From there I proposed a single Automate experience that would look and work the same on every page where people already do their work. AI-generated recommendations, based on how each customer used their account, would show them where to start.

![The foundational approach: source apps and templates on top, all backed by workflows](images/embedded-automate-panel/all-workflows.jpg)
<!-- IMAGE: brainstorm "New foundational approach: They are all workflows" (unnamed-2), redrawn in the site's diagram style -->

![The 2026 vision: embedded experience, unified canvas, unified management, and agents](images/embedded-automate-panel/vision-venn.jpg)
<!-- IMAGE: brainstorm vision diagram (unnamed.png) -->

## 04 · Concept validation {#research}
### Customers backed the direction and showed us what was missing

We tested the idea in two steps before building the panel. First, we moved the Automate button from settings onto the deal records page and ran an A/B test. Discovery went up 3x and activation went up 2x, and the result was statistically significant.

We then tested our first node and card design concept for the Automate panel with 12 customers, to check whether the new builder was easy to understand and use. Having automation right on the page made sense to them, and pre-filling the trigger from the record they were viewing made the biggest difference. One person said, "It's remembered all the context I've gone through. I haven't got to reselect or hunt for it."

> "It's remembered all the context I've gone through. I haven't got to reselect or hunt for it."
>
> Customer, concept test

One finding changed our plans: recommendations felt like ads unless they fit what the person was doing and explained why they mattered. That led to the recommendation framework in the final design.

## 05 · Design direction {#decision}
### Stakeholders and my team disagreed on the builder, so we tested both

Partner teams and leadership thought the builder looked too technical, and that writing each automation as a plain sentence ("When a deal moves to Closed Won, create a task for the deal owner") would make it easier. My team didn't think rewording triggers and conditions would make them easier to understand. We wanted to build on the node-and-card pattern people already knew from the Workflows app, so it would be easier to learn and customers who upgraded to Pro would find the full app familiar. Our first brainstorm also listed the downsides of sentences: lots of custom UI to build, and they might not translate well.

![Early pros and cons: sentence-style builder vs. AI-first creation](images/embedded-automate-panel/pros-cons.jpg)
<!-- IMAGE: brainstorm pros/cons board (unnamed-11) -->

We took the stakeholders' feedback and built two Lovable prototypes to test both concepts with customers and see whether one was actually easier to use. The results were split. People who liked the sentence version said it felt "less like programming and more like just editing a Word doc." People who liked the node and canvas version said, "Makes me feel like I am building a workflow. Nodes are familiar."

> "Less like programming and more like just editing a Word doc."
>
> Customer who preferred the sentence version

> "Makes me feel like I am building a workflow. Nodes are familiar."
>
> Customer who preferred the node and canvas version

The test also showed something I didn't expect: the builder's design changed how people used AI. In the sentence version, people typed their changes to the AI. In the node and canvas version, they edited the cards directly.

![The sentence version and the node and canvas version, side by side as tested](images/embedded-automate-panel/research-styles.jpg)
<!-- IMAGE: the two tested directions side by side -->

With customers split, we went with the sentence version the stakeholders favored, and I led its visual design from there.

My biggest concern had been scale, since every action needs its own sentence. So I built a rulebook and an agent skill that read an action's definition (its field labels, input order, and dependencies) and write its sentence automatically, for every existing and future action. The definition decides the structure, and the skill only handles the grammar.

Translation was the tradeoff we accepted. Each sentence follows the order of the fields in the form, so translators can change the words but can't reorder them. In languages with a different word order, some sentences read less naturally.

## 06 · Final design {#solution}
### Each part of the panel addresses something we saw in research

- Automation used to be buried in settings, so the Automate button now sits on the CRM pages people already use.
- People used to start from an empty builder, so the panel now opens with recommendations for the record they're viewing.
- Setting up a trigger from scratch confused people, so the panel fills in the trigger based on where it was opened.
- Fields used to be hidden inside forms, so each automation now reads as a sentence with the editable parts highlighted.

![Final panel: recommendations, a sentence being edited inline, and the trigger pre-filled from context](images/embedded-automate-panel/final-panel.jpg)
<!-- IMAGE: 3 final states, each captioned with the pain it fixes -->

Because recommendations felt like ads in research, I wrote a framework for how they explain themselves. Each one says what it will do for the business and never why HubSpot picked it. If an account has enough activity, the recommendation can point to real evidence, like "28x this week deal owners were manually assigned." Newer accounts get suggestions that teach good habits instead.

My PM and I also mapped out what Starter and Pro customers could each edit and add, so the same panel could work for both.

![Starter vs. Pro: what each tier can edit, add, and use](images/embedded-automate-panel/tier-map.jpg)
<!-- IMAGE: brainstorm Starter/Pro allow-restrict map (unnamed-5) -->

![Design reviews from February vision to June visual styles](images/embedded-automate-panel/iterations.jpg)
<!-- IMAGE: 3–4 iterations from the dated review rounds, captioned with what each tested and what changed -->

## 07 · Impact {#impact}
### Most workflows built in the panel used features Starter didn't have before

Starter customers had been leaving because HubSpot couldn't automate the work they needed. After launch, 72% of the workflows built in the panel used features that weren't available on Starter before.

- 44K Starter accounts clicked Automate in the first 11 weeks, which is more than 1 in 4 Starter customers.
- About 2,000 accounts started 3,663 workflows in the panel.
- About 1 in 3 of those workflows went live.

Workflows that started from an AI recommendation went live 45% of the time, compared with only 23% of workflows built from scratch.

We built the panel so other teams could reuse it, and Agent Hub Starter did. It launched on September 21 with the panel as its builder, and gave Starter customers one place to create and manage all their workflows for the first time. Weekly workflows turned on went from about 100 to about 340 in the weeks after.

## Reflection {#reflection}
### What I'd do differently

We looked at much more than ease of use. Our brainstorm weighed build time, scalability, and translation. But we didn't make that case strongly enough. If I'd laid out the pros, cons, and tradeoffs of each direction clearly for stakeholders, the conversation would have been about those tradeoffs.

I'd also test more ideas, and test them sooner. Putting several directions in front of customers early would have given everyone the same evidence to work from.

Once we committed to the sentence version, my job was to make it work. The scaling problem I'd worried about is what led me to build the rulebook and skill.

